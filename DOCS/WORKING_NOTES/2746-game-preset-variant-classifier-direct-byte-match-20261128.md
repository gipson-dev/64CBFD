# Preset variant classifier direct byte match - 2026-11-28

`func_1518FDC4` in `conker/src/game/generated_1BA1D0.c` replaces its three-word
zero-return placeholder with **158 words / 632 bytes emitted directly from C**,
VA `0x1518FDC4..0x1519003C`, ROM `0x1BD274..0x1BD4EC`. There is no frame,
alignment tail or new word guard. Its owner-local forward declaration now gives
the recovered interface: `s32 func_1518FDC4(u8 *record, u8 *presetIndex, u8 variant)`.

Actual production: **4,725 / 5,528 (85.47%) total**, **4,052 / 4,855 (83.46%)
Game**, Init 492/492, Debugger 181/181. Zero address drift; 803 still different.
Conversion rows and denominators are unchanged. **251 more matches** reach the
active 90% target of 4,976/5,528. This adds exactly one direct C match.
Previous consumer `6d241bd0`; tools packet `58b62e2c6d67784d0cb3cf5db782b4a41919509c` was committed first.

## Recovered behavior and actual caller

The switch reads the unsigned byte at record +4. **34 supported types** select
one of nineteen preset indices, 0..18. A supported type always writes that
index to the output byte, then accepts only variant zero (return 1); every
other variant returns 0 after the write. The other **222 types** return 0
without writing the output. Variant is an unsigned byte. The supported map
differs from the neighboring pointer selector's 30-type map and was decoded
independently from this classifier's original tables.

The original first instruction stores full incoming A2 to the o32 +8 argument
home before masking it to u8. All three opening words, that argument-home write,
branch delay slots, return paths and instruction order match directly. Native
C evidence uses valid byte objects; guest-only argument-home aliases and fault
prefixes are machine evidence, not portable C semantics.

The current aligned prepared-ROM scan finds one direct JAL, ROM **0x1BC9F4** /
VA **0x1518F544**, in the already recovered **45-word** wrapper `func_1518F51C`.
All 45 original wrapper words and all 158 child words execute in **3,586
fixtures x four streams / 14,344 connected executions**. The wrapper consumes
the output byte and Boolean return and normalizes its default-promoted variant
before the child call. Fresh output-byte and return-value controls both reject.
The typed declaration leaves the complete wrapper's raw body unchanged. Its
subsequent ten-argument factory `func_1518F5D0` remains an **opaque boundary**;
earlier large parents and the factory are not newly qualified.

## Expanded pool and complete owner

The complete owner retains **61 C definitions, no GLOBAL_ASM, all 58 original
exported case aliases, and all sixty other source bodies**. Both generic and
generated padders reproduce the frozen before object and the same selected
whole object. Fifty-nine neighbors retain literal raw/padded bodies. The
remaining neighbor, `func_1519003C`, receives an explicit dependency audit:
its four compiler table bindings move by 580 bytes within the expanded pool,
and its complete **120 bound words remain exact**, with no guard or source
body change. The changed dependency is not excluded from acceptance.

The four contiguous original tables are:

| Function | High table / entries | Low table / entries |
| --- | --- | --- |
| Classifier `func_1518FDC4` | `jtbl_800A7B7C` / 122 | `jtbl_800A7D64` / 23 |
| Retained selector `func_1519003C` | `jtbl_800A7DC0` / 122 | `jtbl_800A7FA8` / 23 |

Each pair stride is 488 bytes. The compiler emits **290 R_MIPS_32 entries /
1,160 table bytes**, followed by eight zero alignment bytes. Every entry has
the correct function owner and target-relative case offset; **290 single-entry
mutations reject**. The compiler padding is not public original data: adjacent
coefficient **`D_800A8004` remains untouched**.

The existing owner Makefile anchor changes from `jtbl_800A7DC0` to
`jtbl_800A7B7C`, with an updated comment. The actual generated **three-command**
recipe and O2/g3/mips2/o32 profile remain unchanged. Guard history is identical.
Four old unrelated IDO Warning 712 diagnostics and six existing duplicate-recipe
warnings remain; no new compiler or assembly warning is introduced.

## Qualification and production acceptance

- SDK/native32: **1,703,936 cases each at O0/O2/O3**, exhaustively crossing all
  256 type bytes, all 256 variant bytes, thirteen output alias modes (separate
  byte and all twelve record bytes), and two initial byte patterns. All twelve
  record bytes, output and exact return are checked. Separate translation units,
  strict aliasing, trapping UBSan and LTO type checks pass. Six semantic controls
  fail with exit 42, including the rejected-variant output write and unsupported
  type's no-write behavior.
- Guest: **10,368 cases x four streams / 41,472 executions**, all **158 reachable
  words**, no unreachable words. Literal complete normal states and access/fault
  prefix states agree for original GNU-linked retail, raw C and both padded
  streams, including **1,382 fault quadruples**. Five alias modes, three pointer
  domains, two stack phases, poisoned A2 high bits and 1,152 guest-only table/
  argument-home cases are included. Four effective semantic controls reject.
- **16 actual GNU links** independently rebase both function entries, all four
  tables and nineteen preset globals, including signed HI16/LO16 carry seams.
  All 158 classifier words, 120 retained-selector words and 290 table entries
  match at each rebase. The classifier's four external code binding positions
  and two original internal PC16 bindings (byte32/64 to `.L15190030`) are retained;
  the selector's 42 external bindings are also checked.
- Independent frozen-before-C plus original-target-ASM prediction equals the
  private and actual production full ELF: **479 changed bytes, zero exclusions**.
  The target body/size change and closed three-record symbol/string serialization
  permutation (`jtbl_800A7B7C`, `D_800A6464`, `D_80098634`) are explicit. No actual
  C bytes supply the prediction. All **720 protected data owners / 189,088 bytes**,
  other linked bodies, addresses, guard history and conversion rows stay fixed.
  Eleven strict-image controls reject: target, both table pairs, adjacent data,
  selector, original wrapper JAL, extent, named table value and ELF header.
- Five complete packaged tests pass in both closed tools roots before and after
  installation: **20 fresh checks**, equal reports and audited import/data
  closures. Shared `make tools-check` passes. The real dirty tools sibling and
  its dependency fingerprints are preserved. Both reused wrapper-test dependencies
  are pinned explicitly; the selected isolated root is `sibling-overlay-v2/tools`,
  and the initial twin is preserved.

ELF SHA256: `eb53348470049c098c82f8b68cdd57cee2659eca50365cb0924ab6502293df6c`.
No new visible gameplay acceptance is claimed. README changes are its two
aggregate rows only. Graph refresh uses scoped AST extraction with all previous
IDs and qualification fields retained, including the relocated selector's
existing qualification. Final graph/hook/immutable-bank receipts live in
`conker/build/game-preset-variant-classifier-1518fdc4-private/`.

Host applicability is assessed read-only: the N64 owner table anchor is specific
to this decomp build. No host edit/build/launch; Release stays frozen. N82
`func_1514EECC` remains parked. No push or subagent is used.

Next: continue ordinary unmatched Game matching from the sealed N92 bank.
