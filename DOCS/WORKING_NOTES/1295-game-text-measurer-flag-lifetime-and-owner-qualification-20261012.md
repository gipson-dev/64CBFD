# Game Text Measurer Flag Lifetime And Owner Qualification

Date: 2026-10-12. Continue func_150428D4 in
conker/src/game/generated_6E770.c, original VA 0x150428D4..0x15042C40,
ROM 0x6FD84..0x700F0: 219 words / 876 bytes, frame 0x80. This checkpoint
advances original lifetime/layout fitting and reusable full-owner gates after
[Note 1294](1294-game-text-measurer-native32-qualification-20261012.md).
It is not a byte match or installation. Production remains the zero-return
placeholder at 199 differences. No matching/conversion credit; keep this
target and the wider Game goal open.

## Baseline And Source Experiments

Consumer 4d47991b975b24a864861051c7f65cd940724102 and mounted tools
b5e4600af6ca76a77574eb09124ae0cacb648750 were clean at entry. Codex sole
writer, zero Claude calls. Read bounded live ASM/source/test evidence and
query the existing graph. No OGL/Release change/build, ROM/save/config or
editor/debugger mutation, package/account/bridge installation or push.

Bounded signed/typed parameter reuse, paired allocator controls, indexed
loops, expression grouping, metrics records and flag captures are experiments,
not blanket qualification of every form. Indexed input with index zero set
before the empty check reproduces retail's separate first/second text loads,
zero-index setup and strength-reduced cursor. Source-local font-address
rematerialization removes the hoisted address without changing the production
compiler profile. Use the primary project's
[IDO 5.3 guide](https://github.com/n64decomp/oot/blob/master/docs/guides/-O2%20decompilation%20%28for%20IDO%205.3%29.md)
to guide those source-local experiments; measure actual code rather than
treating its allocator hypotheses as proof. Do not cache the font pointer's
value: read it again after width writes.

| Candidate | Body Words | Frame | Differences | Qualification |
| --- | --- | --- | --- | --- |
| initial-index-late, previous closer baseline | 217 | 0x80 | 185 | Prior public/native qualification |
| indexed-early | 218 | 0x80 | 213 | Opening read shape, not selected |
| remat-metrics-state-after | 218 | 0x80 | 168 | Public/native and exact saves/homes; private equivalence rejected |
| capture-declaration-after-record | 218 | 0x80 | 174 | Public/native and six bounded private flag-home cases |
| capture-reuse-typed-parameter | 218 | 0x80 | 175 | Screen only, not selected |
| ternary-flag-indexed-remat | 228 | 0x90 | 224 | Screen only, not selected |

The 168-difference shape has the original S0..S6/RA save sequence, thirteen
opening words and the subsequent empty/index setup byte-exact. The five
metrics outputs occupy their original SP+0x64/0x60/0x5C/0x58/0x54 homes.
However, its use-font member is always stored in the local record and read
late. It does not reproduce retail's T0 flag, call-only SP+0x68 spill and
early reload. A smaller word score is not a full private-equivalence result.

## Private Discriminant And Better Lifetime

Run the complete original and candidate with actual normalizer65/metrics115
instructions, no helper hooks. Point width at incoming SP+phase-0x18, which
is the measurer's frame SP+0x68. These are synthetic guest stack aliases,
not portable native C pointers. Two phases give four discriminants:

| Text | Original Width/Height/Third | Always-Stored Flag Shape |
| --- | --- | --- |
| A | 19, 18, 0 | 20, 18, 0 |
| 0xA8 | 32, 15, 3 | 41, 25, 3 |

Reject that shape as a match. An ordinary flag store overwrites the aliased
width, and a late flag read after extended width writes incorrectly enables
ordinary font measurement. This is an executed numeric difference, not only
a fingerprint or instruction-score failure.

The call-only capture variant copies the flag into its SP+0x68 record home
only around func_150415E0 and reloads it before width writes. Both phases now
agree for A, 0xA8 and A/0xA8: six cases, including accumulated width reset by
the actual private spill. The latter returns 32,18,3 in both forms. A fresh
compiled negative moves the reload after the width store; its private 0xA8
result is 41,25,3 rather than original 32,15,3. The gate is effective.

Prefer that temporal invariant over the lower 168 score. The capture candidate
is still 218 words/frame 0x80/174 differences and saves S0..S7/RA, not original
S0..S6/RA. It coalesces the initial text with the flag in S3 and uses S4 for
glyph; retail reuses S3 for text/glyph and keeps the flag in caller-saved T0.
Its store/load scheduling and complete private trace are not matching. These
are not 174 independent scheduling words; no broad retail-copy guard batch.

## Qualification And Owner Gates

Thirteen final focused tests pass in 49.893 seconds, no skips. Both new named
forms pass 755 complete public guest cases against original/reference with
the actual helpers, including all bytes, two phases, output/font/factor/
scale/text aliases, NULL/empty, zero-payload skipping and both discriminants
from the earlier live-pointer/nested-truncation gates. Complete helper-call
arguments, including all five private output homes, match retail. Each new
body also passes native733 O2/O0: 1,466 executions per body. Keep the earlier
clear/closer bodies and existing effective controls qualified; unselected
screen forms are not thereby qualified.

Both full copied owners run the actual no-unroll profile and asm-processor
pre/post pipeline. No GLOBAL_ASM block is present in this current owner, so
this is not a new GLOBAL_ASM-body execution claim. All seven other functions'
bodies, extents and relative relocations match the frozen before owner; all
normalized pools remain exact. Each target body equals its isolated compile.

Both real routes, pad_c_object.py and pad_generated_object.py, preserve the
existing metrics pool binding and unchanged old guard manifest. Assemble
their outputs and compare entire text and relocations: only the 876-byte
target slot changes. Both routes agree, all neighbor metadata stays exact,
and no generated rodata survives. No target guards are added.

An initial owner assertion confused symbol size with slot extent. Inspect
the emitted .size followed by .space 0x4: the candidate body is 872 bytes,
followed by one candidate zero to reach the 876-byte slot; the next normalizer
starts exactly there. That zero is not an original retail tail. Check all
three facts separately; do not count padding as matching the missing word.

Receipts under conker/build/game-text-measurer-recovery-test/:
lifetime-fit.json, lifetime-owner.json, lifetime-private-witness.json,
captured-lifetime.json and captured-lifetime-owner.json. Full private RAM/
GPR/FPR equivalence, deliberate whole-measurer faults, independent rebases,
FCSR/invalid conversions, hardware/renderer/gameplay and installation remain
unproven. Native qualification stays finite/in-range and host-endian; the
synthetic private aliases stay guest-only.

The documented zdbug modes 6 and 5 were attempted sequentially in the new,
ignored conker/build/game-text-measurer-flag-trace-20261012 directory. Both
terminate with child signal 11 in this prepared uopt and leave a zero-byte
uoptlist. No valid trace or allocator-cost inference is claimed. Ordinary
compiles continue to pass; do not alter/install the compiler or debugger.
The first shell invocation rejected unquoted comma-bearing flags before
launch; quote those arguments for PowerShell. No live trace process remains.

## Preserve And Bank

All nine frozen production inputs stay byte-exact: source, entire ELF,
guards, progress CSV, Makefile, original slice ASM, table data, metrics pool
and retail layout. Protected data remains 189,088 bytes/720 owners with zero
differences, SHA-256
0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670.
Source 802b4d27659c80620c2ca509df4c3da84d136c5c92b758d7a6390c4428d2273d,
ELF 978d39eab009d4134e5c03d4bdd2d433010812544a5be599c823fdff1ce2aa14,
guards 3f12cf872b84100963934734de2e67f5f07073ce3112ccbd2e5c4cb8af84666e.

Preserved aggregates: Game 2,813/4,823 (58.32%), total 3,486/5,496
(63.43%), Init 492/492, Debugger 181/181; zero drift / 2,010 different.
No fresh matching credit or README churn. These are the unchanged previous
measurements, not a claim that compatible C is now installed.

After updating the indexes, the two frozen-production/corruption gates pass
again in 1.594 seconds. All 4,452 relative links in the six updated documents
and unchanged root README resolve; git diff --check passes.

Bank mounted tools ce4cc1a796a7fc9a38fa3903c34ebb7b798f4157 first, then
consumer docs/exact gitlink, no push. Consumer/mounted/older ROM-free checks
and native Windows py_compile pass. Preserve older standalone HEAD
ddbdd16b53ce60b054fb6e11bf0649a41f48375a and all 78 other saved hashes;
verify the two known files before identical updated copies. No new mirror
file, dirty count357 unchanged, final80 hashes; no older history commit/reset.
Before final reporting require clean active repositories and a fresh terminal
post-consumer-commit Graphify Rebuilt receipt, advanced log bytes/UTC and
zero native workers. Keep excluded-but-existing graph nodes, no force/purge.

The standalone native Graphify update exits one on protective shrink refusal:
18,299 candidate nodes versus 40,068 saved. Preserve 19,398 excluded-but-
existing nodes from 2,972 files; no force, purge or package/skill update.

## Continue This Same Target

1. Start with capture-declaration-after-record's temporal flag invariant,
   not the privately rejected 168-difference shape. Recover original S3
   text/glyph reuse and caller-saved T0 flag; remove the extra saved-register
   lifetime through actual source fitting, not dummy state or a profile swap.
2. Fit all original 219 words/frame 0x80 and re-run both public/native and
   private discriminants. Current 218/174 is neither word-exact nor fully
   private-equivalent. Do not install a compatible or padded substitute.
3. Requalify the selected final body in the full owner/padders, independent
   links/rebases, deliberately fired fault prefixes and complete literal
   ELF/guard-history audit. Measure fresh matching progress only after the
   finished installation, update README aggregates and bank tools first.
4. Then recover func_150417AC, the remaining 1,098-word formatter. Existing
   guard removal, the full Game goal and independent hardware/FCSR/RSP/RDP/
   renderer/gameplay acceptance remain open.
