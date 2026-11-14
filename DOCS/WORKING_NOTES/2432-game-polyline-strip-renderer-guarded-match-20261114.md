# Game polyline strip renderer guarded match

Date: 2026-11-14. `func_151A7D6C` is now installed and byte-exact in
`conker/src/game/generated_1D4E00.c`. This completes the private screen in
[Note 2431](2431-game-polyline-strip-renderer-semantic-screen-20261114.md).
Its complete **373-word / 1,492-byte** body occupies
`0x151A7D6C..0x151A8340`, ROM `0x1D521C..0x1D57F0`, with the original
**0xC8-byte frame** and no alignment tail.

The full semantic routine emits under the unchanged O2/g3 profile.
**216 words emit directly; 157 expected-word guards** preserve retail's
private stack layout, register assignments and independent scheduling.
There are no inserted or omitted operations, compiler-profile changes,
shared-header changes or changes to the other 22 owner routines. The
obsolete placeholder banner is replaced now that this owner's remaining
placeholder has been recovered.

## Source and normalization

The recovered interface and measured local renderer view remain those
documented in Note 2431: output display-list pointer, owner pointer and
signed 16-bit view. Rendering is gated by flag bit two and successful
cached vertex allocation. The routine configures texture/color/rendering
state, forms a camera-facing offset from the endpoint delta and cross
product, then emits four vertices and two triangles per segment.

The normalizer requires the complete raw body SHA-256
`2dbcf5d06e42583aeec00dd7a6ddb273a4888f04e5555c0d5fd1605678331280`
and the original named binding inventory. Its transformations are explicit:

- Twelve stack-offset mappings place the cursor, two three-component
  vectors, camera, magnitude, synchronization byte, last index and
  projection parameter in their original homes. Saved registers, frame
  size, incoming argument homes and existing floating spills stay fixed.
- Three closed temporary-register exchanges cover the vector and vertex
  loop regions. A separate A1/A2 exchange preserves the texture-coordinate
  constant and later command-pointer roles. Floating register fields are
  excluded from the GPR rewriter.
- The two independent ordinary-RAM rendering-table loads regain their
  original order and temporary roles. Their final integer OR keeps
  retail's commutative operand order.
- The two signed-index narrowing instructions move behind four existing
  color/pointer instructions. Every original load/store remains present.

Every resulting word and binding equals independently assembled retail.
All 157 changed instructions have no relocation attached; named call and
HI16/LO16 bindings remain intact. All 373 individual raw-word corruption
controls and one binding corruption control reject changed inputs.

## Expanded qualification

The retail, raw C and padded streams pass **379 independent-model cases**,
covering every body instruction and preserving callee-save GPR/FPR state.
The prior **16 cases through the two authentic indirect caller windows**
and **eight guest buffer-alias cases** remain in the fresh suite.

Twenty additional cases poison incoming argument homes or redirect the
saved last index, escaped vertex cursor and cached camera pointer. The
three redirect modes produce observable changes and agree across all
three streams. **1,299 fired memory-access boundaries** retain the same
public memory, helper calls and helper observations. This compares public
state prefixes; raw private register state, unrestricted aliases and
portable C fault semantics are not claimed.

Native 32-bit C passes **199 cases in each of six profiles**: O0/O2/O3,
each with strict and disabled strict aliasing. Trapping UBSan and float-cast
overflow checks remain enabled, with SSE arithmetic, disabled contraction
and standard excess precision. All nine source controls are detected:
the prior eight controls plus caching the vertex cursor before a provider
changes it through the retained `Vtx **` output parameter.

Both padders pass **12 GNU links across four independent layouts**,
including HI16 carry boundaries. All 22 owner neighbors and normalized
pools remain unchanged. Prior unchanged neighbor receipts remain prior
evidence rather than newly executed suites.

The adjacent updater's native extractor previously used the renderer's
old `s32` stub signature as its end marker. It now finds the updater's
balanced function span. A fresh source compile and **349 native cases per
six profiles**, including seven effective controls, pass in both tools
environments. The updater's production body is unchanged.

Allocation, projection and graphics helper bodies remain modeled providers
in these tests. This does not claim coupled helper execution, unrestricted
nonfinite/FCSR behavior, hardware rendering or gameplay acceptance.

## Production and repository evidence

The original 698 linked objects, 82 headers, source, assembly, retail input,
compiler, layout, conversion rows and guard manifest were frozen before
installation. The independent shadow uses actual Make compile/pad/assemble
commands and the production link script. Actual production then runs:

```sh
make -C conker -j4 -o retail_word_patches.us.csv build/conker.us.elf progress.csv
```

The production ELF equals the independent image prediction. The strict
whole-image comparison accounts for **1,106 changed bytes with zero
exclusions and no symbol/string ordering groups**. Only this function's
body and expected symbol extent change. All **6,051 function addresses**
and **189,088 protected Game-data bytes** remain fixed. Only the target
owner object changes among 698. All **786 immutable input fingerprints**
pass, including all 82 headers. Conversion rows and Makefile are unchanged;
the prior guard bytes remain an exact prefix with precisely these 157 rows
appended.

Production ELF SHA-256:
`70a81048ef2e25866829e0ae2dd03d0ea6e2d4f59719a0286f77898650a0db2f`.

Tools commit **`11f4e21`** retains the normalizer, both padders, expanded
guest/native checks, updater extractor repair and the renamed integrated
matching suite. It passes before installation in 30.129 seconds, after
installation in the mounted checkout in 28.297 seconds, and in the sibling
overlay in 46.436 seconds. Project tool checks also pass:

```sh
PYTHONPATH=. CBFD_CONSUMER_ROOT=. python3 -m unittest tools.tests.test_game_direction_strip_151a7d6c_match -v
make tools-check
```

All eight overlay source files equal their mounted counterparts. The sibling
retains its **2,439 dirty paths** at `ddbdd16`, with identical before/after
status digests. No sibling files are overwritten or committed. No host files
or frozen Release artifacts are changed; the former `64CBFDOGL` path still
contains diagnostic/capture directories rather than a host source checkout.

The scoped Graphify update covers the owner C and eight tools files. Of
60,188 prior node IDs, **60,184 remain** and **four are uniquely relocated**
to the renamed test module/class/method/docstring. No unexplained nodes are
lost. The result has **60,208 nodes / 113,454 links**. This is not a
full-corpus re-extraction.

Fresh production recount: total **4,478 / 5,516 (81.18%)**, Game
**3,805 / 4,843 (78.57%)**, Init **492 / 492**, Debugger **181 / 181**,
zero address drift and **1,038** still different. **211** further total
matches are required for 85%. The goal remains active. The smallest
remaining mismatch in the fresh listing is **`func_150A76F0`**, 32 words,
in `generated_D4450`; qualify it next. Root README changes are aggregate
figures only.
