# Game Text Measurer UOPT Allocation Trace - 2026-10-12

## Scope And Baseline

Continue func_150428D4, not an easier substitute. Production still contains
the zero-return placeholder: original219 words/876 bytes, frame0x80, ROM
0x6FD84..0x700F0. The fitting seed remains flag-branches-captured222/frame0x80/
146 word differences; its 12-byte overflow and missing retail T0 reset are
not fixed. No source installation, new guards, profile changes or matching credit.

Baseline consumer 3082b41a9bc8e7a635fdefa7fa73615758de177a and mounted tools
faec3b7044986f0c0a0b51ccc36556c20da0e014. Preserve the production fingerprints
and nine-input/data audit from [Note 1299](1299-game-text-measurer-instruction-fault-boundary-and-review-20261012.md).
Game remains 2,813/4,823 byte-exact; total 3,486/5,496. Root README unchanged.

## Diagnostic Failure And Correction

New mode4/mode7 attempts first abort in CFE when verbose output reaches an
unsupported wrapper_fprintf format. Removing only diagnostic verbosity reaches
UOPT, but the debug string printer writes through a null output buffer and
signals11 at native0x422282. An empty uoptlist and debugger exit zero are not
success evidence. These failures do not implicate the function's allocation.

The initial debugger probe misidentifies RSI as a stream descriptor and the
count-only attempt fails. Native f_write_string disassembly and the available
UGEN generated runtime source establish its real signature: RDI is memory,
RSI is simulated SP, EDX is the FILE address. Dereferencing simulated SP even
yields 0x20202020 in one rejected probe. Correct that diagnosis rather than
carrying the descriptor assumption forward.

For the owned UOPT child only, call its existing wrapper___flsbuf at native
0x4074E0 with the actual FILE0x0FB52914 and a leading space. It allocates a
buffer through the existing guest allocator, without modifying prepared
compiler sources/binaries. This reaches another diagnostic-only failure:
wrapper_ecvt is unimplemented and the real-number printer aborts. Suppress
f_write_real at native0x484590 only within that disposable process. Its numeric
output/timings are not valid diagnostic measurements after suppression.

Delete UOPT-address breakpoints before resuming the driver into UGEN/AS1;
otherwise an unrelated child's address map rejects a breakpoint. Require the
actual compiler driver to terminate with code0, not merely the GDB wrapper.
All rejected probes and logs remain ignored under
conker/build/game-text-measurer-uopt-investigation-20261012/.

## Qualified Helper

New mounted tool experiments/game_text_measurer_uopt_trace.py is opt-in and
locked to the prepared cc/uopt fingerprints:

- cc: ca4b4385eb89c5098b665ffe256f59aa1bfd73ccd8f104fcb3eee0314dcd236a
- uopt: 23c108b975e88034af4ccbd89bd054a1ff3ee4ea9de28f25d91d75a7800f527d

It starts a new --nx/--batch GDB process with auto-load disabled before loading
the compiler, follows only that driver's children, and never attaches to the
game/emulator/existing debugger. Exact native addresses are conditional on
the fingerprint and UOPT executable identity. Unknown fingerprints fail
before compilation; nothing is installed or rebuilt to make them match.
Output must resolve inside conker/build, including existing symlink targets.

The helper compiles a normal baseline using the unchanged owner profile,
runs the diagnostic, then compares .text, all function metadata, relocations
and the union of data/literal/BSS pools. Require nonempty output, its completed
optimization banner, a real driver-code0 receipt and unchanged compiler hashes.
Failed/incomplete/missing/changed output cannot become code_unchanged=true.

Fresh complete traces for the same seed:

| Mode | Trace Bytes | Object Identity |
| --- | ---: | --- |
| 4 | 31,237 | Text/functions/relocations/pools identical |
| 6 | 16,275 | Text/functions/relocations/pools identical |
| 7 | 26,549 | Text/functions/relocations/pools identical |

Mode6 now contains actual constrained register assignments and live-range
splits. Its expression52 is the -48 flag virtual register and is assigned
internal color2; expression22, the -12 index virtual register, also gets
color2. These are optimizer-internal IDs, not architectural MIPS register
numbers. Confirm their relation to the emitted V1 flag from actual MIPS
instructions before deriving a new source edit. This trace is allocation
evidence, not proof that all sound C transformations are exhausted.

## Verification And Bank

Six new diagnostic tests pass in 3.568 seconds, no skips. They exercise real
mode6 completion and effective failed/partial/empty/missing-driver/object
controls, separate text/function/relocation/pool corruption, pre/post compiler
fingerprints, mode/path constraints and a resolved symlink escape. Fresh mode4
and mode7 helper invocations also finish with identical objects.

Fresh consumer make tools-check, mounted/older standalone check_project_tools
and Windows py_compile pass. Existing immutable/corruption tests05/06 pass
in 1.696 seconds: all nine frozen inputs and 189,088 protected data bytes/720
owners remain exact. The previous full20 public/native/owner/rebase/fault suite
receipt is reused, not rerun or described as fresh; its code, inputs and profile
are unchanged. No additional Claude call; the one-call lifetime-review budget
and rejected exhaustion assertion from Note1299 remain in force.

All 4,483 relative links across eight checked documents resolve. Standalone
Graphify update finishes with protective exit1: candidate18,344 versus saved
40,113 nodes, retaining19,398 excluded-but-existing nodes from2,972 files.
Preserve that refusal and existing skill/package/zero-node warnings; no force,
purge or dependency update. A post-commit hook receipt is checked separately.
Post-documentation immutable/corruption checks pass in 3.321 seconds.

Commit mounted tools 17bd18baa99a608b6bc2da53d19d14eece14dba8 first, then
consumer documentation and exact gitlink. Only the two new files are copied
into the older standalone mirror after checking neither destination exists:
old HEAD ddbdd16b53ce60b054fb6e11bf0649a41f48375a and all80 earlier hashes stay
unchanged; dirty357 becomes359, with82 checked fingerprints. Do not commit,
reset or duplicate that older history. No push, ROM/save/config/OGL/Release/
editor/guest-debugger mutation. Final reporting requires a fresh terminal
post-consumer Graphify Rebuilt receipt, advanced log bytes/UTC, zero native
workers and clean active tools/consumer repos.

## Resume

```sh
python3 -m tools.experiments.game_text_measurer_uopt_trace --mode 6
python3 -m unittest tools.tests.test_game_text_measurer_uopt_trace -v
```

Use the newly valid allocation trace to investigate the flag/index live-range
boundary, rather than repeating the old crashing modes or archived source
forms. Recover shared T0 zero after normalization and before the first
post-normalizer access, the call-only SP+0x68 spill/early reload, and full219
control flow. Requalify the final private/fired-fault/native/copied-owner/
neighbors/pools/both-padders/independent-links/rebases/whole-ELF/data/guard-prefix
gates before installation and fresh totals. No broad retail word-copy,
overflow trampoline, arbitrary padding or profile swap. Next actual function
after this match remains func_150417AC, 1,098 words; full Game goal is active.
