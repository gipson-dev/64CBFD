# 2636 - Column event walker guarded byte match

Date: 2026-11-22. The total 85% matching goal remains active.

`func_1516944C` in `conker/src/game_1944C0.c` replaces an empty void body with
the complete callback-safe traversal of one descriptor column in both node
rows. The **106 raw C words** normalize to all **105 retail body/slot words**,
with **frame 64**, **18 expected-word/relocation guards**, **one omitted
instruction**, no insertion and no trailing padding. This is a guarded match
that includes a linked end-address fold, rather than direct C word identity.
Original: `conker/asm/nonmatchings/game_1944C0/func_1516944C.s`.
VA 1516944C..151695F0; ROM 1968FC..196AA0; 420 retail bytes.

Production is **4,618 / 5,528 (83.54%) total**, **3,945 / 4,855 (81.26%) Game**,
zero address drift, **910 different**, and **81 more matches** to 85%.
Init remains 492/492 and Debugger 181/181. Conversion rows are unchanged.

## Recovered behavior and interface

The existing `void(s32 column, s32 payload, u8 opcode)` interface is retained.
A signed column at or above 104 becomes 103. The descriptor is 52 bytes,
using the real SDK `struct115` callback at offset 1C. Both rows have 104
pointer entries and a stride of 1A0. Each row increments signed depth
`D_800DD190` even when empty. Before each helper/callback, the current
node's next pointer at +8 is saved in `D_800DD198[depth]`.

The routine calls `func_1516968C(node, payload, opcode)`. Callback presence
is selected once per row, but the callback pointer itself is reloaded after
the helper. The next node is reloaded through the live depth and continuation
slot after each call. The live depth is decremented once per row. Payload
and the byte opcode survive in saved registers; changes to incoming homes
do not replace those captured values.

The selected source assigns descriptor, head and row in that order. It
uses the real array end `D_800DCE50 + sizeof(D_800DCE50)`. No shared header,
prototype, compiler profile or unrelated function source is changed.

## Guard derivation and full-domain opening proof

The opening guards close one four-register allocation permutation and an
independent instruction reorder. An affine modulo-32-bit interpreter proves
all 2^32 column words across the two signed clamp domains, with arbitrary
payload/opcode bits. It verifies all saved role expressions, the 64-byte
frame and every opening stack store. A changed-register control fails.
This is guest ABI evidence; negative array columns are not a portable C domain.

The closing fold uses the measured linker invariant
`D_800DD190 == D_800DCE50 + 0x340`. It retargets the closing HI16/LO16 pair,
omits raw instruction 91's redundant end ADDIU, and updates the branch
register/displacement. Two 1A0 row advances equal 340 modulo 32 bits, so both
forms select the same loop edges for every linked base satisfying the invariant.
All named relocations and 105 normalized words equal original assembly.
Every pre-existing guard row retains its exact bytes.

## Qualification and practical limits

- All 41 raw and padded neighboring functions, constant pools and compiler
  diagnostics remain unchanged. The actual three-command Make recipe
  reproduces the complete qualified owner and 106-word compact target.
- Raw, normalized and retail guest streams each pass 1,934 cases, plus 36
  guest rebase runs. Cases cover all opcode and signed-depth bytes, clamped/
  large/negative columns, both rows, empty lists, callback presence/reload,
  next-pointer and continuation mutations, live depth changes, bounded
  provider recursion, incoming homes, payload aliases and high opcode bits.
  Only the duplicated depth load at index 65 is unexecuted.
- Native SDK32 at O0/O2/O3 each passes 682 cases with strict aliasing,
  UBSan and complete matrix, descriptor, node and continuation-slot canaries.
  The harness supplies typed pointer storage and verifies SDK descriptor
  size/callback offset. Ten effective source controls reject wrong clamp,
  stride, snapshot, next reload, callback reload, omitted callback, depth
  unwind, opcode, payload and missing second row. Native columns are
  nonnegative and clamped; depths/continuation indices are bounded. Negative
  columns, invalid depths and guest frame aliases remain guest-only.
- The complete original/current 15-word packet wrapper `func_1516962C`
  passes 736 cases per raw/normalized/retail stream (2,208 executions).
  It builds the pointer/tag packet at SP+18/1C, including the real delay-slot
  tag store, and narrows all 256 opcode bytes. Packet tail, incoming homes,
  saved ABI and high caller input bits pass. Missing tag and missing byte
  narrowing controls fail. Five direct JAL sites are censused: parents
  1509D8FC, 151616D0, 1516962C, 15190518 and 151ABE00. No aligned pointer
  literals or direct jumps are found. The other four full parent routines
  are not executed by this check. Wrapper 151695F0 calls the separate range
  walker and is not misidentified as this routine's caller.
- The original/current 20-word `func_1516968C` is connected where applicable.
  Its cleanup provider and arbitrary recursive mutations remain explicit
  contracts/extensions, not full provider or gameplay acceptance.
- Across six discriminating cases, 346 access-fault triples compare all
  memory, ordered access traces, calls, observations and saved GPR/FPR state.
  Raw PCs, volatile temporaries, timing, internal return PCs, FCSR and fault
  internals of the recursive provider extension are not equated or modeled.
  Entry RA restoration is checked on completed execution.
- Both isolated padders and 12 GNU links across four HI16 carry boundaries
  reproduce the original body; row/end symbols preserve their adjacency.
  Four malformed expected-word/relocation controls are rejected.
- The complete production ELF equals an independent prediction changing
  only 420 retail target bytes and symbol size 20->420: **323 changed bytes,
  zero exclusions, no metadata permutations**. All 189,088 protected GameData
  bytes across 720 owners remain exact, as do conversion rows and all other
  frozen source/object inputs.
- Seven fresh focused checks pass in both tools configurations before and
  after adoption, plus `make tools-check`. The second configuration uses a
  disposable overlay and invokes its own padder from the actual Make recipe;
  the real sibling's HEAD, dirty state and dependency hashes are preserved.

Raw target SHA256:
`15308276d7eab26843108986f73a18195f465c04a61f60ec8392c01400d66857`.
Qualified complete owner SHA256:
`74e4b5e9c72513d66b43429f63dc210908866d0e1ca0659319d3e9dceccf6dd1`.
Production ELF SHA256:
`9e07c69f727697feee19fdf21fe5d94c40336763012ce5fd039dec646d63ccf9`.

Reusable command from the prepared consumer root:

```sh
python3 -m unittest tools.tests.test_game_column_event_walker_1516944c_match -v
```

The focused packet requires its frozen consumer inputs and fails closed on
changed fingerprints. Task artifacts are in
`conker/build/game-column-event-walker-1516944c-private/`.
Codex owns implementation/validation; Claude calls attempted/completed: 0/0.
The local symbolic, instruction, compiler and caller evidence resolves this
routine without advisory review. Host applicability is checked read-only;
no host/Release build, source import, push or hardware/gameplay claim is made.
Continue the remaining Game functions from the newly banked checkpoint.

Graph maintenance: the native update exited 1 with all
71,128 prior IDs retained. The subsequent serial scoped extraction
covers 9 C/Python files with no missing AST sources, producing
71,193 nodes / 170,319 links and retaining prior qualification
metadata. This is a scoped refresh, not a full-corpus re-extraction. Actual
commit-hook producers must be terminal and their ID/metadata retention audit
must pass before the final immutable bank is accepted.
The native scan protected the larger existing graph from a smaller corpus; the scoped merge supplies this update.
