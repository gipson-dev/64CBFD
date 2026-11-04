# Game animated-quad state update direct match (2026-11-04)

## Outcome

`func_15171FC0` now replaces its zero-return placeholder in
`conker/src/game/generated_19F150.c` with the complete animated-quad state
update. The semantic C emits all 65 retail words directly under both the
owner's normal `-O2 -g3` profile and plain `-O2`, including the original
24-byte frame and all five relocation records. No expected-word guards,
inserted words, omitted words, profile override, or assembly body are needed.

This is source, callback ABI/registry, compact/padded owner, guest/native
execution, strict whole-image, protected-data, production-build, recount, and
graph-retention evidence. It is not gameplay, effect rendering, timing,
allocator/release-system, hardware, save, or PC-port runtime acceptance.

## Recovered behavior and ABI

The function takes one `QuadEffect19F150 *` and has no scalar return. Its
existing, constructor-proven 0x60-byte record layout places signed lifetime,
8.8 fixed-point frame, and signed frame step at `+0x50..+0x54`, followed by
color, image index, and flags at `+0x56..+0x59`.

Lifetimes below `-1` advance one step toward `-1`; reaching `-1` releases the
record through `func_1516972C`. Lifetime zero changes to the terminal `-3`
state, while `-1` is left untouched. Other lifetimes are decremented by the
signed global tick count unless flag bit two is set. The installed subtraction
uses an unsigned intermediate so all 32-bit tick values have defined C
arithmetic while retaining retail's low-halfword store.

The active path adds the signed frame step to the signed 8.8 frame. It indexes
`D_8008CA4C` with the record's unsigned image byte and reads descriptor byte
`+4` as the frame count. Signed division by 256 deliberately truncates toward
zero, matching retail's negative-frame correction before the arithmetic shift.
At or beyond the frame count, flag bit two expires the record to `-3`; without
that flag, the frame clamps to `(frameCount - 1) << 8`.

| Evidence | Value |
| --- | --- |
| Virtual range | `0x15171FC0..0x151720C4` |
| Retail ROM range | `0x19F470..0x19F574` |
| Owner | `generated_19F150`, six neighboring functions |
| Body / retail slot | 65 / 65 words |
| Frame | 24 bytes |
| Bindings | `func_1516972C`, `D_800BE9E4` HI/LO, `D_8008CA4C` HI/LO |
| Registry pointers | ROM `0x230274` and `0x230D04` |
| Natural compact normalized SHA-256 | `0e061335b82db6e05e926b51896c664298eeb5f6ede7f95da7f20cfd9dd3e122` |
| Linked retail body SHA-256 | `0ee78838b31ef96a96d9fdb8845cdcd9fa3324b7ab0feeb9364d5ed4146244b9` |

## Source provenance and naming

The adjacent `Another Source/CBFD-Recompiled` checkout contains the preceding
`19E040` slice and the following `1A0100` slice but no `19F150` source body, so
it supplies no candidate for this function. The recovery is independently
derived from retail assembly, the already exact `func_15171CA0` constructor,
the already exact `func_15171F04` setup wrapper, the existing named
`QuadEffect19F150` layout, and both retail callback registries.

The installed signature corrects the false empty-parameter `s32` placeholder
to a one-record-pointer `void` callback. The concise comment names the two
semantic axes without inventing an unproven gameplay effect name. Three
equivalent typed/condition source forms compile exact under both profiles. A
signed-shift substitute shortens the body to 62 words and differs at 23 retail
positions, while caching the lifetime expands it to 67 words and differs at
63 positions.

## Qualification

The permanent four-test focused suite establishes:

- 4,104 guest cases cover all 65 words, every unsigned image index, signed
  lifetime/frame/step boundaries, full-width tick values, frame counts zero
  through 255, both stack phases, release, decrement, terminal, infinite,
  loop, and clamp routes;
- 32-bit native O0, O2, and O3 each pass 4,096 cases, for 12,288 positive
  executions, while eight independently compiled semantic controls fail;
- both aligned callback pointers are the only retail references, at ROM
  `0x230274` and `0x230D04`; there are no direct JAL sites; and
- all 15 representative active-path root memory-access fault boundaries retain
  their exact instruction and branch-delay context.

Both profiles reproduce the same exact body and relocation map. All five
bindings and six owner neighbors are fixed. The strict 6,052-function image
changes only `func_15171FC0`, preserves every function address with zero
exclusions, and leaves all 189,088 protected Game-data bytes across 720 owners
exact.

The installed focused suite passes all four tests in 36.669 seconds. The
shared match-progress, generated-PC16, guarded-object, and protected-data suite
passes all 19 tests in 8.351 seconds.

## Production closure

The actual Make owner rule rebuilt `generated_19F150`, and the production ELF
equals the independently predicted qualified ELF. The broad `make all` path
linked the image and generated the binary, stopping only at the expected final
retail SHA check. The inherited duplicate `generated_12D630` recipe warning is
unchanged.

| Artifact | SHA-256 |
| --- | --- |
| Qualified / production owner object | `cce81e5463db7c79d6e8643f41792f3be3e2d64ec98c4e8bfe8c1ced9f514aa3` |
| Qualified / production linked ELF | `f6aa912b960e8cdd7a4d4255b8fe726d897d3074fe93a2378cc36f2e62ce1aef` |
| Production rebuilt ROM image | `0232a8da03c4029bdaf578f6806fef1447e23e7e882705b2872921d8a3d08a74` |
| Production map | `2ab021cc02cab424a5dae0e96a4ed5df1fe5f65ea58964f8e4e04b689771fbeb` |
| Installed owner source | `ebaf0839c3bc30a9c6c43af3e87064f0627c1789670b4bcc9c1d8c00e2838087` |
| Guard table | `86559f1ec5fd731636f9ffc1a9960d9fc427cbdc5466bdff7289ea6800f800ab` |
| Retail layout | `67a28e9dfe6bd0dc21e3a386966e69f7507a8e1628dc0f67d46425ac297dadcb` |

## Recount

The fresh production ELF reports:

- Total: **4,144 / 5,512 (75.18%)**, zero address drift, 1,368 different.
- Init: **492 / 492 (100.00%)**, zero drift.
- Game: **3,471 / 4,839 (71.73%)**, zero drift, 1,368 different.
- Debugger: **181 / 181 (100.00%)**, zero drift.

The converted inventory remains 5,512 / 6,046 functions. The active 80%
threshold is 4,410 exact functions, so **266 more** are needed.

## Continuation

Continue the ordinary Game queue at `func_151905BC`, currently a 66-word slot
with 63 real differences. Keep the seven documented handwritten/custom-ABI/
boundary rows (`func_150A76F0`, `func_151F8870`, `func_150A613C`,
`func_150AE280`, `func_15115F68`, `func_151AE2BC`, and `func_150A6760`)
separate until their specific boundaries are addressed. Every ordinary
candidate still requires source/ABI/caller, owner, guest/native, actual Make,
complete-image, protected-data, production recount, documentation, and
graph-retention gates before credit.

## Graph retention

The standard reduced `graphify update .` extracted eight uncached inputs but
proposed only 24,685 nodes against the retained 58,477-node corpus, so
Graphify correctly refused to overwrite `graph.json`. Its fail-closed report
retained 31,816 nodes from 3,754 still-present files outside the reduced scan
corpus. The graph remained byte-identical with SHA-256
`d9042d20f2ca556cf9c50ef31b2414b8badcf56b42824adbd5bd76e32a27a261`.

An explicit ten-path incremental rebuild with `force=False` then produced
58,487 nodes, 112,342 links, and 5,084 communities. Against the saved
pre-change graph, 58,474 / 58,477 old node IDs were retained, including every
ID outside the changed-path set. The three replaced IDs are line-derived
`DOCS/UPDATE_LOG.md` headings, each with its corresponding replacement two
lines later. Thirteen IDs were added: those three relocated headings; the Note
2073 file, title, and seven indexed section headings; and the retained
`QuadEffect19F150` type. The ten-node and seven-link net additions are confined
to the owned changes. This first qualified graph has SHA-256
`af48ce5bf15a8490a2a2c3059e3232f7f67b6a6d9c78624b302199aec2fcc26d`.

After adding this receipt, a one-path stabilization retained all 58,487 prior
IDs and produced 58,488 nodes / 112,343 links with SHA-256
`6f3c78f8a9926262ac4b044472475cbdbd3050373905daa851e6581de84b11ca`.
