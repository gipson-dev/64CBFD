# Paired Reference Event Match

Date: 2026-10-24. Consumer predecessor `17d9c3d5`; tools predecessor
`a6facec1`. Qualification tools committed first as
`88fe8e9f464eab15dcd11db5d0dc64bf88ea476c`. No push requested/performed.
Routine work, zero Claude calls; no provider or dependency changes.

## Recovered Handler

`func_15169850`, `conker/src/game_1944C0.c`, replaces an empty typed
six-word / 24-byte C placeholder. Retain the existing public interface:
`void(s32 pairAddress, u8 command, s32 valueAddress, s32 tagAddress, s32 owner)`.
The address words remain words so all existing declarations and callers keep
their ABI; use descriptive local pointer views inside the body. Remove only
this routine's stale placeholder comment, replacing it with its actual purpose.

Body VA `0x15169850..0x151698F4`, ROM `0x196D00..0x196DA4`, exclusive ends.
The full retail slot ends at VA `0x15169900`, ROM `0x196DB0`: 41 body words
plus three separate zero alignment words. Frame 24, one `R_MIPS_26`
binding at +0x3C to `func_1516972C`. The adopted symbol size becomes 164,
not 176; preserve the complete 176-byte slot without miscounting alignment
as compiler instructions.

Raw 164-byte C SHA-256:
`77ca382addeb0db9b90ba5f5e9da8dc0f2a1fb38693dede1d50750bffac4db1d`.
Original 164-byte body SHA-256:
`da2a12cadbf322c388454a2b82b0bd0a156890c0eb4e5402cd943d1fb328cbb9`.
Full retail slot SHA-256:
`4a3960cad441555e10139f5ccabf55f57c7e0c287410d2235be983c1628913b8`.

Command zero releases the fifth-argument owner if the first pair word equals
the current reference, or the payload byte at +4 equals the current tag.
Preserve the short circuit. Command 0x2D exchanges a matched first reference
for the second and reads tag +9, or exchanges a matched second reference
for the cached first and reads tag +8. The reference word is written before
the tag byte is read. Other byte commands do nothing and ignore all pointees.
Do not reorder or preload tag bytes under overlapping layouts.

## Closed Allocation Cycle

The complete semantic C emits 41 words with five real differences. Ordinary
local-capture, operand-order, unsigned-word, pointer-view and switch screens
do not close them; the switch also changes extent/control flow. Keep the
straight two-command C body and normalize only the measured closed v0/v1
allocation cycle in the command-0x2D region.

| Offset | Expected C Word | Retail Word |
| --- | --- | --- |
| +0x58 | `0x8C820000` | `0x8C830000` |
| +0x5C | `0x8CC30000` | `0x8CC20000` |
| +0x60 | `0x54430007` | `0x54620007` |
| +0x80 | `0x55630005` | `0x55620005` |
| +0x88 | `0xACC20000` | `0xACC30000` |

Derive these five changes by swapping only the two value roles across words
22..34. Verify the full raw hash, one unchanged binding and exact changed
offset set. No inserted/folded instructions, forced physical C registers,
barriers, assembly substitute or compiler-profile changes. This is guarded
semantic C, not compiler-only matching. All new relocation lists are empty.
Preserve the entire historical guard CSV prefix byte-for-byte and append
exactly these five rows with its existing line endings/schema.

## Callers And Release Boundary

The aligned full retail scan finds 27 direct JAL sites and no literal
function-pointer references. All caller declarations remain unchanged.
Execute complete original `func_15149514` and `func_150ECB4C` with both
root images: 60 phases cover byte/high-word incoming commands and reference
paths. Their existing source/object inputs are frozen and unchanged.
Natively execute the actual C passthrough `func_15149514` in 65,536 cases.
This is not a claim to execute the remaining 25 complete parent functions.

Retained `func_1516972C` already matches all 28 words. Run its original/live
guest body connected to the root in 64 phases and compile its actual C body
natively. Its bookkeeping call precedes the late owner-kind reload; kind
0/1 stops, other kinds select a callback from the actual 52-byte-stride table
or the fallback. Provider mutation to kind 7 verifies the reload. Types 2
and 255, NULL/non-NULL callbacks and both stack phases are covered.
Bookkeeping, destructor callback and fallback remain bounded providers;
no full disposal subsystem, heap, gameplay or hardware acceptance is claimed.

## Focused Qualification

Both copies pass eight fresh checks before and after installation, zero
errors/failures/skips, zero reused checks. Primary/mirror pre-install:
23.566s / 23.494s; installed: 23.984s / 24.977s. Both shared project
tools checks exit zero. Use the existing MIPS, native32, frame/fault,
relocation, source-span, object and legacy-padder helpers.

- 6,144 main guest phases cover all byte commands, reference matches, tags,
  provider mutations and both stack phases. Additional upper-word commands
  verify byte narrowing; unsupported commands accept unmapped arguments.
- 2,592 guest alias phases cover reference/tag/source overlaps and incoming
  homes. Independent expected calls/public memory agree for both fitted
  code and raw C; complete original/fitted state and events agree. Do not
  claim raw C's private register state is already matching.
- All 40 reachable body words are visited. Retail's duplicate load at +0x7C
  is unreachable: the earlier likely branch targets +0x80 and executes its
  load in the delay slot, while the first-match path branches over +0x7C.
  Preserve that literal word instead of inventing a visit or deleting it.
- Native32 O0/O2/O3 with trap UBSan: 786,432 selected cases per optimization
  and ten effective defined wrong-C controls. Use allocated word/byte backing
  and a complete typed owner; the reference copy is allocated too, not a
  declared byte array punned as word storage. Exercise defined byte aliases
  and actual release C, keeping guest-private aliases out of native claims.
- Nine independent GNU links and 144 rebases compare original, fitted padded
  and actual Make objects. 864 fired root-access prefixes preserve complete
  state, PC and delay origin; this is not portable C fault-order acceptance.
- Nine full-image corruption controls reject changes to code, alignment,
  retained helper/data, symbol size and image extent. Ten additional checks
  feed corrupt expected words/binding lists to the actual legacy padder;
  all five guard sites fail closed for both corruption kinds.

The first coverage assertion incorrectly demanded a visit to the unreachable
duplicate. Replace that assertion with the explicit branch/word proof and
40-word reachability gate, then rerun both fresh suites. Do not modify the
production routine or original assembly to satisfy a mistaken fixture.

## Production And Preservation

Seal 15,942 initial native files, adding the two owned tools files in both
copies for 15,946 files / 58 focused inputs. Cover all 1,454 link objects.
Actual normal shadow Make uses three commands with IDO `-O2 -g3` and the
ordinary legacy `pad_c_object.py`; it is not an asm-processor recipe.
The complete padded object equals independent qualification. Preserve all
41 other raw/padded owner functions, their pools and inherited diagnostics.
Seven existing neighboring compiler warnings and the duplicate generated_12D630
Make recipe warning remain; isolated selected C has no diagnostics.

Production Make exits zero in 0.571s and reproduces the independently
predicted whole ELF and qualified object. Exactly 108 ELF bytes change:
107 target-code bytes and one symbol-size byte, 24 to 164. Zero metadata
reordering/exclusions. Preserve all other 6,054 bodies, all 6,055 addresses
and protected Game data: 720 owners / 189,088 bytes, SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

After both installed suites, verify all 15,946 native entries before/after
adoption. Four audited overrides only: target source, guard CSV, object and
ELF. Recapture the actual live adopted ELF and independently recount that
stream, not an inferred +1. Use checked native streams, not DrvFS project reads.

Installed ELF SHA-256:
`2538bae4ed9f6bb240faf0a26235db7983717b0a57fb16b566d8c0cc1d34e1c5`.
Installed target object SHA-256:
`7e254b6a13ec7b5034e6e7389cbdb2b8d511f0c4f921b9de246a826d65ac4b7c`.
Guard CSV SHA-256:
`43cb13987e7ff85caae6bd18ca277b1d616ea0fe5a75708c8842bb84c5a53e65`.

Preserve all 1,600 pre-existing older-mirror dirty paths, statuses, hashes
and HEAD; add only the two owned tools files there, leaving 1,602 dirty
paths. Do not reset/commit that independent mirror. Host Release, saves,
configuration, private inputs, providers and dependencies are untouched.

## Measured Progress And Resume

| Section | Byte-Exact C Functions | Address Drift | Still Different |
| --- | --- | --- | --- |
| Total | 3,771 / 5,505 (68.50%) | 0 | 1,734 |
| Game | 3,098 / 4,832 (64.11%) | 0 | 1,734 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

Remove only `func_15169850` from the live-ELF-pinned queue. It was classified
as semantic/other because its empty placeholder already had typed parameters;
do not decrement the simple no-argument zero-return placeholder count.
Remaining source screens: 1,605 placeholders, 120 semantic/other, nine
parser-unlocated. `func_1510D8C0` already has `Gfx *` C missed by the parser;
its private screen and `func_1518C850` remain unmatched/uncredited.
Continue the 44-word queue, including `func_1509E640`; keep the 862-word
`func_1508CAD8` owner stub separate. Target 4,129 exact C functions:
358 more, goal incomplete.

Root README gets only the two aggregate row updates. Retain post-commit
Graphify worker receipts and audit all eight changed-file hashes/mtimes/
membership plus retention of all 43,933 prior nodes. Do not claim old-edge
retention, full-corpus re-extraction or forge a built-at-commit stamp.

Ignored evidence: `conker/build/game-pair-reference-event/qualified/`.
Tools: `tools/experiments/game_pair_reference_event.py` and
`tools/tests/test_game_pair_reference_event.py`.
