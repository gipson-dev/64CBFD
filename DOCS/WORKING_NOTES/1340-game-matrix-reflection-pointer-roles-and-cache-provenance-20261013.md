# Game Matrix Reflection Pointer Roles And Cache Provenance

Date: 2026-10-13

## Scope And Result

Continue the full Game matching goal from consumer `2d444de2`, tools `f3e8f92`
and [Note 1339](1339-game-matrix-reflection-candidate-and-private-buffer-layout-20261013.md).
Target **func_15034F30**, VA `0x15034F30..0x150356C8`, ROM
`0x623E0..0x62B78`, **486 words / 1,944 bytes / frame 0x190**.
The production [source](../../conker/src/game/generated_61D10.c) is unchanged.

The [pointer-role screen](../../tools/experiments/game_matrix_reflection_roles.py)
selects **identity-through-restored-input**: **347 -> 333 literal differences**,
with **21 changed emitted words** relative to Note 1339. Extent, frame and
private matrix addresses stay fixed. This is **uninstalled, not byte-exact and
not credited**. No production source, ELF, guards, profile or progress changes.

The only selected source change reuses two existing pointer variables around
the identity call:

```c
saved = input;
input = (u8 *)reflection;
guMtxIdentF((f32 (*)[4])input);
input = saved;
```

No extra/dead local, padding, physical-register binding or copied instructions.
The emitted function does not store into the incoming input argument's home
at SP+0x19C. The source-level reuse does not establish a recovered retail idiom.

## Complete Source Screen

All **100 complete forms** compile through the prepared IDO toolchain. Among
forms retaining 486 words/frame0x190 there are **19 distinct literal arrays**;
none matches the first 23 retail words. Compare complete arrays, not only scores.
Families include signed/unsigned offsets, positive-count setup, array views,
pointer/flag qualifiers, flat/union storage, loop widths, captured banks,
goto/switch flow, existing-local hints and identity-call pointer reuse.

The score344 secondary cursor setup is rejected by a real access-lifetime
control, not by syntax. On mode2/count0/outputFixed0/disabled-actor input:

| Body | Own Memory Accesses | Output-Home Reads |
| --- | ---: | ---: |
| Retail | 54 | 2 |
| Banked347 | 53 | 1 |
| Cursor setup344 | 52 | 0 |

The lower score removes another retail output-home read. Wrong-extent/frame
forms also remain rejected. An unsigned-offset generator insertion error was
fixed before this final screen; a syntax error is not source-fitting evidence.

## Compiler Cache Evidence

The fingerprint-locked, newly owned compiler capture fires, completes with
exit0 and preserves the complete normal/traced object and pools. Frame writes
remain **88 -> 104 -> 400**, with locals/saved/outgoing **296/88/16**.
Optimizer definitions remain M292/P76, and the four matrices remain at
M offsets **-268/-192/-128/-64**, or SP+0x84/0xD0/0x110/0x150.

Selected optimized-stream address records:

| Byte Offset | Opcode | M Offset | Raw Register Word |
| ---: | --- | ---: | ---: |
| 744 | rlda | -64 | 30 |
| 1,472 | rlda | -268 | 19 |
| 5,600 | rlda | -268 | 19 |

The emitted opening contains **27BE0150**, `addiu fp,sp,0x150`.
Reflection-address caching is already represented in the optimized stream;
it is not merely a later UGEN instruction-scheduling difference. Raw words
are retained alongside emitted confirmation. The decoder's generic `length`
field on rlda is not a matrix size and must not be reported as one.

Retail instead preserves the input bank in s6 at the opening, uses s2 for the
shifted matrix index across concatenation, and rematerializes reflection's
address at calls. Selected333 still opens with AFBE0060 and caches reflection
in fp; its input bank is s5. Neither the saved roles nor their fault lifetime
are restored by the score improvement.

## Flag Lifetime Control Correction

An ordinary `s32 encoded = outputFixed` source initializer emits486/frame0x190/
345. It **does not** produce the hypothesized early snapshot: a controlled
guMtxIdentF action changes argument slot18 from0 to1, and retail, banked347,
selected333 and initializer345 all perform fixed output conversion with
identical complete sampled RAM. Do not reject this form merely by reading
its C initializer position or claim that an early-load fault was observed.

A separately compiled **volatile** snapshot is an effective runtime negative:
487 words/frame0x188, empty compiler diagnostics, the same action fires, but
it misses conversion and produces different public RAM. This deliberately
forced control is not a proposed declaration, eligible extent or actual SDK
behavior. The initial failing test assumption was corrected from emitted
execution evidence; no production contract was relaxed.

## Qualification And Limits

The [focused suite](../../tools/tests/test_game_matrix_reflection_roles.py)
inherits the complete Note 1339 contracts and replaces its historical layout
screen with this 100-form role screen. The original recovery fixture remains
unchanged. Fresh final target/text qualification passes **19 tests in107.605
seconds**:17 role/semantic/layout/fault checks and the two unchanged protected
text-input/corruption controls. The three newly strengthened shape/cache/flag
checks separately pass in4.589 seconds. The earlier rehearsal failed the false
flag-negative assumption and two mistyped module selectors; those are not
passing receipts. This fresh run uses the corrected controls and actual selectors.

- 4,800 guest cases match complete sampled RAM and helper-input packets.
- 48 overlapping-buffer cases and 18 live-home cases pass, including the
  post-callback actor-home replacement and original count/output reloads.
- 256 native32 cases per O2/O0 profile preserve actual body behavior, numeric
  matrix words, opacity and bank restoration; four runtime negatives remain
  effective. This is the same bounded native ABI/provider scope as Note 1339.
- Both complete owner padders preserve all nine neighbors, relocations and
  pools. Both authentic caller windows forward all19 slots at phases0/8.
- Three independently assembled original links and216 rebased semantic cases
  preserve the call/relocation contract, without claiming byte exactness.
- The same mixed-format alias reaches the same rejected provider boundary.
  Final mixed-format results and unrestricted provider behavior remain open.

Full modeled own-access fault sweeps cover **128 domains**, from four modes,
counts0/1, four flag combinations, phases0/8 and actor-word gates0/256.
All **6,912 common cuts** actually fire in original/banked347/selected333.
Old/new own-access counts agree on each domain; **128 original-state
agreements remain 128**, with **no prior equal state lost** and no new one.
The state comparison includes sampled RAM, GPRs, FPRs, modeled FCSR/condition,
LO/HI, own events and raw helper calls. It does not repair the opening cut1:
only pre-access cut0 agrees on these domains. The fixed-input return witness
still differs in GPR9/13 despite equal sampled RAM/FPRs.

This is not exhaustive all-input fault qualification, hardware PC/BD/full
FCSR, execution of SDK/provider implementations, complete parent execution,
emulator/gameplay proof or a direct/guarded matching result.

## One Advisory And Independent Reconciliation

One earlier packet-only Claude advisory completed on firstParty/claude.ai Pro,
with tools and MCP servers disabled, no tool calls and no permission denials.
Its retained packet digest is
`a1fdf726f34b4f7a224e1d00a8669abcb482a24177be4d683e3c01d1edb52e9b`.
There are no additional calls for this question.

The observed retail/source cache contrast is supported. The proposed cause,
that a competing cross-call index must evict reflection, is **unproven**.
Shared top-of-loop indices and direct array passing duplicate existing probes;
the output expressions already used the same index local. The same scalar
assigned in both format arms emits the unchanged486/frame0x190/347 array.
Two address/cursor combinations emit492/frame0x198/476 and are rejected.
An independent input cursor stays486/frame0x190/347. No advisory agreement
is treated as implementation evidence. Selected333 is a separate pointer-use
probe. Read-only profile counters likewise do not establish retail flags.

## Frozen Production And Banking

All seven target inputs and all nine protected text inputs remain identical
to their retained snapshots. Protected Game data: **189,088 bytes / 720 owners /
zero different**. Guards remain14,770 rows, with zero for this target. No
immutable fixture rebase. Totals remain Game2,824/4,823, total3,497/5,496,
1,999 different and zero drift. The root README remains byte-identical.

Both tools copies pass ROM-free wrapper checks and Windows byte-compilation.
Tools **fb429816306affcc47fa764661342bf7315b50ee** commits only the two new role
files first. The consumer records that exact gitlink with these docs; no
production files or root README are part of this checkpoint.
The older mirror retains HEAD ddbdd16 and **all432** initial dirty-path
fingerprints; only the two previously absent role files are added, giving434.
No push, duplicate mirror commit, reset, host edits or Release work.

Direct `graphify update .` refuses the shrink:18,710 proposed versus40,490
existing nodes. Preserve the19,398 retained nodes/2,972 excluded-file and
skill0.9.20/package0.9.26 warnings; do not force an overwrite. Incremental
commit-hook completion and exact commit identities are recorded after banking.

Reproduction from the prepared consumer root under WSL:

```sh
python3 -m unittest tools.tests.test_game_matrix_reflection_roles \
  tools.tests.test_game_text_measurer_recovery.GameTextMeasurerRecoveryTests.test_05_production_and_protected_data_unchanged \
  tools.tests.test_game_text_measurer_recovery.GameTextMeasurerRecoveryTests.test_06_effective_immutable_production_controls -v
make tools-check
```

## Next Work

Keep the full Game goal active on **this same function**. Recover the opening
input-bank/reflection saved roles and cross-call shifted-index lifetime using
source-derived candidates and fired compiler records. Preserve the19-slot ABI,
four real matrices, all sampled RAM/home/caller contracts and every prior
fault-state agreement. Finish the remaining333 words and private/fault/linked
image gates before installation or credit; do not normalize the body wholesale.

## Post-Bank Verification

Consumer **f84a413be938391fdd246b6cf35fa7e3f7af4797** records the exact tools
**fb429816306affcc47fa764661342bf7315b50ee** pin and these working docs.
Both active checkouts are clean after banking. All nine newly added relative
documentation links resolve; root README SHA256 remains
`640d27f289d843d625eabd94f747b399fc31105726db2a78ab245962ac885e8c`.

Four fresh post-bank checks pass **in3.938 seconds**: all seven frozen production
inputs, complete sampled private RAM/return-register boundary, literal opening
fault boundary and the corrected flag lifetime/control. They do not remove
the measured GPR9/13/cut1 differences or establish matching credit.

The incremental hook completes at **40,502 nodes / 80,993 edges**, with no live
workers. It preserves the retained/excluded corpus and skips oversized HTML.
This successful scoped refresh does not turn the direct shrink refusal into
a successful full rebuild. No push or host/Release operation is performed.
