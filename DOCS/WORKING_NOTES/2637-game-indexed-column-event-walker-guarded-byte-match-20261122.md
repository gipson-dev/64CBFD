# 2637 - Indexed-column event walker guarded byte match

Date: 2026-11-22. The total 85% matching goal remains active.

`func_15169260` in `conker/src/game_1944C0.c` replaces its empty void body
with the complete indexed descriptor-column traversal over both node rows.
The **125 raw C words** normalize to all **123 retail body/slot words**,
with **frame 88**, **90 expected-word/relocation guards**, **three omissions**
and **one inserted unreachable signed-depth load**. This is a guarded match
with a closed saved-register remap and local branch transformations.
Original: `conker/asm/nonmatchings/game_1944C0/func_15169260.s`.
VA 15169260..1516944C; ROM 196710..1968FC; 492 retail bytes.

Production is **4,619 / 5,528 (83.56%) total**, **3,946 / 4,855 (81.28%) Game**,
zero address drift, **909 different**, and **80 more matches** to 85%.
Init remains 492/492 and Debugger 181/181. Conversion rows are unchanged.

## Recovered source and live state

The existing `void(void *indices, s32 count, s32 payload, u8 opcode)`
interface remains unchanged. The counter is initialized before the signed
nonpositive-count return. Each current list entry selects one of 104 columns
in each 1A0-byte row. Callback presence is chosen once per row. The list entry
and descriptor callback are read again after `func_1516968C` before indirect
dispatch, allowing a helper to retarget the current entry or callback.

The source uses the real SDK `struct102` node, including its +8 next-pointer
word, and `struct115` descriptor callback at +1C. Next is captured in the live
signed-depth continuation slot before calls. The continuation and signed
depth are reloaded afterward. Each row increments/decrements depth even if
empty. The outer loop reloads the incoming count, advances the input pointer
by four bytes and terminates on `counter == count`; replacing it with a less-
than condition or cached count changes guest behavior.

The local frame view keeps row at SP+40 and counter at SP+50. Its intervening
12 bytes have no recovered use. This is explicitly labeled layout scaffolding;
the original source type or meaning of those bytes is not claimed. Declaring
this view after the SDK node pointer emits both measured offsets directly,
without stack-offset guards, volatile annotations or artificial wide arithmetic.
Shared headers, prototypes, compiler profiles and unrelated source stay fixed.

## Guard derivation

The six-register saved-role cycle maps raw s2->s4, s3->s2, s4->s3, s6->s7,
s7->fp and fp->s6. Corresponding save/restore slots and instruction order are
closed together; helpers may clobber all volatile registers. Remaining guards
reorder independent head arithmetic, commute two unsigned additions, preserve
the callback gate's signed-load delay slot and share the empty-node unwind.
The two empty-node branch-likely sequences become ordinary branches with
the depth increment store in the delay slot. Three redundant words disappear;
the original unreachable signed-depth load is retained at retail index 76.

The closing address fold uses the explicit linked invariant
`D_800DD190 == D_800DCE50 + 0x340`. Source uses the actual array end. Both
HI16/LO16 bindings and all 123 normalized words match original assembly.
All earlier guard-row bytes remain fixed. The large guard count is disclosed;
this is not direct compiler byte identity.

An affine modulo-32-bit opening check covers both signed count domains,
arbitrary pointer/payload/opcode bits, full incoming count/opcode homes,
the zero counter store, saved-role expressions and owned save-store values.
Local branch/store shapes, all 256 depth increment/unwind values and the
end-address algebra are checked. Two effective word controls reject a cached
incoming count and a cached post-helper input entry. These local proofs
complement full-stream tests; arbitrary exception PCs or timing are not equated.

## Qualification and limits

- All 41 other raw and padded functions, pools and compiler diagnostics stay
  fixed. The real three-command Make owner recipe reproduces the complete
  qualified object and compact 125-word target.
- Raw, normalized and retail guest streams each pass 1,908 cases, plus 48
  rebase runs across four HI16 carry boundaries. Cases cover nonpositive/
  positive counts, both rows, distinct parity-dependent heads, all opcode
  and signed-depth bytes, live current/future entry mutation, count-home
  mutation, aliased input homes, continuation/next/depth changes and bounded
  recursive provider extensions. All raw words execute; only retail index
  76 is unreachable. Incoming homes, row/counter slots and completed saved
  GPR/FPR/SP/RA ABI agree.
- Native SDK32 O0/O2/O3 each passes 952 cases with strict aliasing and UBSan.
  The harness supplies full 472-byte SDK nodes and typed pointer matrices,
  verifies descriptor layout, complete node/descriptor/matrix/input/slot
  state, and canaries around node/descriptor/matrix/slot storage. Twelve
  effective source controls catch wrong count, counter, head column, next
  snapshot/reload, callback/current-entry reload, callback omission, depth
  unwind, opcode, second row and pointer advance. Incoming count-home
  mutations, invalid indices/depths and numeric-word byte aliases stay guest-only.
- The complete original/current/private-image 13-word `func_151494E0`
  wrapper passes 544 cases per stream using actual `D_800A5770` entries
  `[35, 95]`, count two, all opcode bytes and wide input bits. Caller homes
  and saved ABI agree. Missing byte narrowing and wrong count controls fail.
  A full aligned code JAL/pointer/direct-J census finds 18 direct JALs,
  no pointer literals and no direct jumps. The other 17 full parents are
  not executed by this test.
- Original/current 20-word `func_1516968C` is connected where applicable.
  Cleanup and arbitrary recursive mutations remain explicit provider
  contracts/extensions, not full cleanup or gameplay acceptance.
- Eight cases yield 788 fault-prefix triples for all non-stack bytes,
  incoming 64 bytes, row H-24 and counter H-8, ordered accesses, calls,
  observations and saved FPR. Private save slots/helper return addresses,
  physical GPR role identity, PCs, FCSR, cycle timing and provider-internal/
  recursive-provider faults are outside this projection. Completed saved
  GPR/SP/RA restoration is checked separately.
- Both isolated padders and 12 GNU links across four carry boundaries match.
  Four malformed expected-word/relocation controls are rejected.
- The production ELF equals an independent literal full-image prediction:
  only the 492-byte target and symbol size 24->492 can change; **369 changed
  bytes, zero exclusions, no metadata permutations**. All 189,088 protected
  GameData bytes across 720 owners, conversion rows and other frozen inputs
  remain fixed.
- Seven fresh focused checks pass in both tools configurations before and
  after adoption, plus `make tools-check`. The second configuration is a
  disposable overlay invoking its own padder from the actual Make recipe;
  the real sibling's HEAD, dirty work and dependency hashes are preserved.

Raw target SHA256:
`2b546bc5c2bd16d198ccc25275c5f5a075efecb80cef37c507f2cf7177bc99a6`.
Qualified complete owner SHA256:
`9ed6f1c3c546808cbb84992f81dc45994d384831f244292944ec01ebba230056`.
Production ELF SHA256:
`c1bb4c3e737ab4976ef5f5d75550ce7876023d9d72a84b1b7b77a92e29041330`.

Reusable command from the prepared consumer root:

```sh
python3 -m unittest tools.tests.test_game_indexed_column_event_walker_15169260_match -v
```

This focused packet requires its frozen consumer inputs and fails closed on
changed fingerprints. Artifacts:
`conker/build/game-indexed-column-event-walker-15169260-private/`.
Codex owns implementation/validation; Claude calls attempted/completed: 0/0.
The local instruction, symbolic, SDK/compiler and caller evidence resolves
this routine without advisory review. Host applicability is read-only;
no host/Release changes, source import, push or gameplay claim is made.
Continue remaining Game functions from the new checkpoint.

Graph maintenance: the native update exited 1 with all
71,201 prior IDs retained. The subsequent serial scoped extraction
covers 9 C/Python files with no missing AST sources, producing
71,285 nodes / 170,912 links and retaining prior qualification
metadata. This is a scoped refresh, not a full-corpus re-extraction. Actual
commit-hook producers must be terminal and their ID/metadata retention audit
must pass before the final immutable bank is accepted.
The native scan protected the larger existing graph from a smaller corpus; the scoped merge supplies this update.
