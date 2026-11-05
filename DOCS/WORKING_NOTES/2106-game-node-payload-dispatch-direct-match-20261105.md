# Filtered node payload dispatcher directly recovered

Date: 2026-11-05. Target `func_1514D3B0`, owner `generated_179F30`.
Source `conker/src/game/generated_179F30.c`; original `conker/asm/179F30.s`.

## Result and recovered contract

The complete **66-word / 264-byte** routine emits directly from semantic C
with **frame 0x38, five bindings and zero guards**. Its VA is
`0x1514D3B0..0x1514D4B8`; ROM is `0x17A860..0x17A968`. All **77 compact
and padded owner neighbors** remain unchanged. Existing O2/g3 options,
the original assembly, layout and every inherited guard byte stay fixed.

The recovered interface is
`s32 func_1514D3B0(u8 *owner, s16 root, s32 first, s32 second)`.
The list head is loaded once from owner+0x2F4. Each node uses the existing
`GameListNode` layout: opaque payload word at +0x10, next at +0x14 and
signed identifier at +0x1C. Unknown payload meanings retain their existing
offset-based names.

1. An identifier equal to the signed root bypasses recursive searching.
2. Otherwise, search starts from `D_8008ABE8[root][2]`, using the already
   exact `func_1514D4B8`. That helper searches ordered link 3 before link 2;
   no speculative child/sibling interpretation is added.
3. A selected node's identifier is reloaded after searching. Its metadata's
   first signed halfword selects a callback in `D_8008AB64`. Only -1 skips
   dispatch; other invalid indices retain the original invalid-access behavior.
4. The callback receives the payload and both complete 32-bit forwarded words.
   Its result becomes a boolean, replacing the preceding result. Thus this
   routine returns the **last invoked callback's boolean**, not an OR of all
   successes. A skipped node preserves the previous result; an empty list
   returns zero.
5. The next pointer is reloaded after helper/callback activity. Live changes
   to identifiers, payloads, links, metadata and callback entries are observed.

The explicit unsigned -1 comparison retains retail's commutative BEQ operand
order. The signed source comparison was semantically equivalent but reversed
one instruction's operands; no guard is used to hide that difference.
The saved S0..S7 roles, RA, incoming raw root home and 56-byte frame match.

## Interface and caller preservation

The former shared declaration incorrectly returned void and narrowed the
forwarded words to bytes. `functions.h` now declares the recovered result,
owner pointer, signed root and full-word arguments. The two wrappers in
`generated_F2820.c` receive a local prototype and explicit owner-handle casts.
The owner cast in `func_15079390` removes exactly one existing Warning 712.

That already exact caller still loads three unsigned source bytes. Its two
forwarded locals become s32 so the corrected prototype preserves the original
register allocation. Leaving those locals as u8 changed four address-base
register fields; widening them restores all eighteen words and bindings.
The source byte loads and values remain unchanged.

A full aligned ROM census finds **six direct calls across four owners**, no
tail jumps and no aligned function-address literals. Private compilation
preserves all **245 functions** in those caller owners: game_A28B0 211,
generated_11A680 8, generated_50D80 11 and generated_F2820 15. Their entire
production objects are byte-identical to the frozen predecessors.

The actual callback table at ROM 0x22F624 contains eight handlers followed
by three NULL words. Its 44 bytes are checked against the linked ELF and
the original ROM. The separate preceding destructor table is not conflated
with it. The actual thirty-slot metadata table contains 28 non-NULL prefixes
and two NULL entries; all original pointer/prefix bytes remain exact.

## Fresh qualification

All **seven pre-install checks pass in 93.305 seconds**; all **seven installed
checks pass in 95.856 seconds**. The installed run also verifies the explicit
callback table and rejects the old zero-return placeholder. Evidence includes:

* **1,276 guest cases per body**: 490 synthetic/boundary/mutation cases,
  all 784 actual root/node combinations through this dispatcher's starting
  links, and two connected original leaf-callback cases. All 66 target words
  are visited. Both stack phases and noncanonical incoming root words are
  included. The original 43-word recursive helper executes directly; the
  original six-word `func_1514EB8C` callback also executes and writes its
  three incoming argument homes. Other callback implementations remain opaque.
* Independent expected results, call order and public memory cover last-result
  replacement, -1 skips, equality bypass, full-word arguments, identifier/
  payload changes after search, next-pointer redirects, live metadata and
  callback changes, and the snapshotted owner head. Helpers clobber caller-save
  GPR/FPR state, HI/LO and all four outgoing argument homes.
* **178 fired access-prefix cuts** compare complete registers, RAM, ordered
  accesses, calls and PC/delay context across original, compact C and padded C.
  Three sparse signed root entries alias existing metadata. Seven invalid
  root/callback cases retain faults, including the three actual NULL callback
  slots. Two bounded list/recursive cycles preserve looping and recursive
  stack growth. No new cycle/depth guard is introduced. These are guest
  instruction-model observations, not portable C fault or hardware-MMU claims.
* All **six original call/delay windows** run at both stack phases, twelve
  cases per body. The **complete eighteen-word `func_15079390` caller** passes
  48 cases per body, using its three actual byte loads, 24-byte frame and the
  connected dispatcher/recursive helper. Other complete parent functions and
  gameplay are not claimed.
* **Nine independent GNU links**, three text/data/helper layouts and 66
  cases per body qualify all five relocation bindings, including HI/LO carries.
* Native32 O0/O2/O3 pass **735 executions**, 245 valid typed fixtures per
  profile, through a volatile callback pointer with UBSan enabled. Structure
  offsets and pointer/word widths are checked. Native fixtures use bounded
  objects and terminating searches; sparse invalid indices and cycles remain
  guest-only. The synthetic index-256 metadata alias has valid native backing.
* **Eleven native and eleven separately compiled IDO controls** each have a
  fired witness: any-success accumulation, initial true, wrong starting link,
  missing equality bypass, byte root/argument narrowing, skipping slot zero,
  raw nonboolean result, wrong payload, cached next and cached identifier.
* **264 raw-byte, five binding and seven whole-image corruption controls**
  fail closed. The old stub fails the independently nonzero result case.

Nineteen shared matcher/padder/relocation/protected-data checks pass in 12.015
seconds; `make tools-check` passes. The sibling tools checkout's twelve
documented standalone matcher/padder checks and smoke test pass in 7.485
seconds. Its consumer-layout data tests cannot run from the standalone layout
and are not counted; the seven mounted data tests pass. The new target suite
is qualified in the mounted checkout only. Sibling edits and untracked work
are untouched. Unchanged neighbor suites are reused through complete code,
binding and data identity, not called fresh checks. Routine Claude calls: zero.

## Production and preserved inputs

The immutable snapshot contains **145 files**, including all headers, target
and caller source/object/assembly, tables, retail ROM, manifests, linker,
Makefile, ELF, binary, progress and graph. Frozen bytes and protected live
inputs are checked. Artifacts are retained under
`conker/build/game-node-payload-dispatch-1514D3B0-match/`.
The starting consumer is `fabf98f7c079a9b7b5a99f5fbcee325e8709fe45`;
mounted tools start at `e629b7ac317d2982ff7154ae81e23699917f63ab`, both clean.
The sibling tools HEAD remains `ddbdd16b53ce60b054fb6e11bf0649a41f48375a`.
Host-port sources, saves and frozen Release artifacts are untouched.

Four inherited owner Warning 712 diagnostics at two `func_1514EC1C` calls
remain identical after source/line normalization. Compact `.reginfo` adds only
S5/S6/S7 use: mask A31FFFFE to A3FFFFFE; all other bytes are pinned. Every
other compact allocatable section and all padded sections remain identical.
No constant pool, compiler-profile change or guard row is added.

Actual Make completes the normal shared-header dependent rebuild. The target
owner and **entire ELF** equal the independent prediction byte for byte. All
**6,052 function addresses** stay fixed; only this target's body changes.
All **189,088 protected data bytes across 720 owners** remain exact. The
literal full-file prediction accounts for **207 changed bytes**, confined to
the function slot and its symbol-size update from 12 to 264. There are
**zero excluded bytes and zero metadata permutations**. Other named
definitions and all four complete caller objects remain unchanged.

| Artifact | SHA-256 |
| --- | --- |
| Natural target | `0d963230f51acf20fce38e6ca82b66cb9afdbca9dfaaddc8e234d229477556b3` |
| Original target | `1b4ee138e6a3ebc678e083572c38d424243fdc1066ea0f4b764e76a1e9555cfe` |
| Production owner | `142e5564e1c8d605f8e6ce8accef7777e768abb2a1bf3aa9a904e9a99c581f25` |
| Complete ELF | `31e41dff4d451e29a3def37e867fd07c44dd5a1a85e2f66dc311cfcd40756006` |
| Code binary | `391bd6cd9f8b3ba46c04f90f6735b94d29c758179a945b89acda86108e1f7924` |
| Unchanged guard manifest | `892dcc21c80c8cc41c6970ed89c7f218e072b5a5487946d406a0d133e7f6d6d6` |

The production build and recount take 95.242 seconds. `make -C conker all`
produces the binary and returns 2 only at the expected incomplete-project
retail checksum mismatch. The inherited duplicate generated_12D630 recipe
warning remains. Source newline styles and unrelated/private inputs are kept.

## Progress and continuation

| Section | Byte-exact / converted | Match | Drift | Different |
| --- | --- | --- | --- | --- |
| Total | 4,177 / 5,512 | 75.78% | 0 | 1,335 |
| Init | 492 / 492 | 100.00% | 0 | 0 |
| Game | 3,504 / 4,839 | 72.41% | 0 | 1,335 |
| Debugger | 181 / 181 | 100.00% | 0 | 0 |

Converted inventory remains 5,512/6,046. Root README gets aggregate rows only.
The 80% threshold is 4,410, leaving **233 more** exact functions. The live
nonexact list selects **func_1516A538** as the next ordinary candidate: 68
words in `generated_197120`, ROM 0x1979E8, frame 0x50, still a zero-return
placeholder. Its source and original assembly are identified through Graphify
and confirmed directly; no C matching credit is added for it here.

Retain the eight separate boundaries from Note 2103: `func_150A76F0`,
`func_151F8870`, `func_150A613C`, `func_150AE280`, `func_15115F68`,
`func_151AE2BC`, `func_150A6760`, `func_150A70C0`.
Keep the wider 80% goal active. Tools are committed before the consumer pin.

Mounted tools are committed as `b9a7f35f0caf925a2bac12f3bb2103fc4b4dfba9`
(`test(game): qualify filtered node payload dispatch`); the consumer records
that exact pointer with the C and documentation. No push is performed.

The ordinary AST-only Graphify update refuses its smaller 24,983-node
replacement and preserves the curated graph. The ten-path scoped refresh
retains 58,778 old IDs, relocates three update-log IDs with unique same-label/
same-source replacements and adds ten IDs. **Zero nodes outside changed
paths are lost**. The result is **58,788 nodes / 112,538 links / 5,106
communities**, SHA-256
`92e4f982cf25be2839674eaeb6f3439f94186739d417e533f11460a7968dc1c1`.
The target is updated to L109, with the same-file call edge to
`func_1514D4B8` present. This scoped result does not remove the previously
documented cross-file call-edge limitation or establish a fresh full-corpus
scan. The 31,816 nodes retained from 3,754 files outside the current scan
corpus are preservation evidence only. Source, relocations and connected
guest execution remain authoritative for the actual call contract.

The final production audit confirms that the entire progress CSV is
unchanged, preserving all conversion rows and byte percentages, and that
all audited ELF/binary/owner/guard hashes, frozen inputs and caller objects
remain stable. Detailed target checks can be rerun in the prepared consumer
with `python3 -m unittest tools.tests.test_game_node_payload_dispatch_match -v`.
