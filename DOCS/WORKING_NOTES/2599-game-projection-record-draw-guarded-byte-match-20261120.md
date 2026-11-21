# Note 2599: Projection record draw guarded byte match

Date: 2026-11-20. Consumer baseline `7370fe35f8147790d9e0e4e8d700532c4c4eade0`;
tools baseline `5457be5a5b82a7a5d1700ea461d0b8ca95a20f7a`.
Qualified tools commit: `a0e7ec9cf2bb16436d7f27dedcf802f70576a3d6`.

`func_15035FE8` replaces its zero-return placeholder with complete semantic C.
Its **88-word / 352-byte retail body and original 104-byte frame** now match
through **46 checked guard rows, seven insertions and nine omissions**. The
existing O2/g3 profile is unchanged. Its caller now uses the correct Gfx cursor
and 32-bit view interface; its entire padded object remains byte-identical.

Fresh production recount: **4,583 / 5,528 (82.91%)** total and
**3,910 / 4,855 (80.54%)** Game, zero address drift and 945 still different.
Init 492/492 and Debugger 181/181 remain exact. **116 more** are needed for
85% at this denominator; the wider goal stays active. Conversion rows and the
complete progress CSV remain unchanged because the old placeholder was already
classified as C. The root README changes only its two aggregate match rows.

## Source, packet and caller

Owner `conker/src/game/generated_61D10.c`, VA `0x15035FE8..0x15036148`, ROM
`0x63498..0x635F8`. The recovered interface is
`Gfx *func_15035FE8(Gfx *commands, s32 view)`.

The routine checks the queued-record byte count, emits smooth/shaded geometry,
clears fog/LOD and disables alpha comparison through the SDK graphics macros.
It checks the count again after those public stores, traverses 12-byte records,
skips flagged records, and constructs a four-integer color packet for the
eight-argument `func_1502CCFC` call. It follows the returned cursor and reloads
the mutable count after each call. The second count gate matters when command
storage aliases public count/record storage.

`ProjectionDrawRecord61D10` declares the matrix pointer at 0, alpha at 4, RGB
bytes at 5..7, slot at 8, two reserved bytes at 9..10 and skip flag at 11.
The existing allocator `func_150356C8` receives the same typed array declaration
and equivalent pointer arithmetic. Its raw instructions and bindings remain
unchanged. All nine owner neighbors and pools are preserved.

The helper's existing complete C in `generated_58F80.c` establishes
`Gfx *(Gfx *, s32 slot, s32 view, u8 *matrix, s32 alpha, s32 *parameters,
s32 mode, s32 extra)`. The recovered root passes mode 0 and extra 1. Native
checks use a complete 15-record array, consistent with the allocator's cap.

The sole aligned JAL is ROM `0x46C54` / VA `0x150197A4`, in
`func_150195A0` in `game_45B80.c`. There is no aligned literal function pointer;
computed callers remain unexcluded. Its prototype and call now preserve the
Gfx pointer type directly. All 16 raw caller functions, bindings and pools,
and the complete padded caller object, remain unchanged. Its three preexisting
Warning 712 messages are identical after path normalization.

## Closed derivation and frame

Raw C emits **90 words / frame 104**, with 63 positional linked differences.
Raw payload SHA-256:
`7af2583da5702262721af815370ad4ea9a9121a095c28a96473db49c37e5800e`.
The parameter packet is at SP+0x54, and all five saved-register/RA homes agree.
No frame, parameter-home or saved-home guard is used. The captured red byte
and explicit post-setup count gate are meaningful source values/control flow;
there is no volatile, artificial padding or physical register binding.

The executable normalizer consumes only the exact raw payload and binding map.
It retains **81 unique source origins**, omits source 38..45's redundant initial
limit calculation/test and source 49's alternative increment, and clones seven
existing limit/jump instructions for the skipped-record path. Constants and
the view move are hoisted, GPR roles are derived, and branches, likely delays
and moved relocations follow the recovered control flow. Positional CSV rows
encode that independently verified relation; ROM is not used to generate it.

The removed initial comparison is dominated by a positive unsigned-byte count.
For every c in 1..255, `12*c-1` lies in 11..3059; in a nonwrapping complete
record array, `B+12*c < B+1` is therefore false. The independent lemma checks
all 255 positive counts, 1,275 boundary/rebase combinations, and effective
zero-count/wrapping counterexamples. The dominating guard and nonwrapping-array
conditions remain explicit obligations.

Original GNU assembly and two independent entry/code/data link contexts agree
on all 88 derived words and bindings, including an HI16/LO16 carry. Corrupt raw
payload/binding controls are rejected. Both full target padders agree and reject
all 46 expected-word corruptions plus every applicable binding corruption.

## Fresh evidence and historical reuse

**12 focused tests pass before and after installation in each tools
configuration**: seven new draw tests and five previous actor-effect tests.
All 346 imported Python fingerprints agree. Six historical
dependency tests and all three older list image gates also run fresh in each
configuration before and after installation. The isolated hybrid overlay has
1090 files: 347 matching sibling files,
725 primary fallbacks, 17 task files and
one bootstrap. The actual dirty sibling preserves its HEAD, exact status and
351 dependency fingerprints.

- Independent instruction-driven proof: three prefix and four inductive-loop
  transfers visit every 90/88 instruction. All **112 private/incoming bytes**
  agree at calls and exits, without exceptions. The invariant closes record+12,
  cached count/limit, cursor, packet pointer, view and next skip-byte recurrence.
  Ordered public stores, quiet read multiplicity, all eight call arguments,
  saved GPR/FPR/SP/RA, returned cursor and opaque full FCSR agree. Providers may
  mutate public state and retain/mutate the passed 16-byte packet. Nine semantic
  controls are rejected; a valid T0/T1 reallocation remains accepted.
- Guest checks: **1,080 cases / 4,170 draw calls**, including 48 public-memory
  aliases. Complete final RAM and cursor returns agree in every case, as do all
  112 private bytes at every call. The corpus includes mutable counts, future
  records, matrices, skip flags and packet writes. Native cases use counts
  0..15; eight additional mapped guest cases exercise larger counts through 255.
- Native SDK32 O0/O2/O3 each pass **1,024 complete-object cases** with strict
  aliasing and UBSan. Four source controls fail as expected. Record arrays,
  Gfx buffers and matrix banks are complete real objects; retained packet
  pointers are used only while the root is active.
- **96 connected caller cases / 381 draw calls** execute ten original caller
  instructions, including the JAL delay and subsequent matrix-command stores.
  Those original stores consume the returned cursor correctly. Six-word o32
  setup/teardown trampolines are explicit test infrastructure. Complete RAM
  agrees between raw and retail streams; this is not full-caller execution.
- Actual Make runs three natural commands per owner. The target's complete
  padded object agrees across both padders; the typed caller's layout-padded
  object is exactly its frozen original. No whole `asm/45B80.s` exists or is
  fabricated for the caller route.

Historical images retain their immutable expected bytes. Exact source/guard
snapshots select private linker scripts with one pinned old dependency for the
actor-effect fixture and two for the older draw/renderer/unlink fixtures. Each
live source/object and frozen object hash is checked. The old `generated_61D10`
object hash independently agrees in all four historical baseline manifests:
`3ce3749fe9ce436c166a9882e7c13ecb4ccddf97ba6d48c7d7fe1aabfbb71b27`.
Multi-object selection and a corrupted second frozen object have fresh controls.

The previous **20 other list semantic checks are explicitly reused**, with
344 unchanged imported Python fingerprints and the
prior linker-only AST audit retained. The renderer source-gate change permits
only the exact new source/guard/typed-caller triple; AST comparison proves its
body generation is unchanged. Fresh owner streams, padders, Make and complete
old-image gates remain enforced. Reused checks are not counted as fresh runs.

The relation assumes quiet mapped/aligned ordinary memory, valid o32 stack,
nonwrapping readable record backing and no public/private stack alias. Providers
preserve saved registers and cannot inspect code PCs or unpassed private homes.
Full downstream rendering, faults/interrupts, hardware and gameplay acceptance
are outside these checks.

## Production result and continuation

Production Make and fresh recount pass. The **entire ELF equals the independent
prediction**, with exactly **286 changed bytes and zero exclusions**: the target
body and symbol size 12 to 352 are the only declared changes. No metadata
permutation is needed. All 6,051 function slots remain, and protected Game data
is unchanged across 189,088 bytes and 720 owners. All 2186
frozen inputs pass the explicit task plan. The existing duplicate
`generated_12D630` recipe warning and the caller's three warnings remain;
the restored target introduces no compiler diagnostics.

Production ELF SHA-256: `a266ba46e1e643906a33f0c2cdb72ec550da4b1b6639e9973aede7e0a22ff1b4`.

Graphify receives a scoped AST merge with old IDs and qualification metadata
retained, including correct C definition/prototype classification in both
changed C owners. This is not a full-corpus extraction. Root README receives
aggregate rows only. No host-port, frozen Release, ROM or save changes; zero
Claude calls and no push.

```sh
python3 -m unittest tools.tests.test_game_projection_record_draw_15035fe8_match -v
python3 -m unittest tools.tests.test_game_actor_randomized_effect_150f97ec_match -v
python3 -m unittest tools.tests.test_game_list_historical_image -v
make -C conker -j4 build/conker.us.elf progress.csv
make tools-check
```

Continue with `func_15036148` in the same owner, VA `0x15036148`, ROM `0x635F8`:
**112-word body / 114-word slot / frame 152**. Its original compiler routine
checks a view-state gate and scans 25 actors using activation/category, height
and radius tests, an extent query and `func_15035808` submissions. The height
sentinel is verified at ROM `0x23C834`: `D_80097D74`, word `0xC61C4000`, -10000.
Recover the void/ignored-return interface, three signed-halfword output homes
and complete ten-argument submit ABI before fitting. Its production
body remains a placeholder, with no new credit. Preserve the older handwritten
and shared-entry boundary findings rather than selecting the shortest slot.
