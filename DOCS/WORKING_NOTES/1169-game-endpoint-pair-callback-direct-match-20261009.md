# Game Endpoint Pair Callback Direct Match

Continue from [Note 1168](1168-game-ribbon-alpha-defined-signed-scaling-20261009.md).
Start clean at parent2b8321ddd77b352e2f2bb1485b2af2634dff39a7 and
tools0269fbbef6e8b09d09fce0ca7bf12dccb3a3ab9e. One Codex writer, zero
Claude calls; tools-first authorized local commits, no push. Preserve older
standalone HEADddbdd16 and all90 initial entries/dirty tracked hashes.

## Installed Result

**func_151B2F04 directly matches all39 retail words**, frame0/pools0/
relocations0/guards0, using the existing O2/g3 profile. Replace its false
12-byte zero-return placeholder with the complete156-byte void callback in
[generated_1DF510.c](../../conker/src/game/generated_1DF510.c).
VA151B2F04..151B2FA0, ROM1E03B4..1E0450; full retail reference is
[asm/1DF510.s](../../conker/asm/1DF510.s).

[Driver](../../tools/experiments/game_endpoint_pair_candidates.py) screens
six complete forms/four profiles,24 rows. Selected O2/g3 is39/0/zero raw
differences; plain O2 is38/0/37 differences. O1/g3 and O1 are50/frame8/48.
Early-return and unsigned-word forms also match under O2/g3. Moving pair
address calculation inside the gate changes42 words; owner-relative form
remains39 words but has23 differences. Profile/shape alone is not equality.
No guards, generated assembly replacement, dummy locals or padding added.

## Actual Callback And Semantics

The existing table declaration is void(*)(struct260*,s32,u8).
[Actual dispatcher source](../../conker/src/game/done/game_1765E0.c)
func_15149434 and its complete23 retail words confirm three O32 arguments,
void result, byte command truncation and selector bounds0..73.
The target is selector18 in D_8008A8D8, actual pointer8008A920.
[Retail table](../../conker/asm/data/22EF80.rodata.s) and linked ELF agree.

Recovered semantic signature is void(u8* owner,u8* packet,u8 kind).
The packet argument is a32-bit address; the current generic table represents
it as s32. Native qualification uses a typed adapter for that table contract,
not an incompatible function-pointer cast. No shared header/table/dispatcher
change is made. This is O32 ABI qualification, not proof that all native
declarations throughout a future host port are reconciled.

Only kind0x2D operates. Owner endpoint words are at28/30, associated bytes
at2C/34. Packet endpoint words are at0/4, associated bytes at8/9.
For each destination endpoint, replace packet-first with packet-second
and byte9, or packet-second with packet-first and byte8, preferring the
first comparison when endpoints are equal. No other destination changes.

After a first-endpoint match, retail reloads packet word4 and then word0.
These reloads follow both the endpoint store and associated-byte store;
overlapping packet/destination layouts can therefore change the second
comparison. Do not pre-cache both packet endpoints or treat the two
updates as an unordered simultaneous swap. The independent ordered
reference tracks captures and reloads separately, matching branch-likely
load annulment and lazy associated-byte reads.

## Qualification

The [eight-test suite](../../tools/tests/test_game_endpoint_pair_match.py)
passes before installation in10.192s and **after installation in12.221s**,
no skips.

- All39 raw words match, original profile preserved, five alternate complete
  representations screened by the driver; no target guards or diagnostics.
- 4,352 independent guest cases/8,704 executions compare full seeded memory,
  ordered loads/stores, all command/associated-byte values, four endpoint
  equality classes/high-bit patterns, eight alias layouts and both stack phases.
- All38 reachable words covered. Retail word17 is an unreachable duplicate
  load between the unconditional branch and its target; no fake coverage.
- 194 missing-byte pairs compare fault prefixes and full memory;48 caller
  argument-home aliases and255 nonmatching-command lazy cases also pass.
  Invalid pointers, argument-home aliases and fault order qualify guest
  instructions only, not portable C invalid-pointer or hardware behavior.
- 13,056 actual native32 cases compare complete1,024-byte memory canaries
  against an independent bytewise reference. Typed direct callback and
  actual dispatcher source with selector-layout projection are compiled.
  Its existing integer packet interface uses a typed adapter, other table
  slots bounded NULL; native tests retain existing -fno-strict-aliasing mode.
- Copied-owner compilation preserves17 neighbors, pools and relative
  relocations; the real padder accepts. Four existing Warning712 diagnostics
  are unchanged in both copies, zero new diagnostics. Isolated target is clean.
- Five compiled negatives change final memory: wrong gate, wrong associated
  byte, omitted second update, wrong destination byte, cached packet endpoints.
- Four independent original/candidate symbol sets, eight links and240
  guest cases preserve exact39-word bodies; zero relocation uses.
- Actual23-word retail dispatcher runs2,048 routing/command/phase cases,
  4,096 executions, across all selector bytes. Both bodies agree on ordered
  accesses, calls and full memory; selector18 executes the real target code.
  Other slots are bounded NULL, not their real callbacks. Actual linked
  dispatcher is byte-exact to retail and actual selector18 pointer is verified.
- Installed whole-ELF audit permits only the156-byte target slot and
  verified target st_size12->156. All other bytes, symbols/addresses and
  metadata remain unchanged. Guard/progress CSVs are byte-identical.

Initial eight-test run failed native initializer braces and a fixture's
incorrect zero-owner-warning expectation. Fix those local fixtures; do not
suppress warnings or change unrelated production calls. The corrected
focused two-test run passes in6.392s. Complete corrected suites above are fresh.
No emulator/hardware/gameplay or all other callback-table routes are proved.
Historical neighbor-suite receipts are not presented as freshly rerun.

## Build And Progress

Fresh make -C conker -j4 build/conker.us.elf progress.csv and
make -C conker match-progress NON_MATCHING=1 both exit0. Existing
generated_12D630 duplicate-recipe warnings and four owner Warning712 messages
remain: two func_151B220C and two func_151B2FD0 integer-to-pointer calls.
Leave their separate ABI recovery work unchanged.

| Section | Byte-exact | Drift | Different |
| --- | ---: | ---: | ---: |
| Total | 3,408/5,489 (62.09%) | 0 | 2,081 |
| Init | 492/492 (100%) | 0 | 0 |
| Game | 2,735/4,816 (56.79%) | 0 | 2,081 |
| Debugger | 181/181 (100%) | 0 | 0 |

One new exact routine; no new conversion credit because the placeholder
was already counted C. Converted functions remain5,489/6,042, Game4,816/5,321;
converted bytes remain85.98% total/85.33% Game. Guards remain11,510.
Root README changes only its two aggregate match rows.
Protected Game data remains189,088 bytes/720 owners, zero differing bytes/owners.

## Immutable Evidence

Ignored conker/build/game-endpoint-pair-test holds before-source/elf/guards/
progress and baseline.json, plus shape/guest/faults/native/owner/rebases/
dispatcher/audit receipts. The final24-row driver catalog is in
conker/build/game-endpoint-pair/measurements.json.
The local installation audit explicitly skips if its immutable pre-install
baseline is absent in a prepared clone; this checkout has it, no skips.

| Artifact | Before SHA256 | Installed SHA256 |
| --- | --- | --- |
| Owner source | 3cfa29f32fd1d2e25471356060b6b053bdc17e3a5880addaadd645b04293c56b | d073be9f0303c7d748137fd54ab51b5afc2ba06fd4a56c28a6ae9e6811cf9455 |
| ELF | 054e17ad283ea120ed7e8a370ceb5c378cad08f891cd88ee872150e6902f4751 | 994d45f06c10d21941b643b731f239382382488f87cf6c67dd613858765fe704 |
| Guards | 1d9d7c6c3c0f0905aa40cd9f58c1d39c2aa46ec1aad9c8e7f0d097cdca8fc030 | unchanged |
| Progress CSV | 5c104a10b09965a84863a7b353b1bfb1e49d3a56d0760cdba6383fa71fb92f24 | unchanged |

Protected Game data SHA256:
0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670.
This genuine install supersedes earlier whole-ELF history receipts; do not
recapture old renderer/constructor/alpha baselines to conceal the change.

## Next Target

Toolsc6b2d59bc38c5acdee2f58be4680a5c7e4d28ce2 banks exactly the driver and suite first,
then source/docs and exact consumer pin. Both tools checks pass;57
AST/exact-mirror pairs and155 documents/4,354 relative links/zero broken pass.
Mirror only the two absent authored files; older checkout ends with92
entries, all90 initial entries and dirty hashes/HEAD preserved, no older commit.
Manual graphify update exits1 refusing17,130 nodes over retained38,906,
retaining19,398 excluded-but-existing nodes; no force/reinstall/purge.
Existing version/devcontainer warnings remain. Wait the separate parent
post-commit graph hook before final clean-state checks.

Recover **func_151B2060**, same owner,40 words/160 bytes, still a false
zero-return placeholder. Complete retail is null-gated, captures an owner
pointer/byte, obtains func_15083E90(1), clears12 descriptor bytes, allocates
kind0x16 via func_151491F4 and copies32 bytes on success. Packet holes and
allocator failure behavior need explicit recovery, not default zero filling.
Its found caller is func_1514DB64, JAL1514DB80/ROM17B030, gated by
D_800BE9F0==0x14; it ignores a return value. Recover the actual callback/
return contract before installation. Initial handoff, not a matched body.
Keep the full ribbon renderer and handwritten live-register fragments open.
Game goal stays active; no OGL/Release/save/editor changes.
