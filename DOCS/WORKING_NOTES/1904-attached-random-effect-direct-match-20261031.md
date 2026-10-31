# Attached random effect restored directly from C

Date: 2026-10-31. Target `func_150B5950`, owner
`conker/src/game/generated_E2DA0.c`, retail assembly `conker/asm/E2DA0.s`.
VA `0x150B5950..0x150B5A3C`, ROM `0xE2E00..0xE2EEC`.
All 59 words (236 bytes) emit directly from semantic C under O2/g3. There
are no guards, insertions, omissions or alignment words. The 56-byte frame
saves S0 at SP+24 and RA at SP+28; the actor home is SP+36 and the three-float
position buffer starts at SP+40. A named, used `f32 sample` declared before
the position array recovers the retail frame and homes without artificial
padding. The original unreachable duplicate attachment load at +0x3C remains.

## Behavior and interface

`void func_150B5950(u8 *record)` snapshots the attached actor pointer from
record+0x28. If the actor's first word is zero or its tag byte at +0x3B differs
from record+0x2C, the record's signed lifetime at +0xE becomes -1. A valid
actor without its +0x1D4 attachment skips both random samples and emissions.

Otherwise, two independent `func_150ADA68(void)` samples are compared against
separate mutable float globals. The first passing comparison copies the
actor's position at +0x14/+0x18/+0x1C and submits it with the record's +0xC and
+1 bytes. The second passing comparison asks `func_150B60E0` for a position,
then submits that position with freshly loaded record bytes. The cached
actor survives provider mutations of record+0x28. Tags and liveness are not
rechecked after providers. Both comparisons are strict and ordered: equality
and unordered NaN cases reject emission.

Both retail thresholds, `D_8009FC98` and `D_8009FC9C`, initially contain
`0x3DDDACEF` (approximately 0.10824). Their separate bindings matter even
though their initial values agree; tests mutate them independently. The RNG
is retained handwritten assembly. Its first instruction overwrites A0 and
its return is in F0; no incoming argument is used. Complete PRNG/hardware
behavior is not newly qualified by this change.

The position wrapper's output parameter is corrected from `s32` to `f32 *`.
Its complete emitted body is unchanged. Original wrapper instructions pass
`D_8009FC30`, the output buffer, and actor->attachment+0x140 to
`func_15143134`. The emitter itself remains unfinished and bounded in tests;
this recovery does not claim to restore its 127-word body.

## Caller and qualification

- Original `func_15149264` supplies one record through callback table
  `D_8008A4E8`, index 69, selected by signed record byte +0x11. The provided
  retail input has no aligned direct JAL to this target and one aligned
  literal pointer at ROM `0x22F0BC` / VA `0x8008A5FC`. The complete 45-word
  dispatcher runs for 192 cases / 3,072 executions, covering all its words,
  lifetime ticking, callback disable, expiry, destructor and cleanup decisions.
  Four poisoned return values prove this callback's result is ignored.
- Raw C, original assembly, padded owner and actual-Make object agree across
  three independent GNU-linked layouts. All nine bindings agree, including
  HI/LO carry boundaries.
- Guest tests cover 576 ordinary cases / 2,304 executions, ten alias cases,
  92 interrupted-access prefixes and 18 branch-delay cuts. All 58 reachable
  target words are visited; the duplicate load at +0x3C is not forced reachable.
  Registers, floating registers, HI/LO, memory, ordered callbacks, argument
  payloads, and access traces agree literally across the four images.
- The original 12-word position wrapper is connected for 192 cases / 768
  executions. All its words execute, including reloading the actor attachment
  and supplying the real point-source/matrix argument shape. The downstream
  transform, effect emitter, RNG, destructor and cleanup stay bounded models.
- Native32 runs 262,144 cases each at O0, O2 and O3 with trapping UBSan.
  The corpus spans all 65,536 kind/selector byte pairs, stale actor/tag gates,
  absent attachments, independent random decisions, NaNs/equality, callback
  mutations, complete record/actor state, argument/payload logs and canaries.
  All 15 compiled negative controls fail with semantic mismatch (exit 1).
- Both tools copies pass eight fresh canonical methods and shared tools checks.
  After installation, two checks run freshly in each copy; six unchanged
  semantic checks are reused only under full input/module/artifact identity.
- All 11 neighboring raw/padded routines and normalized pools remain fixed.
  Three actual Make commands reproduce the qualified object. Executed compiler
  and assembler diagnostics are empty; the dry plan retains two unrelated,
  pre-existing duplicate-recipe warnings.
- Strict image prediction has zero exclusions: 195 changed bytes = 174 target
  code bytes + one symbol-extent byte + 20 metadata bytes. The latter are two
  closed, named two-symbol reorderings: D_8009FC98/D_800A8F98 at symbol offset
  0x2C1894 and D_8009FC9C/D_800A8F9C at 0x2DE7B4, including their exact string
  blocks. Every named definition retains its value, extent, type and section
  except the target's explicitly recovered size. All 6,055 other function
  bodies and all addresses remain fixed; all 189,088 Game-data bytes and 720
  owners remain exact. Guard CSV, progress inventory and shared headers are
  unchanged.

These checks establish the recovered routine and specified provider contracts.
They do not establish portable C alias/fault behavior, hardware FCSR flags or
traps, complete downstream rendering/PRNG behavior, or gameplay acceptance.

## Banked state

Predecessor consumer `f442569a58a3318f074bf464e64089947f8a0fea`.
Tools committed first at `d5911c580148aa4a68524b18e40ccc4875f8e7c2`; the older mirror's existing work is preserved
without committing that checkout. Actual production ELF SHA-256:
`09bbb74cdc91646d5278f9f13fba388c6f867768bc18498c251633aa19e9585e`.

Actual recount: **3,981 / 5,506 (72.30%)**, Game **3,308 / 4,833 (68.45%)**,
Init 492/492, Debugger 181/181; zero drift, 1,525 different, and **149** more
needed for 4,130/5,506. The 75% goal remains active. Next private screen:
`func_151A90C0`. Evidence: `conker/build/game-attached-random-effect-150B5950-match/`.
Historical completed builds are restorable from sibling `64CBFD Build Archive`.
No push.
