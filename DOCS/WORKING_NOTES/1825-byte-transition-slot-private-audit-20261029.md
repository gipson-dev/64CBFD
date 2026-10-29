# Byte-transition slot allocator: private behavior audit

Verified 2026-10-29 against consumer `0f6c17e661200997c329241bf6eb1614d6008142`.
`func_15187EC0` remains a zero-return placeholder in
`conker/src/game/generated_1B5370.c`. This is an unfinished private
reconstruction, with **zero new converted or exact-function credit**.
Accepted progress remains 3,902/5,506 (70.87%), Game 3,229/4,833 (66.81%),
zero drift; 228 additional exact C functions are needed to reach 75%.

## Retail contract and callers

VA `15187EC0..15187F90`, ROM `1B5370..1B5440`: 52 words, 208 bytes,
24-byte frame. The routine allocates from five 36-byte records at `D_800DF700`
using signed count `D_800DF7B4`. Counts of five or greater return -1 without
touching the pool or invoking `bzero`. The original has no lower-bound check.

The eight arguments are a 32-bit mode, single-precision value and six bytes.
The float arrives as raw bits in A1 after the integer first argument. A2/A3
are spilled to their incoming homes and masked to eight bits. Four further
bytes are loaded from the low bytes of their o32 stack slots. Mode has its
own incoming-home spill/reload. Mode and the four stack bytes are loaded
before the field stores.

For an accepted index, the routine writes the float at +20, duplicates the
first triplet at +0 and +6, writes mode at +16 and the final triplet at +3,
then clears twelve bytes at +24 through `bzero`. Bytes +9 through +15 remain
untouched. It **reloads the shared count after `bzero`**, increments that
value and returns it minus one. Returning the original allocation index
would lose this behavior if the provider changes the count.

An aligned full-ROM scan found three JAL words targeting the entrypoint:
ROM `370CC`, `37178`, `37478`, corresponding to calls in `func_15009BD0`,
`func_15009C7C` and `func_15009F74` in `game_36680.c`. No aligned word equal
to the complete address `15187EC0` was found. This does not exclude computed
or encoded indirect calls. Original caller-window execution remains pending.

The public declaration in `conker/include/functions.h:1142` uses 32-bit
third/fourth parameters and four trailing byte parameters. Narrowing the
third/fourth parameters recovers retail masks but requires audited header
and caller changes before adoption. No public declaration has changed.

## Source and profile screens

Original assembled raw function SHA256:
`28ccf6d29455fc7b0223a585ca8df12fc1189e1d9c84ef88554a9dd70642b517`.
Normal owner profile: O2/g3.

| Private source form | Words | Result |
| --- | ---: | --- |
| Wide third/fourth parameters and byte stores | 44 | Bounded behavior passes; argument homes/masks and scheduling differ |
| Byte third/fourth parameters | 50 | Masks recovered; mode spill/reload and scheduling differ |
| Address-taken mode and byte parameters | 52 | Relocation bindings agree; 22 words still differ |
| Volatile mode and byte parameters | 52 | Same 22 differences; no evidence that the original mode was volatile |

Field-order, byte-pointer, register-parameter, temporary-capture and old-style
definition experiments did not recover an exact body. The old-style float
definition changes the promoted argument ABI and is unsuitable. Direct
compiler screens of O1, O1/g3, O2 without debug, unoptimized debug and O0 did
not recover the body. Disabling loop unrolling under O2/g3 left the 50-word
candidate unchanged. No profile change is justified.

The first profile helper rejected O1/g3 in its assembly-processor flag stage;
the subsequent direct compiler screen completed. A declaration-placement
experiment failed the compiler's C89 rules. Their partial outputs are
historical experiments, not passing qualification receipts.

## Completed behavior evidence and limits

Local ignored stage: `conker/build/game-byte-transition-slot-match/`.
`behavior_audit_v10.py` exited 0: 432 cases each against retail and both
44-word/50-word candidates, totaling **1,296 guest executions**. Comparisons
cover public memory, returns and provider calls, including capacity rejection,
negative/corrupt counts, high argument bits, raw float payloads and count
mutation during `bzero`. Negative indexing is tested only through mapped
guest memory, not claimed as defined portable C behavior.

`native_audit_v13.py` exited 0. Its retained output filename is
`native-audit-v11.json`. **320 cases per profile** pass under native32 O0,
O2, O3 and UBSan. Four deliberate faults are rejected per profile: wrong
capacity comparison, omitted clear, wrong final byte and cached count.
This harness tests the wide-parameter semantic body, valid indexes and
rejected nonnegative counts. Earlier native drivers failed on a missing
private input and an unused-parameter warning in a deliberate mutant.
The final driver derives its input from the transferred source and permits
unused mutant parameters while keeping other warning errors enabled.

These checks establish bounded behavior, not instruction/access-order,
caller, owner or linked-image equivalence. Candidate scripts, objects and
receipts remain local ignored artifacts rather than installed tools.

## Resume

1. Resolve mode-home lifetime and argument-load ordering under O2/g3. The
   plain candidate is still 50 words; the 52-word diagnostic forms retain
   22 differences and are not accepted.
2. Qualify any byte-parameter declaration change across actual callers and
   affected header consumers, including original caller-window execution.
3. Complete emitted-code fault/access-order and relocation controls,
   full-owner padding/neighbors, actual Make and independent whole-image audit.
4. Only then install canonical tools in both copies, commit tools before
   the consumer pin, rebuild production, recount and refresh the graph.

No candidate source, header, guards or compiler profile has been installed.
