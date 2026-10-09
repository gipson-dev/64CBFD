# Game Owner Descriptor Constructor Direct Match

Continue from [Note 1169](1169-game-endpoint-pair-callback-direct-match-20261009.md).
Start clean at parent72c3a187801d478d5240b90776e6bec8d41a61e4 and tools
c6b2d59bc38c5acdee2f58be4680a5c7e4d28ce2. One Codex writer, zero Claude calls.
Tools-first authorized local commits, no push. Preserve older standalone
HEADddbdd16 and all92 initial entries/dirty tracked hashes.

## Installed Result

**func_151B2060 directly matches all40 retail words**, frame0x50, four JAL
relocation uses, zero pools/guards/isolated diagnostics, under existing O2/g3.
Replace its false12-byte zero-return placeholder with the complete160-byte
void constructor and scoped descriptor declarations in
[generated_1DF510.c](../../conker/src/game/generated_1DF510.c).
VA151B2060..151B2100, ROM1DF510..1DF5B0; full retail reference
[asm/1DF510.s](../../conker/asm/1DF510.s) is unchanged.

[Complete-body driver](../../tools/experiments/game_owner_descriptor_candidates.py)
screens six forms/four profiles,24 rows. Selected created-local-first form
matches40/frame0x50/zero differences. Descriptor-first remains40/0x50/eight
differences: its descriptor is shifted four private bytes. Reordering the
two actual locals recovers original SP2C; no dummy variable, fabricated
work, padding, profile or guard changes. Selected plain O2 is38/0x50/38
differences; O1/g3 is45/0x50/42 and O1 is45/0x50/43.

## Complete Descriptor And Calls

The actual32-byte descriptor contains owner pointer at0, captured owner
byte at4, resource pointer at8, active/state bytes atC/D,12 cleared bytes
at10 and a zero word at1C. Five bytes at5..7/E..F remain untouched.
Private descriptor is SP2C..4B; RA saved at SP24. No savedGPR/FP pairs.

NULL owner returns without calls or public reads/writes. Otherwise:
capture owner and owner[3B] before func_15083E90(1); retain its result even
if zero; set active1/state0; SDK bzero clears exactly12 bytes; set final
word0; call func_151491F4(300,-1,0x16,0,0x12,32,255,1).
On allocation success copy all32 descriptor bytes to created+28, including
retail holes. Allocation failure skips memcpy. The function has void
semantics; no invented return value, resource-NULL gate or zeroed holes.

The sole found caller func_1514DB64 ignores a result and gates the call on
D_800BE9F0==0x14. JAL1514DB80/ROM17B030; actual caller is13 words.
[Caller source](../../conker/src/game/generated_179F30.c) and retail agree.
Actual28-word func_151491F4 inserts signed -1 in the fourth argument to
func_15149130, forwarding all remaining widths/values. The common allocator,
resource provider and SDK clear/copy remain bounded hooks in qualification.

SDK bzero is already declared void(void*,int) through ultra64.h; reuse it.
An initial local s32 redeclaration failed because guest s32 is long, not
the SDK's int despite their equal O32 width. Removing the redeclaration
fixes the compile without suppressing diagnostics. No shared header change.

## Qualification

[Eight-test suite](../../tools/tests/test_game_owner_descriptor_match.py)
passes before installation in14.381s and **latest after installation in51.065s**,
no skips. Initial earlier full run14.461s and installed run15.044s also passed.
Final fixture refines canary checks to compare addresses only within the same
backing array and accepts only the intended negative-control rejection labels.

- All40 raw words/frame/four relocations match, no target guards/pools.
- 6,146 guest cases/12,292 executions cover every word, all owner bytes,
  both NULL paths, allocation failure, five resource patterns, output/owner
  aliases, both stack phases and three seeded private patterns.
- Independently expected descriptor compares all32 bytes, including five
  holes. Resource mutation verifies owner pointer/byte were captured first;
  scratchGPR/FP and argument-home clobbers cannot corrupt the private packet.
- Actual13-word context caller connected to the actual28-word allocation
  wrapper passes60 cases with gates0/19/20/21/FFFFFFFF, NULL/non-NULL owner
  and allocation, owner aliases and both phases. Verify all nine common
  allocator arguments; helper mutations change the global gate after capture.
  Common allocator/resource/zero/copy remain hooks, not full hardware proof.
- 7,680 actual native32 typed constructor and actual caller-source cases
  verify defined fields, exact helper sequence/widths, both NULL paths,
  allocation failures and all external canaries. Raw private holes are
  deliberately not compared natively; native follows existing32-bit fixture.
- Copied owner preserves17 neighboring bodies, pools and relative relocations;
  the actual padder accepts. Four existing Warning712 messages are preserved,
  zero new warnings; isolated target compiles clean.
- Five compiled negatives are rejected by expected argument/capture
  checks: late owner byte, wrong resource argument, short clear, wrong kind,
  short copy. Not all negatives are claimed as final-memory-only controls.
  Exact accepted labels are owner-byte-capture, resource-arguments,
  clear-arguments, allocate-arguments and copy-arguments respectively;
  unrelated oracle assertions are test failures, not accepted rejections.
- Four independent original/candidate symbol sets/eight links/four relocation
  uses/96 cases/192 executions preserve byte equality and raw memory/events
  across JAL regions, NULL paths, mutation and owner aliases.
- Missing owner byte faults before any helper; original/candidate prefixes
  agree. Guest fault order does not prove portable C invalid-pointer behavior.
- Whole-ELF audit permits only the160-byte slot and verified st_size12->160.
  Every other code/data/symbol/address/metadata byte is preserved. Actual
  connected bodies remain byte-exact to their complete retail routines.

No emulator, whole common allocator/resource integration, hardware or visible
gameplay acceptance is claimed. Older constructor/renderer/alpha/endpoint
suite receipts are historical, not fresh reruns. This install supersedes
their whole-ELF history fingerprints; do not recapture old baselines.

## Build And Progress

Fresh make -C conker -j4 build/conker.us.elf progress.csv and
make -C conker match-progress NON_MATCHING=1 both exit0. A temporary literal
newline escape in the manual insertion caused an initial compile failure;
remove that stray line and rerun successfully, no warning suppression.
Existing generated_12D630 duplicate-recipe warnings and four owner Warning712
integer-to-pointer calls remain: two func_151B220C, two func_151B2FD0.

| Section | Byte-exact | Drift | Different |
| --- | ---: | ---: | ---: |
| Total | 3,409/5,489 (62.11%) | 0 | 2,080 |
| Init | 492/492 (100%) | 0 | 0 |
| Game | 2,736/4,816 (56.81%) | 0 | 2,080 |
| Debugger | 181/181 (100%) | 0 | 0 |

One new exact function; no conversion credit because placeholder was counted
as C. Converted functions5,489/6,042, Game4,816/5,321 unchanged; converted
bytes85.98% total/85.33% Game. Guard/progress CSVs byte-identical,11,510 guards.
Root README changes only the two aggregate match rows.
Protected Game data189,088 bytes/720 owners, zero differing bytes/owners.

## Immutable Evidence

Ignored conker/build/game-owner-descriptor-test holds before-source/elf/
guards/progress and baseline.json, plus shape/guest/connected/native/owner/
rebases/faults/audit receipts. Final driver24 rows live in
conker/build/game-owner-descriptor/measurements.json.
Without the ignored immutable pre-install baseline, a prepared clone's
history audit explicitly skips after connected-body checks. This checkout
has its original baseline and no skips.

| Artifact | Before SHA256 | Installed SHA256 |
| --- | --- | --- |
| Owner source | d073be9f0303c7d748137fd54ab51b5afc2ba06fd4a56c28a6ae9e6811cf9455 | cc133b478920aaea4c11130a9127437f5b2069190090d3d912f0490333fc77ce |
| ELF | 994d45f06c10d21941b643b731f239382382488f87cf6c67dd613858765fe704 | 5a8540f1093c566336ff4cf268c8ab6bd03d63adcbc3c47c6a72980c4a8a786a |
| Guards | 1d9d7c6c3c0f0905aa40cd9f58c1d39c2aa46ec1aad9c8e7f0d097cdca8fc030 | unchanged |
| Progress CSV | 5c104a10b09965a84863a7b353b1bfb1e49d3a56d0760cdba6383fa71fb92f24 | unchanged |

Protected Game data SHA256:
0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670.

## Checkpoint

Tools0353bcbe59528737408acc58bce2df3fe9034e2c is committed first, containing
only the complete-body driver and eight-test suite. Parent source/docs pin
that exact revision; no push. Fresh make tools-check and older standalone
check_project_tools.py pass. Scoped validation passes59 AST/exact mirror
pairs and156 documents/4,365 relative links with zero broken links.

The independent older tools checkout retains its HEADddbdd16, all92 original
status entries and both original dirty tracked hashes. Only the two absent
authored driver/test files are copied there, producing94 entries; no older
commit, reset or history duplication.

Both manual Graphify updates finish exit1: refuse17,140 nodes over the retained
38,916-node corpus, preserving19,398 excluded-but-existing nodes. No force,
reinstall or purge. The parent post-commit rebuild is a separate receipt;
wait for its processes to finish before reporting the checkpoint.

## Next Target

Recover **func_151B2100**, same owner,67 words/268 bytes/frame0x38.
VA151B2100..151B220C, ROM1DF5B0..1DF6BC; still a zero-return placeholder.
Its complete retail consumes this descriptor: validate both endpoint
objects, sentinel bytes and captured owner codes; invalidation stores
signed -1 at actor+E. Otherwise capture previous state, call151B22F4,
store/reload the new byte state, clear attached records on transition,
and conditionally run151B2348/151B2690 while respecting callee mutation.
Actual callback-table pointer8008A540, selector0x16 in D_8008A4E8, corresponds
to this constructor's kind. Initial evidence only, not a matched/qualified body.
Preserve full ribbon renderer and handwritten live-register workstreams.
Game goal stays active. No OGL/Release/save/editor changes.
