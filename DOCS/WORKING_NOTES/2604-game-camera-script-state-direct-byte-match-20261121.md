# Note 2604: Camera-script countdown direct byte match

Date: 2026-11-21. Consumer baseline `21dee5e30517e2c57dbeb1da25f07880828ba6bf`;
tools baseline `57b6b6a8c044c1fd00ddcc195141e4a0da990d00`.
Qualified tools commit: `0b07aef51228f96f9a78158186e0731f41865965`.

`func_15125C40` replaces its zero-return placeholder with its complete camera
countdown and script-event body. All **93 words / 372 bytes** emit directly
from semantic C under the owner's existing O2/g3 profile: **zero guards,
insertions or omissions**. The original **40-byte frame**, saved S0/RA and six
relocation sites are identical. The recovered interface is
`void func_15125C40(struct108 *camera)`; the obsolete integer-return declaration
and placeholder comment are removed.

Production recount: **4,588 / 5,528 (83.00%)** total, **3,915 / 4,855 (80.64%)**
Game, zero address drift, **940** still different. Init 492/492 and Debugger
181/181 remain exact. **111 more** are needed for 85% at this denominator.
Converted rows are unchanged because the former placeholder already counted
as C. Root README changes are limited to its two aggregate matching rows.

## Recovered behavior

Owner `game_14FF90`; VA `0x15125C40..0x15125DB4`, ROM
`0x1530F0..0x153264`. A 32-bit local snapshots the unsigned state byte at
camera+0x23E. A byte local produces 94 words; repeated field reads produce
97. Both rejected forms preserve the owner's other functions but fail retail
length and scheduling. The selected 32-bit snapshot produces all 93 words
without changing qualifiers or compiler flags.

The routine decrements the countdown at +0x7CC. States 3 and 26 use its active
path. On expiry it submits command 0x18 for state 26, using the actor's truncated
+0x40 float only when `D_800D1940 == 0x42`. It then sets camera flag 2, linked
flag 0x10 and camera halfword flag 0x10, and resets the countdown to one.
Inactive states clear an existing flag 2 by submitting commands 0x10 and 0x0F,
then reset the countdown to two. The original redundant boolean check remains.
Helper calls may change public state, so post-call flag reads remain reloads.

## Qualification

Raw payload SHA256:
`add03ff0a903c1ccf83e611e9cfdb950354e8b5daa5e24f0bcdf68deaf2c4269`.
Raw C, independently assembled retail and the padded body have identical
payloads and relocation bindings. All **44 neighboring functions**, normalized
constant pools and the five existing compiler warnings are preserved.

The independent guest model passes **21,632 cases per stream**, reaching all
93 words and checking full public RAM, calls, ordered accesses, all registers
and private-frame/incoming storage across retail, raw C and padded C. Inputs
cover all category/state byte values through their relevant partitions,
countdown wrap at INT_MIN, both stack phases, provider clobbers and mutations,
and four linked-halfword overlap arrangements. Four altered instruction
controls fail. The original guest engine permits stack phases zero and eight;
coverage uses its complete fetch set, including branches and delay slots.
The connected fixture counts provider calls separately from outer calls.
These guest cases do not establish FCSR exception, MMIO, interrupt or hardware
behavior; their finite conversion inputs remain within the modeled domain.

Native SDK32 execution uses the actual `struct108` and `struct127` declarations
with strict aliasing and UBSan traps: **76,800 cases each at O0/O2/O3**, with six
effective source controls. These cases use defined separate C objects, exclude
signed-decrement overflow, and restrict float conversion to finite representable
values. They make no native private-frame claim. The target MIPS instruction
identity and guest wrap tests are separate evidence.

The original ROM census finds one direct call at `0x15122F00` in
`func_15122C5C`, with no aligned loaded pointer literals. Its four-word connected
window executes **144 cases per stream** through the real JAL, argument delay
slot, target return, and next call. The result is unused before that next call.
Lost-argument and skipped-call controls fail. The whole outer caller remains
unrecovered; computed references are not excluded by the aligned census.

Six GNU links compare original and rebased code+`0x10010` / data+`0x18020`,
including HI16/LO16 carry. The raw target is isolated from its compiled owner
with exact payload/binding equality before linking; unused raw-owner data is
outside this target-only link scope. The full padded owner is checked by the
natural production route and complete image gate.

The existing mixed GLOBAL_ASM Make route executes all **five actual commands**
and reproduces the complete proposed object. There is no Makefile, guard,
profile or shared-header change. The full-image predictor covers **6,051
slots**, with **292 declared changed bytes and zero exclusions**. Only the
target body and its symbol size, 16 to 372 bytes, change. A scratch-object
basename initially changed STT_FILE metadata; using the production basename
for the identical object resolves that artifact without relaxing the gate.
All **189,088 protected Game-data bytes across 720 owners** remain exact.
Production ELF SHA256: `3a4cbd6cc6154467d01fc473f037610a28dc20312167f8458e6a8cc0b407f10d`.

Primary and private sibling configurations each pass the five focused checks
before and after installation. Shared `make tools-check` passes. This direct
conversion preserves other linked bodies/data/guards, so earlier broad suites
are not rerun or described as fresh. Unchanged neighboring instruction streams
retain their existing semantic evidence; the current whole-image gate covers
the changed dependent object without exclusions. The private hybrid contains
1152 files; the real dirty sibling HEAD/status and
351 dependency hashes are preserved. Seven new tools
files are committed before consumer adoption. Frozen production inputs and
additional original assembly/header inputs are checked before credit.

Graph refresh retains old IDs and qualification metadata. Native extraction's
smaller corpus is preserved fail-closed; the serial scoped merge is not a full
corpus re-extraction. The available host scene configuration consumes binary
code and lacks its configured symbol file; no host parity or runtime claim is
inferred. No host/Release/ROM/save changes, no push and zero Claude calls.
The 85% goal remains active.

```sh
python3 -m unittest tools.tests.test_game_camera_script_state_15125c40_match -v
make -C conker -j4 build/conker.us.elf progress.csv
make tools-check
```
