# Owner-linked effect constructor and payload matched directly

Date: 2026-11-10. `func_151B4CD0` replaces its zero-return placeholder with
the complete owner-linked effect constructor: **95 words / 380 bytes**,
original **0x58 frame**, **zero guards**. All instructions emit directly from
semantic C with the existing O2/g3 profile and original helper calls.

Fresh production-ELF recount: **4,320 / 5,513 (78.36%)** total; Game
**3,647 / 4,840 (75.35%)**, Init **492/492**, Debugger **181/181**.
Zero address drift; **1,193** different. **91 more** accepted matches reach
4,411/5,513 and the active 80% goal. Conversion CSV and converted-byte counts
remain fixed. The root README receives aggregate table edits only.

Baseline consumer `747a5593f9c801b0fbacad989f39d44510b40b0b`, tools
`0d055a93c5fffffc92062d5b87586c77b0ba8ab5`, from
[Note 2250](2250-game-view-background-and-split-borders-direct-match-20261110.md).
Bank eight proof files first in tools commit `783ba489c1032f4fedd79f890a11d56e304415f5`. Local commits only.

## Semantic routine and actual caller

Owner `conker/src/game/generated_1E2180.c`; complete original retained in
`conker/asm/1E2180.s`. Retail VA **0x151B4CD0..0x151B4E4C**, ROM
**0x1E2180..0x1E22FC**. The old 12-byte stub differed in 94 retail-slot words.

The recovered semantic interface is:

```c
void *func_151B4CD0(u8 *owner, u8 selector, s32 category);
```

The sole direct call is ROM **0x1C1C28**, VA **0x15194778**, in
`func_151945CC`. Its complete four-word final call window passes owner from
S0, selector **0xFF** and category **1** in the JAL delay slot. There are no
aligned literal pointers to the target. Tests retain the returned factory
pointer and register/stack state at the continuation. The larger caller is
still a zero-return placeholder and is not newly qualified.

The routine returns null for a null owner, classifier result 99, or descriptor
class byte 2. The classifier is `func_15134070(owner)`, and its result selects
the byte at **D_800A3FE6 + type*16**. Real classifier execution covers all 256
actor identity bytes and its complete two-table mapping to types 0..19/99.

For accepted owners, notify `(40, owner, 22)` through `func_1516962C`, then
construct the 48-byte descriptor below. Owner identity and scale are read
after notification. Flags are assigned before the RNG call. The unsigned
random result is reduced modulo 21 and offset by 40, producing duration
40..60. Re-read the descriptor class after RNG to choose payload 1 for class
1 and 0 otherwise. The first class filter and later payload read are distinct.

| Descriptor offset | Field / value |
| --- | --- |
| 0x00, 0x04 | zero words |
| 0x08 | live owner byte +0x3B |
| 0x0C | owner pointer |
| 0x10 | attachment 2 |
| 0x14, 0x18, 0x1C | float vector `(0, -27, 16)` |
| 0x20 | float 15 |
| 0x24 | raw float D_800AA3D0, retail approximately 0.448 |
| 0x28 | signed16 duration `(u32)random % 21 + 40` |
| 0x2A, 0x2B | flags 6, kind 8 |
| 0x2C, 0x2D | signed callback -1, mode 7 |

Submit through `func_1513418C(&descriptor, 1, selector, category)`. If a
record is returned, copy the live one-byte payload to result+0x58 using the
real `memcpy` call. Preserve the original returned record across that copy.
Null allocation and constructor rejection both return null without copying.

The local typed descriptor matches the independently recovered owner-effect
layout in neighboring modules. Native static assertions check its 48-byte
size and field offsets. Its eight unspecified representation bytes are
**0x09..0x0B, 0x11..0x13, 0x2E..0x2F**. Source does not clear or invent them.
Guest tests compare every seeded byte; native tests neither read nor assert
the padding. Physical parameter-home and private payload mutations are
qualified only as emitted guest behavior, not portable C helper effects.

## Direct compiler shape and complete image

The initial semantic body emitted 92 words/frame0x58. A bounded eight-form
screen recovered the exact 95-word body using an explicit payload conditional,
a one-byte payload array and the original flags-store position before RNG.
The array preserves payload **SP+0x20**, rather than a scalar's last byte at
SP+0x23. Descriptor is **SP+0x24**, classifier result **SP+0x1C**, saved factory
result **SP+0x54**, RA **SP+0x14**. Incoming owner/selector/category homes at
entry SP/+4/+8 are reloaded at their original boundaries.

Raw target SHA256:
`c3f01171ee87995283456007e0f57acf3699c57b0a4a7952740dd4ec50289fc2`.
All **11 relocation bindings** remain explicit, including `memcpy` at
0x10022EC0. No inserted/omitted instructions, guard changes, profile edits,
opaque target assembly or data-pool changes.

Freeze **2,268 input fingerprints** and retain exact mutable pre-adoption
inputs. Five actual Make commands include asm-processor preprocessing and
postprocessing, IDO compilation, generated padding and assembly. Independent
whole-owner compilation agrees. All **five other functions**, including the
remaining GLOBAL_ASM routine, preserve code and bindings; pools and zero IDO
diagnostics stay fixed. The owner GPR mask gains V1; independent and actual
Make masks agree. Shared headers, Makefile, profiles, layout, conversion CSV
and the complete previous word-guard file remain unchanged.

The strict whole-ELF prediction accounts for **316 changed bytes**: target
body, symbol extent **12 -> 380**, and two closed two-symbol/string metadata
permutations. Every named definition is checked. **Zero exclusions**; all
**6,050 function addresses** remain fixed. All **189,088 protected bytes /
720 data owners** remain exact, SHA256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

## Qualification and limits

- **622 guest cases / 1,244 executions**, all 95 words visited, complete
  memory/register/access-trace equality, all 48 packet bytes, live class and
  owner/scale reads, unsigned RNG extrema, selector/category widths, null and
  rejection paths, result aliases and private-home/payload stress cases.
- **412 native SDK32 cases** at `-O0`, `-O2`, `-O3`, each matching **586,724
  public/defined-packet/call bytes**, with strict aliasing and UBSan. Native
  logs normalize only private stack addresses; guest checks use literal homes.
  Raw float constants are seeded by bytes so the test fixture does not quiet
  signaling NaNs through an x87 float-return conversion. Source carries raw
  scale bits without arithmetic. Padding is not read in native observations.
- **21 effective compiled semantic controls**, each with a normally completed
  witness and zero earlier execution errors. Private addresses and padding
  are normalized in comparisons, so frame movement alone is not a witness.
- Both padders, **106 word/binding corruption checks**, **16 GNU linker
  comparisons** across four independent low-half symbol sets, **64 rebased
  executions**, and **119 literal instruction-access-cut pairs**.
- **96 real direct-caller pairs**, covering all four call-window words and
  owner/null/filter/allocation/mutation cases. Parent recovery is separate.
- **448 connected-helper pairs** execute the actual classifier, notification,
  64-bit RNG, constructor and byte-copy code. All **183 helper words** are
  checked against current ELF, **181 helper words** are visited. Both real
  classifier tables and all twenty descriptor-class records are loaded from
  the protected image; all 256 identities and twelve RNG seeds are exercised.
  Independent seed evolution, descriptor bytes, factory validation/rejection,
  reciprocal state and final payload copy agree. Allocator, notification
  dispatch, deletion and matrix transform remain explicitly modeled providers.
- Eight complete-image corruption probes, closed live-input/guard checks,
  protected-data audit and complete-address comparison finish the focused suite.

Each environment passes eight fresh pre-install methods and, after source
installation, two fresh methods plus six exactly fingerprinted semantic
reuses. Shared tool smoke is fresh; three unchanged helper regressions per
environment are explicitly reused. The sibling's **2,434 existing dirty paths**
are preserved. It runs target wrappers through a private overlay with recorded
read-only fallbacks; actual Make uses the mounted CLI. This is not a clean
standalone-tools-clone claim.

Production Make agrees with the independent ELF and binary prediction; fresh
progress succeeds. Existing whole-ROM checksum exit2 and duplicate
generated_12D630 warnings remain expected. ELF SHA256:
`cbb877571cc11f9a03de8848b4bb9b85ec37f3e5a94fa269ddc6fd471052bf15`. Binary SHA256:
`75473794d5a5995dc5bffaacb6d05134d14bfa531710d25a99800e98a505168c`.

Codex is the sole writer; zero Claude calls. No push, installation, account
change, host-port edit, save mutation or Release build. FCSR, hardware,
portable padding values, private-home C effects, full caller and gameplay
remain outside this proof.

## Graph and continuation

Scoped Graphify refresh retains or relocates all 59717 old
nodes, producing 59717 nodes / 113103 links.
Outside-scope definitions remain fixed apart from community metadata. All
five C positions and the retained assembly reference are checked. Historical
excluded nodes remain; this is not full-corpus extraction. Post-commit receipts
separately check heading moves and actual graph-worker completion.

```sh
python3 -m unittest tools.tests.test_game_owner_payload_effect_151b4cd0_match -v
make -C conker match-progress NON_MATCHING=1
```

Reproduction requires the prepared PSBBN consumer and retained mutable inputs
under `conker/build/game-next-151B4CD0-match/frozen/`. No private ROM/ELF is
committed.

Next: **`func_15000940`**, 96 words/frame0x28,
in `conker/src/game_2DDF0.c`. Its 12-byte stub differs in
95 retail-slot words, remains unchanged and uncredited.
Inspect its complete original and actual caller/helper contracts first.
Keep the 80% goal active.
