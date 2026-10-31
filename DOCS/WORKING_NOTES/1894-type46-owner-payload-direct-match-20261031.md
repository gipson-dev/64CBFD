# 1894 - Type46 owner payload callback: direct C match

Date: 2026-10-31. Function: `func_1514D564`.

The zero-return placeholder in `conker/src/game/generated_179F30.c` is replaced
with the recovered owner callback. VA `0x1514D564..0x1514D64C`, ROM
`0x17AA14..0x17AAFC`: 58 words / 232 bytes, with no alignment words.
All words and all 11 relocation bindings emit directly from semantic C under
the existing O2/g3 profile. No guards, inserted words, omissions, assembly
injection or shared-header changes are used.

## Recovered behavior and ABI

`void func_1514D564(u8 *owner)` captures the owner pointer and byte `0x3B`,
command 6, and float values 0, -180 and 77 in a 20-byte local extension.
It builds a 36-byte Type46 descriptor from the original four float constants
and owner coordinates at `0x14/0x18/0x1C`, with enabled/mode bytes equal to 1.
It requests 20 extra bytes from `func_150C5370`; allocation failure skips the
copy and final event. On success it copies the extension to record+`0xC8`
and calls `func_1514EC1C(record, owner, 0x15)`.

The 88-byte frame preserves RA at SP+20, extension at SP+28, record home at
SP+48, descriptor at SP+52 and incoming owner home at SP+88. Local declaration
order and early enabled-byte initialization recover retail scheduling and
layout. Initial unsuccessful scheduling experiments remain in the ignored build.
The raw disassembly from the first attempt is historical; selected-final.o,
selected-exact.json and the qualified object are authoritative.

`D_8008AA70` is a 23-entry callback table; slot16 is this routine at ROM
`0x22F570` / VA `0x8008AAB0`. The original `func_1514D15C` dispatcher has three
indirect sites at `0x1514D264`, `0x1514D2A4` and `0x1514D2F0`. Each passes one
owner in A0 and ignores the callback return; the dispatcher produces its own
status. There are no direct aligned J/JAL references and exactly one aligned
literal pointer. This table is distinct from `D_8008AB58`.

## Qualification evidence

- Both tools copies: eight fresh focused methods plus project tool checks.
  After production: two fresh installed methods per copy and six unchanged
  semantic methods reused only through exact module/input/artifact fingerprints.
- Guest: 960 cases / 1,920 executions, three independent GNU layouts, all 58
  words visited, 48 alias cases, 58 fired fault-prefix pairs including five
  branch-delay cuts. Original, raw C, padded and actual-Make images agree.
- Original dispatcher: all 109 words retained, 256 cases, all three callback
  sites exercised with independent callback returns and the one-owner ABI.
- Connected services: 24 cases / 48 executions connect this complete callback
  to 119 original words covering the Type46 provider, factory, initializer,
  memcpy and sqrt. Heap allocation and the final event remain bounded services.
- Native SDK32 O0/O2/O3: 16,384 positive cases per profile with trapping UBSan,
  every owner ID byte, float bit copies, owner mutation during providers,
  initialized payload fields, storage fences and 12 effective semantic controls.
- All 77 compact/padded owner neighbors and constant pools remain identical.
  Three actual Make commands reproduce the qualified padded object. Four
  inherited pointer/integer warnings remain textually identical after normalizing
  only diagnostic filename/line positions. The selected C has no diagnostics.
- Strict complete ELF prediction, zero exclusions: 193 changed bytes, comprising
  184 target-code bytes, one target-extent byte and eight metadata bytes from
  the explicitly closed `D_800A5DE8` / `D_800A58B8` symbol/string permutation.
  All 6,055 other linked bodies, all addresses and 189,088 protected Game data
  bytes across 720 owners are unchanged. The inherited guard manifest and
  conversion inventory CSV are byte-identical.

Guest padding bytes are checked against seeded original stack memory. Native
automatic padding has no portable value claim, and overlapping guest aliases
are not a portable C memcpy-overlap claim. These checks establish matching and
bounded semantics, not gameplay, hardware FCSR or final-event acceptance.

## Banked checkpoint

Tools commit: `30d6f3c5ae3a324bbb7fc3ccdb7d896cb669d4cd` (committed before the consumer change).
Production ELF SHA-256:
`8de49d6bdff7a6e38fb3a06e66840cdb2b84ee8c0fa5a6ab1a7f77e922a20977`.
Actual adopted-ELF recount: **3,971 / 5,506 (72.12%)** overall;
Game **3,298 / 4,833 (68.24%)**; Init492/492; Debugger181/181.
Zero address drift; 1,535 C bodies remain different. The 75% threshold is
4,130 exact functions; **159 more** are required. Next screen: `func_15161F4C`.

Reproducible artifacts and receipts live under ignored
`conker/build/game-type46-owner-payload-1514D564-match/`.
The root README changes only its two aggregate status rows. Detailed recovery
history belongs here. Scoped graph refresh preserves prior nodes and all valid
relationships, retiring the superseded placeholder return-type edge. No push.
