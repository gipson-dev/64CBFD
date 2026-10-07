# Game Sphere Callee Frame Alias Audit

Date: 2026-10-07. Baseline: `47b77791`,
[Note 1084](1084-game-sphere-callee-storage-recovery-20261007.md).

Continue `func_151452C4`. The selected experimental C still emits 126 words,
frame `0x70`, 60 differences. The private direction/origin/relative offsets
remain `0x64/0x58/0x4C` instead of retail `0x58/0x4C/0x28`.
Do not install it or patch these offsets. This checkpoint adds full-frame
behavioral evidence and rules out additional meaningful layout controls;
it does not increase conversion or matching counts.

## Full-Frame Reference

[Independent reference](../../tools/tests/game_sphere_frame_reference.py)
models the eight-argument helper directly, separately from the nine-argument
wrapper. Retail and selected C are checked against their own explicit layouts,
not claimed to have equal private memory. It models:

- Incoming stack arguments, explicit radius/origin homes and saved return word.
- Sequential word-copy writes to direction and origin snapshots.
- Rounded single-precision geometry and the perpendicular-square spill/reload.
- Both point pointers captured before the first point store.
- Private direction/origin rereads after each intervening point/scalar write.
- Each distance pointer reloaded from its incoming home at its actual late use.
- Relative-vector stores followed by live original direction reads in the dot.
- Miss versus post-write rejection and the final helper status.

[Six frame tests](../../tools/tests/test_game_sphere_callee_frame_recovery.py)
pass in 6.698 seconds, zero skips/errors/failures.

1. 1,404 direct-helper external-alias cases now compare **complete memory**, all
   ordered writes and the dot's actual argument pointers, including private
   locals, saved return and incoming homes. Nine centers, six radii, thirteen
   aliases and two stack phases. External retail/trial outputs still agree.
2. 1,296 additional cases vary 27 private/incoming locations, all four output
   pointers, three centers, two radii and two stack phases. Input vectors stay
   external, with zero origin and unit-X direction. Each implementation agrees
   with its layout-specific full-memory/write/status reference; they do not
   necessarily agree with each other.
3. The original frame `+0x58` probe retains retail second-X 24.0 versus trial
   10.0. A frozen-copy calculation would yield 6.0 and is explicitly rejected.
4. A first point at incoming `SP+0x14` overwrites the second-point pointer home
   with float-four bits. Retail still uses the already-loaded original second
   point pointer, producing second-X six. The next two zero coordinates replace
   both distance-pointer homes with zero; both late scalar writes go to the
   deliberately mapped address zero, in order four then six. This is bounded
   mapped guest-memory evidence, not a native null-pointer or gameplay claim.
5. Missing private snapshot storage and the naturally redirected late scalar
   target fail on the intended mapped-memory gate, for both implementations.
6. Compiler controls pin representative workspace/type/initializer results.

The reference's stack-layout/prologue constants are explicit evidence bindings;
the arithmetic and evolving memory are computed independently of decoded
instructions. No equal raw read schedule, full float-domain/FCSR/NaN payload,
native frame aliases, hardware or complete-caller acceptance claim.

## Layout Controls

[New driver](../../tools/experiments/game_sphere_callee_layout_candidates.py)
reproduces 48 controls, all compiling without diagnostics, none exact:

| Family | Controls | Result |
| --- | --- | --- |
| Meaningful named geometry workspace | 16 | 139 or 144 words, frame `0x60`, 124 or 137 differences |
| Scalar/struct/union delta and scalar representations | 21 | Unchanged 126 words/frame `0x70`, 60 differences |
| Array-view delta | 7 | 132 words/frame `0x78`, 128 differences |
| Scalar delta initializers, ordinary/union direction, O2/g3 or O2 | 4 | 126 words, frame `0x68` or `0x70`, 60 to 96 differences |

The workspace contains only actual delta/copy/root/relative values; no dummy
padding, unused fourth component or scratch-only stores are introduced.
It increases emitted stores and changes the frame, so it is rejected.
Scalar wrappers and structure-member delta forms do not move the private slots.
Array delta forms add six instructions and enlarge the frame. Scalar declaration
initializers do not recover the layout; removing g3 also fails to match.
No compiler profile is changed in production.

IDO rejects runtime aggregate initializers such as
`struct17 delta = {arg2->unk0 - arg0->unk0, ...}` with `Invalid constant expression`.
That exploratory compiler failure is recorded, not counted among the 48 valid
maintained controls or proposed as an installable source form. The existing
64-control driver and historical trial remain unchanged.

## Baseline And Resume

All 46 focused frame/recovery/wrapper/projection-schedule/owner-pool tests pass
in 212.519 seconds, zero skips/errors/failures. Project-tool smoke checks,
Python syntax and whitespace pass. Documentation gate: 67 documents,
3,762 relative links, zero broken. This is a focused run, not a new full
production or native geometry checkpoint.

Production retains the exact original 126-word assembly, 53-word direct wrapper
and 13-word dot helper. All 6,059 slots/addresses/extents, protected sections,
720 Game-data owners/189,088 bytes and 10,953 historical guards remain unchanged.
No new production build is required or claimed for these opt-in tests.

Matching remains 3,354/5,465 total (61.37%), Game 2,681/4,792 (55.95%),
2,111 different, zero drift. Conversion remains 5,465/6,042 and Game 4,792/5,321.
Main README aggregates stay current and untouched; handoffs remain in DOCS.
No sibling/frozen Release/save/runtime/push work.

Next: investigate IDO local-allocation/lifetime evidence before adding more
equivalent declaration forms. Recover the actual private offsets in C while
preserving the length/frame, live snapshot rereads and late helper homes.
Re-run the full-frame reference and the explicit retail/trial counterexample;
only then classify remaining scheduling/register differences and complete
owner/padder/caller/install/build/regression gates. Do not normalize private
offsets, invent padding or claim external-alias success as installation proof.
Sampler `func_151432BC` and oriented `func_15142600` stay open.

Ignored receipts: `conker/build/game-sphere-callee-layout-controls/`,
`conker/build/game-sphere-callee-frame-test/`, and the exploratory
`game-sphere-callee-workspace/`, `game-sphere-callee-types/`,
`game-sphere-callee-initializers/` directories under `conker/build/`.
