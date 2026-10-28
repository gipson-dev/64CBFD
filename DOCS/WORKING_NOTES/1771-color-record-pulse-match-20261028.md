# 1771 - Color Record Pulse Match - 2026-10-28

The adopted Native ELF measures **3,849/5,506 exact C functions (69.91%)**,
Game **3,176/4,833 (65.71%)**, zero address drift and 1,657 different.
Only `func_151A5070` gains matching credit. The unchanged 75% threshold is
4,130 exact C functions, requiring **281 more**.

## Recovered routine and interface

`func_151A5070` in `generated_1D0840.c` occupies VA
`0x151A5070..0x151A5130`, ROM `0x1D2520..0x1D25E0`:
48 body words, a 24-byte frame and six relocated bindings, with no guards.
Two HI/LO pairs read `D_800BE9E4` at +16/+28 and +92/+96.
J26 calls reach `func_1516972C` at +44 and `func_10011FA0` at +80.

The canonical descriptor callback is `void(struct102 *)`. Reuse the existing
owner-local `Type5AColorRecord` view through a local cast; the factory already
creates this type as 0x5A with a 0x20-byte base record. Its sole retail pointer
literal is ROM `0x2311B0`, VA `0x8008C6F0`, in descriptor slot 90 at
`D_8008B4A8 + 90 * 52`. There are no direct JAL/J sites. The initial private
typed-record signature was corrected to the registered callback interface;
both versions emit the same raw words, but only the canonical final source
receives qualification and matching credit.

A zero lifetime skips countdown. Otherwise wrapped 32-bit subtraction expires
the record when the signed result is at most zero; expiry calls release and
returns without storing that result or reading color/flag fields. A surviving
result is stored before checking the callback byte. A zero callback byte sends
mode 2 to the Init helper. Preserve its established `void(s32 *)` declaration
and literal `(s32 *)2`: the retained helper stores the bits in `D_80042770`
without dereferencing them. No shared-header or helper changes are needed.

The routine then reloads the clock and multiplies it by two with 32-bit wrap.
A zero state decreases the red byte, clamping a signed result below 0x90 and
setting state to one. Any nonzero state increases it, clamping a signed result
at least 0x100 to 0xFF and clearing state. Preserve the final byte narrowing,
nonbinary state values, late clock read and incoming argument-home reload.
The unreachable lifetime store at +60 remains in the exact 48-word body.

## Complete owner and image

All 22 neighboring functions and raw/padded pools remain unchanged, including
one GLOBAL_ASM routine. The actual five-command generated Make recipe uses
normal O2/g3, preprocesses/compiles/postprocesses/pads/assembles the complete
owner, and reproduces the independent padded object with zero diagnostics.
The word-patch CSV and compiler profile remain unchanged.

Strict independent prediction permits exactly **143 changed image bytes**:
142 target code bytes and one target symbol-size byte (12 to 192), with zero
exclusions. The production build reproduces that image. All 6,056 disassembly
addresses, all 6,055 other bodies, named ELF definitions, section geometry,
map and C inventory remain fixed. All 720 Game data owners / 189,088 bytes
remain exact. The inherited duplicate generated_12D630 Make warning persists.

## Behavioral qualification

Both tools copies pass eight fresh canonical methods and shared tools checks.
Production reruns two installed methods per copy; six semantic checks are reused
only after exact input, module and qualified-artifact fingerprint comparison.

- 4,392 guest cases cover wrapped lifetime/tick extremes, every red byte,
  nonbinary direction/flag values, eight aligned clock aliases, helper effects,
  volatile-register/outgoing-home clobbers and incoming-home redirection.
  Complete state and ordered traces agree, visiting all 47 reachable words.
- 108 cases execute the original 11-word descriptor dispatch window and the
  retained 28/20/8-word release chain plus the four-word Init mode helper.
  The dispatcher queues the next record before calling the target. Current
  helper bytes equal retail. The parent `func_151670C0` remains a placeholder;
  final unlink stays a bounded provider. This is not full-parent or gameplay
  acceptance and gives those routines no new credit.
- Native32 O0/O2/O3 each pass 786,480 cases through the actual `struct115.unk0`
  function-pointer type, with trapped UBSan, whole-storage fences, disjoint
  clock storage or valid corresponding-signed/lifetime/tick-cell aliases.
  All twelve C semantic negatives fail. Guest-only stack-home and overlapping
  byte-field probes are kept separate from portable native C storage claims.
- 194 fired fault-prefix pairs preserve state, trace, PC and delay context.
  Expiry needs no color/flag mapping and performs no remaining-value store.
- Three GNU relocation layouts pass 36 execution cases, checking HI/LO signed
  carry and both J26 bindings. Real padder reproduction, body/binding/extent
  rejection, four actually compiled IDO semantic negatives and six independent
  complete-image corruptions reject altered evidence by value.

## Bank and continuation

Baseline consumer `f1f9b8c6`, tools `835f52a`. Tools are committed first as
`6425b76817c47ae510a4c9414b9adec8efe1bbdf`. The seal verifies 16,288 current
files and 288 focused inputs. Preserve all 1,754 inherited dirty paths in the
older independent tools mirror, adding only the three target modules there.
No mirror commit or push is requested. Host Release stays frozen.

| Artifact | SHA-256 |
| --- | --- |
| Adopted ELF | `3987efc711a7e2d30ee9b4dbabb901846750386b38f384bb6ffdc2fbe31750c9` |
| Padded owner | `b85057c8aafe3f5d04879406d60579c93062346540cc0fb1bdfbcac1af06a16d` |
| Recovered source | `2b068b752175b1345e767860dffe4f608d841ceb66ee64eb20336f35fec9214b` |
| Raw original/compiler body | `bbc7cdbe461437db044d53b39f2781d635e535d8220a063166546906476e1ee8` |
| Complete retail body | `c901c644a9718edc094481c76cbaff7e8513848183388903f94d9f995a9a0542` |
| Unchanged guard CSV | `20131e428c071ea6d2cbee21968f122274bc71fb167a2a356b3033ff5582f8b9` |

Scoped Graphify closeout refreshes eleven changed C/Markdown/tool files. Its
retention gate accounts for all 45,893 old nodes and 94,102 old relationship
contexts, retiring only the target placeholder's false s32 return. Retain
outside-scope manifest freshness and historical communities; do not claim a
full-corpus extraction. Record both call bindings and the real descriptor
registration without inventing a direct caller edge.

Next inspect the 48-word `func_151B9BF0` record constructor. The remaining
queue contains 1,528 placeholders, 120 semantic/other entries and nine unlocated
screens; it is triage only. Keep `func_1514E920` parked and uncredited and the
75% goal open. Routine Claude calls: zero.

Prepared-checkout command:

```sh
python3 -m unittest tools.tests.test_game_color_record_pulse_match -v
```
