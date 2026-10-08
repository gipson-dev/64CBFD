# Game Random Selector Outputs Direct Match

Date: 2026-10-06. Starting checkpoint: `267cc784`.

**`func_1518E5D8` matches all 37 words / 148 bytes directly from C.**
VA 0x1518E5D8..0x1518E66C, ROM 0x1BBA88..0x1BBB1C, frame 0x18.
Replace the zero-return stub in
[generated_1BA1D0.c](../../conker/src/game/generated_1BA1D0.c) with its
seven-pointer void body and two owner-local helper prototypes. Existing O2/g3;
no new guards, profile, shared header, symbol, metadata or data changes.

## Recovered Contract

The first six arguments point to bytes; the seventh points to a halfword.
The first `func_150ADA20` result's low bit gates a fresh read/OR-one/store
through argument one. Argument zero receives byte 0x16 in the second RNG
call's delay slot. The second result's low bit chooses selector three or four
for `func_151429E0`, passing arguments two through four as its RGB outputs.
After that helper, argument five receives byte 0xC8, then argument six receives
halfword 0x401. These are sequential accesses, not an output snapshot.

The retained selector is already retail-exact across 31 words / 124 bytes.
It makes a **third RNG call**, forms
`D_8008A160 + selector*12 + (result&3)*3`, and reads/stores each RGB byte
separately. An output overlapping a later palette byte can affect the next
read. The used 60-byte palette prefix is independently bound to pristine
retail and the linked Game-data section. No selector or palette edits.

The retained RNG is original handwritten assembly: 18 words / 72 bytes at
0x150ADA20, ROM 0xDAED0. It loads/stores the eight-byte `D_800885B0` state.
Its independently modeled recurrence, for unsigned 64-bit incoming state, is:

```text
mixed = ((state & 1) << 32) | ((state >> 1) & 0xFFFFFFFF)
mixed ^= (state & 0xFFFFF) << 12
next = mixed ^ ((mixed >> 20) & 0xFFF)
```

The result is the sign-extended low 32 bits; state can retain bit 32.
Output aliases can mutate state between the first and second calls or after
the third. The wrapper is void: residual V0 is observed in guest tests, not
promoted into a meaningful public integer-return API.

## Compiler Controls

[Driver](https://github.com/gipson-dev/64CBFD-Tools/blob/master/experiments/game_random_selector_outputs_candidates.py)
screens six forms under O2/g3, O2, O1/g3 and O1: **24 controls**, each with
empty isolated diagnostics. The installed 32-bit selector and the inline
ternary call form both match directly under O2/g3. A byte selector omits
retail's A0 narrowing instruction: 36 words and 15 slot differences.
Its ternary and cached-first-result forms have the same O2/g3 output.
Volatile first pointers produce 37 words with 16 differences.

Plain O2 has 22..32 differences despite 36/37-word lengths. All O1 variants
overflow: 41..44 words, frames 0x20 or 0x28. Tests bind every exact length,
frame and difference count, including overflow. No compiler profile change
or instruction normalization is necessary.

Ignored receipts: `conker/build/game-random-selector-outputs/` and
`conker/build/game-random-selector-outputs-test/`.

## Qualification

[Six tests](https://github.com/gipson-dev/64CBFD-Tools/blob/master/tests/test_game_random_selector_outputs_match.py)
compare the independently linked selected C and pristine retail against an
independent ordered-memory reference:

- **4096 opaque guest cases, two bodies**: eight first/second RNG patterns,
  16 output layouts, two callback-mutation modes and two stack phases.
- **16384 connected-selector guest cases, two bodies** add all four third
  RNG variants and execute the complete retained selector.
- **8576 fully connected guest cases, two bodies** execute the retained
  selector and actual 18-word RNG. Twelve boundary/high-bit states across
  all layouts and two stack phases, plus all initial states 0..4095 in both
  phases. All **37 wrapper + 31 selector + 18 RNG words** execute.
- Compare every non-stack byte, complete non-stack read/write/call trace,
  callback-entry memory snapshots, selector/output arguments, residual low
  V0 and saved GPR/FPR/SP/RA restoration. Opaque helpers clobber caller-saved
  registers. Pointer homes and delay-slot status installation are checked.
- **14528 native cases** use the actual selected wrapper and retained
  selector C body: 2048 opaque, 8192 connected-selector and 4288 independent
  RNG-state-model cases. Compare all 256 storage bytes, ordered helper
  targets/arguments and all callback-entry snapshots. Halfword/pointer sizes
  are checked under freestanding 32-bit GCC with warnings as errors.
- Six compiled negative controls detect the zero stub, wrong first bit,
  selector, flag OR and either status/tail store-order change. A separate
  guest RNG control changes DSLL32 to DSLL and detects the lost state carry.

The initial fully connected test caught a fixture defect: the shared
low-word runner masks all registers after an ordinary instruction, losing an
untouched 64-bit RNG temporary. The **local** extension now preserves untouched
wide values and implements LD/SD, 64-bit shifts/OR/XOR; shared runners are
unchanged. The complete connected sweep passes after that correction.

Native RNG calls use the independent recurrence model, not actual MIPS RNG
execution. Native seed-byte aliases follow native endianness; guest aliases
are independently checked big-endian. Palette/state aliases use private
mapped storage as diagnostics, not claims that every overlap is a real caller.
Evidence excludes invalid/private-stack pointers, MMIO, concurrency, complete
caller domains, hardware execution and gameplay. No FP arithmetic is added;
saved FPR transport does not establish full FCSR behavior or host adoption.

All **65 focused post-link tests pass in 310.324 seconds**, no skips:
random selector/output, queue wrapper, both actor-dimension queries,
projection compiler/identity audit, descriptor shape measure, pair clamp,
indexed state-save, random timer and effect-packet regressions.

## Whole Linked Audit

NON_MATCHING ELF/progress/match-progress rebuild passes. Across **6059 slots**,
only `func_1518E5D8` changes; all slot addresses and sizes are preserved.
Init, Init data, Debugger and Game data remain byte-for-byte identical.
All **720 Game-data owners / 189088 bytes** are retail-exact. All **10646
guard rows** retain content/order; both helpers are unchanged and exact.
Target SHA-256:
`e47a679c532d7a7c0034ce81866884310ef78d038bb99845b03ed51dee642a56`.

Baseline and current complete owners compile independently after the normal
assembly processor. Both report the same **four existing Warning 712**
pointer/integer combinations at two calls each to `func_1518E4A0` and
`func_15190454`; only line numbers move. No new owner warnings. The existing
duplicate generated-recipe warning also remains; not a warning-free build.

| Section | Byte-Exact Converted Functions | Drift | Different |
| --- | --- | --- | --- |
| Total | 3318 / 5462 (60.75%) | 0 | 2144 |
| Game | 2645 / 4789 (55.23%) | 0 | 2144 |
| Init | 492 / 492 (100%) | 0 | 0 |
| Debugger | 181 / 181 (100%) | 0 | 0 |

Converted counts/bytes are unchanged because the old stub already counted
as C. README changes only aggregates; detailed recovery belongs here.
No sibling source/build/save/frozen Release change or push.
Root `make tools-check`, Python compile checks and `git diff --check` pass.
Documentation check: 3220 relative links across 23 documents, zero broken.

## Next Work

Inspect `func_1519E6BC`, still a zero-return placeholder in
`game/generated_1CA420.c`: 38 retail words, ROM 0x1CBB6C, frame 0x38.
Retail first calls `func_1519E688`, then reads `D_800E0920`; only a null slot
allocates through `func_151491F4` with eight arguments. It installs the result
in the global even on failure; success copies a 12-byte stack packet to
result+0x28. Recover callback mutations, allocation failure and packet/padding
provenance before installation. This is static inspection, not a new recovery.
Projection/pair-clamp frames remain open; the Game matching goal stays active.
