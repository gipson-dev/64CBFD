# Packet Rectangle Inner Flag Capture And Allocator Order

Date: 2026-10-16. Consumer predecessor **466c976d**, tools predecessor
**3cbb68b**. Continue **func_15095D34**, VA **0x15095D34..0x1509629C**,
ROM **0xC31E4..0xC374C**, owner `conker/src/game/generated_C1D70.c`.

This is production fitting progress, **not a newly byte-matched function**:
**71 -> 18** pointwise retail word differences, still **346 words / 1,384
bytes / frame 0x88**. Literal first **148** and last **91** words now match.
No new word guards, profile changes, assembly substitution or fabricated locals.
The same routine and the wider Game backlog remain open.

## Fired Allocator Evidence

`tools/experiments/game_packet_rectangle_allocator_trace.py` extends the
existing owned mode-5 compiler capture, without changing allocation decisions.
The qualified capture is ignored under
`conker/build/game-packet-rectangle-allocator/allocation-ordinal-qualified-5/`.
Normal/traced full objects, target words, 28 relative bindings and empty pools
agree; the owned UOPT child, UGEN and compiler driver all exit zero. All four
pinned compiler hashes remain unchanged. Existing diagnostic stream allocation
and real-number-printer suppression are inherited instrumentation; do not call
the entire capture passive. New allocator observers only read state.

Actual **75** sequenced events show local coloring before global coloring.
The two critical ranges are visited by the unconstrained **ordinal** pass,
not the optional ranking probe: flag **123** precedes computed fractional-T
**137**. Table/LR/IChain identity and bounded linked-unit snapshots are checked
against their raw native bytes, actual breakpoint PCs, one child PID/inferior,
entry/return ordering and cleanup before UGEN.

| Critical Range | Forbidden Colors | Colors Left | Save / Divisor | Gain | Best Cost | Candidate | Outcome |
| --- | --- | ---: | --- | ---: | ---: | ---: | --- |
| Flag 123 | 1..11 | 11 | 2.0 / 2 | 4.0 | 0.0 | 12 | Assigned 12 |
| Fractional T 137 | 1..12 | 10 | 1.5 / 2 | 3.0 | 14.75 | 14 | Rejected; assigned 0 |

The native gain formula is the observed comparison, **not save/divisor**.
The flag takes the final cheap color; higher-cost colors remain for fractional
T, but cost 14.75 exceeds gain 3.0. Do not describe this as complete register
exhaustion. Direct native float bits at the fired comparison establish these
operands; printed diagnostic real-number timing/cost output is still invalid.

The first `allocation-rank-initial-5` capture is preserved as intermediate
evidence. Its original validator wrongly required every range index to equal
its expression index. Actual split range **436** aliases expression **78**;
only the two critical ranges require equality. Fix the validator and add the
actual cost-gate observation in a new capture, never relabel the old receipt.
Five focused tests pass initially in **1.837s**, including independent
lifecycle controls with updated log hashes, raw-pointer/unit corruption,
wrong PID/PC/order/cost operands and identical-but-invalid object controls.

Upstream [IDO register allocation source](https://raw.githubusercontent.com/n64decomp/ido/master/src/uopt/uoptreg2.c)
and [data declarations](https://raw.githubusercontent.com/n64decomp/ido/master/src/uopt/uoptdata.h)
are reference material for interpreting the algorithm. They do not establish
5.3 binary layout compatibility; pinned native instructions and fired raw
snapshots corroborate the fields used here.

## Source Decision And Qualification

The cost-gate evidence motivates snapshotting flags only inside the actual
flip branch. Keep the direct byte outer predicate and its subsequent snapshot,
use integer `32` for the two inner fractional multipliers while retaining
outer `32.0f`, and distinguish the original S step from its mutable/flipped
value. Both S/T split screens emit the same 18-difference body; select S.
These are used semantic roles, not unused stack padding or register bindings.

Twenty complete-owner source screens cover the predecessor, snapshot routes,
narrow/unsigned flags, block/direct/masked predicates and original S/T roles.
The first qualified inner form has **19** differences. Its distinct
`compiler-inner-qualified` capture validates CFE/UOPT/UGEN streams but is
**prior 19-word evidence**, not a capture of the selected 18-word body.

The selected raw object SHA-256 is
`f95ee415f2eba533fa4076e5f6c42331367bf3444eb855a78b7816f598dc48c3`;
its 28 relative bindings are unchanged and it adds no pools. The linked slot is
`ad37e44da7fb64c05539fe6d3529b2d1c4edf53305fb0e51d68f13dc88c394c2`.
All 18 neighboring functions retain their words and relative bindings.

Twelve pre-install semantic tests pass in **92.326s**. They exercise 2,880
geometry cases in both stack phases, native32 O2/O0/UBSan with 1,048,576
animation cases each, eight effective guest/native controls, 80 guest alias
pairs, 16 arithmetic trap pairs/five special floats, 672 animation pairs,
three original rebase sets/48 pairs and 32 real caller/visibility/renderer
connections. All 346 raw-word, 28 binding, extra-pool and 100 frozen-input
corruptions are rejected.

The longer exact prefix is checked by **64 complete modeled state pairs**,
stopping before the first dispatched PC >= **0x15095F84**. That inequality
also handles flags-zero paths that skip the first flip block. A private-home
control preserves public memory but changes complete state at this boundary.
This is not later private-state, hardware FCSR/fault or gameplay equivalence.

## Full Image Boundary

The first full-image prediction is frozen **before production installation**.
Relink the saved pre-install owner to reproduce the predecessor ELF, then
link the actual emitted candidate. The entire predicted image equals an
exact **1,384-byte slot replacement**, with **204 changed ELF bytes**, zero
metadata serialization changes and zero exclusions. Normal guest rebuild
uses the existing compiler/padder/link pipeline. The pre-existing duplicate
`generated_12D630.c.o` recipe warnings remain unrelated to this change.

Strict after fingerprints:

```text
ELF    8b0b0f94df971019ca6b5123825abf9fcd7d180a76f9572d705b67ae28e6353b
Owner  b440f70a5dbec0f68e036ee2fc181f4b77fd50b3cd32cae894389cd4e1bdc90d
Guards 197a60801a08f0db3ed2afa2461b3d692bd215cf21f78870609589fb06df9c41
```

The checkpoint adapter recognizes only these exact two successor inputs and
validates the saved predecessor bytes. Unknown inputs are never normalized.
Installed checks require the literal complete prediction, all other ELF
bytes, 98 other inputs, prior guard history, all symbol/string bytes and
protected **189,088 bytes / 720 owners** to remain fixed.

## Final Checks And Bank

All **20 final tests pass in 127.844s**, exit zero, after the normal rebuild:

```sh
python3 -m unittest tools.tests.test_game_packet_rectangle_flip_capture tools.tests.test_game_packet_rectangle_flip_capture_installed tools.tests.test_game_packet_rectangle_allocator_trace -v
```

The installed ELF equals the entire first prediction. Both tools copies pass
Windows AST parsing and eleven shared padder tests: consumer **0.059s**,
standalone **0.047s**. `make tools-check` passes. Fresh official matching
measurement remains **Game 2,922/4,828 (60.52%)**, **total 3,595/5,501
(65.35%)**, different **1,906**, address drift **0**. Init 492/492 and
Debugger 181/181 converted C routines remain exact. Conversion figures stay
5,501/6,044 (91.02%), bytes 86.04%; root README already has these figures
and the same date, so no narrative or unnecessary edit is added there.

Tools **05ca56d8267c601d9931983ecb3195a9c2e2361b** commits the six new
experiment/checkpoint/test files before the consumer source/pin/docs. Preserve
old mirror HEAD **ddbdd16** and every one of its **820** initial dirty hashes;
copy only six absent files for **826** dirty paths, never commit/reset it.
Wait for the consumer's incremental graph hook, retaining the existing
19,398 excluded nodes without a full extraction or purge.

## Remaining Work

The first mismatch moves to **+0x250 / 0x15095F84**. Twelve differing words
cover the two flip blocks' scratch allocation and one adjacent load/mask
schedule. Six macro-home words remain at **+0x334, +0x348, +0x34C, +0x380,
+0x3C8, +0x3F8**: selected SP+4/+0/+2 versus retail SP+0xC/+8/+0xA.
The earlier flag home SP+0 now matches, including the retail +0x218 store.
Do not mistake complete public-output agreement for correct remaining homes.

Next inspect the selected body's actual macro temporary allocation and recover
the closed scratch cycles within the remaining **107-word** middle window.
Keep 18 differences explicit; do not replace these with bulk guards or dummy
locals. Original caller backlog, inherited-stack C deferrals and broader
Game/additional-source matching are not completed by this partial fit.

The user confirms the earlier truncated-path `Conkers` scratch file was
disposable; no recovery work is needed. No further Claude/auth attempt, push,
host-port edit/build/launch or frozen Release action occurs.
