# Game radial ground emitter direct match

Date: 2026-11-14. `func_151A9834` replaces its zero-return placeholder in
`conker/src/game/generated_1D4E00.c`. Normal O2/g3 emits all 102 body
words directly, with the original 0xB0-byte frame and no diagnostics.
The complete slot is `0x151A9834..0x151A99D0` (ROM
`0x1D6CE4..0x1D6E80`): body end `0x151A99CC`, followed by one original
zero alignment word. Both body and alignment are checked. There are no
new guards, inserted/omitted operations, compiler-profile changes or
guard-manifest edits.

The complete recovered interface is:

```c
void func_151A9834(f32 *origin, f32 minimum, f32 radius, HeightResult71820 *ground,
    s32 count, u8 selector, u8 *tag, u8 channel, s32 context);
```

A NULL ground result selects a local 36-byte fallback. The routine sets
its height from `D_800A8F68`, metadata/value to zero, flags to seven and
state to zero, retaining the original untouched fields/padding. It copies
the origin height to its working point before the count check, including
for nonpositive counts. Positive bursts snapshot `D_800A8F6C` once.

Each iteration draws two samples in explicit order. The first supplies
`(sample + sample) * angularScale`; the second supplies `sample * radius`.
The existing plane helper writes x/z offsets. The routine then adds the
live origin x/z values and queries the ground with the saved minimum.
The working height persists across helper-visible changes and iterations.
A nonzero full-word query result submits the post-query x/z and resolved
ground height through the freshly read callback table. Tag pointer,
unsigned channel and full context are forwarded unchanged.

The callback's ground pointer uses the existing 32-bit integer slot,
matching the current `func_151DBBD4` interface. The two retail table entries
at `D_8008FA60` are `func_151DBBD4` and `func_150DF4B8`. This recovery
qualifies their calling interface; it does not newly qualify their bodies.

The prepared-image scan finds exactly three direct call instructions,
at ROM `0x10C94C`, `0x164394` and `0x1FD484`. Twenty-four cases execute
the original caller windows at `0x150DF468..0x150DF4A4`,
`0x151CFFAC..0x151CFFDC` and `0x15136EC4..0x15136EEC`, then the entire
recovered callee. They check all nine arguments, actual float-register
transfers, outgoing byte/context stores, caller stack placements, both
tested stack phases and helper-visible mutations. The windows do not
qualify the upstream random-choice logic or complete caller lifecycles.

Guest validation passes 775 independent-model cases against retail,
raw C and padded streams, exercising every body instruction. Cases cover
nonpositive and positive counts, provided/default ground results, hit
patterns, full-word query returns including 0x100 and 0x80000000, poisoned
upper byte-argument bits, signed/zero radii, callback changes after the
query, mutable origins and persistent working heights. Twelve additional
guest-only alias cases place the origin in caller stack storage or overlap
the working point/ground result. Raw and retail machine states agree at
206 fired modeled memory-access prefixes.

Sixteen coupled cases execute the original 22-word `func_1514373C` plane
helper, whose current production body and bindings are independently
checked against ROM. Its sin/cos providers remain deterministic stand-ins.
The general ground-query and effect-callback providers also remain modeled;
real terrain, callback internals, nonfinite/FCSR, unrestricted C aliases,
hardware and gameplay are outside this qualification.

Native 32-bit C passes 391 cases in each of six O0/O2/O3 and
strict/no-strict-aliasing profiles with trapping UBSan, SSE floating point,
disabled contraction and standard excess precision. All seven defined
source controls are detected: resetting working height, missing angle
doubling, using the wrong radius sample, snapshotting the origin before
helpers, truncating the query return, using the wrong submitted height,
and snapshotting the callback before the query. Fixtures use typed,
aligned, disjoint objects. Native checks compare initialized ground
members rather than indeterminate fallback fields or padding.

Both padders pass 12 GNU links across four independent code/data layouts,
including HI16/LO16 carry boundaries. All 22 owner neighbors and normalized
pools remain unchanged. An EOF-only whitespace cleanup was separately
checked: all 23 functions and pools remain identical, and the complete
padded object is byte-identical. Only raw `.mdebug` serialization differed;
the existing padder drops that section. No new image exclusion is used.

Production uses the existing compiler, padding and link rules with the
697 frozen neighboring objects:

```sh
make -C conker -j4 -o retail_word_patches.us.csv build/conker.us.elf progress.csv
```

The production ELF equals the independent shadow prediction. The strict
whole-image audit accounts for all 409 changed bytes with zero exclusions.
Three closed symbol/string serialization changes are accounted for:
the following first and third groups rotate left by one, and the middle
pair swaps:

```text
D_800A8F68 D_800A8B18 D_800A82E8 D_800A4118 D_8009F778 D_8009BB18 D_800A0068
D_800A6BA8 D_80098D28
D_800A8F6C D_800A8B1C D_800A82EC D_800A006C D_8009FC6C D_8009F77C D_8009BB1C
```

Every one of these 16 named definitions retains its value, size,
type/binding, other field and section index. All 6,051 function addresses
and 189,088 protected Game-data bytes remain fixed. Only the target owner
changes among 698 objects. All 787 immutable input fingerprints pass,
including 82 headers, the compiler, retail assembly/input, conversion
rows and unchanged guard manifest. Prior unchanged neighbor receipts
remain prior evidence.

Tools commit `8453c2f` retains the installed suite. It passes in the mounted
checkout and isolated sibling-tools overlay; `make tools-check` also passes:

```sh
PYTHONPATH=. python3 -m unittest tools.tests.test_game_radial_ground_emitter_151a9834_installed -v
```

The sibling retains its 2,439 dirty paths at `ddbdd16`, with identical
before/after status digests. The scoped fail-closed Graphify refresh retains
all 60,150 prior node IDs and reports 60,150 nodes / 113,366 links. It is
not a full-corpus re-extraction. No host files or Release artifacts were
changed. The prior `64CBFDOGL` path contains diagnostic/capture directories,
so no host source/build/runtime comparison was attempted.

Fresh production recount: total **4,477 / 5,516 (81.16%)**, Game
**3,804 / 4,843 (78.55%)**, Init **492 / 492**, Debugger **181 / 181**,
zero address drift and 1,039 still different. **212** further exact total
functions are needed for 85% at this denominator. The goal remains active.
Next screen: `func_151A7D6C`, the remaining placeholder in this owner.
Root README contains aggregate figures only.
