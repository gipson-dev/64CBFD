# Game node-range walker guarded match - 2026-11-09

`func_15169070` now matches its full **124-word / 496-byte** retail slot with
the original **0x58 frame**. Complete semantic C emits 124 words. **45
expected-word/relocation guards** close register allocation, scheduling,
row-end address folding and one redundant limit copy; no words are inserted
or omitted. No compiler profile, shared ABI declaration or conversion-row change.

Fresh linked total **4,298 / 5,513 (77.96%)**, Game **3,625 / 4,840 (74.90%)**,
Init 492/492, Debugger 181/181, zero drift and **1,215** different converted
functions. **113** more accepted matches reach the active 80% goal at
4,411/5,513. README changes only the two aggregate rows.

## Recovered source and remaining scaffolding

Owner: `conker/src/game_1944C0.c`; VA 15169070..15169260,
ROM 196520..196710. The already-converted routine has no separate original .s;
the frozen US ROM supplies the reference/layout. Give the parameters and
locals meaningful names: first, last, payload, opcode, column, head,
descriptor and node. Preserve the existing four-argument ABI, including its
unsigned byte opcode and integer payload address. Explicit byte-pointer casts
at both pre-helper calls remove the target's two pointer/integer warnings.

The owner has **seven inherited CFE warnings before and five after**. The five
unrelated pointer/type warnings remain and are compared by normalized code
and diagnostic identity, not hidden by warning flags. No new diagnostics appear.

Keep the real incoming parameter homes, original saved-register lifetime and
column home at SP+0x40. The preexisting unused padding array changes from 16
to 20 bytes to reproduce that home with the observed 0x58 frame. Its original
purpose remains **unrecovered**; this is explicit source-layout scaffolding,
not evidence that retail declared a 20-byte array.

Compute the descriptor before the column byte offset. Bound the row cursor
by the actual `D_800DCE50` array end. The array is 0x340 bytes: two 0x1A0-byte
rows of 104 four-byte heads. Descriptor stride is 52 bytes, with callback at
offset 0x1C. `func_15143D18` orders/clamps the incoming range using 2 and 104.
Reload the live upper bound at each outer-loop test.

Choose presence of a descriptor callback once per row. Read the head before
incrementing signed byte depth `D_800DD190`; unwind depth even for an empty
head. Before each helper call, save node+8 into the current depth's slot in
`D_800DD198`. On the callback path, reload the function pointer after the
pre-helper. After callbacks, reload depth and its continuation slot. These
orders preserve list mutation, callback replacement and nested traversal.

## Normalization and relocation limits

Normalize the closed S2/S3/S4 role cycle with corresponding save/restore
homes and restore order. Reorder independent descriptor/column initialization
and the outer-loop tail without changing memory/call operations. Fold
`D_800DCE50 + 0x340` from three address instructions into the two-instruction
retail `D_800DD190` address. The released instruction position carries retail's
OR-with-zero copy of the shifted upper bound.

This fold requires **D_800DD190 == D_800DCE50 + 0x340**. The complete frozen
linker/symbol/data inputs and production data-layout audit establish it for
this retail build. Rebase tests preserve this relationship; they do not claim
arbitrary independent relocation of those two labels. Deliberately inconsistent
bindings are rejected by the fixture's declared precondition. Ordinary padders
still operate on expected object words/relocations; the full qualification
supplies the linked layout proof.

All raw words are accounted for by the explicit permutation, saved-role
renaming, address fold and limit copy. Full-payload fingerprints and scope/
binding checks reject unknown input. Both full-owner ordinary padding and
independent target-only generated padding produce the same retail words and
relocations. Each padder rejects **50** stale word/binding cases; all **124**
single-word corruptions fail the payload gate. No blanket metadata exclusion.

Word **75** is the retained signed-byte load before the no-callback label.
The branch-likely delay load supplies that value on normal entry, so public
execution never reaches word 75. All three bodies execute the other **123**
words; the complete 124-word static slot, including the unreachable load,
is verified and preserved. Do not report 124/124 dynamic coverage.

## Live callers and helper boundaries

The whole-ROM census finds three JALs at ROM **892E0, 89300 and 196508**, with
no aligned entry pointers or direct jumps. All three are present in the
current linked image. `func_15169040` is an already byte-exact 12-word C
wrapper. Replace its stale nonmatching-target comment with its actual
complete-range forwarding role; it receives no additional matching credit.

The other two calls live in the already byte-exact **assembly**
`func_1505B9C4`. Its complete 0x77C bytes stay fixed. These calls build an
actor-pointer/tag packet at caller SP+0x40, with the unsigned tag store in the
JAL delay slot. The complete wrapper and original 10-/8-word packet windows
pass **360 executions** across the three target bodies, covering all 30
original caller words. The assembly parent is neither converted nor claimed
fully executed here. Native tests also execute the original C wrapper body
through the selected subject binding in 24 cases per profile.

The range clamp and 20-word pre-helper are independently checked against
retail and connected in guest cases. The pre-helper's downstream cleanup and
descriptor callbacks remain bounded providers. Deliberate mutations and
recursive provider entry are **interface extensions** for stress testing,
not a claim to have reproduced complete callback algorithms or gameplay.
Portable native cases exclude physical incoming-frame and pointer-byte aliases.

## Validation, production and resume

Freeze **673 inputs** from consumer 967ac4ad and mounted tools ff9f760.
Six fresh focused checks pass in each tools environment before and after
installation. Sibling qualification uses an ignored overlay for the six new
modules and records actual helper origins/fingerprints. Its **2,439** existing
dirty paths are preserved. Shared smoke checks run fresh in both copies;
three unchanged regression receipts per copy are explicitly reused by exact
fingerprints. No legacy actor suite is claimed freshly replayed.

Guest: **1,858 cases per body / 5,574 executions**, all opcode bytes and signed
depth bytes, callback replacement, next-link mutations, live range bounds,
payload/frame aliases and nested provider entry; 36 coherent rebase cases.
Native SDK32: **1,206 cases** at each of O0/O2/O3 with UBSan, complete table/
node/slot guards and independent state/trace digests. All **12 controls** are
effective both natively and under IDO. An initial stride mutant ran past the
row table and was rejected as an invalid control; the final control changes
only head stride, terminates, and fails by semantic state. No trap, compiler
failure or unsupported interpreter instruction is counted as a witness.

Four independent GNU links and 16 executions qualify address low halves
0000/7FFC/8000/FFFC. Six image corruptions cover header, target, helper,
retained private overflow, protected data and EOF. The actual owner has a
**three-command** compile/pad/assemble Make recipe and no GLOBAL_ASM entries;
do not impose another owner's five-command asm-processor recipe.

All **41 neighboring functions**, pools and register metadata stay fixed.
Actual Make reproduces the predicted 42-function object. Strict full-image
prediction permits only the target slot and symbol-size 484->496 update:
**150 changed bytes, zero unexplained bytes/exclusions**. All 6,051 linked
addresses, including 6,047 canonical addresses, stay fixed. Protected data
remains exact: 189,088 bytes across 720 owners. Guard history stays an exact
byte prefix. Inherited duplicate generated_12D630 Make warnings and final
all-target checksum exit 2 remain while the project is incompletely matched.

Scoped Graphify AST refresh/retention verifies all 42 C source positions and
preserves old nodes outside changed paths. Previously excluded files that
still exist remain retained; this is not full-corpus semantic extraction.

```sh
python3 -m unittest tools.tests.test_game_node_range_walker_15169070_match -v
```

Prepared predecessor artifacts and receipts are in
`conker/build/game-node-range-walker-15169070-match/`, including production,
both preinstall/installed replays, graph-retention, post-commit and HANDOFF.
The fixture fails closed on unknown source, inputs, scope or bindings.

Next: **func_15075650** in `conker/src/game_A28B0.c`, a 141-word actor
selection/state updater. Inspect its retail control flow, random-number
modulo widths, current-actor reloads and selector modes before fitting. No
candidate for it is installed or credited here. The separate func_1510D404
compiler investigation remains private and uncredited. Routine Claude calls: 0.
