# Game Owner Link Setup Recovery Checkpoint

Continue from [Note 1171](1171-game-owner-state-callback-direct-match-20261009.md).
Start at parent74d909afbfb60090ce7cc1d45502ec939c2a261e/toolsd6552d0.
One Codex writer, zero Claude calls; follow the scoped evidence loop in
[agent workflow](../AGENT_WORKFLOW.md). Commit tools first and the consumer
pin/docs second. No push or independent older tools checkout commit/reset.

## Status

**func_151B2348 remains complete original assembly, not matching C.**
VA151B2348..151B2690, ROM1DF7F8..1DFB40,210 words/840 bytes/frame0xA8.
The full [tracked fragment](../../conker/asm/nonmatchings/generated_1DF510/func_151B2348.s)
and [original owner](../../conker/asm/1DF510.s) are authoritative.
No production source, linked ELF, guard row or progress CSV changes this turn.
Root README aggregates stay unchanged; no conversion or matching credit.

## Recovered Contract

Capture second=actor+30 and first=actor+28 once, before any allocation.
The void actor routine constructs three requests and attachment packets:

| Call | Route | First Owner/Kind/Vector | Second Owner/Kind/Vector | Distance | Result Store |
| --- | ---: | --- | --- | ---: | --- |
| First | 2 | second/5/D_800AA350 | second/10/D_800AA35C | 80.0f | actor+40 |
| Middle | 1 | first/5/D_800AA320 | second/5/D_800AA338 | 170.0f | actor+3C |
| Last | 0 | first/5/D_800AA32C | second/10/D_800AA344 | retained170.0f | actor+38 |

Each endpoint packet is20 bytes: pointer0, code byte4 from owner+3B,
kind byte5, untouched bytes6/7, vector8..13. Two endpoints plus actor pointer28
and route byte2C make48 bytes; bytes2D..2F are also untouched.
Capture the two code bytes separately, including when endpoints alias.

The56-byte request has flags0, duration1000 at2, startXYZ at4,
endXYZ at10, active/enabled bytes1C/1D=1, extra1E=0, width20=5.0f,
kind24=3, distance28, limits2C/30 from D_800AA380/384 and tail34=0.
Start/end initially both use second's coordinates14/18/1C; later start uses
first, end uses second. Retain request fields between calls, except coordinates,
extra and the middle distance update. Do not clear/pad the original holes.

Each call is func_151B30B0(&request,0.0015f,48,255,0).
The float uses A1 bits3AC49BA6, not an integer-typed substitute.
The fifth argument is the outgoing stack word10.
After the first allocation, reload actor from its incoming parameter home and
retain pair=actor+28. Store every returned pointer, includingNULL, at pair+18,
pair+14, pair+10. Copy48 bytes to created+150 only for nonNULL.
No invented actor/endpoint NULL gate or result reread after memcpy.

## Actual Allocator Reference

Read the complete53-word wrapper151B30B0..151B3184, ROM1E0560..1E0634,
frame0x28, in [original allocator owner](../../conker/asm/1E0560.s).
Its C owner remains a false placeholder and is not changed in this checkpoint.
Recovered interface: u8* (void* request,f32 parameter,s32 extraBytes,u8 slot,s32 context).
It calls func_15167A68(0x33,context,extraBytes+0x150,1,slot,1),
returnsNULL on failure, otherwise copies56 bytes to created+10.
Its float calculation reads created+38, the request's distance field28,
not its width field20. It ORs created byte10 with0xE, computes twice
distance-squared/D_800AA390 at138, truncates distance*parameter*4096 at13C,
zeros16 bytes at140 and returns the retained created pointer.
This is static ABI/body evidence, not connected allocator execution.

## Complete Candidate Measurements

[Candidate driver](../../tools/experiments/game_owner_link_setup_candidates.py)
persists17 O2/g3 forms using real layouts, parameter lifetimes and local grouping.
There are no word guards, fabricated padding or production compiler-profile edits.

| Shape | Words | Frame | Raw Positional Word Differences |
| --- | ---: | ---: | ---: |
| Separate selected | 212 | 0xB0 | 200 |
| Grouped actor-home | 211 | 0xA8 | 192 |
| Grouped reused-actor | 208 | 0xA8 | 209 |
| Original | 210 | 0xA8 | 0 |

Same frame/nearby length does not mean nearly matched: packet placement,
saved-register allocation and retained-pair lifetime still differ.
Grouped actor-home places packetSP40/requestSP70 and spills pairSP30;
retail uses packetSP34/requestSP64 and retainedS2, with S0/S1/S2/RA saved
at20/24/28/2C. Grouped reuse retainsS2 but packetSP40/requestSP70 and the
incoming parameter-home stores/reloads differ.
Do not normalize hundreds of unexplained words or replace complete working assembly.

Earlier ignored experiments also tested four compiler profiles, integer result
types, early/array/typed pair forms, volatile pointer cells and whole grouped
workspace addresses. None qualified. These are historical exploratory evidence,
not additional persisted catalog coverage or new acceptance claims.

## Qualification

[Five-test recovery suite](../../tools/tests/test_game_owner_link_setup_recovery.py)
passes23.790s, zero skips. It checks:

- All17 full-body candidates, explicit nonmatching rejection, zero isolated
  diagnostics and no new literal pools; three discriminating shape receipts.
- 384 guest cases/768 executions covering eight allocation-success masks,
  four endpoint aliases, three seeded memories, mutation on/off and two stack
  phases. All210 retail words reached; saved-register return checks pass.
- Independent expected defined request/packet fields, ordered calls and public
  memory. Mutations change endpoint codes/coordinates and actor endpoint
  pointers between allocations; later requests retain captured endpoints.
- Each model's untouched private packet/request holes retain its own original
  stack seed. This is **not raw private-stack or copied-hole retail parity**.
- Five compiled effective negatives: wrong route/distance, late endpoint
  capture, omittedNULL result store and shortened packet copy.
- Native32 GCC compile-time size/offset checks only, **not native semantic
  execution**. Endpoint20/packet48/request56 bytes are verified.
- Original fragment and installed ELF slot equal all210 retail words.
  Source/wholeELF/guards/progress hashes are unchanged through the suite.

Allocator and memcpy are bounded hooks. Actual53-word wrapper/common allocator
integration, native semantic execution, independent symbol rebases, fault
prefixes, copied owner/padder acceptance and hardware/gameplay remain open.
No old constructor/state callback suite is reported as freshly rerun.
Ignored conker/build/game-owner-link-setup-test holds shape/guest/negative/layout/
unchanged receipts. The driver keeps scratch output outside production.

## Checkpoint And Next Step

Tools b7cdf231c22f035033f961aafde076ff6bb62bab commits the driver and focused suite
first; parent docs pin that exact revision. Mounted make tools-check and older
standalone check_project_tools.py pass. Preserve all96 older initial status
entries and both tracked dirty hashes/HEADddbdd16; copy only the two absent
authored files there, leaving98 status entries without committing that checkout.
Validation passes63 AST/exact-mirror pairs and158 documents/4,389 relative
links, zero broken links. Graphify update exits1, refusing17,159 nodes over
retained38,935 and preserving19,398 excluded-but-existing nodes from2,972 files.
Existing version/devcontainer warnings persist; no force/reinstall/purge.
The separate parent post-commit hook must finish before checkpoint close-out;
its result is an operational receipt, not match proof.

Source SHA256: 83e6cc2038b40094c0521589275f851eae341bd29325b56267bcfab9ae90ee30.
ELF SHA256: 7a42ef3e037f2d0665e3d35bf62e4be56d6586a6508586db75702bf5cef9dd84.
Guards SHA256: 1d9d7c6c3c0f0905aa40cd9f58c1d39c2aa46ec1aad9c8e7f0d097cdca8fc030.
Unchanged installed totals: Game2,737/4,814 exact; total3,410/5,487,
zero address drift and2,077 different. Converted5,487/6,042,85.91% bytes.

Resume with the grouped actor-home versus retainedS2/private-stack constraint.
A complete candidate must preserve the incoming actor-home lifetime, packet
holes/reuse and both endpoint captures while fitting210 words/SP34/SP64.
Then qualify raw packet provenance, actual allocator, native32, rebases and
copied owner/padder before installation. Helper151B2690 remains original
176-word assembly; the full renderer remains separate. Game goal stays active.
No OGL/Release/save/editor changes.
