# Seed sprite tick direct match - 2026-11-25

`func_151934B4` replaces the zero-return placeholder in
`conker/src/game/generated_1C0840.c` with a semantic **void sprite update**.
All **106 words / 424 bytes and five relocation positions emit directly
from C**, with the original **72-byte frame** and **zero guards**. Its
107-word retail slot retains its original final alignment NOP; that word
is outside the 424-byte function symbol. No insertion, omission, new tail,
profile change or guard-file change. VA `0x151934B4..0x1519365C`, slot through
`0x15193660`; ROM `0x1C0964..0x1C0B0C`, original tail through `0x1C0B10`.

Production: **4,691 / 5,528 (84.86%) total**, **4,018 / 4,855 (82.76%) Game**,
Init 492/492, Debugger 181/181, zero address drift and 837 still different.
One new match; no additional constructor, dispatcher or effect-provider
credit. **Eight more verified matches reach 85%.** Denominators and
conversion rows are unchanged.

The measured partial runtime view is 180 bytes. Signed halfwords identify
fall ticks at 0x94, target extent at 0x96, expiration phase at 0x98,
position X/Y/Z at 0x9C/0x9E/0xA0, horizontal/vertical extents at 0xA2/0xA4,
floor Y at 0xA6 and growth ticks at 0xAA; signed variant is byte 0xB3.
Other bytes retain their original contents. The seed-sprite name is inferred
from the adjacent recovered sprite constructor and the observed grow/fall
behavior, not recovered original source names.

While vertical extent is below its target, it captures the original signed
growth ticks, arithmetic-shifts by two, writes `(quarter*24)/3` and
`(quarter*6)/3` to the extents, and adds the current integer delta through
a narrowing halfword store. Otherwise it increments and narrows fall ticks,
caps only values above 20, and subtracts half the signed low-32-bit product
of fall ticks and delta from Y. The C explicitly uses unsigned arithmetic
for low-word multiplication/addition; native validation includes full-32-bit
delta extremes. If the narrowed Y is below the floor, variant 1 submits an
effect at `(x,floorY,z)`, then every variant stores phase -1.

The effect ABI is `void(u8,f32,s16,s32,void*,u8,s32)`. The actual arguments
are kind 5, size 30.0, alpha 255, randomize 0, the local three-float vector,
unsigned owner byte 0xC and unsigned owner byte 1 widened to signed 32 bits.
The source retains saved S0 at SP+0x28, RA at SP+0x2C, and the original
position vector at SP+0x38/0x3C/0x40. Opaque provider mutations and volatile
clobbers qualify the final phase store and captured argument lifetimes.

The original callback table `D_8008C9C8` has 22 entries; index 15 at ROM
`0x2314C4` names this target. An aligned whole-ROM census finds that single
literal and no direct J/JAL patterns. Both complete original consumers pass
A0 and ignore V0: the large sprite updater `func_15168870` is 111 words /
frame 24 with selector byte 0xB2; compact updater `func_15167E0C` is 195 words /
frame 32 with selector byte 0x2F. The large consumer checks phase 0x98 and
frees the object on -1. These are binary ABI/layout qualifications, not
claims that other selected table entries or every producer are recovered.

The first candidate already emitted 106 words but differed in 11 words.
Capturing the unshifted growth counter restored the V0/V1 lifetimes and
removed seven differences. Declaring that counter before the vector restored
its SP+0x38 home and removed the final four. Four bounded combinations show
the independent effects. No dummy local or physical register declaration is
used. The source header now accurately describes both recovered functions;
this comment-only normalization retained identical raw and padded owners.
Its first private image is explicitly reused on that basis; final suite
image executions below are fresh.

Validation:

- Complete before/after owner compilation and both production padders match.
  The adjacent constructor's complete body/bindings and all raw/padded pools
  are unchanged. Actual Make replays its three production commands with
  identical full owner output and zero diagnostics.
- Guest: 3,904 cases across five literal instruction streams, including
  signed-halfword boundaries, full-width delta/product wrap, all four rounding
  modes, mutable globals, stack-backed owners, high-bit context/channel bytes
  and provider mutations. Each stream makes 516 opaque effect calls. Full
  memory, private frame, all GPR/FPRs, HI/LO, saved ABI state and FCSR agree,
  including 81 access-fault cut quintuples. All 97 reachable words execute;
  nine impossible constant-divisor trap/check or duplicate-load words remain
  byte-qualified. V0 is compared mechanically, not treated as a void result.
- Native: actual recovered C plus a separately typed provider in three TUs,
  8,192 cases at O0/O2/O3, strict aliasing/FP, UBSan traps and LTO type checks.
  Typed owner, canaries, globals, seven-argument metadata, vector values and
  MXCSR agree. Seven controls complete with comparison exit 42; traps and
  signals are not credited. An ineffective threshold-only clamp mutation was
  replaced by a mutation of the stored cap. Native high-bit context tests use
  the signed-32 seventh parameter; the channel parameter is genuinely u8.
- Callers: each original parent completes 3,456 cases per stream with 1,152
  connected target executions. Both full instruction streams agree, and the
  child is checked against its frame-aware semantic reference. Three V0
  poison values leave expiration unchanged; two wrong phase-consumer controls
  change expiration. No new parent matching credit.
- Actual provider: the complete original 113-word `func_151DBCBC` matches ASM,
  ROM and frozen/live ELF. Its target-applicable randomize-zero arm runs in
  64 cases per stream, reaching the real 14-argument factory call. Vector,
  metadata and the initialized descriptor fields agree; original colour row
  at ROM `0x24FEE3` is pinned. Retained descriptor bytes are preserved rather
  than claimed initialized. The random arm and downstream factory body are
  outside this qualification; the factory is opaque.
- Both scoped padders expose all 212 word corruptions and ten binding
  corruptions. Twenty independent GNU links and 100 guest rebases cover
  helper movement and HI16 carry boundaries. Oversize remains a visible
  generic overflow and is rejected by the generated padder. The complete
  owner checks separately retain the original one-word alignment tail.
- The independent original-ASM image equals the full private and production
  ELF, with exactly 305 changed bytes and zero exclusions. All 189,088
  protected Game-data bytes across 720 owners remain unchanged.
  Production ELF SHA-256: `7039fdf71fd79cad88dc3f03ed00a203cafca924bc012d51cf04daf7e5e946ab`.

| Phase | Elapsed | Tests |
| --- | ---: | --- |
| preinstall-primary | 125.53 s | 5 fresh / 0 reused |
| preinstall-sibling | 101.88 s | 5 fresh / 0 reused |
| installed-primary | 95.049 s | 5 fresh / 0 reused |
| installed-sibling | 199.994 s | 5 fresh / 0 reused |

A final diff check also caught an extra terminal blank line in the C file.
It was removed in both the source and the tools packet; the complete function
body, raw/padded owner and predicted image are unchanged. Prior receipts are
archived under `eof-formatting-fix`. Both installed tools suites were rerun
fresh against the corrected packet before documentation was restored. The
preinstall receipts qualify the equivalent pre-formatting source; installed
receipts qualify the final exact source bytes.

All 20 recorded phase tests are fresh with matching fingerprints across
both tools copies; shared tools-check passes. Unchanged broad suites are
not rerun or reported as fresh. Frozen inputs: 3898;
snapshot entries: 2826. The isolated tools sibling overlay
uses 2220 immutable dependency links and
nine independent task copies, preserving the independently dirty real sibling.

Baseline consumer `ffb68594211a8f5307b8adcc891f4e8137460d95`.
Tools commit `ef9e8316125bf6b76f506da416ce247d66a35ca8`.
Receipts: `conker/build/game-seed-sprite-tick-151934b4-private`.
The historical generated host target is an empty stub; no host transfer,
build, launch or Release change is made. No push, hardware or gameplay
acceptance. Zero Claude calls and no subagents for this function. Scoped graph
retention audits both owner definitions, preserves previous qualification and
old IDs, and observes actual commit-hook termination before publication.
Root README receives aggregate/date rows only. The 85% goal remains active.
