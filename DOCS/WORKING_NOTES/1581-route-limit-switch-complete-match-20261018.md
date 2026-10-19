# Route Limit Switch Complete Match

Date: 2026-10-18. **Installed complete C match: all 44 words / 176 bytes exact.**

Recover `func_1508E6D0`, generated_B3020, VA `1508E6D0..1508E780`, ROM
`BBB80..BBC30`, after [Note 1580](1580-route-slot-reservation-direct-c-conversion-20261018.md).
Consumer predecessor `300be452`; tools predecessor `c1fbc31`. Bank tools
**943620e** first, then consumer source/guards/docs/pin. No push.

## Complete Source And Interface

Replace the false zero-return C stub with `s32 func_1508E6D0(s32 type)`.
Preserve the address name, descriptive full-word parameter and one purpose
comment. The route/limit description is a working subsystem label, not a
claim to recover an original developer-assigned function or enum name.

The switch returns the original literal values for selectors 3, 9, 20, 21,
22, 24, 25, 33, 34, 35, 36, 55, 56, 63, 64 and 65; every other selector returns
100000. Preserve the independent equal-valued return blocks and the two real
shared groups 25/64 and 24/65. Ordering C cases by the retail return blocks emits all 44 words
and the exact 63-entry table directly in isolation, with no frame or compiler
diagnostics. Do not narrow the selector to a byte or combine independent
equal-valued cases merely because their public results agree.

The real call at VA1509E4C8 / ROMCB978 loads A0 with a full-word LW in its JAL
delay slot and consumes the result. Keep that ABI; no original type-name
authenticity or whole-caller execution is inferred.

Isolated raw code SHA:
`98dd4fe3895f04576c1a884b3d5c93acb9e4048db509ea1523b97a02aba5b8d7`.
Full-owner raw code SHA in both profiles:
`457e7f1845b2cdcedb504493f599c5217cd9af4312b53bdabc70a7e789db1799`.

## Table Ownership

The retained table is jtbl_8009DA94, VA `8009DA94..8009DB90`, ROM
`242554..242650`, exactly 63 entries. IDO emits the isolated table at pool
offset0, followed by four alignment bytes. In the complete owner it follows
the existing eight-byte constant 3f91de69ad42c3ca, at offset8. Before recovery
the owner pool is 16 bytes including alignment; afterward it is 272 bytes:
eight unchanged constant bytes, 252 table bytes and 12 alignment bytes.
Every normalized relocation target equals its original function-relative
destination; both owner profiles preserve all 72 other routines and constants.

The existing padder keeps the original global data rather than emitting that
compact pool. Append exactly two expected-word and relocation-checked bindings:
HI16 at +0x10 changes ownership from .rodata to jtbl_8009DA94_game; LO16 at
+0x18 changes the pool addend from8 to0 and uses the same retained symbol.
These are table-ownership bindings, not instruction-scheduling normalization.
No Makefile/compiler-profile change, inserted word, omitted word or shared
padder change. Preserve the complete original guard prefix byte-for-byte.

## Fresh Qualification

Eight pre-install tests pass in **106.861 seconds**. After strengthening the
image-corruption gate, its focused rebase/image test passes in **3.411 seconds**.
All **eight final post-install tests pass in 20.699 seconds**, no skips.

- Run 1,805 selector inputs in both stack phases: low/negative ranges, every
  active table position, all result blocks/default, high-word lookalikes and
  512 deterministic full-word samples. Compare independent literal-map output,
  complete modeled GP/FP/LO state, RAM and ordered reads. All 44 instructions
  and all 63 table entries are visited; out-of-range selectors perform no
  table read. This is a bounded corpus plus an inspected full-word range gate,
  not an exhaustive 2^32 enumeration or hardware execution.
- Pass 126 fired access-cut pairs, one real table-read fault for every entry
  in both stack phases. A mapped table-mutation witness redirects selector3
  to the original 1800-return block. It qualifies guest table ownership, not
  portable mutation of a compiler-owned read-only C switch table.
- Run the same 1,805 inputs in freestanding native32 O0, O2 and O2+UBSan.
  Three ordinary source negatives complete with expected exit21: byte-narrowed
  selector, wrong default, and missing selector63. Crashes/timeouts are not
  accepted as semantic controls; passing native variants exit0.
- Execute 18 actual two-word JAL/LW caller windows across both stack phases,
  checking full-word high-bit selectors and return values. The stop trampoline
  is explicitly synthetic; the complete caller is not executed.
- Four corruption controls independently fire the exact stale-word or stale-
  relocation rejection for each of the two table bindings. Three image-byte
  mutations fire the actual strict image verifier, covering target code and
  unrelated beginning/end regions; no metadata section is excluded.
- Independently assemble the original instructions and all 63 target labels.
  Three GNU maps produce identical source/original code and tables, including
  HI/LO carries. Execute 63 mapped cases across those code and data addresses,
  checking the independent public result map.
- Preserve all 72 owner neighbors in each compiler profile; qualify the actual
  padder and seven expanded shadow Make commands. The normal-profile projection
  override remains identical; no GLOBAL_ASM remains in this owner.

The initial table decoder incorrectly treated the longer default return like
the shorter constant-return blocks; fix only that test fixture. One overlapping
rerun was stopped and is not an acceptance receipt. The completed isolated runs
above are authoritative. No debugger, compiler capture, REA setup or Claude call.

## Exact Image And Production Audit

Retain the original first private link. The initial target-only prediction
exposes 76 extra metadata bytes, not a code/data mismatch. The table's new
external reference reorders one adjacent four-symbol group:
jtbl_8009DA94_game, D_8009FBC0, D_800962F0, .L15032700_game_data becomes
D_8009FBC0, D_800962F0, .L15032700_game_data, jtbl_8009DA94_game.
Check every original name, definition, section, adjacency and string position
before reproducing that exact permutation. No broad metadata allowance.

The full ELF prediction changes exactly **221 bytes**: **144 target-code
bytes**, **one target symbol-size byte** (12 ->176), and **76 symbol/string
serialization bytes**. Actual Make reproduces the complete predicted image,
including all metadata. All other 6,056 bodies, every address, all 189,088
protected Game-data bytes / 720 owners and every frozen input outside the
declared source/guard/image changes stay fixed.

The shared guard manifest triggers a wider dependency rebuild. It succeeds
with existing duplicate generated_12D630 recipe warnings and warnings from
untouched C sources, including pointer/integer combinations, unsupported long
double and -Xfullwarn. The target's compiler diagnostics remain empty; do not
claim a warning-free full build. The CSV's existing mixed line endings remain
intact; Git's CRLF-to-LF advisory is not a compile error or added content churn.

Successor hashes:

- ELF: `50c875272f3f2d883d70b453cbb3a92582d0f65fd0b1ef351b88ce10f8108f72`.
- Owner: `ae4ff8288c031c13f92b513b7fd38658de904e66b3b12c7c8f64531458b58abc`.
- Guards: `4bf9c3985355aa28638ceab3610d581701b20e25a69937ed8e85bdad71c15df4`.

This is an already-C stub replacement, not another conversion-count increment.
Fresh matching: **Game2997/4832 (62.02%)**, **total3670/5505 (66.67%)**, Init
**492/492**, Debugger **181/181**, **1,835 different / zero drift**. Conversion
counts/bytes remain **5505/6044 (91.08%), 86.08% bytes** overall and
**4832/5323 (90.78%), 85.44% bytes** for Game. Exclude repeated CSV headers.
README receives only aggregate matching rows; detailed evidence stays here.

Both tools copies pass their three setup tests and smoke checks; consumer
`make tools-check` passes. All three new tools files are identical ASCII and
Python-valid. Preserve all 1,310 pre-existing mirror hashes and its ddbdd16
HEAD; add only these three files, leaving 1,313 dirty paths. No mirror reset
or commit. Post-commit graph preservation is a separate final gate in ignored
`conker/build/game-route-limit-switch/graph-audit.json`.

```sh
python3 -m unittest tools.tests.test_game_route_limit_switch_match -v
python3 -m tools.experiments.game_route_limit_switch_integration --audit
make -C conker match-progress NON_MATCHING=1
make tools-check
```

## Next Target

This switch is finished. Continue with the unfinished `func_1508E780`, VA
`1508E780..1508E89C`, ROM `BBC30..BBD4C`, **71 words/frame0**, currently68 linked
differences. Recover its signed-halfword D_800D23B0+0x16BC ==0xB8 mode gate,
full-word selector, special-mode returns and default -1. The ordinary switch
has **57 active entries** beginning at jtbl_8009DB90; its three trailing zero
words are alignment, not selectors. Qualify both modes and compact-pool/table
ownership before installation. Broader Game matching remains active; no
sibling host, frozen Release or full-gameplay acceptance claim.
