# Game Boot-Logo Phase Controller Direct Match (2026-11-03)

## Outcome

`func_151DE6D4` now replaces its zero-return placeholder with the semantic
boot-logo phase controller and emits its complete 64-word / 256-byte retail
body directly from C. The recovered body has the retail 32-byte frame, all 20
relocation bindings, both branch-likely threshold routes, and zero positional
word differences. No retail-word guards or inserted assembly words are
required.

This is a source/ABI/dispatch-table, raw and padded owner, guest/native
execution, strict whole-image, protected-data, production-build, recount, and
graph-retention result. It is not live boot playback, renderer, audio, or
hardware acceptance.

## Preserved semantic contract

The function first calls `func_151E530C` to refresh the status intensity. It
then sets object zero's `0x200` state bit and fixes its vertical position at
`1000.0f`. When `D_80000300` is zero, the logo timer `D_800E0A90` is reset to
zero.

With timer value `0x14B` or later and status flag `0x8000` set, the function
skips two protected time ranges. Values below `0x1E0` snap to `0x1E0`; values
from `0x259` through `0x2CF` snap to `0x2D0`. At timer `0x349` or later it
sets `D_8008FE28` to two, changes phase `D_800E0B94` to one, clears
`D_800D2E40`, requests scene `0x21` through
`func_1501C730(6, 0x21, 0, 0, 1)`, and sets `D_800E0B96` to `0xFF`.

The adjacent alternate source supplied a semantic candidate only. Adapted
separate timer/global assignments compiled to the correct 64-word extent and
frame but left six scheduling/register differences. Writing the two updates
as `timer = D_800E0A90 = value` recovers retail's branch-likely delay slots
and shared `v0` stores, eliminating all six differences without guards.

## ABI, owner, and dispatch registration

The recovered ABI is `void func_151DE6D4(void)`. There are no direct retail
`jal` calls. Its only aligned code-pointer literal is ROM `0x2348D8`, slot 11
of `D_8008FDEC`; `func_151E51EC` indexes that phase table and invokes the
entry with `jalr`. The owner is `conker/src/game/generated_20AE20.c`.
Qualification preserves 59 neighboring functions, the owner's retail rodata
binding `jtbl_800AB9BC`, and every non-target byte.

The natural compiler body and linked retail body are each 64 words with a
32-byte frame and zero positional differences. The 20 checked bindings cover
the two helper calls and all addressed globals. The installed guard table is
unchanged because the compiler output needs no normalization.

## Qualification and execution

The permanent qualifier was committed first as tools commit `e66af79`
(`test(game): qualify boot logo phase match`). Its four-test suite passes in
24.959 seconds:

- all 64 retail words, all 20 bindings, 59 owner neighbors, the phase-table
  registration, retail rodata binding, and strict 6,051-function image are
  closed;
- 224 guest cases across stack phases zero and eight exercise timer reset,
  both flag states, every threshold boundary, both skip windows, and scene
  submission, reaching all 64 retail words;
- native 32-bit O0, O2, and O3 builds each pass 112 cases;
- twelve independent semantic controls are rejected; and
- all 256 raw-byte mutations plus all 20 relocation-binding controls fail
  closed.

The shared match-progress, guarded-object, generated-PC16, and protected-data
suite passes all 19 tests in 22.393 seconds. Protected Game data remains exact
at `0x80082760`: 189,088 bytes across 720 owners, zero different bytes or
owners, SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

## Production closure and frozen evidence

The actual production ELF target compiled, padded, assembled, and linked the
changed owner with its required `jtbl_800AB9BC` rodata relocation. The
installed qualifier reproduced the private qualification result. The
subsequent `make -C conker all -j2` generated the ROM image and stopped only
at the expected final retail-ROM SHA mismatch.

| Artifact | SHA-256 |
| --- | --- |
| Natural 64-word compiler body | `ed9c26aabf1dc42806719bc72f348bf143ed08aaf5b99affeee7803a405886ef` |
| Complete linked retail target body | `a8bf3fa92004b4cf3b093f269e5285ff24de9cfd170e3e3e14eaaff5b9899ec2` |
| Installed semantic owner source | `d23b682af822ba1c9e693856b375db65bbbb3650b2c72f1c64d277e1f88c7884` |
| Qualified/production owner object | `d760cd283f5f48e723df4e56c702bd8d1aa318554b7b2590d58cbe8a98d9fbc1` |
| Predecessor linked ELF | `5af028bdaf09038c9d3f51423bbbec0db4601575a87d5e78c197457bc63b4e81` |
| Qualified/production linked ELF | `0e23d0dd59d6dfce9dc5abc84d803a40450dbaf55b42ca6a184b17aa51032207` |
| Production rebuilt ROM image | `841e14321215eaf2e04c081a8f6dc29748d0437319b4f19a72e222617d50018e` |
| Production map | `1cbc78ec7ba3bfd4cd8bef4b83bfdf51fc96dd1d5cf45ab59794d62d86946da1` |
| Unchanged guard table | `f2b66960ae84646edff18e3da5e603689d36b0beef32a71482265b4036bd025e` |
| Aggregate progress catalogue | `96a7f15ab5207027a204f795e91b8f9f3453482ce4ec4d47bd8bcb4b5a305502` |

## Recount

The fresh production ELF reports:

- Total: **4,130 / 5,511 (74.94%)**, zero address drift, 1,381 different.
- Init: **492 / 492 (100.00%)**, zero drift.
- Game: **3,457 / 4,838 (71.46%)**, zero drift, 1,381 different.
- Debugger: **181 / 181 (100.00%)**, zero drift.

The active 80% threshold is 4,409 exact functions, so **279 more** are needed.

## Graph retention

The standard reduced `graphify update .` extracted nine uncached inputs but
proposed only 24,539 nodes against the retained 58,333-node corpus, so
Graphify correctly refused to overwrite `graph.json`. Its fail-closed report
retained 31,816 nodes from 3,754 still-present files outside the reduced scan
corpus. The graph SHA-256 remained
`9ab77c7425ae7a46d7379401f9b8b4f9f4a5a6d9e38efdadd2ff9cb399f78af5`.
No forced refresh was used.

An explicit 11-path incremental rebuild with `force=False` then produced
58,343 nodes, 112,212 links, and 5,192 communities. Against the saved
pre-change snapshot, 58,330 / 58,333 old node IDs were retained. The three
replaced IDs are line-number-derived `DOCS/UPDATE_LOG.md` headings, and each
has one uniquely relocated replacement two lines later; 13 IDs were added for
the Note 2060 file and its section headings. The 22-link net reduction is
confined to the explicitly re-extracted owner and documentation: stale
generic `s32` reference edges and one stale owner call edge were removed,
while the recovered `func_151DE6D4` to `func_151E530C` call and Note 2060
references were added. The resulting graph SHA-256 is
`7a8fd14a53e93a6396ce04d9fa7c4ee75cf662891b78669377462799622b4d7c`.
A final note-only refresh after recording this section preserved the same
58,343-node / 112,212-link topology and completed clustering normally.

## Continuation

Continue the ordinary Game queue at `func_150A76F0`, currently the smallest
remaining real-difference candidate. The seven documented handwritten/custom-
ABI boundary cases remain in their separate lane. Every next candidate still
requires source, ABI/caller, owner, guest/native, actual Make, complete-image,
protected-data, production recount, documentation, and graph-retention gates
before credit.
