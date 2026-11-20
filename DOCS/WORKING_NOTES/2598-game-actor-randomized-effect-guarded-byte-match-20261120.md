# Note 2598: Actor randomized effect guarded byte match

Date: 2026-11-20. Consumer baseline `60fdb566023e0ba45e93d73c6bf31a040d8d9348`;
tools baseline `0eb259f38314ecdfe7df23e503c527d0fe137ff4`.
Qualified tools commit: `5457be5a5b82a7a5d1700ea461d0b8ca95a20f7a`.

`func_150F97EC` replaces its zero-return placeholder with complete semantic C.
Its **89-word / 356-byte retail body and original 112-byte frame** are now
byte-exact through **28 expected-word/binding guards and one inserted reload**.
The existing O2/g3 compiler profile is unchanged. All 16 owner neighbors,
their bindings and pools remain unchanged.

Fresh production recount: **4,582 / 5,528 (82.89%)** total and
**3,909 / 4,855 (80.51%)** Game, zero address drift, 946 still different.
Init 492/492 and Debugger 181/181 remain exact. **117 more** are needed for
85% at this denominator. The progress CSV and conversion counts remain
unchanged because the old placeholder was already classified as C. The root
README changes only its two aggregate match rows; the wider goal stays active.

## Source and ABI

Owner `conker/src/game/generated_124920.c`, VA `0x150F97EC..0x150F9950`,
ROM `0x126C9C..0x126E00`. The interface is
`void func_150F97EC(struct127 *actor, u8 priority, s32 parameter)`.
The existing actor declaration places its pose-bank pointer at `0x1D4`.
If that pointer is present, the routine transforms a source point through the
selected 64-byte pose matrix, draws three real and two integer random values,
and submits the complete fourteen-argument effect request.

`func_15145EA4` takes pointers to the input and output vector pointers;
its four-argument interface is recovered from the complete retail body and
matched C in `conker/src/game_16EE20.c`. Treating it as a direct float-array
transform would lose the actual ABI. The submission helper `func_15102B38`
uses the established fourteen-argument interface, including signed halfword
kind/channel, unsigned byte duration/priority, and the final 32-bit parameter.
Its original body remains in `conker/asm/12FDD0.s`.

The source preserves unsigned 32-bit random remainders: kind 4..6 and duration
100..255. It reloads `D_80088B50` after the mutable providers. The two source
vectors are verified directly against ROM `0x246708..0x246720`:
`(-124,-8,28)` and `(-170,-8,28)`. Local declaration order retains the actual
112-byte frame and exposed pointer/vector/scale homes without volatile,
artificial padding or physical register bindings.

The sole aligned direct JAL is ROM `0x55DC0` / VA `0x15028910` in dispatcher
`conker/asm/50D80.s`. The bounded caller window loads A0 at ROM `0x55CC0`,
rejects null, loads byte A1 from SP+0x773, passes A2=1 in the call delay slot,
and ignores V0. There is no aligned literal function pointer; computed callers
remain unexcluded. This is static interface evidence, not execution of the
complete large dispatcher.

## Closed instruction derivation

Raw C emits **88 words / frame 112**, with 77 positional linked differences.
Raw payload SHA-256:
`492ac73a2088135f7f3ab134e297afa9abf4e9589b6bc76122f4e9e2efaec5a8`.
The normalizer consumes only that exact payload and binding map; it does not
read ROM or original assembly to generate its output. It retains **all 88
unique source origins**, reorders independent opening address work and derives
the closed GPR role changes. It duplicates the incoming actor-home load at
output word 13, yielding all 89 original words. Moved branches and bindings
follow their source origins. Every FP primitive and operand order is retained.
No frame-size guard or instruction omission is used.

Independent GNU assembly and two distinct entry/code/data rebases match the
complete derived payload and bindings. Changed payload/binding controls are
rejected. Both owner padders reject all 28 expected-word corruptions and every
applicable relocation corruption independently. Their complete padded objects
are identical. Actual Make runs the natural **five-command** mixed GLOBAL_ASM
recipe; the existing assembly neighbor is preserved.

## Fresh validation and limits

The new **five-test suite passes before and after installation in both tools
configurations**. All 338 imported Python fingerprints
agree. The isolated hybrid overlay has 1081 files:
347 matching sibling files,
717 primary fallbacks, 16 task files and
one bootstrap. The actual dirty sibling retains its HEAD, exact status and
351 dependency fingerprints.

- The instruction-driven relation covers both gate paths, visits all 88/89
  words, compares ordered FP operations and opaque full FCSR transitions,
  public read multiplicity and divisors, complete call arguments, saved
  GPR/FPR/SP/RA restoration, and **all 124 private/incoming bytes** at every
  call and return. There are no private-home exceptions. Arbitrary o32
  providers may mutate public state and retain/mutate the exposed pointer
  homes, transformed point and later scale buffer. Eight effective semantic
  controls are rejected; a valid T0/T1 reallocation remains accepted.
- Concrete guest checks cover **768 cases and 4,298 logical helper calls**,
  visit all 88/89 words, and compare all 124 private bytes at every call.
  Complete final memory agrees in all 768 cases. Cases cover all 256 selector
  bytes, full-word unsigned RNG values, parameter boundaries, finite signed-zero
  and subnormal real inputs, and provider mutations between random calls.
- Native SDK32 O0/O2/O3 each pass 768 defined cases with strict aliasing and
  UBSan, complete `struct127`/`struct17` objects and all native buffer objects.
  Three source controls fail as expected. The transform provider initializes
  every position component before it is read, and no retained pointer is used
  after the root returns.

The helper bodies are bounded providers in these execution checks. The relation
assumes mapped/aligned quiet ordinary memory, valid o32 stack, no public/private
alias, implemented FP operations with traps disabled, and providers that cannot
inspect PCs or unpassed private homes. Full matrix/RNG/effect engine execution,
fault/interrupt state, hardware and gameplay acceptance are not claimed.

## Historical images and production audit

The older draw/renderer/unlink image fixtures retain their immutable baselines.
They now select a private linker script only for an exact owner-source/guard
pair, checking the new dependency's source and padded-object hashes plus the
frozen old object's hash. The old object hash is independently equal in all
three historical baseline manifests:
`c0a46d99f9f59bd861514b0baca9814773cfdef8ebbad5071c8c41ac7026722d`.
Live linker/source/object files are never substituted or rewritten by this
helper. Five fresh unit tests check selection, untouched live files, each
fingerprint, duplicate snapshots and absent/ambiguous linker references.

All **three historical image gates run fresh before and after installation in
each tools configuration**, including their complete owner compilation,
padders, actual Make routes and zero-exclusion image predictions. The remaining
20 checks from the previous 23-test checkpoint are explicitly **reused**.
Their 345 imported Python files are unchanged;
AST comparison proves the three altered match modules change only linker
selection, and manifest comparison permits only the appended exact snapshot
and frozen-dependency entry. Raw payload/binding fingerprints, original
headers/profiles and complete padded/image checks remain enforced. These
reused semantic checks are not described as freshly rerun tests.

The production Make and fresh recount pass. The **entire ELF equals the
independent prediction**, with exactly **310 changed bytes and zero exclusions**.
The target body and symbol-size update 12→356 are accounted for separately.
Two exact GNU symbol/string swaps are predicted: `D_800A48C8`/`D_800A03C8` and
`D_800A1C54`/`D_800A5F54`. Named definitions and their section indices remain
unchanged. All 6,051 function slots are retained; Game data is unchanged across
189,088 bytes and 720 owners. All 2171 frozen inputs pass
the explicit task plan. The existing duplicate `generated_12D630` recipe warning
remains; the qualified owner introduces no compiler diagnostics.

Production ELF SHA-256: `62ca30c5bdab794c1789e629262471a1fe626bd5e58c4af3b97f70dd8ca272d8`.

Root README receives aggregate rows only. Graphify receives a scoped AST merge
with old IDs and qualification metadata retained, not a full-corpus extraction.
No host-port, frozen Release, ROM or save changes; zero Claude calls and no push.

Reproduce the focused checks in the prepared consumer:

```sh
python3 -m unittest tools.tests.test_game_actor_randomized_effect_150f97ec_match -v
python3 -m unittest tools.tests.test_game_list_historical_image -v
make -C conker -j4 build/conker.us.elf progress.csv
make tools-check
```

Continue with `func_15035FE8`, owner `generated_61D10`, VA `0x15035FE8`, ROM
`0x63498`: **88 words / frame 104**, currently a zero-return placeholder.
Its complete retail body has a byte-count gate, three graphics-state commands,
a 12-byte record loop, skip byte and eight-argument `func_1502CCFC` submissions.
The caller in `game_45B80.c` currently uses an untyped integer interface; recover
the Gfx cursor and view interface together and prove the caller owner unchanged.
This is an inspected next target, not an adopted or credited recovery. Preserve
the older handwritten/shared-entry boundary findings from Note 2597.
