# Init Bitmap Unsigned One-Past Record Fitting

Date: 2026-10-05. Starting HEAD: `661627ce`.

## Result

Continue the concrete bitmap work after
[Note 984](984-init-pause-resume-current-conversion-readiness-20261005.md),
not another inventory-only assessment. Test whether an unsigned one-past
sentinel removes the XOR temporary and whether the existing grouped volatile
view pays for the endpoint arithmetic without another scalar count-address load.

**With unrolling disabled, the grouped candidate emits nineteen body words
and a direct back edge, but sixteen positions differ from retail. Do not
adopt.** Complete standalone text remains eighty bytes, including four bytes
of alignment. Retail increments the cursor in the branch delay slot; this
candidate increments before the branch and stores at `-1(cursor)` in its
delay slot. It also compares against a biased endpoint. Removing XOR alone
does not recover the original three-instruction loop or full tail schedule.

All fourteen new checks pass in 3.587 seconds. The final combined run passes
**154 checks in 72.596 seconds, exit zero, no skips**. Existing Init code/data,
all 47 retained ASM slots and Game data remain retail-exact. This is a
qualified isolated fitting result, not a new production conversion.

## New Source Shapes

Extend `tools/experiments/init_bitmap_ordered.c` with two opt-in shapes:

- Shape 25: captured scalar globals, explicitly volatile pointer/count loads,
  unsigned guest-width addresses and `stop = end + 1`.
- Shape 26: the same unsigned sentinel loop through the existing direct
  volatile record view, anchored experimentally at `0x8003BE70`.

Both use `do { *(volatile u8 *)cursor++ = 0xFF; } while (cursor != stop);`
and retain the signed count reload after filling plus the two-based tail mask.
The unsigned guest word wraps intentionally: an inclusive endpoint of
`0xFFFFFFFF` gives a zero stop value, not an empty range. This differs from
the prior native-pointer one-past trials and their pointer-arithmetic domain.

The guest-width assertion requires four-byte unsigned longs. Compiler-emitted
record layout still measures `(16, 0, 8, 12, 2)`: size, start/count/end offsets
and count width. The grouped type remains experimental, not a recovered
production declaration or original-type provenance claim. Native Shape 26
uses the existing independent host globals, not a host-width recreation of
the guest record layout; guest instructions/layout are qualified separately.

The driver default remains Shapes 1..11. All old Shapes 1..24 produce exactly
the banked preprocessing output in both host/guest selections: 48 checks using
`cc -E -P`, compared first with starting HEAD and then pinned in the new suite.
The experimental record linker symbol is added only for Shape 26, in addition
to the existing Shapes 23/24. No production compiler profile or guard changes.

## Measurements

Cells are body words / differing aligned positions / complete text bytes /
frame bytes. Body includes the return delay instruction. Differences are raw
word-position counts, not instruction edit distance or semantic mismatch counts.

| Shape | O2/g3 | O2/g3 no-unroll | O1 |
| --- | ---: | ---: | ---: |
| 12, unchanged unsigned scalar control | 20 / 19 / 80 / 0 | 20 / 19 / 80 / 0 | 31 / 31 / 128 / 16 |
| 23, unchanged direct record control | 19 / 17 / 80 / 0 | 19 / 17 / 80 / 0 | 31 / 31 / 128 / 16 |
| 25, ordered scalar one-past | 36 / 36 / 144 / 0 | 23 / 23 / 96 / 0 | 36 / 36 / 144 / 16 |
| 26, record one-past | 32 / 32 / 128 / 0 | 19 / 16 / 80 / 0 | 33 / 32 / 144 / 16 |

Default optimized sentinel loops unroll and exceed the retail slot. O1 also
exceeds it. The fitted Shape 26 no-unroll opening and loop are:

```text
addiu a0,v1,1       # captured one-past endpoint
addiu v0,v0,1       # loop begins here
bne   v0,a0,loop
sb    a2,-1(v0)     # branch delay slot
```

Retail instead has `sb t0,0(v0)`, `bne v0,v1,loop`, and `addiu v0,v0,1`
in the delay slot. The new body has no XOR instruction, but it is not a closed
register rename or independent scheduling cycle. No normalization is justified.
Its complete text hash is pinned in the retained receipt as:

```text
273623b5df29fa2f96e0ac5a457af1a6294a0636b080fead846828f3e79ad269
```

## Read-Order Discovery

The initial scalar sentinel source used ordinary scalar-global captures.
Its first paired case failed because optimized code read `0x8003BE7C` before
`0x8003BE70`, opposite retail's start-then-end order. Do not weaken ordered
comparison to final memory equality or qualify only the smaller profile.

The retained Shape 25 explicitly loads both pointer objects and the late
signed count through volatile views. This repairs the experimental access
contract but increases its body by three words in each profile. The initial
unqualified images were overwritten during fresh compilation; they receive
no final corpus credit. The new reversed-read control independently reproduces
the failure boundary: swap retail's opening load pairs, leaving final memory
identical, and require the ordered trace to differ.

## Emitted-Code Qualification

`tools/tests/test_init_bitmap_one_past_record.py` freshly compiles four shapes
in three profiles: twelve objects, six new instruction images. Each shape's
strict native host fixture passes its 79 cases, including repeated calls and
count/end-storage aliases; 158 shape/case combinations belong to new shapes.
Native cases are not proof of arbitrary guest address arithmetic or layout.

The six final new guest images qualify **1098 completed retail/C paired traces
and eighteen bounded prefixes**:

- Existing signed-count/remainder, repeated-call and surrounding-byte cases.
- Captured start/end pointer-storage aliases and the late count-storage reload.
- Wrapped model addresses across zero, plus endpoints exactly at `0xFFFFFFFF`.
- Four-byte and single-byte zero-stop ranges for every tail remainder.
- Existing reversed-endpoint prefixes; a start-zero/end-`0xFFFFFFFF` full-cycle
  case is checked only through its first sixteen stores, not billions of bytes.
- Complete ordered external reads/stores and external memory for completed cases.
- Callee-saved registers, restored SP, actual frame descent and output fences.

The paired count is 1002 existing-domain cases plus 96 zero-stop cases.
Prefixes are twelve reversed-endpoint checks plus six start-zero full-cycle
prefixes. The receipt records all image hashes and an unchanged source hash
during qualification. All six images read only the captured start/end fields
and then the signed count; no unused record field is accessed.

Negative controls reject a hoisted count read, reversed endpoint reads despite
identical final memory, and a false zero-stop early exit. The latter inserts
a local branch guard before the fitted loop and relocates its local branches:
the control produces no stores where the real candidate must fill four bytes.
No defensive empty-range behavior is added to any retained candidate.

The 154-check combined command is Note 981's focused suite plus the new module
and Note 984's two current-byte-depth size/identity checks. It freshly checks
the retained decoder controls and best byte-depth allocation, connected
formatter fixtures, source owners, slots, startup/storage contracts and existing
linked artifact. It does not rerun Note 979's full masked decoder corpora.
Project tool checks, whitespace and checkpoint links pass.

```sh
python3 tools/experiments/compile_init_bitmap_ordered.py --shapes 12 23 25 26
python3 -m unittest tools.tests.test_init_bitmap_one_past_record -v -f
make tools-check
```

Objects, compiler logs, disassembly, layouts and the dedicated
`one-past-record-qualification.json` remain ignored under
`conker/build/init-bitmap-ordered/`. Later suites overwrite generic measurements
but not this dedicated receipt. Tracked source, driver and tests reproduce it.

## Adoption Boundary And Next

- [x] Test a distinct unsigned sentinel/grouped-address interaction.
- [x] Remove XOR in the fitted profile without changing the two-based tail mask.
- [x] Catch and repair the experimental scalar capture order, then requalify.
- [x] Qualify all six final images, zero-stop behavior and three rejection controls.
- [x] Preserve all 48 old preprocessing selections and pass 154 combined checks.
- [ ] Recover retail's store/branch/increment-delay loop and complete nineteen-word schedule.
- [ ] Establish original address/type provenance before any grouped production declaration.

Keep the production ASM owner. Another bitmap trial needs a new explanation
for that delay-slot lifetime; repeating this sentinel/record combination is
not further progress. MMIO still needs its complete eleven-word match; decoder
fitting remains 512 complete bytes over with entry/frame/reservation gates;
formatter connection remains 196 over with interface/placement gates.

Init remains 492 C / 47 ASM entries. The three pre-existing Game experiment
files remain untouched and excluded from this checkpoint. No production
source/relink, README aggregate, full decoder corpus, hardware/gameplay,
sibling source/build, frozen Release, save, ROM promotion or push changes.
