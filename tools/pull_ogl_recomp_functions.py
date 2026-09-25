#!/usr/bin/env python3
"""Pull hand-ported N64Recomp function references from the sibling OGL port.

The OGL port's `recomp_out/.c` is host-side recompilation output. Its
hand-written bodies are useful evidence for 64CBFD matching work, but they are
not IDO-ready decompilation source. This tool captures those bodies with their
line ranges and maps them back to the 64CBFD owner files.
"""

from __future__ import annotations

import argparse
import bisect
import datetime as dt
import re
from pathlib import Path


HAND_PORT_FUNCTIONS = [
    "func_10001050",
    "func_10001194",
    "func_10001420",
    "func_10003C6C",
    "func_10004074",
    "func_1000480C",
    "func_100049E0",
    "func_10004DB0",
    "func_100052A0",
    "func_10005B04",
    "func_10005BE0",
    "func_100061F8",
    "func_10006240",
    "func_15007830",
    "func_15007B3C",
    "func_15015E80",
    "func_1501C880",
    "func_1501CC3C",
    "func_1502AC88",
    "func_1502B350",
    "func_1502B4A8",
    "func_1502B6BC",
]

RELATED_AUDIT_FUNCTIONS = [
    (
        "func_10004514",
        "already in 64CBFD",
        "Normal PI DMA callee mentioned because OGL hand ports call it; not a hand-edited OGL body.",
    ),
    (
        "func_10004F00",
        "already in 64CBFD",
        "Scheduler task-submission callee used by the OGL display-list path; body did not differ from staging.",
    ),
    (
        "func_100050A0",
        "already in 64CBFD",
        "Scheduler creation callee called by the OGL `func_15007830` port; not a missing hand port.",
    ),
    (
        "func_10006380",
        "already recompiled in OGL",
        "Mentioned as part of the real decompressor chain; notes call it correctly recompiled and non-hand-written.",
    ),
    (
        "func_15002FB4",
        "already in 64CBFD",
        "Real non-hand-ported function that exposed the asset-loader blocker; not a missing OGL edit.",
    ),
    (
        "func_1501A39C",
        "still unported",
        "Overflow-reset path of `func_1501C880`; OGL notes explicitly say it is still a ROM stub.",
    ),
    (
        "func_1501C730",
        "still unported",
        "Only other writer for `D_800BE615`; OGL notes call it a separate zeroed-out ROM stub.",
    ),
    (
        "func_1502AB04",
        "deliberately not ported",
        "Asset-cache insert helper; OGL uses a miss-only `func_1502AC88` simplification and explicitly skipped it.",
    ),
]


def line_index(text: str) -> list[int]:
    starts = [0]
    starts.extend(match.end() for match in re.finditer("\n", text))
    return starts


def line_no(starts: list[int], offset: int) -> int:
    return bisect.bisect_right(starts, offset)


def extract_function(text: str, starts: list[int], name: str) -> dict[str, object]:
    pattern = re.compile(rf"RECOMP_FUNC\s+void\s+{re.escape(name)}\s*\([^)]*\)\s*\{{")
    match = pattern.search(text)
    if match is None:
        return {"name": name, "found": False}

    depth = 0
    pos = match.end() - 1
    end = pos
    while end < len(text):
        char = text[end]
        if char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
            if depth == 0:
                end += 1
                break
        end += 1
    else:
        raise ValueError(f"Unterminated function body for {name}")

    body = text[match.start() : end]
    start_line = line_no(starts, match.start())
    end_line = line_no(starts, end)
    return {
        "name": name,
        "found": True,
        "start_line": start_line,
        "end_line": end_line,
        "line_count": body.count("\n") + 1,
        "body": body.rstrip(),
    }


def extract_all_functions(text: str) -> dict[str, str]:
    funcs: dict[str, str] = {}
    for match in re.finditer(r"RECOMP_FUNC\s+void\s+([A-Za-z_][A-Za-z0-9_]*)\s*\([^)]*\)\s*\{", text):
        name = match.group(1)
        depth = 0
        pos = match.end() - 1
        end = pos
        while end < len(text):
            char = text[end]
            if char == "{":
                depth += 1
            elif char == "}":
                depth -= 1
                if depth == 0:
                    end += 1
                    break
            end += 1
        else:
            raise ValueError(f"Unterminated function body for {name}")
        funcs[name] = text[match.start() : end].rstrip()
    return funcs


def load_layout(repo_root: Path) -> dict[str, dict[str, str]]:
    layout_path = repo_root / "conker" / "retail_layout.us.txt"
    layout: dict[str, dict[str, str]] = {}
    if not layout_path.exists():
        return layout

    for raw_line in layout_path.read_text(encoding="utf-8").splitlines():
        if not raw_line or raw_line.startswith("#"):
            continue
        fields = raw_line.split(",")
        if len(fields) != 5:
            continue
        section, obj_name, func_name, start, end = fields
        layout[func_name] = {
            "section": section,
            "object": obj_name,
            "start": start,
            "end": end,
        }
    return layout


def guess_owner(repo_root: Path, entry: dict[str, str] | None) -> str:
    if entry is None:
        return ""

    obj_name = entry["object"]
    section = entry["section"]
    candidates: list[Path] = []

    if section == "game":
        candidates.extend(
            [
                repo_root / "conker" / "src" / "game" / f"{obj_name}.c",
                repo_root / "conker" / "src" / "game" / f"generated_{obj_name}.c",
                repo_root / "conker" / "src" / f"{obj_name}.c",
                repo_root / "conker" / "asm" / f"{obj_name}.s",
            ]
        )
    else:
        candidates.extend(
            [
                repo_root / "conker" / "src" / f"{obj_name}.c",
                repo_root / "conker" / "asm" / f"{obj_name}.s",
            ]
        )

    for path in candidates:
        if path.exists():
            return path.relative_to(repo_root).as_posix()
    return candidates[0].relative_to(repo_root).as_posix()


def count_declared_functions(funcs_h: Path) -> int:
    if not funcs_h.exists():
        return 0
    text = funcs_h.read_text(encoding="utf-8", errors="replace")
    return len(re.findall(r"^void\s+[A-Za-z_][A-Za-z0-9_]*\s*\(uint8_t\* rdram, recomp_context\* ctx\);", text, re.M))


def write_markdown(
    output: Path,
    ogl_root: Path,
    source_c: Path,
    staging_c: Path,
    declared_count: int,
    functions: list[dict[str, object]],
    changed_count: int,
    changed_names: set[str],
    layout: dict[str, dict[str, str]],
    repo_root: Path,
) -> None:
    rel_output = output.relative_to(repo_root).as_posix()
    stamp = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    lines: list[str] = [
        "# 64CBFDOGL Function Pull",
        "",
        f"Generated by `tools/pull_ogl_recomp_functions.py` on {stamp}.",
        "",
        "Source:",
        f"- OGL root: `{ogl_root}`",
        f"- Recomp body file: `{source_c}`",
        f"- Staging comparison file: `{staging_c}`",
        f"- Recomp declarations found: `{declared_count}`",
        f"- Function bodies changed versus staging: `{changed_count}`",
        "",
        "Important: these are host-side N64Recomp functions, not IDO-ready decomp source. Use them as reference evidence when replacing 64CBFD placeholders or reconstructing matching C.",
        "",
        "Audit note: a function-by-function comparison of `recomp_out/.c` against `recomp_out_new/.c` is used to catch edited bodies even when the working notes are incomplete. Bodies marked `changed` differ from staging; bodies marked `reference` are included because the OGL notes identify them as boot-relevant trivial/stub replacements or downstream runtime references.",
        "",
        "## Pulled Functions",
        "",
        "| Function | OGL lines | Body status | 64CBFD retail span | 64CBFD owner |",
        "| --- | ---: | --- | --- | --- |",
    ]

    for item in functions:
        name = str(item["name"])
        entry = layout.get(name)
        owner = guess_owner(repo_root, entry) if entry else ""
        if item["found"]:
            ogl_lines = f"{item['start_line']}-{item['end_line']} ({item['line_count']} lines)"
        else:
            ogl_lines = "missing"
        body_status = "changed" if name in changed_names else "reference"
        span = f"{entry['start']}-{entry['end']}" if entry else ""
        lines.append(f"| `{name}` | {ogl_lines} | {body_status} | `{span}` | `{owner}` |")

    lines.extend(
        [
            "",
            "## Reference Bodies",
            "",
            f"This section is the actual pulled content. Keep `{rel_output}` out of the compile path.",
        ]
    )

    for item in functions:
        name = str(item["name"])
        lines.extend(["", f"### `{name}`", ""])
        if not item["found"]:
            lines.append("Not found in the OGL recomp output.")
            continue
        lines.append(f"Source lines: `{item['start_line']}-{item['end_line']}`")
        lines.extend(["", "```c", str(item["body"]), "```"])

    lines.extend(
        [
            "",
            "## Related Audit Names",
            "",
            "These names appeared in the broader OGL audit but are not pulled as reference bodies.",
            "",
            "| Function | Audit status | 64CBFD retail span | 64CBFD owner | Reason |",
            "| --- | --- | --- | --- | --- |",
        ]
    )

    for name, status, reason in RELATED_AUDIT_FUNCTIONS:
        entry = layout.get(name)
        span = f"{entry['start']}-{entry['end']}" if entry else ""
        owner = guess_owner(repo_root, entry) if entry else ""
        lines.append(f"| `{name}` | {status} | `{span}` | `{owner}` | {reason} |")

    output.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--ogl-root",
        type=Path,
        default=Path(__file__).resolve().parents[1].parent / "64CBFDOGL",
        help="Path to the sibling 64CBFDOGL checkout.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "DOCS" / "64CBFDOGL_FUNCTION_PULL.md",
        help="Markdown file to write in the 64CBFD repo.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    repo_root = Path(__file__).resolve().parents[1]
    ogl_root = args.ogl_root.resolve()
    output = args.output.resolve()
    source_c = ogl_root / "recomp_out" / ".c"
    funcs_h = ogl_root / "recomp_out" / "funcs.h"
    staging_c = ogl_root / "recomp_out_new" / ".c"

    if not source_c.exists():
        raise FileNotFoundError(f"Missing OGL recomp body file: {source_c}")
    if not staging_c.exists():
        raise FileNotFoundError(f"Missing OGL staging recomp body file: {staging_c}")

    text = source_c.read_text(encoding="utf-8", errors="replace")
    staging_text = staging_c.read_text(encoding="utf-8", errors="replace")
    starts = line_index(text)
    extracted = [extract_function(text, starts, name) for name in HAND_PORT_FUNCTIONS]
    current_funcs = extract_all_functions(text)
    staging_funcs = extract_all_functions(staging_text)
    changed_names = {
        name
        for name, body in current_funcs.items()
        if staging_funcs.get(name) != body
    }
    layout = load_layout(repo_root)
    output.parent.mkdir(parents=True, exist_ok=True)
    write_markdown(
        output,
        ogl_root,
        source_c,
        staging_c,
        count_declared_functions(funcs_h),
        extracted,
        len(changed_names),
        changed_names,
        layout,
        repo_root,
    )

    found = sum(1 for item in extracted if item["found"])
    print(f"Pulled {found}/{len(extracted)} hand-port function references into {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
