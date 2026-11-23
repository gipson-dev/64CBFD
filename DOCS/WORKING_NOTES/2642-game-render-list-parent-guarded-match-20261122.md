# 2642 - Complete render-list parent guarded match

Date: 2026-11-22. The total 85% matching goal remains active.

`func_151674F8` in `conker/src/game_1944C0.c` replaces its false zero-return
placeholder with the complete render-list parent. All **348 retail words and
named relocations** match in **frame 144**, using **91 expected-word/binding
guards**, **zero omissions**, and **zero insertions**. Raw C emits 348 words
in the original frame; its register allocation is not byte-exact.

Original: `conker/asm/nonmatchings/game_1944C0/func_151674F8.s`.
VA `151674F8..15167A68`; ROM `1949A8..194F18`; 1,392 bytes.

Production: **4,624 / 5,528 (83.65%) total**, **3,951 / 4,855 (81.38%) Game**,
zero address drift, **904 different**, **75 more matches to 85%**. Init stays
492/492 and Debugger 181/181. Converted-function and converted-byte rows stay
unchanged. This adoption supplies one matching credit.

## Recovered source and interface

The ABI is `Gfx *(Gfx *output, s32 selector, s16 view, s32 row)`. The local
52-byte `ListRenderDescriptor` describes draw at8, before-list at10,
before-hook at14, after-hook at20, after-list at24 and signed mode at30
(offsets hexadecimal). Unread fields remain opaque. The heads use two rows
with 104 pointers each and stride 1A0; list-node next is at8. The descriptor
span has 101 entries. No shared headers or compiler profiles change.

The parent submits the SDK modelview matrix, obtains the selected column
range, and checks each registered callback and nonempty head. It resets the
column's cached graphics state and sentinels before optional display lists
and hooks, clears lighting, and reloads the head after the before hook.
The image identity cache is a 32-bit word invalidated with all ones; using a
pointer view emitted identical code and is not evidence for the original type.

Each draw captures the callback before publishing node->next in the current
depth slot. This preserves callback/next load order and traversal when the
callback destroys links. Mode 1 checks the live output budget after every node,
rolls that node back and retains a sticky overflow flag. Mode 0 can roll the
whole column back. The post-list and post-hook run before the final budget
decision. Geometry restoration and returned cursor follow both early and
ordinary exits. Hooks can change live base, budget, head and later callbacks.

The already four-argument declaration in `conker/src/game_45B80.c` now gives
its graphics cursor and return value their correct pointer types. All 16 raw
functions, pools and diagnostic sets stay identical; its entire padded object
is byte-identical. Six complete callers contain 14 actual JAL sites. All remain
at their original addresses and extents.

The source uses the natural local order, separate cache stores and checked
do-loop to recover 348 words/frame144. A 23-difference probe was rejected because
it rotates callback/next loads across loop entry and backedges. The selected
91-difference source preserves literal memory order. No donor C was imported:
the retained donor only has an assembly pragma for this routine.

## Closed source-to-retail normalization

All 348 instruction origins remain exactly once. Only source origins 43..46
move to 45,46,43,44: a private SP8C counter store and three independent setup
operations have pairwise-disjoint write/read dependencies. No memory access
changes order relative to another access. Every other change is a GPR field.
Opcode/function, shift amount, literal, named relocation and control edges
remain fixed. No padding instructions, branch substitutions or frame guards
are introduced.

A complete integer CFG expands ordinary and likely delay slots, constant
branches, JAL/JALR link writes before delay, argument reads after delay,
o32 caller clobbers and returned/saved-register roles. Reaching definitions
agree at 497 operand pairs over 372 CFG nodes, including every memory address,
store value, branch operand, call target and argument. Three effective controls
reject a wrong indirect target, wrong node argument and lost saved-next store.
Word 224 is the sole unreachable duplicated depth-byte load and is retained.
Raw temporary registers and intermediate private fault states differ.

## Fresh focused validation

- Actual SDK32 native O0/O2/O3 each pass **1,352 cases** under strict aliasing
  and UBSan. All used descriptor/node/cache/row offsets are asserted, with
  typed objects, full numeric/opaque state, command words, ordered callback
  observations, returned cursor and canaries. **36 recursive cases** execute
  two complete child parents each while destroying links and exercising the
  depth-indexed saved-next slots. **20 source controls** all fail by comparison.
  Expectations come from both complete original and raw MIPS parents.
- Native providers have explicit bounded contracts. Descriptor modes remain
  stable during callbacks; legal rows, nodes, arrays and six depth slots are
  used. Views cover signed16 extremes. The fixture's actual SDK matrix is
  eight-byte aligned at its retail address. The narrow GCC uninitialized
  warning suppression covers rollback homes whose initialization follows
  from the stable-mode contract; it is not a source change.
- All **six complete callers (622 words)** and the actual **47-word range
  helper** run **203 cases per parent stream**. All 14 JAL sites and all 47
  helper words execute, covering selectors 0..6, 530 parent invocations and
  1,048 draw calls per stream. Each complete caller/helper slot independently
  equals ROM. Two controls reject a lost row home and a lost range selector.
  Other graphics/output/stage/draw routines remain bounded providers.
- All **nine complete raw/padded/retail parent-by-renderer combinations**
  run **116 cases**, with **224 renderer invocations each**. Actual registered
  columns 5/66 are checked in ROM and the linked ELF. Public memory, ordered
  provider events, callback arguments and returned cursors agree. Range-output
  local addresses are abstracted only after alignment/distinct/frame checks.
- **3,425 normalized/retail access-prefix pairs** agree in full memory,
  GPR/FPR, HI/LO, traces and callback state. **37 raw/padded/retail public
  provider-boundary triples** agree. Raw full fault identity is not claimed.
- Both production padders match. **12 GNU links** across four HI16 carry
  boundaries agree with named bindings retained. Four malformed expected-word
  and binding controls fail closed; two wrong replacements fail complete
  output comparison. No instruction is inserted or omitted.
- Both complete owners preserve all 41 parent neighbors and all 16 raw caller
  functions, pools and diagnostic sets. Six actual Make commands reproduce
  both padded owners. The caller's complete object remains byte-identical.
- Six focused gates run fresh in each tools configuration. Installed checks
  freshly compile both owners, replay Make and compare the entire image;
  the five semantic gates are reused only after exact source, raw payload,
  binding, import, manifest, artifact and native-binary fingerprints agree.
  `make tools-check` passes. The real sibling's dirty state, HEAD and dependency
  hashes are preserved through a disposable overlay.

The ordinary production build passes with the retained legacy compiler and
duplicate `generated_12D630` recipe warnings. Both changed owners' normalized
diagnostic sets equal their frozen predecessors; this is not a warning-free
build claim. All unrelated rebuilt object fingerprints remain fixed.

## Independent full-image audit

The entire production ELF equals the independent prediction: **1,204 changed
bytes, zero exclusions**. The reference does not use the new parent C or its
guards. It compiles the frozen OLD owner and pads it with frozen OLD guards,
requiring that entire object to equal the baseline. Only the parent's slot
is replaced with the independently assembled original routine, and all 41
neighbors remain fixed before the reference link.

The expected ELF starts from the frozen baseline. It changes the 1,392-byte
target window and its symbol size 12->1392, then reconstructs every named
symbol definition and the complete string pool. Only record/name-offset
ordering comes from the independent reference link. Definition values and
strings come from the frozen baseline; the complete named-definition multiset,
ELF geometry and unnamed records stay fixed. No actual-C image diff windows
or arbitrary metadata bytes are copied into the predictor.

All **189,088 protected Game data bytes across 720 owners**, other loaded
bytes, function addresses/extents, conversion rows, shared headers, build
profiles, private inputs and the complete prior guard-byte prefix stay fixed.
The production Make/recount supplies the totals above.

Raw target SHA256:
`0e62dcb99fcd912b1c24ac10e0afc4647c95f1ffbe72c7444219b3d2c10db809`.
Qualified parent owner SHA256:
`6ce25ba2a5e44e0d6a379cecf163b3a0c35b684d9825bcbaaaed92081c8483bc`.
Production ELF SHA256:
`78b10244fec3fed1d7decd56018648cc003b156b26309740d1cf7987b830b848`.

```sh
python3 -m unittest tools.tests.test_game_render_list_parent_151674f8_match -v
```

Artifacts: `conker/build/game-render-list-parent-151674f8-private/`.
Frozen-input checks fail closed. No FCSR, timing, asynchronous, hardware or
gameplay acceptance is inferred. The sibling binary-based host configuration
does not directly consume this decomp C restoration; no host import or Release
change is made. Codex owns implementation and validation; Claude calls: 0/0.
No provider/account changes or push. Continue remaining Game functions to 85%.

Graph maintenance: the native update exited 1 with all
71,632 prior IDs retained. The subsequent serial scoped extraction
covers 14 C/Python files with no missing AST sources, producing
71,721 nodes / 174,114 links and retaining prior qualification
metadata. This is a scoped refresh, not a full-corpus re-extraction. Actual
commit-hook producers must be terminal and their ID/metadata retention audit
must pass before the final immutable bank is accepted.
The native scan protected the larger existing graph from a smaller corpus; the scoped merge supplies this update.

Next target: `func_15168C4C`, the same owner's remaining 122-word/frame104 renderer placeholder. Inspect its real descriptor registration and mode-template domain; retain retail's uninitialized render-word path until its contract is established. No new source or credit is installed for that target.
