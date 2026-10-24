# One-Shot Owner Link Payload Direct C Match

Date: 2026-10-23. Consumer predecessor `2b14eac9`; tools predecessor
`65a27ef4`. Qualification tools committed before the consumer pin as
`7027bcb7a16f82f5e378097befaf6a92be1955b3`. No push requested/performed.

## Recovered Routine

`func_150FAA40`, owner `conker/src/game/generated_126F60.c`:

- VA `0x150FAA40..0x150FAAEC`, ROM `0x127EF0..0x127F9C`.
- All 43 words emit directly from semantic C, frame 72, eight relocations,
  no guards or compiler-profile changes. Symbol size advances from 12 to 172.
- Raw C SHA-256:
  `704f06a665a60c9e2a1207cf9471ef0f3a6f048f2639bf1cedb290f5fb8feb3f`.
- Retail/resolved SHA-256:
  `63384f6a234b6a078e933a313e0b68fbad92d98b0cdbfc2a1c4df370a9ecfd0e`.
- Recover `void func_150FAA40(u8 code, s32 value)`. Preserve the address name
  and existing owner-local `D_800D3098` byte-pointer view; add only a local
  `OneShotLinkPayload`, helper declarations and purpose comment.

If latch byte `D_80088B60` is nonzero, do nothing. Otherwise capture the
current owner's +0x71C/+0x6E8 addresses and positive float zero in a complete
twelve-byte payload. Submit factory arguments
`(300,-1,0x57,-1,0,0x46,12,code,value)`. On successful allocation, set the
latch to one; independently test the retained pointer again before copying
all twelve bytes to allocation +0x28. Failure does not set the latch or copy.
Factory side effects remain observable; do not reread the current owner for
the captured links after the factory returns.

Declare the payload before the allocation pointer and retain both nonnull
tests. Swapping declarations leaves four word differences; combining tests
produces a 41-word body. A word-sized first formal retains one difference.
These are compiler-shape observations, not evidence that the alternate
declarations prove the recovered public interface.

## Original Callers And Helpers

The aligned retail reference census finds exactly two direct JALs and no
literal function pointers. Both original five-word caller windows pass
`(255,1)` and ignore the callee's register result:

| Parent | Window VA | Call VA | Call ROM | Existing Frame |
| --- | --- | --- | --- | --- |
| `func_1502460C` | `0x150253FC` | `0x15025400` | `0x528B0` | `0x158` |
| `func_1509D180` | `0x1509D1D8` | `0x1509D1DC` | `0xCA68C` | `0xC8` |

Execute both complete windows across 32 phases, including allocation failure,
busy latch, helper mutations and both stack phases. Preserve the actual
branch targets and delay slots: the first window returns one to its next
block; the second reloads its saved +0xC4 word. Both parent C bodies remain
placeholders. Their complete objects/source are unchanged; no full dispatcher
or parent-C recovery is claimed.

Execute the byte-exact 49-word `func_15149130` and 11-word `memcpy`, each
verified in the current linked ELF against retail. The factory converts the
twelve-byte payload request into allocator arguments `(35,value,52,1,code,1)`,
initializes the real header and clears sixteen bytes through bounded bzero.
This target visits 47 factory words; the other two belong to the unused
flag-bit-2 branch. All eleven memcpy words are visited. Keep the lower
allocator and bzero providers explicitly bounded, not full implementations.
The owner-local integer-size factory declaration expresses this machine
argument; the legacy shared declaration is not changed by this task.

## Qualification And Boundaries

Both tools copies pass six fresh checks before installation and all six
again after installation, with zero failures/errors/skips and no reused
checks. Final pre-install times: primary 41.094 seconds, mirror 40.802 seconds.
Installed times: primary 42.133 seconds, mirror 41.743 seconds. Both shared
`check_project_tools.py` runs exit zero.

- 10,688 guest phases cover all 256 selector bytes with high incoming bits,
  all 256 latch bytes, word boundaries, failure/success and helper mutations.
  Check captured pointers, all twelve payload bytes, flag ordering, output
  regions and literal GPR/FPR/RAM/event state. Six overlap layouts include
  the latch, global pointer, private packet, argument homes and owner storage.
- Native32 O0/O2/O3 with trap UBSan: 196,608 calls per optimization, including
  repeated latch/failure attempts, full allocation fences and eleven effective
  defined wrong-C controls. Native storage remains disjoint and typed.
- Nine independent GNU links compare original, qualified padded and actual
  Make objects at three entries with independently rebased globals/helpers.
  Forty-eight cases exercise those relocated payload captures and calls.
- All 258 selected root-access fault prefixes fire and retain literal state,
  current PC and branch-delay origin. Nine corruptions of the full image,
  including code, symbol value/size, neighbors and truncation, are rejected.
- In 96 deliberately malformed guest allocation cases, factory initialization
  overwrites the caller's saved RA before the copy. Preserve and compare the
  resulting return escape, only at the exact original JR/delay boundary and
  only for the independently predicted aliases. Do not call them successful
  normal returns or portable C overlap behavior. Hardware/FCSR parity is not
  claimed.

Initial setup exposed an inherited oracle-field namespace collision and the
malformed return boundary above. Retain the failing receipts; neither counts
as a passing run. A tools whitespace check later caught one trailing blank
line. Remove it, verify the complete location-bearing Python AST is identical,
reseal both copies and rerun all pre-install checks on the final file bytes.
Immutable historical snapshots remain pinned; regenerated raw compiler outputs
are not mistaken for those snapshots when exporting private receipts.

## Production Evidence

Whole-owner and isolated raw payloads/bindings equal independent GNU assembly;
all seventeen raw/padded neighbors and owner pools remain fixed. Actual
three-command Make uses normal O2/g3 and emits the complete qualified object
byte-for-byte. Existing duplicate-recipe warnings are unchanged, and owner
compiler diagnostics are empty. Production Make exits zero in 0.593 seconds.

The independent full link predicts only the complete target slot and its
existing symbol-size change. Production reproduces that prediction exactly:

- 140 changed ELF bytes = 139 code bytes + one size byte, zero exclusions.
- All other 6,054 bodies and all 6,055 addresses are fixed; no new guard rows.
- Protected Game data: 720 owners / 189,088 bytes exact, SHA-256
  `0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.
- Result ELF SHA-256:
  `29b741bb3e2c82843345aeb36281bc99b9a887a924ee86a1cb7ce9f150b46b92`.
- Target object SHA-256:
  `02e99d1f9a1d3c22716443f41004f9825558f23662efae841b9c20969c9d3a06`.

Seal 15,910 files, 33 focused inputs and all 1,454 linker objects. Verify the
existing disposable Linux cache against a fresh native capture. Stream scripts,
installed source and result artifacts over native stdin/checked tar, without
Linux reading the Windows project through DrvFS. Native adoption checks every
sealed file before and after promoting only the target object, ELF and the
unchanged linker-script/progress outputs. Only source/object/ELF are mutable.
Preserve all 1,582 older-mirror dirty paths, statuses/hashes and HEAD, adding
only two task files there. Host Release, saves/configuration and unrelated
processes remain untouched.

## Live Recount And Handoff

Capture actual adopted Windows ELF bytes and require equality with both
production and independent-link images before the standard matcher runs.
The fresh matcher exits zero in 1.356 seconds:

| Section | Exact C functions | Address drift | Still different |
| --- | --- | --- | --- |
| Total | 3,757 / 5,505 (68.25%) | 0 | 1,748 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 3,084 / 4,832 (63.82%) | 0 | 1,748 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

The converted-C denominator is unchanged. Reaching 75% still requires 4,129
exact functions, 372 more. Remove only `func_150FAA40` from the ELF-pinned
queue: 1,617 placeholders, 122 semantic/other definitions and nine unlocated
entries remain. Next `func_1512D238` is queued only and uncredited; preserve
the separate 862-word `func_1508CAD8` owner stub queue.

Bank only the nine scoped consumer paths; root README receives only two
aggregate-row updates. Refresh Graphify through the normal hook, then audit
all 43,846 preceding nodes for retention or unique relocation and all eight
changed C/Markdown hashes/mtimes/memberships. Report any missing stamp honestly;
do not forge it or equate excluded-old retention with full re-extraction.
