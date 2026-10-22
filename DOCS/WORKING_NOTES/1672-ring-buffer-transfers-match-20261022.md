# Circular Buffer Transfer Pair Direct C Match

Date: 2026-10-22

## Result

Recover both circular byte-transfer helpers in `conker/src/game_70200.c`
from their twelve-byte zero-return placeholders. Each complete semantic body
emits **42 words / 168 bytes, frame 48 and one memcpy relocation** directly
under the normal O2/g3 profile. No new guards or compiler profiles.

| Function | Direction | VA Span | ROM Span |
| --- | --- | --- | --- |
| func_15043A20 | Linear source into ring | 15043A20..15043AC8 | 70ED0..70F78 |
| func_15043AC8 | Ring into linear output | 15043AC8..15043B70 | 70F78..71020 |

Spans end exclusive. Preserve both original assembly files in
`conker/asm/nonmatchings/game_70200/`. Keep the address-based names,
replace their local declarations with full typed prototypes and add concise
purpose comments. Leave the neighboring callers and skip helper unchanged.
Conversion rows and converted-C denominators do not change.

## Recovered Contract

Arguments are a byte ring pointer, signed 32-bit capacity and cursor, linear
byte pointer and signed 32-bit remaining count. The fifth argument arrives
at incoming SP+0x10 and is captured before any memcpy call. Preserve its
saved-register lifetime even if a callee overwrites the incoming home.

While count is nonzero, choose the smaller transfer according to retail's
signed comparison of capacity against the wrapping 32-bit cursor+count.
Copy either ring+cursor to linear or linear to ring+cursor. Advance both
cursors, subtract the copied count and reset the ring cursor to zero when
it reaches or exceeds capacity. Return the final cursor as a full word.

Explicit unsigned intermediates preserve wrapping integer arithmetic instead
of relying on signed C overflow. Count zero performs no copy or pointer
dereference and returns the original full cursor, including unusual bit
patterns. An initial cursor equal to capacity performs a zero-length first
copy, wraps and then transfers normally. Positive-capacity, backed,
nonoverlapping input/output buffers form the native test domain.

Do not add validation absent from retail. Capacity zero with positive count
repeats zero-length copies without terminating. Negative and overflow-shaped
arguments are qualified only through bounded emitted-instruction prefixes:
no native execution of huge lengths, invalid pointers, overlap portability,
general C fault/MMU semantics or gameplay acceptance is claimed.

## Exact Emission

Both original GNU-assembled routines, fresh isolated C, full raw owner and
normal Make output have identical complete bodies and bindings. The sole
R_MIPS_26 memcpy relocation is at +0x58 in each function.

Raw unlinked body SHA-256:

- Write: `d8a2e99c4a17efcca79bff7e3c901913d98d6d1d29a764bac8124c1906c4f1ad`.
- Read: `7ebddca1423f06e939096e2907025ac1a6afde41cb6e9c7645d674e82354c7c5`.

Preserve all fourteen raw/padded owner neighbors, addresses, pools and the
entire existing guard manifest. Actual Make's three productive commands
(IDO, ordinary C padder, assembler) reproduce the qualified code and
metadata. This is an ordinary C owner, not a generated GLOBAL_ASM-owner
five-command recipe. The existing generated_12D630 duplicate-recipe warning
remains; owner diagnostics are unchanged and isolated diagnostics are empty.

## Qualification

Identical task tools in both local copies:
`experiments/game_ring_buffer_transfers.py` and
`tests/test_game_ring_buffer_transfers.py`.

| Actual Run | Active Tools | Older Mirror | Errors / Failures / Skips |
| --- | --- | --- | --- |
| Full pre-install suite | 8 tests, 7.799s | 8 tests, 7.737s | 0 / 0 / 0 |
| Fresh installed checks | 2 tests, 1.911s | 2 tests, 1.878s | 0 / 0 / 0 |

Explicitly reuse six unchanged pre-install checks per copy only under strict
source, raw/padded object, guard, helper/input and complete-image identity;
they are not fresh installed runs. Shared tools checks pass in both copies
(0.160/0.100s). Routine Codex work uses zero Claude calls.

- 3,712 guest phases visit all 84 words, including byte alignment, capacity 1,
  exact boundaries, repeated wraps, full-buffer fences, fifth-home mutation
  and zero-count unbacked pointers/full-word returns.
- Native32 O0/O2/O3 each pass 1,744 selected-body cases with trap UBSan.
  Sixteen effective defined wrong-C controls cover direction, missing linear
  advance, shifted ring/linear addresses, short/long copies, return value and
  capacity 1 suppression. Native buffers remain backed and nonoverlapping.
- Twelve independent GNU links cover 48 rebase phases. Check 360 fired root
  fault prefixes against original emitted code, sixteen signed-word prefixes,
  capacity-zero behavior bounded to three calls and four effective compiled
  guest-prefix controls. These are instruction-order checks, not portable
  C exception/concurrency guarantees.
- Verify the current Init memcpy against retail, all eleven words, and
  connect its actual code across 288 phases. Hooked and actual-helper scopes
  remain distinct. Preserve 29 historical inputs and reject six complete
  image corruptions with zero metadata exclusions.

## Caller Bounds

The aligned retail scan finds writer JALs at ROM 71114/71130 and reader JALs
at ROM 711A4/711CC/71214, with no literal target pointers. This does not
exclude constructed targets.

Execute the original writer window 15043C48..15043C90 over 48 phases:
load and subtract the four-byte header length, transfer its big-endian word,
chain the returned cursor into the payload transfer and publish OBJECT+0xC.
Execute reader windows 15043CF0..15043D08, 15043D14..15043D34 and
15043D58..15043D78 over 72/96/96 phases: header decode, bounded payload plus
NUL terminator, and full-payload cursor publication at OBJECT+8 with the
original length return.

The first writer fixture started at 15043C4C, skipping the live T7 load.
Including that actual preceding load fixes the fixture without changing C
or weakening memory checks. A second assertion incorrectly assumed the
empty typed writer emitted only JR/NOP: its actual twenty-byte placeholder
contains three argument-home stores before returning. Both corrections
preserve the actual caller-entry state and production baseline.

Full func_15043BB8 and func_15043CA4 remain unchanged twenty-/twelve-byte
placeholders. Unexecuted eligibility and remaining-byte skip paths,
full-parent behavior and natural gameplay remain unqualified.

## Production

Commit tools first: `b84dedaa6aa27e4e1b4f044115dcf815a6ef2af0`. No push.
Preserve all 1,556 prior older-mirror dirty paths, statuses, hashes and HEAD;
add only the two task files, leaving 1,558 dirty paths. Do not reset/commit it.

Seal 15,858 files, including all 1,454 linker objects. Normal Make completes
in 0.503s in the verified Linux copy. Mark the verified unchanged guard
manifest old to avoid unrelated historical-object rebuilds.

The strict independent complete-ELF prediction permits exactly
**278 changed bytes = 276 code bytes + 2 function-size metadata bytes**.
Preserve all other 6,053 bodies, all 6,055 addresses and all 720 protected
Game-data owners / 189,088 bytes. Protected-data SHA-256:
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.
ELF SHA-256:
`87fb5683fc0225a86d7af529467cd36ff02639f0f0cbf59305228dc32638180d`.

Live adoption audit completes in 42.781s. Verify every live static input and
non-target object before and after promoting only the owner object, ELF,
linker script and progress CSV; linker-script and conversion-CSV bytes remain
identical. The complete live ELF equals the independently predicted image.
Padded owner SHA-256:
`0277d2a5c0f506c450a22e08edc3f8f6e2bb27b090563ad8f826ecdbdd1dc73a`.

## Handoff

The standard matcher against the actual live ELF completes in 34.752s:
total **3,741/5,505 (67.96%)**, Game **3,068/4,832 (63.49%)**,
Init 492/492 and Debugger 181/181 exact. Zero address drift; 1,764 different.
The 75% threshold remains 4,129 exact, requiring **388 more matches**.
Queue shapes: 1,633 placeholders, 122 semantic/other and nine unlocated.
Next func_151B8C54 is screened only, unmodified and uncredited.
Keep func_1508CAD8's 862-word stub queued.

Root README changes only its two aggregate rows. Detailed updates belong here
and in concise indexes. Post-commit graph-worker and every-old-node audits
remain private receipts; retain excluded-corpus/large-HTML caveats without
claiming full re-extraction or a fresh corpus-membership recount.
Frozen host Release remains untouched.
