# 1744 - Registered record color command callback directly matched

Verified: 2026-10-27. Target: `func_150FA468` in `generated_126F60`.

## Result

Replace the zero-return placeholder with the complete semantic callback. All
46 words /184 bytes emit directly from the existing O2/g3 profile, including
frame 0x18 and both R_MIPS_26 call bindings. No guards, profile overrides,
assembly replacements or shared-header changes are added. Preserve all 17
other functions and the owner's pools in both raw and padded objects.

- VA: `150FA468..150FA520`; retail ROM: `127918..1279D0`.
- Canonical interface: `void(struct260 *record, s32 eventAddress, u8 command)`.
- The second argument is unused. The incoming full third word is homed, then
  its low byte controls dispatch. The old s32 return was a placeholder artifact.
- Commands 0x4C/0x4E/0x4F write -1 to byte 0x11; 0x4D writes 30. Other commands
  leave the record unchanged. 0x4C submits black, 0x4F white, each with priority
  255. The record store happens before the provider call.
- Existing `struct260` supplies the real byte layout and callback type; retain
  the unknown field name `unk11` rather than inventing a shared semantic rename.

## Registry, caller and provider

The actual 74-entry `D_8008A8D8` registry selects this callback at index 65
(VA 8008A9DC /ROM 22F49C). The aligned retail census finds this single pointer
literal and no direct JAL. `func_15149434` is the complete 23-word dispatcher:
it reads byte 0x13, maps indices at least 74 to zero, checks for a non-null
entry, and passes the record, event word and unsigned command byte. The typed
current C and retained object already match that original dispatcher.

`func_1515D4D4` is the existing 19-word RGB/priority provider. Its actual C
interface is `void(s32,s32,s32,u8)`. The callback always requests maximum
priority, so this route writes RGB bytes, sets D_800DCD7C to one, and writes
D_800DCD27 to 255. Original and retained provider instructions are identical.
The integrated checks cover this maximum-priority route; they do not claim
new qualification of every possible provider priority or other registry body.

## Fresh qualification and explicitly reused evidence

Both tools copies execute all eight canonical methods freshly (primary
6.805s; mirror 6.760s), with zero errors, failures or skips. Both shared
`check_project_tools.py` checks pass.

- 6,192 guest cases cover every command byte, three full incoming-word
  patterns, four initial byte values, two stack phases and five alias layouts.
  All 46 words are visited; original and emitted private state agree exactly.
- 6,144 complete original/retained dispatcher cases cover all 256 selector
  bytes and the real registry. All 23 dispatcher words are visited. Other
  callback implementations are explicit bounded call contracts.
- Native32 O0/O2/O3 each pass 10,752 positive cases using the actual dispatcher
  and color-provider C, typed indirect calls and trapping UBSan. Eight
  functional/order negative controls fire, including late record stores.
- 45 instruction-access fault prefixes fire. An unknown command needs no
  record mapping. An actually compiled unused-event read is rejected against
  unmapped event memory. These are guest-order checks, not portable C faults.
- Six independent GNU links across three layouts preserve both call bindings,
  including a different JAL address region, with 36 rebased guest cases.
- 360 original/retained provider integration cases cover aliases and priorities
  0/254/255, checking RGB, active and priority outputs. Every provider word is
  visited. No emulator, R4300 hardware or live gameplay acceptance is claimed.
- Raw-body/binding negative controls, seven full-image corruptions and three
  wrong-input cases are rejected. All 94 focused inputs and 16,147 sealed
  Native/cache files are checked with four declared adoption overrides.

The actual three-command Make recipe reproduces all 18 compact functions and
the full padded object. Ordinary production Make passes in 0.595s. Each tools
copy then runs two fresh installed owner/image methods; six semantic methods
are reused only after module, snapshot, raw/Make artifact and sealed-input
fingerprints exactly match their fresh private executions. Unchanged broad
neighbor suites are retained receipts, not reported as fresh executions.

## Independent linked image and actual recount

The complete ELF equals the predecessor with exactly 136 target code bytes
and one target symbol-size byte changed: 137 bytes total, zero exclusions.
There is no metadata serialization allowance. All 6,056 function addresses,
6,055 other bodies, conversion CSV and guard history remain fixed. Protected
Game data is exact across 720 owners /189,088 bytes, SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

The captured, adopted Native ELF recount is total 3,821/5,506 (69.40%),
Game 3,148/4,833 (65.14%), Init 492/492 and Debugger 181/181, with zero
address drift and 1,685 different C functions. Reaching 75% requires 4,130
exact functions, 309 more at the current denominator. Remaining source-shape
triage is 1,556 placeholders, 120 semantic/other definitions and nine unlocated
entries; these classifications alone provide no matching credit.

## Ownership and reproducibility

Baseline consumer `06ae54639dfb699ec5a6ae95ccd6d09cab1cdef8`; tools
`9cdb3266bd81e8162e125699d24bafdae738b9ee`. The qualified tools pair is
banked first in `dab739dda5fa3c40fa69da2420611a54d4e5a0b1`, then pinned by
the consumer commit. Preserve the older mirror's 1,698 inherited dirty paths;
only this target's two additional files are written there. Nothing is pushed.

- Snapshot SHA-256: `b3729c1d65035e289aa41ab748dd0a3b47125e6ffc1d744146d47b3d19638fd0`.
- Complete raw target SHA-256: `afaf85b67a60ad1f1817ea2d7cfbd7175ba906766d22c0c2a8c5de9615ee56ee`.
- Padded object SHA-256: `49674b5f19ea6f835ebc250240949d6259a5b7218d577517813787c2cd748458`.
- Adopted ELF SHA-256: `fab3176a559a9a2b3a7e9a61539fa4e48b94c953b3819893b6454bfef01084f4`.
- Reproduce: `python3 -m unittest tools.tests.test_game_record_color_command_match -v`
  from the prepared consumer/cache; ignored evidence lives in
  `conker/build/game-record-color-command-match/`. Each execution uses a new
  PID-specific output directory; frozen inputs and prior receipts are retained.

Codex owns implementation and validation. Routine Claude budget: zero calls.
Refresh the changed-source Graphify graph and retain independently checked
old nodes/valid relationships; scoped extraction is not full-corpus analysis.
The wider 75% goal stays active. Next screened placeholder `func_15116058`
(`generated_142560`, 46 words) is uncredited pending its own full gates.
