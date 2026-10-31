# Packed attached-object state decoder - C recovery and guarded match

2026-10-31. `func_15073B38` in `game_981E0` replaces its zero-return C
placeholder with the recovered packed-field decoder. Its complete 240-byte
slot at VA `0x15073B38..0x15073C28`, ROM `0xA0FE8..0xA10D8`, matches all
60 retail words and four global relocations after four checked tail-register
allocation guards. There are no insertions, omissions or profile changes.

## Recovered behavior and interface

The interface is `void func_15073B38(void)`. Each store resolves the current
`D_800D154C` actor and its attached-object pointer at offset `0x31C`:

1. Read `D_800D1580`, mask its low 16 bits, convert the integer exactly to
   `f32`, and store to the attached object's offset `0xA8`.
2. Read the packed word again, select bits 16..23, convert to `f32` and then
   to `u8`, and store at offset `0xAC`.
3. Read the packed word again, select bits 24..31, and store the byte at `0xAD`.

The local `GameAttachedPackedState` view describes these three offsets without
changing shared structure definitions. Its member names describe the recovered
storage view; no particular gameplay meaning is claimed for the fields.
The source retains two float temporaries and the retail unsigned byte conversion.
Caching the input word changes behavior when the guest output aliases that word.

The routine is frameless. All 60 words are retained. Since the second conversion
input is always an exact integer in `0..255`, its 18 unsigned-conversion fallback
words at indices 28..45 are unreachable for this routine's inputs. The remaining
42 words are exercised. This is distinct from removing or replacing the fallback.
The bounded exact conversions preserve the incoming FCSR on return.

## Tail allocation guards

The compiler emits the semantic routine and complete conversion sequence under
the existing O2/g3 profile. Four expected-word guards normalize one closed tail
allocation cycle: T9 becomes T0 for the actor, T0 becomes T1 for its attached
pointer, and T8 becomes T9 for the final byte. The guards are at offsets
`0xD4`, `0xDC`, `0xE0` and `0xE4`. No other instruction, relocation, frame,
FP operation, control flow, load/store offset or scheduling order changes.
All eight altered-preimage/relocation controls fail closed in the actual padder.

Original and padded execution compare complete machine state literally. The raw
C comparison permits only the four caller-clobbered GP roles T0/T1/T8/T9 to
differ; memory, access traces, FP state, FCSR, and all other registers agree.
The closed instruction-level allocation proof independently checks the four words.

## Qualification and production evidence

- 2,756 guest cases / 8,268 original, raw-C and padded executions exercise all
  42 reachable words, mixed byte/halfword boundaries, FCSR inputs and stack phases.
  All 36 memory-access cuts agree. Two independent symbol layouts pass 18
  rebased cases; 36 guest alias cases qualify the repeated input reads.
- The aligned retail pointer census finds only ROM `0x22B0E4`, corresponding
  to `D_800863FC[206]` (command `0xCE`), and no direct JAL. The original six-word
  dispatch window at ROM `0x98360`, VA `0x1506AEB0..0x1506AEC8`, executes in
  30 cases. The target result is ignored. This qualifies the callback window,
  without claiming recovery of the complete dispatcher parent.
- Native32 SDK C passes 655,360 cases per O0/O2/O3 profile with UBSan: every
  low halfword and every pair of upper bytes, with seven low-halfword boundaries.
  Whole actor/attached-object canaries, input globals and owner pointers agree.
  Nine native wrong variants and ten compiled guest wrong variants have semantic
  witnesses. The cached-input control is guest-only. Compiler/oracle failures
  are not accepted as semantic witnesses; guest aliases and transient FCSR
  changes are not claimed as native C evidence.
- Eight fresh canonical tests pass in each tools copy, plus both shared tools
  checks. Two installed checks per copy run fresh; six unchanged semantic checks
  are explicitly reused under complete input, module and artifact fingerprints.
- Five actual Make commands reproduce the qualified padded object and preserve
  all 327 neighboring owner functions and pools. All 36 inherited compiler
  warnings match after exact file/line relocation; there are zero new diagnostics.
- Strict production whole-image prediction accounts for exactly 160 changed bytes:
  159 target code bytes and one target symbol-extent byte. Metadata changes and
  exclusions are zero. All 6,055 other linked bodies, all 6,056 function addresses,
  inherited guards, and 189,088 protected Game data bytes across 720 owners agree.

## Banking and continuation

Tools commit: `ebde643a699ec30ba7820032d7f104bbea953cd1`. Production ELF SHA-256:
`3da616798cc1b28cd7dc490d7a7d8cafdca9d52355072db68267f42b0c4dd6ec`.
Actual recount: **3,999/5,506 (72.63%)** total, **3,326/4,833 (68.82%)** Game;
Init remains 492/492, Debugger 181/181, and address drift is zero.
**131** more exact functions are needed for 75% (4,130 total).

Receipts are in ignored `conker/build/game-attached-packed-state-15073B38-match/`.
Only the two aggregate README status rows change. The scoped graph refresh covers
the source, three tools modules and seven documents, retains every old node and
valid relationship, and retires the obsolete signed-placeholder return edges.
It does not claim full-corpus extraction, reclustering or new global analytics.
Next queued screen: `func_151638E0`. Private candidates remain uncredited.
No push or host-port/Release changes are included.
