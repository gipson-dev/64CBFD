# Seven-field player status accessor directly recovered

Date: 2026-11-05. Target `func_150859AC`, owner `generated_B21B0`.
Source `conker/src/game/generated_B21B0.c`; original `conker/asm/B21B0.s`.

## Outcome and recovered data views

All eight pre-install checks pass in **127.752 seconds**. The eight fresh
installed checks pass in **106.480 seconds**. Actual Make equals
the independently qualified owner and complete ELF byte for byte.

The complete **68-word / 272-byte** routine emits directly from C with
**no frame, no alignment tail and no word guards**. All sixteen bindings
and seven compact/padded owner neighbors are qualified. VA is
`0x150859AC..0x15085ABC`; ROM is `0xB2E5C..0xB2F6C`. Existing O2/g3
compiler options remain unchanged.

Both incoming arguments are signed halfwords. Their raw 32-bit incoming
words are stored to SP+0/SP+4 before narrowing. A signed slot of at least 255
returns 0 before any table or status access. The seven selectors are:

| Selector | Source | Result |
| --- | --- | --- |
| 0 | `D_800D2340` | Zero-extended 16-bit mask AND the selected bit |
| 1 | `D_800D213C + slot*0x1C` | Signed 32-bit word |
| 2 | `D_800D2140 + slot*0x1C` | Signed 32-bit word |
| 3 | `D_800D2144 + slot*0x1C` | Sign-extended byte |
| 4 | `D_800D2145 + slot*0x1C` | Sign-extended byte |
| 5 | `D_800D2146 + slot*0x1C` | Zero-extended byte |
| 6 | `D_800D2148 + slot*0x1C` | Signed 32-bit word |

Three local 28-byte view types express those load widths and stride without
inventing a complete status-record structure. The mask retains its shared
`s16` declaration and is explicitly converted to `u16` before the AND.
Word-array index multiplication gives the wrong temporary lifetimes; typed
record views recover all retail arithmetic/register words directly.

## Existing switch-pool ownership

The compiler produces a 32-byte private pool: seven R32 text targets at
function offsets `0x4C,0x64,0x80,0x9C,0xB8,0xD4,0xF0` and four zero
alignment bytes. Every byte and target owner/offset is checked. This pool
is consumed by the existing generated-owner padder; it is not linked as a
second data table. The new Make binding maps compact `.rodata` offset zero
to **`jtbl_8009D9A0`**, whose existing retail pool is ROM `0x242460..0x242480`.
All seven case pointers and the zero padding word remain unchanged.

The earlier setter's `jtbl_8009D970` stays in the same protected data owner.
If `func_15085710` is later reconstructed as a switch, re-audit which table
occupies compact pool offset zero and update the owner binding accordingly.
The current accessor's pool fingerprint will reject an unnoticed pool move.

## Caller interface and complete owner checks

A complete aligned retail census finds **40 direct calls across 15 owners**,
with no aligned target-address literals or direct tail jumps. Original ROM
words and available original caller assembly are frozen. The shared header's
guessed `(s16,s32)` declaration is corrected to **`(s16 slot,s16 field)`**.
Local declarations in `generated_5D2C0` and `generated_B3020` are corrected;
`generated_215960` receives the same explicit prototype.

All fifteen caller owners compile before and after those repairs against
separate private copies of the old/new shared header. Both the normal and
no-unroll profiles of `generated_B3020` are included. The resulting sixteen
profile comparisons preserve **507 function bodies/bindings**, representing
434 distinct owner functions. Every allocatable non-text section is compared
with its R32 targets canonicalized by actual section/function ownership.
Private object metadata is not substituted for that proof. Actual production
Make additionally preserves all **fifteen complete caller object files**.

All forty original JAL/delay-slot boundaries are connected to original,
natural and padded target instructions: **200 cases per body** cover caller
stores, signed-halfword/unsigned-byte loads, immediate selectors and register
moves. The actual four-word HUD window at `0x151E9868` adds **36 cases per
body**, proving its zero-result branch consumes the signed status-byte
result correctly. Complete parent-renderer/gameplay behavior is not claimed.

## Semantic qualification and explicit language domains

The eight-check suite records:

* **1,488 guest cases per body** qualify all selectors, signed slot/selector
  boundaries, raw argument homes, word/byte signs, high incoming words and
  both stack phases against an independent read-only contract.
* **131,072 original/padded sweep cases** cover every slot halfword and every
  selector halfword with noncanonical upper words. Invalid selectors preserve
  the incoming V0 in the emitted retail instructions.
* **84 home/data aliases** and **twelve fired access-prefix cuts** compare
  complete registers, RAM and ordered traces across all three bodies. A
  clipped slot also completes with the entire switch table and data unmapped.
  These are guest instruction observations, not native C stack-alias or
  hardware-MMU acceptance.
* **Nine independent GNU links** exercise three text/data/table layouts and
  all sixteen binding carry edges, with 24 cases per body. The checked compact
  pool's two references are projected to the named retail table for these
  independent links, exactly as the consumer padder does.
* Native32 O0/O2/O3 pass **16,153,968 positive executions**, with typed and
  direct calls, all 65,536 mask values, all byte values and distinct word
  patterns. UBSan remains enabled. Nine native and twelve separately compiled
  IDO controls reject wrong clipping, mask extension/bit, field anchors,
  byte signs, argument widths and the emitted invalid-selector result.
* All 272 raw-byte corruptions, sixteen bad bindings, 32 private-pool byte
  corruptions, seven pool relocation corruptions and eleven full-image
  corruptions are rejected. No guard row is introduced.

Native checks deliberately use the source language's defined domains:
mask-case shifts 0..31, record slots 0..254 in allocated typed fixtures, and
clipped slots 255..32767 with every tested selector. The native fixtures use
separate field anchors; actual shared retail storage/home aliases are tested
in the guest model. Other unclipped selectors have no specified C result,
and invalid native shift counts/out-of-object record pointers are not
claimed portable. Their emitted N64 instructions are nevertheless compared
and exercised, including the hardware shift's low-five-bit rule and retained
V0. This preserves the original routine rather than inventing a default
zero result. No host-port acceptance is added.

GCC reports its expected single `-Wreturn-type` warning for the source's
unspecified selector path. The native harness permits only that diagnostic
with `-Wno-error=return-type`, checks its exact warning class, and retains all
other `-Werror`/UBSan gates. None of the native executions enters that path.
The production IDO owner adds no compiler diagnostic.

All **67 reachable words** are visited. The duplicate bounds instruction at
`+0x2C` follows the early return and is unreachable from the entry; its word
is still statically byte-exact and corruption-checked. Caller-fixture fixes
map the actual high caller-local store offsets, explicitly bind the checked
`.rodata` reference for GNU links, and give the unsigned-byte negative control
an effective 0xFF witness. No production body change was needed for those fixes.

The nineteen fresh padder, relocation, matcher and protected-layout checks
pass in **11.045 seconds**, and `make tools-check` passes. Unchanged caller/
neighbor suites are reused through complete code/binding/data identity, not
claimed freshly executed. Routine work uses zero Claude calls and the
documented IDO/GNU path under the existing REA MIPS-adapter limitation.

## Frozen inputs and production image

The immutable snapshot contains **140 files**, including all headers, target
and caller sources/objects, original available assembly, the complete retail
input, protected switch-pool source, Makefile, layout, guard manifest, linker,
ELF, code binary, progress and graph. Qualification artifacts remain in
`conker/build/game-player-status-accessor-150859AC-match/`, with adjacent
source screens. Source newline styles and every guard byte are preserved.

All **6,052 function addresses** stay fixed; only the target body changes.
All **189,088 protected Game bytes across 720 owners** remain exact. The
literal full-file prediction accounts for **318 changed bytes**: 222 in the
target/symbol extent and 96 in four closed named GNU symbol/string swaps.
The pairs start at file offsets `0x2A796C`, `0x2B668C`, `0x2C98CC`,
`0x2D7C3C`. Each symbol's value, size, type, visibility and section is copied
unchanged except the declared target-size 12-to-272 update; only pair order
and derived name offsets change. There are **zero excluded bytes**.

| Artifact | SHA-256 |
| --- | --- |
| Natural target | `1ed345c0c1cf006446afb25619e3a68cc4e2ad547f928a466a01c6372dd70bfe` |
| Retail target | `79a2ee6a2d895bb5d251e23f34f0a77d4ddb4cfd136fa09f91d8075245e18731` |
| Frozen predecessor ELF | `cb8850d1e353bf3ac38ebcc8ed36d7852472aa46f11eb6f1d98aaa53a6e36b90` |
| Production padded owner | `8f43f0e2ab83dda607ae52cf5a1ee08bd6ec681c176305b5e4fe98e38711f4ec` |
| Production complete ELF | `b64005a3ff94807627d9ab64a9793ab03814e9105d27b102120db133eb334895` |
| Production code binary | `595df79e830b341afa34db8d255a529933ad99a90e7362c5a1d27d75d3965b94` |
| Unchanged guard manifest | `98c78a54647943d6bad989031ecb0256e24cf2247923f8fd992118dc7ba00810` |

Actual Make performs its broader rebuild through the existing Makefile
dependency. The inherited duplicate `generated_12D630` recipe warning
remains. `make -C conker all` produces the binary and returns 2 only at the
expected overall retail checksum mismatch for the incomplete decompilation.

## Baselines, progress and continuation

Main baseline is `6d7698e076cb2c1381466a961860e905cb38c4d2`; mounted tools
baseline is `21f0a0d0fc5646dd37f3028eca83a2b015fb4810`. Both start clean.
The sibling tools checkout is untouched; its last recorded checkpoint is
`ddbdd16b53ce60b054fb6e11bf0649a41f48375a` with six tracked edits and 2,428
untracked files. No fresh sibling qualification or frozen Release change is
claimed.

The fresh actual-ELF recount reports:

| Section | Byte-exact / converted | Match | Drift | Different |
| --- | --- | --- | --- | --- |
| Total | 4,173 / 5,512 | 75.71% | 0 | 1,339 |
| Init | 492 / 492 | 100.00% | 0 | 0 |
| Game | 3,500 / 4,839 | 72.33% | 0 | 1,339 |
| Debugger | 181 / 181 | 100.00% | 0 | 0 |

Converted inventory remains 5,512/6,046; root README changes aggregate rows
only. The 80% threshold is 4,410/5,512, leaving **237 more** exact functions.
Fresh ranking selects **func_150A70C0** next. Keep `func_150A76F0`,
`func_151F8870`, `func_150A613C`, `func_150AE280`, `func_15115F68`,
`func_151AE2BC` and `func_150A6760` as separate documented boundary cases.
Keep the wider 80% goal open.

Mounted tools are committed first as
`271aa0867e4ab141c5be886a9add28f25fed2242`
(`test(game): qualify direct player status accessor`). The consumer records
that pointer with the typed C, corrected declarations, existing-pool binding
and documentation. No guard manifest change is included.

The ordinary AST-only Graphify update refuses its smaller 24,955-node
replacement, preserving the existing 58,748-node graph. The twelve-path
scoped refresh retains 58,745 old IDs, removes three relocated update-log
IDs and adds thirteen IDs, including eight note nodes. Each removed node
has a unique replacement with the same label and source path; **zero nodes
outside changed paths are lost**. The graph is **58,758 nodes / 112,523
links / 5,133 communities**, SHA-256
`c56fccb0b69948bc5293e50e20cb37351c7bcfae7038b1afbbe986b66e9c8124`.
The 31,816 nodes retained from 3,754 files outside the current scan corpus
are preservation evidence, not fresh full-corpus extraction. No force
overwrite is used. The final receipt paragraphs add no headings; a final
scoped refresh verifies unchanged topology.
