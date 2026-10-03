# Game Context-3 Highest-Height Query Recovery

Date: 2026-10-03. Baseline: `4e4734f`.

Follow-up: [Note 765](765-game-entity-height-query-semantic-recovery-20261003.md)
recovers the then-placeholder `func_15045F8C` semantically. It remains
non-matching, and the upstream buffer producer remains an open dependency.

## Recovery

`func_1504554C` replaces its zero-return placeholder with the complete
context-3 highest-height query. The original slot is 114 words / 456 bytes,
VMA `0x1504554C..0x15045714`, ROM `0x729FC..0x72BC4`.

The C body uses the existing `-O2 -g3` profile and fifteen strict expected-word
guards. The unguarded body already fits all 114 words, with fifteen differing
aligned positions. Its SHA-256 before normalization is
`c7878d4b09e4c245272e426ed3f5f08297337e94ee16fa9db92645f76b9c737d`.
Ninety-nine words are unchanged by normalization.

## Contract

The arguments are a three-float position, float lower threshold, and the
existing 36-byte height result. When position Y is below threshold, clear
only flag bit 2 and return zero; no initialization or helper call occurs.

Otherwise initialize result height from `D_80098D4C`, reset context with
`func_1510F800(3)`, reload and truncate X/Z, and call the restored handwritten
`func_150A4FA0` collector. The sentinel is original bits `0xC61C4000`
at ROM `0x23D80C`: exactly -10000.0f. It is not the negative of the
positive sentinel used by `func_15045384`.

Scan the returned 16-byte records. Convert signed fixed height to float and
multiply by 1/256. Select the highest height at or below the reloaded Y and
strictly above the current result height. First equal-height candidates win.
Nonpositive counts and no eligible candidate clear only bit 2 after sentinel
initialization.

Cache the selected triangle's three-pointer array and signed byte offset.
Copy three XYZ signed-halfword triplets from each vertex pointer plus that
offset. The shared candidate's `vertexIndex` field carries a byte displacement
in context 3, not a 16-byte vertex index.

Publish zero metadata, flags OR 6, state 4, and zero value. Return one only if
threshold is at or below result height. A selected result below threshold
still publishes all fields and flags OR 6, then returns zero.
No context-0 query globals are published. NaN comparisons retain the original
ordered predicates; no new null checks or return contracts are invented.

## Guard Proof

Fresh word comparison establishes the same fifteen offsets, expected words,
and replacements as the previous context-3 lowest-height query:

| Set | Offsets | Closed change |
| --- | --- | --- |
| Selected-index spill | `0x060, 0x084` | Defining store/reload both move from private 0x24 to 0x20 |
| Count/index registers | `0x08C, 0x094, 0x0CC, 0x0E0, 0x0E4, 0x0EC, 0x0F0` | Complete a0/v1 swap during the candidate scan |
| Vertex-copy schedule | `0x13C, 0x140, 0x144, 0x148, 0x14C, 0x154` | Equivalent six-byte pointer update with identical signed-halfword access order |

The 0x28-byte frame, saved s0 at 0x18, ra at 0x1C, and local spill lifetime
are the same. Slot 0x20 is above the outgoing argument area and never escapes.
Count/index registers are dead before reuse by the copy loop.

Compiler copy stores use -2/0/2 after an early pointer increment; retail uses
4/6/8 and increments in the branch delay slot. Both preserve load X/store X,
load Y/store Y, load Z/store Z, and the next-iteration pointer, including
overlapping source/destination placements. The detailed proof and alias-trace
tests are in [Note 763](763-game-lowest-height-query-recovery-20261003.md).

The new guard test requires every normalization field to equal that proven
set. There are no relocation replacements, inserts, omissions, or mismatch
allowances. Float operations, comparison direction, branches, and calls are
emitted by this function's own semantic C body, not changed by the guards.

## Tests

Thirteen new tests extract the actual production definition and use the
existing freestanding 32-bit shared-layout harness:

- Original layouts, mode 3, truncated X/Z, and state-4 result publication.
- All flag bytes for early rejection, selected-below-threshold failure, and
  nonpositive counts; preserved output fields and absence of early calls.
- Highest eligible selection, first ties, inclusive boundaries, strict
  negative sentinel, and signed fractional fixed heights.
- Positive non-record and negative byte offsets into vertex storage.
- Callback mutations and reloaded position/result height.
- NaN predicates, padding preservation, and unchanged context-0 globals.
- Exact equality with the previously proven fifteen-word normalization set.

## Linked Validation

The full code build and progress regeneration pass. All 196 tool tests,
project checks, and diff checks pass. Independent linked comparison confirms
all 456 bytes equal retail; SHA-256:
`8c5730f5db0cda5086895f2f9d6c46b4cae98cf602377f6db8a0a5c441e4cfbb`.

The preceding lowest-height query, constructor, allocator, list pass, overlap,
callback wrapper, and following `func_15045714` remain exact. The following
function stays at `0x15045714`. The earlier context-0 highest-height query
retains its 76 differences and prior hash, unchanged.
All 5,712 collector/context bytes and both complete Init sections remain exact,
with the hashes from Notes 760 and 761.

The fresh matcher reports Total 3,257 / 5,455 exact C rows (59.71%), Game
2,584 / 4,782 (54.04%), Init 492 / 492, and Debugger 181 / 181.
There is zero drift and 2,198 differing Game rows. Representation totals do
not change because the old placeholder already counted as C. README changes
only the two affected aggregate matching rows.

No gameplay or host-port execution is part of this recovery. The sibling
host port and frozen Release artifacts remain untouched.

## Next

The next function `func_15045714` already matches. The retained 32-word
`func_15045780` wrapper passes addresses of stack slots 0x1C and 0x18 to that
helper, then passes the two-word buffer at 0x18 to `func_15045F8C`, which is
still a zero-return placeholder. Recover that 580-byte downstream query and
its input-buffer contract next, before converting the wrapper or claiming a
working wrapper path. Audit the existing helper's pointer-versus-integer
fourth-argument declaration at the same time; do not infer a numeric context
from the current C parameter name alone. Init's leaves remain deferred.
