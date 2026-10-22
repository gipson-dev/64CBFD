# Randomized Player Byte-State Direct C Match

Date: 2026-10-22

## Result

Recover `func_1507EEF4` in `conker/src/game/generated_AC030.c` from its
twelve-byte zero-return placeholder. Complete semantic C emits all
**43 words / 172 bytes, frame 32 and four bindings** directly under
normal O2/g3. No guards, inserted words or profile changes.

VA 1507EEF4..1507EFA0 / ROM AC3A4..AC450, ends exclusive.
Keep the address-based name and add a purpose comment. The actual interface
is void with no arguments; its only caller ignores V0. No shared headers,
caller declarations, conversion rows or helper bodies need editing.
Preserve the original `conker/asm/AC030.s` and all fifteen owner neighbors.

## Recovered Contract

Capture the current player from D_800D154C, its pointer at +0x31C, and the
state block at that pointer +0x58 once. The state and counter are unsigned
bytes at block +0x0C/+0x0D, or attachment +0x64/+0x65.

1. State zero initializes state 1 and counter zero without drawing RNG.
2. State 1 always calls func_150ADA20, even though it ignores the result.
   Read the counter after the call. At counter >=3, store state 2/count 0.
3. Every other nonzero state draws RNG and computes 8 + (result & 3).
   Read the counter after the call. At or above that threshold, store
   state 1/count 0.
4. If no transition fires, preserve any callee mutation of the captured
   state/counter. Never reselect the branch using a post-call state byte.

Keep the captured attachment through RNG-side changes to the current player
or the player's attachment pointer. Use a separate threshold assignment to
guarantee the RNG call precedes the counter read in C; a compact relational
expression does not specify its operand evaluation order.

Declare the real state pointer before the real threshold local. This natural
order retains the retail pointer spill at SP+0x1C. The reverse declaration
order still emits 43 words but produces four spill-offset differences.
No dummy local, padding declaration or expected-word normalization is used.

## Exact Emission

Raw unlinked SHA-256:
`351b66882b7a1ed47c1eb561335466e3e0f794cbdd16004c86e324041c50d3cb`.

Independent GNU original assembly, isolated C and the complete raw owner
agree on all words and bindings: D_800D154C HI16/LO16 at +0x08/+0x0C,
and func_150ADA20 R_MIPS_26 calls at +0x40/+0x6C.
The ordinary three-command Make recipe reproduces both compact and padded
objects. All fifteen raw/padded neighbors, pools and addresses remain fixed.

The complete independent ELF prediction permits exactly **126 changed bytes:
125 code bytes and one target-size metadata byte**, with zero exclusions.
ELF SHA-256:
`4be66e910d868e90ce2d6ad6955010411a527aa55229d279e0097ff9b8a30d4f`.
Padded owner SHA-256:
`733f918fa9a203aab8c285a3b77f5ba70f1d168336c429d66b417e6c14c608a3`.

## Qualification

Identical task tools in both local copies:
`experiments/game_randomized_byte_state.py` and
`tests/test_game_randomized_byte_state.py`.
Reuse existing owner/padder, MIPS fault-prefix, native32, GNU relocation and
64-bit RNG oracles. Routine work uses zero Claude calls.

- 18,432 guest phases cover every state byte, counter boundaries, all four
  random residues, stack phases, callee clobbers, state/count mutations,
  player/attachment redirection and captured-pointer lifetime. Every one of
  the 43 target words executes.
- Native32 O0/O2/O3 each exercise 139,264 selected-body cases with trap
  UBSan, typed player offset/size assertions and full row/fence comparisons.
  Twelve defined wrong-C controls detect wrong states/clears, strict
  thresholds, wider mask, signed remainder, omitted RNG draws, prematurely
  cached counter, post-call branch recheck and recaptured attachment.
- Nine independent GNU links cover 36 rebase phases. Check 82 actually fired
  root-access fault prefixes and seven strict-image corruptions. Guest
  fault-prefix agreement is not a portable C/MMU exception claim.
- The aligned retail scan finds one direct JAL at ROM AC638 and no literal
  target pointers. Execute the original four-word caller window
  1507F188..1507F198 across sixteen phases, stopping before the next load.
  Its 0x98-byte parent frame and post-call current-player reload are checked.
  Parent func_1507EFD0 remains the same twelve-byte placeholder; complete
  parent execution is not claimed.
- Original and current func_150ADA20 agree on all eighteen words. Connect
  that actual 64-bit shift/XOR RNG across 864 regular phases and 192 guest
  seed-alias phases. All eighteen RNG words execute. The eight-byte seed is
  at 800885B0. This is not a 32-bit LCG or a recovered RNG C body; guest
  byte/seed aliases do not establish portable native C alias behavior.

| Actual Run | Active Tools | Older Mirror | Errors / Failures / Skips |
| --- | --- | --- | --- |
| Full pre-install suite | 8 tests, 93.931s | 8 tests, 84.839s | 0 / 0 / 0 |
| Fresh installed checks | 2 tests, 9.325s | 2 tests, 5.151s | 0 / 0 / 0 |

Shared project-tool checks pass in 0.325s / 0.684s. Reuse six unchanged
pre-install behavioral checks per copy only under strict source, raw/padded
object, helper/input, guard and complete-image identity. Do not describe
those six as fresh installed runs.

## Production

Commit tools first: `cd36a32a55cbc2cc77d0147afe4abb365b800309`. No push.
Preserve all 1,562 older-mirror dirty paths, statuses, hashes and HEAD;
add only the two task files, leaving 1,564 dirty paths. Do not reset or
commit that independently dirty mirror.

Seal 15,870 files and all 1,454 linker objects. Advance the predecessor's
two already-committed source fingerprints, its qualified owner object and
ELF; preserve the prior fixture-only test fingerprints. Verify all current
bytes before sealing rather than trusting historical row metadata.

Normal Make completes in 4.875s in the verified Linux copy. Mark only the
verified unchanged guard manifest old to avoid unrelated historical-object
rebuilds. Preserve inherited generated_12D630 duplicate-recipe warnings;
owner diagnostics are unchanged and isolated diagnostics are empty.

Preserve all other 6,054 linked bodies, all 6,055 addresses and all 720
protected Game-data owners / 189,088 bytes. Protected-data SHA-256:
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

Live adoption audit passes in 22.985s. Verify every static input and
non-target object before and after promoting only the target owner object,
ELF, linker script and progress CSV. The edited C already equals its
qualified proposal. Linker-script and conversion-CSV bytes remain identical.
Reproduce the complete independent 126-byte prediction with zero exclusions.

## Handoff

The standard matcher against the actual live ELF completes in 8.106s:
total **3,744/5,505 (68.01%)**, Game **3,071/4,832 (63.56%)**,
Init 492/492 and Debugger 181/181 exact. Zero address drift; 1,761 different.
The 75% threshold remains 4,129 exact, requiring **385 more matches**.
Queue shapes: 1,630 placeholders, 122 semantic/other and nine unlocated.
Next func_1515F1B0 is screened only, unmodified and uncredited.
Keep func_1508CAD8's 862-word stub queued.

Root README changes only its two aggregate rows. Detailed updates belong here
and in concise indexes. Post-commit graph-worker and every-old-node audits
remain private receipts. Preserve excluded-corpus/large-HTML caveats without
claiming full re-extraction or a fresh corpus-membership recount.
Host Release, saves and configuration remain untouched.
