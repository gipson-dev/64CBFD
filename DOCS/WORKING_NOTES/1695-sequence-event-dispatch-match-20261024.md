# Sequence Event Dispatch Match

Date: 2026-10-24. Consumer predecessor `4b71fbc9`; tools predecessor
`88fe8e9f`. Qualification tools committed first as
`f5559d5a767f997f29b66666d922cf2e64689494`. No push requested/performed.
Routine work, zero Claude calls; no provider or dependency changes.

## Recovered Routine

`func_1509E640`, `conker/src/game/generated_CBAF0.c`, replaces a three-word
zero-return placeholder with the complete three-command audio/sequence
request handler. VA `0x1509E640..0x1509E6F0`, ROM `0xCBAF0..0xCBBA0`,
exclusive ends: 176 bytes / 44 body words, frame 24, eight bindings.
There is no separate alignment tail in this function.

Recover `s32(s32 sequence, s32 command, s32 *packet)` with actual typed
declarations for the three downstream services. Commands are full words,
not bytes. Preserve the original `D_800D3840` symbol and its signed width
without assigning an unproven wider meaning to that global.

- Command zero starts the supplied sequence/resource with level 32767 when
  the signed selector is below 3, otherwise packet word +8, and mode/pan 64.
- Command one forwards packet word +8 to the level setter. Forward word +12
  only when the selector equals 4; otherwise forward zero.
- Command two submits the stop request without reading packet contents.
- Every recognized command returns exactly one regardless of lower-service
  return, allocation failure or an empty resource. Other commands return
  zero without reading the packet or global selector.

Raw C SHA-256:
`4d6ba0007690260651de4ff3f2da7ef73a1702922a48493445e770b4ee1342dd`.
Resolved/retail SHA-256:
`593065996ce157a660ff459f1931856f28fa03706f334a6ed28ffd4c9b9225ed`.

## Derived Layout Guards

The complete semantic C emits 44 words with 27 real differences. Ordinary
ternary/local, branch, switch, capture, initialized-local and return-expression
screens do not emit the literal retail schedule. A private O1 diagnostic is
58 words; no-debug and no-unroll variants also fail. Do not adopt a different
profile, add a volatile declaration or disguise these results as direct C.
Keep the normal O2/g3 source and derive the layout transformation explicitly.

Word indices below are zero-based:

1. Rotate raw words 6..21 left by one, placing the early second global HI16
   setup at word 21. The permutation is closed, not a discarded address load.
2. Map output words 24..33 from input indices
   `[25,33,27,28,29,30,31,26,32,24]`. This places each arm's argument load
   and the zero argument in retail's respective branch/call delay slots.
3. Repair six crossing-branch displacements at output words 2/5/7/9/19/29.
   Convert the selected BNE to BNEL at word 24 with its derived target.
4. The raw NOP now at output word 31 becomes the literal retail duplicate
   packet load. It is unreachable, not an additional active read: the likely
   branch targets word 32, while the other arm branches from 29 to 40 with
   word 30 as its delay slot. All 43 reachable words are exercised.

Append exactly 27 expected-word/expected-relocation guards. Preserve every
instruction slot and all eight bindings; no insertion/omission rows or size
padding. One raw NOP is explicitly reconstructed as an unreachable retail
load. This is guarded semantic C, not compiler-only matching or just a
register-allocation cycle. Validate the complete raw hash, permutation,
branch shapes, source loads and exact changed-word count before fitting.

| Binding | Raw Offset | Retail Offset |
| --- | --- | --- |
| Selector HI16, first path | +0x0C | +0x0C |
| Selector LO16, first path | +0x30 | +0x2C |
| Start JAL | +0x48 | +0x44 |
| Selector HI16, second path | +0x18 | +0x54 |
| Selector LO16, second path | +0x58 | +0x58 |
| Level JAL, selector-four path | +0x70 | +0x6C |
| Level JAL, zero-fade path | +0x80 | +0x80 |
| Stop JAL | +0x90 | +0x90 |

## Caller And Helper Boundaries

The aligned retail scan finds no direct JAL sites and one literal function
reference at ROM 0x22CFA8, table slot 5 in `D_800884D4`. Verify all fifteen
table words remain identical in the live ELF and original ROM.

Execute the actual 26-word handwritten VM window
`0x150AE12C..0x150AE194` with header selector zero (disabled) or six
(registered index five): 240 phases. It reads the full command at packet+4,
passes the packet as argument three, and clears only header bits 12..15 in
argument one, preserving upper bits. Check its explicit S7 saved-return and
16-byte call-area contract using a return boundary marker. Do not call this
recovery of the full VM C parent or execution of unrelated table entries.

Retained helpers are byte-exact before installation and remain unchanged:
`func_1001263C` 43 words, `func_151F2D6C` 36 and `func_151F2BA8` 16.
Execute all 95 words in 5,184 connected guest phases and compile all three
actual C bodies natively. Verify both existing `_retail` aliases used by
the Init body resolve to the same addresses as their canonical functions.

The start helper clears its size output before the variadic resource request
`(&size, 2, 22, sequence)`, always stores the low sequence halfword, then
submits level/pan/envelope/attachment only when resource and size are nonzero.
Exercise the full-word 0xD2 envelope distinction, failed/empty resource paths,
signed level clamp, fade values and the stop state store. Interrupt masking,
resource lookup, pan, envelope and attachment remain bounded providers.
This is not full audio/resource backend, audible, gameplay or hardware acceptance.

## Focused Qualification

Both copies pass eight fresh checks before and after installation, zero
errors/failures/skips, zero reused checks. Primary/mirror pre-install:
14.573s / 14.096s; installed: 15.898s / 15.610s. Both shared tools checks
exit zero. Reuse existing MIPS, native32, frame/fault, relocation, object,
source-span and generated-padder helpers.

- 6,208 guest phases cover signed selector boundaries, all low command words
  through 511, additional high words, provider results and mutations, normal,
  global-overlapping and private-home packet layouts. Raw C public results,
  calls and memory agree with the independent reference; fitted code agrees
  with complete original state/events. No raw private-state match is claimed.
- All 43 reachable root words are visited. The unvisited +0x7C duplicate is
  retained and accounted for, not silently filtered out of the body length.
  Ignored NULL/truncated packet tests preserve conditional read boundaries.
- Native32 O0/O2/O3 with trap UBSan covers 331,776 selected cases per
  optimization and eleven effective defined wrong-C controls. Use complete
  typed arrays for packet/global aliases; no out-of-object arithmetic or
  declared byte-array word punning. Keep guest-private homes out of native
  portability claims. Actual helper C runs through typed lower providers.
- Fifty-four actual padder corruptions reject expected-word and relocation
  changes at every new guard site. The filtered negative fixtures retain all
  guard rows for this owner; separate full-prefix checks protect history.
- Nine GNU links and 288 rebases compare independently assembled original,
  qualified padded and actual Make objects, including global HI/LO carry and
  helper-address boundaries. 288 fired root-access prefixes preserve full
  state, PC and delay origin. Nine strict-image corruptions are rejected.

The first fixtures omitted unsupported-command coverage from their visit
union and one aliased native mutation from the expected model; both were
corrected before fresh passing checks. A private `inspect.py` diagnostic
also shadowed the standard library when launching the prepared runner.
Rename only that owned scratch file to `inspect_shape.py` in both caches;
do not relax production code, import checks or the immutable input seal.

## Production And Preservation

Seal 15,946 initial native files, adding the two owned tools files in both
copies for 15,950 files / 33 focused inputs and all 1,454 linker objects.
Actual shadow Make uses three ordinary commands, IDO O2/g3 and the normal
generated-slice padder. Its complete padded object equals qualification.
Preserve all three raw/padded neighbors and pools, including the unchanged
92-word `func_1509E730` placeholder. Do not credit that larger dispatcher.

Isolated and owner compiler diagnostics are empty. The inherited duplicate
generated_12D630 Make recipe warning remains; no warning-free build claim.
Production Make exits zero in 0.588s and reproduces the independently
predicted whole ELF and qualified object. Exactly 123 ELF bytes change:
122 target-code bytes and one symbol-size byte, 12 to 176. Zero metadata
reordering/exclusions. Preserve all other 6,054 bodies, all 6,055 addresses
and protected Game data: 720 owners / 189,088 bytes, SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

Audit all 15,950 native entries before/after adoption, with only target source,
guard CSV, object and ELF overrides. Recapture the actual live adopted ELF
and independently recount that stream, not an inferred +1. Use checked native
streams rather than DrvFS project reads.

Installed ELF SHA-256:
`2c89c9966d6847006e478c855b30aed572b30ba016bb90b021dbd5418cc66730`.
Installed target object SHA-256:
`6de7193fba7795045145bafe0320c0a27a6676a20aa72f6cd72ffdc8f67828bd`.
Guard CSV SHA-256:
`3a5b68d16b833e8b1e1c054f492606354062658a3bfa01cd520b97f9f29a5d1c`.
The previous 43cb1398 guard prefix remains byte-identical before 27 appended rows.

Preserve all 1,602 pre-existing older-mirror dirty paths/statuses/hashes/HEAD;
add only the two owned tools files, leaving 1,604 dirty paths. Do not reset
or commit that independent mirror. Host Release, saves, configuration,
private inputs, providers and dependencies are untouched.

## Measured Progress And Resume

| Section | Byte-Exact C Functions | Address Drift | Still Different |
| --- | --- | --- | --- |
| Total | 3,772 / 5,505 (68.52%) | 0 | 1,733 |
| Game | 3,099 / 4,832 (64.13%) | 0 | 1,733 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

Remove only `func_1509E640` from the live-ELF-pinned queue. Remaining source
screens: 1,604 simple placeholders, 120 semantic/other, nine unlocated.
`func_1510D8C0` already has `Gfx *` C missed by the parser; its private
screen and `func_1518C850` remain uncredited. Continue the 44-word queue,
including `func_150D21CC`, keeping the 92-word dispatcher above and the
862-word `func_1508CAD8` owner stub separate. Target 4,129 exact C functions:
357 more, goal incomplete.

Root README changes only its two aggregate matching rows. Retain normal
post-commit Graphify worker receipts and audit all eight changed-file hashes,
mtimes/membership and all 43,943 prior nodes. Do not claim old-edge retention,
full-corpus re-extraction or forge a commit stamp.

Ignored evidence: `conker/build/game-sequence-event-dispatch/qualified/`.
Tools: `tools/experiments/game_sequence_event_dispatch.py` and
`tools/tests/test_game_sequence_event_dispatch.py`.
