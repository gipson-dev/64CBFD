# Owner Burst Frame Trace And Aligned Packet Qualification

Verified 2026-10-17. Consumer predecessor `3e0a133c`; tools predecessor
`44ac35d`. Both active trees began clean. Continue the complete experimental
`func_150F2D14` recovery from [Note1508](1508-owner-burst-emitter-recovery-and-private-layout-gap-20261017.md).
This checkpoint fixes the observed public packet-padding discrepancy in an
alternative candidate. It is **not byte-exact, installed, or matching credit**.

## Target And Storage Evidence

Owner `generated_11FF10`, original `asm/11FF10.s`: VA
`150F2D14..150F3194`, ROM `1201C4..120644`, 288 words / 1,152 bytes,
retail frame `0x150`. The production placeholder remains unchanged.

`tools/experiments/game_owner_burst_frame_trace.py` reuses the fingerprint-locked
CFE/UOPT/UGEN tracer on newly owned compiler children. Three independent traces
check fired probes, complete child/driver exit, captured stream identity and
normal-object code/functions/relocations/pools. Each isolated target reproduces
its full-owner target words and all 25 relative relocation bindings exactly.
No active debugger, compiler installation or dependency configuration changes.

All three traces contain exactly one procedure, **513 CFE / 466 UOPT records**.
Each observes four frame events: zero, 96 saved bytes, 144 saved-plus-outgoing
bytes, and the final frame. Outgoing arguments reserve 48 bytes. Observed
temporary pools, temporary size and temporary base remain zero; there is **no
observed late UGEN frame growth** in these traces.

| Candidate | CFE Local Bytes | UOPT Local Bytes | UGEN Aligned Locals | Final Frame |
| --- | ---: | ---: | ---: | ---: |
| Previous selected body | 188 | 200 | 200 | `0x158` |
| Descriptor alignment only | 192 | 204 | 208 | `0x160` |
| Descriptor and input-pair alignment | 196 | 208 | 208 | `0x160` |

Source-line markers bind decoded storage operands to actual statements.
Seven independent emitted-address checks cover the delta, both pointer pairs,
descriptor position, constructor descriptor argument, copied payload argument
and saved data pointer, plus the actual frame prologue.

The new aligned-pair form reproduces **every packet object's physical
caller-SP-relative address**, even though live SP and saved-register slots
still differ:

| Object | Previous Candidate | Aligned Candidate | Retail |
| --- | ---: | ---: | ---: |
| Delta | -172 | -180 | -180 |
| Output-pointer pair | -160 | -168 | -168 |
| Input-pointer pair | -152 | -160 | -160 |
| 52-byte payload | -144 | -148 | -148 |
| 88-byte descriptor | -92 | -96 | -96 |
| Saved data pointer | -4 | -4 | -4 |

The descriptor-only form moves the payload/descriptor correctly, but leaves
the pointer pairs and delta four bytes away. Adding 8-byte alignment to the
input-pair storage closes those remaining packet-address differences.
The u64-aligned unions are **layout proposals**, not proof of original
union/u64/double source types. Earlier helpers and checkpoints are not rewritten.

## Bounded Candidate Screens

`tools/experiments/game_owner_burst_storage_candidates.py` banks six complete
source proposals. Differences below compare the 288 overlapping retail words;
overflow is reported separately and is never silently discarded.

| Form | Words | Frame | Overlapping Differences | Overflow Words |
| --- | ---: | ---: | ---: | ---: |
| `aligned-pairs` | 288 | `0x160` | 85 | 0 |
| `aligned-const-scale` | 288 | `0x160` | 103 | 0 |
| `aligned-copy-phase` | 289 | `0x160` | 125 | 1 |
| `aligned-const-copy` | 289 | `0x158` | 141 | 1 |
| `aligned-inline-owner` | 294 | `0x158` | 243 | 6 |
| `aligned-inline-data` | 295 | `0x150` | 264 | 7 |

The useful aligned-pair candidate's raw SHA-256 is
`23e2faa5074572a4fddad79b0676cc091d94668583ecf8b952b8015c1dc5f079`.
Actual padding leaves its target words identical; all 11 raw/padded neighbors,
25 bindings and normalized owner pools remain unchanged. No guards are added.

The constant-scale screen is motivated by `D_800A196C`'s retail rodata location,
not a recovered C qualifier. Reusing post-transform union storage and removing
scalar homes do not solve matching. In particular, the frame-fitting 295-word
form has a seven-word overflow and is explicitly rejected by the real padder.
Its proposed volatile alias is not an accepted original declaration.

## Fresh Qualification

Six final tests pass in **68.711s**. These qualify research and deliberately
assert remaining failures; passing this suite is not installation acceptance.

- **3,900** ordinary comparisons plus **28** modeled FP-edge comparisons check
  complete public memory and complete call packets across retail/raw/padded
  images, with uniform and nonuniform stack contents and two stack phases.
  No padding bytes are masked. The previous nine copied payload-padding
  differences and constructor descriptor-hole differences are eliminated
  within this corpus. All 287 reachable retail words are reached; duplicate
  offset `0x8C` / VA `150F2DA0` remains unreachable.
- **39 effective fail-closed controls** reject corrupt storage/frame/pool
  observations, missing probe/lifecycle markers, altered wire captures,
  ambiguous source markers and a wrong emitted frame instruction.
- Native32 O2/O0 each pass **960 typed defined-field cases** with UBSan and
  six effective equality, signed-counter and copy-length controls. These do
  not qualify native padding or guest-private stack behavior.
- The first paired fault at cut zero still has a **16-byte live-SP mismatch**.
  The aligned body remains 85 words different, with frame `0x160` instead of
  `0x150`; full private/fault-prefix, caller and installation gates remain open.
- Random, transform, basis and constructor providers remain bounded opaque
  contracts. FP edges use the existing bounded model, not hardware traps,
  general FCSR, NaN-payload or gameplay acceptance.

The prior selected-body recovery/rebase receipts remain valid for their
unchanged inputs, but are **reused prior evidence**, not fresh aligned-candidate
rebase/private qualification. The corrected final six-test run above replaces
an earlier test-fixture error in the source-marker negative-control setup;
that failed run is not counted as passing evidence.

## Preserved Baseline And Resume

All **266 protected entries / 244 paths**, production source, guards, profiles,
conversion rows and earlier checkpoint fixtures remain unchanged. Complete ELF
SHA-256 remains
`5efb8a9f598af0712d97eaf4d0f2ab2df134e349ad16eddfeb0f75e74128b7d4`:
all 6,057 bodies/addresses and 189,088 Game-data bytes / 720 owners are preserved.
No new normal production build is claimed or required for uninstalled research.

Fresh match-progress is Game **2,964 / 4,828 (61.39%)**, total
**3,637 / 5,501 (66.12%)**, 1,864 different and zero address drift. Converted
counts remain 5,501 / 6,044 overall. Init 492/492 and Debugger 181/181 remain
byte-exact among converted functions. Root README is unchanged.

Tools **c2c5a97** is committed before the consumer docs/pin. Both tools copies
freshly pass 12 shared tests and their smoke checks. Six ASCII/AST parses and
three byte-identical task pairs pass. Mirror destinations were absent before
copying; all 1,134 prior hashes and HEAD `ddbdd16b` are preserved, with 1,137
dirty paths afterward. No mirror commit/reset, push, Claude call, host-port
change or frozen Release action.

- [x] Trace automatic-storage placement and bind wire coordinates to emitted addresses.
- [x] Qualify complete public packets without padding masks in the aligned proposal.
- [x] Reject misleading frame-only/overflow fixes and preserve the installed baseline.
- [ ] Continue this **same function** at UOPT's 12-byte local-area expansion
  and scalar-home lifetimes. The aligned local budget must shrink from 208
  to 192 bytes while retaining the retail packet addresses to obtain frame
  `0x150`; do not assume missing scalar declarations or absent spill events
  establish the cause.
- [ ] Then recover V0/V1 roles, saved FPR roles and setup scheduling, and
  qualify full private/fault behavior, rebases, callers and the complete first
  linked image before installation. Keep the 139-word gate, both fade lifetime
  gaps and wider Game goal open.

```sh
python3 -m tools.experiments.game_owner_burst_frame_trace --form aligned-pairs
python3 -m tools.experiments.game_owner_burst_storage_candidates
python3 -m unittest tools.tests.test_game_owner_burst_frame_trace -v
make -C conker match-progress NON_MATCHING=1
make tools-check
```
