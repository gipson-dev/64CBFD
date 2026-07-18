#!/usr/bin/env python3
"""Replace GLOBAL_ASM pragmas with validated non-matching C placeholders."""

import argparse
import re
from pathlib import Path

from generate_placeholder_c import function_layout, placeholder_definition


PRAGMA = re.compile(
    r'^[ \t]*#pragma[ \t]+GLOBAL_ASM\("([^"]+)"\)[ \t]*$',
    re.MULTILINE,
)
MARKER = re.compile(r"/\* Non-matching C placeholders for ([^ ]+\.s)\. \*/")
DECLARATION_BLOCK = re.compile(
    r"\n?/\* Generated placeholder declarations\. \*/\n.*?"
    r"/\* End generated placeholder declarations\. \*/\n?",
    re.DOTALL,
)


def name_parameters(parameters):
    parameters = parameters.strip()
    if not parameters or parameters == "void":
        return parameters
    result = []
    for index, parameter in enumerate(part.strip() for part in parameters.split(",")):
        if parameter == "...":
            result.append(parameter)
            continue
        pointer_name = re.search(r"\*\s*[A-Za-z_]\w*\s*(?:\[[^]]*\])?$", parameter)
        words = re.findall(r"[A-Za-z_]\w*", parameter)
        has_name = bool(pointer_name) or (
            "*" not in parameter
            and len(words) >= 2
            and not (words[0] == "struct" and len(words) == 2)
        )
        if has_name:
            result.append(parameter)
        elif parameter.rstrip().endswith("*"):
            result.append(f"{parameter}arg{index}")
        else:
            result.append(f"{parameter} arg{index}")
    return ", ".join(result)


def declared_signature(name, texts):
    pattern = re.compile(
        rf"^[ \t]*(?:extern[ \t]+)?"
        rf"(?P<return>(?:struct[ \t]+\w+|[A-Za-z_]\w*)(?:[ \t]*\*)?)"
        rf"[ \t]*{re.escape(name)}[ \t]*\((?P<parameters>[^;{{}}]*)\)[ \t]*;",
        re.MULTILINE,
    )
    for text in texts:
        for match in pattern.finditer(text):
            return_type = match.group("return").strip()
            if return_type in {"return", "if", "while", "for", "switch"}:
                continue
            return (
                re.sub(r"\s*\*\s*$", " *", return_type),
                name_parameters(match.group("parameters")),
            )
    return None


def call_argument_counts(name, text):
    counts = []
    for match in re.finditer(rf"\b{re.escape(name)}[ \t]*\(", text):
        start = match.end() - 1
        depth = 0
        end = None
        for index in range(start, len(text)):
            char = text[index]
            if char == "(":
                depth += 1
            elif char == ")":
                depth -= 1
                if depth == 0:
                    end = index
                    break
        if end is None:
            continue
        suffix = text[end + 1:].lstrip()
        if suffix.startswith("{"):
            continue
        arguments = text[start + 1:end].strip()
        if not arguments:
            counts.append(0)
            continue
        depth = 0
        count = 1
        for char in arguments:
            if char == "(":
                depth += 1
            elif char == ")":
                depth -= 1
            elif char == "," and depth == 0:
                count += 1
        counts.append(count)
    return sorted(set(counts))


def load_headers(project_dir):
    return [path.read_text() for path in (project_dir / "include").rglob("*.h")]


def layouts(project_dir, asm_names, source_text, headers):
    result = {}
    search_texts = [DECLARATION_BLOCK.sub("", source_text), *headers]
    for asm_name in asm_names:
        entries = function_layout(project_dir / asm_name)
        for name, size in entries:
            signature = declared_signature(name, search_texts)
            declared = signature is not None
            if signature is None:
                return_type = "void" if size < 12 else "s32"
                counts = call_argument_counts(name, search_texts[0])
                if len(counts) > 1:
                    raise ValueError(f"{name} is called with multiple argument counts: {counts}")
                count = counts[0] if counts else 0
                parameters = ", ".join(f"s32 arg{index}" for index in range(count))
            else:
                return_type, parameters = signature
            result[name] = (size, return_type, parameters, declared)
    return result


def replacement(project_dir, asm_name, typed_layout):
    definitions = []
    for name, size in function_layout(project_dir / asm_name):
        _size, return_type, parameters, _declared = typed_layout[name]
        definitions.extend(placeholder_definition(name, size, return_type, parameters))
    lines = [
        f"/* Non-matching C placeholders for {asm_name}. */",
        *definitions,
    ]
    return "\n".join(lines).rstrip()


def replace_existing_definitions(text, typed_layout):
    for name, (size, return_type, parameters, _declared) in typed_layout.items():
        definition = "\n".join(
            placeholder_definition(name, size, return_type, parameters)
        ).rstrip()
        pattern = re.compile(
            rf"^[A-Za-z_]\w*(?:[ \t]*\*)?[ \t]*{re.escape(name)}\([^)]*\) \{{\n"
            rf"(?:    return [^;]+;\n)?\}}",
            re.MULTILINE,
        )
        text, count = pattern.subn(definition, text, count=1)
        if count != 1:
            raise ValueError(f"could not refresh generated definition for {name}")
    return text


def add_missing_declarations(text, typed_layout):
    text = DECLARATION_BLOCK.sub("", text)
    declarations = [
        f"{return_type} {name}({parameters});"
        for name, (_size, return_type, parameters, declared) in typed_layout.items()
        if not declared
    ]
    if not declarations:
        return text
    includes = list(re.finditer(r"^#include[^\n]*\n", text, re.MULTILINE))
    if not includes:
        raise ValueError("cannot place generated declarations: no #include lines")
    block = (
        "\n/* Generated placeholder declarations. */\n"
        + "\n".join(declarations)
        + "\n/* End generated placeholder declarations. */\n\n"
    )
    offset = includes[-1].end()
    return text[:offset] + block + text[offset:].lstrip("\n")


def convert(path, project_dir, headers, check_only=False):
    path = Path(path)
    text = path.read_text()
    pragmas = list(PRAGMA.finditer(text))
    asm_names = [match.group(1) for match in pragmas]
    if not asm_names:
        asm_names = MARKER.findall(text)
    if not asm_names:
        raise ValueError(f"no generated GLOBAL_ASM placeholders found in {path}")
    typed_layout = layouts(project_dir, asm_names, text, headers)

    if pragmas:
        replacements = []
        for match in pragmas:
            rendered = replacement(project_dir, match.group(1), typed_layout)
            replacements.append((match.span(), rendered))

        for (start, end), rendered in reversed(replacements):
            text = text[:start] + rendered + text[end:]
    else:
        text = replace_existing_definitions(text, typed_layout)
    text = add_missing_declarations(text, typed_layout)

    if not check_only:
        if not text.endswith("\n"):
            text += "\n"
        path.write_text(text, newline="\n")
    return len(asm_names)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("project_dir", help="project root containing asm/ and src/")
    parser.add_argument("sources", nargs="+", help="C sources to convert")
    parser.add_argument(
        "--check",
        action="store_true",
        help="validate every pragma without modifying its source",
    )
    args = parser.parse_args()

    project_dir = Path(args.project_dir)
    headers = load_headers(project_dir)
    total = 0
    for source in args.sources:
        total += convert(source, project_dir, headers, args.check)
    action = "Validated" if args.check else "Processed"
    print(f"{action} {total} GLOBAL_ASM placeholder groups across {len(args.sources)} sources.")


if __name__ == "__main__":
    main()
