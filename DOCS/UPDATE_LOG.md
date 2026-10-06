# Update Log

## 2026-10-06 Game Effect Configuration Packet Direct Match

[Note 1043](WORKING_NOTES/1043-game-effect-configuration-packet-direct-match-20261006.md)
replaces `func_1519EA78`'s stub with all 69 words directly, frame 0x70.
Separate captured float local, complete 60-byte packet and typed scalar
handoff; 32 controls, 1296 two-body guest cases, 65536 width sweeps,
100 two-body float-pattern cases and 131072 native cases. Only target
changes across 6059; protected sections/720 owners/10646 guards intact.
Owner diagnostics empty. README total 3321/5462 and Game 2648/4789 exact,
zero drift. All 26 focused post-link tests pass in 219.250 seconds, no skips.
Callee `func_15152190` remains a C
placeholder; wrapper qualification is not a full effect-path restoration.
Next `func_1519EB8C`; no sibling/Release change or push.

## 2026-10-06 Game Address Record Allocator Direct Match

[Note 1042](WORKING_NOTES/1042-game-address-record-allocator-direct-match-20261006.md)
replaces `func_1519E970`'s stub with all 37 words directly, frame 0x20.
Owner-before-flags source shape, typed pointer return and seven arguments;
48 controls, 1152 cases per three two-body guest modes, 65536 extra width
sweeps and 131072 native cases. All 85 chain words execute. Retained helpers
unchanged; only target changes across 6059 slots; protected sections/720
owners/10646 guards intact. Owner diagnostics empty. README now total
3320/5462 and Game 2647/4789 exact, zero drift. All 77 focused post-link tests
pass in 468.864 seconds, no skips.
Next `func_1519EA78` configuration packet. No sibling/Release edit or push.

## 2026-10-06 Game Conditional Packet Allocator Direct Match

[Note 1041](WORKING_NOTES/1041-game-conditional-packet-allocator-direct-match-20261006.md)
replaces `func_1519E6BC`'s stub with all 38 words directly, frame 0x38.
Post-cleanup gate, failure publication and captured packet; three padding
bytes remain untouched. 24 controls; 3072 cases in each of three two-body
guest modes, 1536 extra code-byte sweeps and 18432 native cases. Retained
helpers unchanged; 138 reachable chain words execute. Only target changes
across 6059; protected sections/720 owners/10646 guards intact. Owner
diagnostics empty. README now total 3319/5462 and Game 2646/4789 exact,
zero drift. All 71 focused post-link tests pass in 369.862 seconds, no skips.
Next `func_1519E970`'s record allocator.
No sibling/Release edit, complete gameplay/host adoption or push.

## 2026-10-06 Game Random Selector Outputs Direct Match

[Note 1040](WORKING_NOTES/1040-game-random-selector-outputs-direct-match-20261006.md)
replaces `func_1518E5D8`'s stub with all 37 words directly, frame 0x18.
Seven output pointers, ordered RNG/flag/status/selector/tail stores;
24 controls, 4096 opaque / 16384 connected-selector / 8576 fully connected
guest and 14528 native cases. All 86 wrapper/selector/RNG words execute.
Retained helpers/palette unchanged; only target changes across 6059 slots;
protected sections/720 owners/10646 guards intact. Four owner warnings equal
baseline. README now total 3318/5462, Game 2645/4789 exact, zero drift.
All 65 focused post-link tests pass in 310.324 seconds, no skips.
Next inspect `func_1519E6BC`'s conditional
allocation/packet contract. No sibling/Release edit, host adoption or push.

## 2026-10-06 Game Actor Position Queue Wrapper Direct Match

[Note 1039](WORKING_NOTES/1039-game-actor-position-queue-wrapper-direct-match-20261006.md)
replaces `func_1517D5FC`'s stub with all 37 words directly, frame 0x28.
Signed coordinates, actual actor stride and captured float bits, shifted
selector; 32 controls, 24576 opaque / 37936 connected guest and 8192 opaque /
49152 connected native cases. All 59 post-link tests pass in 255.215 seconds,
no skips. Existing helper/guards unchanged. Only target
changes across 6059; protected sections/720 owners/10646 guards intact.
README now total 3317/5462, Game 2644/4789 exact, zero drift. Next recover
`func_1518E5D8`'s RNG/selector/output contract. No sibling/Release edit or push.

## 2026-10-06 Game Alternate Actor Dimensions Direct Match

[Note 1038](WORKING_NOTES/1038-game-alternate-actor-dimensions-direct-match-20261006.md)
replaces `func_1515C244`'s stub: 41 direct C words plus two retail padding
words, complete 43-word slot exact. Local signed +0xE8 view; no shared header,
guards/profile/data change. 16 controls, 43008 guest / 21504 native cases.
All 52 post-link tests pass in 228.619 seconds, no skips.
Only target changes across 6059; protected sections/720 owners/10646 guards
intact. Baseline/current owner diagnostics empty. README now total 3316/5462
and Game 2643/4789 exact, zero drift. Next qualify `func_1517D5FC`'s queue
handoff; no complete gameplay/caller-domain claim, sibling/Release edit or push.

## 2026-10-06 Game Actor Dimensions And Position Direct Match

[Note 1037](WORKING_NOTES/1037-game-actor-dimensions-position-direct-match-20261006.md)
replaces `func_1515C1A0`'s stub with all 41 retail words directly under O2/g3.
No guards/profile/data/header change; existing actor/point layouts. Signed
dimensions, ordered alias-sensitive XYZ and vertical adjustment; 16 controls,
36864 guest / 18432 native cases. All 47 post-link tests pass in 193.845
seconds, no skips. Only target changes across 6059; protected sections/720
owners/10646 guards intact. Both owner compiles have
empty diagnostics. README: total 3315/5462, Game 2642/4789 exact, zero drift.
Next independently qualify `func_1515C244`; no sibling/Release edit or push.

## 2026-10-06 Game Projection Wrapper ABI And Frame Audit

[Note 1036](WORKING_NOTES/1036-game-projection-wrapper-abi-and-frame-audit-20261006.md)
banks 20 compiler controls and the observed six-argument/four-output ABI.
No exact form or production edit. Three tests pass in 14.634 seconds;
58 retained helper words equal retail. All linked slots/data/guards and
matching aggregates unchanged. Output-alias/connected/native qualification
remains required. Next inspect `func_1515C1A0`; no sibling/Release edit or push.

## 2026-10-06 Game Descriptor Shape Measure Direct Match

[Note 1035](WORKING_NOTES/1035-game-descriptor-shape-measure-direct-match-20261006.md)
replaces `func_1514462C`'s zero-return stub with the complete 56-word measure,
directly under O2/g3, no frame/guards/profile/data change. Correct descriptor
pointer prototype and two float externs; signed halfwords and wrapped box
product, ordered float work and masked shape dispatch. 48 controls, 21504
three-body guest cases and 10752 native cases. Only target changes across
6059; all 58 tests pass in 94.861 seconds, no skips. Protected sections/720
owners/10646 guards intact. Owner warnings equal
baseline source/headers. README now total 3314/5462 and Game 2641/4789 exact,
zero drift, 2148 different. Next: 101-word `func_15144CEC` placeholder.
Pair-clamp frame remains open; no full callers/gameplay/FCSR, sibling/frozen
Release change or push. Game matching remains active.

## 2026-10-06 Game Pair Clamp Saved Register Backend Audit

[Note 1034](WORKING_NOTES/1034-game-pair-clamp-saved-register-backend-audit-20261006.md)
banks nine accepted uopt controls, 108 corner guest runs and the explicit
non-matching boundary. None recovers the frame; all production slots/data/
guards stay unchanged. Next qualify `func_1514462C`'s isolated 56-word direct
shape-measure recovery. All nine pair tests pass in 35.646 seconds, no skips.
No production/profile or aggregate-count change,
full gameplay acceptance, sibling/frozen Release edit or push.

## 2026-10-06 Game Pair Clamp Register Lifetime Audit

[Note 1033](WORKING_NOTES/1033-game-integer-pair-clamp-register-lifetime-audit-20261006.md)
banks the post-`fe925393` compiler follow-up: 64 parameter/local register-hint
forms under O2/g3 and O1/g3, 128 controls. O2/g3 bodies are unchanged; O1/g3
uses frame 0x20 and overflows the slot. No exact form. 1536 corner guest runs
retain retail ordered traces and full footprints. All 51 tests pass in
93.572 seconds, no skips; all 6059 slots/protected sections/720 owners/10646
guards equal the checkpoint. No production, guard,
profile, data or README-count change. Continue saved-pointer/frame and tail
matching; `func_15143D18` remains 36 differences. No sibling/frozen Release
change, gameplay acceptance or push. Game goal remains active.

## 2026-10-06 Game Integer Pair Clamp XOR Access Recovery

[Note 1032](WORKING_NOTES/1032-game-integer-pair-clamp-xor-access-recovery-20261006.md)
replaces `func_15143D18`'s temporary-swap approximation with the retail
ordered XOR reads/writes and sequential endpoint clamps. Still non-matching:
29 raw words, frame zero, seven padding words, 36 aligned differences.
92 controls find no exact form. 24576 guest cases cover all 36 retail words;
7168 old-body access traces differ despite equal final outputs. 12288 native
cases pass; all 50 combined tests pass in 64.519 seconds, no skips.
Only target changes across 6059; protected sections/720 owners
and all 10646 guards unchanged. Three owner warnings equal baseline.
README totals unchanged: 3313/5462 total, Game 2640/4789 exact, zero drift,
2149 different. Continue saved-pointer frame/lifetime and return-tail matching.
No new guards/profile/header/data, full gameplay claim, sibling/frozen Release
change or push. Game matching remains active.

## 2026-10-06 Game Indexed State Save Direct Match

[Note 1031](WORKING_NOTES/1031-game-indexed-state-save-direct-match-20261006.md)
replaces `func_15123934`'s stub and incorrect commented indexing draft with
the complete 38-word save/install/mark/callback pass, directly under O2/g3.
No new guards/profile/data. 32 controls; 7680 opaque / 4736 connected cases,
six zero-mask prefixes, 2520 native cases; all 43 tests pass in 48.052 seconds,
no skips. Only target changes across 6059; protected sections/owners/10646
guards unchanged. Five owner warnings equal baseline. README: total 3313/5462
and Game 2640/4789 exact, zero drift, 2149 different. Next: `func_15143D18`
XOR-swap/clamp matching, not placeholder recovery. No sibling/frozen Release
change, full gameplay/valid-domain expansion claim or push; Game remains active.

## 2026-10-06 Game Random Reload Timer Direct Match

[Note 1030](WORKING_NOTES/1030-game-random-reload-timer-direct-match-20261006.md)
replaces `func_150D26F0`'s stub with its gated timer/dispatch/unsigned reload.
All 39 words emit directly, frame 0x20; no new guards/profile/data. 76 controls,
896 gate / 1920 reload / 48 trap three-way and 1408 native cases; full word
coverage and preserved post-callback field reads. All 35 tests pass in 20.151
seconds, no skips. Only timer changes across 6059; protected sections/720
owners and 10646 guards unchanged. README: total 3312/5462, Game 2639/4789
exact, zero drift, 2150 different. Next: 38-word `func_15123934` placeholder.
No full dispatcher/RNG/gameplay, hardware trap delivery, sibling/frozen
Release change or push claim. Game matching remains active.

## 2026-10-06 Game Float Reference Packet Wrapper Direct Match

[Note 1029](WORKING_NOTES/1029-game-float-reference-packet-wrapper-direct-match-20261006.md)
replaces `func_150C2804`'s stub with its six-argument 28-byte packet dispatch.
All 37 words emit directly under existing O2/g3; no new guards/profile/data.
24 compiler controls, 2304 opaque / 256 float-pattern / 288 connected-retail
three-way cases and 14400 native cases. All wrapper and original callee words
execute; unchanged production `func_15134908` already matches all 50 words,
correcting the stale prior handoff. Next: 39-word `func_150D26F0` placeholder.
All 92 tests pass in 233.716 seconds; eight packet tests rerun with the callee
equality assertion pass in 6.375 seconds, no skips.
Only wrapper changes across 6059 slots; protected sections/owners and all
10646 guards intact. README totals: 3311/5462 and Game 2638/4789 exact,
zero drift, 2151 different. No sibling/frozen Release change or push;
full production helper-chain/gameplay/FCSR acceptance remains separate.

## 2026-10-06 Game Linked Record Position Tail Match

[Note 1028](WORKING_NOTES/1028-game-linked-record-position-tail-match-20261006.md)
matches all 72 words of `func_150E6FAC` through three closed-layout guards and
one saved-RA insertion. Semantic source remains unchanged at 71 raw words;
not a direct C match. 16 source/backend controls; 3360 three-way guest cases,
71 reachable words and one structurally unreachable load. Only this slot
changes across 6059; protected data and all old guards intact.
All 84 combined tests pass in 267.948 seconds, no skips. README aggregate
rows updated: total 3310/5462 and Game 2637/4789 exact, zero drift, 2152 different.
Next ordinary candidate `func_150C2804`; edge helper stays non-matching at 102.
No sibling/frozen Release change or push; Game goal remains active.

## 2026-10-06 Game Graph Edge Crossing Scope Audit

[Note 1027](WORKING_NOTES/1027-game-graph-edge-crossing-scope-audit-20261006.md)
banks 101 source-only scope/plane/aggregate/operand controls, empty diagnostics,
no improvement beyond 102 differences. All 6059 linked slots match the prior
receipt. No production/data/guard/profile or README aggregate change; Game
2636/4789 exact, zero drift. Next inspect `func_150E6FAC`'s return tail.
The edge helper remains non-matching. No sibling/frozen Release change or push.

## 2026-10-06 Game Graph Edge Crossing Lifetime Improvement

[Note 1026](WORKING_NOTES/1026-game-graph-edge-crossing-lifetime-improvement-20261006.md)
improves `func_15086D94` from 151 to 102 real differences: 207 emitted words,
no padding, frame 0x80 versus retail 0x90. The saved prefix and complete outer
loop emit directly; the count is loaded once. 209 compiler controls with empty
diagnostics; 2177 four-way guest cases and 288 native footprints. All 62 tests
pass, no skips. Only helper
changes across 6059 slots; root/parent and protected data/guards intact.
README/counts unchanged: Game 2636/4789 exact, zero drift, 2153 different.
Next: frame/minimum home and normal/side/constant lifetimes. Still not a byte
match or full helper-chain/FCSR/gameplay acceptance. No sibling/frozen Release
change, host transplant or push.

## 2026-10-06 Game Graph Edge Crossing Recovery

[Note 1025](WORKING_NOTES/1025-game-graph-edge-crossing-recovery-20261006.md)
recovers `func_15086D94`'s horizontal crossing pass, replacing its zero-return
stub. Not byte-exact: 206 emitted / 207 slot words, frame 0x78, 151 differences.
Preserve the last-fraction result, including later rejected crossings, and
the retail 100.0f initial minimum. 39 forms / 78 compiler controls; 2177
three-way guest cases, 198 retail words visited, 288 native full footprints.
All 58 combined tests pass, no skips.
Only this slot changes in the 6059-slot audit; root/parent, protected sections,
720 data owners and 10643 guards unchanged. README/counts unchanged:
3309/5462 total and 2636/4789 Game exact, zero drift, 2153 different.
Next: helper frame/private homes and normal lifetimes. No full helper-chain/
FCSR/gameplay acceptance, sibling/frozen Release change or push.

## 2026-10-06 Game Root Neighbor Lookup Direct Match

[Note 1024](WORKING_NOTES/1024-game-root-neighbor-lookup-direct-match-20261006.md)
recovers `func_15085DF8`: all 168 words directly from C, frame 0x80, no guards/
profile/overflow. Seventy controls; 3275 three-way guest cases, 166 executed
words plus two always-annulled delays, 1536 native cases. All 45 lookup/parent/
lifetime/visitor tests pass, no skips. Exactly two slots change in the 6059-slot
audit: lookup and the geometric helper's float ABI. Parent, protected data and
all guards unchanged. README totals: 3309/5462, Game 2636/4789 exact, zero drift,
2153 different. Next: recover the still-placeholder 207-word `func_15086D94`;
parent remains 282 differences. No full helper-chain/gameplay/FCSR acceptance,
sibling/frozen Release change or push.

## 2026-10-06 Game Zone Selection Lifetime Improvement

[Note 1023](WORKING_NOTES/1023-game-zone-neighbor-selection-lifetime-screen-20261006.md)
improves `func_1508B3F8` from 340 to 282 aligned differences: 369 emitted words,
frame 0x140, no padding. Still non-matching; no new guards/profile/overflow or
query enlargement. Ninety-one compiler controls, 2990 four-way guest cases,
full parent/visitor coverage and 1424 native footprints. All 17 qualification/
lifetime and 13 visitor regression tests pass. Only parent changes across
6059 slots; all protected sections/owners/guards intact. README aggregates
and counts unchanged. Next: query/private homes and address lifetimes; the
233-difference control is one word too large and remains uninstalled.
No full lookup/gameplay, sibling/frozen Release change or push.

## 2026-10-06 Game Zone Neighbor Selection Recovery

[Note 1022](WORKING_NOTES/1022-game-zone-neighbor-selection-recovery-20261006.md)
recovers `func_1508B3F8`'s full parent pass, not a byte match: 367 body words /
369-word slot, frame 0x140, 340 differences. 58 controls; 2990 three-way guest
cases, full parent/visitor coverage and 1424 native footprints. Fourteen
qualification and sixty focused regression tests pass, no skips.
All 6059 addresses/lengths survive; only parent and exactly
four argument homes in the still-placeholder lookup change. Protected data
and all guards intact. README/counts remain accurate and unchanged.
Next: parent private homes/constant-address lifetimes, not broad guards.
No full lookup/gameplay, sibling/frozen Release change or push.

## 2026-10-06 Game Record Neighbor Visitor Byte Match

[Note 1021](WORKING_NOTES/1021-game-record-neighbor-visitor-match-20261006.md)
recovers `func_1508B2A8` across all 84 words, frame 0x30 and five saves.
Six guards close two complete temporary-register lifetimes; no profile override,
insertion/omission or assembly edit. Twenty-four controls, 4096 leaf and 4608
recursive three-way cases, full word coverage and 2304 native footprints.
All 13 qualification tests and 49 focused regressions pass, no skips.
Only target changes in 6059 slots; protected sections/720 owners and all older
guards stay intact. Totals: 3308/5462, Game 2635/4789 exact, zero drift,
2154 different. README only aggregate tables/date updated. Next: inspect parent
1508B3F8. No full caller/gameplay, sibling/frozen Release change or push.

## 2026-10-05 Game Record Dispatcher Direct Match

[Note 1020](WORKING_NOTES/1020-game-record-dispatcher-direct-match-20261005.md)
matches all 38 words of `func_15040CC8` directly, removing the old overflow
body. Integer record ABI and divide-by-one update retain retail index/frame/
saves without emitting a divide; no guards/profile/header change. 45 controls,
12288 three-way guest cases, full word coverage. All 16 matching/native tests
and 39 shared-oracle regressions pass, no skips. Sixteen later overflow bodies
shift -156 bytes unchanged; 13 trampoline slots only retarget one jump word.
All other slots/retail addresses, protected sections/720 owners and guards
remain intact. Totals: 3307/5462, Game 2634/4789 exact, zero drift, 2155 different.
README only aggregate tables updated. No sibling/frozen Release change or push.

## 2026-10-05 Game Position Radius Append Direct Match

[Note 1019](WORKING_NOTES/1019-game-position-radius-append-direct-match-20261005.md)
recovers `func_1508B20C`'s complete 39-word leaf directly from C, replacing
the zero-return placeholder. No guards or profile/header/assembly change.
34 compiler controls; nine qualification tests pass, with 8192 three-way
guest cases, 252 bounded actual-caller cases, 65536 native cases and full
instruction coverage. Another 57 focused regression tests pass, no skips.
Only target changes across 6060 slots; protected sections/720 owners and
all 10637 older guards unchanged. Totals: 3306/5462, Game 2633/4789 exact,
zero drift, 2156 different. README only aggregate tables updated.
No sibling/frozen Release change, full caller/gameplay acceptance or push.

## 2026-10-05 Game Actor Context Dispatcher Byte Match

[Note 1018](WORKING_NOTES/1018-game-actor-context-dispatcher-byte-match-20261005.md)
matches all 107 words of `func_15044380`. Direct C recovers frame/homes;
15 guarded words normalize a proven register cycle, independent schedule
and commutative add. 19 controls, 6184 three-way guest cases, 107/107 words;
nine matching tests pass, no skips. Only target changes in 6060 slots;
protected sections/720 owners and all older guards remain intact.
Totals: 3305/5462, Game 2632/4789 exact, zero drift, 2157 different.
README only aggregate tables updated. No sibling/frozen Release change or push.
All 320 affected-slice tests pass in 57.212 seconds, no skips; tools,
whitespace and 2982 relative links pass. Nineteen final controls reproduce.

## 2026-10-05 Game Actor Triangle Cached Iterator Audit

[Note 1017](WORKING_NOTES/1017-game-actor-triangle-cached-iterator-audit-20261005.md)
banks 78 controls / 1914 bounded comparisons, without a production change.
Cached read recovery trades for excess frame; mixed bounds exceed the slot.
No new exact function, profile, guards, host transplant or push. Continue
Game matching with the 107-word actor context dispatcher `func_15044380`.

## 2026-10-05 Game Actor Triangle Reduced Frame And Read Lifetime Screen

[Note 1016](WORKING_NOTES/1016-game-actor-triangle-reduced-frame-and-read-lifetime-screen-20261005.md)
reduces the installed frame 0x160 to 0x140 and differences 273 to 242.
All seven array homes match; 302 body/slot words, no new guards or profile.
The early actor/ID/count read shape remains different; it is not claimed
retail-exact. 77 controls / 4488 bounded comparisons; scope-only frame
reduction is disproven. 64 focused tests and five final frame probes pass.
Only target changes in 6060 slots; protected sections/data/CSV and README
counts stay intact. Next: last eight frame bytes and original read/SDK loop.
No exact-function gain, sibling/frozen Release change or push.
367 regression tests pass in 527.136 seconds, no skips, including the final
read probe. Tools, staged whitespace and 2993 relative links pass.

## 2026-10-05 Game Actor Triangle Private Home Recovery

[Note 1015](WORKING_NOTES/1015-game-actor-triangle-private-home-recovery-20261005.md)
recovers all seven retail private-array homes without changing operation
text or capacities. `func_1502F490` improves 275 to 273 differences; frame
0x160 and 298-word body still do not match retail. No guards/profile change.
Thirty-six controls include 1848 bounded comparisons; oversized loops are
not installed. Only target changes in 6060 slots; protected sections, data
owners, CSV and README counts are preserved. Next: reserved homes and SDK
loop lifetimes. No new exact function, sibling/frozen Release change or push.
60 focused / 362 regression tests pass in 269.380 / 818.122 seconds, no skips;
tools, staged whitespace and all 2983 checked relative links pass.

## 2026-10-05 Game Actor Triangle Lifetime And First-Match Audit

[Note 1014](WORKING_NOTES/1014-game-actor-triangle-lifetime-and-overlapping-range-audit-20261005.md)
banks 34 controls with 1914 bounded guest comparisons. No production change
or new byte-exact function; one-word raw-score improvement remains only a
candidate, with the wrong frame/control-flow shape. Explicit overlap tests
reject first-match overwrites and premature continued scanning; native
reference cases expand to 64512 plus 33 aliases. Counts/README unchanged.
Next: reserved private homes and mixed scalar/array placement for the same
transform. No sibling/frozen Release change or push.
All 57 focused checks pass in 309.237 seconds, no skips; tools, whitespace
and 2981 links pass. All 6060 slots/protected sections remain intact;
the prior full corpus is not rerun in this test/experiment/doc-only audit.

## 2026-10-05 Game Actor Triangle Layout Audit

[Note 1013](WORKING_NOTES/1013-game-actor-triangle-layout-screen-20261005.md)
banks ten array/output-cursor controls after `623b96ae`. All compile without
diagnostics; fitting forms pass 120 bounded guest comparisons. None improves
the frame/difference metrics; oversized 308-word forms are not installed.
Production, linked slots and README counts stay unchanged. Next: actual
spill lifetimes and edge/matrix-loop shapes. The Game goal remains active.

## 2026-10-05 Game Actor Triangle Remap Semantic Recovery

[Note 1012](WORKING_NOTES/1012-game-actor-triangle-remap-semantic-recovery-and-matrix-tail-restoration-20261005.md)
recovers complete `func_1502F490` C and restores its necessary original matrix
leaf assembly/tail-register interface. The C still differs at 275 words:
298 body / 302 slot, frame 0x160 versus retail 0x138. No guards/profile change.
All 53 focused tests pass: 1715 three-way cases, actual phase/matrix/tail
connections, 57344 native references and 33 aliases. Only two slots change
in 6060; protected sections, 720 data owners and CSV remain intact.
Exact C numerators stay 3304 total / 2631 Game; denominators fall to 5462 /
4789 because the false C matrix placeholder becomes retained ASM. Zero drift;
README aggregate update only. Next: this transform's frame/array/loop match.
No PC gameplay claim, sibling/frozen Release change or push.
All 355 combined tests pass in 829.704 seconds, no skips; tools, whitespace
and 2965 relative links pass. The C transform remains non-matching.

## 2026-10-05 Game Actor Buffer Copy Direct Match

[Note 1011](WORKING_NOTES/1011-game-actor-buffer-copy-direct-match-20261005.md)
recovers `func_1502F948`, all 45 words / frame 0x28 directly exact with
default IDO and no guards/profile override. Cached-ID/fresh-copy semantics
pass 13461 three-way guest cases, 163840 native reference cases and 16384
native gate cases; three incorrect semantic controls fail. Actual wrapper
and SDK-copy connections are bounded, not complete heap/gameplay acceptance.
Only target changes in 6060 slots; protected sections and CSV remain intact.
Counts now 3304 / 5463 total, 2631 / 4790 Game, zero drift. README aggregates
updated; caller stays 109 differences. Next: complete `func_1502F490`.
No sibling/frozen Release change or push.
All 41 focused checks pass in 173.674 seconds; all 343 combined checks pass
in 690.045 seconds, no skips. Tools, whitespace and 2955 relative links pass.

## 2026-10-05 Game Actor Reference Coordinate Phase Match

[Note 1010](WORKING_NOTES/1010-game-actor-reference-coordinate-phase-match-20261005.md)
recovers `func_1502F3C8`, all 50 words / frame 0x30 linked exact with 16
relocation-aware prelude/register/schedule guards. Qualification covers 3841
three-way cases and 82944 native whole-record cases; stale-bound and missing
joint controls fail. Only target changes in 6060 slots; protected sections
and prior patch rows remain intact. Counts now 3303 / 5463 total,
2630 / 4790 Game, zero drift. README aggregates updated; caller remains
109 differences. Next: `func_1502F948`, not a full transform/PC gameplay claim.
All 30 focused checks pass in 99.051 seconds and all 332 combined checks
pass in 374.293 seconds, no skips. Tools, whitespace and 2941 links pass.

## 2026-10-05 Game Actor Pass Lifetime Audit

[Note 1009](WORKING_NOTES/1009-game-actor-pass-lifetime-audit-and-helper-handoff-20261005.md)
banks 176 reproducible compiler controls and 48 bounded guest comparisons.
Twenty focused tests pass in 47.471 seconds, no skips. Production and README
remain unchanged; `func_1502BEE4` still has 109 differing words. Next is its
50-word `func_1502F3C8` phase helper; caller matching remains unfinished.
No sibling/frozen Release change or push.

## 2026-10-05 Game Actor Pass Array Layout Progress

[Note 1008](WORKING_NOTES/1008-game-actor-pass-array-layout-and-connected-selector-20261005.md)
recovers the caller's array offsets and queued-count spill, reducing differences
from 115 to 109. `func_1502BEE4` remains non-matching: 175 body / 176 slot words,
frame 0x88, no new guards/profile override. The maximum-depth spill is still
0x78 rather than 0x34. Nineteen focused checks pass; 400 new three-way cases
connect the existing selector and dispatcher. Only target changes across 6060
slots; protected sections/prior exact functions/patch CSV preserved. Counts
remain 3302 / 5463 total, 2629 / 4790 Game, zero drift; README unchanged.
No conversion/Init ASM or sibling/frozen Release change. Next: caller max-depth
spill, address lifetimes and complete retail schedule.
All 321 combined checks pass in 289.549 seconds, no skips; tools and
whitespace checks pass. No byte-exact function-count increase is claimed.
All 2934 checked relative documentation links resolve.

## 2026-10-05 Game Actor Update Pass Semantic Recovery

[Note 1007](WORKING_NOTES/1007-game-actor-update-pass-semantic-recovery-and-captured-order-20261005.md)
replaces `func_1502BEE4`'s placeholder with live actor scans and captured stable
predecessor-depth updates. This remains non-matching: 174 body / 176 slot
words, frame 0x88, 115 differences, no new guards/profile override. All 771
three-way cases, 257 connected dispatcher cases and 16384 native independent
reference cases pass; seventeen focused checks, no skips. Full phase callees
and gameplay acceptance remain separate. Only target changes in 6060 slots;
previous exact functions/patch CSV unchanged. Build/tools pass. Counts stay
3302 / 5463 total, 2629 / 4790 Game, zero drift; README aggregates unchanged.
No conversion/Init ASM or sibling/frozen Release change. Next: caller stack
layout, register lifetimes and instruction scheduling, without broad guards.
All 319 combined checks pass in 305.557 seconds, no skips; protected sections,
tools, whitespace and 2927 relative links pass.
After `981ec732`, eight local-storage controls pass 64 boundary cases;
none improves matching. Eighteen focused checks pass in 39.427 seconds.
Production remains the banked semantic recovery, with 115 differences.

## 2026-10-05 Game Actor Update Dispatcher Direct Recovery

[Note 1006](WORKING_NOTES/1006-game-actor-update-dispatch-direct-match-and-carried-slot-abi-20261005.md)
replaces `func_1502BD84`'s placeholder with its original callback dispatcher,
work/status stores and live optional-field reads. All 88 words / frame 0x20
emit directly under default IDO, no guards/profile override. The carried slot
argument to `func_1502EEF4` is recovered from its actual prefix and covered by
an omitted-slot counterexample. Nine focused tests pass, including 5194
three-way cases, 49152 native cases/two mutations and 48 bounded real callee
prefixes. Only target changes in 6060 slots; full downstream update acceptance
is not claimed. Rebuild/protected sections/tools pass. README aggregates:
3302 / 5463 overall, 2629 / 4790 Game, zero drift. Patch table, conversion/Init
ASM and sibling/frozen Release unchanged. All 311 combined checks pass in
257.161 seconds, no skips; whitespace/relative links pass. Next:
`func_1502BEE4`, full caller.

## 2026-10-05 Game Actor Display-List Scan Recovery

[Note 1005](WORKING_NOTES/1005-game-actor-display-list-scan-match-and-live-callback-state-20261005.md)
replaces `func_1502BAD0`'s placeholder with its 25-actor SDK display-list scan.
All 173 words / frame 0x48 match under default IDO with eleven closed
constant-register/equality-order guards. Three-way target and native C
qualification cover asymmetric signed alpha gates, callback-mutated state,
cursor returns, full tables and signed-view lifetime. Thirteen focused tests
pass, no skips. Only target changes across 6060 slots; retained caller/renderer
placeholders are preserved, not claimed complete. Rebuild/protected sections/
tools/whitespace pass. README aggregates: 3301 / 5463 overall, 2628 / 4790 Game,
zero drift. Conversion/47 retained Init ASM functions and sibling/frozen Release
unchanged. All 302 combined checks pass in 265.481 seconds, no skips; relative
links resolve. Next: `func_1502BD84`, actor update callback dispatcher.

## 2026-10-05 Game Resource Size Query Direct Recovery

[Note 1004](WORKING_NOTES/1004-game-resource-size-query-direct-match-and-aligned-header-20261005.md)
replaces `func_1502B9B4`'s placeholder with SDK-varargs traversal, rounded
raw size and aligned compressed-header read. All 69 body / 71 slot words
and frame 0x68 emit directly under default IDO O2/g3, no guards/profile
override. Incoming descriptor and both private-header choices remain;
native qualification uses positive descriptor-writing paths and explicit
MIPS u64 alignment. Actual lookup/cache and Init caller prefixes pass,
stopping before bank load without claiming full audio startup. The aligned
caller declaration changes no caller words; only target changes in all
6060 audited slots. Rebuild/protected sections/tools/whitespace/links pass;
all 272 combined checks pass in 239.593 seconds, no skips.
README aggregates: 3300 / 5463 overall,
2627 / 4790 Game, zero drift. Conversion/Init ASM, patch table and sibling/
frozen Release unchanged. Next: `func_1502BAD0`, 25-actor display-list scan.

## 2026-10-05 Game Counted Pointer Loader Direct Recovery

[Note 1003](WORKING_NOTES/1003-game-counted-pointer-loader-direct-match-and-full-caller-20261005.md)
replaces `func_1502B7F0`'s placeholder with SDK-varargs traversal, pointer
output and separate unsigned returned size. All 60 words / frame 0x48
emit directly under default IDO O2/g3; no guards/profile override. Original
incoming descriptor/private size and live pointer-store/size-reload order
are retained. Native qualification is positive descriptor-writing paths
only. Actual lookup/cache/block and 432 full Game caller cases pass,
including unsigned division/fallback behavior and NULL/nonzero size.
The shared declaration/caller cast are aligned; all 6060 slots audited,
only target changes. Rebuild/protected sections/tools/whitespace pass. All
261 combined checks pass in 217.336 seconds, no skips. README aggregates: 3299 / 5463 overall,
2626 / 4790 Game, zero drift. Conversion/Init ASM, patch table and sibling/
frozen Release unchanged. Next: `func_1502B9B4`, phase-aligned header size query.

## 2026-10-05 Game Optional-Size Loader Direct Recovery

[Note 1002](WORKING_NOTES/1002-game-optional-size-loader-direct-match-and-live-output-aliases-20261005.md)
replaces `func_1502B5C8`'s zero-return placeholder with semantic optional-size
SDK-varargs traversal and block loading. All 61 words / frame 0x50 emit
directly under default IDO O2/g3, no guards/profile override. Incoming descriptor
seeds, separate fallback storage, live output/descriptor aliases and distinct
allocation-failure sizes are preserved. Native qualification is positive
descriptor-writing paths only, not defined native zero-depth behavior.
Boundary/actual-callee/global-alias and 108 full Game caller cases pass;
six aligned caller declarations/casts preserve complete retail-exact slots.
All 247 final checks pass in 246.404 seconds, no skips; tools/whitespace pass.
Rebuild/protected-section checks pass. README aggregates: 3298 / 5463 overall,
2625 / 4790 Game, zero drift. Conversion/Init ASM, patch table and sibling/
frozen Release unchanged. Next: `func_1502B7F0`, 60 words / 0x48 frame,
pointer output with separate returned size rather than commented void body.

## 2026-10-05 Game Buffer Variadic Wrapper Direct Recovery

[Note 1001](WORKING_NOTES/1001-game-buffer-variadic-wrapper-direct-match-and-incoming-descriptor-frame-20261005.md)
replaces `func_1502B8E0`'s zero-return placeholder with semantic SDK-varargs
traversal and caller-buffer loading. All 53 words / frame 0x48 emit directly
under default IDO O2/g3, no guards/profile override. The unwritten descriptor
at entry SP-0x14 remains seed-sensitive on zero depth; target tests preserve
that instruction behavior without claiming defined native C. Native tests
execute positive descriptor-writing paths only. Boundary/actual-callee and
48 full Game caller cases pass; eight mismatch prefixes stop at syscall.
Maintained Game/Init caller prototypes are aligned and full slots/frames
remain exact. The third original caller is still a placeholder, reference only.
Rebuild and protected-section comparisons pass. All 232 final checks pass in
178.769 seconds, no skips; tools/whitespace pass. README aggregates:
3297 / 5463 overall, 2624 / 4790 Game, zero drift. Conversion/Init ASM, patch
table and sibling/frozen Release unchanged. Next: `func_1502B5C8`, 61 words /
0x50 frame, including optional size-output aliases and zero-depth seed state.

## 2026-10-05 Game Caller-Buffer Resource Loader Direct Recovery

[Note 1000](WORKING_NOTES/1000-game-caller-buffer-resource-loader-direct-recovery-and-syscall-boundary-20261005.md)
replaces `func_1502B224`'s zero-return placeholder with its semantic raw/
compressed caller-buffer loader. All 75 words / frame 0x30 emit directly under
default IDO O2/g3, no guards/profile override. Native/boundary/600 connected
retail-caller checks preserve cap rounding, header capture/live scratch and
retained decoded count. Forty mismatch-prefix cases stop at the actual syscall
boundary; returning error hooks are not real trap/cleanup qualification.
All 221 final checks pass in 161.605 seconds, no skips; protected Init
code/data, Debugger code and Game data remain exact. Rebuild succeeds.
README: 3296 / 5463 overall, 2623 / 4790 Game, zero drift.
Conversion/Init ASM, patch table and sibling/frozen Release unchanged.
Next: `func_1502B8E0`, 53 words / frame 0x48; preserve its zero-depth incoming
descriptor seed rather than synthesizing initialization.

## 2026-10-05 Game Variadic Table-Address Resolver Recovery

[Note 999](WORKING_NOTES/999-game-variadic-table-address-resolver-recovery-and-connected-init-caller-20261005.md)
recovers `func_1502B020` from its zero-return placeholder. All 60 linked words
and frame 0x48 match with two checked independent loop-store guards; raw C
has two differences, with no profile/insertion/omission change. Boundary and
actual lookup/cache hit/miss checks retain zero-depth size one, full argument
consumption, optional output aliases and final descriptor reread. Connected
retail Init sound-caller cases cover 42/43 reachable words. Both Init caller
prototypes now match the recovered interface; full rebuild retains Init
exactness. All 210 final checks pass in 172.769 seconds, no skips; both caller
slots and protected Init code/data, Debugger code and Game data remain exact.
README totals: 3295 / 5463 overall, 2622 / 4790 Game, zero drift.
Conversion/Init ASM unchanged; sibling/frozen Release untouched.
Next: `func_1502B224` raw/compressed resource loader, 75 words / frame 0x30.

## 2026-10-05 Game Variadic Table-Range Wrapper Recovery

[Note 998](WORKING_NOTES/998-game-variadic-table-range-wrapper-recovery-and-guarded-loop-stores-20261005.md)
recovers `func_1502B110` from its zero-return placeholder. Its full 69-word /
0x48-frame body matches with two checked independent loop-store guards;
raw C still has two differences, no profile/insertion/omission change. All
8316 boundary and 200 actual-callee three-way cases pass, with 1386 native
boundary and 544 actual-C connected cases retaining SDK varargs, descriptor
gates and original range arguments. Full consumer rebuild succeeds. All 199
final checks pass in 148.664 seconds, no skips; protected Init code/data,
Debugger code and Game data remain exact. README
totals: 3294 / 5463 overall, 2621 / 4790 Game, zero drift. Conversion/Init ASM
unchanged; sibling/frozen Release untouched. Next: `func_1502B020` resolver.

## 2026-10-05 Game Table-Range Loader Direct Recovery

[Note 997](WORKING_NOTES/997-game-table-range-loader-direct-recovery-and-caller-qualification-20261005.md)
recovers `func_1502AF04` from its zero-return placeholder. Its 71-word DMA and
in-place pair-offset body matches directly, including the 0x40 frame; no
guards or profile override. The safely sequenced DMA arguments reject an
otherwise raw-exact unsequenced form. All 6336 native, 12672 instruction and
60 connected retail-wrapper cases pass. All 190 final checks pass, no skips,
with protected sections exact after rebuilding. README totals:
3293 / 5463 overall, 2620 / 4790 Game, zero drift. Conversion/Init ASM and
patch table unchanged; sibling/frozen Release untouched. Next:
recover variadic table-range wrapper `func_1502B110`.

## 2026-10-05 Game Cached Lookup Guarded Match

[Note 996](WORKING_NOTES/996-game-cached-lookup-frame-and-guarded-miss-path-match-20261005.md)
matches all 159 linked `func_1502AC88` words. The recovered 0xA0 frame/local
layout emits the complete hit path directly; twelve checked miss-path guards
normalize temporaries and ABI-equivalent buffer alignment. Raw C is still
twelve words different, with no profile, insertion or omission change. All
11088 connected three-way cases and 1056 native hit aliases pass, including
live clock/output alias behavior and both stack phases. All 183 final checks
pass, no skips; full consumer rebuild and protected-section identity hold.
README totals: 3292 / 5463 overall, 2619 / 4790 Game, zero drift.
Conversion/Init ASM unchanged; sibling/frozen Release untouched. Next:
recover table-range loader `func_1502AF04` from its zero-return placeholder.

## 2026-10-05 Game Cache Installer Alias-Preserving Guarded Match

[Note 995](WORKING_NOTES/995-game-cache-installer-alias-preserving-word-copy-and-guarded-match-20261005.md)
matches all 97 linked `func_1502AB04` words using its one-word offset copy and
41 checked schedule/register guards. Raw C remains 41 words different; no
insertion, omission, profile or interface changes. All 2550 new three-way cases
retain exact reads and independent store windows, with every omitted-guard
control rejected. Native overlap gates remain intact. All 176 final checks pass,
no skips; full consumer rebuild and protected-section identity hold. README
totals: 3291 / 5463 overall, 2618 / 4790 Game, zero drift.
Conversion/Init ASM unchanged; sibling/frozen Release untouched. Next:
cached lookup `func_1502AC88`.

## 2026-10-05 Game Cache Installer Frame And Alias Gate

[Note 994](WORKING_NOTES/994-game-cache-installer-frame-recovery-and-pair-copy-alias-gate-20261005.md)
recovers the complete `func_1502AB04` prologue and retail 0x28 frame; raw
differences fall from 93 to 74. Production remains non-matching, with scalar
copies and no new guards/profile changes. A raw-exact aggregate-copy candidate
is rejected for changing a native partially overlapping input descriptor.
All 171 final checks pass, no skips; 833 bounded native aliases and 2550
three-way instruction traces retain live reads and final cache memory.
Protected sections remain exact. A 97-word one-word-copy trial remains experimental
at 41 differences. Exact/conversion counts and README aggregates unchanged;
no sibling source/build/save or frozen Release change.

## 2026-10-05 Game Block Loader Direct Match

[Note 993](WORKING_NOTES/993-game-block-loader-direct-output-size-and-frame-match-20261005.md)
matches all 86 `func_1502B350` words directly from C, including the retail
0x30 frame, without guards or profile changes. All 165 combined checks pass,
no skips; connected resource fixtures, neighboring exact routines and complete
Init/Debugger/data identity hold. The 37-form / 296-trial source/profile screen
reproduces the result. README totals: 3290 / 5463 overall, 2617 / 4790 Game,
zero drift. Conversion/Init ASM unchanged; no sibling source/build/save or
frozen Release change. Next: cache installer `func_1502AB04`.

## 2026-10-05 Game Offset Relocator Guarded Match

[Note 992](WORKING_NOTES/992-game-offset-relocator-typed-scan-and-guarded-bulk-match-20261005.md)
matches all 72 linked `func_1502B4A8` words with a typed automatic-count scan
and seventeen temporary-register guards. Not a direct compiler match; the
77-word variadic loader remains raw-exact. All 161 combined checks pass,
including 5113 three-way relocation cases and partial-allocation rejection.
Full consumer rebuild and complete Init/Debugger/data identity hold. README
totals: 3289 / 5463 overall, 2616 / 4790 Game, zero drift. Conversion/Init ASM
unchanged; no host source/build/save or frozen Release change. Next: `func_1502B350`.

## 2026-10-05 Game Variadic Resource Loader Direct Match

[Note 991](WORKING_NOTES/991-game-variadic-resource-loader-direct-stack-match-20261005.md)
matches the complete 77-word `func_1502B6BC` slot directly from C, with its
retail 0x50 frame. Local fallback selection and descriptor declaration order
resolve seventeen differences without guards/profile/interface changes.
All 155 combined checks pass, no skips; complete Init/Debugger/data remain
exact. README totals: 3288 / 5463 overall, 2615 / 4790 Game, zero drift.
Conversion/Init ASM unchanged; no sibling source/build/save or frozen Release
change. Next matching target: offset relocator `func_1502B4A8`.

## 2026-10-05 Game Attachment Guarded Register Match

[Note 990](WORKING_NOTES/990-game-attachment-walker-guarded-register-match-20261005.md)
matches the complete 45-word linked `func_15168E54` slot with nine expected-word
guards. Unguarded C still differs at nine words; source/profile unchanged.
All 154 combined checks pass, including full-word three-way instruction
coverage and exhaustive native opcode/subtype tests. Full consumer rebuild
and complete Init/Debugger/data identity hold. README exact totals: 3287 / 5463
overall, 2614 / 4790 Game, zero drift. No conversion/Init ASM or host/frozen
Release changes; sibling already has the retail attachment sequence.

## 2026-10-05 Game Resource Helper Direct Match

[Note 989](WORKING_NOTES/989-game-resource-helper-address-word-direct-match-20261005.md)
completes all 46 words of `func_151336A8`, including retail's final address
handoff, directly from C with no guards/profile/interface changes. All 148
combined checks pass, no skips; connected resource/texture tests and protected
section identities hold. README exact totals: 3286 / 5463 overall, 2613 / 4790
Game, zero drift. No new conversion or Init ASM reduction. Sibling already
has this helper's retail sequence; no host or frozen Release changes.

## 2026-10-05 Game Immediate Texture Release Direct Match

[Note 988](WORKING_NOTES/988-game-immediate-texture-release-direct-frame-match-20261005.md)
completes all 46 words of `func_1510D7AC` without guards or profile changes.
Full table-indexed C with captured signed priority recovers the retail 0x28
frame and incoming-ID spill/reload. Three new checks reproduce the source
screen and preserve neighbors; the actual lifecycle suite still qualifies
callback changes and connected release/maintenance/reload. All 65 combined
checks pass, no skips; complete Init/Debugger/data remain exact. README exact
totals are now 3285 / 5463 overall, 2612 / 4790 Game, zero drift. Conversion
and Init ASM counts unchanged; host placeholder/frozen Release untouched.

## 2026-10-05 Game Nullable Cleanup Direct Rematch

[Note 987](WORKING_NOTES/987-game-nullable-cleanup-typed-pointer-direct-rematch-20261005.md)
restores all nineteen words of `func_150F631C` by reading typed pointer fields
against the current cleanup prototype. No guards or profile changes. All 62
combined checks pass, including 343 callback cases and protected section
identity. Fresh exact totals: 3284 / 5463 overall, 2611 / 4790 Game, zero drift.
README aggregate snapshot updated; details remain here and in working notes.
No new C conversion, Init ASM reduction or sibling/frozen Release change.

## 2026-10-05 Game Light Selector Experiment

[Note 986](WORKING_NOTES/986-game-light-selector-candidate-fitting-and-connected-frame-witness-20261005.md)
banks full experimental `func_1515D914` and fourteen qualification checks.
No-unroll complete text fits at 2224 / 2404 bytes; three profiles pass 17410
standalone pairs each and the native fixture passes 192 retail-derived cases.
A twelve-pair connected witness rejects promotion: the renderer's changed
frame moves the first-directional seed and changes count/cursor. All 109
final combined checks pass, no skips, with complete existing Init/Debugger/data
exact. No production owner, README aggregate or sibling/frozen Release change.
The formerly paused Game experiment files are banked together in this checkpoint.

## 2026-10-05 Init Bitmap Unsigned Sentinel

[Note 985](WORKING_NOTES/985-init-bitmap-unsigned-one-past-record-fitting-20261005.md)
adds opt-in ordered scalar/grouped unsigned one-past trials and fourteen checks.
Record no-unroll C fits nineteen words with no XOR, but sixteen differ and
retail's increment-delay lifetime is not recovered. Whole text stays 80 bytes.
Final candidates pass 1098 complete paired traces and eighteen prefixes;
zero-stop and read-order controls prevent final-memory-only qualification.
All 154 combined checks pass, no skips; old preprocessing and complete existing
Init/data plus Game data hold. No production adoption, README aggregate or
sibling/frozen Release change; paused Game experiments remain excluded.

## 2026-10-05 Init Pause-Resume Decision

[Note 984](WORKING_NOTES/984-init-pause-resume-current-conversion-readiness-20261005.md)
refreshes all 47 remaining ASM owners and the conversion queue. Seventeen
entries remain investigation targets; thirty intentionally retain assembly.
No replacement is ready: bitmap/MMIO full matches unresolved, decoder 512
bytes over and formatter connection 196 over, with ownership gates open.
All 140 fresh checks pass, no skips, including current byte-depth size/hash
reproduction and complete existing Init/data plus Game-data identity.
Detailed next steps stay in working docs; no README aggregate or production
change. Preserve the three paused Game experiment files outside this checkpoint.

## 2026-10-05 Game Viewport Renderer

[Note 983](WORKING_NOTES/983-game-viewport-renderer-semantic-recovery-20261005.md)
recovers complete `func_1510B9D0`, its typed public declaration and explicit
legacy caller casts without changing the caller's bytes. C fits 347 / 356 words,
frame 0xB8 versus 0x98 retail, 343 differences, no guards/profile override.
All 95 final combined checks pass after shared-header rebuild/link: 5379 paired
renderer traces, 96 actual connected leaves, 4608 native cases, four invalid
prefixes. Complete existing Init/Debugger/data stay exact. Downstream placeholders,
original-frame matching and natural pixels remain open. No README aggregate,
Init conversion, sibling/frozen Release change or push.

## 2026-10-05 Game Command Helper

[Note 982](WORKING_NOTES/982-game-viewport-command-helper-semantic-recovery-20261005.md)
recovers complete `func_1510B7B4` from its placeholder: 103 / 105 words,
twelve packets, 104 raw differences, no guards/profile override. All 81 combined
checks pass after fresh source build/padding/link, including 65600 native cases,
97 paired traces and three invalid prefixes. Complete existing Init/Debugger/data
remain exact. README aggregates, Init owners and sibling/frozen Release unchanged.
Full `func_1510B9D0` renderer and natural submission/pixels remain open.

## PC-port cross-project update - 2026-09-23

The sibling `64CBFDOGL` host port now completes Training through the natural Windy entrance and a fresh retained-save reload in RelWithDebInfo; repeat traversal used FLY. The user has **VERIFIED the second-level Chapters unlock**. The Gargoyle held-release repair uses original `func_15073A50` (232 bytes); guest/ROM builds and exact-byte checks are recorded in [host Note 738](../../64CBFDOGL/DOCS/WORKING_NOTES/738-gargoyle-actor-and-original-held-release-20260923.md). This is scoped progression evidence, not complete retail presentation or full-game acceptance.

The host-only `conker_settings.exe` is implemented with four-port device assignments, shared keyboard/controller bindings, Save and input hot reload; Video/Audio/Paths remain placeholders. It does not add an N64-ROM settings executable or replace Ares settings. See [host settings guide](../../64CBFDOGL/DOCS/CONKER_SETTINGS.md), [current host status](../../64CBFDOGL/DOCS/CURRENT_STATUS.md) and [active host roadmap](../../64CBFDOGL/DOCS/roadmap.md). Host Release is frozen after the requested 2026-09-23 `conker_pc` build; the latest Training suite retains its documented baseline failures/errors. No guest matching percentage is inferred from these host milestones.

This log tracks repository-facing documentation, workflow, and project maintenance updates.

For code-level progress, run:

```sh
make -C conker progress
```

## 2026-10-02

### 2026-10-05 current Init full corpus checkpoint

- Init [Note 981](WORKING_NOTES/981-init-bitmap-record-view-fitting-and-ordered-read-qualification-20261005.md)
  tests grouped volatile start/end/count field reads. Optimized nineteen-word
  body retains the two-based mask, but seventeen differ; XOR loop/schedule
  remain unresolved and complete standalone text stays 80 bytes. Ten new
  checks qualify 1002 completed ordered retail/C traces, twelve bounded
  prefixes and unused-field read rejection. All 138 combined checks pass in
  70.804 seconds in the final rerun, no skips; complete existing Init/data and Game data hold.
  Forty-four old-shape host/guest preprocessing comparisons hold. No production
  conversion, original-type claim, README aggregate or host/Release change.

- Init [Note 980](WORKING_NOTES/980-init-packed-bit-width-screen-and-restored-candidate-20261005.md)
  screens wide bit-count and both-field locals on the banked byte-depth lead.
  Public builder saves one/three O2 words, but total executable text stays
  4496 bytes after alignment; both profiles gain eight frame/call-bound bytes.
  Reject before semantic qualification, restore source exactly. All 83 fresh
  restored connected/native/inventory/slot/call/reporting checks pass in
  345.010 seconds, no skips; complete existing Init/data and Game data hold.
  No production or test-code change, README aggregate or host/Release change.
  Unchanged candidate retains Note 979's corpus evidence; screens receive none.

- Init [Note 979](WORKING_NOTES/979-init-byte-depth-full-masked-cu1-corpus-qualification-20261005.md)
  qualifies the banked byte-depth packed O2/g3 decoder in both masked CU1
  modes: 507 pages each, 1014 paired runs pass in 1604.214 seconds, no skips.
  Both terminal stack descents are 3248 bytes with 80-byte known-neighbor
  clearance; reservation ownership is not inferred. Candidate hash, complete
  allocation and all eight during-run source hashes hold. After terminal
  receipt verification, reporter-only failure gates and two mocked controls
  are added; all 32 supporting checks pass in 1.483 seconds, no skips.
  Still 4496 / 3984 bytes, 512 over; entry/frame/private-stack/hardware gates
  remain open. No production adoption, README aggregate or host/Release change.

### 2026-10-05 current Init fitting checkpoint

- Init [Note 978](WORKING_NOTES/978-init-mmio-record-view-fitting-and-ordered-access-qualification-20261005.md)
  tests grouped volatile publication fields with scalar and explicit-local
  controls. Direct record saves sixteen complete bytes in three profiles,
  but has nine O2/g3 or eight O1 raw differences; locals worsen O1 text/stack.
  Nine new checks qualify sixty paired traces and order/read/width rejection
  controls with no host MMIO execution. Keep original assembly/declarations;
  no production conversion, original-type provenance or README/host change.
  All 128 combined checks pass, no skips; complete existing Init slots/code/data
  and Game data stay retail-exact. No fresh production relink or hardware claim.

### 2026-10-04 current Init corpus checkpoint

- Init [Note 977](WORKING_NOTES/977-init-bitmap-all-ones-mask-fitting-and-retail-loop-boundary-20261004.md)
  tests an unsigned all-ones bitmap value/mask and an arithmetic control.
  Optimized mask variant fits nineteen words with seventeen raw differences;
  IDO rematerializes the constant, retaining the XOR loop and different tail.
  Whole optimized text stays 80 bytes after alignment, checked by the receipt.
  Reject adoption. Nine new checks qualify 1002 retail/C pairs and twelve
  prefixes; all 119 combined checks and forty old-shape preprocessing
  comparisons pass, no skips. Existing Init slots/code/data and Game data
  stay exact; production owners, README totals and host/Release unchanged.

- Init [Note 976](WORKING_NOTES/976-init-remaining-conversion-decision-and-decoder-cache-matrix-20261004.md)
  records all remaining adoption decisions: seventeen investigation targets,
  thirty intentional owners, no approved replacement. The sixteen-case cache
  interaction matrix has no text/stack win; a persistent parent-mask recurrence
  grows O2 by 32 bytes and increases O1 stack, so its source/selector are
  removed before semantic qualification. Qualified decoder remains 4496 bytes,
  512 over retail including adapter. Bitmap/MMIO/formatter gates remain open;
  78 decoder/owner/slot/call plus 43 bitmap/MMIO/formatter checks pass, no skips.
  All existing Init code/data and Game data remain raw retail-exact;
  production owners, README totals, sibling and frozen Release stay unchanged.

- Init [Note 975](WORKING_NOTES/975-init-builder-byte-depth-induction-and-rejected-replication-helpers-20261004.md)
  qualifies opt-in byte-depth builder induction. Both packed profiles save
  sixteen complete bytes; optimized executable is 4496, still 512 over retail.
  All 58 connected/native and twenty owner/slot/call checks pass, no skips;
  ordered physical table cells and disabled packed hashes are checked.
  Aligned-end O2 grows, so no default change. Both new out-of-line replication
  helpers regress and are removed. Production Init/README/host/Release remain
  untouched; full guarded corpus and entry/frame/private-stack gates stay open.

- Init [Note 974](WORKING_NOTES/974-init-decoder-complement-low-mask-fitting-trial-20261004.md)
  measures the opt-in complemented shared-mask trial. Two words change, but
  optimized allocation remains 4336 C + 176 adapter = 4512 bytes, 528 over.
  All 59 trial checks across two runs and twenty separate owner/slot/call
  checks pass, no skips. Compiled mask classes/high widths, disabled control
  hashes and complete existing Init/data are checked. Fresh size accounting
  directs next fitting to builder/shared-call structure, not this neutral
  identity. No adoption, production relink, README aggregate, host or Release
  change; full guarded corpus and hardware acceptance remain separate.

- Game [Note 973](WORKING_NOTES/973-game-palette-updater-and-connected-color-qualification-20261004.md)
  recovers palette updater `func_1510CB10`: 168 / 170 words, retail 0x68 frame,
  135 raw differences, no guards/profile override/drift. Fourteen new checks
  qualify 398353 native cases, 1251 complete paired traces and three invalid-
  slot prefixes; actual angle helper/updater/color/writer connections pass.
  All 257 combined checks pass after fresh source compile/link; complete
  Init/Debugger/data and previous identities remain intact. README aggregates
  unchanged. Next full renderer 1510B9D0 and helper 1510B7B4; RSP/RDP/natural
  effects and matching remain open. Sibling updater/diagnostics already exist;
  no host or frozen Release changes.

- Game [Note 972](WORKING_NOTES/972-game-palette-color-emitter-byte-match-and-segment-connection-20261004.md)
  finishes pending palette color emitter `func_1510CDB8`: 42 / 42 raw-exact
  words from SDK macros, frameless, no guards/profile override/drift. Six new
  checks include 262144 native alpha cases, 812 complete paired traces, three
  invalid-index prefixes and actual color -> writer; complete module 1710 pairs.
  All 243 combined checks pass after forced source build/link; full Init/
  Debugger/data and prior identities remain intact. Total 3283 / Game 2610
  exact, zero drift, 2180 different. README matching rows updated only; next
  palette updater `func_1510CB10`. Full renderer and natural effects stay open;
  sibling already has the emitter, no host/frozen Release changes.

- Init [Note 971](WORKING_NOTES/971-init-pause-resume-remaining-assembly-decision-20261004.md)
  resumes the requested remaining-ASM decision. All 110 focused checks pass,
  no skips; 492 C / 47 ASM entries and complete existing Init code/data plus
  Game data remain exact. Seventeen investigation targets, thirty intentional
  owners; no replacement is ready. Bitmap is 20 / 19 words, decoder 528 bytes
  over, formatter 196 over; MMIO full C match unresolved. Two interrupted Game
  color-emitter edits stay separate and unbanked. No production Init/README/
  sibling/Release changes or new compiler hypothesis/relink claimed.

- Game [Note 970](WORKING_NOTES/970-game-queued-segment-writer-and-big-endian-alias-qualification-20261004.md)
  recovers SDK-based queued segment writer: 40 / 44 words, frameless, 38 raw
  differences, no guards. Ten new checks include actual queue workflow and
  898 paired big-endian instruction traces, all body instructions and byte
  aliases. Corrupt-count cases use extended storage, not real queue safety.
  All 237 combined checks pass, no skips; fresh link preserves exact helpers,
  complete Init/Debugger/data and previous identities. Next connected color
  emitter `func_1510CDB8`; full renderer and staged producer stay separate.
  No README aggregate or host/frozen Release change.

- Game [Note 969](WORKING_NOTES/969-game-immediate-texture-cache-release-recovery-20261004.md)
  recovers immediate cache release `func_1510D7AC`: 46 / 46 words, four frame/
  spill differences, no guards. Six new tests qualify all 65536 priority/activity
  pairs, every valid ID, callbacks and actual retain/release/maintenance/reload.
  All 227 combined checks pass, no skips; fresh link preserves exact full Init
  code/data, Debugger code, Game data and prior identities. Read-only sibling
  audit finds this helper still a zero-return stub; separate host sync gate.
  Next 44-word queued segment writer `func_1510D8C0`. README/Init/frozen Release
  unchanged; no real allocator/DMA/decoder or natural-effects acceptance claimed.

- Game [Note 968](WORKING_NOTES/968-game-texture-metadata-and-cache-maintenance-recovery-20261004.md)
  finishes interrupted metadata/cache maintenance recovery: 58 / 62 and
  125 / 129 words, 54/119 differences, no guards; maintenance frame 0x40
  against retail 0x60. Seventeen new checks qualify bounded metadata, callback
  ordering and actual connected lifecycle; all 221 combined checks pass,
  no skips. Fresh link preserves complete Init code/data, Debugger code, Game
  data and exact initializer/startup. Resolves the pending Game work described
  by Notes 966/967. Real guest DMA/decoder, staged producer and natural effects
  remain open; next 46-word immediate release `func_1510D7AC`. README/sibling/
  frozen Release unchanged.

- Init [Note 967](WORKING_NOTES/967-init-decoder-entry-value-lifetime-fitting-trials-20261004.md)
  qualifies three immutable entry-value lifetime trials: literal/length and
  combined capture save one optimized compressed-unit word, but final padding
  absorbs the saving. Optimized packed images remain 4512 bytes, 528 over retail.
  All 151 trial checks and twenty ownership/section audits pass, no skips;
  three final size reruns verify padding attribution. Disabled-option instruction
  images remain unchanged; full Init code/data and Game data stay exact. Reject
  adoption; production Init/README and separate pending Game work are unchanged.

- Init [Note 966](WORKING_NOTES/966-init-resume-preincrement-bitmap-and-conversion-decisions-20261004.md)
  resumes the build to success and qualifies a new preincrement bitmap shape:
  32/20/32 words against nineteen, 501 completed model pairs and six prefixes.
  Reject adoption: extra cursor bias and incorrect branch-delay scheduling.
  All 110 focused checks pass, no skips; remaining owners/slots and full Init
  code/data plus Game data stay exact. Retain 47 ASM entries; seventeen are
  investigation targets, thirty intentional owners. Production Init/README
  unchanged. Separate Game metadata/maintenance edits are preserved, buildable
  but not yet behavior-qualified, and excluded from this Init checkpoint.

- Game [Note 965](WORKING_NOTES/965-game-texture-resource-setup-resolver-and-attachment-recovery-20261004.md)
  recovers setup/resolver/attachment: 152 / 163, 155 / 162 and 45 / 45 words,
  159/142/9 differences, retail frames and no guards. Sixteen new tests qualify
  all valid IDs, signed priorities, failures, cleanup and actual helper/setup/
  resolver/attachment; all 204 combined checks and fresh link pass, preserving
  Init code/data, Game data, exact leaves and prior recoveries. Metadata loader
  and cache maintenance remain placeholders; original unwritten scratch and
  actual guest DMA/decoder are unqualified. README/Init/sibling/Release unchanged.

- Init [Note 964](WORKING_NOTES/964-init-remaining-assembly-current-conversion-decisions-20261004.md)
  refreshes the remaining ASM decisions after production relink: 102 focused
  checks pass, no skips; all 47 owners/slots and complete Init code/data plus
  Game data remain exact. Seventeen investigation targets and thirty intentional
  ASM owners remain. No candidate is ready; decoder 528 bytes over, formatter
  196 over, small leaves non-matching. Record bitmap-first pickup steps;
  production Init source and README aggregates remain unchanged.

- Game [Note 963](WORKING_NOTES/963-game-asset-table-cache-lookup-and-block-load-recovery-20261004.md)
  recovers cache installer, metadata-writing lookup and block loader: 87 / 97,
  158 / 159 and 77 / 86 words, 93/156/78 differences, no guards. Fourteen new
  checks connect actual lookup/block/variadic/relocation and qualify cache and
  allocation/decode-result order. All 188 combined checks and fresh link pass,
  preserving Init code/data, Game data, previous recoveries and exact callers.
  Deeper setup/attachment and actual guest DMA/decompression remain open.
  No README aggregate or sibling/Release changes.

- Game [Note 962](WORKING_NOTES/962-game-variadic-resource-loader-and-offset-relocation-recovery-20261004.md)
  recovers the variadic resource loader and offset relocation helper: 77 / 77
  and 65 / 72 words, 17 and 71 differences, no new guards. Typed interfaces
  preserve three exact callers; fourteen new tests connect actual constructor/
  helper/loader/relocation and other callers. All 174 combined checks and fresh
  link pass, retaining Init code/data, Game data and prior recoveries. Lookup
  and block-load placeholders still prevent production loading qualification.
  No README aggregate, retained Init assembly or host changes.

- Game [Note 961](WORKING_NOTES/961-game-extended-child-constructor-and-resource-helper-recovery-20261004.md)
  recovers extended constructor `func_1513264C` and resource helper `func_151336A8`:
  255 / 256 and 45 / 46 words, 184 and nine differences, no guards. Fifteen new
  tests connect actual child/constructor/helper bodies; all 160 combined tests
  and fresh link pass, preserving complete Init code/data, Game data and prior
  recoveries. Three deeper loader/setup/attachment placeholders remain; no
  pipeline/gameplay acceptance or host changes. README/Init aggregates unchanged.

- Game [Note 960](WORKING_NOTES/960-game-extended-child-emission-semantic-recovery-20261004.md)
  recovers `func_150E93DC` and its pointer wrapper: 206 body / 208 slot words,
  0x138 frame, 200 raw differences, no guards; wrapper stays fifteen-word exact.
  Thirteen new tests and all 145 combined checks pass, no skips. Fresh link
  preserves complete Init code/data, Game data and prior recoveries. Retail's
  descriptor holes and 28-byte extra payload stay unspecified. Constructor
  `func_1513264C` remains a placeholder; recover it and qualify resource helpers
  next. PC child synchronization remains separate; Init/README unchanged.

- Init [Note 959](WORKING_NOTES/959-init-decoder-packed-parent-and-bit-tail-fitting-trials-20261004.md)
  qualifies new packed-parent and shared-refill/inline-tail experiments:
  optimized totals are 4528 / 4544 bytes, both worse than 4512 baseline.
  All 125 trial and baseline audit/ledger tests pass, no skips; default-option
  instruction images remain unchanged. Reject production adoption; Init/README
  counts and exact existing linked code/data remain intact. Full corpora and
  connected stack/entry ownership remain separate gates.

- Init [Note 958](WORKING_NOTES/958-init-resume-remaining-assembly-readiness-20261004.md)
  resumes the requested assembly-conversion assessment: 102 fresh checks pass,
  no skips; all retained owners/slots and complete existing Init code/data and
  Game data stay exact. Seventeen entries are investigation targets, thirty
  remain intentional assembly. Decoder is 528 bytes over; best connected
  formatter 196 over. Small leaves lack complete matches, although older bitmap
  forms fit. No production source or README changes; Game child left untouched.

- Game [Note 957](WORKING_NOTES/957-game-extended-weighted-emitter-semantic-recovery-20261004.md)
  recovers `func_150E9178` and its 60-byte payload: 153 words / 0xF8 frame,
  54 differences, no guards. Eleven new connected tests; all 132 combined tests
  and fresh link pass, preserving complete Init code/data, Game data and exact
  neighbors. README unchanged. PC source synchronization is open; next recover
  placeholder child `func_150E93DC` before claiming a complete effect pipeline.

- Game [Note 956](WORKING_NOTES/956-game-child-emission-callback-recovery-and-fitting-20261004.md)
  finishes `func_150E8D5C` and pointer interfaces: 219 words / 0x120 frame,
  213 differences, no guards, resolving the 225 / 224 fitting failure.
  Thirteen new child/chain tests and fresh relink preserve full Init code/data,
  Game data and exact constructor/wrappers/helpers. All 121 combined tests pass,
  no skips; README aggregates unchanged.
  PC-port child source is still a stub: synchronization and gameplay remain
  open, with `func_150E9178` the next DECOMP semantic target.

- Init [Note 955](WORKING_NOTES/955-init-bitmap-fill-value-right-shift-mask-trial-20261004.md)
  rejects a new right-shift mask/value-lifetime shape: 20 optimized words
  against nineteen retail. Eight new tests qualify 501 pairs/six prefixes;
  34 combined tests pass, no skips. Init source, exact existing sections and
  README totals unchanged; next recover the preserved Game child fitting gate.

- Init [Note 954](WORKING_NOTES/954-init-resume-conversion-decision-and-interrupted-game-build-20261004.md)
  verifies 492 C / 47 assembly entries, exact retained owners and existing linked
  Init/Game data. Ninety-three focused tests plus one fresh decoder size check
  pass; no candidate is ready to adopt. Decoder remains 528 bytes over, and
  connected glyph ownership/fitting is open. Interrupted Game child build
  fails by one word (225 / 224); its source/interface edits remain preserved
  and unqualified. No production Init or README aggregate changes.

- Game [Note 953](WORKING_NOTES/953-game-descriptor-position-writer-and-weighted-chain-recovery-20261004.md)
  restores the four-mode descriptor-position writer and void interface,
  179 words / 0x78 frame in its 218-word slot, 196 differences, no guards.
  Eleven new tests connect the actual weighted caller and helpers; 100 combined
  tests and fresh link pass. Complete Init code/data, Game data and exact
  neighbors remain intact. Position-placeholder
  gate resolved in source/tests; child callback remains unrecovered. README
  aggregates unchanged, no gameplay acceptance or sibling/Release promotion.

- Init [Note 952](WORKING_NOTES/952-init-bitmap-address-difference-induction-trial-20261004.md)
  rejects a new address-difference folding trial: 22 O2 words against nineteen,
  despite removing XOR. Eight new tests / 501 pairs / six bounded prefixes and
  93 combined Init tests pass. Retained ownership and full existing Init/data
  images remain exact; README aggregates and pending Game recovery unchanged.

- Init [Note 951](WORKING_NOTES/951-init-resume-conversion-readiness-and-repeatable-audit-20261004.md)
  refreshes the remaining-assembly decision: 47 entries / 12,252 bytes, with
  two small C candidates, ten connected decoder and five diagnostic entries,
  and thirty retained boot/hardware/SDK owners. Seven new audit checks,
  78 retained tests and 46 freshly compiled decoder tests pass: 131 across three
  runs, no skips. Decoder remains 528 bytes over; all existing Init code/data
  and Game data stay exact.
  No production conversion or README aggregate change; pending Game work kept.

- Game [Note 950](WORKING_NOTES/950-game-weighted-event-emitter-semantic-recovery-20261004.md)
  recovers the code-0x33 weighted emitter, 144 words / original 0xC8 frame,
  44 differences and no guards. Ten new / 82 combined tests and fresh link
  pass; complete Init/Game data and exact neighbors stay intact. README
  aggregates unchanged. Its placeholder position-writer dependency is an
  explicit runtime gate and the next recovery priority, not accepted gameplay.

- Game [Note 949](WORKING_NOTES/949-game-event-payload-creators-and-connected-dispatch-match-20261004.md)
  completes both preserved event creator recoveries, 39/39 words each directly
  matching with no guards. Seven new tests qualify actual dispatcher/timer
  chains; all 72 combined tests and fresh production link pass. Full Init,
  Game data and exact neighbors remain intact. README matching rows now show
  Game 2609 / total 3282 exact; representation counts stay unchanged.

- Init [Note 948](WORKING_NOTES/948-init-bitmap-equality-exit-lifetime-trials-20261004.md)
  tests two new exit-region/address-lifetime shapes. Eight tests qualify
  1,002 fresh guest pairs and twelve bounded prefixes; both optimized bodies
  are 21 words, so neither replaces the nineteen-word assembly owner.
  All 78 combined tests pass, no skips.
  Existing linked Init code/data, README totals and pending Game edits stay
  unchanged; compiler/control-flow rejection evidence is retained in the docs.

- Init [Note 947](WORKING_NOTES/947-init-remaining-assembly-conversion-map-20261004.md)
  maps all 47 remaining assembly entries and distinguishes C-expressible
  candidates from qualified replacements. Seventy tests pass; existing linked
  Init sections, all retained slots and complete Game data remain exact.
  No production conversion, rebuild or README aggregate change is claimed;
  two unfinished Game edits remain untouched and outside this checkpoint.

- Game [Note 946](WORKING_NOTES/946-game-event-packet-and-sound-dispatch-direct-match-20261004.md)
  recovers `func_150E8930`, all 84 words directly matching with no guards.
  Sixty-five tests and fresh link pass; its timer caller remains exact, and
  complete Game data/Init and neighbors are preserved. README matching rows
  now show Game 2607 / total 3280 exact. Both follow-up creators remain open.

- Game [Note 945](WORKING_NOTES/945-game-world-emitter-dispatch-direct-byte-match-20261004.md)
  recovers `func_150E81A8` and matches all 129 words directly from C. Fifty-nine
  tests and a fresh production relink pass; full Game data, Init code/data and
  neighboring exact bodies are preserved. README matching rows now show Game
  2606 / total 3279 exact; detailed recovery evidence stays in working docs.

- Init [Note 944](WORKING_NOTES/944-init-bitmap-exit-edge-control-flow-trials-20261004.md)
  records two new exit-edge source shapes and eight guest-fixture tests.
  All 54 combined tests pass, with 1,002 new pairs/twelve bounded prefixes;
  neither form improves complete-slot fitting. Original Init owners and
  README aggregates stay unchanged; the next Game semantic target is retained.

- Init [Note 943](WORKING_NOTES/943-init-resume-linked-baseline-and-conversion-shortlist-20261004.md)
  verifies the current linked Init code/data and all 47 retained assembly
  slots, refreshes the 492-C inventory and records the conversion shortlist.
  Sixty-two focused tests pass; no production replacement is ready. The
  successful up-to-date build check is distinguished from a fresh relink.
  Detailed assessment stays in working docs; README aggregates unchanged.

- Game [Note 942](WORKING_NOTES/942-game-physical-data-order-and-literal-pool-restoration-20261004.md)
  closes the physical data-layout gate: all 189,088 bytes / 720 owners match
  retail after owner-order, literal-pool and targeted padding repairs. The
  full link and 53 tests pass; Init is preserved and instruction aggregates
  remain unchanged. Detailed results stay here, not in the README.

- Init [Note 941](WORKING_NOTES/941-init-bitmap-unsigned-induction-guest-qualification-20261004.md)
  records two rejected unsigned-induction bitmap trials and new actual guest
  differential tests. All 46 focused tests pass; 1,002 completed pairs and
  twelve bounded prefixes preserve alias/wrap contracts. No production owner
  or README aggregate changes; the existing Game link repair remains separate.

- Init [Note 940](WORKING_NOTES/940-init-pause-resume-conversion-decision-20261004.md)
  refreshes the pause-resume decision: 492 C / 47 assembly entries, all source
  owners verified, 54 focused tests passing. Remaining candidate gates and
  ordered next steps are explicit; README aggregates stay unchanged. Preserved
  baseline Init bytes are exact, distinct from the unfinished Game link trial.

- Game [Note 939](WORKING_NOTES/939-game-curve-update-direct-match-and-data-placement-gate-20261004.md)
  recovers `func_150E7C9C`, all 212 words directly matching with no guards.
  Thirty-two tests pass; README shows Game 2605 / total 3278 exact. A separate
  physical Game-data placement check fails for the pan coefficient, so runtime
  acceptance is open and layout auditing takes priority over another batch.

- Game [Note 938](WORKING_NOTES/938-game-random-curve-record-direct-byte-match-20261004.md)
  replaces `func_150E7994`'s placeholder with its sampled curve builder and
  matches all 194 words directly from C. Twenty-six focused tests pass; no
  guards or drift. README matching rows now show Game 2604 / total 3277 exact;
  conversion counts and Init production ownership remain unchanged.

- Game [Note 937](WORKING_NOTES/937-game-random-edge-emitter-semantic-recovery-20261004.md)
  recovers alternate emitter `func_150E76D0` with twenty-one focused tests
  passing. Both actual dispatcher/helper paths are exercised; production body
  fits its slot with no drift or guards. Byte matching remains open and
  README aggregates are unchanged. Init production ownership is unchanged.

- Init [Note 936](WORKING_NOTES/936-init-split-destination-validation-interface-trial-20261004.md)
  rejects the split-validation interface as a fitting improvement. All 1,728
  paired fixtures and sixteen combined tests pass; keep original owners and
  resume the unfinished Game alternate emitter recovery next.

- Init [Note 935](WORKING_NOTES/935-init-shared-formatter-setup-text-stack-tradeoff-20261004.md)
  measures shared destination setup: sixteen-byte text saving with increased
  stack cost. Sixteen combined tests and 1,152 paired fixtures pass; retain
  the experiment opt-in without changing production or README totals.

- Init [Note 934](WORKING_NOTES/934-init-connected-semantic-c-formatters-and-layout-cost-20261004.md)
  recovers both connected C formatter trials with 576 paired fixtures passing.
  Fifteen combined tests pass; measured text/stack costs keep production
  ownership and README aggregates unchanged.

- Init [Note 933](WORKING_NOTES/933-init-glyph-adapter-production-placement-and-stack-boundaries-20261004.md)
  adds production adoption boundary checks: occupied experimental address,
  fifteen caller sites and two stack regimes. Twenty tests pass; conditional
  overlay containment is not production ownership or a C conversion.

- Init [Note 932](WORKING_NOTES/932-init-connected-glyph-c-adapter-qualification-20261004.md)
  qualifies the connected glyph C adapter with twenty combined tests passing.
  Added executable/stack cost is measured; production layout/ownership remain
  open, so source owners and README aggregate tables are unchanged.

- Init [Note 931](WORKING_NOTES/931-init-glyph-pixel-seeding-and-countdown-fitting-20261004.md)
  fits the experimental glyph C body in 29 words with 2,128 paired fixtures
  passing. Connected adapter and layout gates remain open; this is fitting
  progress, not a production conversion or README aggregate change.

- Init [Note 930](WORKING_NOTES/930-init-semantic-glyph-writer-differential-qualification-20261004.md)
  adds a compiled semantic glyph trial and 798 paired ordered-memory/alias
  fixtures. Sixteen combined tests pass; smallest body remains one word larger
  than retail before adapter cost. No production conversion claimed.

- Init [Note 929](WORKING_NOTES/929-init-connected-glyph-formatter-contracts-20261004.md)
  qualifies connected formatter/setup/glyph execution and delay-slot cursor
  behavior. Twenty-four combined tests pass; C/adapters remain experimental
  next work, with no production conversion or README aggregate change.

- Init [Note 928](WORKING_NOTES/928-init-glyph-writer-register-and-pixel-contract-20261004.md)
  adds executable glyph register/pixel contracts across 262 rendering fixtures.
  Nineteen combined tests pass; connected interfaces/adapters remain open,
  production source and README aggregates unchanged.

- Init [Note 927](WORKING_NOTES/927-init-bitmap-unsigned-range-comparison-trials-20261004.md)
  retains two rejected unsigned-range bitmap trials: twenty O2 words versus
  nineteen retail. All 869 bounded host fixtures and 33 retained-contract
  tests pass; production ownership and README aggregates remain unchanged.

- Init [Note 926](WORKING_NOTES/926-init-remaining-assembly-readiness-refresh-20261004.md)
  refreshes the remaining assembly decision: 47 entries / 12,252 bytes,
  two small C candidates, decoder 528 bytes too large with ownership gates
  open. Thirty-eight focused tests pass; no production conversion claimed.

- Game [Note 925](WORKING_NOTES/925-game-positioned-emitter-descriptor-recovery-20261004.md)
  recovers the positioned emitter helper and pins descriptor extent through
  the retail callee's 0x58-byte copy. Sixteen tests pass; 74 words fit the
  76-word slot with 69 differences, no guards/drift. README aggregates unchanged.

- Game [Note 924](WORKING_NOTES/924-game-probability-gated-random-dispatch-recovery-20261004.md)
  recovers both random-dispatch branches plus the shared tail. Fifteen tests
  pass; 195-word body fits its 196-word slot with 183 differences, no guards.
  Adjacent call ABIs typed; helper bodies still placeholders. README unchanged.

- Game [Note 923](WORKING_NOTES/923-game-fixed-random-parameter-initializer-match-20261004.md)
  recovers the fixed/random initializer as a direct 43-word C match. Fourteen
  focused tests pass, including complete independent IDO equality. Fresh
  matcher Game 2603 / total 3276 exact, zero drift; README aggregates refreshed.

- Game [Note 922](WORKING_NOTES/922-game-vector-random-parameter-initializer-match-20261004.md)
  recovers the vector/random parameter initializer as a direct 62-word match.
  Five new tests / fourteen combined pass, including complete independent IDO
  equality. Fresh matcher Game 2602 / total 3275 exact; README aggregates refreshed.

- Game [Note 921](WORKING_NOTES/921-game-linked-record-position-exit-layout-trials-20261004.md)
  records twenty isolated exit/profile compilations and twenty passing host
  shape/test runs. No full retail match; production's 71-word shared-RA tail,
  fifteen differences and aggregate snapshot remain unchanged.

- Game [Note 920](WORKING_NOTES/920-game-linked-record-position-stack-and-float-shape-20261004.md)
  restores linked-record position stack/float shape directly from C, reducing
  differences from 38 to 15. Thirteen tests pass; return-tail matching remains
  open. No guards, address drift or README aggregate change.

- Game [Note 919](WORKING_NOTES/919-game-linked-record-position-semantic-recovery-20261004.md)
  replaces the linked-record position placeholder with semantic C. Thirteen
  tests pass; 71-word body fits its 72-word slot, with 38 differing positions,
  no guards and no address drift. Matching/conversion totals remain unchanged.

- Init [Note 918](WORKING_NOTES/918-init-bitmap-store-qualifier-and-sentinel-trials-20261004.md)
  rejects store-qualifier and end-plus-one sentinel bitmap forms across three
  compiler profiles. Nine shapes pass 711 host combinations; 33 retained
  contract tests pass. No production conversion or README aggregate change.

- Game [Note 917](WORKING_NOTES/917-game-random-range-position-recovery-and-match-20261004.md)
  recovers the random range position routine as a direct 37-word C match.
  Four new tests cover unsigned selection, call/data timing and overlapping
  output; fourteen combined checks pass. Game 2601 / total 3274 exact;
  README aggregate rows refreshed, Init conversion/adoption gates unchanged.

- Game/Init [Note 916](WORKING_NOTES/916-game-object-position-sound-adapter-and-init-return-contract-20261004.md)
  recovers the 37-word nullable object-position sound adapter and corrects
  its Init callee's u16 return contract without changing that 29-word slot.
  Thirteen tests pass; full Init sections exact, Game 2600 / total 3273 exact.

- Game [Note 915](WORKING_NOTES/915-game-status-record-reset-recovery-and-match-20261004.md)
  finishes `func_151E5034` as a direct 37-word C match without guards. Nine
  focused tests and fresh production ELF/progress refresh pass. Game 2599 exact,
  total 3272 exact, zero drift; README aggregate snapshot updated only.

- Init [Note 914](WORKING_NOTES/914-init-rejected-dynamic-symbol-and-header-gate-fitting-20261004.md)
  rejects dynamic symbol ordering and encoded header gate trials: no complete
  saving / O2 bound +40, and O2 text +16 respectively. Source restored exactly;
  fifteen focused checks pass. Qualified 4512-byte candidate remains unchanged.

- Init [Note 913](WORKING_NOTES/913-init-distance-operation-o2-full-masked-cu1-set-corpus-20261004.md)
  qualifies all 507 distance-operation packed O2 masked CU1-set pages in
  818.478 seconds, no skips. With Note 912: 1014 paired runs, fixed text
  4512 / descent 3248 / margin 80 and hashes. Fitting and ownership remain open.

- Init [Note 912](WORKING_NOTES/912-init-distance-operation-o2-full-masked-cu1-clear-corpus-20261004.md)
  qualifies all 507 distance-operation packed O2 masked CU1-clear pages in
  826.726 seconds, no skips. Text 4512, descent 3248, margin 80 and source
  hashes hold; 22 supporting checks pass. CU1-set and production gates open.

- Init [Note 911](WORKING_NOTES/911-init-distance-operation-local-fitting-20261004.md)
  retains opt-in distance operation local: packed O2 4512 linked, sixteen
  bytes saved, 528 excess, unchanged stack bound. Bounded qualification and
  separate backreference storage guard pass; defaults identical. Changed full
  corpora, fitting and production ownership remain open; README unchanged.

- Init [Note 910](WORKING_NOTES/910-init-bitmap-shared-fill-mask-lifetime-trials-20261004.md)
  rejects two shared fill/mask lifetime trials: twenty/twenty-two O2 words
  versus nineteen retail. All seven host shapes pass 553 fixture combinations,
  and 33 retained-contract checks pass. Production conversion remains open.

- Init [Note 909](WORKING_NOTES/909-init-resume-conversion-readiness-audit-20261004.md)
  verifies all 47 remaining assembly source owners, records 38 passing focused
  checks and updates the conversion work list. Bitmap/MMIO matches and decoder
  fitting/ownership remain open. Production and README aggregates unchanged.

- Init [Note 908](WORKING_NOTES/908-init-startup-thread-stack-top-and-constructor-contract-20261004.md)
  pins executed startup thread arguments and constructor publications/write
  extent. Constructor +0x130 is not later context +0x230; original neighbor
  fence retained. Twenty-five combined checks pass, including crossing-store
  negative controls. No reservation manifest or production change claimed.

- Init [Note 907](WORKING_NOTES/907-init-rejected-builder-replication-span-deficit-trials-20261004.md)
  rejects entry/byte-unit replication deficits: O2 text +32 / bound +16,
  O1 also larger. Source restored exactly; seventeen retained-builder/size/
  accounting checks pass. Qualified decoder and production unchanged.

- Init [Note 906](WORKING_NOTES/906-init-dynamic-order-o2-full-masked-cu1-set-corpus-20261004.md)
  qualifies all 507 dynamic-order packed O2 masked CU1-set pages in 836.723
  seconds, no skips. With Note 905: 1,014 paired pages across both modes;
  unchanged text 4,528, descent 3,248 and margin 80. Production gates open.

- Init [Note 905](WORKING_NOTES/905-init-dynamic-order-o2-full-masked-cu1-clear-corpus-20261004.md)
  qualifies all 507 dynamic-order packed O2 masked CU1-clear pages in 835.460
  seconds, no skips. Text 4,528, descent 3,248, known-neighbor margin 80;
  hashes fixed. Matching CU1-set and production gates remain open.

- Init [Note 904](WORKING_NOTES/904-init-dynamic-order-cursor-text-stack-tradeoff-20261004.md)
  retains opt-in order-table cursor/countdown: packed O2 text 4,528, saving
  32 with eight more stack bytes; O1 text grows sixteen. Forty-five bounded
  passes / one corpus skip, all-count prefix and alignment checks pass.
  Defaults exact; changed-candidate full corpus and production gates open.

- Init [Note 903](WORKING_NOTES/903-init-bitmap-return-value-lifetime-trials-20261004.md)
  rejects cursor-return and endpoint-return matching hypotheses: both O2
  bodies grow to 21 words, retaining XOR comparison. Reproducible host behavior
  and return checks pass; 33 retained-contract tests pass. No production change.

- Init [Note 902](WORKING_NOTES/902-init-pointer-owned-o2-full-masked-cu1-set-corpus-20261004.md)
  qualifies all 507 combined packed O2 masked CU1-set pages in 823.148
  seconds, no skips. With Note 901: 1,014 paired pages across both modes,
  unchanged text 4,560, descent 3,240 and margin 88. Fitting and production open.

- Init [Note 901](WORKING_NOTES/901-init-pointer-owned-o2-full-masked-cu1-clear-corpus-20261004.md)
  qualifies all 507 combined-candidate packed O2 masked CU1-clear pages in
  819.113 seconds, no skips. Text 4,560, descent 3,240, known-neighbor margin
  88; source hashes fixed. Matching CU1-set and production gates remain open.

- Init [Note 900](WORKING_NOTES/900-init-pointer-owned-tight-adapter-fitting-20261004.md)
  retains paired guest pointer ownership and 176-byte tight adapter: packed
  executable text 4,560 / 5,968, unchanged bounds, sixteen-byte isolated O2
  text-plus-rodata span saving. Corrected bounded run 44 passes / one corpus
  skip with executed stale-read controls; defaults exact, full corpus open.

- Init [Note 899](WORKING_NOTES/899-init-tight-adapter-return-scheduling-and-alignment-20261004.md)
  retains opt-in 184-byte adapter: RA in branch delay, combined SP restore,
  word-aligned subsection. Executable text saves eight, but rodata gap prevents
  a whole footprint claim. Forty-one bounded passes / one corpus skip and
  separate dependency pass; default text and FPR order retained, full corpus open.

- Init [Note 898](WORKING_NOTES/898-init-global-mask-and-explicit-abi-copy-trials-20261004.md)
  rejects global low-mask and explicit ABI-copy forms: no fitting improvement.
  Exact source restored; sixteen focused checks pass. Production/defaults,
  qualified candidate and README unchanged.

- Init [Note 897](WORKING_NOTES/897-init-core-return-control-flow-trials-20261004.md)
  rejects two core return shapes: success-first neutral, shared-result increases
  O2 text and both bounds. Exact qualified source restored; ten focused tests
  pass. Production/defaults and README unchanged.

- Init [Note 896](WORKING_NOTES/896-init-fixed-length-cursor-endpoint-trials-20261004.md)
  rejects three fixed-length endpoint forms: whole O2 text neutral, O1 grows
  sixteen bytes. Exact source restored; nine ledger/size/initializer checks
  pass. Qualified candidate, production and README unchanged.

- Init [Note 895](WORKING_NOTES/895-init-builder-wide-operation-and-header-packing-trials-20261004.md)
  rejects wider operation and combined-header packing: no whole-text savings,
  eight-byte call-bound growth in both profiles. Exact qualified source restored;
  twenty focused tests pass. Production/defaults and README unchanged.

- Init [Note 894](WORKING_NOTES/894-init-scan-deficit-o1-full-masked-cu1-set-corpus-20261004.md)
  qualifies all 507 scan-deficit packed O1 CU1-set pages, no skips. Together
  Notes 893/894: 1,014 paired pages across both modes. Both O1 gates checked
  off; text 5,984, descent 3,200 / margin 128. Twenty-six supporting passes
  and unchanged hashes; changed-option O2 and production gates remain open.

- Init [Note 893](WORKING_NOTES/893-init-scan-deficit-o1-full-masked-cu1-clear-corpus-20261004.md)
  qualifies all 507 guarded scan-deficit packed O1 CU1-clear pages, no skips.
  Text 5,984, descent 3,200 equals bound, minimum SP 0x80031D90 / margin 128.
  Twenty-six supporting passes and six unchanged hashes; matching CU1-set and
  production ownership/hardware remain open. Production/README unchanged.

- Init [Note 892](WORKING_NOTES/892-init-builder-inplace-scan-deficit-fitting-20261004.md)
  retains opt-in bounded in-place scan deficit: O1 core saves 32 bytes,
  packed frames/bounds unchanged, O2 text neutral. Thirty-nine whole bounded
  passes / one corpus skip and separate six-image branch gate pass. Default
  packed text preserved exactly; changed-option full corpora remain open.

- Init [Note 891](WORKING_NOTES/891-init-mask-before-refill-lifetime-trials-20261004.md)
  rejects pure-mask-before-refill lifetime changes in take-bits and lookup:
  both grow complete text in both profiles, bounds unchanged. Exact source
  restored and fifteen focused checks pass; production/README unchanged.

- Init [Note 890](WORKING_NOTES/890-init-builder-sort-offset-local-trials-20261004.md)
  rejects local sort offsets in both store orders: no whole O2 text saving,
  eight-byte call-bound growth in both profiles. Exact source restoration and
  seventeen semantic/ledger passes; production and README unchanged.

- Init [Note 889](WORKING_NOTES/889-init-current-assembly-conversion-decision-20261004.md)
  refreshes the remaining-assembly conversion decision: 47 rows / 12,252 bytes,
  two small matching candidates, connected decoder still 592 linked bytes over.
  Thirty-three focused tests pass with no skips; no production conversion.
  Frame/adapter recovery is completed experimental work, not a new first step.

- Init [Note 888](WORKING_NOTES/888-init-live-sp-guard-full-masked-cu1-set-corpus-20261004.md)
  qualifies all 507 live-SP-guarded packed O2/g3 masked CU1-set pages in
  804.839 seconds, no skips. With Note 887: 1,014 paired pages across both
  guarded modes. Text 4,576 / 592 excess, descent 3,240 equals bound, minimum
  SP 0x80031D68 / neighbor margin 88. Twenty-six supporting checks pass, nine
  hashes hold. Both corpus gates checked off; fitting/reservation/ownership/
  hardware remain open. Production and README unchanged.

- Init [Note 887](WORKING_NOTES/887-init-live-sp-guard-full-masked-cu1-clear-corpus-20261004.md)
  qualifies all 507 live-SP-guarded packed O2/g3 masked CU1-clear pages in
  806.976 seconds, no skips. Text 4,576 / 592 excess, descent 3,240 equals
  bound, minimum SP 0x80031D68 / neighbor margin 88. Twenty-six supporting
  checks pass; nine source blobs hold. Matching guarded CU1-set and fitting/
  reservation/hardware/ownership remain; production and README unchanged.

- Init [Note 886](WORKING_NOTES/886-init-live-sp-write-fence-and-negative-qualification-20261004.md)
  adds a live-SP write-only oracle fence with executed below-frame negative
  controls. Thirty-seven bounded tests pass / one corpus skip; thirteen
  storage tests pass. Candidate size/bounds hold; full guarded corpus and
  reservation remain open. Production/defaults/README unchanged.

- Init [Note 885](WORKING_NOTES/885-init-mmio-published-address-dataflow-trial-20261004.md)
  probes the published address as MMIO destination in five profiles. O1
  retains the address but still differs; no matching replacement or guard
  batch. Ten bounded store traces and three assembly checks pass. Production
  ownership, profiles, decoder qualification and README unchanged.

- Init [Note 884](WORKING_NOTES/884-init-builder-descending-count-clear-trials-20261004.md)
  rejects descending count-clear forms: no aggregate O2 saving, O1 growth,
  and a stack penalty for post-decrement. Source restored exactly; thirteen
  focused retained gates pass. Production/defaults/README unchanged.

- Init [Note 883](WORKING_NOTES/883-init-stored-output-cursor-and-countdown-trials-20261004.md)
  rejects stored output-pointer and countdown forms: both add sixteen core
  text bytes in each profile and increase stored-frame costs. Source restored
  exactly; thirteen focused retained tests pass, including bad-complement
  state. No production/default/README change or trial semantic acceptance.

- Init [Note 882](WORKING_NOTES/882-init-core-limit-predicate-and-local-lifetime-trials-20261004.md)
  measures and rejects unsigned workspace-limit and local-limit forms: raw
  word savings disappear into padding; the local form increases O1 stack
  bound eight bytes. Qualified source restored exactly, twelve focused
  retained gates pass. No production/default/README changes.

- Init [Note 881](WORKING_NOTES/881-init-direct-fpr-adapter-full-masked-cu1-set-corpus-20261004.md)
  qualifies all 507 direct-load packed O2/g3 masked CU1-set pages in
  790.940 seconds, no skips. With Note 880: 1,014 paired pages across both
  masked modes. Text 4,576 / 592 excess, descent 3,240 equals bound, minimum
  SP 0x80031D68 / neighbor margin 88. Eleven supporting gates pass; eight
  source blobs unchanged. Both corpus gates checked off; production and
  README unchanged, fitting/ownership/hardware/reservation remain open.

- Init [Note 880](WORKING_NOTES/880-init-direct-fpr-adapter-full-masked-cu1-clear-corpus-20261004.md)
  qualifies all 507 direct-load packed O2/g3 masked CU1-clear pages in
  808.272 seconds, no skips. Text 4,576 / 592 excess, depth 3,240 equals
  bound, minimum SP 0x80031D68 / neighbor margin 88. Eleven supporting
  gates pass, eight source blobs unchanged. Matching CU1-set and fitting/
  ownership/hardware/reservation remain; production and README unchanged.

- Init [Note 879](WORKING_NOTES/879-init-direct-fpr-load-adapter-fitting-20261004.md)
  adds opt-in direct FPR loads: adapter 192 bytes, packed O2/g3 linked 4,576,
  592 over retail, saving 64 bytes. Shared transfer model gains separate
  word-load receipts; default assembled text remains byte-identical.
  New-option corpus and fitting/ownership/hardware gates remain open.
  Fresh bounded suite: 36 passed / one corpus skip; eleven shared/default
  regressions pass, with observed stack descent matching all six bounds.

- Init [Note 878](WORKING_NOTES/878-init-callee-adapter-full-masked-cu1-set-corpus-20261004.md)
  qualifies all 507 current packed O2/g3 pages with masked CU1 set in 792.002
  seconds, no skips. With Note 877: 1,014 paired pages across both masked
  modes, unchanged source, callee-return guard on every page. Text 4,640 /
  656 excess; descent 3,240 / neighbor margin 88. Sixteen supporting gates
  pass; corpus gates checked off, promotion gates remain. No README totals change.

- Init [Note 877](WORKING_NOTES/877-init-callee-adapter-full-masked-cu1-clear-corpus-20261004.md)
  qualifies all 507 current first-refill/callee-adapter packed O2/g3 pages
  with masked CU1 clear in 839.425 seconds, no skips. Callee-return guard
  checks every page; text 4,640 / 656 excess, descent 3,240 / margin 88.
  Sixteen supporting gates pass, source blobs unchanged. Note 875 CU1-clear
  gate checked off; current CU1-set and promotion gates remain open.

- Init [Note 876](WORKING_NOTES/876-init-unretained-pointer-argument-ownership-trials-20261004.md)
  records three unretained pointer/address ownership trials and corresponding
  two-store adapter omission: no linked saving, O1 workspace-only grows.
  Core/adapter restored exactly, fifteen focused gates pass. Retained O2
  remains 4,640 / 656 excess, current changed corpus and promotion gates open.

- Init [Note 875](WORKING_NOTES/875-init-callee-preserving-core-adapter-fitting-20261004.md)
  banks opt-in callee-preserving adapter: ten reloads removed, frame stores
  retained, all six shapes save 48 linked bytes. Packed O2 4,640 / 656 excess.
  Whole bounded suite 34 passes / one corpus skip; sixteen supporting gates
  and a strengthened executed-clobber negative gate pass. Initial failed
  probe assumption and correction documented; omitted-option text unchanged.
  Full changed corpus and production-promotion gates remain open.

- Init [Note 874](WORKING_NOTES/874-init-lookup-exit-shape-and-offset-predicate-trials-20261004.md)
  records two unretained lookup exit forms: helper word savings are absorbed
  by padding, full text/bounds hold. Exact source restoration, fifteen focused
  gates and 256-byte host classification probe pass. No production count change.

- Init [Note 873](WORKING_NOTES/873-init-explicit-first-refill-lookup-fitting-20261004.md)
  banks opt-in initial-refill shared lookup: packed O2/O1 core saves sixteen
  bytes, linked O2 4,688 / 704 excess. All shape bounds hold, observed descents
  match. Final guest run 33 passes / one corpus skip plus sixteen supporting
  passes; omitted-option text equals qualified baseline. Changed corpus and
  production-promotion gates remain open; no README total change.

- Init [Note 872](WORKING_NOTES/872-init-allocation-table-full-masked-cu1-set-corpus-20261004.md)
  qualifies all 507 current packed O2/g3 pages with masked CU1 set in 804.532
  seconds, no skips. Together with Note 871: 1,014 paired pages on unchanged
  current source across both masked modes. Text 4,704 / 720 excess; descent
  3,240 and neighbor margin 88 unchanged. Fifteen supporting gates pass;
  corpus gates checked off in Notes 867/871, fitting/ownership/hardware remain.
  No production conversion, README total change or unrelated Game staging.

- Init [Note 871](WORKING_NOTES/871-init-allocation-table-full-masked-cu1-clear-corpus-20261004.md)
  qualifies all 507 current toggle/parent-cursor/allocation-table packed O2/g3
  pages with exception-masked CU1 clear: 798.099 seconds, no skips. Text
  4,704 / 720 excess; descent 3,240 matches bound, known-neighbor margin 88.
  Fifteen helper/selection gates pass. Note 867 CU1-clear gate checked off;
  current CU1-set and production-promotion gates remain open. No README totals
  change or unrelated Game staging.

### 2026-10-03 resume checkpoint

- Init [Note 870](WORKING_NOTES/870-init-rejected-stride-only-replication-capture-20261003.md)
  rejects two stride-only indexed replication forms (+8 stack bytes both
  profiles) and restores the source. Fresh retained-config guest suite:
  32 passes / one intentional corpus skip, 260.739 seconds; all six observed
  descents match static bounds. No production or README total change.

- Init [Note 869](WORKING_NOTES/869-init-rejected-take-bits-mask-and-drop-inlining-20261003.md)
  closes the two remaining narrow mask/drop inlining subsets: neither improves
  both compiler profiles or the core call bound. Source restored exactly;
  fourteen focused gates pass. No new option or production count change.

- Init [Note 868](WORKING_NOTES/868-init-rejected-take-bits-drop-inlining-20261003.md)
  records rejected drop-only helper inlining (+16 O2 / +32 O1 core bytes,
  no call-bound improvement), exact source restoration and fourteen passing
  focused gates. Fresh inventory remains 47 assembly rows / 12,252 bytes.
  No production conversion, README total change or unrelated Game staging.

- Init [Note 867](WORKING_NOTES/867-init-builder-table-derived-allocation-fitting-20261003.md)
  banks opt-in table-derived allocation. Packed O2 saves 16 linked bytes
  to 4,704 / 720 excess, with all six stack bounds unchanged. Ordered
  allocation gate now observes actual retail s3 updates at 0x10006C38;
  the original once-at-return FPR19 assumption/failure is recorded.
  Corrected gate and omitted-option text checks pass; fresh whole run has
  32 passes / one corpus skip, plus fourteen helper passes, observed
  descents matching bounds. Production/defaults/README totals unchanged, unrelated
  Game work preserved and excluded; changed corpus and fitting remain open.

- Init [Note 866](WORKING_NOTES/866-init-parent-ascent-offset-cursor-fitting-20261003.md)
  banks opt-in parent-offset cursor fitting. Packed O2 linked text falls
  to 4,720 / 736 excess with unchanged stack bounds; packed O1 holds.
  Mixed other-profile costs and two rejected mask-reuse trials are measured.
  Active root-descent/short-tree guard and omitted-option text checks pass;
  31 guest tests pass, one corpus skip, plus fifteen focused passes; all
  observed descents match bounds. Defaults/production/README totals
  unchanged; changed corpus and fitting/ownership/hardware stay open.
  Unrelated Game work is preserved and excluded.

- Init [Note 865](WORKING_NOTES/865-init-toggle-cache-interactions-and-rejected-sort-cursors-20261003.md)
  banks changed-base cache/parent/sorted-array matrices and two rejected
  sorted-length cursor trials: 44 fresh object receipts, no improving
  text/bound metric. Exact source restored; sixteen focused gates pass,
  no skips. Packed O2 stays 4,736 / 752 excess. Move structural fitting
  to allocation/parent ascent or shared calls; no surviving source/default/
  README total change. Unrelated Game work preserved and excluded.

- Init [Note 864](WORKING_NOTES/864-init-builder-reversed-code-toggle-first-loop-20261003.md)
  banks opt-in reversed-code toggle-first fitting. Packed O2 public body
  saves three words but aligned total holds at 4,736 / 752 excess; packed
  O1 and aligned profiles save 16 bytes, frame O1 32. Stack bounds hold.
  Exhaustive host code/mask pairs and omitted-option text comparisons pass;
  final checks are 44 pass / one corpus skip, observed descents matching
  static bounds. Current-option corpus
  remains separate from Notes 862/863. Production/defaults/README totals
  unchanged; unrelated Game work preserved and excluded.

- Init [Note 863](WORKING_NOTES/863-init-offset-sum-full-masked-cu1-set-corpus-20261003.md)
  banks all 507 revised-combination packed O2/g3 retail pages with masked
  CU1 set in 814.477 seconds. Both masked modes now cover 1,014 paired
  pages for unchanged source; text/descent/clearance stay 4,736/3,240/88.
  Sixteen corpus/helper checks pass, no skips; completed current-source
  corpus checklist items are checked off. Return to fitting (752 bytes);
  other-profile/ownership/hardware remain open. No production/default/README
  total edits; unrelated Game work preserved and excluded.

- Init [Note 862](WORKING_NOTES/862-init-offset-sum-full-masked-cu1-clear-corpus-20261003.md)
  banks all 507 revised-combination packed O2/g3 retail-page comparisons
  with exception-masked CU1 clear in 790.137 seconds. Text/descent/clearance
  stay 4,736/3,240/88; sixteen corpus/helper checks pass with no skips.
  CU1 set is the next separate qualification gate. Fitting, other profiles
  and ownership/hardware remain open; no source/default/README total edits.
  Unrelated Game work is preserved and excluded.

- Init [Note 861](WORKING_NOTES/861-init-builder-offset-accumulator-lifetime-stack-recovery-20261003.md)
  removes the opt-in prefix sum's stack penalty by reusing `available`.
  Linked text stays 4,736 / 752 excess; packed call bound/builder frame
  return to 392/200 and known-neighbor clearance to 88. Aligned O2/O1
  also recover eight bound bytes. Fresh checks pass: 43 tests, one corpus
  skip, all observed descents match bounds and omitted-option text bytes hold;
  full revised corpus, further fitting and ownership/hardware remain open.
  Defaults/production/README totals unchanged; unrelated Game edits excluded.

- Init [Note 860](WORKING_NOTES/860-init-builder-running-offset-sum-text-stack-tradeoff-20261003.md)
  banks an opt-in running prefix sum and two rejected pointer-loop trials.
  Packed O2 saves 16 linked bytes to 4,736 / 752 excess, at an eight-byte
  larger call bound; known-neighbor clearance is 80. Original defaults and
  the 4,752-byte baseline remain available. Ordered prefix stores pass;
  43 final checks pass, one intentional corpus skip. Observed six-shape
  descent matches static bounds. Full changed corpus,
  fitting and ownership/hardware gates remain open; Game work excluded.

- Init [Note 859](WORKING_NOTES/859-init-rejected-match-copy-refill-trials-and-size-ledger-20261003.md)
  banks four rejected copy/refill trials, exact experiment-source restoration
  and fresh size-ledger evidence. Best text stays 4,752, 768 over retail;
  fifteen focused checks pass. Next target is builder/shared-call overhead,
  not these inferior loops. No surviving source/default/README total edits;
  unrelated Game work remains preserved and excluded.

- Init [Note 858](WORKING_NOTES/858-init-dynamic-repeat-value-selection-and-cursor-end-fill-20261003.md)
  banks repeat-value/cursor-end fitting with ordered nonzero/minimum/maximum
  fills and inherited overflow gates. Best bounded O2 falls to 4,752, still
  768 over retail; stack costs hold. Prior two-mode full corpus remains
  scoped to the no-new-option build. Fresh changed corpus and fitting stay
  open. Production/adapter/defaults/README totals unchanged; Game work excluded.

- Init [Note 857](WORKING_NOTES/857-init-simple-seed-full-masked-cu1-set-corpus-20261003.md)
  banks all 507 fresh current-combination masked-CU1-set comparisons.
  Notes 856/857 complete both masked modes for packed O2/g3: 1,014 paired
  runs, unchanged text/descent/clearance 4,768/3,240/88. Related corpus
  checklist items are checked off; return to fitting with 784 bytes left.
  Other-profile/ownership/hardware remain open. No source/default/README
  total edits; unrelated Game work remains preserved and excluded.

- Init [Note 856](WORKING_NOTES/856-init-simple-seed-full-masked-cu1-clear-corpus-20261003.md)
  banks all 507 fresh current-combination masked-CU1-clear corpus comparisons.
  Text/descent/clearance remain 4,768/3,240/88; full context and poisoned-state
  checks pass. Changed CU1-set corpus remains open, then further fitting;
  best text is still 784 over retail. No source/default/README total edits;
  unrelated Game work remains preserved and excluded.

- Init [Note 855](WORKING_NOTES/855-init-cache-interaction-matrix-and-simple-seed-combination-20261003.md)
  banks a freshly qualified existing-option combination after 32-way fitting.
  Best O2 linked text falls to 4,768, 784 over retail, with unchanged stack
  bounds. Explicit literal/EOB/stale-word and bounded/helper/default checks
  pass. Changed corpus and fitting remain open. Production/source bodies/
  adapter/defaults/README totals unchanged; unrelated Game work excluded.

- Init [Note 854](WORKING_NOTES/854-init-abi-seed-pointer-cursor-and-ordered-register-copy-20261003.md)
  banks opt-in ABI seed fitting with six ordered register-word reads/writes.
  Frame O2 saves 64 linked bytes; aligned/packed O2 save eight stack bytes.
  O1 growth is explicit. Best text stays 4,784, still 800 over retail;
  bounded/helper/default checks pass. Changed corpus and fitting remain open.
  Production/adapter/defaults/README totals unchanged; Game work excluded.

- Init [Note 853](WORKING_NOTES/853-init-core-owned-state-initialization-and-adapter-fitting-20261003.md)
  banks opt-in adapter state ownership with poisoned read-before-write
  qualification. All six links save 16; best packed O2 is 4,784, still
  800 over retail. Stack bounds hold and default adapter object is unchanged.
  Final bounded/helper/default checks pass; changed corpus and structural
  fitting remain open. Production/defaults/README totals unchanged; unrelated
  Game work remains preserved and excluded.

- Init [Note 852](WORKING_NOTES/852-init-dynamic-shared-repeat-extraction-and-stack-fitting-20261003.md)
  banks shared dynamic repeat extraction with active code/overflow gates.
  O2 saves eight stack bytes; O1 grows eight. Best packed text stays 4,800,
  816 over retail; bounded/helper checks pass. Changed corpus and structural
  fitting remain open. Production/defaults/README totals unchanged; unrelated
  Game work remains preserved and excluded.

- Init [Note 851](WORKING_NOTES/851-init-stored-shared-length-extraction-and-failure-bit-state-20261003.md)
  banks smaller alternate-profile stored extraction with retail failure bit
  state and an active delay-slot-aware restoration gate. Final bounded/helper
  tests pass; best packed O2 remains 4,800, 816 over retail. Changed corpus
  and structural fitting stay open. No production/default/README total edits;
  unrelated Game work remains preserved and excluded.

- Init [Note 850](WORKING_NOTES/850-init-byte-packed-header-load-and-unaligned-core-qualification-20261003.md)
  banks byte-packed header fitting with actual unaligned loads, alignment
  metadata rejection and all-offset/header-format qualification. Best linked
  text is 4,800, still 816 over retail; stack bounds remain unchanged.
  Changed corpus remains open. No production/default/README aggregate edits;
  unrelated Game work preserved and excluded.

- Init [Note 849](WORKING_NOTES/849-init-stream-masked-dispatch-and-buffered-byte-rewind-fitting-20261003.md)
  banks combined stream fitting with a proven active rewind gate. Best linked
  text is 4,832, still 848 over retail; bounded/initializer checks pass and
  stack bounds hold. Changed full corpus remains open. No production/default/
  README aggregate edits; unrelated Game work preserved and excluded.

- Init [Note 848](WORKING_NOTES/848-init-fixed-length-pointer-ranges-and-complete-table-qualification-20261003.md)
  banks smaller O2 fixed initialization with exact ordered-length/full-table
  checks and bounded contexts. Best linked text is 4,848, still 864 over
  retail; O1 growth is explicit. Changed full corpus remains open. No
  production/default/README aggregate changes; unrelated Game work excluded.

- Init [Note 847](WORKING_NOTES/847-init-builder-operation-selection-fitting-and-rejected-dataflow-trials-20261003.md)
  banks bounded arithmetic-operation fitting and rejected prefix/countdown
  receipts. Alternate profiles shrink; best packed O2 stays 4,864 after
  padding. No prior corpus receipt is reassigned to the new opt-in form.
  Production, defaults and README aggregates unchanged; Game work excluded.

- Init [Note 846](WORKING_NOTES/846-init-histogram-cursor-full-masked-cu1-clear-corpus-20261003.md)
  banks all 507 changed packed O2/g3 masked-CU1-clear comparisons, completing
  both masked CU1 corpus gates. Size/stack remain unchanged; next return to
  fitting with other-profile and hardware limits explicit. No production or
  README aggregate changes; unrelated Game work remains excluded.

- Init [Note 845](WORKING_NOTES/845-init-histogram-cursor-full-masked-cu1-set-corpus-20261003.md)
  banks the changed histogram variant's full 507-page masked-CU1-set pass
  in packed O2/g3. Size/stack receipt remains 4,864/3,256 with 72-byte
  neighbor clearance. CU1-clear and further fitting remain open; production
  and README aggregates are unchanged, with unrelated Game work preserved.

- Init [Note 844](WORKING_NOTES/844-init-builder-histogram-cursor-fitting-and-bounded-qualification-20261003.md)
  banks histogram-only decoder fitting: 16-byte packed reduction in both
  profiles, 4,864 linked bytes with 880 still to remove. Bounded stream and
  direct builder qualification passes; changed full corpus remains open.
  No production conversion or README aggregate changes; Game work preserved.

- Init [Note 843](WORKING_NOTES/843-init-debugger-entry-frame-and-seeded-resume-footer-20261003.md)
  qualifies retail debugger early exits and seeded footer return/EPC/state
  contracts, preserving bounded stack/register evidence. All 62 focused tests
  pass. UI/TLB predicates and actual resume remain unqualified; next fitting
  work retains those constraints. No production or README aggregate changes.

- Init [Note 842](WORKING_NOTES/842-init-post-diagnostic-page-state-cleanup-and-continuation-20261003.md)
  qualifies retail return-tail/table/bitmap CPU stores with instrumented
  hardware-facing calls. Fault/requeue continuation, unmap indices and cache
  operands are bounded receipts, not resumed gameplay proof. All 58 focused
  tests pass; no production, decoder/adapter, fitting or README totals edits.

- Init [Note 841](WORKING_NOTES/841-init-diagnostic-overlay-placement-and-positive-pool-bounds-20261003.md)
  qualifies diagnostic overlay/SP/DMA/TLB arguments and allocation extents
  for all positive direct counts. Zero/tiny pool arithmetic is explicitly
  outside that bound. All 54 focused tests pass; no hardware/runtime failure
  claim, production edits, decoder/adapter or README aggregate changes.

- Init [Note 840](WORKING_NOTES/840-init-retail-loaded-page-table-loop-write-footprint-20261003.md)
  qualifies the original loaded-pointer startup loop: 508 offsets, 2,032
  exact write bytes, untouched DMA tail/input guard. All 41 focused tests pass.
  DMA/cache, other writers and complete reservations remain open. No production,
  decoder/adapter, fitting or README aggregate changes.

- Init [Note 839](WORKING_NOTES/839-init-block-local-storage-writers-and-fr1-fixture-correction-20261003.md)
  adds optional block-local literal tracking and identifies 33 store candidates.
  Corrects the callback fixture to FR=1 independent FPR high/low words and
  requalifies both profiles. All 34 focused tests pass. No production, decoder/
  adapter or README totals changes; full ownership and fitting stay open.

- Init [Note 838](WORKING_NOTES/838-init-static-storage-literal-census-and-enclosing-bss-clear-20261003.md)
  adds a retail literal-pair census and pinned startup clear-argument test.
  The enclosing BSS clear does not prove individual reservations; scheduled-
  apart/computed writers remain outside the census. All 17 focused tests pass.
  No production, fitting, decoder/adapter or README aggregate changes.

- Init [Note 837](WORKING_NOTES/837-init-syscall-fault-dispatch-and-disabled-diagnostics-route-20261003.md)
  qualifies bounded retail syscall fault dispatch and the diagnostic-disabled,
  no-event-queue route to the scheduler boundary. Thread remains stopped/faulted;
  seeded EPC is not advanced. All 32 focused tests pass. Full entry/resume,
  enabled diagnostics and reservations remain open; no production or totals edits.

- Init [Note 836](WORKING_NOTES/836-init-retail-cleanup-callback-null-path-and-fatal-slot-20261003.md)
  replaces the callback-only stub assumption with executable retail null-path
  evidence alongside compiled Init sweep C in both profiles. The fatal slot
  is pinned as syscall plus NOPs. All 28 focused tests pass; async/exception/
  reservation ownership and fitting remain open. No production, README totals,
  decoder/adapter or pending Game edits.

- Init [Note 835](WORKING_NOTES/835-init-guest-tag-sweep-and-retag-lifetime-contract-20261003.md)
  qualifies recovered aging/full sweeps and retag C in both IDO guest profiles.
  Tag FF pool/bitmap storage survives both sweeps; selected adjacent blocks
  and free gaps preserve traversal. All 25 focused tests pass. Real Game
  callback effects, fatal/reservation ownership and fitting remain open.
  No production, README totals, decoder/adapter or pending Game edits.

- Init [Note 834](WORKING_NOTES/834-init-guest-free-reinsertion-and-resize-coalescing-20261003.md)
  qualifies actual C free/reinsertion/coalescing in fresh big-endian IDO guest
  builds. Both profiles reclaim the private heap across 512 resize cycles;
  adjacent live data/tags survive. All 22 focused tests pass. Production,
  README totals, decoder/adapter and pending Game work unchanged; tag-sweep,
  fatal/reservation ownership and fitting remain open.

- Init [Note 833](WORKING_NOTES/833-init-page-pool-retry-and-zero-count-fallback-contract-20261003.md)
  qualifies bounded setup retry paths and native zero-request allocation.
  Positive inputs alone do not exclude zero post-fallback geometry. All 26
  focused tests pass. No runtime failure claim or behavior fix; production,
  README totals, decoder/adapter and pending Game work unchanged.

- Init [Note 832](WORKING_NOTES/832-init-storage-boundaries-page-table-cache-and-output-pool-20261003.md)
  adds bounded original-word storage arithmetic tests. Table DMA ends at input;
  inclusive cache operands cross workspace without proving input capacity.
  Separate pool indexing passes; all ten focused tests pass. Full ownership
  and fitting remain open; production/README and pending Game work unchanged.

- Init [Note 831](WORKING_NOTES/831-init-explicit-corpus-cu1-modes-and-clear-full-pass-20261003.md)
  adds explicit corpus CU1 mode selection and passes all 507 masked CU1-clear
  pages on loop-lookup packed O2. Nine selector/mask tests pass; ordinary corpus
  discovery skips. Defaults and production unchanged; other profiles,
  ownership/fault bounds and the 896-byte text excess remain open.

- Init [Note 830](WORKING_NOTES/830-init-loop-lookup-full-masked-corpus-20261003.md)
  closes the full 507-page masked corpus gate for loop-lookup packed O2/g3,
  CU1 set, in 759.786 seconds. Text/descent is 4,880/3,256; neighbor margin
  72 bytes. Other profiles/mode, ownership/fault bounds and fitting stay open.
  Production, default profiles, README aggregates and Game work unchanged.

- Init [Note 829](WORKING_NOTES/829-init-shared-lookup-loop-fitting-and-context-qualification-20261003.md)
  retains an opt-in shared lookup loop: packed O2 saves 16 linked text bytes,
  with 420 bounded context comparisons and an explicit nested-path gate.
  Across two runs, 29 tests pass and one corpus skips. Default costs and
  production remain unchanged; full new-source corpus and fitting stay open.

- Init [Note 828](WORKING_NOTES/828-init-shadow-fitting-trials-and-helper-attribution-20261003.md)
  records five rejected size-only fitting hypotheses and separates actual
  builder code from embedded capture/lookup helpers. Temporary edits are
  removed; fresh restored compilation reproduces baseline text. No production
  conversion, new execution qualification or README aggregate changes.

- Init [Note 827](WORKING_NOTES/827-init-full-masked-shadow-corpus-20261003.md)
  passes all 507 pages in the explicit masked context, CU1 set, smallest shadow
  profile (709.832 seconds). Text/descent remains 4,896/3,256, neighbor margin
  72 bytes. Other full-corpus profiles/mode, ownership/fault bounds and fitting
  remain open; production, README aggregates and pending Game work unchanged.

- Init [Note 826](WORKING_NOTES/826-init-exception-entry-mask-and-masked-context-qualification-20261003.md)
  pins/executes the entry Status mask and qualifies 72 masked compiled context
  comparisons across six profiles/both CU1 modes. All 29 focused tests pass.
  Corpus context selection is explicit; full masked corpus and remaining
  ownership/fitting gates are open. Production code, README totals and Game
  work remain unchanged.

- Init [Note 825](WORKING_NOTES/825-init-context-neighbor-guard-and-first-shadow-corpus-20261003.md)
  recovers retail's 0x230 thread footprint beyond the SDK's 0x1B0 header.
  All 507 pages pass the smallest shadow profile with CU1 set and the corrected
  neighbor guard; stack margin is 72 bytes. All 23 focused tests pass. Other
  full-corpus profiles/mode, complete ownership and fitting remain open.
  Production ownership, shared headers, README totals and Game work unchanged.

- Init [Note 824](WORKING_NOTES/824-init-distance-builder-and-multiblock-fpr-history-20261003.md)
  qualifies distance-tree outcomes and multiblock FPR history with 144 more
  gated comparisons (348 shadow contexts total). All 19 focused tests pass,
  including pre-wrapper scratch-FPR checks. Actual code/stack costs and
  production ownership remain unchanged; Game work is preserved separately.

- Init [Note 823](WORKING_NOTES/823-init-semantic-scratch-fpr-publication-20261003.md)
  adds opt-in semantic scratch-FPR publication. All 204 new bounded context
  comparisons pass across six images and both CU1 paths. State/adapter costs
  are explicit; full shadow corpus, original storage ownership and fitting
  still gate production conversion. README totals and pending Game work unchanged.
  All 110 focused tests pass, including native all-retail-page semantic checks.

- Init [Note 822](WORKING_NOTES/822-init-fpr-provenance-and-failure-frame-corrections-20261003.md)
  recovers f1-f11 write provenance and corrects signed symbol classification
  plus an opt-in distance-root lifetime. All 103 focused tests pass. Expanded
  failure cases distinguish matching seeded context from unseeded frame gaps;
  complete CU1-set publication and production conversion remain unclaimed.

- Init [Note 821](WORKING_NOTES/821-init-original-core-call-adapter-and-exception-context-20261003.md)
  adds an isolated original-call adapter and retained-wrapper execution: 60
  CU1-clear context runs pass, six CU1-set probes retain an explicit f1-f11
  compatibility gap. All 95 focused tests pass. Code/stack costs are measured;
  production ownership, storage requirements and README totals are unchanged.

- Init [Note 820](WORKING_NOTES/820-init-all-retail-pages-through-compiled-guest-core-20261003.md)
  qualifies all 507 retail pages across six compiled core images: 3,042 core
  runs and fixed initializations pass. All 83 focused regressions and 18
  final-source representative core runs pass. Explicit buffer/read guards
  retain the original ABI/storage/hardware boundary; no production conversion.

- Init [Note 819](WORKING_NOTES/819-init-compiled-guest-stream-core-and-fixed-initializer-qualification-20261003.md)
  extends linked guest execution to fixed initialization and connected stored,
  fixed, dynamic and core paths. All 74 combined checks pass; tested state and
  partial-error behavior match retail. No production ownership/count change.

- Init [Note 818](WORKING_NOTES/818-init-compiled-guest-builder-differential-execution-20261003.md)
  adds actual linked IDO builder execution under a bounded MIPS model, not just
  native C or size receipts. Six images pass 186 retail comparisons; all 63
  combined checks pass. No production C ownership or aggregate change.

- Init [Note 817](WORKING_NOTES/817-init-builder-symbol-cursor-and-capacity-qualification-20261003.md)
  qualifies pointer-end and remaining-count symbol cursors with full-capacity
  tests. The smallest O2 candidate is 4,160 bytes, still 176 over retail,
  at a 376-byte call-frame bound. Production owners/counts remain unchanged.

- Init [Note 816](WORKING_NOTES/816-init-builder-leaf-fill-and-bounded-length-scan-trials-20261003.md)
  gains sixteen text bytes from bounded histogram scans without frame growth.
  Per-run leaf capture is negative. Generated receipts now separate public
  call units and embedded helpers; production assembly/counts are unchanged.

- Init [Note 815](WORKING_NOTES/815-init-decompressor-semantic-slot-ledger-correction-20261003.md)
  corrects swapped dynamic/compressed slot roles in Notes 812-813 and the
  fixed-wrapper label. Generated receipt accounting and retail-call tests
  identify the builder, not the dynamic decoder, as the main slot overrun.
  The total deficit remains 224 bytes; production assembly/counts unchanged.

- Init [Note 814](WORKING_NOTES/814-init-dynamic-code-lookup-capture-and-inline-mask-trials-20261003.md)
  measures full lookup capture, mask-only capture and inline-mask forms.
  All pass focused semantic tests, but none improves O2 size/stack. Direct-call
  receipts distinguish removed helper dependencies from text/frame savings.
  Cursor-only and the exact production baseline remain the comparison points.

- Init [Note 813](WORKING_NOTES/813-init-dynamic-length-base-and-pointer-cursor-trials-20261003.md)
  measures length-base capture and pointer-cursor variants. Cursor-only improves
  both O2 text and stack: 4,208 bytes / 368-byte bound in the smaller shape.
  Capture-plus-cursor gives no text benefit and increases stack. Physical frame
  and malformed/error tests remain separate from hardware ABI qualification.

- Init [Note 812](WORKING_NOTES/812-init-rolled-scratch-cache-and-local-allocation-trials-20261003.md)
  qualifies selected rolled scratch-cache combinations and measures a local
  allocation cursor. Best text is 4,224 bytes, 240 over retail; lower-stack lead
  remains uncached aligned. Local cursor gives no rolled win. The new individual
  slot ledger keeps aggregate fit separate from entry/ABI restoration.

- Init [Note 811](WORKING_NOTES/811-init-parent-byte-addressing-and-no-unroll-profile-20261003.md)
  rejects byte-parent lookup as a size improvement but establishes no-unroll as
  a strong fitting lead: 4,256-byte aligned/bounded O2 text, 384-byte core frame
  bound, 272 bytes over retail. Wrapped-label tests and guest profile receipts
  remain separate from hardware ABI qualification. Production remains exact.

- Init [Note 810](WORKING_NOTES/810-init-builder-workspace-base-capture-trial-20261003.md)
  measures a stable workspace-base capture. All 78 focused tests pass, but
  sixteen guest compiles reject it as a size/stack improvement. Static opcode
  receipts distinguish reduced state loads from increased stack traffic.
  Default text bytes and production owners stay unchanged.

- Init [Note 809](WORKING_NOTES/809-init-decompressor-combined-builder-qualification-20261003.md)
  qualifies aligned/packed entries combined with bounded builder shifts. Packing
  saves sixteen O2 text bytes but regresses frame-backed stack and O1 text;
  seventy focused tests and eight guest compiles pass. The retail/C builder
  instruction ledger directs the next size investigation; no production change.

- Init [Note 808](WORKING_NOTES/808-init-decompressor-entry-alignment-packing-and-bounded-shift-trials-20261003.md)
  adds entry alignment/packing and bounded builder-shift trials. The latter
  improves both guest text and direct-call frame bounds without fitting retail.
  Entry-layout/opcode receipts, sanitizer coverage and generated tree tests
  qualify the observed domain; no production conversion or README increase.

- Init [Note 807](WORKING_NOTES/807-init-decompressor-flat-bit-helper-and-builder-base-codegen-trials-20261003.md)
  adds isolated flat-bit-helper and two builder-base capture trials. Their
  measured text/stack tradeoffs do not fit retail or qualify a production
  adapter. Seventy-five variant test methods cover both scratch representations,
  including the shared all-retail-page C corpus;
  default candidate, production assembly and README aggregates remain unchanged.

- Init [Note 806](WORKING_NOTES/806-init-exception-storage-boundaries-and-all-retail-core-page-survey-20261003.md)
  adds a fresh guest thread-layout receipt, original context extent and
  page-table DMA checks, wrapper canaries, and all-507-page retained-core survey.
  Maximum workspace span is 3,564 bytes; SDK size is not retail context extent.
  No production owner, SDK header, linker or README aggregate change.

- Init [Note 805](WORKING_NOTES/805-init-exception-decoder-fr1-full-width-fpr-context-model-20261003.md)
  adds a connected full-width FPR model restricted to FR=1. It preserves both
  original CU1 paths and the unconditional f0 delay load, explicitly marks
  MTC1 upper halves unknown, and covers success/failure context restoration.
  No production conversion, README aggregate change or hardware acceptance.

- Init [Note 804](WORKING_NOTES/804-init-retail-page-dma-and-exception-core-address-qualification-20261003.md)
  adds original-ROM-identity-checked qualification of all 507 retail pages,
  maximum DMA separation, and three retained-core calls at exception addresses.
  All 98 Init tests pass; no production conversion or README aggregate change.

- Init [Note 803](WORKING_NOTES/803-init-decompressor-frame-backed-c-and-guest-call-frame-bounds-20261003.md)
  implements frame-backed experimental C with physical table addresses and
  root/staging aliases. Fourteen variant tests and all 95 Init tests pass;
  guest text remains overlong at 5,312/5,600 bytes. The driver measures
  conservative direct-call frame bounds including unnamed helpers. Production
  assembly/README aggregates stay unchanged; connected adapter/context and
  fitting code generation remain open.
  All 570 project tool tests and guest/tool/build/matcher checks pass;
  both complete Init sections remain independently retail-exact.
- Init [Note 802](WORKING_NOTES/802-init-decompressor-physical-frame-mapping-and-contract-tests-20261003.md)
  implements a physical frame view and nine scratch/ABI tests. All 76 Init
  tests pass; both guest profiles validate all frame offsets. Initializer
  aliases, pointer/index translation, return cells, bounded stack depth, and
  exception FPR-delay evidence are retained. Production assembly and aggregate
  coverage stay unchanged. All 551 project tool tests and tool/build/matcher
  checks pass; both complete Init sections remain independently retail-exact.
  Frame-backed C/adapter/context work remains next.
- Init [Note 801](WORKING_NOTES/801-init-post-pause-assembly-conversion-assessment-20261003.md)
  records the post-pause conversion decision: 492 C / 47 assembly rows,
  all 67 Init tests passing, 492/492 exact C functions, and both complete
  sections independently retail-exact. Small bitmap/MMIO matching gates and
  connected decompressor ABI/layout work are distinguished from retained
  SDK/hardware assembly. No Init owner or README aggregate changes; pending
  Game source/tests are preserved outside the assessment.
- Game Note 800 replaces `func_1507C22C`'s placeholder with its 25-record
  actor-step dispatcher and matches all 62 words using seven independent
  address-setup scheduling guards. Ten new tests, forty focused tests, and
  all 532 tool tests pass; final argument-form rerun/build/matcher checks pass.
  Both Init sections and neighboring matches are preserved. README updates
  only total/Game aggregate match rows. Connected updater/predicate recovery
  remains open; no gameplay or full-system acceptance is claimed.

- Init Note 799 tests volatile byte stores and saved-comparison/break loop
  scheduling in six isolated guest trials. None matches the nineteen-word
  bitmap slot; all 237 host shape/case combinations pass, including two alias
  fixtures per shape. No production Init or aggregate change is made.

- Init Note 798 completes two bounded guest compiler/layout trials for the
  isolated decompressor: 4,928/5,328 text bytes versus the retained 3,984-byte
  region and 2,668-byte explicit state. Neither profile is a matching owner
  replacement. Added oversubscribed-tree fixtures preserve model behavior;
  nine semantic tests, all 522 tool tests, and tool/build/matcher checks pass. Both whole Init
  sections remain independently exact. No conversion or README total change.

- Init Note 797 adds an isolated connected semantic C candidate and nine
  differential tests. All 67 focused Init tests, all 522 tool tests, and tool
  checks pass. Table,
  stream, output publication, header/limit, and error states match retained
  instruction-word oracles on covered inputs. Production remains assembly;
  no README aggregate increase or host-port build is made.

- Init connected-stream Note 796 adds eleven dynamic/multiblock/core-entry
  oracle tests. All 58 focused Init tests and all 513 tool tests pass; both header forms and unaligned
  inputs, repeats, cursor rewind, limits, and partial-output failures are
  characterized. Production Init remains assembly; next is isolated semantic
  C comparison before any owner replacement or aggregate increase.

- Init compressed-decoder Note 795 adds ten fixed-stream/error oracle tests.
  All 47 focused Init tests, all 502 tool tests, and tool checks pass; both complete linked Init
  sections remain retail-exact. Zlib valid-output comparisons and retail-model
  error/count/history boundaries are characterized. Production remains
  assembly; README aggregates and host-port artifacts are unchanged.

- Init table-builder Note 794 adds nine instruction-word/canonical-oracle tests.
  All 37 focused Init tests, all 492 tool tests, and tool checks pass. Fixed allocations explain
  root pointers 0x8003BE94/0x8003C858; incomplete-table statuses and a synthetic
  narrow-root model boundary are recorded. Production Init remains assembly;
  no README aggregate change or host-port build is made.

- Init remaining-assembly assessment and connected decompressor contract are
  recorded in Notes 792/793. Eight new stored-block/interface tests and all
  28 focused Init tests and all 483 tool tests pass; tool checks pass.
  Shared-frame/FPR ownership,
  strict stored-block limits, and ignored fixed-wrapper decoder status are
  characterized. No production Init conversion or README aggregate change.

- Game `func_1507C324` converts its nineteen-word retained assembly to semantic
  nested float copy/clamp C, remaining byte-exact through eight closed-FPR
  allocation guards. Fourteen new tests, thirty focused copy/clamp/dimension
  tests, and all 475 tool tests pass; full rebuild/project checks pass. Earlier
  Game regressions, dimension helper, restored spans, and Init sections are
  unchanged. C/exact-C counts rise by one; README updates only aggregate tables.
  [Note 791](WORKING_NOTES/791-game-nested-float-copy-clamp-conversion-and-match-20261003.md)

- Game `func_1507C3E0` recovers the empty dimension helper, preserving subtype
  mappings, state precedence, distinct radii, expansion/scaling order, and
  nullable ordered outputs. Sixteen focused tests and all 461 tool tests pass;
  build/project checks pass. It remains non-matching with no new guards or
  profiles. Adjacent exact routines, Game regressions, and Init sections are
  unchanged; no aggregate/README update is needed.
  [Note 790](WORKING_NOTES/790-game-actor-dimension-helper-semantic-recovery-20261003.md)

- Init allocator `func_10003C6C` corrects a duplicate header addition in its
  rear C allocation path. Six production-body host tests cover bitmap setup
  counts, heap ownership/bounds, all alignment classes, both directions, and
  exhaustion. The legacy guarded layout is refreshed; the allocator slot and
  both full Init sections independently remain retail-exact. Full rebuild and
  matcher, twenty focused Init tests, and all 445 tool tests pass; aggregate
  tables/README unchanged. This is a semantic fix,
  not a new assembly-to-C conversion or direct compiler match.
  [Note 789](WORKING_NOTES/789-init-bitmap-allocator-provenance-and-rear-bound-correction-20261003.md)

- Init bitmap contract audit adds eight instruction-word-driven tests and
  establishes positive inputs 107..362 for the only direct retail resize call.
  Fourteen focused Init tests, all 439 tool tests, and project tool checks pass.
  No C conversion,
  production guard, or README aggregate change; allocator provenance and a new
  compiler hypothesis remain open.
  [Note 788](WORKING_NOTES/788-init-bitmap-retail-caller-domain-and-edge-contract-20261003.md)

- Game `func_1510F800` now explicitly forwards its s32 context argument to the
  retained setter, preserving its direct eight-word retail match. Fifteen
  focused/integrated tests and all 431 tool tests pass; build/project checks
  pass. Previous exact slots, non-matching hashes, restored spans, and Init
  sections are unchanged. Aggregates and README remain unchanged because the
  wrapper was already byte-exact C. Dimension helper recovery remains open.
  [Note 787](WORKING_NOTES/787-game-context-forwarding-interface-recovery-20261003.md)

- Game `func_1504452C` is recovered as a three-vertex transform, correcting the
  prior dispatcher label. All 75 words match after twenty expected-word guards
  normalize proven closed register cycles and independent origin loads. Eleven
  focused tests and all 416 tool tests pass; full rebuild/project checks pass.
  Exact C increases to 3,269 total / 2,596 Game, with zero drift and 2,193
  different C rows. README changes only aggregate matcher tables.
  [Note 786](WORKING_NOTES/786-game-three-vertex-transform-recovery-and-match-20261003.md)

- Game `func_15044380` replaces its zero-return placeholder with the complete
  actor/context dispatcher. Fourteen focused tests and all 405 tool tests pass;
  build/project checks pass. Its 107-word body remains non-matching at twenty
  positions, with no new guards/profiles. Exact regression slots, prior hashes,
  restored spans, and Init sections are unchanged; aggregate tables and README
  remain unchanged. Dimension/context helper recovery and chain acceptance
  remain open.
  [Note 785](WORKING_NOTES/785-game-actor-context-dispatcher-semantic-recovery-20261003.md)

- Game `func_15044660` replaces a false zero-return C placeholder with the
  complete original 156-word / 624-byte actor-preparation assembly. Special
  actor types retain a stack-index read not initialized by the routine; no
  guessed ordinary-C value is introduced. Three assembly regression tests
  are added. Total C inventory is now 5,462 / 6,042, exact C remains 3,268,
  and zero drift remains. README aggregate tables reflect the reclassification.
  [Note 784](WORKING_NOTES/784-game-actor-preparation-restoration-and-stack-boundary-20261003.md)

- Game `func_15047700` replaces its empty body with the reflection look-at
  builder, retail degenerate-axis branches, and complete SDK direction/color
  output with preserved padding. Fourteen focused tests and all 388 tool tests
  pass; build/project checks pass. It remains non-matching at 245 differences
  across 288 words, with no new guards/profiles. Both matrix wrappers, earlier
  exact routines, restored spans, and both complete Init sections remain exact.
  Aggregates and README remain unchanged.
  [Note 783](WORKING_NOTES/783-game-reflection-look-at-matrix-semantic-recovery-20261003.md)

- Game `func_15047390` replaces its empty body with the complete SDK-grounded
  look-at matrix builder and retail-specific exact-zero normalization guards.
  It remains non-matching: 188 body words plus two padding nops, 171 differences,
  no new word guards/profiles. Twelve focused tests and all 374 tool tests pass;
  full build/project checks pass. The fixed-matrix wrapper, prior restored
  spans, and both Init sections remain exact. Aggregate tables and README
  stay unchanged because the empty body was already counted as C.
  [Note 781](WORKING_NOTES/781-game-look-at-matrix-semantic-recovery-20261003.md)

- Game `func_150472C0` converts retained assembly to the complete void descriptor/
  height-result builder and matches all 52 words directly. Reordering equivalent
  flag contributions removes the last two differences without new guards or
  profiles. Eight focused tests and all 362 tool tests pass; full build/project
  checks pass. Prior recovered spans and both Init sections remain unchanged.
  README adds one converted and exact row; actor-builder matching remains open.
  [Note 780](WORKING_NOTES/780-game-descriptor-height-result-builder-direct-match-20261003.md)

- Game `func_1504715C` replaces its zero-return placeholder with the complete
  void actor-to-height-result builder. It remains non-matching: 85 body words
  plus four padding nops in the 89-word slot, 76 differences, no new guards/
  profiles. Twelve focused tests and all 354 tool tests pass; full build/
  project checks pass. Prior recovered spans and both Init sections remain
  unchanged. Aggregate tables and README are unchanged, since the placeholder
  was already counted as C and the recovered routine is not byte-exact.
  [Note 779](WORKING_NOTES/779-game-actor-height-result-builder-semantic-recovery-20261003.md)

- Game `func_15046D00` replaces its zero-return placeholder with the complete
  outer highest-height combiner. All 161 words match directly without new
  guards/profiles. Twelve focused tests and all 342 tool tests pass; full
  build/project checks pass. Both Init sections and prior recovered spans
  remain unchanged. README changes only exact/different aggregates; converted
  totals remain fixed. Next establish `func_1504715C`'s actor/result contract.
  [Note 778](WORKING_NOTES/778-game-outer-highest-combiner-direct-match-20261003.md)

- Game `func_1504697C` replaces its zero-return placeholder with the complete
  highest entity/terrain combiner. All 161 words match directly without new
  guards/profiles. Twelve focused tests and all 330 tool tests pass; full
  build/project checks pass. Both Init sections and prior recovered spans
  remain unchanged. Terrain highest retains its prior non-matching hash.
  README changes only exact/different aggregates; converted totals stay fixed.
  [Note 777](WORKING_NOTES/777-game-entity-terrain-highest-combiner-direct-match-20261003.md)

- Game `func_150466F8` converts retained assembly to the complete entity/
  terrain lowest-height combiner. All 161 words match directly without new
  guards/profiles. Twelve focused tests and all 318 tool tests pass; full
  build/project checks pass. Prior neighbors/spans and both entire Init
  sections remain unchanged. README adds one converted and exact row;
  Game conversion rounds to 90.00%.
  [Note 776](WORKING_NOTES/776-game-entity-terrain-lowest-combiner-direct-match-20261003.md)

- Game `func_15046460` replaces its zero-return placeholder with the complete
  highest-height combiner and matches all 166 words directly. No new guards
  or profiles. Ten new tests and all 306 tool tests pass; full build/project
  checks pass. Both Init sections and recovered spans remain unchanged.
  README updates only exact/different aggregates; converted totals do not
  change because this was already counted as C.
  [Note 775](WORKING_NOTES/775-game-highest-height-combiner-direct-match-20261003.md)

- Game `func_150461D0` converts retained assembly to the complete lowest-height
  combiner and matches all 164 words directly, without new guards/profile.
  Ten new tests and all 296 tool tests pass; full build/project checks pass.
  Recovered neighbors and both entire Init sections remain unchanged. README
  aggregates add one converted and exact row. The Init reassessment still
  leaves its two small matching-C candidates deferred.
  [Note 774](WORKING_NOTES/774-game-lowest-height-combiner-direct-match-20261003.md)

- Game `func_15045D48` converts retained assembly ownership to the complete
  context-3 entity lowest-height query. The cached entity pointer and state
  `3` distinguish it from the previous context's late-reload variants. It
  remains non-matching: 144 body words plus one padding nop, 72 differences,
  no new guards. Fifteen new tests and all 286 tool tests pass; full build
  and project checks pass. README aggregates add one converted row only.
  [Note 773](WORKING_NOTES/773-game-context3-entity-lowest-height-query-recovery-20261003.md)

- Game `func_15045AE4` replaces its zero-return placeholder with the complete
  context-2 entity highest-height query, preserving state `2` and late
  entity-index/base reloads. Its 153-word slot contains 150 semantic body
  words and three padding nops, with 88 differences and no new guards.
  Fifteen new tests and all 271 tool tests pass; full code build and project
  checks pass. Aggregate tables, including README, remain unchanged.
  [Note 772](WORKING_NOTES/772-game-context2-entity-highest-height-query-recovery-20261003.md)

- Game `func_15045880` is now the complete semantic entity lowest-height
  query instead of retained assembly ownership. It remains non-matching:
  150 body words plus three padding nops, 88 word differences, no new guards.
  Fifteen new tests cover all flags, metadata, helper reloads, and alias-sensitive
  entity-index/base reloads. All 256 tool tests pass; full build and project
  checks pass. README aggregates add one converted row, not an exact match.
  [Note 771](WORKING_NOTES/771-game-entity-lowest-height-query-semantic-recovery-20261003.md)

- Game `func_150470B0` and `func_15046C00` convert from retained assembly
  to direct semantic C matches: 172 and 128 bytes. Eleven new tests cover
  both dispatch caller shapes and the reversed cached-height bounds. All 241
  tool tests pass; full code build and project checks pass. The corrected
  `func_1504530C` signature preserves its 120 exact bytes. README aggregates
  add two converted/exact rows; no new guards or compiler profiles.
  [Note 770](WORKING_NOTES/770-game-opposite-cached-height-query-and-dispatch-direct-match-20261003.md)

- Game `func_15045800` converts from retained assembly to C, and its cached
  query `func_15047004` replaces the zero-return placeholder. Both match
  directly: 128 and 172 bytes, no new guards or profile changes. Twelve new
  integrated behavior tests and all 230 tool tests pass. Corrected float/
  pointer signatures preserve both sibling dispatch wrappers' exact bytes.
  README aggregates add one converted row and two exact rows.
  [Note 769](WORKING_NOTES/769-game-cached-height-query-and-dispatch-direct-match-20261003.md)

- Rechecked the remaining Init assembly: 47 rows / 12,252 bytes, of which
  two small leaves remain plausible but unproven matching C candidates.
  Both complete Init sections remain exact; no Init production source changed.
  [Note 768](WORKING_NOTES/768-init-remaining-assembly-current-decision-20261003.md)

- Game `func_15045780` is converted from retained assembly to semantic C;
  all 128 bytes match directly without guards or profile changes. Five new
  behavior tests and all 218 tool tests pass. README aggregate tables reflect
  one additional converted/exact C row, not a new Init conversion.
  [Note 767](WORKING_NOTES/767-game-entity-height-wrapper-direct-match-20261003.md)

- The original `func_150A6568` producer, interior cleanup, and shared empty
  return replace their placeholders; all 520 bytes match retail. Both C
  helpers remain exact with explicit secondary-count pointer contracts.
  Five new tests cover assembly/link bytes and C forwarding. All 213 tool
  tests pass. Full build and
  project checks pass. README aggregates remove one false C row / 504 bytes.
  Natural wrapper qualification remains separate.
  [Note 766](WORKING_NOTES/766-game-entity-scan-producer-assembly-restoration-20261003.md)

- Game `func_15045F8C` replaces its placeholder with the entity-indexed
  highest-height query. Its 145-word slot contains 144 semantic body words
  and one padding nop, with 72 differences and no new guards. Twelve new
  tests cover metadata and alias-sensitive reloads. All 208 tool tests pass. Full build and project
  checks pass; matching aggregates and README tables remain unchanged.
  The upstream shared-register producer still needs restoration.
  [Note 765](WORKING_NOTES/765-game-entity-height-query-semantic-recovery-20261003.md)

- Game `func_1504554C` is recovered as the context-3 highest-height query.
  All 114 words match with fifteen strict compiler-layout guards; thirteen
  new tests and all 196 tool tests pass. Full build and project checks pass.
  Total exact C rows are 3,257 / 5,455 and Game 2,584 / 4,782, with zero
  drift and 2,198 different rows. README changes only aggregate matching rows.
  [Note 764](WORKING_NOTES/764-game-context3-highest-height-query-recovery-20261003.md)

- Game `func_15045384` is recovered as a lowest-height query and matches all
  114 retail words with fifteen strict compiler-layout guards. Thirteen new
  tests and all 183 tool tests pass; full build and project checks pass.
  Total exact C rows are 3,256 / 5,455 and Game 2,583 / 4,782, with zero
  drift and 2,199 different rows. README updates only aggregate matching
  tables and the snapshot date.
  [Note 763](WORKING_NOTES/763-game-lowest-height-query-recovery-20261003.md)

- Twenty new Init MMIO partial-volatility/profile experiments produce no
  matching conversion. Three original-assembly regression tests were added;
  all 170 tool tests pass. Production source and README aggregates remain
  unchanged by this experiment.
  [Note 762](WORKING_NOTES/762-init-mmio-partial-volatility-trials-20261003.md)

- The original collector/context assembly replaces 23 placeholders across six
  inventory groups; all 5,712 bytes match. All 167 tool tests pass. README
  aggregate coverage now excludes those false C rows.
  [Note 760](WORKING_NOTES/760-game-collector-context-assembly-restoration-20261003.md)
- Init still has 47 retained assembly rows and two deferred small-leaf
  candidates, neither with a proven matching C replacement. Both complete
  sections match retail. No Init conversion is claimed.
  [Note 761](WORKING_NOTES/761-init-resume-conversion-decision-20261003.md)

### Game highest-height query recovered semantically

- `func_150450CC` replaces its zero-return placeholder with candidate selection,
  signed vertex copying, optional metadata, and original result flags. The
  144-word slot holds a 143-word body and one padding nop, with 76 differences.
  No new word guards or compiler override are added.
- Eleven new tests and all 164 tool tests pass. Full build and project checks
  pass; recovered neighboring spans and both whole Init sections remain exact.
- Matching totals and README aggregates do not change. The candidate collector
  remains a placeholder with a handwritten shared-register retail interface.
  [Note 759](WORKING_NOTES/759-game-highest-height-query-semantic-recovery-20261002.md)
  records the semantic evidence and whole-group dependency audit.

### Game position/scale overlap wrapper return completed

- `func_15044CE4` now explicitly returns `s32` and forwards the overlap result
  consumed by the list callback caller. All 23 words remain directly exact;
  no new word guard or compiler profile is needed.
- Six new tests include all 65,536 signed scales, alias-sensitive load/store
  timing, byte preservation, and actual wrapper/overlap integration. All 153
  tool tests, the full build, and project checks pass. Neighboring spans and
  both complete Init sections remain exact.
- Matching totals and README aggregates do not change. See
  [Note 758](WORKING_NOTES/758-game-position-scale-overlap-wrapper-return-20261002.md)
  for the contract proof and next placeholder, `func_150450CC`.

### Game oriented record overlap matched

- `func_15044B78` replaces its zero-return placeholder with the full player /
  oriented-record overlap test. All 91 words match; six strict guards normalize
  only the complete store/load pairs for three private integer stack slots.
- `func_15048A40` now explicitly returns the float result consumed by retail;
  its twelve-word span remains directly exact.
- Sixteen new 32-bit tests and all 147 tool tests pass. The full code build,
  project checks, neighboring recovered spans, and both whole Init sections
  pass verification. Total matching C rises to 3,255 / 5,461 (59.60%);
  Game matching C rises to 2,582 / 4,788 (53.93%).
- README changes only its aggregate table. See
  [Note 757](WORKING_NOTES/757-game-oriented-record-overlap-match-20261002.md)
  for semantics, stack proof, tests, and the next wrapper-return task.

### Init resume and remaining assembly boundary

- Rebuilt and regenerated the production baseline: Init 492 / 492 C rows
  exact, with both complete Init code/data sections identical to retail.
- Reconfirmed 47 assembly rows / 12,252 bytes. Two small leaf experiments
  remain deferred; the other 45 require retained assembly or whole-contract
  work. No completed conversion or README aggregate change is claimed.
- Preserved the interrupted, oversized Game overlap recovery in a named Git
  stash. [Note 756](WORKING_NOTES/756-init-resume-verification-and-conversion-boundary-20261002.md)
  records the conversion boundaries and exact draft recovery command.

### Game record list processor directly matched

- `func_15044A28` replaces its zero-return placeholder with the full callback,
  delay, lifetime, unlink, and mode-2 release-marking pass. All 84 words emit
  directly from C without guards; constructor and allocator remain exact.
- Fifteen new 32-bit tests and all 131 tool tests, project checks, and the full
  code build pass. Both complete Init sections remain exact. The halfword at
  `0x04` is now named lifetime; release marking is not immediate deallocation.
- Exact C is Total 3,254 / 5,461 (59.59%) and Game 2,581 / 4,788 (53.91%),
  with zero drift and 2,207 different rows. README aggregate tables updated.
  Next downstream dependency: `func_15044B78`. See
  [Working Note 755](WORKING_NOTES/755-game-record-list-processor-direct-match-20261002.md).

### Game common record allocator directly matched

- `func_15044964` replaces its null-return placeholder with header
  initialization and tail-list registration. All 49 words emit directly from
  C without guards; the 37-word position/scale constructor remains exact.
- Ten new 32-bit tests cover failure, bounds, list insertion, mutation, and
  actual constructor integration. All 116 tool tests, project checks, and the
  full code build pass; both complete Init sections remain exact.
- Exact C is Total 3,253 / 5,461 (59.57%) and Game 2,580 / 4,788 (53.88%),
  with zero drift and 2,208 different rows. README aggregate tables updated.
  Next lifecycle dependency is `func_15044A28`; no gameplay acceptance is claimed.
  See [Working Note 754](WORKING_NOTES/754-game-common-record-allocator-direct-match-20261002.md).

### Game position/scale constructor directly matched

- `func_150448D0` replaces its zero-return placeholder with a 32-byte record
  constructor. All 37 words emit directly from C, with no guards or override.
- Seven new 32-bit tests and all 106 tool tests, project checks, and the full
  code build pass. Both complete Init sections remain exact.
- Exact C is Total 3,252 / 5,461 (59.55%) and Game 2,579 / 4,788 (53.86%),
  with zero drift and 2,209 different rows. README aggregate tables updated.
- Common allocator `func_15044964` still has a null-return body and is next;
  the constructor match is not complete allocation-path or gameplay proof.
  See [Working Note 753](WORKING_NOTES/753-game-position-scale-constructor-direct-match-20261002.md).

### Game record dispatcher semantically recovered

- `func_15040CC8` replaces its zero-return placeholder with thirty direct
  eight-byte record dispatches and post-dispatch cleanup. The obsolete draft
  incorrectly treated the argument as an array of loaded record pointers.
- The default compiler emits 39 words, one beyond the retail slot; the existing
  overflow mechanism preserves the slot and following address. No guards or
  compiler override were added, and no byte-exact progress is claimed.
- Eight new 32-bit tests and all 99 tool tests, project checks, and the full
  code build pass. Both complete Init sections remain exact. README totals
  remain unchanged; next ordinary recovery is `func_150448D0`. See
  [Working Note 752](WORKING_NOTES/752-game-record-dispatcher-semantic-recovery-20261002.md).

### Init bitmap loop and mask experiments completed

- The final matrix of 55 shape/profile combinations establishes no exact
  `func_10005BE0` replacement. All eleven candidate source shapes pass 65
  positive-count host cases twice each, including bounds and final masks.
- Production assembly, shared declarations, ownership, and README totals are
  unchanged. Both small Init leaves remain deferred; ordinary Game work can
  resume at `func_15040CC8`. No project rebuild or gameplay test was performed.
  See [Working Note 751](WORKING_NOTES/751-init-bitmap-loop-mask-profile-trials-20261002.md).

### Init MMIO pointer-lifetime experiments completed

- Twenty isolated compilations test five new shapes across four IDO profiles.
  Relocation-resolved comparison finds no exact eleven-word replacement for
  `func_100038E0`; production assembly and conversion totals are unchanged.
- Pointer-lifetime variants either retain the previous optimized address
  rematerialization or introduce a frame. No production build or hardware
  execution was performed. Next bounded Init experiment: `func_10005BE0`.
  See [Working Note 750](WORKING_NOTES/750-init-mmio-pointer-lifetime-profile-trials-20261002.md).

### Remaining Init assembly reassessed on resume

- Fresh inventory confirms 492 C / 47 assembly rows; all 492 Init C rows
  match, and both complete linked Init code/data sections remain exact.
- Two small leaves remain deferred experiments: MMIO `func_100038E0` and
  bitmap `func_10005BE0`. Neither has a proven matching replacement; the
  other 45 rows need retained assembly or separate whole-contract work.
- No source, README totals, or host artifacts changed, and no rebuild was
  performed. Candidate blockers and acceptance steps are recorded in
  [Working Note 749](WORKING_NOTES/749-init-remaining-assembly-resume-assessment-20261002.md).

### Game row-destination byte fill matched

- `func_1501CDC0` replaces its zero-return placeholder with sixteen-byte
  fills across active destination pointers, preserving repeated pointer
  loads and the count reread. All 37 words match with two strict guards.
- Six 32-bit tests cover zero counts, exact bounds, 120-byte row stride,
  thirty slots, duplicates, and a self-aliasing pointer reload case. All
  91 tool tests, project checks, and the full build pass. Both entire Init
  sections remain byte-exact.
- Total exact C is 3,251 / 5,461 (59.53%); Game is 2,578 / 4,788 (53.84%).
  Resume ordinary Game at `func_15040CC8`. See
  [Working Note 748](WORKING_NOTES/748-game-row-destination-byte-fill-match-20261002.md).

### Game menu-state reset directly matched

- `func_151DE85C` replaces its zero-return placeholder with gate reset,
  exact external-call arguments, global state setup, and object-byte reset.
  All 35 words match directly from C without guards or overrides.
- Five new tests cover call ordering, global and object writes, call-time
  mutation, and repeated reset. All 85 tool tests, project checks, and the
  full build pass. Both entire Init sections remain byte-exact.
- Total exact C is 3,250 / 5,461 (59.51%); Game is 2,577 / 4,788 (53.82%).
  Resume ordinary Game at `func_1501CDC0`. See
  [Working Note 747](WORKING_NOTES/747-game-menu-state-reset-direct-match-20261002.md).

### Game descriptor-record constructor matched

- `func_151D2F00` replaces its zero-return placeholder with allocation,
  a sixteen-byte descriptor copy, flag-bit clear, and bookkeeping resets.
  All 36 words match with six strict argument-scheduling guards.
- Five new tests check allocation failure, forwarding, exact copy, reset
  offsets, preserved storage, and all 256 flag-byte values. All 80 tool
  tests, project checks, and the full build pass. Both entire Init sections
  remain byte-exact.
- Total exact C is 3,249 / 5,461 (59.49%); Game is 2,576 / 4,788 (53.80%).
  Resume ordinary Game at `func_151DE85C`. See
  [Working Note 746](WORKING_NOTES/746-game-descriptor-record-constructor-match-20261002.md).

### Game owner and selector event handler matched

- `func_151BD21C` replaces its zero-return placeholder with zero-event flag
  handling and bidirectional event-`0x2D` owner/selector remapping. All 40
  words match with nine strict entries, including one inserted return nop.
- Eight 32-bit source tests cover owner/selector matching, remap directions,
  equal-endpoint precedence, unsupported codes, and aliasing. All 75 tool
  tests, project checks, and the full build pass. Both entire Init sections
  remain byte-exact.
- Total exact C is 3,248 / 5,461 (59.48%); Game is 2,575 / 4,788 (53.78%).
  Resume ordinary Game at `func_151D2F00`. See
  [Working Note 745](WORKING_NOTES/745-game-owner-selector-event-handler-match-20261002.md).

### Game eleven-child-slot cleanup recovered and matched

- `func_151B1918` replaces its zero-return placeholder with a void cleanup
  routine: reset two fields, release each non-null child in eleven slots,
  and clear every slot. All 35 words match with six strict guards.
- Seven freestanding 32-bit tests preserve actual guest pointer width and
  slot stride while checking release order, null slots, duplicates,
  callback mutation, and repeated cleanup. All 67 tool tests, project
  checks, and the full build pass. Both complete Init sections remain exact.
- Total exact C is 3,247 / 5,461 (59.46%); Game is 2,574 / 4,788 (53.76%).
  Resume ordinary Game at `func_151BD21C`. See
  [Working Note 744](WORKING_NOTES/744-game-eleven-child-slot-cleanup-match-20261002.md).

### Game threshold-scaled record update matched

- `func_151A4900` replaces its zero-return placeholder with two independent
  threshold gates, paired float increments, and byte-output scaling. All
  39 words match with eleven strict scheduling/operand-order guards.
- Seven new tests cover field offsets, threshold boundaries, independent
  gates, signed scales, low-word wrap, unused arguments, and a 256-case
  sweep that checks the entire record. All 60 tool tests, project checks,
  and the full build pass. Both complete Init sections remain byte-exact.
- Total exact C is 3,246 / 5,461 (59.44%); Game is 2,573 / 4,788 (53.74%).
  Resume ordinary Game at `func_151B1918`. See
  [Working Note 743](WORKING_NOTES/743-game-threshold-scaled-record-update-match-20261002.md).

### Game position publication and callback directly matched

- `func_15163504` replaces its zero-return placeholder with coordinate
  publication from three independent float pointers and optional callback
  dispatch. All 41 words match directly from C without guards or overrides.
- Six source-behavior tests cover independent inputs, signed truncation,
  sentinel handling, publication ordering, callback results and mutation,
  and halfword narrowing. All 53 tool tests, project checks, and the full
  build pass. Both complete Init sections remain byte-exact.
- Total exact C is 3,245 / 5,461 (59.42%); Game is 2,572 / 4,788 (53.72%).
  Resume ordinary Game at `func_151A4900`. See
  [Working Note 742](WORKING_NOTES/742-game-position-publication-and-callback-direct-match-20261002.md).

### Game compact timed callback lifecycle matched

- `func_1515FFEC` replaces its zero-return placeholder with the complete
  41-word lifecycle body, preserving its distinct compact-record offsets
  and callback table. Two strict guards normalize only flag spill width.
- The lifecycle test fixture now runs eight behavior tests independently
  against each record layout. All 47 tool tests, the full build, and project
  checks pass. Both complete Init sections remain byte-exact.
- Total exact C is 3,244 / 5,461 (59.40%); Game is 2,571 / 4,788 (53.70%).
  Resume ordinary Game at `func_15163504`. See
  [Working Note 741](WORKING_NOTES/741-game-compact-timed-callback-record-match-20261002.md).

### Game secondary timed callback lifecycle matched

- `func_15158224` replaces its zero-return placeholder with the complete
  41-word lifecycle body. Two strict guards normalize only the completion
  flag's spill/reload width across the callback.
- Eight source-behavior tests cover the timer gate, expiry, zero boundary,
  sentinel, callback results, halfword wrap, mutation, and selector offset.
  All 39 tool tests, the full build, and project checks pass. Both complete
  Init sections remain byte-exact.
- Total exact C is 3,243 / 5,461 (59.38%); Game is 2,570 / 4,788 (53.68%).
  Resume ordinary Game at `func_1515FFEC`. See
  [Working Note 740](WORKING_NOTES/740-game-secondary-timed-callback-record-match-20261002.md).

### Game dual matrix emitter recovered and directly matched

- `func_15157FE8` replaces its zero-return placeholder with both SDK matrix
  commands and matches all 36 words directly from C, without guards.
- Three new source-behavior tests, all 31 tool tests, project checks, and the
  full code build pass. Both complete Init sections remain byte-exact.
- Total exact C is 3,242 / 5,461 (59.37%); Game is 2,569 / 4,788 (53.65%).
  Resume ordinary Game at `func_15158224`. See
  [Working Note 739](WORKING_NOTES/739-game-dual-matrix-emitter-direct-match-20261002.md).

### Init bitmap leaf contract experiment

- Retail confirms inclusive bitmap endpoints and a partial final-byte mask.
  Local candidate declarations correct the pointer interpretation without
  altering shared headers.
- Three compiler trials yield no direct match. The nineteen-word candidate
  passes 65 host behavior cases; original assembly and Init totals remain.
  See [Working Note 738](WORKING_NOTES/738-init-bitmap-leaf-contract-and-compiler-experiment-20261002.md).

### Init MMIO leaf compiler experiment

- Five isolated `func_100038E0` variants establish the current compiler
  differences but no direct eleven-word match. Original assembly is retained.
- No production source, word patches, profiles, or progress totals changed.
  Fresh matcher and complete Init code/data comparisons preserve the baseline.
- Resume Init at bitmap initializer `func_10005BE0`. See
  [Working Note 737](WORKING_NOTES/737-init-mmio-leaf-bounded-compiler-experiment-20261002.md).

### Init memory-clear leaf converted

- `func_10001420` replaces its assembly owner with a complete semantic C
  clear loop. Six strict guards preserve only retail register allocation;
  all nine linked words and the following function boundary match.
- Three behavior tests check the exact 4,064-byte range, surrounding sentinels,
  and repeat calls. All 28 tool tests, project checks, and the full build pass.
  Entire Init code/data comparisons retain their exact baseline hashes.
- Init reaches 492 / 539 C rows (91.28%), all exact, and 151,796 C bytes
  (92.53%). Total exact C is 3,241 / 5,461 (59.35%). See
  [Working Note 736](WORKING_NOTES/736-init-memory-clear-leaf-conversion-20261002.md).

### Remaining Init assembly reassessed

- All 48 rows / 12,288 bytes are accounted for by SDK assembly, boot/hardware
  contracts, shared-frame decompression, custom leaves, and debug/glyph code.
- Three small leaves are plausible C rewrite experiments, but no additional
  compiler-generated recovery or byte-exact C replacement is established.
- Fresh read-only checks reconfirm all 491 C rows, the entire 164,048-byte
  code section, and 17,376 initialized-data bytes exact. No source conversion,
  rebuild, or aggregate change was made. See
  [Working Note 735](WORKING_NOTES/735-init-retained-assembly-reassessment-20261002.md).

### Game vector normalizer byte-matched

- `func_15145128` matches all 50 retail words after recovering the original
  optional-output expression shape and multiplication order. Three guarded
  words normalize its leaf-frame allocation and fallback local address.
- Nine behavior tests pass for ordinary, zero, optional-output, in-place,
  and aliasing cases. The full code build, matcher, all 25 tool unit tests,
  and project checks pass; both complete Init sections remain byte-exact.
- Overall exact C progress is 3,240 / 5,460 (59.34%); Game is 2,568 / 4,788
  (53.63%), with 2,220 different C rows and zero address drift. See
  [Working Note 734](WORKING_NOTES/734-game-vector-normalizer-match-20261002.md).

### Init MIDI handler recovered and complete Init image byte-matched

- `__n_CSPHandleMIDIMsg` emits all 954 retail words directly from complete
  semantic C, without word guards or a profile override.
- The generated linker now preserves the retail audio data/rodata order.
  Restored physical jump-table placement and six omitted constants make the
  entire 164,048-byte Init code section and 17,376-byte initialized-data
  section byte-exact in direct comparisons with the pristine image.
- Init reaches 491 / 539 C rows, all 491 exact. The supported Init C queue is
  complete; 48 original assembly rows remain intentionally. The full code
  build, matcher, all 16 tool unit tests, and tool checks pass. Resume Game's
  50-word `func_15145128`. See
  [Working Note 733](WORKING_NOTES/733-init-midi-handler-and-complete-init-image-match-20261002.md).

### Init SDK sine recovered and constant ownership repaired

- Init `__sinf` replaces its 448-byte assembly slice with separate semantic
  C ownership, preserving the unrelated Game `sinf` source.
- All 112 words emit directly from C. A scoped linker anchor also restores
  the original math/NaN data addresses; all 224 audited constant bytes match.
- Init is now 490 / 539 C rows, with all 490 byte-exact. The one remaining
  supported C conversion is `__n_CSPHandleMIDIMsg`; 48 handwritten/shared-frame
  rows retain assembly. The full non-matching code build, matcher, and focused
  tests pass. See
  [Working Note 731](WORKING_NOTES/731-init-remaining-assembly-conversion-triage-20261002.md) and
  [Working Note 732](WORKING_NOTES/732-init-sdk-sine-recovery-and-constant-layout-match-20261002.md).

### Init meta-handler body restored and assembly classification corrected

- Explicit layout ownership restores the omitted 716-byte
  `__n_CSPHandleMetaMsg` and fixes the event handler's call relocation. Both
  handlers match all 992 bytes; Init now has 489 exact C rows and no drift.
- The separate function raises Init's measured denominator to 539 and reduces
  the MIDI handler's actual remaining span to 3,816 bytes. Direct guest and
  SDK assembly evidence retains the decompressor and queue helpers as assembly.
- The full code build, linked matcher, and direct byte comparisons pass. See
  [Working Note 730](WORKING_NOTES/730-init-meta-handler-layout-and-assembly-provenance-correction-20261002.md).

### Init compact-sequence event handler recovered and assembly remainder audited

- `__n_CSPHandleNextSeqEvent` replaces its 69-word `GLOBAL_ASM` fallback with
  semantic C and the retail `jtbl_8002C460_init` rodata anchor.
- The matcher finds no real instruction differences. Its one linked mismatch
  follows the already shifted `__n_CSPHandleMetaMsg` address, so Init now has
  487 exact C rows, one address-drift row, and zero different C rows.
- The remaining 50 Init assembly rows were divided between established
  handwritten low-level routines and a smaller candidate set. Init can advance
  further, but converting all 50 would erase original assembly ownership. See
  [Working Note 729](WORKING_NOTES/729-init-compact-sequence-event-handler-and-assembly-audit-20261002.md).

### Game timed callback lifecycle byte-matched

- `func_1513B798` replaces its zero-return placeholder with the optional
  signed-timer update, indexed completion callback, and completed-record
  release path.
- The complete 41-word slot emits from semantic C. Two guarded words retain
  retail's byte-width completion-flag spill across the indirect callback.
- The refreshed matcher reports **3,235 / 5,456 (59.29%)** overall and
  **2,567 / 4,788 (53.61%)** in Game, with zero address drift and 2,221
  different C rows. See
  [Working Note 728](WORKING_NOTES/728-game-timed-callback-lifecycle-match-20261002.md).

### Game resource-descriptor chain callback byte-matched

- `func_15133FD8` replaces its zero-return placeholder with the counted
  descriptor loop that threads `func_15133EEC`'s display-list result through
  each eight-byte resource entry.
- The complete 38-word slot emits from semantic C. Three guarded words retain
  retail's commutative pointer-add operand order and two independent
  publication slots.
- The refreshed matcher reports **3,234 / 5,456 (59.27%)** overall and
  **2,566 / 4,788 (53.59%)** in Game, with zero address drift and 2,222
  different C rows. See
  [Working Note 727](WORKING_NOTES/727-game-resource-descriptor-chain-callback-match-20261002.md).

### Game resource-table prefix offset byte-matched

- `func_1510D374` replaces its zero-return placeholder with the resource
  offset calculation that starts at `D_1A37E0` and sums the requested unsigned
  halfword lengths from `D_80091D20`.
- The complete 36-word routine emits directly from semantic C, including
  retail's remainder loop and four-entry unroll, without guard rows or a
  compiler-profile override.
- The refreshed matcher reports **3,233 / 5,456 (59.26%)** overall and
  **2,565 / 4,788 (53.57%)** in Game, with zero address drift and 2,223
  different C rows. See
  [Working Note 726](WORKING_NOTES/726-game-resource-table-prefix-offset-match-20261002.md).

### Game owner-ID effect payload constructor byte-matched

- `func_150F5C08` replaces its zero-return placeholder with the four-argument
  wrapper that builds a 12-byte owner/ID payload, requests object type `0x51`,
  and conditionally copies the payload into the result.
- The complete 36-word routine emits directly from typed semantic C without
  guard rows or a compiler-profile override. Its 144 linked bytes match retail
  with SHA-256 `3e0454c779174a16f23f0c473b717c27c75c4dc20711e5279db09e1837548818`.
- The refreshed matcher remains **3,232 / 5,456 (59.24%)** overall and
  **2,564 / 4,788 (53.55%)** in Game, with zero address drift and 2,224
  different C rows; the preceding measurement already included this
  live-tree match. See
  [Working Note 725](WORKING_NOTES/725-game-owner-id-effect-payload-constructor-match-20261002.md).

### Game effect payload constructor byte-matched

- `func_150F4D5C` replaces its zero-return placeholder with a fixed
  five-argument wrapper that builds a 12-byte owner/selector payload, requests
  effect type `0x56`, and conditionally copies the payload into the result.
- The complete 36-word routine emits directly from typed semantic C without
  guard rows or a compiler-profile override.
- The refreshed matcher reports **3,232 / 5,456 (59.24%)** overall and
  **2,564 / 4,788 (53.55%)** in Game, with zero address drift and 2,224
  different C rows. See
  [Working Note 724](WORKING_NOTES/724-game-effect-payload-constructor-match-20261002.md).

### Game actor water-state flag transition byte-matched

- `func_150DF820` replaces its zero-return placeholder with the staged actor
  flag transition, attached-actor water test, 750-unit state publication, and
  dry-state callback dispatch.
- The 38-word active body and two padding words preserve retail's frame,
  offsets, branches, delay slots, and relocations. Sixteen guarded words
  normalize one closed integer-register allocation chain.
- The refreshed matcher reports **3,231 / 5,456 (59.22%)** overall and
  **2,563 / 4,788 (53.53%)** in Game, with zero address drift and 2,225
  different C rows. See
  [Working Note 723](WORKING_NOTES/723-game-actor-water-state-flag-transition-match-20261002.md).

### Game selector/vector output initializer byte-matched

- `func_150B060C` replaces its zero-return placeholder with selector lookup,
  null failure handling, two float constants, and three signed-coordinate
  conversions into a 24-byte output record.
- Reading the successful record through the output pointer field reproduces
  retail's exact load lifetime and schedule. All 41 words emit directly from
  semantic C without guard rows or a profile override.
- The refreshed matcher reports **3,230 / 5,456 (59.20%)** overall and
  **2,562 / 4,788 (53.51%)** in Game, with zero address drift and 2,226
  different C rows. See
  [Working Note 722](WORKING_NOTES/722-game-selector-vector-output-initializer-match-20261002.md).

### Game special-event mode dispatcher byte-matched

- `func_15015F40` replaces its zero-return placeholder with the retail
  38-entry event switch, mode-byte update, and decremented index publication.
- The retained `assets/23B040.bin` table proves the eight special events. The
  established object rodata anchor retargets IDO's switch relocations to
  `jtbl_800966C0_game`; all 31 words emit without guard rows.
- The refreshed matcher reports **3,229 / 5,456 (59.18%)** overall and
  **2,561 / 4,788 (53.49%)** in Game, with zero address drift and 2,227
  different C rows. See
  [Working Note 721](WORKING_NOTES/721-game-special-event-mode-dispatch-match-20261002.md).

### Game sentinel coordinate distance byte-matched

- `func_15086BD0` replaces its zero-return placeholder with the retail
  `0xFF` sentinel gate and signed XYZ Euclidean distance calculation across
  two 16-byte records.
- Thirteen expected-word replacements normalize IDO's equivalent address,
  pointer, and load schedule. Two checked insertions retain retail's empty
  branch delay and unreachable duplicate return; three rows are
  relocation-aware.
- The refreshed matcher reports **3,228 / 5,456 (59.16%)** overall and
  **2,560 / 4,788 (53.47%)** in Game, with zero address drift and 2,228
  different C rows. See
  [Working Note 720](WORKING_NOTES/720-game-sentinel-coordinate-distance-match-20261002.md).

### Game object-control reset byte-matched

- `func_150634E4` replaces its zero-return placeholder with canonical
  object-pool indexing, two attached-state resets, control dispatches `0x1D`
  and `0x1E`, and three object-control byte clears.
- Correcting `D_800CC2D0` to its `struct127` array contract and using the
  signed result as an unsigned array index reproduces retail's division and
  shift/add scaling directly from C. No guards or profile override are
  required.
- The refreshed matcher reports **3,227 / 5,456 (59.15%)** overall and
  **2,559 / 4,788 (53.45%)** in Game, with zero address drift and 2,229
  different C rows. See
  [Working Note 719](WORKING_NOTES/719-game-object-control-reset-match-20261002.md).

### Game sixteen-word varargs adapter byte-matched

- `func_15042E3C` replaces its fixed 17-parameter implementation with the
  retail varargs contract and copies sixteen incoming words into the array
  passed to `func_15042ECC`.
- IDO reproduces the complete four-way-unrolled aligned copy loop directly
  from C after placing the `va_list` before the array declaration. No guards,
  insertions, omissions, relocation-aware rows, or profile override are
  required.
- The refreshed matcher reports **3,226 / 5,456 (59.13%)** overall and
  **2,558 / 4,788 (53.43%)** in Game, with zero address drift and 2,230
  different C rows. See
  [Working Note 718](WORKING_NOTES/718-game-sixteen-word-varargs-adapter-match-20261002.md).

### Game trailing marked-record compactor byte-matched

- `func_1503DDD0` replaces its zero-return placeholder with index validation,
  selected-record state marking, and backward compaction of trailing marked
  records.
- Correcting `D_800C6650` to its pointer-owned `struct160` table contract
  restores retail indexing. Sixteen expected-word replacements normalize one
  closed compiler loop schedule; no insertion, omission, relocation-aware
  row, or profile override is required.
- The refreshed matcher reports **3,225 / 5,456 (59.11%)** overall and
  **2,557 / 4,788 (53.40%)** in Game, with zero address drift and 2,231
  different C rows. See
  [Working Note 717](WORKING_NOTES/717-game-trailing-marked-record-compactor-match-20261002.md).

### Game indexed resource lazy-loader byte-matched

- `func_1503D774` replaces its zero-return placeholder with the indexed cache
  check, resource-kind-`0x11` load, failure status, and successful payload
  pointer publication.
- Six expected-word replacements normalize the compiler stack/register
  schedule, and one checked omission removes its redundant result copy. No
  relocation-aware row, insertion, or profile override is required.
- The refreshed matcher reports **3,224 / 5,456 (59.09%)** overall and
  **2,556 / 4,788 (53.38%)** in Game, with zero address drift and 2,232
  different C rows. See
  [Working Note 716](WORKING_NOTES/716-game-indexed-resource-lazy-loader-match-20261002.md).

### Game table-pointer relocator byte-matched

- `func_1503D484` replaces its zero-return placeholder with the
  sentinel-terminated eight-byte record walk, optional pointer rebasing, and
  record-count publication.
- The complete 35-word routine emits directly from semantic C. No
  expected-word guards, checked insertions or omissions, relocations, or
  profile override are required.
- The refreshed matcher reports **3,223 / 5,456 (59.07%)** overall and
  **2,555 / 4,788 (53.36%)** in Game, with zero address drift and 2,233
  different C rows. See
  [Working Note 715](WORKING_NOTES/715-game-table-pointer-relocator-match-20261002.md).

### Game slot-state updater byte-matched

- `func_1502FD70` replaces its zero-return placeholder with the per-slot byte
  state update used by category `0x1D` and optional attached objects.
- Correcting `D_800D2040` to its 187-byte array contract restores bytewise
  indexing. Seventeen expected-word guards normalize the compiler's sentinel
  allocation and fallback schedule; no relocations, insertions, omissions, or
  profile override are required.
- The refreshed matcher reports **3,222 / 5,456 (59.05%)** overall and
  **2,554 / 4,788 (53.34%)** in Game, with zero address drift and 2,234
  different C rows. See
  [Working Note 714](WORKING_NOTES/714-game-slot-state-updater-match-20261002.md).

### Game configurable randomized record spawner byte-matched

- `func_1500F9D0` replaces its zero-return placeholder with the five-argument
  variant of the randomized record allocator and initializer.
- The complete 37-word routine emits directly from semantic C. No expected-word
  guards, checked insertions or omissions, relocations, or profile override are
  required.
- The refreshed matcher reports **3,221 / 5,456 (59.04%)** overall and
  **2,553 / 4,788 (53.32%)** in Game, with zero address drift and 2,235
  different C rows. See
  [Working Note 713](WORKING_NOTES/713-game-configurable-randomized-record-spawner-match-20261002.md).

### Game randomized record spawner byte-matched

- `func_1500F378` replaces its zero-return placeholder with randomized type
  selection, fixed-form allocation, and four-value record initialization.
- The complete 37-word routine emits directly from semantic C. No expected-word
  guards, checked insertions or omissions, relocations, or profile override are
  required.
- The refreshed matcher reports **3,220 / 5,456 (59.02%)** overall and
  **2,552 / 4,788 (53.30%)** in Game, with zero address drift and 2,236
  different C rows. See
  [Working Note 712](WORKING_NOTES/712-game-randomized-record-spawner-match-20261002.md).

### Game paired object-state transition byte-matched

- `func_150CF0A0` replaces its zero-return placeholder with the caller-state
  dispatch and gated state-two updates for objects `0xFE` and `0xFD`.
- The complete 40-word routine emits directly from semantic C. No expected-word
  guards, checked insertions or omissions, relocations, or profile override are
  required.
- The refreshed matcher reports **3,219 / 5,456 (59.00%)** overall and
  **2,551 / 4,788 (53.28%)** in Game, with zero address drift and 2,237
  different C rows. See
  [Working Note 711](WORKING_NOTES/711-game-paired-object-state-transition-match-20261002.md).

### Game delta-intensity limiter byte-matched

- `func_150BA424` replaces its zero-return placeholder with the negative-delta
  gate, capped actor and distance intensity candidates, and minimum-byte store.
- The complete 39-word routine emits directly from semantic C. No expected-word
  guards, checked insertions or omissions, relocations, or profile override are
  required.
- The refreshed matcher reports **3,218 / 5,456 (58.98%)** overall and
  **2,550 / 4,788 (53.26%)** in Game, with zero address drift and 2,238
  different C rows. See
  [Working Note 710](WORKING_NOTES/710-game-delta-intensity-limiter-match-20261002.md).

### Game plane-side predicate byte-matched

- `func_150A2E4C` replaces its zero-return placeholder with the signed-origin
  conversion and non-positive plane-expression predicate used by retail.
- The semantic C preserves retail's fourth-argument overwrite. Twenty
  expected-word guards normalize the compiler's floating-point allocation and
  schedule without insertions, omissions, relocations, or a profile override.
- The refreshed matcher reports **3,217 / 5,456 (58.96%)** overall and
  **2,549 / 4,788 (53.24%)** in Game, with zero address drift and 2,239
  different C rows. See
  [Working Note 709](WORKING_NOTES/709-game-plane-side-predicate-match-20261002.md).

### Game path-count pointer contract byte-matched

- Corrected `D_800D2108` from an inline byte-array declaration to the
  pointer-owned path-count table used by retail.
- That shared contract makes `func_150778F0` and `func_1507A528` byte-exact
  across all 46 and 62 words directly from semantic C. No expected-word guards
  or compiler-profile overrides are required.
- The refreshed matcher reports **3,216 / 5,456 (58.94%)** overall and
  **2,548 / 4,788 (53.22%)** in Game, with zero address drift and 2,240
  different C rows. See
  [Working Note 708](WORKING_NOTES/708-game-path-count-pointer-contract-match-20261002.md).

### Game randomized-step callback byte-matched

- `func_1518F7C4` replaces its zero-return placeholder with the randomized
  float accumulation, object update, and signed-selector callback dispatch.
- The typed record and callback table recover the semantic contract. Twenty-two
  stale-guarded rows normalize IDO's closed frame, retained-pointer, call-delay,
  and callback-branch schedule; seven checked insertions and two omissions
  preserve the complete 37-word retail slot.
- The refreshed matcher reports **3,214 / 5,456 (58.91%)** overall and
  **2,546 / 4,788 (53.17%)** in Game, with zero address drift and 2,242
  different C rows. See
  [Working Note 707](WORKING_NOTES/707-game-randomized-step-callback-match-20261002.md).

### Game position-sample ring recorder byte-matched

- `func_1515CF9C` now uses the recovered signed status-buffer contract and a
  structured 12-byte position copy, followed by the slot's float sample.
- The routine advances the sample count and write cursor, wraps the cursor at
  capacity, and writes status `-1` when no slot remains. Thirty-two of the 37
  retail words emit directly from C; four expected-word guards normalize the
  five-word reset/exit schedule, including one inserted branch.
- The refreshed matcher reports **3,213 / 5,456 (58.89%)** overall and
  **2,545 / 4,788 (53.15%)** in Game, with zero address drift and 2,243
  different C rows. See
  [Working Note 706](WORKING_NOTES/706-game-position-sample-ring-recorder-match-20261002.md).

### Game geometry-mode command helper byte-matched

- `func_15142B7C` retains its two cached-mode gates but now emits the clear and
  set commands through `gSPClearGeometryMode` and `gSPSetGeometryMode`.
- The original post-increment SDK macro shape restores retail's display-list
  cursor lifetime, command-store order, branches, and delay slots. All 37
  words emit directly from semantic C without guards or a compiler-profile
  override.
- The refreshed matcher reports **3,212 / 5,456 (58.87%)** overall and
  **2,544 / 4,788 (53.13%)** in Game, with zero address drift and 2,244
  different C rows. See
  [Working Note 705](WORKING_NOTES/705-game-geometry-mode-command-helper-match-20261002.md).

### Game global-position query byte-matched

- `func_150FCF1C` replaces its zero-return placeholder with the nullable
  three-coordinate conversion and the original `func_15165BB0` query.
- The semantic C emits 33 of the 37 retail words directly. Four
  expected-word guards move the local float vector from IDO's persistent
  `sp+0x24` placement to retail's `sp+0x20` placement; no compiler-profile
  override is used.
- The refreshed matcher reports **3,211 / 5,456 (58.85%)** overall and
  **2,543 / 4,788 (53.11%)** in Game, with zero address drift and 2,245
  different C rows. See
  [Working Note 704](WORKING_NOTES/704-game-global-position-query-match-20261002.md).

### Game scaled indexed-global updater byte-matched

- `func_1509DF20` replaces its zero-return placeholder with the event-state and
  global-mode gates, paired indexed float updates, and indexed status-byte set.
- Both float tables receive the event value multiplied by `1/65536`. All 37
  retail words emit directly from semantic C without guards or a compiler
  profile override; retaining the repeated event value/index expressions
  reproduces retail's independent load and address-calculation schedule.
- The refreshed matcher reports **3,210 / 5,456 (58.83%)** overall and
  **2,542 / 4,788 (53.09%)** in Game, with zero address drift and 2,246
  different C rows. See
  [Working Note 703](WORKING_NOTES/703-game-scaled-indexed-global-updater-match-20261002.md).

### Game payload-record initializer byte-matched

- `func_1518BCD0` replaces its zero-return placeholder with the six-argument
  record allocation, null return, 0x1C-byte payload copy to offset `0x10`, and
  two independent five-bit random field initializations.
- All 36 retail words emit directly from semantic C without guards or a
  compiler-profile override. The `u8` selector contract reproduces the low-byte
  reload from spilled `a1`, while the record local recovers retail's reuse of
  `s0` from allocator owner to return pointer.
- The refreshed matcher reports **3,209 / 5,456 (58.82%)** overall and
  **2,541 / 4,788 (53.07%)** in Game, with zero address drift and 2,247
  different C rows. See
  [Working Note 702](WORKING_NOTES/702-game-payload-record-initializer-match-20261002.md).

### Game color-driver callback family byte-matched

- `func_150D149C` and `func_150D1B40` replace their zero-return placeholders
  with the shared float-driver pattern: update fields `0x30`, `0x2C`, and
  `0x28` using callback-specific ranges, then publish the truncated first
  component with two retained global color channels.
- Their complete 37- and 36-word slots emit directly from semantic C without
  guards or compiler-profile overrides. An explicit pointer to field `0x28`
  recovers its duplicate stack lifetime; a local full-width integer publisher
  declaration reproduces retail's plain `trunc.w.s` conversion.
- The refreshed matcher reports **3,208 / 5,456 (58.80%)** overall and
  **2,540 / 4,788 (53.05%)** in Game, with zero address drift and 2,248
  different C rows. See
  [Working Note 701](WORKING_NOTES/701-game-color-driver-callback-family-match-20261002.md).

### Game script-result flag callback byte-matched

- `func_150C7350` replaces its zero-return placeholder with the unconditional
  `0x80004000` flag update, six-argument `func_1509BE40` query, and conditional
  set/clear of bit `0x00400000`.
- The complete 36-word retail slot emits directly from semantic C without
  guards or a compiler-profile override. The early-return source form recovers
  the saved-register lifetime, branch-likely delay load, mask construction,
  shared epilogue, and trailing padding word.
- The refreshed matcher reports **3,206 / 5,456 (58.76%)** overall and
  **2,538 / 4,788 (53.01%)** in Game, with zero address drift and 2,250
  different C rows. See
  [Working Note 700](WORKING_NOTES/700-game-script-result-flag-callback-match-20261002.md).

### Game randomized event descriptor byte-matched

- `func_150FFC3C` replaces its zero-return placeholder with the nested-owner
  gate and seven-byte event descriptor containing a randomized duration,
  randomized variant, one-hot owner mask, and `-1` terminator.
- All 35 retail words emit directly from semantic C without guards or a
  compiler-profile override. The byte-array representation and source write
  order reproduce both random calls, pointer reload, branch-likely exit, and
  descriptor submission schedule.
- The refreshed matcher reports **3,205 / 5,456 (58.74%)** overall and
  **2,537 / 4,788 (52.99%)** in Game, with zero address drift and 2,251
  different C rows. See
  [Working Note 699](WORKING_NOTES/699-game-randomized-event-descriptor-match-20261002.md).

### Game vector-argument forwarder byte-matched

- `func_150E3340` replaces its zero-return placeholder with the forwarding call
  that duplicates a three-word vector, supplies mode `0x1A` and scale `10.0f`,
  and passes a three-float position plus trailing word and halfword arguments.
- All 35 retail words emit directly from semantic C without guards or a
  compiler-profile override. The recovered parameter types reproduce the
  retail frame, incoming argument spills, load schedule, call delay slot, and
  `void` epilogue.
- The refreshed matcher reports **3,204 / 5,456 (58.72%)** overall and
  **2,536 / 4,788 (52.97%)** in Game, with zero address drift and 2,252
  different C rows. See
  [Working Note 698](WORKING_NOTES/698-game-vector-argument-forwarder-match-20261002.md).

### Game timer/position updater byte-matched

- `func_150CBA30` replaces its zero-return placeholder with the signed timer
  decrement, timer-scaled updates to two position fields, and the flag-gated
  shifted-value clamp for byte `0x5C`.
- All 35 retail words emit directly from semantic C without guards. Testing the
  reloaded timer directly keeps its lifetime separate from the later signed
  clamp value and recovers retail's register allocation.
- The refreshed matcher reports **3,203 / 5,456 (58.71%)** overall and
  **2,535 / 4,788 (52.94%)** in Game, with zero address drift and 2,253
  different C rows. See
  [Working Note 697](WORKING_NOTES/697-game-timer-position-byte-clamp-match-20261002.md).

### Game resource-teardown finalizer byte-matched

- `func_15080C64` replaces its zero-return placeholder with the active-state
  and record-byte gates, `func_15080BE8` teardown, category-sensitive global
  flag update, and optional pending-record completion/clear.
- All 36 retail words emit directly from semantic C without guards. Expressing
  the record-byte test directly from `D_800D1950` recovers retail's temporary
  register allocation.
- The refreshed matcher reports **3,202 / 5,456 (58.69%)** overall and
  **2,534 / 4,788 (52.92%)** in Game, with zero address drift and 2,254
  different C rows. See
  [Working Note 696](WORKING_NOTES/696-game-resource-teardown-finalizer-match-20261002.md).

### Game attachment-state transition byte-matched

- `func_15074664` now uses the retail shared-store control flow: state-one
  entry calls `func_10011FDC(5)`, state-one exit calls `func_10011FDC(0)`,
  and the potentially reloaded attachment receives the requested state byte.
- Treating the prior state byte as unsigned and joining the final assignment
  reduces the raw compile from 37 words to the exact 35-word retail slot. The
  complete routine emits directly from semantic C without guards.
- The refreshed matcher reports **3,201 / 5,456 (58.67%)** overall and
  **2,533 / 4,788 (52.90%)** in Game, with zero address drift and 2,255
  different C rows. See
  [Working Note 695](WORKING_NOTES/695-game-attachment-state-transition-match-20261002.md).

### Game trigonometric lookup byte-matched

- `func_150489B0` replaces its zero-return placeholder with the byte-angle
  quadrant lookup across `D_8009A020`, `D_8009A220`, `D_8009A420`, and
  `D_8009A620`, including the reflected indexes and result signs.
- All 36 lookup words match. Thirty-one emit directly from semantic C; five
  stale-checked words preserve retail's shift-before-negate indexing shape.
  Seven additional checked words keep adjacent `func_15048A40` exact after
  correcting the lookup's `f32 func(u8)` contract.
- The refreshed matcher reports **3,200 / 5,456 (58.65%)** overall and
  **2,532 / 4,788 (52.88%)** in Game, with zero address drift and 2,256
  different C rows. See
  [Working Note 694](WORKING_NOTES/694-game-trigonometric-lookup-match-20261002.md).

### Game timer-expiry callback byte-matched

- `func_1503EEC0` replaces its zero-return placeholder with the selected-entry
  update, signed timer subtraction/store, and indexed expiry callback.
- All 35 retail words match. Sixteen emit directly from semantic C; nineteen
  stale-checked words preserve one closed register-allocation and scheduling
  cycle, including relocation-aware guards for both referenced global tables.
- The refreshed matcher reports **3,199 / 5,456 (58.63%)** overall and
  **2,531 / 4,788 (52.86%)** in Game, with zero address drift and 2,257
  different C rows. See
  [Working Note 693](WORKING_NOTES/693-game-timer-expiry-callback-match-20261002.md).

### Game attachment-state updater byte-matched

- `func_150333A8` replaces its zero-return placeholder with the global disable
  gate, attached-object state clear, and reference-height/`+300.0f` threshold
  update for byte `3`.
- All 38 retail words match. Thirty-one emit directly from semantic C; seven
  stale-checked words normalize one commutative float equality and the closed
  equivalent branch-likely/delay-slot store layout.
- The refreshed matcher reports **3,198 / 5,456 (58.61%)** overall and
  **2,530 / 4,788 (52.84%)** in Game, with zero address drift and 2,258
  different C rows. See
  [Working Note 692](WORKING_NOTES/692-game-attachment-state-updater-match-20261002.md).

### Game group-record activator byte-matched

- `func_150227BC` replaces its zero-return placeholder with the complete
  count-sized walk over a selected 30-byte ID row. Each ID is resolved through
  `func_151149AC`, and byte `0x6E` on the returned record is set to one.
- All 35 retail words match. Thirty-three emit directly from semantic C; two
  stale-checked rows normalize only the independent row-offset subtraction and
  index initialization around the opening branch.
- The refreshed matcher reports **3,197 / 5,456 (58.60%)** overall and
  **2,529 / 4,788 (52.82%)** in Game, with zero address drift and 2,259
  different C rows. See
  [Working Note 691](WORKING_NOTES/691-game-group-record-activator-match-20261002.md).

### Game counted resource-owner teardown byte-matched

- `func_151EDB58` replaces its zero-return placeholder with the complete
  auxiliary-resource release, owner free, and count-sized pointer-array loop.
- All 33 retail words emit directly from semantic C. The frame, saved
  registers, release order, branch-likely delay slots, and loop schedule need
  no expected-word guards or compiler-profile override.
- The refreshed matcher reports **3,196 / 5,456 (58.58%)** overall and
  **2,528 / 4,788 (52.80%)** in Game, with zero address drift and 2,260
  different C rows. See
  [Working Note 690](WORKING_NOTES/690-game-counted-resource-owner-teardown-match-20261002.md).

### Game event-record matcher byte-matched

- `func_151D7538` restores selector-`0x3D` word/tag matching and object
  destruction, plus the alternate event-forwarding path with both embedded
  record addresses.
- Its complete 35-word retail slot matches. The compact semantic body emits
  34 words; fourteen stale-checked rows, including one checked insertion,
  preserve the retail pointer lifetime and closed compiler register allocation.
  Neither relocation-bearing call is patched.
- The refreshed matcher reports **3,195 / 5,456 (58.56%)** overall and
  **2,527 / 4,788 (52.78%)** in Game, with zero address drift and 2,261
  different C rows. See
  [Working Note 689](WORKING_NOTES/689-game-event-record-matcher-match-20261002.md).

### Game mode-offset adjuster byte-matched

- `func_151CD224` restores the sampled-value delta, embedded-record scale,
  mode byte dispatch, and positive/negative output update.
- Its complete 39-word retail slot matches. Six stale-checked rows, including
  one checked insertion, preserve the shared record base and mode register;
  three trailing retail padding words are retained by the generated-object
  layout tool.
- The refreshed matcher reports **3,194 / 5,456 (58.54%)** overall and
  **2,526 / 4,788 (52.76%)** in Game, with zero address drift and 2,262
  different C rows. See
  [Working Note 688](WORKING_NOTES/688-game-mode-offset-adjuster-match-20261002.md).

### Game output-default initializer byte-matched

- `func_151B498C` restores its thirteen output writes: two packed mode words,
  eight `0xFF` values, one zero, and byte selectors `5` and `0x2B`.
- All 34 retail words emit directly from semantic C without expected-word
  guards or a compiler-profile override.
- The refreshed matcher reports **3,193 / 5,456 (58.52%)** overall and
  **2,525 / 4,788 (52.74%)** in Game, with zero address drift and 2,263
  different C rows. See
  [Working Note 687](WORKING_NOTES/687-game-output-default-initializer-match-20261002.md).

### Game threshold/intensity updater byte-matched

- `func_151A787C` restores its two signed threshold tests, elapsed-tick-scaled
  halfword updates, and timer-scaled byte outputs.
- All 35 retail words match. Nineteen emit directly from semantic C; sixteen
  stale-checked words normalize one commutative multiply and one closed
  compiler register-allocation and scheduling cycle.
- The refreshed matcher reports **3,192 / 5,456 (58.50%)** overall and
  **2,524 / 4,788 (52.72%)** in Game, with zero address drift and 2,264
  different C rows. See
  [Working Note 686](WORKING_NOTES/686-game-threshold-intensity-updater-match-20261002.md).

### Game tick-compensated damping callback byte-matched

- `func_1519C4E4` restores its elapsed-tick loop over two floating-point
  damping fields and its conditional timer-times-scale byte reduction.
- All 34 retail words emit directly from semantic C without expected-word
  guards or a compiler-profile override.
- The refreshed matcher reports **3,191 / 5,456 (58.49%)** overall and
  **2,523 / 4,788 (52.69%)** in Game, with zero address drift and 2,265
  different C rows. See
  [Working Note 685](WORKING_NOTES/685-game-tick-compensated-damping-callback-match-20261002.md).

### Game clamped height-byte updater byte-matched

- `func_1518B1D8` restores its nonnegative height-delta gate, scaled object
  candidate, half-delta candidate, upper clamps, minimum selection, and byte
  store at offset `0x70`.
- All 35 retail words match. Twenty-five emit directly from semantic C; ten
  stale-checked suffix words normalize only the compiler phi register and an
  equivalent branch-delay schedule.
- The refreshed matcher reports **3,190 / 5,456 (58.47%)** overall and
  **2,522 / 4,788 (52.67%)** in Game, with zero address drift and 2,266
  different C rows. See
  [Working Note 684](WORKING_NOTES/684-game-clamped-height-byte-match-20261002.md).

### Game active-row wrapper byte-matched

- `func_1517F4D8` restores its indexed timer and mapped-mode gates, unchanged
  handle returns for inactive rows, and three-byte parameter-row dispatch to
  `func_1517F08C`.
- All 35 retail words emit directly from semantic C without expected-word
  guards or a compiler-profile override.
- The refreshed matcher reports **3,189 / 5,456 (58.45%)** overall and
  **2,521 / 4,788 (52.65%)** in Game, with zero address drift and 2,267
  different C rows. See
  [Working Note 683](WORKING_NOTES/683-game-active-row-wrapper-match-20261002.md).

### Game mode dispatcher byte-matched

- `func_15170EC4` restores the sparse global-mode dispatch to
  `func_15170B90`, including the mode-2 and mode-`0x10` parameter sets, the
  caller selector's low byte, and the full trailing payload.
- All 34 retail words emit directly from semantic C without expected-word
  guards or a compiler-profile override.
- The refreshed matcher reports **3,188 / 5,456 (58.43%)** overall and
  **2,520 / 4,788 (52.63%)** in Game, with zero address drift and 2,268
  different C rows. See
  [Working Note 682](WORKING_NOTES/682-game-mode-dispatcher-match-20261002.md).

### Game packed two-axis integrator byte-matched

- `func_1516F864` restores the packed signed X/Y velocity reconstruction,
  global time-scale multiplication, and packed position accumulation.
- All 34 retail words now match. Thirty-two stale-checked expected-word rows,
  including two relocation-aware global-address rows, preserve compiler
  register allocation while leaving the recovered arithmetic and schedule
  explicit in C.
- The refreshed matcher reports **3,187 / 5,456 (58.41%)** overall and
  **2,519 / 4,788 (52.61%)** in Game, with zero address drift and 2,269
  different C rows. See
  [Working Note 681](WORKING_NOTES/681-game-packed-two-axis-integrator-match-20261002.md).

### Game resource-release family and height predicate byte-matched

- `func_1514795C`, `func_151571C4`, and `func_15158A20` restore three
  33-word inclusive resource scans, conditional frees, and trailing-slot
  releases over their respective object layouts.
- `func_15159084` restores its mode exclusions, global-height and flag test,
  fallback object-height comparison, and state-byte override. One
  stale-checked word preserves retail's commutative floating-equality operand
  order; the other 38 words emit directly from semantic C.
- The refreshed matcher reports **3,186 / 5,456 (58.39%)** overall and
  **2,518 / 4,788 (52.59%)** in Game, with zero address drift and 2,270
  different C rows. See
  [Working Note 680](WORKING_NOTES/680-game-resource-release-family-and-height-predicate-match-20261002.md).

### Game resource release and vertex rotation byte-matched

- `func_151325C8` restores the inclusive resource-entry scan, conditional
  allocator releases, and final trailing-slot release.
- `func_151436B4` now materializes all four trigonometric results before its
  vertex stores, reproducing retail's complete 34-word call and arithmetic
  schedule. Both functions emit directly from semantic C without guards.
- The refreshed matcher reports **3,182 / 5,456 (58.32%)** overall and
  **2,514 / 4,788 (52.51%)** in Game, with zero address drift and 2,274
  different C rows. See
  [Working Note 679](WORKING_NOTES/679-game-resource-release-and-vertex-rotation-match-20261002.md).

### Game angular motion-update family byte-matched

- `func_1511515C` and `func_151151FC` restore signed packed-rate integration
  and 0-to-360-degree wrapping for two object components.
- `func_15115EDC` restores pre-update position snapshots and type-`0x4B`
  displacement extension after `func_15115E0C`. One stale-checked word
  preserves the retail record-pointer register across a mismatched declaration.
- The refreshed matcher reports **3,180 / 5,456 (58.28%)** overall and
  **2,512 / 4,788 (52.46%)** in Game, with zero address drift and 2,276
  different C rows. See
  [Working Note 678](WORKING_NOTES/678-game-angular-motion-update-family-match-20261002.md).

### Game render-parameter wrapper family byte-matched

- `func_1510E7A4`, `func_1510E82C`, and `func_1510E8BC` now restore the
  argument adapters around `func_1510E950`, including raw coordinate words,
  mixed float/integer stack arguments, default bounds, and the final mode.
- Their complete 34-, 36-, and 37-word slots emit directly from semantic C
  without expected-word guards or compiler-profile overrides.
- The refreshed matcher reports **3,177 / 5,456 (58.23%)** overall and
  **2,509 / 4,788 (52.40%)** in Game, with zero address drift and 2,279
  different C rows. See
  [Working Note 677](WORKING_NOTES/677-game-render-parameter-wrapper-family-match-20261002.md).

### Game owner-event callback byte-matched

- `func_15100230` now restores event `0x48` owner-pointer/owner-ID matching,
  object destruction on a match, and forwarding of all other events with the
  embedded owner record.
- Its complete 35-word callback uses a function-specific `-O1 -g3` object.
  Twenty-eight stale-checked words preserve the closed retail schedule and
  relocation-aware placement of both calls.
- The refreshed matcher reports **3,174 / 5,456 (58.17%)** overall and
  **2,506 / 4,788 (52.34%)** in Game, with zero address drift and 2,282
  different C rows. See
  [Working Note 676](WORKING_NOTES/676-game-owner-event-callback-match-20261002.md).

### Game condition state flags byte-matched

- `func_150F9A20` now replaces its zero-return placeholder with the complete
  condition query and state update. Condition `0x4025` selects mutually
  exclusive flags `0x80`/`0x08` and writes `85.0f` or zero to field `0x190`.
- The complete 36-word slot emits directly from semantic C without expected
  word guards. See
  [Working Note 675](WORKING_NOTES/675-game-condition-state-flag-match-20261002.md).

### Game command-row loop byte-matched

- `func_150413FC` now replaces its zero-return placeholder with the complete
  zero-terminated command loop. It translates each command, processes the
  associated eight-byte row, and threads the returned state into the next
  iteration.
- Its 33-word extent, frame, calls, loop updates, and epilogue emit from
  semantic C. Nine stale-checked words normalize only the independent
  prologue schedule.
- The refreshed matcher reports **3,172 / 5,456 (58.14%)** overall and
  **2,504 / 4,788 (52.30%)** in Game, with zero address drift and 2,284
  different C rows. See
  [Working Note 674](WORKING_NOTES/674-game-command-row-loop-match-20261002.md).

### Game object teardown byte-matched

- `func_15106E78` now replaces its zero-return placeholder with the complete
  object teardown: indexed destructor callback, two optional child releases,
  and embedded-record cleanup.
- All 32 words emit directly from C with no guarded normalization. The adjacent
  `func_15106EF8` and `func_15106F24` wrappers now use the recovered pointer
  ABI and remain byte-exact.
- The refreshed matcher reports **3,171 / 5,456 (58.12%)** overall and
  **2,503 / 4,788 (52.28%)** in Game, with zero address drift and 2,285
  different C rows. See
  [Working Note 673](WORKING_NOTES/673-game-object-teardown-match-20261002.md).

### Init sound-event dispatcher byte-matched

- `_n_handleEvent` now replaces its zero-return placeholder with the complete
  extended sound-player dispatcher: resource resolution, voice allocation,
  envelope timing, pan/volume/pitch/effect updates, retries, cleanup,
  channel-volume changes, and child-sound startup.
- The typed body compiles to 1,241 words. Retail's 1,363-word closed layout is
  reproduced by 1,241 stale-checked rows, including 122 insertions and 87
  relocation-aware rows.
- Direct comparison reports zero differences across all 5,452 bytes. Both
  spans share SHA-256
  `583662222304bf87a3b24bc9495055b930b2076e36ecb37183fa5612a36b8525`.
  Totals are **3,170 / 5,456 (58.10%)** overall and
  **487 / 487 (100.00%)** in Init, with zero address drift and zero different
  Init C rows. The absolute `jtbl_8002C708_init` table remains a separate
  shifted Init-data layout issue. See
  [Working Note 672](WORKING_NOTES/672-init-sound-event-dispatcher-match-20261002.md).

## 2026-10-01

### Init compact-sequence voice handler byte-matched

- `__n_CSPVoiceHandler` now replaces its zero-return placeholder with the
  complete compact-sequence event loop. It handles sequence references,
  envelopes, tremolo/vibrato, MIDI/meta dispatch, master volume, Rare's two
  custom control events, restartable play/stop state, and final voice/channel
  cleanup.
- The readable body compiles to 667 words. Retail's 684-word closed IDO layout
  is reproduced by 667 stale-checked rows, including 17 insertions and 45
  relocation-aware rows.
- Direct comparison reports zero differences across all 2,736 bytes. Both
  spans share SHA-256
  `c5673a64d3bce5c9a7b63077a0d36dc5e87fa6096ea470c2902ef76c85c4331e`.
  Totals are **3,169 / 5,456 (58.08%)** overall and
  **486 / 487 (99.79%)** in Init, with zero address drift and one different
  Init C row. See
  [Working Note 671](WORKING_NOTES/671-init-compact-sequence-voice-handler-match-20261001.md).

### Init path-projection query byte-matched

- `func_1000A750` now replaces its zero-return placeholder with the full
  path-relative spatial query. It finds the nearest authored point, compares
  its adjacent segments, projects and clamps the source position, and forwards
  the resulting offsets to `func_1000A420` for attenuation and pan.
- The readable semantic body contains 404 words. Retail's five-block unrolled
  distance scan and closed IDO layout are reproduced by 401 stale-checked
  rows, including 176 insertions and 19 relocation-aware rows. The already
  matched neighboring `func_1000A420` remains byte-exact.
- Direct comparison reports zero differences across all 2,320 bytes. Both
  spans share SHA-256
  `29dd260425d94890348301d23f84c2bafbc69119f06e2044f6c003c8aaabb8c1`.
  Totals are **3,168 / 5,456 (58.06%)** overall and
  **485 / 487 (99.59%)** in Init, with zero address drift and two different
  Init C rows. See
  [Working Note 670](WORKING_NOTES/670-init-path-projection-query-match-20261001.md).

### Init 64DD interrupt handler byte-matched

- `__osLeoInterrupt` now replaces its zero-return placeholder with the
  source-grounded 64DD PI/Leo interrupt state machine. It handles DMA-busy and
  mechanical-interrupt recovery, read/write sector DMA, C1/C2 bookkeeping,
  two-block track transitions, failure reporting, and completion delivery.
- The compiler emits 440 words. Of those, 323 emit directly; 117
  stale-checked rows, including 52 relocation-aware rows, normalize the closed
  IDO allocation and scheduling difference. The existing layout tool supplies
  the retail slot's final zero word, with no insertion or omission guards.
- Direct comparison reports zero differences across all 1,764 bytes. Both
  spans share SHA-256
  `2c73138bf3c4ec93d256f0014f9526852817bf7460b691ea4fac3a36f140e695`.
  Totals are **3,167 / 5,456 (58.05%)** overall and
  **484 / 487 (99.38%)** in Init, with zero address drift and three different
  Init C rows. See
  [Working Note 669](WORKING_NOTES/669-init-64dd-interrupt-handler-match-20261001.md).

### Init conversion helper byte-matched

- `func_10002718` now replaces its zero-return placeholder with the complete
  SDK conversion dispatcher. It handles character, signed and unsigned
  integer, floating-point, pointer, string, `%n`, percent, and fallback
  conversions while advancing the aligned argument cursor.
- The compact semantic body contains 338 words and emits 42 retail words
  directly. The remaining layout is normalized by 296 stale-checked rows,
  including 87 insertions, three omissions, and four relocation-aware rows.
- Direct comparison reports zero differences across all 1,688 bytes. Both
  spans share SHA-256
  `422fae5d07d1c40324ccac587ce494ec46c539fe74ddd18750242eb4b6dcb9ca`.
  Totals are **3,166 / 5,456 (58.03%)** overall and
  **483 / 487 (99.18%)** in Init, with zero address drift and four different
  Init C rows. See
  [Working Note 668](WORKING_NOTES/668-init-conversion-helper-match-20261001.md).

### Init formatted-output dispatcher byte-matched

- `func_100020D0` now replaces its empty placeholder with the complete
  callback-driven formatted-output loop. It emits literal runs, parses format
  flags, width, precision and length modifiers, dispatches conversion, and
  writes each padded conversion segment in retail order.
- The compact semantic body contains 361 words and emits 95 retail words
  directly. The remaining layout is normalized by 266 stale-checked rows,
  including 44 insertions, three omissions, and ten relocation-aware rows.
- Direct comparison reports zero differences across all 1,608 bytes. Both
  spans share SHA-256
  `fbc33626d707e258fdce37f95a3d2c5a989c31b39ee14a00d1db74d7b7f00dfa`.
  Totals are **3,165 / 5,456 (58.01%)** overall and
  **482 / 487 (98.97%)** in Init, with zero address drift and five different
  Init C rows. See
  [Working Note 667](WORKING_NOTES/667-init-formatted-output-dispatcher-match-20261001.md).

### Init numeric formatter byte-matched

- `func_10001AA8` now replaces its zero-return placeholder with the numeric
  layout stage used by the floating formatter. It handles fixed, scientific,
  and general formats; trims precision; inserts decimal and exponent fields;
  and computes deferred width padding.
- The compact semantic body contains 365 words and emits 87 retail words
  directly. The remaining layout is normalized by 278 stale-checked rows,
  including 13 insertions, eight omissions, and three relocation-aware rows.
- Direct comparison reports zero differences across all 1,480 bytes. Both
  spans share SHA-256
  `d34588b845730b80b2a13a9bdaf75c284a2ad8f0bb718fb73cbc08fb1968243e`.
  Totals are **3,164 / 5,456 (57.99%)** overall and
  **481 / 487 (98.77%)** in Init, with zero address drift and six different
  Init C rows. See
  [Working Note 666](WORKING_NOTES/666-init-numeric-formatter-match-20261001.md).

### Init sound-record updater byte-matched

- `func_10011624` now replaces its zero-return placeholder with the complete
  bounded sound-record update pass. It validates stale handles, derives
  listener-relative volume and pan, runs optional callbacks, creates voices,
  updates changed parameters, smooths distance-driven pitch, and retires
  inactive records.
- The compact semantic body contains 356 words and emits 64 retail words
  directly. The remaining layout is normalized by 293 stale-checked rows:
  292 word substitutions, one insertion, and 20 relocation-aware rows.
- Direct comparison reports zero differences across all 1,428 bytes. Both
  spans share SHA-256
  `670591f6d2289fc90f772638ae1d52533acd7ca2cc7d3b659fe6f3db194f7e2f`.
  Totals are **3,163 / 5,456 (57.97%)** overall and
  **480 / 487 (98.56%)** in Init, with zero address drift and seven different
  Init C rows. See
  [Working Note 665](WORKING_NOTES/665-init-sound-record-updater-match-20261001.md).

### Init instrument channel loader byte-matched

- `func_1001B7D0` now replaces its zero-return placeholder with the complete
  program-resource and channel-default loader. It releases the previous
  resource, relocates unresolved sounds, transfers envelope and instrument
  defaults, and records missing-resource state.
- Repeated channel indexing and retail-ordered stack locals reproduce the
  complete 345-word `-g` body directly from semantic C. No expected-word
  guards, insertions, omissions, or relocation overrides are required.
- Direct comparison reports zero differences across all 1,380 bytes. Both
  spans share SHA-256
  `9fe00cc8721b345585d353b756b7131239bcfc9f104f87f4f6c0d9dcb9e41f1f`.
  Totals are **3,162 / 5,456 (57.95%)** overall and
  **479 / 487 (98.36%)** in Init, with zero address drift and eight different
  Init C rows. See
  [Working Note 664](WORKING_NOTES/664-init-instrument-channel-loader-match-20261001.md).

### Init audio-environment controller byte-matched

- `func_10012020` now replaces its zero-return placeholder with the complete
  five-mode audio-environment controller: mode overrides, oscillator-driven
  pitch targets, transition ramps, master gain, and two-channel updates.
- The semantic compact body emits 111 of 336 retail words directly. The Init
  object now retargets its generated switch table to `jtbl_8002C410_init`;
  225 stale-checked rows include the final retail padding `nop` and 103 rows
  with relocation metadata for the table, constants, globals, and calls.
- Direct comparison reports zero differences across all 1,344 bytes. Both
  spans share SHA-256
  `983583d5193a47ee8b1140807b1a8dbdda67951e3d8b31bb21c2cc89a14ed8fb`.
  Totals are **3,161 / 5,456 (57.94%)** overall and
  **478 / 487 (98.15%)** in Init, with zero address drift and nine different
  Init C rows. See
  [Working Note 663](WORKING_NOTES/663-init-audio-environment-controller-match-20261001.md).

### Init sequence transition dispatcher byte-matched

- `func_1000D96C` now replaces its zero-return placeholder with the complete
  sequence-record transition path. It resolves primary and child records,
  detaches stale children, allocates replacements, and applies the six
  transition modes and their fade values.
- The semantic compact body contains 293 words, with 73 emitted directly at
  their retail positions. Two hundred twenty scoped, stale-checked rows
  normalize the closed IDO layout; they include seven scheduled word
  insertions and 20 relocation-aware rows.
- Direct comparison reports zero differences across all 1,200 bytes. Both
  spans share SHA-256
  `925f906618db0bc5a5e8a3b5ffc06cb886e87031928dffac85ac005bb893faf1`.
  Totals are **3,160 / 5,456 (57.92%)** overall and
  **477 / 487 (97.95%)** in Init, with zero address drift and 10 different
  Init C rows. See
  [Working Note 662](WORKING_NOTES/662-init-sequence-transition-dispatcher-match-20261001.md).

### Init SDK float formatter byte-matched

- `func_10001550` now replaces its empty placeholder with the recovered SDK
  `_Ldtob` algorithm for `%f`, `%e`, `%E`, `%g`, and `%G` conversions.
- The 296-word semantic body restores NaN/Inf handling, decimal power scaling,
  eight-digit chunk generation, significant-digit selection, and rounding.
  One hundred seventy-six scoped, stale-checked rows, including 10
  relocation-aware rows, normalize the remaining IDO allocation and frame
  layout while retaining the exact control flow and calls.
- Direct comparison reports zero differences across all 1,184 bytes. Both
  spans share SHA-256
  `fade94f3c21abd93ef6e80ac921e889a4577d4e9cd7e0180f0c21dbf37bdcd2b`.
  Totals are **3,159 / 5,456 (57.90%)** overall and
  **476 / 487 (97.74%)** in Init, with zero address drift and 11 different
  Init C rows. See
  [Working Note 661](WORKING_NOTES/661-init-sdk-float-formatter-match-20261001.md).

### Init audio channel updater byte-matched

- `func_1000D2F8` now replaces its zero-return placeholder with the complete
  three-channel sequence and state updater. It handles deferred sequence
  replacement, child promotion and failure cleanup, callback state, three
  parameter ramps, channel-volume refresh, and linked-channel validation.
- The semantic C emits retail's exact 280-word extent and control-flow order.
  One hundred thirteen function-scoped, stale-checked rows normalize the
  remaining closed IDO allocation and scheduling differences. Two additional
  scoped rows retain the exact 133-word `func_1000D758` caller after correcting
  the channel-index ABI.
- Direct comparison reports zero differences across all 1,120 bytes. Both
  spans share SHA-256
  `4735e2a088809328cac08aa82b49cf965dbd98d84de66acffe2bee99c5ed0b92`.
  Totals are **3,158 / 5,456 (57.88%)** overall and
  **475 / 487 (97.54%)** in Init, with zero address drift and 12 different
  Init C rows. See
  [Working Note 660](WORKING_NOTES/660-init-audio-channel-updater-match-20261001.md).

### Init audio subframe builder byte-matched

- `func_1001FB40` now replaces its zero-return placeholder with the complete
  auxiliary-bus audio command builder: opening clears, main-filter dispatch,
  mixer routing, effect refresh, and ADPCM and pole-filter commands.
- Recovered SDK audio macros reproduce the retail command-temporary lifetimes
  and branch-delay schedule. The compact object emits all 296 words and every
  relocation directly from C, with no expected-word guards or insertions.
- Direct comparison reports zero differences across all 1,184 bytes. Both
  spans share SHA-256
  `092c988cb1f4f75ee8947a2e663b9b103ce8eaf84ccc12a28ca1ea2f0392f145`.
  Totals are **3,157 / 5,456 (57.86%)** overall and
  **474 / 487 (97.33%)** in Init, with zero address drift and 13 different
  Init C rows. See
  [Working Note 659](WORKING_NOTES/659-init-audio-subframe-builder-match-20261001.md).

### Init channel event and timer updater byte-matched

- `func_1000CEAC` now replaces its zero-return placeholder with the complete
  per-channel queue drain, event-mask decoder, mode-specific flag/timer
  updates, active-voice transition, and sixteen-slot countdown pass.
- The semantic C emits the exact 275-word extent. Two hundred thirty
  function-scoped, stale-checked rows normalize its closed compiler allocation
  and layout differences; 41 rows preserve relocation changes explicitly.
- Direct comparison reports zero differences across all 1,100 bytes. Both
  spans share SHA-256
  `3dd80b02cc6d85f41dedfcb2f18b5e7997d72a2f4370377755a16e75142f3618`.
  Totals are **3,156 / 5,456 (57.84%)** overall and
  **473 / 487 (97.13%)** in Init, with zero address drift and 14 different
  Init C rows. See
  [Working Note 658](WORKING_NOTES/658-init-channel-event-timer-update-match-20261001.md).

### Init audio-runtime bootstrap byte-matched

- `func_10008F90` now replaces its zero-return placeholder with the audio
  runtime bootstrap: callbacks, sample sizing, synthesis parameters, streaming
  pools, command buffers, queues, and audio-thread startup.
- A scoped macro-enabled function object prevents IDO's translation-unit state
  from perturbing already matched neighbors. The semantic body emits 263
  words; 139 stale-checked rows restore the 271-word retail stream through
  eight insertions, with 45 relocation-aware rows.
- Direct comparison reports zero differences across all 1,084 bytes. Both
  spans share SHA-256
  `7d897607c391e61d966f2a5e6f8cff10d99527081e8193fb3d7b01c73dee38c3`.
  Totals are **3,155 / 5,456 (57.83%)** overall and
  **472 / 487 (96.92%)** in Init, with zero address drift and 15 different
  Init C rows. See
  [Working Note 657](WORKING_NOTES/657-init-audio-runtime-bootstrap-match-20261001.md).

### Init bidirectional heap allocator byte-matched

- `func_10003C6C` now replaces its zero-return placeholder with the core Init
  allocator: class-based alignment, head/tail free-list search, block splitting
  or consumption, physical/free-link repair, and largest-block maintenance.
- The semantic C emits the exact 258-word extent. Two hundred sixteen
  function-scoped, stale-checked rows normalize its closed frame, allocation,
  and schedule differences; 42 rows preserve relocation changes explicitly.
- Direct comparison reports zero differences across all 1,032 bytes. Both
  spans share SHA-256
  `7b188602de53c31d0fc1e07510cee2edd09e91b94dff1e5a1f295a026afdcaea`.
  Totals are **3,154 / 5,456 (57.81%)** overall and
  **471 / 487 (96.71%)** in Init, with zero address drift and 16 different
  Init C rows. See
  [Working Note 656](WORKING_NOTES/656-init-bidirectional-heap-allocator-match-20261001.md).

### Init packed spatial-audio state updater byte-matched

- `func_1000BF60` now replaces its zero-return placeholder with its full
  sound-`0x22` state updater: conditional startup, three spatial queries,
  changed-channel volume and position writes, and two mode transitions.
- The semantic C emits 250 words with retail's `0x60` frame. One hundred eleven
  function-scoped, stale-checked rows restore the 252-word retail stream,
  including two redundant `move a2` insertions and two relocation-aware rows.
- Direct comparison reports zero differences across all 1,008 bytes. Both
  spans share SHA-256
  `e7a0f3fa7e4953b9c62c703ee6c206047cdf9ddc3dc3452c2217b800435b3e1d`.
  Totals are **3,153 / 5,456 (57.79%)** overall and
  **470 / 487 (96.51%)** in Init, with zero address drift and 17 different
  Init C rows. See
  [Working Note 655](WORKING_NOTES/655-init-packed-spatial-audio-state-match-20261001.md).

### Init scheduler and render thread byte-matched

- `func_100049E0` now replaces its empty placeholder with the full seven-class
  scheduler message loop: retrace client notifications and counters, delayed
  task timing, SP yield/completion handling, pending graphics-task dispatch,
  idle rendering, and guarded controller reads.
- The semantic C emits 239 words in retail's `0, 2, 1, 3, 6` case order.
  One hundred fifty function-scoped, stale-checked rows restore the 244-word
  retail stream through 148 replacements and five insertions; 44 rows carry
  relocation changes explicitly. The switch remains anchored to the existing
  `jtbl_8002C0A0_init` data.
- Direct comparison reports zero differences across all 976 bytes. Both spans
  share SHA-256
  `623dd58fd193533d32ee6d6c98a80c1d07bf0926bef273f14b9b58e8f79d68ad`.
  Totals are **3,152 / 5,456 (57.77%)** overall and
  **469 / 487 (96.30%)** in Init, with zero address drift and 18 different
  Init C rows. See
  [Working Note 654](WORKING_NOTES/654-init-scheduler-render-thread-match-20261001.md).

### Init audio-library bootstrap byte-matched

- `func_10008180` now replaces its zero-return placeholder with the full audio
  bootstrap: heap and synthesizer setup, bank loading and relocation, sequence
  table loading, 150 even-length normalizations, three sequence players, and
  final sound-player configuration.
- The semantic C emits 213 words. Sixty-four function-scoped, stale-checked
  rows restore the 214-word retail schedule, including one checked insertion
  for the sequence-loop pointer update and 10 relocation-aware rows for the
  reordered sequence and player globals.
- Direct comparison reports zero differences across all 856 bytes. Both spans
  share SHA-256
  `e5edcb6039f9b8e816dacd1dea8996ed458a81fa7a68f9f342ef13de781a5dbf`.
  Totals are **3,151 / 5,456 (57.75%)** overall and
  **468 / 487 (96.10%)** in Init, with zero address drift and 19 different
  Init C rows. See
  [Working Note 653](WORKING_NOTES/653-init-audio-library-bootstrap-match-20261001.md).

### Init handwritten bcopy restored

- The `0x10023A10..0x10023D20` `bcopy` slot now links the splitter-extracted
  original handwritten assembly instead of the simplified byte-loop C
  substitute. The retail routine selects overlap-safe forward or backward
  copying, peels alignment, and uses 32-byte, 16-byte, 4-byte, and byte tails.
- Direct linked-ELF comparison confirms all 196 words, including the three
  trailing padding words, match retail. Both 784-byte spans share SHA-256
  `9de2251afa4dd169a3c55e33d2be4c540174550516f075ec6a6f0f9855fb6e6d`.
- This is an ownership correction rather than a new C match. The measured C
  totals are now **3,150 / 5,456 (57.73%)** overall and
  **467 / 487 (95.89%)** in Init, with zero address drift and 20 different
  Init C rows. See
  [Working Note 652](WORKING_NOTES/652-init-handwritten-bcopy-restoration-20261001.md).

### Init resource-request manager byte-matched

- `func_10009CBC` now distinguishes encoded resource requests from existing
  handles, resolves transfer metadata, acquires a free manager node or evicts
  the last eligible inactive node, and maintains the active and free lists.
- For new requests it allocates and clears a rounded buffer, performs the
  required cache maintenance, advances the DMA-message index, submits a
  high-priority PI transfer, and replaces the caller's encoded value with the
  resource node. The semantic C emits 205 words; 107 function-scoped,
  stale-checked rows, including three checked insertions, normalize the
  remaining IDO register and scheduling cycle. Relocation-aware rows move the
  `D_8002AE50`, `D_80041330`, and `D_800416F0` address pairs and affected calls
  to their retail words within the same semantic schedule.
- The linked and retail 832-byte spans share SHA-256
  `aa485f43fb54b12658083b22b286f6e3c97cf462aa1e1e6f7637cc2bbaec7131`.
  Totals are **3,150 / 5,457 (57.72%)** overall and
  **467 / 488 (95.70%)** in Init. See
  [Working Note 651](WORKING_NOTES/651-init-resource-request-manager-match-20261001.md).

### Init spatial attenuation and pan calculator byte-matched

- `func_1000A420` now selects the original planar or three-axis distance
  helper, computes normalized attenuation between the configured near and far
  limits, and clamps the result to the signed 15-bit range.
- When requested and sufficiently separated, it derives horizontal direction,
  applies listener rotation, maps the result into the engine's packed pan
  range, and writes optional pan and raw-distance outputs. Eighty-one
  stale-checked rows normalize a closed temporary-register schedule; one
  checked insertion restores the retail narrowing move. No relocation moves.
- The linked and retail 816-byte spans share SHA-256
  `c55660dda7d31b77b81018ecf5bfe1fcdaac6a2bb3f29ba21604485e066964b1`.
  Totals are **3,149 / 5,457 (57.71%)** overall and
  **466 / 488 (95.49%)** in Init. See
  [Working Note 650](WORKING_NOTES/650-init-spatial-attenuation-pan-match-20261001.md).

### Init resource-completion manager byte-matched

- `func_1000A03C` now drains nonblocking completion messages, finds each
  resource node, moves it from the pending list to the active list, and
  relocates type-1 resource table entries.
- Its second phase clears completed voice flags, releases idle resources,
  recycles their nodes, and services `D_8003E384` through `func_1000A348`.
  The semantic C recovers the retail 120-byte frame and `s0`-`s3` lifetimes;
  86 stale-checked rows, including five checked insertions, normalize the
  remaining closed IDO list and delay-slot schedule without moving any
  relocations.
- The linked and retail 780-byte spans share SHA-256
  `42c65b8dbbdff63a3471f0a348effb6a07ee2bf0293af5b159513b9340bbe989`.
  Totals are **3,148 / 5,457 (57.69%)** overall and
  **465 / 488 (95.29%)** in Init. See
  [Working Note 649](WORKING_NOTES/649-init-resource-completion-manager-match-20261001.md).

### Init audio-event parameter update byte-matched

- `func_1000F85C` now rejects invalid or inactive sound handles and forwards
  parameter updates to the indexed active sound state.
- Selector `0x10` converts pitch cents with `alCents2Ratio` and preserves the
  resulting floating-point bits in the integer event payload. Selector `0x11`
  is normalized to `0x10`. Twenty-six words emit directly from semantic C;
  22 stale-checked rows preserve one closed compiler scheduling difference,
  including the moved table and call relocations.
- The linked and retail 192-byte spans share SHA-256
  `1a0eb4cb47c876f07f4200adf31d43e19fcb899941bb5ffe02d34f9df25e0ee3`.
  Totals are **3,147 / 5,457 (57.67%)** overall and
  **464 / 488 (95.08%)** in Init. See
  [Working Note 648](WORKING_NOTES/648-init-audio-event-parameter-update-match-20261001.md).

### Init handle-record lookup byte-matched

- `func_1000FEF0` now validates its nonzero handle and scans enabled
  `D_80041FE0` records for the handle plus two exact owner selectors.
- Its explicit count and narrowed-key lifetimes recover the retail frame,
  saved `s0`, and 40-word rolled loop. A per-function no-unroll object override
  preserves every neighboring `init_EB00` match. Thirty-two words emit
  directly from C; eight stale-checked rows normalize the remaining opening
  schedule and closed `v0`/`a1` allocation choice.
- The linked and retail 160-byte spans share SHA-256
  `634cdf00d310c2aa443ae12aeb10a84e894b20225f95659a9e8738eac2ed2f50`.
  Totals are **3,146 / 5,457 (57.65%)** overall and
  **463 / 488 (94.88%)** in Init. See
  [Working Note 647](WORKING_NOTES/647-init-handle-record-lookup-match-20261001.md).

### Init active-record lookup byte-matched

- `func_1000FF90` now scans the active `D_80041FE0` records for a primary
  identifier, two independently optional selectors, and a clear disable bit.
- Declaring the third selector unsigned reproduces retail's two independent
  `-1` constants and exact 35-word control-flow shape. Twenty-two words emit
  directly from C; thirteen stale-checked rows normalize one closed
  `a0`/`a1`/`a3` compiler-allocation cycle, including two table-base
  relocations.
- The linked and retail 140-byte spans share SHA-256
  `eb36532b03f324f494ecc9c6cf7753c062f747d46e2de603413d378c6d5a72d4`.
  Totals are **3,145 / 5,457 (57.63%)** overall and
  **462 / 488 (94.67%)** in Init. See
  [Working Note 646](WORKING_NOTES/646-init-active-record-lookup-match-20261001.md).

### Init listener/audio update byte-matched

- `func_10011BB8` replaces its zero-return placeholder with the recovered
  listener snapshot, audio-record processing and compaction, and two-channel
  transition update.
- Fifty-seven of 180 linked words emit unchanged from semantic C. One hundred
  twenty-seven stale-checked rows normalize the closed IDO allocation and
  scheduling cycle; four of those rows omit redundant compact-object moves so
  the recovered body retains the retail 180-word extent.
- The linked and retail 720-byte spans share SHA-256
  `46f06a5608ddf3ddaa80ec0b81444b7b4463fee22ab930ca536ccd71394fa0de`.
  Totals are **3,144 / 5,457 (57.61%)** overall and
  **461 / 488 (94.47%)** in Init. See
  [Working Note 645](WORKING_NOTES/645-init-listener-audio-update-match-20261001.md).

### Init PRENMI shutdown thread byte-matched

- `func_100052A0` replaces its empty placeholder with the recovered shutdown
  path: synchronization, thread stops, VI reset, four-port motor cleanup, two
  elapsed-time waits, cache writeback, and the final park loop.
- One hundred sixty-one of 180 linked words emit directly from semantic C.
  Nineteen relocation-aware rows bind the compiler's function-local static
  timer references to the canonical retail timer symbols without changing
  instruction selection or scheduling.
- The linked and retail 720-byte spans share SHA-256
  `19f1d82d263567b460cce60c28d40fe7c017c72193c23311adbb2664ebb37ba4`.
  Totals are **3,143 / 5,457 (57.60%)** overall and
  **460 / 488 (94.26%)** in Init. See
  [Working Note 644](WORKING_NOTES/644-init-prenmi-shutdown-thread-match-20261001.md).

### Init packed audio-state updater byte-matched

- `func_1000C530` replaces its zero-return placeholder with the recovered
  packed transition-state updater, including sound-slot start, stop, value,
  mode, expiry, and high-byte fade behavior.
- One hundred thirty-eight of 174 linked words emit directly from semantic C.
  Thirty-six stale-checked non-relocating rows normalize the remaining IDO
  local allocation, scheduling, and commutative operand-order differences.
- The linked and retail 696-byte spans share SHA-256
  `0bb708b2a657dd68247bd5fc413a15779db6418cda26509bd6aaaefe644881fa`.
  Totals are **3,142 / 5,457 (57.58%)** overall and
  **459 / 488 (94.06%)** in Init. See
  [Working Note 643](WORKING_NOTES/643-init-packed-audio-state-updater-match-20261001.md).

### Init integer formatter byte-matched

- `_Litob` now uses the recovered wide format-code ABI with unsigned-byte
  comparisons while retaining the SDK integer-to-string algorithm for signed,
  octal, decimal, hexadecimal, precision, and field-width formatting.
- Ten of 168 linked words emit directly from semantic C. One hundred
  fifty-seven stale-checked rows normalize 158 words in IDO's closed
  allocation/scheduling cycle, including one guarded final delay-slot
  insertion and all moved relocations.
- The linked and retail 672-byte spans share SHA-256
  `ec1902fca7a676159f2cd92ce58465dd9c03c1c0e0c7831d2301b6d2dfb09f04`.
  Totals are **3,141 / 5,457 (57.56%)** overall and
  **458 / 488 (93.85%)** in Init. See
  [Working Note 642](WORKING_NOTES/642-init-integer-formatter-match-20261001.md).

### Init common system initializer byte-matched

- `__osInitialize_common` replaces its empty placeholder with the recovered
  CPU/FPU setup, PIF initialization, exception-vector installation, cache and
  RDB setup, clock-rate adjustment, cold-reset NMI clear, and 64DD Leo probe.
- Sixty-nine of 168 linked words emit directly from semantic C. Ninety-nine
  stale-checked rows normalize IDO's remaining frame, register allocation,
  copy, clock-store, and MMIO scheduling differences while preserving moved
  relocations.
- The linked and retail 672-byte spans share SHA-256
  `853e38c0f3d587f1f6e1f70d7fb0c4b640fbfcaf314727d7975b757c1b8dc4e4`.
  Totals are **3,140 / 5,457 (57.54%)** overall and
  **457 / 488 (93.65%)** in Init. See
  [Working Note 641](WORKING_NOTES/641-init-common-system-initializer-match-20261001.md).

### Init sound-slot dispatcher byte-matched

- `func_10010BE8` replaces its zero-return placeholder with the recovered
  handle reuse, free-slot scan, generation update, effect-mix adjustment,
  cents-to-pitch conversion, and bank-sound allocation behavior.
- Seventy-nine of 164 linked words emit directly from semantic C. Eighty-five
  stale-checked rows normalize IDO's frame, register allocation, loop
  induction, and scheduling differences while preserving moved relocations.
- The linked and retail 656-byte spans share SHA-256
  `3e184b650c03d5c5992a6ac1877b3246acd1a5c3a0a77807fcc6ab86dfdb7d4d`.
  Totals are **3,139 / 5,457 (57.52%)** overall and
  **456 / 488 (93.44%)** in Init. See
  [Working Note 640](WORKING_NOTES/640-init-sound-slot-dispatcher-match-20261001.md).

### Init boot-loader thread byte-matched

- `func_10001194` replaces its empty placeholder with the recovered memory
  clearing, cache invalidation, framebuffer allocation, compressed Game-image
  transfer, relocation-table decode, and subsystem startup sequence.
- Eighty-seven of 163 words emit directly from semantic C. Seventy-six
  stale-checked rows normalize compiler allocation and scheduling while
  preserving shifted call, global, and section-boundary relocations.
- The linked and retail 652-byte spans share SHA-256
  `681ac3de3b09479dfe0890da9d095fded0097f673189325a1b87e771a0ee983e`.
  Totals are **3,138 / 5,457 (57.50%)** overall and
  **455 / 488 (93.24%)** in Init. See
  [Working Note 639](WORKING_NOTES/639-init-boot-loader-thread-match-20261001.md).

### Init music-control callback byte-matched

- `func_1000BCBC` replaces its zero-return placeholder with the recovered
  channel initialization, scene-`0x13` distance level, and event-driven
  secondary channel update.
- Ninety-nine of 169 words emit directly from semantic C. Seventy
  stale-checked rows normalize IDO's closed allocation and scheduling cycles
  around the two float-to-unsigned conversions while preserving relocations.
- The linked and retail 676-byte spans share SHA-256
  `a480744a95151b2487e577091d004e331f215c5f2fa8feb1583a958d2ad8ff9e`.
  Totals are **3,137 / 5,457 (57.49%)** overall and
  **454 / 488 (93.03%)** in Init. See
  [Working Note 638](WORKING_NOTES/638-init-music-control-callback-match-20261001.md).

### Init PI device-manager loop byte-matched

- `func_10002E50` replaces its zero-return placeholder with the recovered PI
  command thread: the custom direct-PI ownership handshake, DMA and EDMA
  dispatch, loopback completion, event wait, and access-queue release.
- The canonical libultra case order emits the retail control flow and jump
  table. All 148 words emit directly from semantic C; no word guards are used.
- The linked and retail 592-byte spans share SHA-256
  `827b2c980c11c00f6ac52be3d05a66941f1d7a4d2850bd4a5a4d3263e5123ba2`.
  Totals are **3,136 / 5,457 (57.47%)** overall and
  **453 / 488 (92.83%)** in Init. See
  [Working Note 637](WORKING_NOTES/637-init-pi-device-manager-loop-match-20261001.md).

### Init audio-task submission byte-matched

- `func_100095A0` replaces its zero-return placeholder with the recovered AI
  backlog policy, aligned output selection, synthesis-frame call, scheduler
  task construction, queue submission, and command-buffer toggle.
- The source restores the 64-byte frame and complete 139-word extent. Of those
  words, 68 emit directly from semantic C and 71 stale-checked rows normalize
  compiler allocation and scheduling while preserving all relocations.
- The linked and retail 556-byte spans share SHA-256
  `0ccabf4750562b5e4fcd9ed0470bc6e10bb5aab211258c1ed3b4c2ceaeaeb360`.
  Totals are **3,135 / 5,457 (57.45%)** overall and
  **452 / 488 (92.62%)** in Init. See
  [Working Note 636](WORKING_NOTES/636-init-audio-task-submission-match-20261001.md).

### Init three-channel audio-mix coordinator byte-matched

- `func_1000D758` replaces its empty placeholder with the recovered
  three-record classifier and prioritized channel-mix policy, followed by the
  three-channel refresh and frame-parameter forwarding loops.
- Of 133 words, 112 emit directly from semantic C. Twenty-one stale-checked
  rows normalize one closed compiler register-allocation cycle; four retain
  the existing address relocations.
- The linked and retail 532-byte spans share SHA-256
  `9dc672958d710f32ad34fd9e7b08f3b4059ded72a7e096e7ce7438440241852c`.
  Totals are **3,134 / 5,457 (57.43%)** overall and
  **451 / 488 (92.42%)** in Init. See
  [Working Note 635](WORKING_NOTES/635-init-three-channel-audio-mix-coordinator-match-20261001.md).

### Init actor secondary-audio creator byte-matched

- `func_10010344` replaces its zero-return placeholder with the recovered
  actor-owned secondary-audio allocator. It chooses the direct camera-aware or
  positional path, applies actor-specific range and flag policy, retires the
  prior callback, and stores the replacement handle.
- Its recovered return contract is `s32`. Of 133 words, 115 emit directly
  from semantic C and 18 stale-checked rows normalize compiler register
  allocation and independent scheduling, including two relocation-aware rows.
- The linked and retail 532-byte spans share SHA-256
  `e4ab5af56af48c42b725a3aef809a80675e61953528b74452ed71ff35c59c03b`.
  Totals are **3,133 / 5,457 (57.41%)** overall and
  **450 / 488 (92.21%)** in Init. See
  [Working Note 634](WORKING_NOTES/634-init-actor-secondary-audio-creator-match-20261001.md).

### Init threshold audio-state callback byte-matched

- `func_1000B638` replaces its zero-return placeholder with the recovered
  packed-state callback. It gates per-player audio from the record's 500-unit
  threshold, applies level-specific channel transitions, and maintains the
  separate level-`0x27` effect bit.
- The 126-word routine emits 114 words directly from semantic C. Twelve
  stale-checked rows normalize one closed compiler register-allocation cycle
  and one stack-slot selection.
- The linked 504-byte span has SHA-256
  `9606b7c262cfd3a32317eb6775ec0fa9b29db52b3d7f5974048b14a33140cb8d`.
  Totals are **3,132 / 5,457 (57.39%)** overall and
  **449 / 488 (92.01%)** in Init. See
  [Working Note 633](WORKING_NOTES/633-init-threshold-audio-state-callback-match-20261001.md).

### Init sequence-buffer replacement byte-matched

- `func_10008CE8` replaces its zero-return placeholder with the recovered
  compact-sequence replacement path. It performs bounded stop polling, frees
  and reallocates a changed sequence buffer, copies its aligned payload, binds
  the sequence, and restarts the selected player.
- Recovering the 8-byte metadata record and compact polling loops emits 121 of
  126 words directly from semantic C. Five stale-checked rows normalize two
  independent compiler stack-slot selections.
- The linked 504-byte span has SHA-256
  `81fcae361887ea2de962c306ac07c2b55afbd4d8f4c3ee1fa34274c5afc81b14`.
  Totals are **3,131 / 5,457 (57.38%)** overall and
  **448 / 488 (91.80%)** in Init. See
  [Working Note 632](WORKING_NOTES/632-init-sequence-buffer-replacement-match-20261001.md).

### Init actor positional-audio creator byte-matched

- `func_10010154` replaces its zero-return placeholder with the recovered
  actor-bound audio allocator. It rejects inactive actors, handles the direct
  camera-aware path, applies actor-ID-specific range and flag policy, retires
  the prior handle, and creates a positional replacement when the actor stays
  active.
- Its recovered return contract is `s32`, avoiding the false `u16`
  normalization from the placeholder declaration. Of 124 words, 78 emit
  directly from semantic C and 46 stale-checked rows normalize the remaining
  compiler register allocation and scheduling.
- The linked and retail 496-byte spans share SHA-256
  `0c51638492ad873409e1f0207c4185ddbcb9288bcfc7b8384ba1e065d39fb915`.
  Totals are **3,130 / 5,457 (57.36%)** overall and
  **447 / 488 (91.60%)** in Init. See
  [Working Note 631](WORKING_NOTES/631-init-actor-positional-audio-creator-match-20261001.md).

### Init actor event/audio dispatcher byte-matched

- `func_1000EFB4` replaces its zero-return placeholder with the recovered
  actor callback. It validates the active actor/value pair, scans a terminated
  actor-ID list, returns the actor's packed state and truncated coordinates on
  acceptance, and handles the `0xCA`, `0x2CF`, and `0x2D2` sound events.
- The complete 125-word body emits directly from semantic C with no retail
  word guards. The linked and retail 500-byte spans share SHA-256
  `0835e229b55c402d6fac8e84fe5249cf3549d000c72e31a961e5247a09a77c09`.
- Totals are **3,129 / 5,457 (57.34%)** overall and
  **446 / 488 (91.39%)** in Init. See
  [Working Note 630](WORKING_NOTES/630-init-actor-event-audio-dispatch-match-20261001.md).

### Init packed audio-state transition byte-matched

- `func_1000C350` replaces its zero-return placeholder with the recovered
  packed state transition. It initializes channel masks on first entry,
  dispatches the mode-3 and mode-6 transitions, clears non-level-0x1D channel
  state, and synchronizes the low seven state bits with `D_80041F08`.
- The complete 120-word control-flow shape emits from semantic C. Of those,
  119 words match directly; one stale-checked non-relocating guard preserves
  retail's commutative equality-branch operand order.
- The linked and retail spans share SHA-256
  `e3002a2667674611eea979e4716e2117d436bb7d3878a2c78c71062948187d99`.
  Totals are **3,128 / 5,457 (57.32%)** overall and
  **445 / 488 (91.19%)** in Init. See
  [Working Note 629](WORKING_NOTES/629-init-packed-audio-state-transition-match-20261001.md).

### Init direct PI copy routine byte-matched

- `func_1000480C` replaces its incomplete commented draft with the recovered
  polled PI copy. It rounds the size to an even count, waits for software and
  hardware ownership, then copies through the uncached device window using
  aligned words or the retail two-byte-misaligned halfword sequence.
- The semantic C body compiles to 113 words. A table of 112 stale-checked,
  relocation-aware rows, including two inserted epilogue words, normalizes
  IDO's frame, saved-register allocation, and instruction schedule to retail's
  complete 117-word padded slot.
- The linked and retail spans share SHA-256
  `a34d2643235b5ceaf6120ddd09fbfc9b5ecb9f0ab34dcb09d55a081c90f1403e`.
  Totals are **3,127 / 5,457 (57.30%)** overall and
  **444 / 488 (90.98%)** in Init. See
  [Working Note 628](WORKING_NOTES/628-init-direct-pi-copy-match-20261001.md).

### Init controller-pak read routine byte-matched

- `__osContRamRead` now restores the retail retry-time PIF RAM preparation:
  all 16 words are set to `0x000000FF` and `pifstatus` is cleared before each
  read DMA attempt.
- The no-pak path retains the value already produced by `CHNL_ERR`; removing a
  redundant assignment recovers retail's direct fallthrough into retry
  handling. The complete 145-word routine emits directly from semantic C with
  no expected-word guards.
- The linked and retail spans share SHA-256
  `bf8aa2ecac0083d38e003575c990c79882ead67450e9d1d777462ba2dea9b4be`.
  Totals are **3,126 / 5,457 (57.28%)** overall and
  **443 / 488 (90.78%)** in Init. See
  [Working Note 627](WORKING_NOTES/627-init-controller-pak-read-match-20261001.md).

### Init allocator free/coalescing routine byte-matched

- `func_10004074` replaces its zero-return placeholder with the recovered
  interrupt-protected allocator free path. It validates the payload pointer,
  clears the allocation state, coalesces adjacent physical blocks, repairs or
  inserts the result in the address-ordered free list, and updates the tail and
  largest-free-block caches.
- The semantic C occupies the complete 119-word slot. Twenty-four words emit
  directly; 95 stale-checked relocation-aware rows normalize IDO's frame,
  register allocation, branches, and scheduling while preserving both
  `osSetIntMask` calls and all allocator-global references.
- The linked and retail spans share SHA-256
  `f1baa8fbaeb74356ce2ff072fab39380ec3e2f06dab02e7ef33269f8eb04567c`.
  Totals are **3,125 / 5,457 (57.27%)** overall and
  **442 / 488 (90.57%)** in Init. See
  [Working Note 626](WORKING_NOTES/626-init-allocator-free-coalescing-match-20261001.md).

### Init audio request allocator byte-matched

- `func_1000FA64` replaces its zero-return placeholder with the recovered
  bounded request allocation, callback-dependent flag setup, optional
  coordinate replacement, packed record initialization, cents-to-ratio
  conversion, queue submission, and committed-handle return.
- The semantic C occupies the complete 109-word slot. Nine words emit
  directly; 100 stale-checked relocation-aware rows normalize IDO's stack,
  scheduling, and register allocation while preserving the two calls and two
  global address pairs.
- The linked and retail spans share SHA-256
  `d8f6e2f920e541908664a49316ed5a4d01e494969639bdb3023beedc2b706e30`.
  Totals are **3,124 / 5,457 (57.25%)** overall and
  **441 / 488 (90.37%)** in Init. See
  [Working Note 625](WORKING_NOTES/625-init-audio-request-allocator-match-20261001.md).

### Init object-aware audio dispatcher byte-matched

- `func_10010FFC` replaces its zero-return placeholder with the recovered
  object validity gates and audio dispatch selection. Camera-backed objects
  dispatch directly through `func_10010BE8`; other objects use three-quarters
  of the requested volume and forward a spatial request through
  `func_10010E78`.
- The spatial path recovers the object-type range lookup, unsigned scale
  conversion, 80/256 clamp behavior, truncated object coordinates, fixed
  500-unit lower range, and computed upper range. Eleven of 115 words emit
  directly from semantic C; 104 stale-checked relocation-aware rows normalize
  the compiler's persistent scheduling displacement and register allocation.
- The linked and retail spans share SHA-256
  `f082d41b929c07fc57b6645669c3e923b7ff3a20be2696b0d2379e0a26ffce7d`.
  Totals are **3,123 / 5,457 (57.23%)** overall and
  **440 / 488 (90.16%)** in Init. See
  [Working Note 624](WORKING_NOTES/624-init-object-audio-dispatch-match-20261001.md).

### Init DMA page-cache helper byte-matched

- `func_100097CC` replaces its zero-return placeholder with the recovered
  active-page scan, cache-hit timestamp refresh, free-node allocation, and
  doubly linked active/free-list maintenance.
- A cache miss aligns the device address after retaining its low bit, stamps
  the 0x800-byte page with the current frame, claims one of 32 DMA message
  slots, starts `osPiStartDma`, and returns the physical DRAM address with the
  retained bit restored. Thirty-five of 109 words emit directly from semantic
  C; 74 stale-checked relocation-aware rows normalize compiler allocation and
  scheduling.
- The linked and retail spans share SHA-256
  `64c77129d302ef6d7adfd48564394809ef11918a2c59289cadfe7a162ba5b0c5`.
  Totals are **3,122 / 5,457 (57.21%)** overall and
  **439 / 488 (89.96%)** in Init. See
  [Working Note 623](WORKING_NOTES/623-init-dma-page-cache-helper-match-20261001.md).

### Init nearest-anchor forwarder byte-matched

- `func_1000F6B8` replaces its zero-return placeholder with the recovered
  nearest-anchor scan and the complete twelve-argument `func_1000A420`
  forwarding call.
- The semantic C recovers the signed 16-bit coordinates, unsigned squared-
  distance comparison, retained nearest relative vector, zero-count path,
  secondary relative vector, packed output pointer, and returned result.
  Sixty-eight stale-checked rows normalize 69 compiler-only allocation and
  scheduling words; 36 of the 105 retail words emit directly from C.
- The linked and retail spans share SHA-256
  `a41ddca24f43504374daf24585eb0bc8b865ffb36960baf9dc2ce8296df570bd`.
  Totals are **3,121 / 5,457 (57.19%)** overall and
  **438 / 488 (89.75%)** in Init. See
  [Working Note 622](WORKING_NOTES/622-init-nearest-anchor-forwarder-match-20261001.md).

### Init audio thread loop byte-matched

- `func_10009400` restores the message-driven audio thread: it receives
  scheduler messages, runs the two-frame submission cycle, captures the audio
  completion token after the first successful frame, and handles both
  terminal message types.
- Shutdown now closes the audio manager and enters retail's permanent receive
  loop. The recovered semantic C has retail's 104-word extent and branch
  topology. Twenty-seven stale-checked guards normalize compiler-only stack,
  saved-register, and close-schedule differences.
- The linked and retail spans share SHA-256
  `2a41b5bdbbeefb67b41d391642d2911785132b61f5f7be1a10bc9d3dda894e94`.
  Totals are **3,120 / 5,457 (57.17%)** overall and
  **437 / 488 (89.55%)** in Init. See
  [Working Note 621](WORKING_NOTES/621-init-audio-thread-loop-match-20261001.md).

## 2026-09-30

### Init controller-pak write transaction byte-matched

- `__osContRamWrite` now restores Conker's 16-word PIF RAM initialization and
  status clear before each controller-pak readback attempt.
- Keeping the extracted channel error in `ret` removes a redundant SDK
  reassignment and recovers retail's exact 140-word control flow. All words
  emit directly from C with no guards, insertions, or omissions.
- The linked and retail spans share SHA-256
  `dee476f995e4d64d1d057744683116e6245a537352bd0740fc1a74e405c33adc`.
  Totals are **3,119 / 5,457 (57.16%)** overall and
  **436 / 488 (89.34%)** in Init. See
  [Working Note 620](WORKING_NOTES/620-init-controller-pak-write-transaction-match-20260930.md).

### Init audio-record cleanup and dispatch byte-matched

- `func_1000E17C` restores three passes over the twelve-record audio pool:
  finished eligible records are invalidated, stale secondary links are
  cleared, and active eligible identifiers are dispatched through
  `func_1000DE1C`.
- The recovered C has retail's 94-word extent and control flow. Eighteen
  stale-checked replacements normalize a closed register-allocation and
  address-completion schedule; five relocation-only guards preserve the
  three independent record-pool address lifetimes.
- The linked and retail spans share SHA-256
  `a3fd280d56d3bd1bdabfb0dd492979c232b8fc91404eca3957b50a24d81bfdc5`.
  Totals are **3,118 / 5,457 (57.14%)** overall and
  **435 / 488 (89.14%)** in Init. See
  [Working Note 619](WORKING_NOTES/619-init-audio-record-cleanup-dispatch-match-20260930.md).

### Init controller-pak write packet builder byte-matched

- `__osPackRamWriteData` now clears all 16 PIF RAM words before constructing
  the write request, matching Conker's extension to the canonical SDK body.
- Restoring canonical `*ptr++` channel-prefix writes recovers the final two
  branch-adjacent stores. All 96 retail words emit directly from C with no
  guards, insertions, or omissions.
- The linked and retail spans share SHA-256
  `cdf63a7878b35bab75e7439410fc7835571158ed2351f8ed0f75196b8b429087`.
  Totals are **3,117 / 5,457 (57.12%)** overall and
  **434 / 488 (88.93%)** in Init. See
  [Working Note 618](WORKING_NOTES/618-init-controller-pak-write-packet-builder-match-20260930.md).

### Init VI manager thread byte-matched

- `viMgrMain` restores the canonical SDK retrace loop, including context
  swaps, client notification, timer interrupts, interrupt counting, and
  64-bit time accumulation.
- All 102 retail opcodes emit directly from C. Ten stale-checked
  relocation-only guards bind the discarded function-local `retrace` static
  to retail `D_80037E30` without rewriting an instruction.
- The linked and retail spans share SHA-256
  `5856a698d1f28b707e9768ffe365d925abf9bd588699baec40447970e450a7de`.
  Totals are **3,116 / 5,457 (57.10%)** overall and
  **433 / 488 (88.73%)** in Init. See
  [Working Note 617](WORKING_NOTES/617-init-vi-manager-main-match-20260930.md).

### Init VI manager creation byte-matched

- `osCreateViManager` restores timer-service initialization, VI and counter
  messages, temporary priority handling, manager state, interrupt protection,
  and VI thread startup from the canonical SDK body.
- All 94 retail words emit directly from C with no word guards. Expressing the
  stack top from the adjacent message-buffer base preserves retail's distinct
  stack and queue address materializations despite their shared address.
- The linked and retail spans share SHA-256
  `a2bae43e3aad95cb561f2ee54b5d0a09c7a71b1dd254f71dce0c90b0e0dbbabd`.
  Totals are **3,115 / 5,457 (57.08%)** overall and
  **432 / 488 (88.52%)** in Init. See
  [Working Note 616](WORKING_NOTES/616-init-create-vi-manager-match-20260930.md).

### Init channel attachment byte-matched

- `func_1000B3D4` restores direct parent replacement, the three-slot channel
  allocation scan, and retirement of an idle child before replacement.
- Sixty-five of 93 retail words emit directly from C. Twenty-eight
  stale-checked replacement guards normalize three closed register-allocation
  cycles without moving or rewriting relocations.
- The linked and retail spans share SHA-256
  `94732e1b11f4b548bf993a41315257f5d00810379afd568f162a694c10ada44f`.
  Totals are **3,114 / 5,457 (57.06%)** overall and
  **431 / 488 (88.32%)** in Init. See
  [Working Note 615](WORKING_NOTES/615-init-channel-attachment-match-20260930.md).

### Init audio-DMA cleanup byte-matched

- `func_100099BC` restores completion-queue draining, generation-expiry
  checks, active-list unlinking, free-list insertion, and generation advance.
- Thirty-five of 92 retail words remain direct compiler output. Fifty-six
  replacement guards and one checked insertion normalize IDO's closed
  register-allocation and branch-scheduling differences.
- The linked and retail spans share SHA-256
  `9d14cf21f945591ae4e069646be433e9d22ac916927177d502fd0e7cce73622d`.
  Totals are **3,113 / 5,457 (57.05%)** overall and
  **430 / 488 (88.11%)** in Init. See
  [Working Note 614](WORKING_NOTES/614-init-audio-dma-cleanup-match-20260930.md).

### Init deferred-record compactor byte-matched

- `func_10011310` restores the pending-record delay countdown, matching
  resource-slot release, survivor count, and in-place four-byte compaction.
- Twenty-six of 91 retail words remain direct compiler output. Fifty-five
  replacement guards and ten checked insertions normalize IDO's closed
  register-allocation and address-rematerialization differences.
- The linked and retail spans share SHA-256
  `828a7eefa3237b51cd4f4828947fcfdee4611afc4a363d0e04d2506cbcfc4d9a`.
  Totals are **3,112 / 5,457 (57.03%)** overall and
  **429 / 488 (87.91%)** in Init. See
  [Working Note 613](WORKING_NOTES/613-init-deferred-record-compactor-match-20260930.md).

### Init channel-state initializer byte-matched

- `func_1000E934` restores the paired 16-entry channel-table fills, channel
  reset call, four per-channel state clears, record-table clear, and all 12
  `-1` sentinels.
- Fifty-nine of 88 words emit directly from semantic C. Twenty-nine
  stale-checked guards normalize only compiler scheduling, including six
  moved low-address relocations; no words are inserted or omitted.
- The linked and retail spans share SHA-256
  `58dda18e23f8c45a173a8db40555b9ece0d587592ff475e28a82a03c5f3e866c`.
  Totals are **3,111 / 5,457 (57.01%)** overall and
  **428 / 488 (87.70%)** in Init. See
  [Working Note 612](WORKING_NOTES/612-init-channel-state-initializer-match-20260930.md).

### Init controller-pak read packet builder byte-matched

- `__osPackRamReadData` restores Conker's opening 16-word PIF RAM clear before
  the canonical SDK read-request packet construction.
- Establishing the PIF pointer before a signed literal-16 loop reproduces all
  91 retail words directly from C and retained padding. No expected-word
  guards, insertions, or omissions are used.
- The linked and retail spans share SHA-256
  `9cb0dfb5ca12bc56ef6b89440bad89924d74a4cf6b4957f1236eb3cd03c40400`.
  Totals are **3,110 / 5,457 (56.99%)** overall and
  **427 / 488 (87.50%)** in Init. See
  [Working Note 611](WORKING_NOTES/611-init-controller-pak-read-packet-builder-match-20260930.md).

### Init pending note-end query byte-matched

- `func_1001ADA4` restores the SDK allocated-event scan, accumulated event
  time, voice-specific note-end decision, and allocated-to-free-list transfer.
- Seventy-six of 97 words emit directly from typed C. Twenty stale-checked
  replacement guards and one checked insertion normalize four branch offsets
  and the closed relink/return tail; no words are omitted.
- The linked and retail spans share SHA-256
  `a23783a71d1e0d4ee84491f53a75f82cde29c37c044fb29f0d21dd2745f0874e`.
  Totals are **3,109 / 5,457 (56.97%)** overall and
  **426 / 488 (87.30%)** in Init. See
  [Working Note 610](WORKING_NOTES/610-init-pending-note-end-query-match-20260930.md).

### Init nearest-listener spatial query byte-matched

- `func_100114D0` restores the inclusive listener-table scan, unsigned
  squared-distance selection, relative-coordinate setup for `func_1000A420`,
  and fixed-point output scale.
- Thirty-five of 85 words emit directly from semantic C and retained padding.
  Fifty stale-checked guards normalize one closed register allocation and call
  schedule; no instructions are inserted or removed.
- The linked and retail spans share SHA-256
  `eb9ee13fc4faf8a4bbbf4cfffbff5e90d51e1bd6d88e9c403f52ba91c0b67818`.
  Totals are **3,108 / 5,457 (56.95%)** overall and
  **425 / 488 (87.09%)** in Init. See
  [Working Note 609](WORKING_NOTES/609-init-nearest-listener-spatial-query-match-20260930.md).

### Init planar direction encoder byte-matched

- `func_1000B060` restores vector normalization, signed-angle folding,
  caller offset application, range-band folding, and encoded return
  construction.
- Fifty-eight of 84 words emit directly from semantic C and retained padding.
  Twenty-six stale-checked guards normalize one closed FP/integer allocation
  and schedule; no instructions are inserted or removed.
- The linked and retail spans share SHA-256
  `d12c643410bab7b05ab9364b986eac6839ee1300617681239c6b5299fba2879a`.
  Totals are **3,107 / 5,457 (56.94%)** overall and
  **424 / 488 (86.89%)** in Init. See
  [Working Note 608](WORKING_NOTES/608-init-planar-direction-encoder-match-20260930.md).

### Init nonrepeating random selector byte-matched

- `func_1000F568` restores bounded random selection, the per-record
  availability mask, cyclic fallback to the next available choice, and mask
  replenishment after exhaustion.
- Seventy-three of 84 words emit directly from semantic C. Eleven
  stale-checked guards normalize five shifted branches, five commutative
  operand orders, and one optimized-away raw-mask reset assignment.
- The linked and retail spans share SHA-256
  `f669a659ee095e77b72fdefe06d91f096ad7ed2b43b1552eda234db999bfeb44`.
  Totals are **3,106 / 5,457 (56.92%)** overall and
  **423 / 488 (86.68%)** in Init. See
  [Working Note 607](WORKING_NOTES/607-init-nonrepeating-random-selector-match-20260930.md).

### Init framebuffer task dispatcher byte-matched

- `func_10004DB0` restores the nonblocking graphics-task receive, current and
  next VI framebuffer gates, countdown update, submission retry, and phase-six
  completion dispatch.
- Seventy-five of 84 words emit directly from semantic C. Nine stale-checked
  guards normalize the remaining branch/register schedule and insert one
  address materialization; the complete tail otherwise emits directly.
- The linked and retail spans share SHA-256
  `86b7fab90235a558ee8af0ac506a9eed2d888e0bbaef406bb763a1f3a4d66f74`.
  Totals are **3,105 / 5,457 (56.90%)** overall and
  **422 / 488 (86.48%)** in Init. See
  [Working Note 606](WORKING_NOTES/606-init-framebuffer-task-dispatcher-match-20260930.md).

### Init spatial-volume callback byte-matched

- `func_1000C7E8` restores mode-specific resource setup, active-state
  selection, and a clamped distance-based channel value.
- Thirty-three of 83 words emit directly from semantic C and retained slot
  padding. Fifty stale-checked guards normalize one closed IDO
  floating-point allocation and instruction schedule; no instructions are
  inserted or removed.
- The linked and retail spans share SHA-256
  `8b0ef26f08fc4e4ac97da787b65fb1e3377e5d9dfd7beaf356e25550c14c6423`.
  Totals are **3,104 / 5,457 (56.88%)** overall and
  **421 / 488 (86.27%)** in Init. See
  [Working Note 605](WORKING_NOTES/605-init-spatial-volume-callback-match-20260930.md).

### Init chunked PI DMA reader byte-matched

- `func_100046E4` selects a PI completion queue from the running thread,
  invalidates the destination cache, and reads in synchronous chunks no
  larger than `0x14000` bytes.
- Seventy of 74 words emit directly from typed semantic C. Four stale-checked
  guards normalize only the frame allocation, two message-local addresses,
  and frame release; no instructions are inserted or removed.
- The linked and retail spans share SHA-256
  `3e86429dbeb207960589ce8b2f3305a853d406b5fc5e3643be4ad4e4c0b95e40`.
  Totals are **3,103 / 5,457 (56.86%)** overall and
  **420 / 488 (86.07%)** in Init. See
  [Working Note 604](WORKING_NOTES/604-init-chunked-pi-dma-reader-match-20260930.md).

### Init active-entry mode dispatcher byte-matched

- `func_1000E2F4` scans the three active entries, selects the channel stop or
  release path from the incoming mode and metadata flag, and stores that mode
  globally.
- Fifty-eight of 70 words emit directly from semantic C. Twelve stale-checked
  guards normalize one closed, non-relocating metadata-test register cycle;
  no instructions are inserted or removed.
- The linked and retail spans share SHA-256
  `9c7c8f921694c0fed12dc7ca5c311ccc242df93cb2ad3d55e9ad76300ff911d0`.
  Totals are **3,102 / 5,457 (56.84%)** overall and
  **419 / 488 (85.86%)** in Init. See
  [Working Note 603](WORKING_NOTES/603-init-active-entry-mode-dispatcher-match-20260930.md).

### Init entry mask value updater byte-matched

- `func_1000E46C` resolves an entry, saturates its percentage to a byte,
  dispatches channel-backed entries, and updates the selected value bytes of
  unbound entries.
- All 71 words emit directly from semantic C. Reusing the incoming percentage
  and signed mask parameters preserves retail's saved-register lifetimes, so
  no expected-word guards or compiler-profile changes are required.
- The linked and retail spans share SHA-256
  `1e96762e70a9a2b3a72c015cdb62fa7ac620a2e7ba751cee8f29b0bf22a2a686`.
  Totals are **3,101 / 5,457 (56.83%)** overall and
  **418 / 488 (85.66%)** in Init. See
  [Working Note 602](WORKING_NOTES/602-init-entry-mask-value-updater-match-20260930.md).

### Init record mask filter byte-matched

- `func_1000CDA0` validates its typed record and active handle, conditionally
  sets flag bits zero and one, and reports whether the incoming low-byte mask
  is fully cleared by the resulting flag complement.
- Forty-nine of 67 words emit directly from recovered C. Sixteen stale-checked
  replacements and two guarded insertions normalize the local-slot and
  redundant default-return schedule.
- The linked and retail spans share SHA-256
  `164c1732fc0ffe8c739238c8e3a4d813fc695781a41d8a5d3bbc5c9a65d92c0e`.
  Totals are **3,100 / 5,457 (56.81%)** overall and
  **417 / 488 (85.45%)** in Init. See
  [Working Note 601](WORKING_NOTES/601-init-record-mask-filter-match-20260930.md).

### Init dual-framebuffer clear byte-matched

- `func_10003ACC` packs its RGB inputs as RGBA5551, clears framebuffer zero
  with a scalar loop, and clears framebuffer one with a remainder loop plus a
  four-pixel bulk loop.
- The recovered semantic C uses the retail no-unroll object profile.
  Fifty-seven stale-checked guards normalize IDO's closed register allocation
  and loop schedule across the 65-word slot.
- The linked and retail spans share SHA-256
  `90aebf408fc334f16c47bd3141064d4bb1434fd80b2e9a8aa9581b524559822f`.
  Totals are **3,099 / 5,457 (56.79%)** overall and
  **416 / 488 (85.25%)** in Init. See
  [Working Note 600](WORKING_NOTES/600-init-dual-framebuffer-clear-match-20260930.md).

### Init actor sound dispatcher byte-matched

- `func_10010630` ignores inactive actors, dispatches camera-owned sounds
  through `func_10010F30`, and otherwise submits a positional sound record
  with truncated actor coordinates and the actor refresh callback.
- The semantic C restores the complete two-path behavior. Fifty-four
  stale-checked guards preserve retail's saved `s0`/`s1` lifetimes, argument
  setup, moved callback-address relocation pair, and call schedule.
- The linked and retail spans share SHA-256
  `3bec2ba128af0a55c7bb606f06d3d3cca59c83994bae3efe841627a5854c2feb`.
  Totals are **3,098 / 5,457 (56.77%)** overall and
  **415 / 488 (85.04%)** in Init. See
  [Working Note 599](WORKING_NOTES/599-init-actor-sound-dispatcher-match-20260930.md).

### Init spatial channel-value updater byte-matched

- `func_1000C934` selects a flag-dependent limit, optionally subtracts a
  masked spatial query in level `0x37`, updates channel `0x54` when the pending
  value differs, and returns the value with bit 31 set.
- Thirty-nine of 57 words emit directly from the recovered semantic C.
  Eighteen stale-checked guards preserve one non-relocating value-register,
  branch-delay, and epilogue scheduling cluster.
- The linked and retail spans share SHA-256
  `4e561733cb18a6f8daf394a820982539e2d912471df045a9ef3207798cbc4886`.
  Totals are **3,097 / 5,457 (56.75%)** overall and
  **414 / 488 (84.84%)** in Init. See
  [Working Note 598](WORKING_NOTES/598-init-spatial-channel-value-updater-match-20260930.md).

### Init virtual task-address converter byte-matched

- `_VirtualToPhysicalTask` copies an incoming `OSTask` into the fixed temporary
  task and converts seven non-null task pointers to physical addresses.
- The repository-local SDK body emits all 68 retail words directly under the
  existing `sptask.c` profile. No expected-word guards or profile changes are
  required, and the adjacent task-load/start functions remain byte-exact.
- The linked and retail spans share SHA-256
  `39bdaef9aafe9186372b8b1b14301f33e467f2108ea4521d3e140aad7d45306f`.
  Totals are **3,096 / 5,457 (56.73%)** overall and
  **413 / 488 (84.63%)** in Init. See
  [Working Note 597](WORKING_NOTES/597-init-virtual-task-address-converter-match-20260930.md).

### Init Leo disk initializer byte-matched

- `osLeoDiskInit` configures the 64DD PI handle, writes the domain-two timing
  registers, clears transfer state, and links the handle into the PI table
  while interrupts are disabled.
- The recovered SDK body uses the retail `-O1` profile. Seven stale-checked
  guards normalize one adjacent-field scheduling cluster, omit a redundant
  handle-address load, and preserve the 60-word retail extent.
- The linked and retail spans share SHA-256
  `7d204edfe2419d1dc472aaba89b7665d3ca50a8969dc9c573e26338dceb566bc`.
  Totals are **3,095 / 5,457 (56.72%)** overall and
  **412 / 488 (84.43%)** in Init. See
  [Working Note 596](WORKING_NOTES/596-init-leo-disk-initializer-match-20260930.md).

### Init Leo resume helper pair byte-matched

- `__osLeoAbnormalResume` restores disk buffer-manager state, clears the PI
  interrupt, and restores the global PI interrupt mask. `__osLeoResume`
  appends the PI event message and wakes a waiting queue thread.
- Both helpers emit directly from repository-local libultra C under the stock
  SDK `-O1` profile. The abnormal helper preserves retail's IO-busy-only
  polling mask; no word guards are required.
- The linked and retail spans share SHA-256
  `500e2acc2a1a8684d801922f996043336aa5ddb2a54566badb22d54f4dd60a14`
  and `ebe24919f2d63e916824fb1bec7ffbb078a46070afe16b3420a1a5c3452b2cbe`.
  Totals are **3,094 / 5,457 (56.70%)** overall and
  **411 / 488 (84.22%)** in Init. See
  [Working Note 595](WORKING_NOTES/595-init-leo-resume-helper-pair-match-20260930.md).

### Init halfword-table selector byte-matched

- `func_10011EB8` maps an input to a five-pair table row, optionally computes
  the multiplayer scale, and resolves selectors at least two through
  `func_1000F568`.
- The semantic C emits the full routine in retail order. Two bounded guards
  restore redundant input copies and move the existing call relocation,
  consuming two trailing padding words.
- The linked and retail spans share SHA-256
  `4b4a026b8a28e4703983b808e69359a8682c0b7577a6b35144145a2c0cf6a16f`.
  Totals are **3,092 / 5,457 (56.66%)** overall and
  **409 / 488 (83.81%)** in Init. See
  [Working Note 594](WORKING_NOTES/594-init-halfword-table-selector-match-20260930.md).

### Init single-node release recycler byte-matched

- `func_10009BE4` returns a node's retained value, removes it from the active
  list, inserts it into the reusable list, and preserves the odd-pointer
  sentinel callback path.
- Twenty-eight of 54 words emit directly from semantic C. Twenty-six
  stale-checked guards preserve the manager, sentinel, and reusable-list
  schedules, including the moved relocations.
- The linked and retail spans share SHA-256
  `667204c47707c5e69f2314fde2be2e4f4afb0075e1e053824489d3e381190a67`.
  Totals are **3,091 / 5,457 (56.64%)** overall and
  **408 / 488 (83.61%)** in Init. See
  [Working Note 593](WORKING_NOTES/593-init-single-node-release-recycler-match-20260930.md).

### Init packed-timer callback byte-matched

- `func_1000EDA0` refreshes a packed high half, decrements its signed low-half
  timer, and dispatches the record through `func_10010630` on expiry.
- Forty-one of 52 words emit directly from semantic C. Eleven stale-checked
  guards preserve one closed expiry-path temporary-register rotation.
- The linked and retail spans share SHA-256
  `886bdb392b620bfbe0696c157098759fb4be73d307ceaabcf1ab4c3e9bd3f72b`.
  Totals are **3,090 / 5,457 (56.62%)** overall and
  **407 / 488 (83.40%)** in Init. See
  [Working Note 592](WORKING_NOTES/592-init-packed-timer-callback-match-20260930.md).

### Init mode-flag dispatch wrapper byte-matched

- `func_1000CAE4` updates two independent state bits across global mode
  `0x42`, event `0x58`, a timed transition, and one fixed low-byte dispatch.
- All 49 words emit directly from semantic C. Its frame, saved register,
  argument homes, branches, delay slots, and calls require no guards.
- The linked and retail spans share SHA-256
  `aefe1f79eec76c20160be8b0aa7962cd15f8375113ec490913b5bf3240b586ac`.
  Totals are **3,089 / 5,457 (56.61%)** overall and
  **406 / 488 (83.20%)** in Init. See
  [Working Note 591](WORKING_NOTES/591-init-mode-flag-dispatch-wrapper-match-20260930.md).

### Init actor-coordinate refresh callback byte-matched

- `func_1000EE70` validates an event record's actor and caller gate, refreshes
  the orientation class and three truncated coordinates for a matching actor,
  and otherwise performs the original handle-liveness fallback.
- Thirty-four of 52 words emit directly from semantic C. Eighteen
  stale-checked guards preserve one closed temporary-register rotation.
- The linked and retail spans share SHA-256
  `529b4111534c32467e43c8889c4f475252494d74e82022ca94bbcae6090cc1ad`.
  Totals are **3,088 / 5,457 (56.59%)** overall and
  **405 / 488 (82.99%)** in Init. See
  [Working Note 590](WORKING_NOTES/590-init-actor-coordinate-refresh-callback-match-20260930.md).

### Init released-node recycler byte-matched

- `func_1000A348` releases inactive active-list records, repairs both list
  directions, and splices each record into the reusable list.
- Thirty-five of 54 words emit directly from semantic C. Nineteen
  stale-checked guards preserve the closed manager-register and free-list
  splice schedule.
- The linked and retail spans share SHA-256
  `3b03c2654be6fe46335aeccddb64cca509d8edddb5f980c04918b85486affe7a`.
  Totals are **3,087 / 5,457 (56.57%)** overall and
  **404 / 488 (82.79%)** in Init. See
  [Working Note 589](WORKING_NOTES/589-init-released-node-recycler-match-20260930.md).

### Init handwritten bzero restored

- `bzero` now uses the original handwritten libultra implementation instead
  of the approximate byte-at-a-time C loop.
- Its unaligned prefix, 32-byte block loop, word tail, and byte tail match all
  40 retail words without expected-word guards.
- The linked and retail spans share SHA-256
  `6cb49ba97859396e62e39990cd9a31a7a775d8e8b5618695b03027823a7b2863`.
  The row is now correctly assembly-classified; exact-C totals are
  **3,086 / 5,457 (56.55%)** overall and **403 / 488 (82.58%)** in Init. See
  [Working Note 588](WORKING_NOTES/588-init-handwritten-bzero-restoration-20260930.md).

### Init fixed-point parameter wrapper byte-matched

- `func_10010E78` scales an unsigned magnitude through `func_1000F6B8`, then
  dispatches the nonzero result with the returned packed parameter split into
  its low seven bits and high-bit flags.
- Forty-five of 46 words emit directly from semantic C. One stale-checked
  guard preserves retail's commutative fixed-point multiply operand order.
- The linked and retail spans share SHA-256
  `593c63fd1ac1b69d9efa566fd99515abc6d72ae3a4fe946b892928752c35e6bb`.
  Totals are **3,086 / 5,458 (56.54%)** overall and
  **403 / 489 (82.41%)** in Init. See
  [Working Note 587](WORKING_NOTES/587-init-fixed-point-parameter-wrapper-match-20260930.md).

### Init channel level/mask updater byte-matched

- `func_1000E588` maps a clamped percentage to an 8-bit live-channel level or
  sets/clears the requested mask in an inactive channel record.
- Its complete 51-word body emits directly from semantic C with no guards.
- The linked and retail spans share SHA-256
  `2ad78a07cd78b178c8b0cbc6194b6876624d7175951a0c2a007fe05a62e55e88`.
  Totals are **3,085 / 5,458 (56.52%)** overall and
  **402 / 489 (82.21%)** in Init. See
  [Working Note 586](WORKING_NOTES/586-init-channel-level-mask-updater-match-20260930.md).

### Init channel-transition updater byte-matched

- `func_1000DF68` updates a channel target, optionally snaps and refreshes the
  active channel, and computes an absolute per-step transition amount.
- Forty-seven of 59 words emit directly from semantic C. Twelve stale-checked
  guards preserve retail's closed clamp/store/epilogue schedule.
- The linked and retail spans share SHA-256
  `e3f6789eb12fdf89b984522ef3520b5996babbbae4f94646ea8610ff45011f9a`.
  Totals are **3,084 / 5,458 (56.50%)** overall and
  **401 / 489 (82.00%)** in Init. See
  [Working Note 585](WORKING_NOTES/585-init-channel-transition-updater-match-20260930.md).

### Init record cleanup byte-matched

- `func_1000DEC4` scans the 12-entry record table, releases stale owner-table
  links, resets inactive records, and clears each record's final four bytes.
- Its recovered combined 32-bit tail clear and non-prototype state-query
  declaration emit all 41 words directly from semantic C with no guards.
- The linked and retail spans share SHA-256
  `01b0138764c7dd80ffaa2bdfa297452223ede4057776661b7927b7ef467dbb0c`.
  Totals are **3,083 / 5,458 (56.49%)** overall and
  **400 / 489 (81.80%)** in Init. See
  [Working Note 584](WORKING_NOTES/584-init-record-cleanup-match-20260930.md).

### Init identifier dispatcher byte-matched

- `func_1000DE1C` masks an incoming identifier, expands identifier zero
  through `func_1000B548`, and dispatches each positive result through
  `func_1000D96C`.
- Forty of 42 words emit directly from semantic C. Two stale-checked guards
  preserve retail's lower local-array placement.
- The linked and retail spans share SHA-256
  `10798837035d04b29314204b925729e8be19c77d5ef415a9eacf8f24bfad8bff`.
  Totals are **3,082 / 5,458 (56.47%)** overall and
  **399 / 489 (81.60%)** in Init. See
  [Working Note 583](WORKING_NOTES/583-init-identifier-dispatcher-match-20260930.md).

### Init handwritten osSetIntMask restored

- `osSetIntMask` is restored from an empty C placeholder to its original
  handwritten CP0/MI interrupt-mask routine.
- The complete 160-byte slot is independently byte-exact, including all data
  relocations, the MI mask-table lookup, CP0 status write, and hazard nops.
- The rebuilt and retail spans share SHA-256
  `4f77fb7a5c63f84cc4f19456f3608deb338d495a7c560abf9cb4a8548f7275b1`.
  The row is now correctly classified as raw assembly, leaving **398 / 489
  (81.39%)** byte-exact Init C rows and 91 different C rows. See
  [Working Note 582](WORKING_NOTES/582-init-handwritten-setintmask-restoration-20260930.md).

### Init handwritten osInvalDCache restored

- `osInvalDCache` is restored from an empty C placeholder to its original
  43-word cache body plus one retail padding word.
- The complete 176-byte slot is independently byte-exact and retains the
  original range checks, endpoint handling, cache operations, and fallback.
- The rebuilt and retail spans share SHA-256
  `7ea4c6bffed307fe915ab8ef0ae37d86482e17b132eb99598f82ad5cbca40a71`.
  The row is now correctly classified as raw assembly, leaving **398 / 490
  (81.22%)** byte-exact Init C rows and 92 different C rows. See
  [Working Note 581](WORKING_NOTES/581-init-handwritten-invaldcache-restoration-20260930.md).

### Init handwritten osMapTLB restored

- `osMapTLB` is restored from an empty C placeholder to its original 45-word
  CP0/TLB body plus three retail padding words.
- The complete 192-byte slot is independently byte-exact and retains the
  original `mfc0`, `mtc0`, `tlbwi`, and hazard-nop sequence.
- The rebuilt and retail spans share SHA-256
  `df58b390004db1a7de5265449eafe8115ecaf81acad24b5471290157b28cc85e`.
  The row is now correctly classified as raw assembly, leaving **398 / 491
  (81.06%)** byte-exact Init C rows and 93 different C rows. See
  [Working Note 580](WORKING_NOTES/580-init-handwritten-maptlb-restoration-20260930.md).

### Game event-0x3E owner dispatcher byte-matched

- `func_150F7310` handles event `0x3E` by comparing incoming and object owner
  identities and destroying the object on either match. Other events forward
  through `func_15149514`.
- Twenty-three of 35 words emit directly from semantic C. Twelve stale-checked
  guards normalize the closed identity-register cycle and one load schedule.
- The linked and retail spans share SHA-256
  `48c08c6129179c91ef5a8cfcfc843012e4ec73ee2fa9353bc1442508c71b4969`.
  Totals are **3,081 / 5,461 (56.42%)** overall and
  **2,502 / 4,788 (52.26%)** in Game. See
  [Working Note 579](WORKING_NOTES/579-game-event-3e-owner-dispatcher-match-20260930.md).

### Game command-0x5C owner-payload allocator byte-matched

- `func_150F2C8C` builds a 16-byte owner payload, allocates command `0x5C`
  with allocator argument `0x44`, and copies the payload into a successful
  allocation.
- All 34 words and both call relocations emit directly from semantic C with
  no expected-word guards.
- The linked and retail spans share SHA-256
  `4c4e9b52574cae5bba65ecb5a0911f8b0ec9895325756631c3dc9a13157fe95b`.
  Totals are **3,080 / 5,461 (56.40%)** overall and
  **2,501 / 4,788 (52.23%)** in Game. See
  [Working Note 578](WORKING_NOTES/578-game-command-5c-owner-payload-allocator-match-20260930.md).

### Game object-entry matrix builder byte-matched

- `func_150F2518` selects an object entry, builds its rotation matrix, writes
  its XYZ translation, and converts it into the current matrix slot.
- Twenty-seven of 34 words emit directly from semantic C. Seven stale-checked
  guards normalize one closed address-register cycle and preserve both
  `D_800BE9C0` relocations.
- The linked and retail spans share SHA-256
  `0cc68b8a90190392cd5688cf29f8ef05a9496b0b10e7a79980b34d6efdfee906`.
  Totals are **3,079 / 5,461 (56.38%)** overall and
  **2,500 / 4,788 (52.21%)** in Game. See
  [Working Note 577](WORKING_NOTES/577-game-object-entry-matrix-builder-match-20260930.md).

### Game owner-event dispatcher byte-matched

- `func_150F15F8` handles event `0x43` by comparing owner word and identity
  byte fields and destroying a matching object. Other events forward the
  owner record and object fields to `func_15149514`.
- Twenty-six of 35 words emit directly from semantic C. Nine stale-checked
  guards normalize one closed owner/object identity-register cycle.
- The linked and retail spans share SHA-256
  `3680ee0fd4268a962063b7b48e7d229d1e99000861d24f013ef5f200a18c18e1`.
  Totals are **3,078 / 5,461 (56.36%)** overall and
  **2,499 / 4,788 (52.19%)** in Game. See
  [Working Note 576](WORKING_NOTES/576-game-owner-event-dispatcher-match-20260930.md).

### Game command-0x38 owner-payload allocator byte-matched

- `func_150D5440` builds a 12-byte owner payload, allocates command `0x38`
  with subtype `0x28`, and copies the payload into a successful allocation.
- All 34 words emit directly from semantic C with no guards. The linked and
  retail spans share SHA-256
  `797214ab3db1016376fa9239eb154a0fe954d86f45ae7fbe845a7ba3e71f34fa`.
- Totals are **3,077 / 5,461 (56.34%)** overall and
  **2,498 / 4,788 (52.17%)** in Game. See
  [Working Note 575](WORKING_NOTES/575-game-command-38-owner-payload-allocator-match-20260930.md).

### Game fixed-point coordinate interpolator byte-matched

- `func_150B73F0` computes two signed 16.16 fixed-point interpolations between
  halfword endpoints and stores the resulting X/Y coordinates as floats.
- Thirteen of 37 words emit directly from semantic C. Twenty-four stale-checked
  guards normalize one closed register-allocation cycle; instruction order,
  divide traps, immediates, float stores, and control flow already match.
- The linked and retail spans share SHA-256
  `5ff8bb8bebad3257d3ce7d34f41d03f4517bd0b6c4e0cf9afd7692eeb9c41e18`.
  Totals are **3,076 / 5,461 (56.33%)** overall and
  **2,497 / 4,788 (52.15%)** in Game. See
  [Working Note 574](WORKING_NOTES/574-game-fixed-point-coordinate-interpolator-match-20260930.md).

### Game owner-payload allocator byte-matched

- `func_150B0C58` builds a 12-byte payload containing its owner pointer,
  owner ID byte, and zero float, then allocates command `0x58` with subtype
  `0x43` and copies the payload into a successful allocation.
- All 34 words emit directly from semantic C with no guards. The linked and
  retail spans share SHA-256
  `ac0b02a319621df6c63c1acb70a87ca4951000e4a82f9cd3b68178ad0abe2ba2`.
- Totals are **3,075 / 5,461 (56.31%)** overall and
  **2,496 / 4,788 (52.13%)** in Game. See
  [Working Note 573](WORKING_NOTES/573-game-owner-payload-allocator-match-20260930.md).

### Game random-duration selector byte-matched

- `func_1507F4C0` selects mode-dependent random duration ranges and returns
  zero for nonzero modes while global state `0x31` is active.
- Twenty-nine of 35 words emit directly from semantic C. Six stale-checked
  guards preserve retail's frame and two post-call stack slots. The linked and
  retail spans share SHA-256
  `55ec7967c98d5eabe2b7d0293f09b16178590c39b8639308c777852b2ed1d4d2`.
- Totals are **3,074 / 5,461 (56.29%)** overall and
  **2,495 / 4,788 (52.11%)** in Game. See
  [Working Note 572](WORKING_NOTES/572-game-random-duration-selector-match-20260930.md).

### Game scripted-position effect dispatcher byte-matched

- `func_15076768` now handles mode zero by forwarding the current actor to
  `func_15197A7C`. Mode one derives an effect descriptor and dispatches it at
  the actor's X/Z coordinates with a fixed Y coordinate of `-390.0f`.
- Thirty of 35 words emit directly from semantic C. Five stale-checked guards
  normalize one closed position-store/descriptor-address scheduling cycle.
  The linked and retail spans share SHA-256
  `d67a510fcc3d0c50ccfad8e060acdc820a3c1fb2ce8bfa38a1304ccf5c60429b`.
- Totals are **3,073 / 5,461 (56.27%)** overall and
  **2,494 / 4,788 (52.09%)** in Game. See
  [Working Note 571](WORKING_NOTES/571-game-scripted-position-effect-dispatch-match-20260930.md).

### Game byte-table index lookup byte-matched

- `func_15041480` now narrows its input to an unsigned byte, scans all 80
  entries of `D_800848D0` four at a time, and returns the matching index or 80.
- All 34 words emit directly from semantic C under an object-specific
  `-Wo,-loopunroll,0` profile. No expected-word guards are used. The linked
  and retail spans share SHA-256
  `dffbcfa8fd45b23a77815de868084b779498276451ac20ede147c70a42466fc1`.
- Totals are **3,072 / 5,461 (56.25%)** overall and
  **2,493 / 4,788 (52.07%)** in Game. See
  [Working Note 570](WORKING_NOTES/570-game-byte-table-index-lookup-match-20260930.md).

### Game table-record dispatcher byte-matched

- `func_15024130` now walks `D_800C3D50` in 12-byte record strides and calls
  `func_1502A8A0` once per entry with the record's word, byte, halfword, second
  word, and the shared dispatch argument.
- Thirty-two of 33 words emit directly from semantic C. One stale-checked,
  non-relocating guard preserves retail's commutative table-base addition
  operand order. The linked and retail spans share SHA-256
  `94b7a32ec40b961cc226a811d8b5e56961f489be88f3a66d0151e7a4aa3bbe50`.
- Totals are **3,071 / 5,461 (56.24%)** overall and
  **2,492 / 4,788 (52.05%)** in Game. See
  [Working Note 569](WORKING_NOTES/569-game-table-record-dispatch-match-20260930.md).

### Game signed-position effect dispatcher byte-matched

- `func_15013D38` now sets the source flag, converts three signed coordinates
  into a local float vector, defaults its stored dispatch value to one, and
  calls `func_151BE850` with retail's trailing arguments `(1, 0xFF, 1)`.
- Thirty-nine of 44 words emit directly from semantic C. Five stale-checked,
  non-relocating guards normalize one closed vector-address/call-constant
  setup cycle. The linked and retail spans share SHA-256
  `d8ddb22ea0408713dc0b53f28741dd3aefe9de2acb182b2f2f71ee34a63fa1ed`.
- Totals are **3,070 / 5,461 (56.22%)** overall and
  **2,491 / 4,788 (52.03%)** in Game. See
  [Working Note 568](WORKING_NOTES/568-game-signed-position-effect-dispatch-match-20260930.md).

### Handwritten Init TLB probe restored

- `__osProbeTLB` is restored from its false zero-return C placeholder to the
  original handwritten CP0/TLB implementation, preserving the EntryHi save,
  TLB probe/read hazards, page selection, valid-bit test, address translation,
  and EntryHi restore.
- Its complete 48-word, 192-byte slot independently matches retail, including
  two padding words. Both spans have SHA-256
  `349227b84b51cb246abaf9de4bf56eba78054d85575e1bfb09acfdb8d1bc0c28`.
- The exact-C numerator remains 3,069. Correcting the ownership denominator
  yields **3,069 / 5,461 (56.20%)** overall and
  **398 / 492 (80.89%)** in Init. See
  [Working Note 567](WORKING_NOTES/567-init-handwritten-probetlb-restoration-20260930.md).

### Game global mode-state updater byte-matched

- `func_151D66F0` now preserves the mode-6 availability gate, normalizes the
  selector when its mode argument is zero, updates the paired global state
  bytes, and releases the retained resource when the selector is disabled.
- All 34 words and their relocations emit directly from semantic C with no
  guard rows. The linked ELF and pristine decompressed retail spans share
  SHA-256 `891d28f56a54c034702efd5cd9fae345a6402c9b469fc259ab59040be46ca8a7`.
- Totals are **3,069 / 5,462 (56.19%)** overall and
  **2,490 / 4,788 (52.01%)** in Game. See
  [Working Note 566](WORKING_NOTES/566-game-global-mode-state-updater-match-20260930.md).

### Game midpoint-timestep integrator byte-matched

- `func_151CEA20` now advances velocity from acceleration, advances position
  from midpoint velocity, advances a second scalar from its rate, clamps that
  scalar to `1.0f`, and returns success.
- Fourteen of 35 words emit directly from semantic C. Twenty-one stale-checked
  guards normalize closed FP-register cycles and one equivalent load/store
  schedule; both `D_800BE9A4` relocation words emit naturally. Linked SHA-256
  is `f62b31514b1fa56a41b3eb39f54ba112e9a37df616d6e21bc62f7c54c68cc0ef`.
- Totals are **3,068 / 5,462 (56.17%)** overall and
  **2,489 / 4,788 (51.98%)** in Game. See
  [Working Note 565](WORKING_NOTES/565-game-midpoint-timestep-integrator-match-20260930.md).

### Game object-selector payload-wrapper twin byte-matched

- `func_151B1AB0` now implements the second null-gated owner/selector payload
  wrapper, using command type `0x3C`, overflow value `0x11`, and third argument
  `0x15` before copying the 12-byte payload into a successful allocation.
- Sixteen of 33 words emit directly from semantic C. Seventeen independently
  scoped stale-checked guards normalize the same closed IDO schedule as its
  `func_15192920` structural twin. Linked SHA-256 is
  `244442f6df0e8eb0c7d7de8476d15861a355f5a958ab34ebbb0c4a24c2c26977`.
- Totals are **3,067 / 5,462 (56.15%)** overall and
  **2,488 / 4,788 (51.96%)** in Game. See
  [Working Note 564](WORKING_NOTES/564-game-object-selector-payload-wrapper-twin-match-20260930.md).

### Game object-selector payload wrapper byte-matched

- `func_15192920` now ignores null owners, captures the owner's selector byte,
  requests a command-`0x23` record, and copies its 12-byte owner/selector/zero
  payload into a successful allocation.
- Sixteen of 33 words emit directly from semantic C. Seventeen stale-checked
  guards normalize the early call-argument/local-store schedule and exchange
  the selector and zero-float stores around the allocation call. Linked
  SHA-256 is
  `22a75e9e7d0e3f7d317b63e54214725208a2fc9a4bdb938f04f0352aa72cda4a`.
- Totals are **3,066 / 5,462 (56.13%)** overall and
  **2,487 / 4,788 (51.94%)** in Game. See
  [Working Note 563](WORKING_NOTES/563-game-object-selector-payload-wrapper-match-20260930.md).

### Game command-0x1D payload allocator byte-matched

- `func_1518AADC` now allocates a 40-byte command-`0x1D` payload, clears four
  words, retains its owner, duplicates a signed halfword, and stores a byte
  selector.
- Twenty-three of 33 words emit directly from semantic C. Ten stale-checked
  guards normalize the post-call halfword/pointer swap and retained
  owner/selector store schedule. Linked SHA-256 is
  `7e6524e62e23ce9f04813a749375ae59fd2ce4fd0cb2a8b3ff2d56c313256671`.
- Totals are **3,065 / 5,462 (56.11%)** overall and
  **2,486 / 4,788 (51.92%)** in Game. See
  [Working Note 562](WORKING_NOTES/562-game-command-1d-payload-allocator-match-20260930.md).

### Game selector display-list appender byte-matched

- `func_15183BA4` now maps a selector through the 11-byte `D_800A72D0` table
  and conditionally appends the corresponding non-null `D_800DDF78` display
  list to its output cursor.
- All 33 words / 132 bytes emit directly from semantic C with no guards or
  compiler override. The original `gSPDisplayList(dl++, value)` macro shape
  recovers retail's cursor snapshot and update. Linked SHA-256 is
  `0eb643956a1f00342d1e746734b5b8127d7b84832163a0a6c9e3a90250dcb046`.
- Totals are **3,064 / 5,462 (56.10%)** overall and
  **2,485 / 4,788 (51.90%)** in Game. See
  [Working Note 561](WORKING_NOTES/561-game-selector-display-list-appender-match-20260930.md).

### Game three-entry position queue writer byte-matched

- `func_1517D578` now appends a signed position, selector byte, two trailing
  halfwords, and one float to the global queue while its count is below three.
- The semantic C emits the exact 33-word extent and control flow. Twenty-nine
  stale-checked guards normalize one closed IDO pointer/register and opening
  schedule cycle, including both moved relocations. Linked SHA-256 is
  `71f575144e94e2e3cac83b62e3e197e36edfa34d7c1ad864f439cb942be99e01`.
- Totals are **3,063 / 5,462 (56.08%)** overall and
  **2,484 / 4,788 (51.88%)** in Game. See
  [Working Note 560](WORKING_NOTES/560-game-three-entry-position-queue-writer-match-20260930.md).

### Game transformed-position short writer byte-matched

- `func_1516441C` now transforms one inline payload vector through its embedded
  transform pointer, truncates the resulting floats, and writes three signed
  position halfwords to the render record.
- All 35 words / 140 bytes emit directly from semantic C with no guards or
  compiler override. Linked SHA-256 is
  `2b3e339b55f5ccfb744f48761aab23bb7e518571dc34d5aeef4826b8a7015d26`.
- Totals are **3,062 / 5,462 (56.06%)** overall and
  **2,483 / 4,788 (51.86%)** in Game. See
  [Working Note 559](WORKING_NOTES/559-game-transformed-position-short-writer-match-20260930.md).

### Game two-entry selection event callback byte-matched

- `func_15158B3C` now switches or clears the current pointer/selector pair in
  response to byte operations `0x2D` and zero.
- Twenty-six of 37 words emit directly from semantic C. Ten guarded rows
  normalize an 11-word return-delay and temporary-register scheduling cycle.
  Linked SHA-256 is
  `f6f19275e72e485804598ba595d662c7522ed0f876312a865749ff013dad34e5`.
- Totals are **3,061 / 5,462 (56.04%)** overall and
  **2,482 / 4,788 (51.84%)** in Game. See
  [Working Note 558](WORKING_NOTES/558-game-two-entry-selection-event-callback-match-20260930.md).

### Game owner-list matching-node cleanup byte-matched

- `func_1514EDF0` now repeatedly searches the list at owner offset `0x2F4`
  and unlinks every node whose object key matches its first argument.
- Twenty-nine of 32 words emit directly from semantic C. Three guarded words
  normalize only IDO's equivalent `sp+0x38` local pointer placement to retail's
  `sp+0x34` slot. Linked SHA-256 is
  `318a5ff08113e9167dc286d85f9442ff04d79e5a5c4890cce2a5ebe9d43d6165`.
- Totals are **3,060 / 5,462 (56.02%)** overall and
  **2,481 / 4,788 (51.82%)** in Game. See
  [Working Note 557](WORKING_NOTES/557-game-owner-list-matching-node-cleanup-match-20260930.md).

### Game bit-zero state-operation callback byte-matched

- `func_1514E89C` toggles, sets, or clears bit zero of the object state word
  for operations zero, one, and two. Unsupported operations return zero;
  handled operations return one.
- All 33 words / 132 bytes emit directly from C with no guards. The K&R
  byte-typed third argument preserves retail's entry spill without changing
  neighboring callers. Linked SHA-256 is
  `e3b31f4007d3288e78f7111a743bcdb9e6ae4ebd371d4c4db5ecdb1df6f61851`.
- Totals are **3,059 / 5,462 (56.01%)** overall and
  **2,480 / 4,788 (51.80%)** in Game. See
  [Working Note 556](WORKING_NOTES/556-game-bit-zero-state-operation-callback-match-20260930.md).

### Game indexed saved-state restorer byte-matched

- `func_151239CC` checks an indexed saved-state slot, restores its identifier,
  four words, and two halfwords, refreshes derived state, clears the slot's
  active flag, and returns whether restoration occurred.
- All 34 words / 136 bytes match. Thirty-two words emit directly from C; two
  stale-checked guards preserve retail's equivalent top-frame pointer spill
  and reload. Linked SHA-256 is
  `ec56b71f610b4610715e4fcf2392dfb3a9a19190390075a9053f0466bb6ad33a`.
- Totals are **3,058 / 5,462 (55.99%)** overall and
  **2,479 / 4,788 (51.78%)** in Game. See
  [Working Note 555](WORKING_NOTES/555-game-indexed-saved-state-restorer-match-20260930.md).

### Game mode-gated object cleanup wrapper byte-matched

- `func_1511A738` conditionally resolves its object-table index in mode one,
  clears the object's state and float fields when that lookup succeeds, and
  always runs the shared update and position-forwarding helpers.
- All 34 words / 136 bytes emit directly from C with no guards. Linked
  SHA-256 is
  `a1053a069258527eb633d4a5874bdd5c7cdac0c558ad4075cc3587436922a264`.
- Totals are **3,057 / 5,462 (55.97%)** overall and
  **2,478 / 4,788 (51.75%)** in Game. See
  [Working Note 554](WORKING_NOTES/554-game-mode-gated-object-cleanup-wrapper-match-20260930.md).

### Game two-tag record index scan byte-matched

- `func_1511A410` scans eight-byte records to find the first two entries whose
  signed tag is `-3`, stopping at signed sentinel `-0x21`.
- All 33 words / 132 bytes match through 13 stale-checked guards for one
  closed stack-base scheduling and temporary-register chain. Linked SHA-256
  is `c9f324d509e8a4e3282456e941568a37a88c4b1e6dc32ae7d04bbe8c52384c67`.
- Totals are **3,056 / 5,462 (55.95%)** overall and
  **2,477 / 4,788 (51.73%)** in Game. See
  [Working Note 553](WORKING_NOTES/553-game-two-tag-record-index-scan-match-20260930.md).

### Game state-two countdown finalizer byte-matched

- `func_1510D720` mirrors the indexed countdown finalizer and changes the
  indexed state to two when the activity byte reaches zero.
- All 35 words / 140 bytes emit directly from C with no guards. Linked
  SHA-256 is
  `291ebfdf97818a363db055caf102d3c63d6c9470df7db1bc76e7479705857527`.
- Totals are **3,055 / 5,462 (55.93%)** overall and
  **2,476 / 4,788 (51.71%)** in Game. See
  [Working Note 552](WORKING_NOTES/552-game-state-two-countdown-finalizer-match-20260930.md).

### Game indexed countdown finalizer byte-matched

- `func_1510D694` decrements an indexed activity byte and, on its transition
  to zero, expands the dirty index bounds and changes the indexed state to
  three.
- All 35 words / 140 bytes emit directly from C with no guards. Linked
  SHA-256 is
  `14b2c699b48bf4376cc3f16817191178ab21579419ba72f7755cf4ee0895d309`.
- Totals are **3,054 / 5,462 (55.91%)** overall and
  **2,475 / 4,788 (51.69%)** in Game. See
  [Working Note 551](WORKING_NOTES/551-game-indexed-countdown-finalizer-match-20260930.md).

### Game camera-vector forwarding wrapper byte-matched

- `func_1510B32C` forwards a slot and three float words with a zero fifth
  argument, stores the components in `{z, x, y}` order, and raises the update
  flag.
- All 33 words / 132 bytes match through eight stale-checked guards for the
  old-style-call float ABI and FP-register sequence. Linked SHA-256 is
  `1d1156abe599b3f2474a382805b158a19073bd10f6a273c4e72de1927b0bc317`.
- Totals are **3,053 / 5,462 (55.90%)** overall and
  **2,474 / 4,788 (51.67%)** in Game. See
  [Working Note 550](WORKING_NOTES/550-game-camera-vector-forwarding-wrapper-match-20260930.md).

### Game type-0x28 object sweep byte-matched

- `func_150FDD10` refreshes state and, in mode one, scans 25 object records to
  dispatch each type-`0x28` record through `func_150ED638`.
- All 36 words / 144 bytes match through five stale-checked guards for one
  closed `s1`/`s2` allocation cycle. Linked SHA-256 is
  `56ee5e91620600813e41fa84f7931a7b38a7fecfc30d645b6c37ac1f89edf5fc`.
- Totals are **3,052 / 5,462 (55.88%)** overall and
  **2,473 / 4,788 (51.65%)** in Game. See
  [Working Note 549](WORKING_NOTES/549-game-type-28-object-sweep-match-20260930.md).

### Game record-type eligibility predicate byte-matched

- `func_150EC3D4` rejects the comparison record and records without backing
  data, then accepts type bytes `0`, `1`, `2`, `3`, `4`, `0x28`, and `0x77`.
- All 34 words / 136 bytes emit directly from C with no guards. Linked SHA-256
  is `5f7e19ea141ba700d88ecee856c302cc37b327e096dc9a07b5b10aefd7c785a7`.
- Totals are **3,051 / 5,462 (55.86%)** overall and
  **2,472 / 4,788 (51.63%)** in Game. See
  [Working Note 548](WORKING_NOTES/548-game-record-type-eligibility-predicate-match-20260930.md).

### Game motion timestep integrator byte-matched

- `func_150DEACC` advances three coordinates from their velocities and the
  global timestep, reduces vertical speed, and reports whether it is still
  nonnegative.
- All 35 words / 140 bytes emit directly from C with no guards. Linked SHA-256
  is `c1609045c6bc30f63ae3ffa4404d008a6ac91ec834ded44a1135c11840981ae3`.
- Totals are **3,050 / 5,462 (55.84%)** overall and
  **2,471 / 4,788 (51.61%)** in Game. See
  [Working Note 547](WORKING_NOTES/547-game-motion-timestep-integrator-match-20260930.md).

### Handwritten Game absolute-ordering helper restored

- `func_150AD9A0` is restored from its false zero-return C placeholder to the
  original 32-word handwritten absolute-value ordering body.
- The linked 128-byte span is exact with SHA-256
  `4a4f0a1e59e72bbf4c79d7209381c926f46563f59a94c9b2456f36e58382b620`.
- The ownership correction changes the C denominator: totals are
  **3,049 / 5,462 (55.82%)** overall and **2,470 / 4,788 (51.59%)** in Game.
  See [Working Note 546](WORKING_NOTES/546-game-handwritten-absolute-ordering-helper-restoration-20260930.md).

### Game object-position forwarding adapter byte-matched

- `func_1509F77C` resolves an object, truncates its three position floats, and
  forwards the coordinates and caller fields to `func_1000F91C`.
- All 33 words / 132 bytes emit directly from C with no guards. Linked SHA-256
  is `7f7016927ccef67069847fbfce123b4a612f7c2c321e445b26dc058627757d9b`.
- Totals are **3,049 / 5,463 (55.81%)** overall and
  **2,470 / 4,789 (51.58%)** in Game. See
  [Working Note 545](WORKING_NOTES/545-game-object-position-forwarding-adapter-match-20260930.md).

### Game state-three convergence scanner byte-matched

- `func_1509CDDC` restores initial slot processing and repeated 204-byte scans
  of state-3 entries until a complete pass reports no changes.
- All 34 words match retail through 18 guarded contraction/scheduling rows;
  linked SHA-256 is `79a48e8c7f7ddf3f651113de5f1827c8645dfa89ed180c301a154838cba28405`.
- Totals are **3,048 / 5,463 (55.79%)** overall and
  **2,469 / 4,789 (51.56%)** in Game. See
  [Working Note 544](WORKING_NOTES/544-game-state-three-convergence-scan-match-20260930.md).

### Game packed-byte rate updater byte-matched

- `func_15077404` restores the active packed-byte rate update, signed 16-bit
  result truncation, negative clamp, two output stores, and fallback store.
- The complete 176-byte linked span matches all 44 retail words. Thirty-three
  guarded source words and one inserted scheduling word normalize the closed
  compiler register-allocation cycle; the linked ELF span has SHA-256
  `85f549020a856aac2adf5142775d97f1ce8016b59dfb5ed4f796b58c50a802e9`.
- Totals are **3,047 / 5,463 (55.78%)** overall and
  **2,468 / 4,789 (51.53%)** in Game. See
  [Working Note 543](WORKING_NOTES/543-game-packed-byte-rate-update-match-20260930.md).

`func_150413FC` remains non-matching because IDO retains five saved registers
and a 48-byte frame while retail uses four saved registers and a 40-byte
frame. It is parked on that closed allocation cycle; the ordinary queue now
continues with `func_1509CDDC`.

## 2026-09-29

### Game auxiliary-state allocator byte-matched

- `func_1503B7C0` restores allocation and clearing of an 0x50-byte auxiliary
  record, its `30.0f` field, and its PRNG-derived modulo-30 halfword.
- The complete 128-byte function emits directly from semantic C without guard
  rows. Linked and retail spans share SHA-256
  `8994679685f5b6fc094da283e915dd0eee9b0eb5c37aeb33bb08ec1b739d0c00`.
- Totals are **3,046 / 5,463 (55.76%)** overall and
  **2,467 / 4,789 (51.51%)** in Game. See
  [Working Note 542](WORKING_NOTES/542-game-auxiliary-state-allocator-match-20260929.md).

### Game indexed 64-bit flag query byte-matched

- `func_1501D2C4` restores the global override and indexed
  `D_800C3A60[index] & (1LL << bit)` query.
- The complete 132-byte function emits directly from semantic C without guard
  rows. Linked and retail spans share SHA-256
  `75bd476d39efde90ed25537c9acdc86d0d2ef7744c55d1c4340db96d33a8ad54`.
- Totals are **3,045 / 5,463 (55.74%)** overall and
  **2,466 / 4,789 (51.49%)** in Game. See
  [Working Note 541](WORKING_NOTES/541-game-indexed-64-bit-flag-query-match-20260929.md).

### Game indexed constructor wrapper byte-matched

- `func_1501D1D4` restores the seven-argument `func_1502B6BC` call, its two
  local outputs, and the indexed success/failure handle update.
- The complete 132-byte function emits directly from semantic C without guard
  rows. Linked and retail spans share SHA-256
  `05f16c6812cc11dc9363f53b441b15cb02723d07be71832972168ba7fce45f85`.
- Totals are **3,044 / 5,463 (55.72%)** overall and
  **2,465 / 4,789 (51.47%)** in Game. See
  [Working Note 540](WORKING_NOTES/540-game-indexed-constructor-wrapper-match-20260929.md).

### Init primary/child record lookup byte-matched

- `func_1000B1FC` searches all three primary records and then their optional
  child records for a matching identifier.
- Two explicit integer-indexed loops emit the complete 152-byte function
  directly from C without guard rows. Linked and retail spans share SHA-256
  `354ea04ae4d20834968caad5738373e6337461f7cdd7fb391adcd4d0f78d8d48`.
- Totals are **3,043 / 5,463 (55.70%)** overall and
  **398 / 493 (80.73%)** in Init. See
  [Working Note 539](WORKING_NOTES/539-init-primary-child-record-lookup-match-20260929.md).

### Game reflected byte-position update byte-matched

- `func_151E55A8` restores the signed step, byte-position update, reflection at
  both range boundaries, and direction-byte toggle.
- The complete 132-byte function emits directly from semantic C without guard
  rows. Linked and retail spans share SHA-256
  `2b2a6d2d094e1dafe4f418b34038e4ec1b09c2026358f7dd2694bd6776965182`.
- Totals are **3,042 / 5,463 (55.68%)** overall and
  **2,464 / 4,789 (51.45%)** in Game. See
  [Working Note 538](WORKING_NOTES/538-game-reflected-byte-position-update-match-20260929.md).

### Game linked-endpoint event handler byte-matched

- `func_151B70B4` restores zero-event detach state and event-`0x2D`
  replacement of either linked endpoint and its selector byte.
- Nineteen stale-checked transformations normalize one closed IDO
  register/scheduling cycle, including two restored preload words. The
  144-byte spans share SHA-256
  `044f8a0c25072ab7a3589f49051658a9275c5c05284eb5b41e406a31f4db30b1`.
- Totals are **3,041 / 5,463 (55.67%)** overall and
  **2,463 / 4,789 (51.43%)** in Game. See
  [Working Note 537](WORKING_NOTES/537-game-linked-endpoint-event-handler-match-20260929.md).

### Game second motion-threshold update byte-matched

- `func_151AFC08` restores its flag-gated progress clamp and paired accumulator
  update using the semantic body shared with `func_150CC638`.
- Thirteen stale-checked transformations normalize the duplicate IDO allocation
  pattern. The 128-byte spans share SHA-256
  `f513b7f3c9bee8f04c2afe8007ea87e74d5ba3cd3a2c240639dcd9bc60eb3bfe`.
- Totals are **3,040 / 5,463 (55.65%)** overall and
  **2,462 / 4,789 (51.41%)** in Game. See
  [Working Note 536](WORKING_NOTES/536-game-second-motion-threshold-update-match-20260929.md).

### Game four-resource teardown byte-matched

- `func_1519F400` now releases four resource fields through their recovered
  ownership-specific teardown paths.
- All 35 words emit directly from C; the 140-byte spans share SHA-256
  `42485dfa9f8061de584a11197449d96173d89c7f9fd07617b80c36e3d2e45650`.
- Totals are **3,039 / 5,463 (55.63%)** overall and
  **2,461 / 4,789 (51.39%)** in Game. See
  [Working Note 535](WORKING_NOTES/535-game-four-resource-teardown-match-20260929.md).

### Game indexed slot teardown event pair byte-matched

- `func_15172CA8` now deactivates an occupied indexed slot and emits its two
  recovered `func_1517EE40` teardown events.
- All 32 words emit directly from C; the 128-byte spans share SHA-256
  `85845ebeab1c34c3ccaac89e2f3f6c17cdcc73f798354419eabaa2a1de864a90`.
- Totals are **3,038 / 5,463 (55.61%)** overall and
  **2,460 / 4,789 (51.37%)** in Game. See
  [Working Note 534](WORKING_NOTES/534-game-indexed-slot-teardown-event-pair-match-20260929.md).

### Game descriptor-copy allocation wrapper byte-matched

- `func_15157898` now forwards the recovered constructor arguments and copies
  its 56-byte descriptor to a successfully allocated object.
- All 32 words emit directly from C; the 128-byte spans share SHA-256
  `2b6f5e119f028f88171da469e55663785d9b29990910dd5d10dc1f2de93a07db`.
- Totals are **3,037 / 5,463 (55.59%)** overall and
  **2,459 / 4,789 (51.35%)** in Game. See
  [Working Note 533](WORKING_NOTES/533-game-descriptor-copy-allocation-wrapper-match-20260929.md).

### Game randomized RGBA initializer byte-matched

- `func_15152ABC` now selects one of five RGB triplets and generates an alpha
  byte in the inclusive range 155 through 255 from two RNG results.
- The unsigned remainder operations and byte-width table index emit all 31
  retail words directly from C with no expected-word guards.
- The linked and retail 124-byte spans share SHA-256
  `88d2149442bf8daa04fcfad60211c9ac28fe73d3f87a481e14acbb788959d265`.
- Totals are **3,036 / 5,463 (55.57%)** overall and
  **2,458 / 4,789 (51.33%)** in Game, with no address-drift rows. See
  [Working Note 532](WORKING_NOTES/532-game-randomized-rgba-initializer-match-20260929.md).

### Game owner-payload allocation wrapper byte-matched

- `func_1514F3CC` now builds the retail 12-byte owner payload, requests its
  fixed `0x12C` object, and conditionally copies the payload to offset `0x28`.
- The typed payload and direct allocator call emit all 32 retail words with no
  expected-word guards.
- The linked and retail 128-byte spans share SHA-256
  `0d2c9ded4f628ae40ae053987cf654b78cdca2553954cee3a4d9433974a4cc92`.
- Totals are **3,035 / 5,463 (55.56%)** overall and
  **2,457 / 4,789 (51.31%)** in Game, with no address-drift rows. See
  [Working Note 531](WORKING_NOTES/531-game-owner-payload-allocation-wrapper-match-20260929.md).

### Game fixed resource-constructor wrapper byte-matched

- `func_1514DBB8` now forwards its incoming owner to `func_15160A58` with
  resource `D_800A58A0` and the complete recovered 16-argument constructor
  configuration.
- The direct fixed-argument call emits all 32 retail words, including the
  72-byte frame and stack-store schedule, with no expected-word guards.
- The linked and retail 128-byte spans share SHA-256
  `87d5dcc1c3831a00b3ddcd3a65994a1b55e497ccc924c820ed8cafd6e055a110`.
- Totals are **3,034 / 5,463 (55.54%)** overall and
  **2,456 / 4,789 (51.28%)** in Game, with no address-drift rows. See
  [Working Note 530](WORKING_NOTES/530-game-fixed-resource-constructor-wrapper-match-20260929.md).

### Game current-player threshold dispatcher byte-matched

- `func_150DEB58` now indexes the current `0x9A0`-byte player record, returns
  zero when float field `0x388` is below `5.0f`, and otherwise dispatches
  `func_15140410` with embedded records `0x120` and `0x12C` plus the signed
  incoming mode.
- The typed record view emits all 34 retail words directly from C; no
  expected-word guards are needed.
- The linked and retail 136-byte spans share SHA-256
  `f6c3bce2d227ddb0b50324b277e7367e65edae74debfba82802ec09ceada3973`.
- Totals are **3,033 / 5,463 (55.52%)** overall and
  **2,455 / 4,789 (51.26%)** in Game, with no address-drift rows. See
  [Working Note 529](WORKING_NOTES/529-game-current-player-threshold-dispatch-match-20260929.md).

### Game mode-selected color wrapper byte-matched

- `func_150D22F4` now selects record byte `0x3C` with three `0xFF` channel
  arguments when mode byte `0x28` equals one, or record byte `0x3D` with three
  zero channels otherwise, then returns the handle from `func_1517F08C`.
- The typed three-argument wrapper emits all 32 retail words directly from C;
  no expected-word guards are needed.
- The linked and retail 128-byte spans share SHA-256
  `7bb68200536b66166927c2070077dbc5ac251147b697bc66c064635dd18c443c`.
- Totals are **3,032 / 5,463 (55.50%)** overall and
  **2,454 / 4,789 (51.24%)** in Game, with no address-drift rows. See
  [Working Note 528](WORKING_NOTES/528-game-mode-selected-color-wrapper-match-20260929.md).

### Game motion-threshold updater byte-matched

- `func_150CC638` now gates on object flag bit zero, tightens the byte at
  offset `0x5C` from the signed halfword at `0x1C`, and conditionally adds the
  motion-record rate times `D_800BE9A4` to both position accumulators.
- Thirteen stale-checked guards normalize only IDO's equivalent register and
  address schedule; two inserted words retain retail's repeated `0x128`
  record-pointer materialization.
- The linked and retail 128-byte spans share SHA-256
  `f513b7f3c9bee8f04c2afe8007ea87e74d5ba3cd3a2c240639dcd9bc60eb3bfe`.
- Totals are **3,031 / 5,463 (55.48%)** overall and
  **2,453 / 4,789 (51.22%)** in Game, with no address-drift rows. See
  [Working Note 527](WORKING_NOTES/527-game-motion-threshold-updater-match-20260929.md).

### Game randomized effect-parameter wrapper byte-matched

- `func_150B6754` now calls the PRNG twice, derives unsigned `200..255` and
  `15..25` parameters, and forwards them with fixed RGB values and its incoming
  byte/context to `func_15182670`.
- Keeping both PRNG calls in the final argument expression restores retail's
  temporary spill, so all 35 words emit directly from C without guards.
- The linked and retail 140-byte spans share SHA-256
  `fb70b61aec9a52557abb3566fc9c99564e9583ec845ef8e730bcde9ce3ec9209`.
- Totals are **3,030 / 5,463 (55.46%)** overall and
  **2,452 / 4,789 (51.20%)** in Game, with no address-drift rows. See
  [Working Note 526](WORKING_NOTES/526-game-randomized-effect-parameter-wrapper-match-20260929.md).

### Game coordinate-query wrapper byte-matched

- `func_150A32B4` now constructs a stack-local `struct127` from three integer
  coordinates, mirrors its position fields, submits it through
  `func_150A1DA0`, and returns whether the query produced zero.
- The existing `struct127` layout reproduces the `0x350`-byte frame and all 31
  words directly from C with no expected-word guards.
- The linked and retail 124-byte spans share SHA-256
  `e14902f3383e5012a58c5da9916095a0fcfda96dd0709a830e73375e9fe79f5f`.
- Totals are **3,029 / 5,463 (55.45%)** overall and
  **2,451 / 4,789 (51.18%)** in Game, with no address-drift rows. See
  [Working Note 525](WORKING_NOTES/525-game-coordinate-query-wrapper-match-20260929.md).

### Game bounded table-buffer append byte-matched

- `func_1507EBB8` now selects a source sequence and byte length by index,
  appends it only when the resulting buffer count remains below 40, and
  advances the count after `bcopy`.
- A full-width local for the byte-table length restores retail's frame and
  register lifetime, so all 32 words emit directly from C without guards.
- The linked and retail 128-byte spans share SHA-256
  `6264e616750342b961bace698a74aa7a7f62df4dcba9df8a664422c21cee6499`.
- Totals are **3,028 / 5,463 (55.43%)** overall and
  **2,450 / 4,789 (51.16%)** in Game, with no address-drift rows. See
  [Working Note 524](WORKING_NOTES/524-game-bounded-table-buffer-append-match-20260929.md).

### Game secondary collision-classifier wrapper byte-matched

- `func_15046F84` now uses `func_15047004`'s classification to delegate class
  zero to `func_15046D00` and map classes one and two to false and true.
- The observed ABI and sibling switch shape emit the complete 32-word routine
  directly from C with no expected-word guards.
- The linked and retail 128-byte spans share SHA-256
  `70ad2ec1ad364a1b82e41a9c63b2116dea4702ff54c0833feeb3c4e930559646`.
- Totals are **3,027 / 5,463 (55.41%)** overall and
  **2,449 / 4,789 (51.14%)** in Game, with no address-drift rows. See
  [Working Note 523](WORKING_NOTES/523-game-secondary-collision-classifier-wrapper-match-20260929.md).

### Game collision-classifier wrapper byte-matched

- `func_15046C80` now classifies its position and collision record through
  `func_15047004`, delegates class zero to `func_1504697C`, and maps classes
  one and two to false and true.
- Its observed four-argument ABI and three-way switch emit the complete
  32-word routine directly from C with no expected-word guards.
- The linked and retail 128-byte spans share SHA-256
  `b5786bc19624a7b4064536d78eda93d2752e60b8bda9395662d593924fb6f823`.
- Totals are **3,026 / 5,463 (55.39%)** overall and
  **2,448 / 4,789 (51.12%)** in Game, with no address-drift rows. See
  [Working Note 522](WORKING_NOTES/522-game-collision-classifier-wrapper-match-20260929.md).

### Game 25-byte group deduplicating append byte-matched

- `func_1502225C` now scans a selected 25-byte row in `D_800C3518`, returns
  when the incoming byte already exists, and otherwise appends it while
  incrementing the corresponding `D_800C3510` count.
- The typed row stride reproduces the complete 33-word routine directly from
  semantic C with no expected-word guards.
- The linked and retail 132-byte spans share SHA-256
  `26a69edf89a280a0b5a539dda7f210dadfd03750bc373bb2b445a3b6f565e688`.
- Totals are **3,025 / 5,463 (55.37%)** overall and
  **2,447 / 4,789 (51.10%)** in Game, with no address-drift rows. See
  [Working Note 521](WORKING_NOTES/521-game-25-byte-group-deduplicating-append-match-20260929.md).

### Game callback-state setup byte-matched

- `func_151E4E64` now runs its two setup calls, raises the high bit in
  `D_800E0B9A` once `D_800E0A90` reaches `0x4B1`, and conditionally installs
  callback `func_151E4E00` with state bytes `7` and `8`.
- The complete 33-word routine emits directly from semantic C with no
  expected-word guards.
- The linked and retail 132-byte spans share SHA-256
  `d265bd58b30d5d4a492a624a5fe5e9644255b0f276ad7d413c9ed06946404fc9`.
- Totals are **3,024 / 5,463 (55.35%)** overall and
  **2,446 / 4,789 (51.08%)** in Game, with no address-drift rows. See
  [Working Note 520](WORKING_NOTES/520-game-callback-state-setup-match-20260929.md).

### Game record-match release wrapper byte-matched

- `func_1518F49C` now forwards its record, selector, and embedded owner fields
  to `func_15169850`, then conditionally releases the owner for selector
  `0x49` when either the record word or discriminator byte matches.
- Correcting the third argument to its 32-bit ABI and reloading its low byte
  from the argument home slot reproduces retail's 40-byte frame. Explicit
  comparison locals preserve the retail register lifetimes, so all 32 words
  emit directly from C with no expected-word guards.
- The linked and retail 128-byte spans share SHA-256
  `60e99d1939859e1e9b6d3415de34212abe309135238fa1ba79be3c37d0077bbb`.
- Totals are **3,023 / 5,463 (55.34%)** overall and
  **2,445 / 4,789 (51.05%)** in Game, with no address-drift rows. See
  [Working Note 519](WORKING_NOTES/519-game-record-match-release-wrapper-20260929.md).

### Game record-window initializer byte-matched

- `func_15183974` now indexes `D_800DDE80` as five-word records, initializes
  the selected and following records when their first words are zero, and
  copies the selected record's fourth word into the following record.
- The typed record layout reproduces retail's address and register allocation.
  Four expected-word guards preserve one equivalent record-pointer spill at
  retail stack offset `0x1C`; the other 27 words emit directly from C.
- The linked and retail 124-byte spans share SHA-256
  `2fa35f0fd488dbd398137f278e58cd14d8b44842fd89bad6d083c8f5cbdd2c6e`.
- Totals are **3,022 / 5,463 (55.32%)** overall and
  **2,444 / 4,789 (51.03%)** in Game, with no address-drift rows. See
  [Working Note 518](WORKING_NOTES/518-game-record-window-initializer-match-20260929.md).

### Game fixed-payload object spawn byte-matched

- `func_1514D978` now builds its 32-byte payload, creates the corresponding
  object, copies the payload to offset `0x58`, and registers tag `0x13`.
- The payload/result declaration order preserves retail's stack map. All 31
  words emit directly from C with no expected-word guards.
- The linked and retail 124-byte spans share SHA-256
  `88988aac1c2edc8f456aa37224844513cc58ef01dd750e045a040b8266ee8b3c`.
- Totals are **3,021 / 5,463 (55.30%)** overall and
  **2,443 / 4,789 (51.01%)** in Game, with no address-drift rows. See
  [Working Note 517](WORKING_NOTES/517-game-fixed-payload-object-spawn-match-20260929.md).

### Game owner-identity object spawn byte-matched

- `func_151001B4` now builds its eight-byte owner/identity payload, creates
  the fixed type-`0x12C`/subtype-`0x4E` object, and conditionally copies the
  payload to object offset `0x28`.
- The correct allocator ABI and narrow payload type reproduce all 31 retail
  words directly from C. No expected-word guards are used.
- The linked and retail 124-byte spans share SHA-256
  `560751d5b99b1ad36a492f2f4100f5d38e2f0ca2ca844e71cd9f1cee93161a04`.
- Totals are **3,020 / 5,463 (55.28%)** overall and
  **2,442 / 4,789 (50.99%)** in Game, with no address-drift rows. See
  [Working Note 516](WORKING_NOTES/516-game-owner-identity-object-spawn-match-20260929.md).

### Game indexed resource-chain teardown byte-matched

- `func_150C0A48` now follows the owner's signed-index entry chain, releases
  each resource, and reloads the table before reading the next index.
- An explicit integer-base entry address preserves retail's commutative
  operand order. All 30 words emit directly from C with no guards.
- The linked and retail 120-byte spans share SHA-256
  `f4396ce3f3be8f1c133a1b70e34bd11fe5c83a539813888e6a90f801573fbddc`.
- Totals are **3,019 / 5,463 (55.26%)** overall and
  **2,441 / 4,789 (50.97%)** in Game, with no address-drift rows. See
  [Working Note 515](WORKING_NOTES/515-game-indexed-resource-chain-teardown-match-20260929.md).

### Game owner-payload object spawn byte-matched

- `func_150BDE90` now builds its eight-byte owner payload, creates the fixed
  type-`0x12C`/subtype-`0x4F` object, and conditionally copies the payload to
  object offset `0x28`.
- The correct allocator ABI and narrow payload type reproduce all 31 retail
  words directly from C. No expected-word guards are used.
- The linked and retail 124-byte spans share SHA-256
  `c1210a8e98cd676608cb4aa49a6c41cf1d50889ec535d5174e64d22d10e21275`.
- Totals are **3,018 / 5,463 (55.24%)** overall and
  **2,440 / 4,789 (50.95%)** in Game, with no address-drift rows. See
  [Working Note 514](WORKING_NOTES/514-game-owner-payload-object-spawn-match-20260929.md).

### Game resource slot-array teardown byte-matched

- `func_150B6D78` now releases the standalone `D_800D9894` allocation,
  scans and clears ten allocation slots, and sets the owning state to 3.
- Thirty-one words emit directly from semantic C. Two relocation-aware stale
  checks preserve retail's independent cursor/end address-finalization order.
- The linked and retail 132-byte spans share SHA-256
  `c9f16b9bdec0d5a3f4a6f2778cd94a59aad0204e99ea73f300251dbcaa83423d`.
- Totals are **3,017 / 5,463 (55.23%)** overall and
  **2,439 / 4,789 (50.93%)** in Game, with no address-drift rows. See
  [Working Note 513](WORKING_NOTES/513-game-resource-slot-array-teardown-match-20260929.md).

### Game two-angle trigonometric updater byte-matched

- `func_150A0D14` now scales float inputs at offsets `0xC` and `0x10`, calls
  the paired cosine and sine helpers for each, and stores four outputs at
  offsets `0x24..0x30`.
- A narrow typed record view and correct floating-return prototypes reproduce
  all 30 retail words directly from C, including the saved `$f20` lifetime.
  No expected-word guards are used.
- The linked and retail 120-byte spans share SHA-256
  `dac05049dfcc33eb162289598122317e867b460999b13b459c433af7ce230fc4`.
- Totals are **3,016 / 5,463 (55.21%)** overall and
  **2,438 / 4,789 (50.91%)** in Game, with no address-drift rows. See
  [Working Note 512](WORKING_NOTES/512-game-two-angle-trigonometric-updater-match-20260929.md).

### Game resource teardown byte-matched

- `func_15080BE8` now clears its active byte, releases its primary object and
  allocation, conditionally frees three auxiliary allocations, clears their
  owner slot, and performs the final teardown tagged `0x5622`.
- Four relocation-aware stale checks preserve retail's `v0` lifetime for the
  optional-allocation load, null test, and free-call delay-slot move. Every
  other word emits directly from the semantic C body.
- The linked and retail 124-byte spans share SHA-256
  `cd3ecd60f04fee86983201b3860e4136788407f2e8ee6b6919b8b0ad28bf0294`.
- Totals are **3,015 / 5,463 (55.19%)** overall and
  **2,437 / 4,789 (50.89%)** in Game, with no address-drift rows. See
  [Working Note 511](WORKING_NOTES/511-game-resource-teardown-match-20260929.md).

### Game timed HUD fade helper byte-matched

- `func_151EC178` now derives a saturated 8x alpha ramp after timer `0x5DD`,
  applies white modulation, draws fixed resource `D_800E0BD8[0x74]`, and
  returns its incoming display-list pointer unchanged.
- Nineteen relocation-aware stale checks restore retail's separate scaled and
  result registers and the displaced two-call tail after IDO collapses that
  merge. The complete tracked slot remains 30 words.
- The linked and retail 120-byte spans share SHA-256
  `3d94d64b056ac0c8f9b14949c3456faa92bfe86305e718365922d0f7e438a47b`.
- Totals are **3,014 / 5,463 (55.17%)** overall and
  **2,436 / 4,789 (50.87%)** in Game, with no address-drift rows. See
  [Working Note 510](WORKING_NOTES/510-game-timed-hud-fade-helper-match-20260929.md).

### Game subsystem-state initializer byte-matched

- `func_151DDBA0` now performs its five-argument setup, updates the global
  mode and state bytes, invokes three subsystem routines, and raises both
  ready flags.
- The semantic C body reproduces all 32 retail words directly, including the
  32-byte frame, stack argument, call delay slots, and final paired stores.
  No expected-word guards are used.
- The linked and retail 128-byte spans share SHA-256
  `fa65b54c86b9b6abdf04525f540a144ff1760fbf26793da7e5df98d6153cad1b`.
- Totals are **3,013 / 5,463 (55.15%)** overall and
  **2,435 / 4,789 (50.85%)** in Game, with no address-drift rows. See
  [Working Note 509](WORKING_NOTES/509-game-subsystem-state-initializer-match-20260929.md).

### Game five-state impact dispatcher byte-matched

- `func_15194794` now performs both unconditional setup calls and dispatches
  `func_151AF270` when state byte `arg1[4]` is in the range zero through four.
- The grouped switch reproduces retail's complete 31-word control flow. Two
  relocation-aware stale checks retarget its generated jump-table load to
  retained retail symbol `jtbl_800A82BC_game`; no words are added or removed.
- The linked and retail 124-byte spans share SHA-256
  `dcbbb3f61a3783037fa53380faa1f99774cc4caa431b8c30b6883f8c390b16e7`.
- Totals are **3,012 / 5,463 (55.13%)** overall and
  **2,434 / 4,789 (50.82%)** in Game, with no address-drift rows. See
  [Working Note 508](WORKING_NOTES/508-game-five-state-impact-dispatch-match-20260929.md).

### Game reference-counted resource release byte-matched

- `func_1518CA04` now ignores reserved index `0x1E4`, decrements its nonzero
  byte reference counter, and performs allocation cleanup only when that
  counter transitions to zero.
- A short-circuit decrement expression reproduces retail's `v0` pointer,
  `v1` value lifetime, `0x20` frame, and both cleanup calls directly from C.
  No expected-word guards are used.
- The linked and retail 124-byte spans share SHA-256
  `dfa0b48be60169a821895ce7a48189eff8755b2d682a1497651eaec3aa1b925a`.
- Totals are **3,011 / 5,463 (55.12%)** overall and
  **2,433 / 4,789 (50.80%)** in Game, with no address-drift rows. See
  [Working Note 507](WORKING_NOTES/507-game-reference-counted-resource-release-match-20260929.md).

### Game byte-selected coefficient clamp byte-matched

- `func_15182F58` now selects a coefficient from a 24-byte row using the
  current byte selector, multiplies it by `arg0 * 40`, and clamps the result
  to the inclusive range from zero through 39.
- Preserving integer scaling before float conversion and expressing the upper
  clamp as `else if` reproduce all 33 retail words directly from C. No
  expected-word guards are used.
- The linked and retail 132-byte spans share SHA-256
  `0873fbb7ea8b86165e60c1c6cdb73f6cb692d345f177b80efa4b6165f1847db2`.
- Totals are **3,010 / 5,463 (55.10%)** overall and
  **2,432 / 4,789 (50.78%)** in Game, with no address-drift rows. See
  [Working Note 506](WORKING_NOTES/506-game-byte-selected-coefficient-clamp-match-20260929.md).

### Game cached resource setup byte-matched

- `func_1517A9A8` now preserves the incoming display-list cursor when its
  selector is cached; on a cache miss it builds a 20-byte output record,
  passes the selector shifted by eight to `func_15094F70`, and updates the
  cached selector.
- The volatile selector lifetime restores retail's two independent stack
  reloads and complete 30-word extent. Six stale checks normalize only the
  independent call-argument setup order.
- The linked and retail 120-byte spans share SHA-256
  `096d913e68b8486c3adef397b4f0076b0c2948e4bd0ffa13139747bada4a89dd`.
- Totals are **3,009 / 5,463 (55.08%)** overall and
  **2,431 / 4,789 (50.76%)** in Game, with no address-drift rows. See
  [Working Note 505](WORKING_NOTES/505-game-cached-resource-setup-match-20260929.md).

### Game display-list address relocator byte-matched

- `func_15168F08` now walks eight-byte display-list commands using signed
  opcodes and relocates the 24-bit address in opcode `1` and qualifying opcode
  `0xDC` commands.
- Explicit index-based cursor updates, volatile opcode reloads, and separate
  mask/add stores restore retail's complete control flow and memory traffic.
  Eighteen stale checks normalize one closed register-allocation chain.
- The linked and retail 124-byte spans share SHA-256
  `87b6edb1eaa07348ff987b92fadfd41fe157af7bb3bd4bd60ee33b3b46bc764f`.
- Totals are **3,008 / 5,463 (55.06%)** overall and
  **2,430 / 4,789 (50.74%)** in Game, with no address-drift rows. See
  [Working Note 504](WORKING_NOTES/504-game-display-list-address-relocator-match-20260929.md).

### Game group-value deduplicating append byte-matched

- `func_15022640` now searches the populated prefix of a 30-byte per-group
  value row, returns on a duplicate, and appends new values while incrementing
  the corresponding byte count.
- Correcting the incoming value ABI to `s32` avoids a false truncation spill.
  A separate signed loop-bound lifetime restores retail's `a3` bound copy and
  `slt`/`bnez` loop. All 31 words emit directly from C with no guards.
- The linked and retail 124-byte spans share SHA-256
  `6a43dab9f135f13b92604ed942ab52b6b38913b931457760c0544a753e3cbc88`.
- Totals are **3,007 / 5,463 (55.04%)** overall and
  **2,429 / 4,789 (50.72%)** in Game, with no address-drift rows. See
  [Working Note 503](WORKING_NOTES/503-game-group-value-deduplicating-append-match-20260929.md).

### Game actor-slot selector byte-matched

- `func_1503F964` now implements its enable-gated, wrapped scan across 25
  actor slots and stores the first index whose actor state has bit
  `0x00800000` set.
- The recovered C reproduces retail's 35-word control flow and branch-delay
  updates. Fourteen stale-checked guards normalize only one closed `a0`/`v1`
  register-allocation cycle, including the `D_800CC2D0` relocation pair.
- The linked and retail 140-byte spans share SHA-256
  `2a29585ac9a143e8d168f4be74450d0b0bd8d0342407f438c8ed303bb2f53260`.
- Totals are **3,006 / 5,463 (55.02%)** overall and
  **2,428 / 4,789 (50.70%)** in Game, with no address-drift rows. See
  [Working Note 502](WORKING_NOTES/502-game-actor-slot-selector-match-20260929.md).

### Game six-word actor query byte-matched

- `func_151420F8` copies a six-word query template, derives the current actor
  index, submits the query, and reports whether the result differs from `-1`.
- Replacing six scalar assignments with the recovered aggregate copy restores
  retail's alternating load/store schedule. A signed actor-stride divisor and
  explicit result branch recover the remaining instructions directly from C;
  no expected-word guards are used.
- The linked and retail 136-byte spans share SHA-256
  `4a242943a6ff310e5ae3c7004300f1cb55b84a08625c9b69fc6f668cc1481ec2`.
- Totals are **3,005 / 5,463 (55.01%)** overall and
  **2,427 / 4,789 (50.68%)** in Game, with no address-drift rows. See
  [Working Note 501](WORKING_NOTES/501-game-six-word-actor-query-match-20260929.md).

### Game opcode-record byte counter byte-matched

- `func_150027F8` scans eight-byte records until opcode `-0x21`, adding four,
  two, or one output bytes for the supported opcode classes.
- Recovering the integer data-address ABI restores retail's repeated
  `base + (index << 3)` loads and complete 32-word control flow. Fourteen
  stale-checked words normalize only the closed opcode/index register cycle.
- The linked and retail 128-byte spans share SHA-256
  `72ef7693e63f911f4b3d0ea14dda74673b109c312244bfea5d48cf2effe0b0b0`.
- Totals are **3,004 / 5,463 (54.99%)** overall and
  **2,426 / 4,789 (50.66%)** in Game, with no address-drift rows. See
  [Working Note 500](WORKING_NOTES/500-game-opcode-record-byte-counter-match-20260929.md).

### Game path-node spawn randomizer byte-matched

- `func_15079790` selects the current actor identifier, generates two signed
  random offsets, and places the actor around its indexed path node.
- Restoring separate actor/path-table lookups for the X and Z writes recovers
  the retail 60-word body and `30(sp)` random-offset slot directly from C. No
  expected-word guards are used.
- The linked and retail 240-byte spans share SHA-256
  `17a05b13fc4c788386d4fe5f06b22abd7c5fb77eb5a898f1ec0d7fe121570def`.
- Totals are **3,003 / 5,463 (54.97%)** overall and
  **2,425 / 4,789 (50.64%)** in Game, with no address-drift rows. See
  [Working Note 499](WORKING_NOTES/499-game-path-node-spawn-randomizer-match-20260929.md).

### Game height-gated action selector byte-matched

- `func_1506DC10` selects action `9` below its floor-height gate; otherwise it
  chooses one of four randomized action identifiers and dispatches it for the
  current actor.
- Recovering the no-argument callback signature removes a false debug
  argument-home store and restores the 37-word extent. One stale-checked word
  preserves retail's commutative floating-equality operand order.
- The linked and retail 148-byte spans share SHA-256
  `21f8135feae7f64d4abfb9c2139abe072e30532dbfacc08743be5cf824bf03a8`.
- Totals are **3,002 / 5,463 (54.95%)** overall and
  **2,424 / 4,789 (50.62%)** in Game, with no address-drift rows. See
  [Working Note 498](WORKING_NOTES/498-game-height-gated-action-selector-match-20260929.md).

### Game byte-state reset byte-matched

- `func_15010600` clears six scalar state bytes, then clears paired 12-byte
  regions at `D_800D992A` and `D_800D993A`.
- Replacing the broad `bzero` placeholder with the recovered loop restores
  retail's four-way unrolling. Four relocation-aware stale checks normalize
  only one independent scalar-store scheduling window.
- The linked and retail 128-byte spans share SHA-256
  `f731c29b484f488587e75844d64f3b7525bbd46b48dbabc3f4c1521ad4d00c37`.
- Totals are **3,001 / 5,463 (54.93%)** overall and
  **2,423 / 4,789 (50.60%)** in Game, with no address-drift rows. See
  [Working Note 497](WORKING_NOTES/497-game-byte-state-reset-match-20260929.md).

### Game audio DMA reader byte-matched

- `func_151F3C4C` clamps the requested read to the configured audio extent,
  obtains and calls the synthesizer DMA callback, invalidates the returned
  cached range, copies it to the destination, and advances the DMA cursor.
- Reusing the callback-state local for the DMA result restores retail's
  32-byte frame and every stack offset. Eleven stale-checked words normalize
  two closed register-allocation cycles without changing instruction count.
- The linked and retail 300-byte spans share SHA-256
  `761449b54f35127e444756f8e17dfbd58f03c91ae450b500a21b39f6710e5814`.
- Totals are **3,000 / 5,463 (54.91%)** overall and
  **2,422 / 4,789 (50.57%)** in Game, with no address-drift rows. See
  [Working Note 496](WORKING_NOTES/496-game-audio-dma-reader-match-20260929.md).

### Init sound-handle lookup byte-matched

- `func_1000F4D8` masks the incoming identifier once, scans all sixteen
  twelve-byte sound records, and validates matching live handles.
- In-place argument normalization emits the complete 36-word retail body
  directly from C. No expected-word guards or assembly restoration are used.
- The linked and retail 144-byte spans share SHA-256
  `e1997a581a20e13ffd2f3b88fb29e08ec757f0e79095e9bb50492b56928926ce`.
- Totals are **2,999 / 5,463 (54.90%)** overall and
  **397 / 493 (80.53%)** in Init, with no address-drift rows. See
  [Working Note 495](WORKING_NOTES/495-init-sound-handle-lookup-match-20260929.md).

### Game water-buoyancy response byte-matched

- `func_15058F24` applies the water-surface entry, buoyancy, settling,
  rising, sinking, and terminal-velocity response for an actor.
- Preserving the original blend factor fixes the initial velocity scale;
  thirty stale-checked words normalize only IDO scheduling and temporary
  register allocation, with no inserted or omitted instructions.
- The linked and retail 540-byte spans share SHA-256
  `cc8850f8e8a135673446e62d2e2970372482b610029b53414e54706f610376d4`.
- Totals are **2,998 / 5,463 (54.88%)** overall and
  **2,421 / 4,789 (50.55%)** in Game, with no address-drift rows. See
  [Working Note 494](WORKING_NOTES/494-game-water-buoyancy-response-match-20260929.md).

### Init record-key updater byte-matched

- `func_100100E0` samples the active-record count once, walks the 48-byte
  record table by pointer, and replaces three key words on exact matches.
- Its semantic C emits the complete 29-word retail control-flow shape. Twenty
  relocation-aware stale checks normalize one closed `$v0`/`$v1` allocation
  cycle without inserting or omitting instructions.
- The linked and retail 116-byte spans share SHA-256
  `cec07d243965cab8d62e7af4a4a557e8ce5e1177ded4ea275655300ff1b1b678`.
- Totals are **2,997 / 5,463 (54.86%)** overall and
  **396 / 493 (80.32%)** in Init, with no address-drift rows. See
  [Working Note 493](WORKING_NOTES/493-init-record-key-updater-match-20260929.md).

### Init handwritten cache routines restored

- Restored `osInvalICache` and `osWritebackDCache` from false empty C
  placeholders to their original handwritten libultra assembly ownership.
- Both 32-word routines preserve their primary-cache opcodes, aligned range
  loops, wrap protection, full-cache fallback loops, and explicit delay slots.
- The linked and retail 128-byte spans share SHA-256 values
  `cf9ac7a3378e8d2013f33517eebd339955e401c76380ec29ca56152a34f0040d`
  and `21514538b715f668861f169883c91749feb94cb501d5dfd9a24b67f782fa1b69`.
- The ownership correction yields **2,996 / 5,463 (54.84%)** overall and
  **395 / 493 (80.12%)** in Init, with no address-drift rows. See
  [Working Note 492](WORKING_NOTES/492-init-handwritten-cache-routine-restoration-20260929.md).

### Init arena-anchor initializer byte-matched

- `func_10003BD0` initializes the arena head at `D_800380B4`, clears fields
  `0x0`, `0x4`, `0xC`, and `0x10`, computes the available size in field `0x8`,
  and installs the initialized node in all three final anchor globals.
- The semantic C preserves retail's repeated global-head loads. Twenty
  stale-checked, relocation-aware guards normalize one closed IDO scheduling
  permutation and insert the retained `D_800380BC` low-half address word.
- The linked and retail 112-byte spans share SHA-256
  `daff5038fcc53e085d9b5dd4c1683c53f53e11a74ff73ea438b7edca3336bffc`.
- Totals are **2,996 / 5,465 (54.82%)** overall and **395 / 495 (79.80%)**
  in Init, with no address-drift rows. See
  [Working Note 491](WORKING_NOTES/491-init-arena-anchor-initializer-match-20260929.md).

### Game impact-effect dispatcher pair byte-matched

- Replaced adjacent empty placeholders `func_15194320` and `func_15194394`
  with their recovered five-state impact-effect dispatch switches.
- All 29 words in each function emit directly from semantic C. A target-specific
  rodata anchor maps their compiler jump-table relocations to retail's two
  preserved five-entry tables; no expected-word guards are required.
- The linked and retail 116-byte spans share SHA-256 values
  `8437b4dd34bf84b387ab2bc2a1f2994c271cbfc9db1040a2ea8aea0691302db3`
  and `94c06f34b68c23f199ab3e8ac64f9c76776135864bfe7f9d9a2819369ffa1deb`.
- Totals are **2,995 / 5,465 (54.80%)** overall and **2,420 / 4,789
  (50.53%)** in Game, with no address-drift rows. See
  [Working Note 490](WORKING_NOTES/490-game-impact-effect-dispatch-pair-match-20260929.md).

### Game identity-matrix initializer byte-matched

- Recovered `guMtxIdentF` as an unrolled identity-matrix initializer using
  float diagonal stores and integer zero stores for the off-diagonal entries.
- The O3 profile emits retail's 19-instruction leaf schedule and trailing
  padding word. Five stale-checked guards normalize only the equivalent
  `$f0` versus retail `$f4` diagonal-constant register choice.
- The linked and retail 80-byte slots share SHA-256
  `3314c8cd2632384c565633ca83d65b1b11477a1d6457ecab8d8eb30dfce96408`.
- Totals are **2,993 / 5,465 (54.77%)** overall and **2,418 / 4,789
  (50.49%)** in Game, with no address-drift rows. See
  [Working Note 489](WORKING_NOTES/489-game-identity-matrix-initializer-match-20260929.md).

### Game offset position halfword writer byte-matched

- Replaced `func_150C7D7C`'s zero-return placeholder with its recovered source
  position query and three offset, truncated halfword outputs.
- All 32 executable words emit directly from semantic C, and the following
  zero padding word also matches. No expected-word guards are required.
- The linked and retail 128-byte executable bodies share SHA-256
  `18e3c934ee0783473d0aede4c877f66f969b43924fb18678f7210490066a8eb8`;
  their complete 132-byte tracked slots share
  `c4ef61067900cb3ed96347ae8f10d7f584a99329af68d91fb82f84fc595df062`.
- Totals are **2,992 / 5,465 (54.75%)** overall and **2,417 / 4,789
  (50.47%)** in Game, with no address-drift rows. See
  [Working Note 488](WORKING_NOTES/488-game-offset-position-halfword-writer-match-20260929.md).

### Game small record-copy allocator byte-matched

- Replaced `func_1515FF74`'s zero-return placeholder with its recovered record
  allocation, explicit null return, and eight-byte payload copy.
- All 30 words emit directly from semantic C. The forwarded category, adjusted
  offset, byte selector, allocator stack arguments, `memcpy` call, and result
  lifetime require no expected-word guards.
- The linked and retail 120-byte spans share SHA-256
  `9fa00267f5c4abdc9ea6b53cfb528fd6267781e75343bd4a68140e4daec73f9f`.
- Totals are **2,991 / 5,465 (54.73%)** overall and **2,416 / 4,789
  (50.45%)** in Game, with no address-drift rows. See
  [Working Note 487](WORKING_NOTES/487-game-small-record-copy-allocator-match-20260929.md).

### Game record find-or-create updater byte-matched

- Replaced `func_151557FC`'s zero-return placeholder with its recovered record
  lookup, fallback allocation, float update, and conditional state/timer setup.
- All 40 words emit directly from semantic C. The actor-table `0x32C` stride,
  byte `0xAD` relocation, branch-likely control flow, and both call delay slots
  require no expected-word guards.
- The linked and retail 160-byte spans share SHA-256
  `26ead8d1e4d9a93f6827eea92120b99ba1e86a29c5067c4de1de8169a17e2dec`.
- Totals are **2,990 / 5,465 (54.71%)** overall and **2,415 / 4,789
  (50.43%)** in Game, with no address-drift rows. See
  [Working Note 486](WORKING_NOTES/486-game-record-find-or-create-update-match-20260929.md).

### Game record allocator initializer byte-matched

- Replaced `func_15155780`'s zero-return placeholder with its recovered record
  allocation, null return, four field initializers, and notification call.
- Twenty-three words emit directly from semantic C. Eight guarded words
  normalize one independent success-path scheduling permutation; both call
  relocations and the complete null path remain compiler-emitted.
- The linked and retail 124-byte spans share SHA-256
  `4d92e5ed8d32b2f0a6b0c792b45f24b113301cb1eec8f2e968d9f65272daf21a`.
- Totals are **2,989 / 5,465 (54.69%)** overall and **2,414 / 4,789
  (50.41%)** in Game, with no address-drift rows. See
  [Working Note 485](WORKING_NOTES/485-game-record-allocator-initializer-match-20260929.md).

### Game two-owner linked-list lookup byte-matched

- Replaced `func_15155FD4`'s zero-return placeholder with its recovered scan
  across two owner records and each owner's linked list.
- Typed owner and node records reproduce the complete 21-word control-flow
  skeleton. Eight relocation-aware guarded words normalize one closed
  owner/end register-allocation cycle without adding or removing instructions.
- The linked and retail 84-byte spans share SHA-256
  `321b9b3da9418278f6de2c2970961e4df0babf026867ae99d5f8f30473d11094`.
- Totals are **2,988 / 5,465 (54.68%)** overall and **2,413 / 4,789
  (50.39%)** in Game, with no address-drift rows. See
  [Working Note 484](WORKING_NOTES/484-game-two-owner-linked-list-lookup-match-20260929.md).

### Game packed indexed-byte updater byte-matched

- Restored `func_1506EF5C`'s repeated active-object reads while retaining its
  recovered sentinel, mode, packed selector, and two indexed byte stores.
- The repeated global expressions reproduce retail's full 22-word skeleton.
  Twenty guarded words normalize IDO's register allocation, four checked
  symbol relocations, scheduling, and equivalent `0xFFFF` encoding; the
  return pair emits directly from C.
- The linked and retail 88-byte spans share SHA-256
  `bb1533bcd2675ab5ab801d3148a589be179a3ce3d5e4a339f0def4f69c842d9a`.
- Totals are **2,987 / 5,465 (54.66%)** overall and **2,412 / 4,789
  (50.37%)** in Game, with no address-drift rows. See
  [Working Note 483](WORKING_NOTES/483-game-packed-indexed-byte-updater-match-20260929.md).

### Game optional-callback teardown pair byte-matched

- Replaced adjacent zero-return placeholders `func_151A8584` and
  `func_151A85D4` with their recovered optional callback-table dispatch,
  shared teardown call, and distinct final callbacks.
- The old-style no-explicit-argument callback calls preserve the incoming
  object in physical register `a0`, matching retail's indirect-call ABI.
  Symmetric guarded rows omit one early compiler spill per function and
  normalize ten path-sensitive scheduling/register words in each span.
- The linked and retail 80-byte spans share SHA-256 values
  `0cddd7a739041989c01637e7f6cf128c15a6546ed7774eb55c6af2430650b3dd`
  and `51544c0fe63745d31a8fad4928ae9ff643e5c4d4ae4fbf9f13e495cc1e801dfe`.
- Totals are **2,986 / 5,465 (54.64%)** overall and **2,411 / 4,789
  (50.34%)** in Game, with no address-drift rows. See
  [Working Note 482](WORKING_NOTES/482-game-optional-callback-teardown-pair-match-20260929.md).

### Game list-node allocator wrapper byte-matched

- Replaced `func_1514EBA4`'s zero-return placeholder with its recovered
  allocator call, null return, and list-node field initialization.
- The native signed-halfword second parameter reproduces retail's stack-home
  load. Twenty-four words emit directly from semantic C; six guarded words
  preserve two independent three-word scheduling cycles.
- The linked and retail 120-byte spans share SHA-256
  `df64ed7a708de97209ab59c3300454d23b0b136d2f6536fd7590342c55353244`.
- Totals are **2,984 / 5,465 (54.60%)** overall and **2,409 / 4,789
  (50.30%)** in Game, with no address-drift rows. See
  [Working Note 481](WORKING_NOTES/481-game-list-node-allocator-wrapper-match-20260929.md).

### Game parameter-block call adapter byte-matched

- Replaced `func_15133510`'s zero-return placeholder with its recovered call
  forwarding three integer fields and eight float fields from one parameter
  block to `func_151424F4`.
- All 30 words emit directly from semantic C with no expected-word guards.
  The typed call naturally reproduces retail's saved `s0`, 64-byte outgoing
  frame, stack argument stores, call delay slot, and epilogue.
- The linked and retail 120-byte spans share SHA-256
  `212f7aca0a9183382226942e0dfc15bbfd4c9606b7db86d79fa4b59e84d5381a`.
- Totals are **2,983 / 5,465 (54.58%)** overall and **2,408 / 4,789
  (50.28%)** in Game, with no address-drift rows. See
  [Working Note 480](WORKING_NOTES/480-game-parameter-block-call-adapter-match-20260929.md).

### Game object type/status mapper byte-matched

- Replaced `func_150B66DC`'s zero-return placeholder with its recovered
  normalized type selector and target status-byte updates.
- All 30 words emit directly from semantic C with no expected-word guards.
  An explicit source-object pointer preserves retail's opening `v0` lifetime,
  early constant return value, and complete branch-likely schedule.
- The linked and retail 120-byte spans share SHA-256
  `f517d090f9e18290dc22a4267a688ec99b90b73ce0f1ae41b6af86a2cce35d78`.
- Totals are **2,982 / 5,465 (54.57%)** overall and **2,407 / 4,789
  (50.26%)** in Game, with no address-drift rows. See
  [Working Note 479](WORKING_NOTES/479-game-object-type-status-mapper-match-20260929.md).

### Game angular state integrator byte-matched

- Replaced `func_150AFBF4`'s zero-return placeholder with its recovered
  timestep integration, wrapped angle, sine transform, and scalar output.
- Twenty-six words emit directly from semantic C. Three guarded scheduling
  normalizations omit an unused scratch-parameter home and move the derived
  value-pointer spill/reload into retail's stack slot.
- The linked and retail 116-byte spans share SHA-256
  `72132aa45284c9b660a8e383d7676ed19df6d95609f2cd27d5eb49be8defcfb2`.
- Totals are **2,981 / 5,465 (54.55%)** overall and **2,406 / 4,789
  (50.24%)** in Game, with no address-drift rows. See
  [Working Note 478](WORKING_NOTES/478-game-angular-state-integrator-match-20260929.md).

### Game float-state scaler byte-matched

- Replaced `func_151339D4`'s zero-return placeholder with its recovered
  position accumulation and six float-field scaling updates.
- All 31 words emit directly from semantic C with no expected-word guards.
  Separating the scale declaration from its assignment preserves retail's
  opening field/stack load order and later return-value schedule.
- The linked and retail 124-byte spans share SHA-256
  `7737373cb0aeb0a501b6af28c2e958084f14fbdc979e25e1ab83a2fe14f45c65`.
- Totals are **2,980 / 5,465 (54.53%)** overall and **2,405 / 4,789
  (50.22%)** in Game, with no address-drift rows. See
  [Working Note 477](WORKING_NOTES/477-game-float-state-scaler-match-20260929.md).

### Game audio DMA prefetch wrapper byte-matched

- Replaced `func_151F3D78`'s zero-return placeholder with its recovered DMA
  callback acquisition and `0x810`-byte prefetch request.
- All 26 words emit directly from semantic C with no expected-word guards.
  Retail padding is now applied to the owning `game_21FC90` object, and two
  standalone audio sources have corrected layout ownership rows.
- The linked and retail 104-byte spans share SHA-256
  `3a57cd163b38e4edc9e3beea97a3bbb961bff87fc574ec20cb1f18e5e8d135b7`.
- A clean full regeneration also reclassified unchanged Init routine
  `func_10012588` from address drift to exact. Totals are **2,979 / 5,465
  (54.51%)** overall and **2,404 / 4,789 (50.20%)** in Game, with no remaining
  address-drift rows. See
  [Working Note 476](WORKING_NOTES/476-game-audio-dma-prefetch-wrapper-match-20260929.md).

### Game event identity-release handler byte-matched

- Replaced `func_150F1684`'s zero-return placeholder with its recovered
  command-`0x43` identity filter and matching-object release dispatch.
- Fifteen of 22 words emit directly from semantic C. Seven fail-closed guards
  normalize one closed key/pointer/comparison register-allocation cycle.
- The linked and retail 88-byte spans share SHA-256
  `c4af721c70a7170cd352101e862a3e86c2bdb4ff161979503d064105f56f0ff9`.
- Totals are **2,977 / 5,465 (54.47%)** overall and **2,403 / 4,789
  (50.18%)** in Game. See
  [Working Note 475](WORKING_NOTES/475-game-event-identity-release-handler-match-20260929.md).

### Game packed-mask setter byte-matched

- Recovered `func_1507A4D4`'s explicit four-byte mask local, mirroring the
  adjacent clear-mask routine before setting the active object's word.
- Five of 21 words emit directly from semantic C. Sixteen fail-closed guards
  normalize the packed-byte load schedule and temporary-register allocation,
  including every moved relocation.
- The linked and retail 84-byte spans share SHA-256
  `7b5a575d011936f80c735669b60c8a2a24d26c2cde4ca4a610ce057a70c219fe`.
- Totals are **2,976 / 5,465 (54.46%)** overall and **2,402 / 4,789
  (50.16%)** in Game. See
  [Working Note 474](WORKING_NOTES/474-game-packed-mask-setter-match-20260929.md).

### Game normalized coordinate-output routine byte-matched

- Replaced `func_1510B958`'s placeholder with its recovered pair of normalized
  record-coordinate calculations and output stores.
- Twenty-five of 30 words emit directly from semantic C. Five fail-closed
  guards normalize only the independent opening table-load/index schedule.
- The linked and retail 120-byte spans share SHA-256
  `3b4951f5cfb30124cdb1616129dd0a5550a80c40c8f3b0d5ec6c649fe7b399fc`.
- Totals are **2,975 / 5,465 (54.44%)** overall and **2,401 / 4,789
  (50.14%)** in Game. See
  [Working Note 473](WORKING_NOTES/473-game-normalized-coordinate-output-match-20260929.md).

### Game descriptor float-forwarding adapter byte-matched

- Replaced `func_150B9D14`'s placeholder with its recovered twelve-argument
  descriptor-to-`func_15142600` forwarding call.
- All 30 words emit directly from semantic C with no guarded replacements.
- The linked and retail 120-byte spans share SHA-256
  `235546b1e70cf0682de3289f8d12540ad11fc76ceef2f6e0f0288f20c68f186b`.
- Totals are **2,974 / 5,465 (54.42%)** overall and **2,400 / 4,789
  (50.11%)** in Game. See
  [Working Note 472](WORKING_NOTES/472-game-descriptor-float-forwarding-adapter-match-20260929.md).

### Game conditional record-dispatch wrapper byte-matched

- Replaced `func_15095A90`'s placeholder with its recovered stack-flag setup
  and conditional five-argument record dispatch.
- All 30 words emit directly from semantic C with no guarded replacements.
- The linked and retail 120-byte spans share SHA-256
  `d8ac1a75d5ffe67afa27db5b941e1061d2c9ae3710f844bdcbbe23ca36b5e28d`.
- Totals are **2,973 / 5,465 (54.40%)** overall and **2,399 / 4,789
  (50.09%)** in Game. See
  [Working Note 471](WORKING_NOTES/471-game-conditional-record-dispatch-wrapper-match-20260929.md).

### Game variable-tail descriptor wrapper byte-matched

- Replaced `func_15094FE8`'s placeholder with its recovered descriptor setup
  and complete variable-tail final dispatch.
- All 30 words emit directly from semantic C with no guarded replacements.
- The linked and retail 120-byte spans share SHA-256
  `552edff8f4df1216c778a7dfc877db65bce0f6d25ec744671c9b1f6dec7f41eb`.
- Totals are **2,972 / 5,465 (54.38%)** overall and **2,398 / 4,789
  (50.07%)** in Game. See
  [Working Note 470](WORKING_NOTES/470-game-variable-tail-descriptor-wrapper-match-20260929.md).

### Game descriptor-install wrapper byte-matched

- Replaced `func_15094F70`'s placeholder with its recovered descriptor setup
  and ten-argument final dispatch.
- All 30 words emit directly from semantic C with no guarded replacements.
- The linked and retail 120-byte spans share SHA-256
  `8d9ae7535f57bf56b9ce25835cb5dc2d6cf8b9fd835967b89a85a095ac263f64`.
- Totals are **2,971 / 5,465 (54.36%)** overall and **2,397 / 4,789
  (50.05%)** in Game. See
  [Working Note 469](WORKING_NOTES/469-game-descriptor-install-wrapper-match-20260929.md).

### Game classifier fallback wrapper byte-matched

- Replaced `func_1504530C`'s placeholder with its recovered classifier dispatch
  and fallback call.
- All 30 words emit directly from semantic C with no guarded replacements. The
  unhandled path preserves the classifier return value exactly as retail does.
- The linked and retail 120-byte spans share SHA-256
  `328e786deff2085910be798eef006116221c3ccb28fe5d7418974696df4439f5`.
- Totals are **2,970 / 5,465 (54.35%)** overall and **2,396 / 4,789
  (50.03%)** in Game. See
  [Working Note 468](WORKING_NOTES/468-game-classifier-fallback-wrapper-match-20260929.md).

### Game paired-mask predicate byte-matched

- Replaced `func_1503EF4C`'s placeholder with its recovered two-word mask
  selection and per-player overlap checks.
- Twenty-eight of 30 words emit directly from semantic C; two fail-closed
  guards preserve retail's commutative `and` operand order.
- The linked and retail 120-byte spans share SHA-256
  `a0fd6178724b9b83a3389a5846d315a002e7711dc8b2dbb3b83129cce9650649`.
- Game has crossed the halfway mark at **2,395 / 4,789 (50.01%)**. Overall
  totals are **2,969 / 5,465 (54.33%)**. See
  [Working Note 467](WORKING_NOTES/467-game-paired-mask-predicate-match-20260929.md).

### Game owned float-array allocator byte-matched

- Replaced `func_15036C70`'s placeholder with its recovered `0x48`-byte
  allocation, clear, and paired three-float array initialization.
- All 30 words emit directly from semantic C with no guarded replacements.
- The linked and retail 120-byte spans share SHA-256
  `83af44c1f6ffc8a91ffd89ea28e4c8c6e7e34c55ca89db063f3437378fb516e1`.
- Totals are **2,968 / 5,465 (54.31%)** overall and **2,394 / 4,789
  (49.99%)** in Game. See
  [Working Note 466](WORKING_NOTES/466-game-owned-float-array-allocator-match-20260929.md).

### Game type-selector state handler byte-matched

- Replaced `func_15033440`'s placeholder with its recovered selector
  `0x27`/`0x29`/`0x35` handling, state-byte clear, and timer adjustment.
- All 30 words emit directly from semantic C with no guarded replacements.
- The linked and retail 120-byte spans share SHA-256
  `d3bddf169bbc128bf1dc34ca2573abeb8614985e05818949bf18e7ee6be2afcb`.
- Totals are **2,967 / 5,465 (54.29%)** overall and **2,393 / 4,789
  (49.97%)** in Game. See
  [Working Note 465](WORKING_NOTES/465-game-type-selector-state-handler-match-20260929.md).

### Game oscillation and angle updater byte-matched

- Replaced `func_151B8BE0`'s placeholder with its sine-based output update,
  timestep angle advance, angle normalization, and final state callback.
- Twenty-two of 29 words emit directly from semantic C; seven fail-closed
  guards preserve one equivalent floating-point temporary cycle.
- The linked and retail 116-byte spans share SHA-256
  `a78173b8ca18bd598d1836c8e2a37e2cbcc47ad86fe5af291d52c8795aa9afae`.
- Totals are **2,966 / 5,465 (54.27%)** overall and **2,392 / 4,789
  (49.95%)** in Game. See
  [Working Note 464](WORKING_NOTES/464-game-oscillation-angle-update-match-20260929.md).

### Game object-record cleanup byte-matched

- Replaced `func_1518E308`'s zero-return placeholder with its recovered owner
  reset, 100-record live-pointer release loop, and complete `0x960`-byte array
  clear.
- All 29 words emit directly from semantic C with no guarded replacements,
  including retail's branch-likely loop increment and retained array base.
- The complete linked and pristine retail 116-byte spans share SHA-256
  `a062376721760a70f62df07a70915d1a422edc96387ff8ec416e4248dc20dcf6`.
- Totals are **2,965 / 5,465 (54.25%)** overall and **2,391 / 4,789
  (49.93%)** in Game. See
  [Working Note 463](WORKING_NOTES/463-game-object-record-cleanup-match-20260929.md).

### Game accelerated-motion integrator byte-matched

- Replaced `func_1515B994`'s zero-return placeholder with its recovered
  timestep-based position and velocity integration and averaged-velocity
  secondary accumulation.
- Seventeen of 31 words emit directly from semantic C. Fourteen fail-closed
  expected-word guards preserve retail's equivalent floating-point register
  lifetimes and independent load/store schedule.
- The complete linked and pristine retail 124-byte spans share SHA-256
  `f22fcf8d8bea13e9b9dd8fb27fdbba4edc7b3382187883b96a8b59006e502b09`.
- Totals are **2,964 / 5,465 (54.24%)** overall and **2,390 / 4,789
  (49.91%)** in Game. See
  [Working Note 462](WORKING_NOTES/462-game-accelerated-motion-integrator-match-20260929.md).

### Game packed-byte submission wrapper byte-matched

- Completed `func_150721A4`, which splits `D_800D1580` into high, low, and
  middle bytes and submits them with the current object to `func_1506160C`.
- Extended `pad_c_object.py` to honor guarded word omission before deciding
  that an ordinary C function needs an overflow trampoline. A focused unit
  test covers contraction of an otherwise oversized function.
- Three guarded omissions remove redundant IDO moves; nine guarded
  replacements preserve retail's equivalent register allocation and call
  schedule. The linked and pristine retail 68-byte spans share SHA-256
  `23364d3eb1884f0df6cef21145f9029869c884555332de80fb722d6d2d36a2a0`.
- Totals are **2,963 / 5,465 (54.22%)** overall and **2,389 / 4,789
  (49.89%)** in Game. See
  [Working Note 461](WORKING_NOTES/461-game-packed-byte-submission-wrapper-match-20260929.md).

### Game zero-payload record dispatcher byte-matched

- Replaced `func_1514DAA4`'s zero-return placeholder with its recovered object
  flag update, two-zero-word payload allocation, payload copy, and event
  `0x13` dispatch.
- Twenty-seven of 29 words emit from semantic C. Two fail-closed expected-word
  guards reproduce retail's independent payload-size load and retained-object
  spill schedule around the allocator call.
- The linked ELF and pristine retail 116-byte spans share SHA-256
  `86252aec5532b02318f5211fd7a49240a496794ab58da9d4a86654495738b51b`.
- Totals are **2,962 / 5,465 (54.20%)** overall and **2,388 / 4,789
  (49.86%)** in Game. See
  [Working Note 460](WORKING_NOTES/460-game-zero-payload-record-dispatch-match-20260929.md).

### Game auxiliary-record reset byte-matched

- Replaced `func_1511A7C0`'s zero-return placeholder with its recovered
  auxiliary-record initialization and live-count float-array clear.
- The routine writes the enabled/state bytes, zeroes the current value, sets
  bounds `260.0f` and `100.0f`, and clears one float for every entry described
  by the owner's halfword count.
- All 30 words emit directly from semantic C, including retail's
  branch-likely loop and array-base reload, with no guarded replacements. The
  linked and pristine retail spans share SHA-256
  `5f44289b94c6d621b6172d793da5c279b95a7c0d83d380882901d219512b3654`.
- Totals are **2,961 / 5,465 (54.18%)** overall and **2,387 / 4,789
  (49.84%)** in Game. See
  [Working Note 459](WORKING_NOTES/459-game-auxiliary-record-reset-match-20260929.md).

### Game type-0x64 record allocator byte-matched

- Replaced `func_15104170`'s zero-return placeholder with its recovered
  `func_15167A68` allocation and record initialization.
- A successful allocation initializes the timer to `0xF`, clears two state
  bytes, retains the caller's two words, and stores the first argument as a
  selector byte. Correcting the function's contract to `void` removes an
  artificial return-value copy and reproduces retail's null path.
- All 29 words emit directly from semantic C with no guarded replacements.
  The linked and pristine retail spans share SHA-256
  `31cd26b3f8dc9d4dad65be176cb2da0a5c555d08a8d1db15f85f1df654543519`.
- Totals are **2,960 / 5,465 (54.16%)** overall and **2,386 / 4,789
  (49.82%)** in Game. See
  [Working Note 458](WORKING_NOTES/458-game-type64-record-allocator-match-20260929.md).

### Game actor-slot creation adapter byte-matched

- Replaced `func_150E32D0`'s zero-return placeholder with its recovered
  14-argument call to `func_150E3020`, including the retail zero/default
  fields, forwarded object value, and forwarded single-precision value.
- A nonnull result becomes the created actor's slot byte plus one; allocation
  failure remains zero. The complete 28-word routine emits directly from C
  with no guarded replacements.
- Its linked and pristine retail spans share SHA-256
  `0c4470a908e85d619883409c95c287e4b01e2232345c2f15cc6984cc0ab0588e`.
  Totals are **2,959 / 5,465 (54.14%)** overall and **2,385 / 4,789
  (49.80%)** in Game. See
  [Working Note 457](WORKING_NOTES/457-game-actor-slot-creation-adapter-match-20260929.md).

### Game coordinate-event wrapper twins byte-matched

- Replaced the zero-return placeholders for `func_150B3E74` and
  `func_150B3EE8` with their shared three-coordinate event-dispatch behavior.
- Both routines truncate the object floats at offsets `0x10`, `0x14`, and
  `0x18` to signed halfwords, call `func_1000FC18(0x221, ..., 0xFA0)`, and
  then invoke their distinct `func_151478F4` or `func_15147928` callback.
- All 29 words in each routine emit directly from semantic C with no guarded
  replacements. Their complete linked spans match retail with SHA-256
  `5d8fee60e1072f4d463b9ddb9aa49798d374ac0f46b921e80b13d684e0a013bc`
  and `c509e2d4d06f21b27f1e0706ca67b87e692c894f3e7569f9cd29098c5c75d7c1`.
- Totals are **2,958 / 5,465 (54.13%)** overall and **2,384 / 4,789
  (49.78%)** in Game. See
  [Working Note 456](WORKING_NOTES/456-game-coordinate-event-wrapper-twins-match-20260929.md).

### Game random remainder writer byte-matched

- Recovered `func_15084C30` as a type-`0x94` record updater that stores an
  unsigned random remainder as a float.
- Fourteen fail-closed guards omit one redundant object copy and normalize the
  record, remainder, and floating-point register cycle. All 128 linked bytes
  match SHA-256 `ff9cee201c305307e1a9da8857616d5e4b10753c2fb04df6464316c75d1fc6b2`.
- Totals are **2,956 / 5,465 (54.09%)** overall and **2,382 / 4,789
  (49.74%)** in Game. See [Working Note 455](WORKING_NOTES/455-game-random-remainder-writer-match-20260929.md).

### Game three-record dispatch loop byte-matched

- Replaced `func_15096D08`'s zero-return placeholder with its recovered
  mode-gated scan of the three records at `D_800D2DC0`.
- Unless `D_800C35EA` equals one, the routine visits records at a `0x24`-byte
  stride, calls `func_15096A68(index)` for each nonempty record, and exits on
  the first nonzero result.
- All 28 words, both global relocation pairs, and the call relocation emit
  directly from semantic C with no guards. Direct comparison matches all 112
  linked bytes with SHA-256
  `15e463f0914a3cd4f1ecc2d323f812dbe8bd443b83acd89e6e0859cccc283a0c`.
  Fresh totals are **2,955 / 5,465 (54.07%)** overall and
  **2,381 / 4,789 (49.72%)** in Game. See
  [Working Note 454](WORKING_NOTES/454-game-three-record-dispatch-loop-match-20260929.md).

### Game packed descriptor builder byte-matched

- Replaced `func_15095060`'s zero-return placeholder with its recovered typed
  construction of the packed descriptor at `D_800D2C90`.
- The routine optionally publishes that descriptor, selects either the source
  word or an entry indexed by `arg1 >> 8`, and copies two halfwords and three
  bytes from the source record.
- Thirty relocation-aware expected-word guards normalize IDO's repeated
  descriptor-address materialization, deferred table-index calculation,
  temporary-register lifetimes, and final return schedule. Six guarded source
  words are omitted, the final repeated address word is repurposed, and one
  trailing `nop` is inserted. The guards verify the compiler input and fail
  closed if it changes.
- The focused object matches all 29 retail words. Direct comparison matches all
  116 linked bytes with SHA-256
  `7e3c0b9009d0e83b9a405b6373de2aacc7545df9c12723db4fc78095317b0b55`.
  Fresh totals are **2,954 / 5,465 (54.05%)** overall and
  **2,380 / 4,789 (49.70%)** in Game. See
  [Working Note 453](WORKING_NOTES/453-game-packed-descriptor-builder-match-20260929.md).

### Game active-object state updater byte-matched

- Replaced `func_1507C370`'s zero-return placeholder with its recovered
  traversal of the active `D_800CC2D0` object range.
- Each non-null object state is passed to `func_1507C3E0` together with
  pointers to its adjacent halfwords at offsets `0x114`, `0x116`, and `0x118`.
- All 28 words, three global `HI16`/`LO16` relocation pairs, and the call
  relocation emit directly from semantic C with no guards. Direct comparison
  matches all 112 linked bytes with SHA-256
  `f76ebf3e5c54848c244a826c349a9b156683e93f088e363b88d3e31ccab607af`.
  Fresh totals are **2,953 / 5,465 (54.03%)** overall and
  **2,379 / 4,789 (49.68%)** in Game. See
  [Working Note 452](WORKING_NOTES/452-game-active-object-state-update-match-20260929.md).

### Game multi-argument forwarding wrapper byte-matched

- Replaced `func_1503F5B8`'s zero-return placeholder with its recovered typed
  call to `func_1505E0C4`.
- The wrapper forwards its object and two word arguments, reads the selector
  byte at object offset `0x3F5`, preserves two caller floats and the final
  stack word, and supplies the remaining selectors and floats as zero.
- All 29 words and the call relocation emit directly from semantic C with no
  guards. Direct comparison matches all 116 linked bytes with SHA-256
  `6398afee78289df1a106eeb809f135089e0481c1fcaa07602fb253bf3c7bea8a`.
  Fresh totals are **2,952 / 5,465 (54.02%)** overall and
  **2,378 / 4,789 (49.66%)** in Game. See
  [Working Note 451](WORKING_NOTES/451-game-multi-argument-forwarder-match-20260929.md).

### Game projection clamp byte-matched

- Reworked the two fallback paths in `func_15145548` to copy the complete
  three-float vector structures.
- The routine calls `func_1514563C` with either the supplied scalar output or
  a stack local, copies the first vector for a negative projection or failed
  query, and writes the first vector plus direction when the projection is
  above one.
- All 61 words and the helper-call relocation emit directly from semantic C
  with no guards. Direct comparison matches all 244 linked bytes with SHA-256
  `9c7a2fd3165ac85709a9677e3110a65943a5f92c9caa2cb1451fd8206fba2230`.
  Fresh totals are **2,951 / 5,465 (54.00%)** overall and
  **2,377 / 4,789 (49.63%)** in Game. See
  [Working Note 450](WORKING_NOTES/450-game-projection-clamp-match-20260929.md).

### Game timer and position updater byte-matched

- Replaced `func_15174920`'s zero-return placeholder with its recovered capped
  remaining-time calculation and signed position updates.
- The routine caps byte `0x3F` at 200, subtracts the unsigned product of
  `D_800BE9E4` and owner word `0x18`, clears halfword `0x38` if the result is
  negative, and otherwise accumulates owner word `0x14` into halfword `0x34`
  and its scaled seventh into halfword `0x36`.
- All 32 tracked words, including three trailing padding words, and both
  global relocations emit directly from semantic C with no guards. Direct
  comparison matches all 128 linked bytes with SHA-256
  `0db30d81a7b896df6df0ca76299e033339c2e26e5c5968b95a95105e84a194d6`.
  Fresh totals are **2,950 / 5,465 (53.98%)** overall and
  **2,376 / 4,789 (49.61%)** in Game. See
  [Working Note 449](WORKING_NOTES/449-game-timer-position-update-match-20260929.md).

### Game selector-transition dispatcher byte-matched

- Replaced `func_151AE06C`'s zero-return placeholder with its recovered
  admission query and requested/current selector transition.
- Corrected the selector argument types for `func_151AE264` and
  `func_151AE0E4`, restoring retail's byte spill/reload across the replacement
  call. Reversing the two independent source loads reproduces retail's
  temporary-register allocation.
- Twenty-nine of 30 words and all four call relocations emit from semantic C.
  One expected-word guard preserves retail's commutative equality-branch
  operand order. Direct comparison matches all 120 linked bytes with SHA-256
  `540db7d8ff6e8ae46dac27e83c1fdf131ce6275da182665eb858b303353d595c`.
  Fresh totals are **2,949 / 5,465 (53.96%)** overall and
  **2,375 / 4,789 (49.59%)** in Game. See
  [Working Note 448](WORKING_NOTES/448-game-selector-transition-dispatch-match-20260929.md).

### Game child-pointer release loop byte-matched

- Reworked `func_151BFB2C` into its recovered primary-pointer release and
  two-entry child-array cleanup.
- The loop keeps an `s32` counter but canonicalizes it through `u8` in the
  loop condition. Ordering the constant field offset before the scaled index
  also reproduces retail's commutative address-add operand order.
- All 30 words and both call relocations emit directly from semantic C with
  no guards. Direct comparison matches all 120 linked bytes with SHA-256
  `acd08cbda50fab15b1c03fdebaaa7f19e11a51276b5b6acf3021d19296910c95`.
  Fresh totals are **2,948 / 5,465 (53.94%)** overall and
  **2,374 / 4,789 (49.57%)** in Game. See
  [Working Note 447](WORKING_NOTES/447-game-child-pointer-release-loop-match-20260929.md).

### Game position-descriptor dispatch byte-matched

- Replaced `func_151C9AC0`'s zero-return placeholder with its recovered
  position-vector construction, object-descriptor generation, and dispatch.
- The source position uses owner X/Z and owner Y plus `2.0f`; reversing the
  two local declarations reproduces retail's descriptor-at-`0x20` and
  position-at-`0x44` stack layout.
- All 28 words and both call relocations emit directly from semantic C with
  no guards. Direct comparison matches all 112 linked bytes with SHA-256
  `2d6f3976e971d57fc7ab110f7482f6cfff0424a126dd67d0445621e88aeff3fe`.
  Fresh totals are **2,947 / 5,465 (53.92%)** overall and
  **2,373 / 4,789 (49.55%)** in Game. See
  [Working Note 446](WORKING_NOTES/446-game-position-descriptor-dispatch-match-20260929.md).

### Game command 0x1E record builder byte-matched

- Replaced `func_1518AB60`'s zero-return placeholder with its recovered
  command `0x1E` allocation, null return, and record initialization.
- The semantic body stores the full-width owner at offset `0x10`, clears the
  words at `0x14` and `0x18`, and stores the selector byte at `0x1C`.
- Twenty-six of 28 words emit directly from C. Two expected-word guards
  preserve retail's linked selector reload/store register allocation. Direct
  comparison matches all 112 linked bytes with SHA-256
  `efb71a2eeaa43131b257ca76adf61765cd193e36396339f8a3796fd61921b3d0`.
  Fresh totals are **2,946 / 5,465 (53.91%)** overall and
  **2,372 / 4,789 (49.53%)** in Game. See
  [Working Note 445](WORKING_NOTES/445-game-command-1e-record-builder-match-20260929.md).

### Game per-slot mode initializer byte-matched

- Replaced `func_15181D00`'s zero-return placeholder with its recovered zero
  and active-mode initialization paths across four parallel slot tables.
- A full-width `s32` mode parameter preserves retail's direct branch and final
  byte store. An initial `u8` signature was rejected because IDO emitted a
  three-word spill, mask, and reload sequence beyond the retail span.
- All 28 words and twelve relocations emit directly from semantic C with no
  guards. Direct comparison matches all 112 linked bytes with SHA-256
  `90db6f25d42c5e2c18435daace07fbcdebc254eb75f8fd653e55d38191e757f9`.
  Fresh totals are **2,945 / 5,465 (53.89%)** overall and
  **2,371 / 4,789 (49.51%)** in Game. See
  [Working Note 444](WORKING_NOTES/444-game-per-slot-mode-initializer-match-20260929.md).

### Game multiplayer-slot reset byte-matched

- Replaced `func_151298C0`'s zero-return placeholder with its recovered
  multiplayer-mode gate and per-player reset of the `0x24`-byte slot table.
- The routine clears the slot halfword at offset `2`, writes `-1.0f` at
  offset `4`, and copies `D_800A3610` to offset `8` for the player selected by
  `arg0->unk23D`.
- All 29 words and six relocations emit directly from semantic C with no
  guards. Direct comparison matches all 116 linked bytes with SHA-256
  `8fff14e7c9b648c89670a714b6e49fbbab7cecd3e055020618b33a3650abb410`.
  Fresh totals are **2,944 / 5,465 (53.87%)** overall and
  **2,370 / 4,789 (49.49%)** in Game. See
  [Working Note 443](WORKING_NOTES/443-game-multiplayer-slot-reset-match-20260929.md).

### Game record-ID lookup byte-matched

- Replaced `func_151149AC`'s zero-return placeholder with its recovered
  reserved-zero handling and bounded scan of the global `0xA0`-byte record
  table for a matching ID at offset `0x72`.
- Separate index, byte-offset, base, and cursor lifetimes reproduce retail's
  loop. Spelling the return as `offset + base` also preserves retail's
  commutative operand order.
- All 28 words and four relocations emit directly from semantic C with no
  guards. Direct comparison matches all 112 linked bytes with SHA-256
  `1d8d1610b05bc50bc8c25302965ca183b2a1f4d02e1f8697796056b2166b48f5`.
  Fresh totals are **2,943 / 5,465 (53.85%)** overall and
  **2,369 / 4,789 (49.47%)** in Game. See
  [Working Note 442](WORKING_NOTES/442-game-record-id-lookup-match-20260929.md).

### Game two-command record updater byte-matched

- Replaced `func_15109064`'s zero-return placeholder with its recovered
  command `0x1D` payload copy and command `0x1E` state-byte toggle.
- Twenty-six of 30 words emit directly from the semantic `switch`. Four
  guarded normalizations preserve one commutative address-add order and the
  explicit copy-path store, return, and delay-slot schedule.
- Direct comparison matches all 120 linked bytes with SHA-256
  `8072d145681a82314d4e37392823be0e48170fbc1897c198e8d46dd415a6e6f3`.
  Fresh totals are **2,942 / 5,465 (53.83%)** overall and
  **2,368 / 4,789 (49.45%)** in Game. See
  [Working Note 441](WORKING_NOTES/441-game-two-command-record-update-match-20260929.md).

### Game mode-gated table-value updater byte-matched

- Replaced `func_15108BC0`'s zero-return placeholder with its recovered
  owner-relative record lookup, `0x3E7` sentinel path, global mode-byte gate,
  and `0x44`-byte table-value lookup.
- Nineteen of 30 words emit directly from semantic C. Eleven guarded
  normalizations preserve retail's independent table-address/register
  schedule and insert its explicit table-path return-delay `nop`.
- Direct comparison matches all 120 linked bytes with SHA-256
  `87330ef5ce608175b955cbf82685645a8fc86b7a62ac1ca2c510672233bd943e`.
  Fresh totals are **2,941 / 5,465 (53.82%)** overall and
  **2,367 / 4,789 (49.43%)** in Game. See
  [Working Note 440](WORKING_NOTES/440-game-mode-gated-table-value-match-20260929.md).

### Game actor-indexed spatial-effect wrapper byte-matched

- Replaced `func_150FFB6C`'s zero-return placeholder with its recovered
  position forwarding, actor-index derivation, actor-halfword lookup, flag
  merge, and `func_1505D1C4` effect call.
- Explicit actor-index and halfword locals let IDO fill the signed-division
  latency with retail's independent loads before reading `mflo`.
- All 28 words emit directly from semantic C with no expected-word guards.
  Direct comparison matches all 112 linked bytes with SHA-256
  `df92d35779e03d460d880c2851953b934cce41d52f5cd14206ef8158e240a919`.
  Fresh totals are **2,940 / 5,465 (53.80%)** overall and
  **2,366 / 4,789 (49.40%)** in Game. See
  [Working Note 439](WORKING_NOTES/439-game-actor-indexed-spatial-effect-wrapper-match-20260929.md).

### Game two-slot resource cleanup byte-matched

- Replaced `func_150F739C`'s zero-return placeholder with its two-slot indexed
  release loop and final `func_1514EDF0` owner cleanup call.
- Non-null pointers at owner offsets `0x30` and `0x34` are released through
  `func_1516972C`; the pointer at `0x28` is then forwarded with the owner.
- Twenty-three of 28 words emit directly from semantic C. Five guarded words
  omit one redundant opening temporary and normalize a closed `v0`/`t8`
  counter-register cycle. Direct comparison matches all 112 linked bytes with
  SHA-256
  `2224059e793572ec1e461b485fa463d8ed184af981c738c15b8bdfc55d53bb6a`.
  Fresh totals are **2,939 / 5,465 (53.78%)** overall and
  **2,365 / 4,789 (49.38%)** in Game. See
  [Working Note 438](WORKING_NOTES/438-game-two-slot-resource-cleanup-match-20260929.md).

### Game fixed payload-setup wrapper byte-matched

- Replaced `func_150ECC00`'s zero-return placeholder with its recovered
  `func_151C9AC0` notification and `func_150ECA68` payload-setup calls.
- The second call uses the fixed tuple `0, 0xFF, 0, 0xFF, 4, -1` followed by
  the caller's selector and final word. Modeling the selector as volatile
  preserves retail's two independent stack-byte loads.
- All 28 words emit directly from semantic C with no expected-word guards.
  Direct comparison matches all 112 linked bytes with SHA-256
  `5af0f6f5ba18580c81f2287f4d54cfd6f25fcdea88f33ff5853d1733759c1c0b`.
  Fresh totals are **2,938 / 5,465 (53.76%)** overall and
  **2,364 / 4,789 (49.36%)** in Game. See
  [Working Note 437](WORKING_NOTES/437-game-fixed-payload-setup-wrapper-match-20260929.md).

### Game validated payload dispatcher byte-matched

- Replaced `func_150ECB8C`'s zero-return placeholder with its target-state and
  selector validation, shared owner invalidation, and payload dispatch.
- A valid target receives six local record bytes through `func_1502EA98`; an
  inactive target or selector mismatch writes `-1` to the owner's halfword at
  offset `0x0E`.
- All 29 words emit directly from semantic C with no expected-word guards.
  Direct comparison matches all 116 linked bytes with SHA-256
  `68df9f722f643d62ec6be026854fd09c8e361cb94615261afd64d54b6cee4240`.
  Fresh totals are **2,937 / 5,465 (53.74%)** overall and
  **2,363 / 4,789 (49.34%)** in Game. See
  [Working Note 436](WORKING_NOTES/436-game-validated-payload-dispatch-match-20260929.md).

### Game damped motion-state integrator byte-matched

- Replaced `func_150D13A0`'s zero-return placeholder with its five recovered
  floating-field updates and final `func_15059C84` state-refresh call.
- A minimal offset-accurate state type captures the position, velocity,
  scale, lift-position, and lift-velocity fields. The independent scale update
  precedes the lift-position update in source to preserve retail's IDO
  register lifetimes and instruction schedule.
- All 28 words emit directly from semantic C with no expected-word guards.
  Direct comparison matches all 112 linked bytes with SHA-256
  `e81264e9e1921d131d19d246e269c70b250ce8bf241825d6f1d6c3040ab3c090`.
  Fresh totals are **2,936 / 5,465 (53.72%)** overall and
  **2,362 / 4,789 (49.32%)** in Game. See
  [Working Note 435](WORKING_NOTES/435-game-damped-motion-state-integrator-match-20260929.md).

### Game subtype-2 single-byte allocation payload wrapper byte-matched

- Recovered `func_150D04C4`'s signed-halfword parameter and original
  eight-byte local payload buffer.
- The wrapper allocates a subtype-2 record through `func_150CFF10` and copies
  one zero byte into a successful allocation's payload destination.
- All 28 words emit directly from semantic C with no expected-word guards.
  Direct comparison matches all 112 linked bytes with SHA-256
  `245b46b27d2fe98769d605328c6ad1707b46c6e141b43780c8e4dda15ef79688`.
  Fresh totals are **2,935 / 5,465 (53.71%)** overall and
  **2,361 / 4,789 (49.30%)** in Game. See
  [Working Note 434](WORKING_NOTES/434-game-single-byte-subtype2-payload-match-20260929.md).

## 2026-09-28

### Game eight-byte allocation payload wrapper byte-matched

- Recovered `func_150D02B4`'s signed-halfword parameter and original 12-byte
  local record layout.
- The wrapper initializes a floating zero and halfword zero, allocates a
  subtype-1 record through `func_150CFF10`, and copies the local record's
  eight-byte prefix into a successful allocation's payload destination.
- All 30 words emit directly from semantic C with no expected-word guards.
  Direct comparison matches all 120 linked bytes with SHA-256
  `ce5cfca6e4c29e1436a90a321944d7eb038dcad21ec146b83f59457a56586ee8`.
  Fresh totals are **2,934 / 5,465 (53.69%)** overall and
  **2,360 / 4,789 (49.28%)** in Game. See
  [Working Note 433](WORKING_NOTES/433-game-eight-byte-allocation-payload-match-20260928.md).

### Game callback-gated record-state updater byte-matched

- Recovered `func_150D0034`'s signed callback-selector gate, optional indexed
  callback, failure-state write, and final status-bit clear.
- Volatile selector reads preserve retail's two independent byte loads and
  branch-likely schedule. Expressing the byte clear as promoted `~1` restores
  the original `0xFFFE` mask.
- All 35 words emit directly from semantic C with no expected-word guards.
  Direct comparison matches all 140 linked bytes with SHA-256
  `b7054a84fa9bb16c0971dd8874a53f7a6db60c6d57bad0ef1d65f8dc43239799`.
  Fresh totals are **2,933 / 5,465 (53.67%)** overall and
  **2,359 / 4,789 (49.26%)** in Game. See
  [Working Note 432](WORKING_NOTES/432-game-callback-gated-record-state-update-match-20260928.md).

### Game handwritten two-block word transform restored

- Replaced `func_150B1DB0`'s false zero-return C placeholder with its original
  28-word handwritten assembly body.
- The routine transforms two 64-bit words per iteration with retained mask
  bits and five-bit bidirectional shifts, stores both results, and advances
  through the caller's half-open range in 16-byte blocks.
- The original MIPS III `ld`/`sd` and `dsll`/`dsrl` operations, trapping
  `addi` pointer updates, and loop delay slot are preserved directly. All 112
  linked bytes match retail with SHA-256
  `dec18e02cec836269f4ceff6550b667ceaaaf0c2fbb06db63767cc62065ffcf2`.
- This ownership correction leaves the exact numerator at **2,932** while the
  C denominator becomes **5,465 (53.65%)** overall and **4,789 (49.24%)** in
  Game. See
  [Working Note 431](WORKING_NOTES/431-game-handwritten-two-block-word-transform-restoration-20260928.md).

### Game indexed halfword-sequence dispatcher byte-matched

- Replaced `func_15080784`'s zero-return placeholder with its nullable
  sequence gate, current/end byte-index comparison, optional halfword
  submission, and index advance.
- Nonzero sequence entries are forwarded to `func_1001263C` with arguments
  `0x7FFF` and `0x40`; zero entries are skipped while still advancing the
  current index.
- All 28 words emit directly from semantic C with no expected-word guards.
  Direct comparison matches all 112 linked bytes with SHA-256
  `f594c1f1cae3306800ce46b21fb1fccc6e04787a892f61d7011e3f63ee5f65b1`.
  Fresh totals are **2,932 / 5,466 (53.64%)** overall and
  **2,358 / 4,790 (49.23%)** in Game. See
  [Working Note 430](WORKING_NOTES/430-game-indexed-halfword-sequence-dispatch-match-20260928.md).

### Game floor-threshold state trigger byte-matched

- Reshaped `func_1506D6B4` around retail's two early exits, health-dependent
  state selection, packed `D_800D1580` update, and final `func_1506D584` call.
- The trigger ignores the sentinel floor value and floor values below the
  signed actor threshold. Otherwise it selects state byte `0x29` or `0x2C`,
  preserves the packed value's low 16 bits, and clears its middle byte.
- Thirty-two of 38 words emit directly from semantic C. Six expected-word
  guards normalize one commutative floating comparison operand order and one
  closed integer temporary-register cycle. Direct comparison matches all 152
  linked bytes with SHA-256
  `690e50073ee7d0d285273ab36186c7fea022fabf86b1a9ce25c9f2ee82b69a9c`.
  Fresh totals are **2,931 / 5,466 (53.62%)** overall and
  **2,357 / 4,790 (49.21%)** in Game. See
  [Working Note 429](WORKING_NOTES/429-game-floor-threshold-state-trigger-match-20260928.md).

### Game quaternion hemisphere normalizer byte-matched

- Replaced `func_15049C40`'s zero-return placeholder with its four-component
  dot product and conditional in-place quaternion negation.
- A negative dot product negates all four components of the second quaternion,
  selecting the equivalent representation in the same hemisphere as the
  first quaternion.
- All 30 words emit directly from semantic C with no expected-word guards.
  Direct comparison matches all 120 linked bytes with SHA-256
  `72c4d1b7cee3dc8bf2561bc11b2cb4068a34014c26038ac1ebf6060fbc9f2951`.
  Fresh totals are **2,930 / 5,466 (53.60%)** overall and
  **2,356 / 4,790 (49.19%)** in Game. See
  [Working Note 428](WORKING_NOTES/428-game-quaternion-hemisphere-normalizer-match-20260928.md).

### Game signed XZ coordinate query byte-matched

- Replaced `func_15045714`'s zero-return placeholder with its query-mode
  selection, signed X/Z coordinate conversion, and result store.
- The routine truncates position floats at offsets `0` and `8`, narrows both
  to signed 16-bit coordinates, and forwards them with the context and
  unsigned selector to `func_150A6500`.
- Twenty-four of 27 words emit directly from semantic C. Three expected-word
  guards normalize only the closed `v1`/`v0` position-pointer allocation
  cycle. Direct comparison matches all 108 linked bytes with SHA-256
  `84efd8a61af7f41170600c4e2a234589aa9723e0da7953b036a48ac0b383bb43`.
  Fresh totals are **2,929 / 5,466 (53.59%)** overall and
  **2,355 / 4,790 (49.16%)** in Game. See
  [Working Note 427](WORKING_NOTES/427-game-signed-xz-coordinate-query-match-20260928.md).

### Game gated active-object scan byte-matched

- Replaced `func_150347E8`'s zero-return placeholder with its global disable
  gate and fixed-stride scan across the object table.
- Each record with nonzero words at offsets `0` and `0x9C` is dispatched to
  `func_15034728`. The walk advances by `0x32C` bytes through the exclusive
  end marker at `D_800D121C`.
- All 30 words emit directly from semantic C with no expected-word guards.
  Direct comparison matches all 120 linked bytes with SHA-256
  `a559ebb0f27b18ffd2c9d3b1c9e7e0a43a4525d56175f4a5ba2269920502ad3b`.
  Fresh totals are **2,928 / 5,466 (53.57%)** overall and
  **2,354 / 4,790 (49.14%)** in Game. See
  [Working Note 426](WORKING_NOTES/426-game-gated-active-object-scan-match-20260928.md).

### Game signed record-command writer byte-matched

- Replaced `func_15034340`'s zero-return placeholder with its indexed record
  lookup, signed control-byte gate, and command-6 output writer.
- The record stride is `0x32C` bytes. A nonzero signed byte at offset `0x1D1`
  writes command 6 followed by that byte scaled by 200, then returns the
  four-byte-advanced output cursor; zero returns the original cursor.
- All 28 words emit directly from semantic C with no expected-word guards.
  Direct comparison matches all 112 linked bytes with SHA-256
  `529ddd228334416cf0838ce6bf9a03ff9cb7ec638c76c9ed12e5975534320d47`.
  Fresh totals are **2,927 / 5,466 (53.55%)** overall and
  **2,353 / 4,790 (49.12%)** in Game. See
  [Working Note 425](WORKING_NOTES/425-game-signed-record-command-writer-match-20260928.md).

### Game dual-layout owner release byte-matched

- Replaced `func_151CB49C`'s zero-return placeholder with its event-`0x21`
  direct-owner comparison and event-zero nested-owner comparison.
- Either matching path releases the input object through `func_1516972C`;
  every mismatch and unsupported event returns without side effects. An
  explicit referenced-object local reproduces retail's `v0/t0` allocation.
- All 29 words emit directly from semantic C with no expected-word guards.
  Direct comparison matches all 116 linked bytes with SHA-256
  `3232754db39e3f954bcc006026de28587b62ebe879fe65f461b4b3b2f1c4b870`.
  Fresh totals are **2,926 / 5,466 (53.53%)** overall and
  **2,352 / 4,790 (49.10%)** in Game. See
  [Working Note 424](WORKING_NOTES/424-game-dual-layout-owner-release-match-20260928.md).

### Game four-pointer cleanup byte-matched

- Replaced `func_151B222C`'s zero-return placeholder with its three-entry
  indexed pointer-release loop and final independent pointer release.
- The loop retains object offset `0x28` as its base and saves each nullable
  pointer before dispatch. An `s32` induction variable explicitly narrowed to
  `u8` after each increment reproduces retail's `s0` loop schedule.
- All 28 words emit directly from semantic C with no expected-word guards.
  Direct comparison matches all 112 linked bytes with SHA-256
  `dc75cd68d4c35a41ea0c10f1c33213c1ede085a635f7c5243bff33d6db63c063`.
  Fresh totals are **2,925 / 5,466 (53.51%)** overall and
  **2,351 / 4,790 (49.08%)** in Game. See
  [Working Note 423](WORKING_NOTES/423-game-four-pointer-cleanup-match-20260928.md).

### Game event callback-table dispatch byte-matched

- Replaced `func_15190550`'s zero-return placeholder with its event-`0x2A`
  pre-handler, object callback-table lookup, null gate, and three-argument
  forwarding call.
- The `u8` event formal reproduces retail's incoming canonicalization and the
  save/restore around the pre-handler. The typed nullable callback emits the
  complete `jalr` path directly; no expected-word guards are required.
- Direct comparison matches all 108 linked bytes with SHA-256
  `9193a39a64e3fed0ea5f093cf70ce6e95b41bc79c21f38a34ca894441df6fe66`.
  Fresh totals are **2,924 / 5,466 (53.49%)** overall and
  **2,350 / 4,790 (49.06%)** in Game. See
  [Working Note 422](WORKING_NOTES/422-game-event-callback-table-dispatch-match-20260928.md).

### Game mapped three-byte-row dispatch byte-matched

- Replaced `func_1517F3A0`'s zero-return placeholder with its selector mapping,
  zero-map passthrough, packed three-byte row lookup, and six-argument
  dispatch.
- Expressing the zero mapping as an early return reproduces retail's ordinary
  branch, passthrough delay slot, and shared epilogue. All 27 words emit
  directly from semantic C with no expected-word guards or profile override.
- Direct comparison matches all 108 linked bytes with SHA-256
  `bca8c2263f7d6ccb6f2a7572fc5ed850bef668670172b0d7be811a287aff4595`.
  Fresh totals are **2,923 / 5,466 (53.48%)** overall and
  **2,349 / 4,790 (49.04%)** in Game. See
  [Working Note 421](WORKING_NOTES/421-game-mapped-three-byte-row-dispatch-match-20260928.md).

### Game owned cleanup-list teardown byte-matched

- Replaced `func_15178DA4`'s zero-return placeholder with its resource stop,
  deletion-safe cleanup-list walk, owner-matched node releases, and final
  record teardown.
- Saving each next pointer before a possible node release preserves traversal.
  Function-scope local declaration order reproduces retail's `s0` lifetime and
  `sp+0x20` list-head spill. All 28 words emit directly from semantic C with
  no expected-word guards or compiler-profile override.
- Direct comparison matches all 112 linked bytes with SHA-256
  `4c71e7e00d926b0f5f3d26a468b5e9e78f540befe4c42b7e15adfaadd962c27f`.
  Fresh totals are **2,922 / 5,466 (53.46%)** overall and
  **2,348 / 4,790 (49.02%)** in Game. See
  [Working Note 420](WORKING_NOTES/420-game-owned-cleanup-list-teardown-match-20260928.md).

### Game record-mediated dispatch byte-matched

- Replaced `func_15173C90`'s zero-return placeholder with its narrowed record
  lookup, null gate, high-bit-cleared flag extraction, table-index calculation,
  and five-argument dispatch.
- The full-width third argument is narrowed only for `func_151149AC`, matching
  retail's call delay slot without changing the caller ABI. Semantic C emits
  26 words directly; two expected-word guards swap independent argument
  staging instructions into retail order.
- Direct comparison matches all 112 linked bytes with SHA-256
  `87de100270dfcecc257f5181f12efce8f30d295ee468b3eb7adc258d79683bc0`.
  Fresh totals are **2,921 / 5,466 (53.44%)** overall and
  **2,347 / 4,790 (49.00%)** in Game. See
  [Working Note 419](WORKING_NOTES/419-game-record-mediated-dispatch-match-20260928.md).

### Game resource-install callback byte-matched

- Replaced `func_15166F6C`'s zero-return placeholder with its global resource
  install and nine-argument setup dispatch.
- Recovering the four fixed callback arguments restores retail's `0x30` frame
  and incoming argument home slots. Passing `D_800DD228` after assigning it
  retains the destination base in `v0` and reproduces the complete retail
  schedule. All 27 words emit directly from C with no guards.
- Direct comparison matches all 108 linked bytes with SHA-256
  `1d8be5028b0b03a7fc525437b36e570682ceaee7ffb91eef469a9f4951f6ce44`.
  Fresh totals are **2,920 / 5,466 (53.42%)** overall and
  **2,346 / 4,790 (48.98%)** in Game. See
  [Working Note 418](WORKING_NOTES/418-game-resource-install-callback-match-20260928.md).

### Game coordinate-equality classifier byte-matched

- Replaced `func_15159230`'s zero-return placeholder with its unsigned mode
  canonicalization, three exact coordinate comparisons, and mismatch result
  selection.
- A complete coordinate match returns `0`. A mismatch returns `2` for modes
  `1` and `2`, and `1` for every other mode. Semantic C emits the comparison
  prefix directly; eleven expected-word guards retain retail's ordinary
  branches and shared return instead of IDO's equivalent branch-likely tail.
- Direct comparison matches all 136 linked bytes with SHA-256
  `8676af640e21d085de785f26264d34916e066fd5e94c6b0e763c9e9bd664fc8c`.
  Fresh totals are **2,919 / 5,466 (53.40%)** overall and
  **2,345 / 4,790 (48.96%)** in Game. See
  [Working Note 417](WORKING_NOTES/417-game-coordinate-equality-classifier-match-20260928.md).

### Game partial-zero payload allocator byte-matched

- Replaced `func_1514DA38`'s zero-return placeholder with its 28-byte local
  payload, allocation, copy into record offset `0x58`, and type-`0x13`
  dispatch.
- Retail zeroes payload words 5, 6, and 0 through 3 while intentionally
  leaving word 4 untouched. Declaring the saved result before the payload
  reproduces retail's `sp+0x34` result slot and `sp+0x18` payload base. All 27
  words emit directly from C with no guards.
- Direct comparison matches all 108 linked bytes with SHA-256
  `c742e2358884d79f9ae480d50e5725e72b6e7e7c5afe4ca285c9249045270546`.
  Fresh totals are **2,918 / 5,466 (53.38%)** overall and
  **2,344 / 4,790 (48.94%)** in Game. See
  [Working Note 416](WORKING_NOTES/416-game-partial-zero-payload-allocation-match-20260928.md).

### Game packed-resource lazy initializer byte-matched

- Replaced `func_15116110`'s zero-return placeholder with its empty-handle
  gate, packed selector and byte extraction, resource lookup, returned-handle
  store, and packed-source clear.
- Recovering the selector as `u16` and the two packed fields as `u8` restores
  retail's 27-word frame and argument staging. Semantic C emits 20 words
  directly; seven guards preserve one closed register/scheduling cycle among
  the three independent masks and two stack argument stores.
- Direct comparison matches all 108 linked bytes with SHA-256
  `d875f1fa9ab49b5c9f16a90e00a78da99489bcd27738cfee3ef6b462d6133135`.
  Fresh totals are **2,917 / 5,466 (53.37%)** overall and
  **2,343 / 4,790 (48.91%)** in Game. See
  [Working Note 415](WORKING_NOTES/415-game-packed-resource-lazy-init-match-20260928.md).

### Game record selector-bit test byte-matched

- Replaced `func_15114050`'s zero-return placeholder with its active-record
  gate, selector `-1` shortcut, and per-record selector-bit lookup.
- The routine derives the record index from the pointer difference divided by
  the `0xA0` record stride, then tests `1 << selector` in `D_800DBF94`. All 29
  words emit directly from semantic C with no guards or profile changes.
- Direct comparison matches all 116 linked bytes with SHA-256
  `b952efb961befdab310b53b58d5eb7f15e234ca2ecd12b28a014a1abdb02824d`.
  Fresh totals are **2,916 / 5,466 (53.35%)** overall and
  **2,342 / 4,790 (48.89%)** in Game. See
  [Working Note 414](WORKING_NOTES/414-game-record-selector-bit-test-match-20260928.md).

### Game float timer reset byte-matched

- Replaced `func_150E88C0`'s zero-return placeholder with its frame-delta
  subtraction, negative-timer random reseed, and follow-up event call.
- The timer at offset `0x28` is reset to `201.0f` plus a random value scaled by
  `D_800A1378`. All 28 words emit directly from semantic C with no guards or
  compiler-profile changes.
- Direct comparison matches all 112 linked bytes with SHA-256
  `94893d3fec01a0867260d976a9d1cdfd0153235d3a20289e838f3e3cffc7c4e5`.
  Fresh totals are **2,915 / 5,466 (53.33%)** overall and
  **2,341 / 4,790 (48.87%)** in Game. See
  [Working Note 413](WORKING_NOTES/413-game-float-timer-reset-match-20260928.md).

### Game float event-payload wrapper byte-matched

- Replaced `func_150E8854`'s zero-return placeholder with its event allocation,
  successful-allocation gate, and four-byte `10.0f` payload copy.
- Semantic C emits 25 of 27 words directly. Two expected-word guards move the
  local payload and its `memcpy` source address from IDO's `sp+0x34` choice to
  retail's equivalent `sp+0x30` slot.
- Direct comparison matches all 108 linked bytes with SHA-256
  `1e7751de0c93b1888850f728df5f0b90a89bcaa36e83dbabbfbaa07772aa5503`.
  Fresh totals are **2,914 / 5,466 (53.31%)** overall and
  **2,340 / 4,790 (48.85%)** in Game. See
  [Working Note 412](WORKING_NOTES/412-game-float-event-payload-match-20260928.md).

### Game single-byte allocation payload wrapper byte-matched

- Recovered `func_150D0134`'s narrow wrapper arguments and the shared
  pointer-returning `func_150CFF10` allocator signature.
- The wrapper requests allocation mode `8` with subtype `0`, then copies one
  zero byte into the allocated record's pointer at offset `0x48`. An eight-byte
  local payload buffer reproduces the retail `0x38` frame and `sp+0x30`
  payload address. All 27 words emit directly from C with no guards.
- Direct comparison matches all 108 linked bytes with SHA-256
  `0d1eadac7711e811b1e7d805fefe01989a18b564686543b50b1a9af057183856`.
  Fresh totals are **2,913 / 5,466 (53.29%)** overall and
  **2,339 / 4,790 (48.83%)** in Game. See
  [Working Note 411](WORKING_NOTES/411-game-single-byte-allocation-payload-match-20260928.md).

### Game global-gated parameter dispatcher byte-matched

- Replaced `func_150C7870`'s zero-return placeholder with its global gate and
  two state-selected calls to `func_1511650C`.
- The state flag selects arguments `(1, 0x353, 1000.0f)` or
  `(1, 0x43, 400.0f)`. Recovering the callee's `f32` fourth parameter prevents
  default promotion to `double` and restores the retail register-only call
  convention. All 28 words emit directly from C with no guards.
- Direct comparison matches all 112 linked bytes with SHA-256
  `e0afeec217c6d5c40f909dfb7f902188fd3bf85fd14216569996e8ff29e28cad`.
  Fresh totals are **2,912 / 5,466 (53.27%)** overall and
  **2,338 / 4,790 (48.81%)** in Game. See
  [Working Note 410](WORKING_NOTES/410-game-global-gated-parameter-dispatch-match-20260928.md).

### Game two-event command dispatcher byte-matched

- Replaced `func_150C19C0`'s zero-return placeholder with its command mapping
  and call to `func_15142314` through the owner pointer at offset `0x1D4`.
- Event `1` selects command `0x18`; event `2` selects command `0x15`. Retail
  has no default assignment, and the recovery preserves that contract. A
  two-case switch reproduces all 27 words directly from C with no guards.
- Direct comparison matches all 108 linked bytes with SHA-256
  `61edfab9f109b2b4bd29a04b5e856450a8fc8b4bff97757c439029055d77f36f`.
  Fresh totals are **2,911 / 5,466 (53.26%)** overall and
  **2,337 / 4,790 (48.79%)** in Game. See
  [Working Note 409](WORKING_NOTES/409-game-two-event-command-dispatch-match-20260928.md).

### Game event-linked object removal byte-matched

- Replaced `func_150BE150`'s zero-return placeholder with its two event-gated
  comparisons against the tracked pointer at object offset `0x28`.
- Event `0x21` compares the payload pointer directly; event zero compares the
  payload object's linked pointer at `0x318`. A match calls `func_1516972C` on
  the current object. An explicit payload local recovers the final three load
  and register-allocation words, allowing all 29 words to match without guards.
- Direct comparison matches all 116 linked bytes with SHA-256
  `84d13c435234d104c77b0fc196c0dc32333168538b30046bc6f3b95c2a208484`.
  Fresh totals are **2,910 / 5,466 (53.24%)** overall and
  **2,336 / 4,790 (48.77%)** in Game. See
  [Working Note 408](WORKING_NOTES/408-game-event-linked-object-removal-match-20260928.md).

### Game staged halfword ramp byte-matched

- Replaced `func_150B71A8`'s zero-return placeholder with its staged updates
  of signed halfwords at offsets `0x38` and `0x3A`.
- The first field advances by `D_800BE9E4 << 8` and clamps at `0x1000`; the
  second field begins only when the first was already complete. The semantic
  `if`/`else if` form emits all 30 words directly from C with no guards.
- Direct comparison matches all 120 linked bytes with SHA-256
  `829a2f70ead72049202fa8171e7aaa45b60323401d02e4842e5efa6c9e177acb`.
  Fresh totals are **2,909 / 5,466 (53.22%)** overall and
  **2,335 / 4,790 (48.75%)** in Game. See
  [Working Note 407](WORKING_NOTES/407-game-staged-halfword-ramp-match-20260928.md).

### Game indexed coordinate setter byte-matched

- Replaced `func_150A3444`'s zero-return placeholder with its three signed
  coordinate stores into an indexed 52-byte record in `D_800D3098`.
- Signed 16-bit parameters reproduce retail's incoming spills and sign
  extensions. Three direct member assignments preserve the repeated global
  table-pointer loads and emit all 27 words directly from C with no guards.
- Direct comparison matches all 108 linked bytes with SHA-256
  `ddbe910de039f583be412b8888b86891c0a3358c0585d2df05c2c3eccb302182`.
  Fresh totals are **2,908 / 5,466 (53.20%)** overall and
  **2,334 / 4,790 (48.73%)** in Game. See
  [Working Note 406](WORKING_NOTES/406-game-indexed-coordinate-setter-match-20260928.md).

### Game packed-record activation byte-matched

- Replaced `func_150A0264`'s zero-return placeholder with its 12-byte record
  lookup, active/secondary flag updates, destination clear, and packed-field
  replacement.
- The source-value load remains before the destination clear so aliased input
  preserves retail behavior. The semantic C matches the complete memory and
  control-flow schedule; 12 stale-checked expected-word guards normalize only
  a closed temporary-register allocation cycle.
- Direct comparison matches all 108 linked bytes with SHA-256
  `5d4825ac297505b071ef5aa2f75fee798810e57f3134845acde47bdabe72758b`.
  Fresh totals are **2,907 / 5,466 (53.18%)** overall and
  **2,333 / 4,790 (48.71%)** in Game. See
  [Working Note 405](WORKING_NOTES/405-game-packed-record-activation-match-20260928.md).

### Game resolved-object dispatch wrapper byte-matched

- Replaced `func_1509F5F4`'s empty placeholder with its object lookup, optional
  validation, and forwarding call to `func_10010344`.
- A nonzero sixth argument bypasses validation; otherwise dispatch requires
  `func_10010894` to return zero. The semantic short circuit and narrowed
  parameter types emit all 27 retail words directly from C with no guards.
- Direct comparison matches all 108 linked bytes with SHA-256
  `9239aa6a6b4788f6821422b9ce5c85dce833dc9fb1bc102ab1e18ccad7a4e820`.
  Fresh totals are **2,906 / 5,466 (53.17%)** overall and
  **2,332 / 4,790 (48.68%)** in Game. See
  [Working Note 404](WORKING_NOTES/404-game-resolved-object-dispatch-wrapper-match-20260928.md).

### Game seven-group byte canonicalizer byte-matched

- Replaced `func_15084D00`'s zero-return placeholder with its seven-group
  byte-table search over the input record's byte at offset four.
- A match returns the group's first byte; a complete miss returns the original
  byte. An `s32` cached value reproduces retail's register allocation, allowing
  all 28 words to emit directly from C with no guards.
- Direct comparison matches all 112 linked bytes with SHA-256
  `3b3e792efd6c29d299a34033d671ade846af96083c28773f36a40ab1e1006588`.
  Fresh totals are **2,905 / 5,466 (53.15%)** overall and
  **2,331 / 4,790 (48.66%)** in Game. See
  [Working Note 403](WORKING_NOTES/403-game-seven-group-byte-canonicalizer-match-20260928.md).

### Game owner status-byte clear byte-matched

- Replaced `func_150806A8`'s zero-return placeholder with its two guarded
  owner/state-byte clears at offsets `0x74` and `0x75`.
- Each byte is cleared only when nonzero and bit `0x80` is absent. Separate
  cached values and the alias-sensitive owner-pointer reload reproduce all 28
  retail words directly from C with no guards.
- Direct comparison matches all 112 linked bytes with SHA-256
  `3e9c20b8f2a2d5ac38c781068c7119d964c98007c366f73f9d6ad5a8987b754e`.
  Fresh totals are **2,904 / 5,466 (53.13%)** overall and
  **2,330 / 4,790 (48.64%)** in Game. See
  [Working Note 402](WORKING_NOTES/402-game-owner-status-byte-clear-match-20260928.md).

### Game two-word bit test byte-matched

- Replaced `func_1503E1F4`'s zero-return placeholder with its low/high flag-word
  selection and bit test over `D_800C6660[index]`.
- The high-word path relies on MIPS variable-shift masking, while a shared
  fallthrough return reproduces retail's branch-likely zero paths. All 27 words
  emit from semantic C with no guards.
- Direct comparison matches all 108 linked bytes with SHA-256
  `149a553e39a8961ded8d1eb039d1b56f8c176a2343f34c6f71d59b3db9055d29`.
  Fresh totals are **2,903 / 5,466 (53.11%)** overall and
  **2,329 / 4,790 (48.62%)** in Game. See
  [Working Note 401](WORKING_NOTES/401-game-two-word-bit-test-match-20260928.md).

### Game five-bucket byte canonicalizer byte-matched

- Replaced `func_1503D5F0`'s zero-return placeholder with directly indexed
  nested loops over five byte-table buckets.
- A match returns the bucket's first byte; no match returns the input. The
  `generated_6A3D0` slice now uses retail's no-unroll IDO profile, producing
  the frame-free 28-word routine without guards or collateral matcher losses.
- Direct comparison matches all 112 linked bytes with SHA-256
  `56c2590b5e3a77f9c9f80f334aa4e5736c07ef83de10fa409d160adf5948adf1`.
  Fresh totals are **2,902 / 5,466 (53.09%)** overall and
  **2,328 / 4,790 (48.60%)** in Game. See
  [Working Note 400](WORKING_NOTES/400-game-five-bucket-byte-canonicalizer-match-20260928.md).

### Game current-record vector copy byte-matched

- Replaced `func_1503A60C`'s zero-return placeholder with its destination
  pointer lookup and three floating-point component stores.
- The source keeps all three `D_800C3E78`-indexed expressions separate. IDO
  therefore preserves retail's alias-sensitive reloads after each indirect
  store and emits all 27 words directly without guards.
- Direct comparison matches all 108 linked bytes with SHA-256
  `2cc7a51561b11b95abf5d25dc8ea767973ece17d01457d2d7e71933cd8efb466`.
  Fresh totals are **2,901 / 5,466 (53.07%)** overall and
  **2,327 / 4,790 (48.58%)** in Game. See
  [Working Note 399](WORKING_NOTES/399-game-current-record-vector-copy-match-20260928.md).

### Game linked-list match dispatcher byte-matched

- Refined `func_150303E4`'s existing semantic reconstruction to recover its
  explicit zero-key return and retail linked-list pointer lifetimes.
- Each node's `next` pointer is captured before a matching node is passed to
  `func_15030158`, preserving traversal if that handler mutates the current
  node. The revised C emits all 33 words directly with no guards.
- Direct comparison matches all 132 linked bytes with SHA-256
  `5c1b5952bd66823179dfd610d3d9b5ba523126ca392c627190586bd569c251f3`.
  Fresh totals are **2,900 / 5,466 (53.06%)** overall and
  **2,326 / 4,790 (48.56%)** in Game. See
  [Working Note 398](WORKING_NOTES/398-game-linked-list-match-dispatcher-match-20260928.md).

### Game per-entry cleanup loop byte-matched

- Replaced `func_15022754`'s zero-return placeholder with its indexed,
  zero-based cleanup loop over `D_800C363A[index]` entries.
- The count is reloaded after every `func_150226BC(i, index)` call, preserving
  retail behavior if cleanup changes the bound. IDO emits the complete routine
  directly, including its branch-likely loop; no guards are required.
- Direct comparison matches all 104 linked bytes with SHA-256
  `37df4ff61f1705188a1a6f62ca49098bd2599db4c21f6962f81e7929ff52287b`.
  Fresh totals are **2,899 / 5,466 (53.04%)** overall and
  **2,325 / 4,790 (48.54%)** in Game. See
  [Working Note 397](WORKING_NOTES/397-game-per-entry-cleanup-loop-match-20260928.md).

### Game indexed 64-bit flag setter byte-matched

- Replaced `func_1501D258`'s zero-return placeholder with its global enable
  gate and indexed 64-bit bitset update.
- The typed `D_800C3A60[index] |= 1LL << bit` expression reproduces retail's
  `__ll_lshift` ABI, array addressing, and paired word stores directly. No
  expected-word guards are required.
- Direct comparison matches all 108 linked bytes with SHA-256
  `d290ae23b10b11613cb5737ff78c3b7a462bf6cecf9b78b88af3c5501959bedb`.
  Fresh totals are **2,898 / 5,466 (53.02%)** overall and
  **2,324 / 4,790 (48.52%)** in Game. See
  [Working Note 396](WORKING_NOTES/396-game-indexed-64-bit-flag-setter-match-20260928.md).

### Game packed-coordinate callback byte-matched

- Replaced `func_1518CCA8`'s zero-return placeholder with its packed X/Y
  coordinate update, zero-Z gate, and low-nibble callback-table dispatch.
- An explicit upper-half mask recovers retail's extraction shape. Ten scoped
  expected-word guards normalize only one closed temporary-register
  allocation cycle.
- Direct comparison matches all 120 linked bytes with SHA-256
  `11ea57903c0bc7e72ed5d68b72e52c9b0ee5039ab8344aa6068a6b527125e3e6`.
  Fresh totals are **2,897 / 5,466 (53.00%)** overall and
  **2,323 / 4,790 (48.50%)** in Game. See
  [Working Note 395](WORKING_NOTES/395-game-packed-coordinate-callback-match-20260928.md).

### Game entrypoint main loop byte-matched

- Replaced `func_15007830`'s zero-return placeholder with the complete Game
  startup sequence and permanent five-state dispatch loop.
- Corrected `D_800BEA68` to inline `struct195` storage and recovered the
  retail jump table, signed halfword parameters, event submission, and shared
  cleanup path.
- Sixty-six scoped guards normalize one closed IDO saved-register cycle and
  two omitted unreachable epilogue words. Direct comparison matches all 496
  linked bytes with SHA-256
  `35409e3b55dd3cc62229f6fe0dbb7d58cfa76db9b03e30b1dec4c8c621b22e90`.
  Fresh totals are **2,896 / 5,466 (52.98%)** overall and
  **2,322 / 4,790 (48.48%)** in Game. See
  [Working Note 394](WORKING_NOTES/394-game-entrypoint-main-loop-match-20260928.md).

### Game timed-record lifecycle byte-matched

- Recovered `func_1519EA04` as an enabled signed-timer update that optionally
  clears its owner's word at offset `0x30` before deleting the expired record.
- The corrected `void` routine reproduces all 29 retail words directly from
  semantic C. An explicit boolean/owner lifetime preserves retail's `v0`
  reuse without expected-word guards.
- Direct comparison matches all 116 linked bytes with SHA-256
  `8cbe4bb85537d3bd53f45bef0bfb83d5ccc0259c5fc02ed2b1863e8c60b05f45`.
  Fresh totals are **2,895 / 5,466 (52.96%)** overall and
  **2,321 / 4,790 (48.46%)** in Game. See
  [Working Note 393](WORKING_NOTES/393-game-timed-record-lifecycle-match-20260928.md).

### Game actor-target transform byte-matched

- Recovered `func_151A4E34` as a guarded actor-target transform that rejects
  null targets and actor type nibble `0xF`, indexes a 64-byte target row, and
  calls `func_15143134` with the caller's transform records.
- The 26-word semantic routine emits 25 words directly. One expected-word
  guard preserves only retail's commutative target-plus-index operand order.
- Direct comparison matches all 104 linked bytes with SHA-256
  `b509f6c7a3fe22a678e98f30ba1602b5bc741eab0666884c09469ef9fdbcab9a`.
  Fresh totals are **2,894 / 5,466 (52.95%)** overall and
  **2,320 / 4,790 (48.43%)** in Game. See
  [Working Note 392](WORKING_NOTES/392-game-actor-target-transform-match-20260928.md).

### Second Game object-ID state pair byte-matched

- Recovered `func_1519BEB8` and adjacent `func_1519BF20` as the second
  six-entry object-ID scan pair that clears or sets byte `0x14` in the
  selected `D_800E0900` row.
- The 26-word and 27-word semantic routines reproduce their complete retail
  control flow, schedules, delay slots, and relocations. Two expected-word
  guards per function normalize only the retained object-ID register.
- Direct comparisons match all 104 and 108 linked bytes. Fresh totals are
  **2,893 / 5,466 (52.93%)** overall and **2,319 / 4,790 (48.41%)** in Game.
  See
  [Working Note 391](WORKING_NOTES/391-game-second-object-id-state-pair-match-20260928.md).

### Game object-ID state pair byte-matched

- Recovered adjacent `func_151993E4` and `func_1519944C` as six-entry object-ID
  scans that select a row from `D_800E0900` and respectively clear or set its
  state byte at offset `0x14`.
- The 26-word and 27-word routines reproduce retail's post-tested loop,
  branch-likely schedule, delay slots, and relocations. Two expected-word
  guards per function normalize only the retained object-ID register.
- Direct comparisons match all 104 and 108 linked bytes. Fresh totals are
  **2,891 / 5,466 (52.89%)** overall and **2,317 / 4,790 (48.37%)** in Game.
  See
  [Working Note 390](WORKING_NOTES/390-game-object-id-state-pair-match-20260928.md).

### Game allocator-copy and setup pair byte-matched

- Recovered `func_15169900` as a `0x5E` record allocation followed by a
  null-gated 60-byte payload copy into the record at offset `0x10`.
- Recovered adjacent setup twins `func_1518E66C` and `func_1518E6D4` as typed
  seven-argument `func_1518D1C0` calls using selectors `3` and `4` and static
  descriptors `D_800A7460` and `D_800A749C`, followed by the shared record
  state stores.
- All three 26-word / 104-byte routines emit directly from semantic C with
  their retail frames, schedules, delay slots, and relocations. No expected-
  word guards or compiler overrides are required.
- Fresh totals are **2,889 / 5,466 (52.85%)** overall and
  **2,315 / 4,790 (48.33%)** in Game. See
  [Working Note 389](WORKING_NOTES/389-game-allocator-copy-and-setup-pair-match-20260928.md).

### Game packed-counter state update byte-matched

- Recovered `func_15168B44` as a typed volatile packed-counter update. The
  nonzero low-half path deliberately publishes the cleared upper half before
  merging the decremented low half, then refreshes the signed timer; the
  zero-low-half path consumes the upper count from the available byte when it
  fits.
- The semantic C reproduces the complete 26-word / 104-byte routine. Twenty
  expected-word guards normalize one closed IDO register-allocation and
  independent-instruction scheduling cycle; no relocation is changed.
- Fresh totals are **2,886 / 5,466 (52.80%)** overall and
  **2,312 / 4,790 (48.27%)** in Game. See
  [Working Note 388](WORKING_NOTES/388-game-packed-counter-state-match-20260928.md).

### Game display-list matrix pair byte-matched

- Recovered `func_15157F80` as two `gSPMatrix` appends: the fixed matrix at
  `D_80089470` and the indexed 64-byte matrix at `D_800DCC10`, followed by a
  ready-byte store and return of the advanced display-list cursor.
- The complete 26-word / 104-byte routine emits directly from semantic C. The
  F3DEX2 macro converts source flags `2` and `6` into retail command words
  `0xDA380003` and `0xDA380007`; no expected-word guards are needed.
- Fresh totals are **2,885 / 5,466 (52.78%)** overall and
  **2,311 / 4,790 (48.25%)** in Game. See
  [Working Note 387](WORKING_NOTES/387-game-display-list-matrix-pair-match-20260928.md).

### Game object-request builder byte-matched

- Recovered `func_1514F5CC` as a typed 28-byte stack request containing the
  object pointer, object ID, float parameter, count `20`, size `0x12C`, and
  mode `4`, followed by submission through `func_150C0AC0`.
- The complete 29-word / 116-byte routine emits directly from semantic C with
  the retail frame, store schedule, relocations, call delay slot, and implicit
  result convention. No expected-word guards or compiler override are needed.
- Fresh totals are **2,884 / 5,466 (52.76%)** overall and
  **2,310 / 4,790 (48.23%)** in Game. See
  [Working Note 386](WORKING_NOTES/386-game-object-request-builder-match-20260928.md).

### Game record ring-slot allocator byte-matched

- Recovered `func_1512D604` as an indexed record cursor that returns the old
  eight-byte slot, increments the cursor at offset `0xA8`, and wraps it to zero
  after slot 19.
- The semantic C reproduces the complete 26-word / 104-byte routine. Twenty
  relocation-aware expected-word guards preserve one closed IDO register
  allocation cycle while retaining both `D_800DC2B0` relocations.
- Fresh totals are **2,883 / 5,466 (52.74%)** overall and
  **2,309 / 4,790 (48.20%)** in Game. See
  [Working Note 385](WORKING_NOTES/385-game-record-ring-slot-match-20260928.md).

### Game byte-timer state byte-matched

- Recovered `func_1512D2F8` as a two-state byte timer driven by
  `D_800BE9E4` and bounded by the indexed `D_800DC290` duration table.
- An explicit state dispatch and compound byte update reproduce all 28 words /
  112 bytes directly from C, with no expected-word guards or compiler override.
- Fresh totals are **2,882 / 5,466 (52.73%)** overall and
  **2,308 / 4,790 (48.18%)** in Game. See
  [Working Note 384](WORKING_NOTES/384-game-byte-timer-state-match-20260928.md).

### Game object float-range update byte-matched

- Recovered `func_15121C00` as a typed six-argument object-field update followed
  by a scaled store from offset `0x37C` to offset `0x39C`.
- All 25 words / 100 bytes emit directly from semantic C, including the unused
  middle-float ABI spill, with no expected-word guards or compiler override.
- Fresh totals are **2,881 / 5,466 (52.71%)** overall and
  **2,307 / 4,790 (48.16%)** in Game. See
  [Working Note 383](WORKING_NOTES/383-game-object-float-range-update-match-20260928.md).

### Game indexed matrix compose byte-matched

- Recovered `func_15110360` as a three-angle matrix build followed by an
  in-place compose with the matrix at offset `0xBC` of an indexed `0x180`-byte
  global record.
- A typed record access reproduces retail's complete 26-word / 104-byte
  schedule directly from C, with no expected-word guards or compiler override.
- Fresh totals are **2,880 / 5,466 (52.69%)** overall and
  **2,306 / 4,790 (48.14%)** in Game. See
  [Working Note 382](WORKING_NOTES/382-game-indexed-matrix-compose-match-20260928.md).

### Game event-payload dispatcher byte-matched

- Recovered `func_15108FFC` as a local two-word descriptor copy and a payload
  containing two 32-bit values plus one byte, submitted as event `0x1D`.
- All 26 words / 104 bytes emit directly from semantic C with no expected-word
  guards or compiler-profile override.
- Fresh totals are **2,879 / 5,466 (52.67%)** overall and
  **2,305 / 4,790 (48.12%)** in Game. See
  [Working Note 381](WORKING_NOTES/381-game-event-payload-dispatch-match-20260928.md).

### Game dual event-byte dispatcher byte-matched

- Recovered `func_150F9720` as an eight-bit indexed lookup into four two-byte
  pairs followed by two command-`0x42` event submissions.
- The complete 26-word / 104-byte schedule emits from semantic C. Eleven
  expected-word guards normalize only IDO's eight-byte-larger event-buffer
  frame and affected stack slots; no relocation is changed.
- Fresh totals are **2,878 / 5,466 (52.65%)** overall and
  **2,304 / 4,790 (48.10%)** in Game. See
  [Working Note 380](WORKING_NOTES/380-game-dual-event-byte-dispatch-match-20260928.md).

### Game actor-position query byte-matched

- Recovered `func_150E36BC` as a one-based eight-slot actor query with a
  required type byte of `0x27`.
- The routine truncates the actor's three floating-point coordinates into
  caller outputs. All 31 words / 124 bytes emit directly from semantic C with
  no expected-word guards or compiler-profile override.
- Fresh totals are **2,877 / 5,466 (52.63%)** overall and
  **2,303 / 4,790 (48.08%)** in Game. See
  [Working Note 379](WORKING_NOTES/379-game-actor-position-query-match-20260928.md).

### Game record-output accessor byte-matched

- Recovered `func_150A3330` as a five-argument accessor over `0x34`-byte
  records reached through `D_800D3098`.
- All 26 words / 104 bytes emit directly from semantic C with no expected-word
  guards or compiler-profile override.
- Fresh totals are **2,876 / 5,466 (52.62%)** overall and
  **2,302 / 4,790 (48.06%)** in Game. See
  [Working Note 378](WORKING_NOTES/378-game-record-output-accessor-match-20260928.md).

### Game active-record counter byte-matched

- Recovered `func_1509CB68` as a four-record unrolled population count over
  the 204 records from `D_80087430` through `D_80088420`.
- The `generated_C9EC0` object now uses retail's no-unroll profile. Twenty-three
  of 27 words emit directly from semantic C; four relocation-aware guards
  preserve the independent opening schedule. All 108 bytes match retail.
- Fresh totals are **2,875 / 5,466 (52.60%)** overall and
  **2,301 / 4,790 (48.04%)** in Game. See
  [Working Note 377](WORKING_NOTES/377-game-active-record-counter-match-20260928.md).

### Game sequence-state advance byte-matched

- Recovered `func_1507F454`'s current-player state lookup, sequence cursor
  increment, byte-table lookup, and zero-terminator reset.
- Twenty-one of 27 words emit directly from semantic C. Six relocation-aware
  guards preserve retail's closed register-allocation cycle; all 108 bytes now
  match retail. The guard table has 1,667 rows and zero duplicate keys.
- Fresh totals are **2,874 / 5,466 (52.58%)** overall and
  **2,300 / 4,790 (48.02%)** in Game. See
  [Working Note 376](WORKING_NOTES/376-game-sequence-state-advance-match-20260928.md).

### Game record-value adjuster byte-matched

- Recovered `func_15034EB4`'s signed global scale, owner multiplier, indexed
  record subtraction, and optional second-record update.
- Twenty-six of 27 words emit directly from semantic C. One expected-word
  guard selects retail's equivalent operand order for a commutative `mul.s`;
  all 108 bytes now match retail. The guard table has 1,661 rows and zero
  duplicate keys.
- Fresh totals are **2,873 / 5,466 (52.56%)** overall and
  **2,299 / 4,790 (48.00%)** in Game. See
  [Working Note 375](WORKING_NOTES/375-game-record-value-adjuster-match-20260928.md).

### Game object-state filter byte-matched

- Recovered `func_15033F70`'s global disable gate and attached-object checks.
  Object types `0x0C` and `0x16`, null attachments, and state `3` are rejected;
  the accepted path clears the state byte and returns success.
- All 28 words and 112 bytes emit directly from semantic C with no
  expected-word guards. Independent linked and retail span hashes agree.
- Fresh totals are **2,872 / 5,466 (52.54%)** overall and
  **2,298 / 4,790 (47.97%)** in Game. See
  [Working Note 374](WORKING_NOTES/374-game-object-state-filter-match-20260928.md).

### Game display-list address relocator byte-matched

- Recovered `func_15004CE0` as an eight-byte command scan terminated by the
  signed `0xDF` opcode. Signed opcode loads, the unsigned byte-3 index, an
  indexed cursor, and the original double-read of the opening opcode restore
  the retail control flow and all memory behavior.
- Ten expected-word guards normalize only compiler register allocation and
  one commutative pointer-add operand order. All 28 words and 112 bytes now
  match retail; the guard table has 1,660 rows and zero duplicate keys.
- Fresh totals are **2,871 / 5,466 (52.52%)** overall and
  **2,297 / 4,790 (47.95%)** in Game. See
  [Working Note 373](WORKING_NOTES/373-game-display-list-address-relocator-match-20260928.md).

### Init channel-parameter updater byte-matched

- Corrected `func_1000CBF0`'s first two parameters from `s16` to the retail
  32-bit types and restored the original repeated `D_800417B0[i]` accesses.
- This removes a fixed-slot overflow trampoline and emits all 25 retail words
  directly, with no expected-word guards. It also preserves retail's full
  32-bit `arg1 == 0` test before the low-halfword stores.
- Fresh totals are **2,870 / 5,466 (52.51%)** overall and
  **393 / 495 (79.39%)** in Init. See
  [Working Note 372](WORKING_NOTES/372-init-channel-parameter-updater-match-20260928.md).

### Init hardware interrupt routine byte-matched

- Recovered `__osSetHWIntrRoutine` from the local libultra source: disable
  interrupts, install the handler in the hardware interrupt table, then
  restore the saved interrupt mask.
- Assigned the routine its retail `-O1` object profile. All 20 words and 80
  bytes now match directly with no expected-word guards.
- Fresh totals are **2,869 / 5,466 (52.49%)** overall and
  **392 / 495 (79.19%)** in Init. See
  [Working Note 371](WORKING_NOTES/371-init-hardware-interrupt-routine-match-20260928.md).

### Handwritten Init CP0/TLB routine restored

- Replaced `osMapTLBRdb`'s empty C placeholder with its original handwritten
  CP0/TLB assembly, preserving the `mfc0`, `mtc0`, and `tlbwi` sequence.
- All 22 instruction words and two slot-padding words match retail directly
  with no expected-word guards.
- The row correctly moves from C to raw assembly. Fresh totals are
  **2,868 / 5,466 (52.47%)** overall and **391 / 495 (78.99%)** in Init. See
  [Working Note 370](WORKING_NOTES/370-init-handwritten-maptlbrdb-restoration-20260928.md).

### Handwritten Init entrypoint restored

- Replaced `func_10001000`'s false zero-return C placeholder with its original
  handwritten startup clear-and-jump assembly.
- The routine deliberately uses `addi`, clears `0x16690` bytes in paired
  stores, installs the stack, and jumps indirectly into initialization. Its 14
  instruction words and six slot-padding words match retail with no guards.
- The row correctly moves from C to raw assembly. Fresh totals are
  **2,868 / 5,467 (52.46%)** overall and **391 / 496 (78.83%)** in Init. See
  [Working Note 369](WORKING_NOTES/369-init-handwritten-entrypoint-restoration-20260928.md).

### Game player-status row renderer byte-matched

- Completed all 427 words and 1,708 bytes of `func_151E966C`, reducing its
  linked mismatch from the reconstructed 415-word baseline to zero.
- Recovered the SDK display-list macro form, direct cursor lifetime, 32-bit
  player/count values, signed call conversions, shared row-center induction,
  and retail saved-register allocation. The unguarded semantic body reached
  the exact `0x6AC` extent with 116 persistent compiler-only differences.
- Added 116 relocation-aware expected-word guards for the remaining stack-slot,
  register-allocation and instruction-scheduling differences. Fresh totals are
  **2,868 / 5,468 (52.45%)** overall and **2,296 / 4,790 (47.93%)** in Game.
  See [Working Note 368](WORKING_NOTES/368-game-player-status-row-renderer-byte-match-20260928.md).

### Game team-counter panel byte-matched

- Completed the matching pass for 273-word `func_151E9D18`, reducing its
  linked mismatch from 178 words to zero while retaining semantic C.
- Restored retail's stack-local layout, conditional resource selection,
  32-bit loop/value lifetimes, explicit signed call conversion, and SDK
  `gDP*` display-list macros.
- Two expected-word guards exchange only the final independent record-load
  and end-pointer-add schedule. Fresh totals are **2,867 / 5,468 (52.43%)**
  overall and **2,295 / 4,790 (47.91%)** in Game. See
  [Working Note 367](WORKING_NOTES/367-game-team-counter-panel-byte-match-20260928.md).

### Game team-counter panel reconstructed

- Replaced `func_151E9D18`'s zero-return placeholder with semantic C for its
  texture selection, three total-aggregation modes, cached counters, paired
  panel rectangles, and two text calls.
- Correcting the accumulators to retail's 32-bit lifetimes removes redundant
  sign extensions and produces the exact `0x444` code extent. A retained
  debug-layout gap also restores the exact `0xA0` frame.
- The fresh mismatch falls from 272 to 178 of 273 words. Exact-function totals
  therefore remain unchanged. See
  [Working Note 366](WORKING_NOTES/366-game-team-counter-panel-reconstruction-20260928.md).

### Game player-status row renderer reconstructed

- Replaced `func_151E966C`'s zero-return placeholder with semantic C for its
  cached player counts, hidden-player mask, colored status rows, depleted gray
  boxes, missing-player icons, and texture/RDP setup.
- The body compiles to `0x698` bytes inside its fixed `0x6AC` span and uses
  retail's exact `0x100` frame. It remains non-matching at 415 of 427 words,
  so the exact-function totals do not change.
- Recovered the fourth and fifth arguments as `s8` and `u8`, including the
  texture-failure early returns and normal terminal pipe-sync. See
  [Working Note 365](WORKING_NOTES/365-game-player-status-row-renderer-reconstruction-20260928.md).

### Game HUD/status renderer reconstructed

- Replaced `func_151E89A0`'s zero-return placeholder with semantic C for its
  player-state scan, HUD masks, score digits, texture loads, status icons, and
  warning overlays.
- The reconstructed body uses retail's `0x158` frame and compiles to `0xC84`
  bytes within the fixed `0xCCC` slot. It remains non-matching at 803 of 819
  words, so the exact-function totals do not change.
- Corrected the generated draft's selected-player state from unsigned `255`
  to retail's signed `-1` sentinel. See
  [Working Note 364](WORKING_NOTES/364-game-hud-status-renderer-reconstruction-20260928.md).

### Game scaled scissored texture rectangle byte-exact

- Recovered all 175 words of `func_151E86E4` as the project-provided
  `gSPScisTextureRectangle` command writer wrapped by optional horizontal and
  vertical resolution scaling. It clips negative coordinates, adjusts the
  starting texture coordinates for clipping, emits the three-command texture
  rectangle sequence, and returns the advanced display-list pointer.
- The semantic wrapper and existing graphics macro reproduce the complete
  control flow, conversions, clipping arithmetic, command words, and exact
  extent. Four guarded words keep `D_8008FE20` in retail's `$f12` lifetime
  instead of IDO's equivalent `$f2`; the guard table now has 1,532 rows and
  zero duplicate keys.
- Linked and pristine 700-byte spans share SHA-256
  `5cb9c62ff81b996c5f05763db1290f2287e0c0b4b5e4fadb2da230c16f7ade0a`.
  Fresh totals are **2,866 / 5,468 (52.41%)** overall and
  **2,294 / 4,790 (47.89%)** in Game.

### Game display-list overflow guard byte-exact

- Recovered all 49 words of `func_151E8620`. It marks display-list activity,
  invokes the current mode callback when present, clears two mode-dependent
  state values, computes the emitted `Gfx` command count, and falls back to
  the original pointer when that count exceeds the configured limit.
- Semantic C reproduces the complete control flow, 32-byte frame, stack slot,
  pointer arithmetic, and explicit overflow boolean. Fourteen guarded words
  normalize only independent callback/original-pointer register lifetimes and
  post-call scheduling; no branch target, arithmetic operation, or call is
  changed. The guard table now has 1,528 rows and zero duplicate keys.
- Linked and pristine 196-byte spans share SHA-256
  `d830d34cd5e00f4d8d151f71bdd967086b13b71bfa9af6d7ac67f5ab76d41572`.
  Fresh totals are **2,865 / 5,468 (52.40%)** overall and
  **2,293 / 4,790 (47.87%)** in Game.

### Game mode-resource setup byte-exact

- Recovered all 92 words of `func_151E84B0`. It obtains a base result, passes
  it through the current mode callback when present, selects one of four
  resource-table indices from controller/runtime state, optionally performs
  color and resource setup, clears the active marker, and returns the result.
- Semantic C emits all behavior, control flow, calls, registers, stack slots,
  and scheduling directly. A retained declaration restores retail's local-
  slot gap; two guarded words normalize only IDO's resulting 40-byte frame to
  retail's 32-byte frame. The guard table now has 1,514 rows and zero
  duplicate keys.
- Linked and pristine 368-byte spans share SHA-256
  `dcce149dab839960d8e6ba7fec108cac61da0328fbf0f2d218fb53fbe974a341`.
  Fresh totals are **2,864 / 5,468 (52.38%)** overall and
  **2,292 / 4,790 (47.85%)** in Game.

### Game timed event transition byte-exact

- Recovered all 50 words of `func_151E83E8`. A zero cursor is changed to
  `-1` while event `0x1D` is registered; after the shared update and predicate
  path, timer `0x65` triggers cleanup, mode `1`, state clears, and event
  `0x21` dispatch.
- IDO emits all retail instructions directly from semantic C. No guarded
  words or relocation substitutions are needed; the guard table remains at
  1,512 rows with zero duplicate keys.
- Linked and pristine 200-byte spans share SHA-256
  `c9c159a99c0ca96242f08a223857956bcfa2753dbe34a25d1a0887d5dba4e964`.
  Fresh totals are **2,863 / 5,468 (52.36%)** overall and
  **2,291 / 4,790 (47.83%)** in Game.

### Game marker-table cursor byte-exact

- Recovered all 76 words of `func_151E82B8`. It handles the timed mode-nine
  transition, normalizes sentinel cursor states, scans the marker-pointer
  table to byte `0x2A`, handles a following `0x3D` terminator, and resets the
  transition timer.
- Semantic C emits every substantive retail instruction. One guarded word
  preserves only retail's commuted equality-branch operand order; the guard
  table now has 1,512 rows, zero duplicate keys, and exactly one row for this
  function.
- Linked and pristine 304-byte spans share SHA-256
  `4abd7ddbc182747cbd0d4604e7b7f6050d6e5c094ee70e2d4f30ee7f5cfeb0a7`.
  Fresh totals are **2,862 / 5,468 (52.34%)** overall and
  **2,290 / 4,790 (47.81%)** in Game.

### Game timed mode transition byte-exact

- Recovered all 41 words of `func_151E8214`. Outside mode `8`, it clears the
  transition timer while `func_1517EFDC` is false and, at timer `0xA1`, resets
  the input/state globals before selecting mode `8` and raising the transition
  flag.
- IDO emits all retail instructions directly from semantic C. No guarded words
  or relocation substitutions are needed; the guard table remains at 1,511
  rows with zero duplicate keys.
- Linked and pristine 164-byte spans share SHA-256
  `19b672f8cd503cffe4161a9ce5fab0e0b80c4f7177123ac0e88fa72b12ae2051`.
  Fresh totals are **2,861 / 5,468 (52.32%)** overall and
  **2,289 / 4,790 (47.79%)** in Game.

### Game object-slot spawn byte-exact

- Recovered all 163 words of `func_151E7F60`, including prior-object release,
  descriptor construction from object and position tables, object creation,
  scale/flag initialization, optional auxiliary allocation, and final setup.
- Semantic C emits every substantive retail instruction. Twenty-four guarded
  words normalize only IDO's 88-byte frame and local stack offsets to retail's
  80-byte layout; the guard table now has 1,511 rows and zero duplicate keys.
- Linked and pristine 652-byte spans share SHA-256
  `f4cfd6fbbab3328dad19b95e18360a746ca00efd75770c63d0d54cca12644440`.
  Fresh totals are **2,860 / 5,468 (52.30%)** overall and
  **2,288 / 4,790 (47.77%)** in Game.

### Game code-integrity checksum byte-exact

- Recovered `func_151E7EF8` as a call to the three-way state dispatcher
  followed by a word checksum over `func_151DDC20..func_151DE7D4`.
- A checksum mismatch against `0xBFC924E3` clears the first word of
  `osSpTaskLoad`. Explicit start and end locals reproduce retail's complete
  address setup and loop directly from C; no guard rows are needed.
- Linked and pristine 104-byte spans share SHA-256
  `e921d7cef916745ba7736417867809da191c952fad73becbf514d6f5f81be152`.
  Fresh totals are **2,859 / 5,468 (52.29%)** overall and
  **2,287 / 4,790 (47.75%)** in Game.

### Game state-transition dispatch byte-exact

- Recovered `func_151E4E00` as a state reset followed by mode `3` selection
  and a five-argument dispatch for event `0x1D`.
- The literal global-write sequence reproduces retail's first clear in the
  preceding call delay slot and its complete argument setup directly from C.
  No guard rows or relocation substitutions are needed.
- Linked and pristine 100-byte spans share SHA-256
  `b9e858200c78ed83eab87512429e3b959bd15e9e51b833ce8c5d90ce4e593b74`.
  Fresh totals are **2,858 / 5,468 (52.27%)** overall and
  **2,286 / 4,790 (47.72%)** in Game.

## 2026-09-27

### Game owned-state teardown byte-exact

- Recovered `func_151D13E0` as a null-gated teardown of the object stored at
  owner offset `0x30`: clear its state byte, update three flag bits, write
  halfword `0x28`, clear its linked record, and release the owner slot.
- Preserving retail's repeated owner-slot loads makes the entire 26-word leaf
  routine exact directly from C. No guard rows or relocation substitutions are
  needed.
- Linked and pristine 104-byte spans share SHA-256
  `0244d7b415296c133f4e777a20a9f3de1c752d82b13a12814a4e4a39beff5bec`.
  Fresh totals are **2,857 / 5,468 (52.25%)** overall and
  **2,285 / 4,790 (47.70%)** in Game.

### Game four-handler event broadcast byte-exact

- Recovered `func_151C9ED4` as an event-`0x21` broadcast of one stack record
  through four handlers, followed by a clear of `D_8008CD00`.
- The recovered C emits the complete call schedule, delay slots, saved-`s0`
  lifetime, and relocations. Four scoped rows preserve retail's 40-byte frame
  and local-record offset instead of IDO's 48-byte allocation.
- Linked and pristine 100-byte spans share SHA-256
  `0a54d1e0755c866e9e47eb8ad4f5481f02d22e423d506a4c40fcb667e2473918`.
  Fresh totals are **2,856 / 5,468 (52.23%)** overall and
  **2,284 / 4,790 (47.68%)** in Game.

### Game paired-record dispatch byte-exact

- Recovered `func_151B3040` as two calls over adjacent embedded records at
  object offsets `0x150` and `0x164`.
- An explicit embedded-record base and volatile byte argument reproduce
  retail's stack lifetime and second-call address reuse directly from C; no
  guard rows are needed.
- Linked and pristine 112-byte spans share SHA-256
  `06670f0bf180924a64312f13ccee3fc1eb5e2d3887c5bbe550a97d99609e7b87`.
  Fresh totals are **2,855 / 5,468 (52.21%)** overall and
  **2,283 / 4,790 (47.66%)** in Game.

### Game line-projection helper byte-exact

- Restored `func_1514563C`'s projection of a point onto a directed line,
  including its optional amount output and zero-length direction rejection.
- Reversing six commutative dot-product operands matches retail directly;
  eighteen scoped rows preserve the original leaf frame and final FP-register
  allocation.
- Linked and pristine 260-byte spans share SHA-256
  `19c6f8f57853c7b7d404c4ba8fe718d0c7cad42955a1b1ec2ea13d27680c730f`.
  Fresh totals are **2,854 / 5,468 (52.19%)** overall and
  **2,282 / 4,790 (47.64%)** in Game.

### Original handwritten floating PRNG restored

- Restored `func_150ADA68` from its maintained behavioral C equivalent to the
  original 25-word MIPS III assembly body. The C form compiled to 26 words and
  therefore occupied an out-of-line overflow section behind a trampoline.
- Retail shares the handwritten `func_150ADA20` seed transform instruction for
  instruction, then converts the low 16 bits to a scaled floating result.
- Linked and pristine 100-byte spans share SHA-256
  `65a5f1c67d8297c015c78583648d7a7e45bff89f98a13fe724ff0bdffe3ebe46`.
  The exact numerator remains **2,853**; fresh scans are
  **2,853 / 5,468 (52.18%)** overall and **2,281 / 4,790 (47.62%)** in Game.

### Game type-result selector byte-exact

- Restored `func_151928B0` as a type selector: types `0..4` write zero, type
  `0x53` writes one, and unsupported types return failure without writing.
- The generated-slice build retargets the compiler switch to retail's original
  five-entry `jtbl_800A8160_game`; four scoped rows retain the shared epilogue.
- The linked span has SHA-256
  `5df09e47be03d532d51cb3be24137de3e4bb65af2be2d7a3b7f6f83212c0fe88`.
  Fresh totals are **2,853 / 5,469 (52.17%)** overall and
  **2,281 / 4,791 (47.61%)** in Game.

### Game identity-gated event flag byte-exact

- Restored `func_151A931C` as matching-identity handling for event `0x17`
  bit-set and event `0x18` bit-clear operations on object byte `0x28`.
- Its real narrow-argument prototype makes caller `func_151A9024` exact
  directly, removing 13 old guard rows. Four scoped early-return rows remain
  on the target, shrinking the guard table by nine rows overall.
- The linked target span has SHA-256
  `446dc159df56fc710bf2b9167bf56038ddf19db80a6eb46cf527e64adf94fc15`.
  Fresh totals are **2,852 / 5,469 (52.15%)** overall and
  **2,280 / 4,791 (47.59%)** in Game.

### Game linked-record retirement byte-exact

- Restored `func_1519F48C` as state-specific linked-record field cleanup,
  link retirement, actor flag cleanup, and link-slot activation.
- Semantic C reproduces 21 of 25 retail words. Four function-scoped guard rows
  retain retail's shared `record + 0x58` base across the state tests and stores.
- The linked span has SHA-256
  `9f3cf4224facdf4f49be4bf99dc0f87c954f2ef38c2ac71c9b79044638c714e9`.
  Fresh totals are **2,851 / 5,469 (52.13%)** overall and
  **2,279 / 4,791 (47.57%)** in Game.

### Game bounded record-float update byte-exact

- Restored `func_1518804C` as a valid-index check, `[0.0f, 1.0f]` clamp, and
  first-float update in a 36-byte record array.
- The natural upper-bound and lower-bound branches reproduce all 29 retail
  words directly, including the branch-likely zero setup.
- The linked span has SHA-256
  `d102c486f94767caa8adbdc5fc2170ccb56a0e95f6014a82d00a657770ad278c`.
  Fresh totals are **2,850 / 5,469 (52.11%)** overall and
  **2,278 / 4,791 (47.55%)** in Game.

### Game conditional byte remap byte-exact

- Restored `func_15182768` as a signed-selector test followed by a six-argument
  `func_1517F08C` remap using bytes from the record at offset `0x28`.
- Updating the first argument in place reproduces all 26 retail words directly,
  including the branch-likely return and final register moves.
- The linked span has SHA-256
  `c37eb6ea3bc8d3f98df5b7f4ac3bccdd1305c56f1d5f1d5ee28761720e157638`.
  Fresh totals are **2,849 / 5,469 (52.09%)** overall and
  **2,277 / 4,791 (47.53%)** in Game.

### Game packed node update byte-exact

- Restored `func_15178C34` as a byte-ID lookup followed by two packed word
  stores and a signed halfword store into the selected node.
- Correcting the fifth parameter to `s16` reproduces all 26 retail words
  directly, including the stack halfword load, without matching guards.
- The linked span has SHA-256
  `d95e4bc7333312ac17d400f54e3868d3bb50f56992bf5da1252ddabd00477356`.
  Fresh totals are **2,848 / 5,469 (52.08%)** overall and
  **2,276 / 4,791 (47.51%)** in Game.

### Game owner-list unlink byte-exact

- Restored `func_1514ED8C` as an owner-head update, doubly linked-list splice,
  node release through `func_1516972C`, and saved payload return.
- Direct repeated link expressions reproduce all 25 retail words, including
  the branch-likely delay slots, without matching guards.
- The linked span has SHA-256
  `020ffa1b0ba6edd6dccd51c81dab466b8783efb6fd5e85ea7be8d6d0b47339be`.
  Fresh totals are **2,847 / 5,469 (52.06%)** overall and
  **2,275 / 4,791 (47.48%)** in Game.

### Game optional-owner callback dispatch byte-exact

- Restored `func_15141250` as an optional owner update, global active-count
  decrement, and indexed one-argument callback dispatch.
- Corrected `D_80089FE4` to its observed one-argument callback type and marked
  the owner pointer slot volatile so both retail loads remain visible.
- The linked span has SHA-256
  `6f88fbf60af2c237ad6c02abe4a3d6eafe680309efda564ab7cb569e09a6c72a`.
  Fresh totals are **2,846 / 5,469 (52.04%)** overall and
  **2,274 / 4,791 (47.46%)** in Game.

### Game reference-relative angle update byte-exact

- Restored `func_1511BE5C` as a signed-coordinate conversion, subtraction from
  the global reference position, `func_150484A0` angle calculation, and scaled
  float store.
- A direct typed expression reproduces all 24 retail words without matching
  guards, including the argument-conversion and call-delay schedule.
- The linked span has SHA-256
  `9e74ca5f6539068fb711027533d856fa8433fd8c3c3c6057e928c1e374ddca04`.
  Fresh totals are **2,845 / 5,469 (52.02%)** overall and
  **2,273 / 4,791 (47.44%)** in Game.

### Game cached-pointer fallback wrapper byte-exact

- Restored `func_1511BDF4` as a cached pointer lookup with a
  `func_15083E90` fallback, followed by a five-argument `func_1511BB04` call.
- Separate cached and selected pointer variables reproduce all 26 retail words
  directly, including the branch merge and fallback-call delay slot.
- The linked span has SHA-256
  `02175db4753159757ba782321d1a0c783f5c21a6323fb0b07ad06382f1c552b5`.
  Fresh totals are **2,844 / 5,469 (52.00%)** overall and
  **2,272 / 4,791 (47.42%)** in Game.

### Game paired matrix wrapper byte-exact

- Restored `func_151148A8` as two `func_150A8050` matrix constructions followed
  by an in-place `func_150A7A48` multiply.
- Typed matrix and three-float parameters reproduce all 25 retail words
  directly, with no matching guards.
- The linked span has SHA-256
  `1db33e9c444428eb5b1b54519defbdc5638d3fa048b9f9d332a1c4682915a410`.
  Fresh totals are **2,843 / 5,469 (51.98%)** overall and
  **2,271 / 4,791 (47.40%)** in Game.

### Game counted halfword release byte-exact

- Restored `func_1510D630` as a counted signed-halfword walker. It dispatches
  each entry through `func_1510D694` and releases the original allocation when
  the walk is complete.
- Explicit allocation, entry, and end aliases reproduce all 25 retail words
  directly, including saved-register lifetimes and loop branch operand order.
- The linked span has SHA-256
  `b9daef576d039ea0ae4a4688e13a98f687a438a57216ee6b3ca60d49774d7ed7`.
  Fresh totals are **2,842 / 5,469 (51.97%)** overall and
  **2,270 / 4,791 (47.38%)** in Game.

### Game byte-scaled dispatch byte-exact

- Restored `func_1510448C` as a signed-gate and record-byte dispatch helper.
  Its nonzero path scales byte `0x1B` by `63 / 256` and forwards the result to
  `func_1517F08C`; the two zero paths return the original first argument.
- Typed C reproduces 20 of 26 words. Six guarded words preserve retail's
  equivalent scaled-value and signed-gate temporary-register chains.
- The linked span has SHA-256
  `4f28f367f8ab43a3b00119126304196f2ace9b38088f5fe71694993340b6c9bf`.
  Fresh totals are **2,841 / 5,469 (51.95%)** overall and
  **2,269 / 4,791 (47.36%)** in Game.

### Game seven-argument forwarding wrapper byte-exact

- Restored `func_150FFCC8` as a five-argument wrapper that appends the global
  word in `D_8008FC8C` and byte addressed by `D_8008FC94` to its first call,
  then forwards a repeated pointer and mode `0x8003A` to its second call.
- The typed source reproduces all 25 retail words directly, including the
  caller-stack fifth argument and both call delay slots; no guards are needed.
- The linked span has SHA-256
  `5d1665206f529f78d841815deae9bea9fb5eb553f80dee8c15d26e5acc284415`.
  Fresh totals are **2,840 / 5,469 (51.93%)** overall and
  **2,268 / 4,791 (47.34%)** in Game.

### Game state-flag selector byte-exact

- Restored `func_150829D8` as an object state-flag selector. It clears the
  retail mask, sets bit `0x4`, and conditionally sets bit `0x2` according to
  the current game state and linked object's byte gate.
- The direct C switch reproduces all 27 retail words and uses the retained
  original 69-entry table at `jtbl_8009CC40_game`; no guarded words are needed.
- The linked span has SHA-256
  `77cdd4a69fb33b7fdbb9dff3a70e358f52fb924ad779f1e9d75c84743e46813d`.
  Fresh totals are **2,839 / 5,469 (51.91%)** overall and
  **2,267 / 4,791 (47.32%)** in Game.

### Game packed path-record writer byte-exact

- Restored `func_1507A100` as an indexed path-record halfword writer. It packs
  signed `D_800D1892` as the high byte with `D_800D1893` as the low byte and
  stores the result through the current object's path-table selection.
- The corrected pointer expression removes the old three-word compiler
  overflow and reproduces 19 of the 25 retail words directly. Six guarded
  register-allocation words preserve retail's equivalent final address chain.
- The linked span has SHA-256
  `8ad8feeacaca9d8b4ac2246da3caa2172958223c80920410221ea0dd92c9d4da`.
  Fresh totals are **2,838 / 5,469 (51.89%)** overall and
  **2,266 / 4,791 (47.30%)** in Game.

### Game aggregate forwarding wrapper byte-exact

- Restored `func_15049260` as a wrapper that receives and forwards one
  36-byte aggregate by value, replacing the incorrect nine-independent-word
  prototype.
- Typed C reproduces all 27 words / 108 bytes directly, including the four
  incoming register spills, three-word copy loop, restored argument
  registers, call delay slot, and epilogue. No guarded words are required.
- The linked span has SHA-256
  `cf413bcb9875e8025308d33beffc2313e7dd55575a4fe5a097c866357053ca3f`.
  Fresh totals are **2,837 / 5,469 (51.87%)** overall and
  **2,265 / 4,791 (47.28%)** in Game.

### Game indexed state initializer byte-exact

- Restored `func_1503F108` as an indexed state initializer: it writes `0x8C`
  into a 16-byte control record, writes `6` into the corresponding
  `0x32C`-byte object record, and stores `10.0f` through the control record's
  leading pointer.
- Typed C reproduces all 25 words / 100 bytes directly, including both
  strength-reduced index calculations, their interleaved scheduling, the
  field widths, and the floating-point store. No guarded words are required.
- The linked span has SHA-256
  `ae4ee765731e161dc2b0b5475eeb4d1f83d597aa03a16a75dd2b18002070592f`.
  Fresh totals are **2,836 / 5,469 (51.86%)** overall and
  **2,264 / 4,791 (47.26%)** in Game.

### Game record-byte classifier byte-exact

- Restored `func_1502EE8C` as a classifier for a byte in a `0x32C`-byte
  record: values `0..1` remain unchanged, `2..3` map to `0..1`, and values
  `4+` clamp to `2`.
- The complete 26-word / 104-byte span matches retail. Typed C reproduces the
  record-index multiplier, load, value/result register lifetimes, and return;
  six guarded words preserve retail's ordinary-branch CFG instead of IDO's
  branch-likely rewrite.
- The linked span has SHA-256
  `ad2f5842790e41297970334d3fa181230b0a119fb85bfae9eadcf2b0be9afcf3`.
  Fresh totals are **2,835 / 5,469 (51.84%)** overall and
  **2,263 / 4,791 (47.23%)** in Game.

### Game resource-size selector byte-exact

- Restored `func_1502DB20` as a resource-size selector over `D_800C4ED0`.
  Fourteen IDs return the table value minus four; every other ID returns the
  value unchanged.
- IDO reproduces all 25 words / 100 bytes directly from one switch, including
  the isolated ID 59 path and 64-entry `117..180` jump-table dispatch.
- Extended generated-slice padding with guarded compact-rodata retargeting and
  fixed `match_progress.py` so internal `.L` jump targets remain part of their
  enclosing function. Both paths have regression coverage.
- The complete linked span has SHA-256
  `d84d8b8a9ab78162b67744ee3f461014abf7ef58b7b51b398fb7b45d93819a29`.
  Fresh totals are **2,834 / 5,469 (51.82%)** overall and
  **2,262 / 4,791 (47.21%)** in Game.

### Game resource-entry reset byte-exact

- Restored `func_15023440` as a `struct163` reset helper with distinct release
  and active-resource refresh paths.
- All 25 words / 100 bytes match retail directly from structured C, including
  both branch-likely paths, saved-object lifetime across the calls, and the
  final leading-halfword reset. No guarded word patches are required.
- The complete linked span has SHA-256
  `a8d81a7d4b3a413a1f964ff45762715e657657e89cd4b13c1076393c346bf7a1`.
  Fresh totals are **2,833 / 5,469 (51.80%)** overall and
  **2,261 / 4,791 (47.19%)** in Game.

### Game four-handle cleanup byte-exact

- Restored `func_151D5E30` as a four-entry cleanup loop that calls
  `func_100043B4(handle, 3)` for each nonzero handle.
- All 24 words / 96 bytes match retail. Typed C reproduces the frame, saved
  registers, unsigned-byte loop counter, call, and epilogue; three guarded
  words preserve retail's retained-handle register and non-likely null-test
  schedule.
- The complete linked span has SHA-256
  `8a7230c21df7247d5bea3fff7fefbe01360547b2e816318b17bc6455f0914653`.
  Fresh totals are **2,832 / 5,469 (51.78%)** overall and
  **2,260 / 4,791 (47.17%)** in Game.

### Game mode-driven slot updater byte-exact

- Restored `func_151AE640` as a typed callback that clears a tracked slot in
  mode zero and swaps either member of a two-word pair in mode `0x2D`.
- All 28 words / 112 bytes match retail. Structured C reproduces the byte
  argument normalization, comparisons, branch-likely path, and slot writes;
  four guarded words preserve retail's zero-mode return scheduling and the
  two local branch targets shifted by its explicit delay-slot `nop`.
- The complete linked span has SHA-256
  `290f1de7726975b100bdf3b023d45174364d7fda0e0a2060cef19eeb052d4328`.
  Fresh totals are **2,831 / 5,469 (51.76%)** overall and
  **2,259 / 4,791 (47.15%)** in Game.

### Game fixed-scale transform copy byte-exact

- Restored `func_1519EF04` as a typed transform-copy helper that scales two
  source components by `10.0f` and copies two three-float vectors.
- All 27 words / 108 bytes match retail directly from C, including the
  constant load, floating-point hazard `nop`, and final return sequence. No
  guarded word patches are required.
- The complete linked span has SHA-256
  `538df983afbd767f37e9900031a7f0012a06eb70b77d7523a944083e8f40d98c`.
  Fresh totals are **2,830 / 5,469 (51.75%)** overall and
  **2,258 / 4,791 (47.13%)** in Game.

### Game scaled transform copy byte-exact

- Restored `func_1519ED24` as a typed transform-copy helper that applies the
  shared scale to two source components and copies two three-float vectors.
- All 24 words / 96 bytes match retail. The C reproduces the data flow; five
  guarded relocation-aware word entries preserve retail's independent setup
  scheduling at the function head.
- The complete linked span has SHA-256
  `c387b23efc90a3b66e61c6405b7a0f5c85193ede03ffef9e7a2aada0ba64fa01`.
  Fresh totals are **2,829 / 5,469 (51.73%)** overall and
  **2,257 / 4,791 (47.11%)** in Game.

### Game linked-position callback byte-exact

- Restored `func_1518E298` as a four-argument callback that validates its
  linked source and copies three truncated position floats into destination
  halfwords.
- All 28 words / 112 bytes match retail directly from C. The explicit unused
  parameters reproduce the frameless argument-home stores, while nested
  positive tests reproduce the shared default-return path. No guarded word
  patches are required.
- The complete span has SHA-256
  `394557df7bda8712ee5a6684d29ccf265f919731ac1f8b0acf9a200c004bc2da`.
  Fresh totals are **2,828 / 5,469 (51.71%)** overall and
  **2,256 / 4,791 (47.09%)** in Game.

### Game display-list state helper byte-exact

- Restored `func_1517EA4C` as a three-command `Gfx` helper using
  `gDPPipeSync`, `gDPSetCombine`, and `gDPSetOtherMode`.
- All 24 words / 96 bytes match retail directly from the standard macros,
  including macro-local temporary allocation and constant-load scheduling.
  No guarded word patches are required.
- The complete span has SHA-256
  `12a220ce6dd9bd2e40cbdc7e70533c694b619289159f5ca2f20418b1ddc74acf`.
  Fresh totals are **2,827 / 5,469 (51.69%)** overall and
  **2,255 / 4,791 (47.07%)** in Game.

### Game lifetime updater byte-exact

- Restored `func_15166204` as a signed halfword accumulator plus an unsigned
  byte lifetime countdown that destroys the object when the timer expires.
- All 25 words / 100 bytes match retail directly from C. Initializing the
  timer before the accumulator and spelling expiry as the primary branch
  reproduces retail's register lifetime, branch-likely form, and dead
  duplicate store without guarded word patches.
- The complete span has SHA-256
  `1a61744e11c39328ddee4adaaf1d193d7b88382e326b16990c76e93d61b2a689`.
  Fresh totals are **2,826 / 5,469 (51.67%)** overall and
  **2,254 / 4,791 (47.05%)** in Game.

### Game scaled fixed-point clamp byte-exact

- Restored `func_1515F040` as a two-stage signed float clamp followed by an
  in-place `65536.0f` scale, truncation, and indexed `D_800DCD10` store.
- All 27 words / 108 bytes match retail. Three guarded entries move the
  independent lower-bound `lui` into the first FP comparison slot and omit
  IDO's now-redundant hazard `nop`, matching the established sibling pattern.
- The complete span has SHA-256
  `df3794fced13b76134a228cb6d09226fb5de3e875ce14f3d7a43123269755d35`.
  Fresh totals are **2,825 / 5,469 (51.65%)** overall and
  **2,253 / 4,791 (47.03%)** in Game.

### Game category-29 identity filter byte-exact

- Restored `func_151640C0` around volatile ABI parameter slots and explicit
  record, object, owner, source-ID, and target-ID lifetimes.
- All 29 words / 116 bytes match retail. Structured C restores the category
  gate, three short-circuit identity checks, branch delay loads, and conditional
  `func_1516972C` call; nine guarded words preserve retail register allocation.
- The complete span has SHA-256
  `5c7f07b4183a17f6647dd6ac0b115f58ff60fa10d84f4c0c4e04f8ec6800c8b9`.
  Fresh totals are **2,824 / 5,469 (51.64%)** overall and
  **2,252 / 4,791 (47.00%)** in Game.

### Game integer range clamp byte-exact

- Restored `func_15143DA8` as a typed three-argument range clamp with its
  volatile pointer home slot, XOR-swap lifetime, cached comparison value, and
  distinct return codes for the lower and upper clamps.
- All 24 words / 96 bytes match retail. Structured C restores the complete
  branch and delay-slot layout; nine guarded words preserve IDO's retail local
  register allocation.
- The complete span has SHA-256
  `48fe80871bb5898a546f9cc24607c2e7623247fd8d33110039c6467297c2425a`.
  Fresh totals are **2,823 / 5,469 (51.62%)** overall and
  **2,251 / 4,791 (46.98%)** in Game.

### Game cached render-mode wrapper byte-exact

- Reshaped `func_15142FBC` around an explicit cache-difference update block and
  retained display-list command pointer.
- All 34 words / 136 bytes match retail. Structured C restores the cache-hit
  branch-likely return and command-pointer lifetime; three guarded words move
  the cursor increment and `D_800DD21C` HI16 setup across independent stores.
- The complete span has SHA-256
  `2f32966b66192dae3b5e58437d96dc69ea5606a1b676b41966996d9d980460ea`.
  Fresh totals are **2,822 / 5,469 (51.60%)** overall and
  **2,250 / 4,791 (46.96%)** in Game.

### Game typed eight-float forwarding wrapper byte-exact

- Replaced the zero placeholder at `func_15133760` with its destination plus
  eight-float forwarding call to `func_15142838`.
- All 24 words / 96 bytes match retail directly from C with no guarded words.
  The typed callee contract preserves single-precision arguments and naturally
  reproduces the mixed GPR/stack ABI, saved source pointer, and call schedule.
- The complete span has SHA-256
  `2f32a09575c94a5c410e4972036f77aa1e3f26d4f43cbe8b57f824663f5b4809`.
  Fresh totals are **2,821 / 5,469 (51.58%)** overall and
  **2,249 / 4,791 (46.94%)** in Game.

### Game nine-argument dual dispatcher byte-exact

- Replaced the zero placeholder at `func_1513164C` with its two-call
  dispatcher. It first sends arguments 5 through 9 to `func_15131514`, then
  sends arguments 1 through 4 plus argument 9 to `func_1513137C` and returns
  the second result.
- All 24 words / 96 bytes match retail directly from C with no guarded words.
  The nine-argument signature naturally reproduces the 32-byte frame, incoming
  argument home slots, stack-argument reloads, call delay slots, and epilogue.
- The complete span has SHA-256
  `d1f2ddb2fc806b978707ae893df837c78ef338cc51db51e04be4c5441ab7e941`.
  Fresh totals are **2,820 / 5,469 (51.56%)** overall and
  **2,248 / 4,791 (46.92%)** in Game.

### Game relative hierarchy-index lookup byte-exact

- Replaced the zero placeholder at `func_1510FE30` with its relative-offset
  hierarchy traversal rooted at `D_800DBE48`. Offset `+0xC` descends without
  changing the index; offset `+0x4` advances to a sibling and increments it.
- All 28 tracked words / 112 bytes match retail directly from C with no guarded
  words. A shared sibling pointer update reproduces the original branch-delay
  arithmetic, increment, null termination, and three trailing layout words.
- The complete span has SHA-256
  `3c50f9175be4aac89031574212071c25c6da4d7a2c0fb0759961dc2ad1761d74`.
  Fresh totals are **2,819 / 5,469 (51.55%)** overall and
  **2,247 / 4,791 (46.90%)** in Game.

### Game secondary object-eligibility predicate byte-exact

- Replaced the zero placeholder at `func_151028AC` with the secondary form of
  the object-eligibility predicate, using caller pointer/flag offsets
  `+0x170/+0x174`.
- All 29 tracked words / 116 bytes match retail directly from typed C with no
  guarded words. Its 26 executable words reproduce the selector, nested-owner,
  branch-likely, and flag-test schedule; generated-slice padding preserves the
  three trailing layout words.
- The complete span has SHA-256
  `46ddfc72dd6c62c3641e2897081b79a165585a68b99e031779e04614fe1b8279`.
  Fresh totals are **2,818 / 5,469 (51.53%)** overall and
  **2,246 / 4,791 (46.88%)** in Game.

### Game object-eligibility predicate byte-exact

- Replaced the zero placeholder at `func_1510281C` with its object-eligibility
  predicate. A matching selector requires a nested object whose owner's byte
  `+0x197` is clear; surviving paths return the low flag bit from the caller's
  byte `+0xD4`.
- All 26 words / 104 bytes match retail directly from typed C with no guarded
  words. Advancing the base pointer by `0x110` before addressing its selector
  at relative offset `+0x22` reproduces retail's pointer lifetime and exact
  branch-likely schedule.
- The complete span has SHA-256
  `3d65ee6d48fdac7191cf7ff9857fd9e97d6e2fae1a47af955cf3aaa91cd57994`.
  Fresh totals are **2,817 / 5,469 (51.51%)** overall and
  **2,245 / 4,791 (46.86%)** in Game.

### Game actor parameter initializer byte-exact

- Replaced the zero placeholder at `func_150FB188` with its actor-field and
  five-float stack-parameter initialization before calling `func_15157DEC`.
  It writes `-95.0f`, `-80.0f`, and zero to actor offsets `+0x54..+0x5C`,
  then forwards three zeros and two copies of `D_800A1DC0`.
- All 24 words / 96 bytes match retail. The typed C has retail's exact extent,
  frame, call, and return sequence; seventeen guarded words normalize the
  compiler's independent scheduling, FP lifetimes, and moved global relocation
  pair.
- The complete span has SHA-256
  `01144cdde22851e6ac89ae165b93f105ed789a3d297fd0e77e9773a11973a827`.
  Fresh totals are **2,816 / 5,469 (51.49%)** overall and
  **2,244 / 4,791 (46.84%)** in Game.

### Game script-gated high-flag wrapper byte-exact

- Replaced the zero placeholder at `func_150F52B0` with its script-dispatch
  wrapper. It calls `func_1509BE40(1, 0x401C, 6, 0x9000)` and sets or clears
  bit 31 of actor word `+0x84` according to the result.
- All 24 words / 96 bytes match retail directly from C with no guarded words.
  The direct branch reproduces the saved incoming pointer, call delay slot,
  branch-delay reload, high-bit materialization, and shared epilogue.
- The complete span has SHA-256
  `101a6dbcb8cea8393fd0b05a1b1b5018023f189c8b26d6ef52fcdd77a01a49e1`.
  Fresh totals are **2,815 / 5,469 (51.47%)** overall and
  **2,243 / 4,791 (46.82%)** in Game.

### Game actor-state byte selector byte-exact

- Replaced the zero placeholder at `func_150F1CB0` with its ordered actor-state
  selector. Halfword `+0x84` chooses byte `+0x68`; the low two bit-pairs of
  word `+0x2E4` choose and optionally override byte `+0x69`.
- All 24 words / 96 bytes match retail directly from C with no guarded words.
  The ordered stores naturally reproduce both branch delay slots and the
  alias-driven `+0x2E4` reload after writing byte `+0x69`.
- The complete span has SHA-256
  `56494e88f5d715bac816b14d0224f33c4a07cf1ea3a74785482ab275bc80ce51`.
  Fresh totals are **2,814 / 5,469 (51.45%)** overall and
  **2,242 / 4,791 (46.80%)** in Game.

### Game mapped record-active predicate byte-exact

- Replaced the zero placeholder at `func_150DF8C0` with its typed predicate.
  It maps indices `0..2` through rodata bytes `0x3B, 0x3C, 0x3D`, selects the
  corresponding `0x34`-byte record from runtime table pointer `D_800D3098`,
  and tests record byte `+0x14`.
- All 24 words / 96 bytes match retail directly from C with no guarded words.
  Modeling both the three-byte rodata object and record layout reproduces the
  original unaligned stack copy, relocations, strength reduction, and registers.
- The complete span has SHA-256
  `f561e7c6bf079ec34a150cf8de10d548606801d1bed3893c687a8c0cde77242b`.
  Fresh totals are **2,813 / 5,469 (51.44%)** overall and
  **2,241 / 4,791 (46.78%)** in Game.

### Game typed effect-spawn wrapper byte-exact

- Replaced the zero placeholder at `func_150C1660` with its typed wrapper around
  `func_1514C2F0`. It forwards three incoming float coordinates, supplies
  `80.0f` as the fourth float, and passes the fixed effect configuration plus
  the incoming low-byte selector through the eight stack arguments.
- All 24 words / 96 bytes match retail directly from C with no guarded words.
  The recovered `u8`/`s8`/`s16` stack contracts explain the callee's original
  big-endian byte and halfword loads while reproducing the caller schedule.
- The complete span has SHA-256
  `6f7f51e26c1e53fd7518734316f89e63941584f038798f4abac9b9875903ebad`.
  Fresh totals are **2,812 / 5,469 (51.42%)** overall and
  **2,240 / 4,791 (46.75%)** in Game.

### Game tagged table-value serializer byte-exact

- Replaced the zero placeholder at `func_150B58F0` with its typed four-byte
  serializer. Global mode 1 leaves the output cursor unchanged; other modes
  write tag `0x1A`, append a halfword selected from `D_800CC34A` using the
  incoming index and a `0x32C`-byte record stride, then advance the cursor.
- All 24 words / 96 bytes match retail directly from C with no guarded words.
  IDO emits the exact branch/return schedule and shift/add/sub strength
  reduction for the record stride.
- The complete span has SHA-256
  `f6d93c4607cecde125be160a07313bf365fe1f4ad166045b96596e0b31c52600`.
  Fresh totals are **2,811 / 5,469 (51.40%)** overall and
  **2,239 / 4,791 (46.73%)** in Game.

### Game counted object-dispatch loop byte-exact

- Replaced the zero placeholder at `func_1508434C` with its typed counted
  dispatch loop. It reads the unsigned count byte at object offset `0x2C9`,
  substitutes one when that byte is zero, and calls `func_150843AC` once for
  each index from zero through count minus one.
- All 24 words / 96 bytes match retail directly from C with no guarded words.
  The source reproduces retail's retained object/count/index registers,
  zero-to-one normalization, empty-loop guard, and branch-likely post-test.
- The complete span has SHA-256
  `83fcda040d8f514bb3346c5db1daf2b45d2f74d998f6dd88fca5175461716227`.
  Fresh totals are **2,810 / 5,469 (51.38%)** overall and
  **2,238 / 4,791 (46.71%)** in Game.

### Game complementary history-marker wrapper byte-exact

- Replaced the zero placeholder at `func_1507EE58` with its typed byte-history
  wrapper. It inserts the incoming marker into the five-byte history through
  `func_1507EEB8`, then inserts `0x12` after marker `0x11` or `0x11` after
  marker `0x12`.
- All 24 words / 96 bytes match retail directly from C with no guarded words.
  The `u8` argument contract reproduces the incoming home-slot reload, while
  the source-level `if`/`else if` emits both retail branch-likely paths, three
  call relocations, their delay slots, and the shared epilogue.
- The complete span has SHA-256
  `1d32e38706b456f78bb80f1980911262f13dc972b5e4ed4fd73191b10743c01f`.
  Fresh totals are **2,809 / 5,469 (51.36%)** overall and
  **2,237 / 4,791 (46.69%)** in Game.

### Game packed event-mask updater byte-exact

- Recovered the explicit byte lifetimes in `func_1507488C`: the packed event
  value selects an actor-local word at offset `0x2E4`, supplies an eight-bit
  mask, conditionally inverts its low-bit gate, and adds the signed top byte to
  actor byte `0x138` when that gate remains active.
- All 26 words / 104 bytes match retail. Twenty-two guarded words preserve the
  retail register and branch schedule while explicitly retaining both global
  relocations. A full rebuild exposed stale overflow output in neighboring
  `func_1506EE60`; its retained packed value and low-half ABI are corrected,
  and a guarded 19-word overflow replacement restores its retail dispatcher.
- The spans have SHA-256
  `9d7e011a25b9d1c74c33c0fbfd7b61ec7a2250fbbfdeb7a657dda5a69d7a7176`
  (`func_1507488C`) and
  `3bafca9eac8e0ba631d319f1ce8a96fe5562a95bfe3c6fc6bceb8990346ba13c`
  (`func_1506EE60`). Fresh totals are **2,808 / 5,469 (51.34%)** overall and
  **2,236 / 4,791 (46.67%)** in Game.

### Game signed-coordinate event wrapper byte-exact

- Replaced the zero placeholder at `func_15044D40` with its typed event-call
  wrapper. It converts signed coordinates at record offsets `0x6`, `0x8`, and
  `0xA` to floats, forwards the signed halfword at `0x10`, and calls
  `func_1505D1C4` with trailing arguments `0xFF, 0, 0, 0` before returning zero.
- All 24 words / 96 bytes match retail directly from C with no guarded words.
  The existing position/scale record layout plus the callee's eight-argument
  declaration reproduce the complete FP schedule, stack arguments, call delay
  slot, and explicit post-call zero result.
- The complete span has SHA-256
  `b848b28be2b8e6f198978fdef7b26edb1566def1a2068d1c50f1e59ab72c736a`.
  Fresh totals are **2,807 / 5,469 (51.33%)** overall and
  **2,235 / 4,791 (46.65%)** in Game.

### Game actor-position query wrapper byte-exact

- Replaced the zero placeholder at `func_1503F904` with its typed query
  wrapper. It truncates the actor coordinates at offsets `0x14` and `0x1C` to
  signed 16-bit values and calls `func_1503F800` on the embedded data at
  offset `0x320`, forwarding the selector and constant fifth argument `1`.
- All 24 words / 96 bytes match retail directly from C with no guarded words.
  The unused third incoming argument retains retail's ABI spill, while the
  five-argument call reproduces the frame, floating-point conversion schedule,
  call delay slot, and untouched return value.
- The complete span has SHA-256
  `69d25b286871e4066bd8dd2c0d9860c569f2f74a0e75e5cdd729956128995a62`.
  Fresh totals are **2,806 / 5,469 (51.31%)** overall and
  **2,234 / 4,791 (46.63%)** in Game.

### Game bounded record-byte lookup byte-exact

- Replaced the zero placeholder at `func_1503DA3C` with its indexed record
  lookup. It resolves one of the 187 pointers at `D_800D19A0`, rejects null or
  out-of-range entries with `0xFF`, and otherwise returns the requested byte
  from the optional buffer stored in the preceding `0x38`-byte header.
- All 24 words / 96 bytes match retail directly from C with no guarded words.
  The typed header reproduces the two tail fields, and a ternary nullable-byte
  expression preserves retail's joined `v1` result and branch-delay layout.
- The complete span has SHA-256
  `cd897bcd1ed09dca607a2f374dde0d76ecbdeb299e2806264d6f6a901876d3d3`.
  Fresh totals are **2,805 / 5,469 (51.29%)** overall and
  **2,233 / 4,791 (46.61%)** in Game.

### Game indexed flag predicate byte-exact

- Replaced the zero placeholder at `func_1503B95C` with its indexed flag
  predicate. It reads the flag byte at `D_800CC5CB[index * 0x32C]`, clears
  byte `0x4E` of the supplied record and rejects when bit `0x02` is set,
  rejects without mutation when bit `0x01` is set, and otherwise accepts.
- All 24 words / 96 bytes match retail directly from C with no guarded words.
  Keeping the zero-extended flag in a word-sized temporary reproduces retail's
  `v0` lifetime and complete branch/delay-slot shape.
- The complete span has SHA-256
  `65a1b3ed7d8a1c961d3a7383c20d10959fbe356696bf0083283342ae4c56ca85`.
  Fresh totals are **2,804 / 5,469 (51.27%)** overall and
  **2,232 / 4,791 (46.59%)** in Game.

### Game three-slot resource cleanup byte-exact

- Replaced the zero placeholder at `func_150233E4` with the recovered cleanup
  loop over the three `struct163` records at `D_800C3CA0`. Active records pass
  their resource pointer at offset `0x34` to `func_1516D2E0`, then clear that
  pointer and their leading active halfword.
- All 23 words / 92 bytes match retail. The shared record now exposes its
  signed active halfword and resource pointer while retaining its `0x38`-byte
  size; two relocation-aware guarded rows retain retail's independent table-end
  and cursor address-completion schedule.
- The complete span has SHA-256
  `34cb02339eb3c43068a7172810cbfbe8f197106b1f7574581056dc6d71f7f896`.
  Fresh totals are **2,803 / 5,469 (51.25%)** overall and
  **2,231 / 4,791 (46.57%)** in Game.

### Init owner-reference repair byte-exact

- Recovered `func_1000B294`, which walks the three root table entries and
  repairs matching owner links on each root and its `unk60` child by replacing
  the old owner token with the record's own address.
- All 24 words / 96 bytes match retail. An Init-object no-unroll profile and
  two relocation-aware guarded scheduling swaps reproduce the short retail
  loop; one dead initial load preserves IDO's retail register allocation
  without changing behavior.
- Neighboring `func_1000B548` remains exact across all 60 words after its
  compiler unroll was represented explicitly as four record probes per outer
  iteration. Fresh totals are **2,802 / 5,469 (51.23%)** overall and
  **391 / 497 (78.67%)** in Init.

### Game phase/scale updater byte-exact

- Recovered `func_151DADA0` around a typed state record embedded at object
  offset `0x110`. Its byte phase advances by signed rate times `D_800BE9E4`,
  the biased phase is converted through `func_151423D8`, and two state floats
  drive the output fields at offsets `0x4C` and `0x50`.
- All 34 words / 136 bytes match retail. The typed state produces the retail
  shared-base and complete floating-point schedule directly from C; four
  guarded rows retain retail's equivalent `a0` phase lifetime and explicit
  masked-argument move.
- The complete span has SHA-256
  `6723b622c69527ac88243bffdc7dc384d71bfc069638272ee12fce606ab64d8f`.
  Fresh totals are **2,801 / 5,469 (51.22%)** overall and
  **2,230 / 4,791 (46.55%)** in Game.

### Game extended record validity predicate byte-exact

- Replaced the zero-return placeholder at `func_151C2E94` with the recovered
  four-condition record predicate. It rejects the comparison record itself, a
  null leading word, ID byte `0xFF`, or extended ID byte `0xFF` at offset
  `0x127`; every other record returns one.
- All 23 words / 92 bytes match retail directly from C. The source-level early
  returns reproduce retail's branch-likely chain and duplicated delay-slot
  loads without guarded scheduling words.
- The complete span has SHA-256
  `3d887e9020b87ba223d5866416343f7fee5008bd84f8b0cfd34f972166b65edb`.
  Fresh totals are **2,800 / 5,469 (51.20%)** overall and
  **2,229 / 4,791 (46.52%)** in Game.

### Game indexed callback dispatcher byte-exact

- Replaced the zero-return placeholder at `func_151A9060` with its recovered
  object callback dispatcher. It sets object flag bit `0x04`, validates the
  signed index at offset `0x18` against the eight-entry table, and calls a
  nonnull table entry with the object and validated index.
- All 24 words / 96 bytes match retail directly from C. Restoring the callback
  as a two-argument function keeps the index live in `a1` and selects `v0` for
  the callback pointer, reproducing retail without guarded scheduling words.
- The complete span has SHA-256
  `f1dcb7d5d51145eba852cfa5ddc264f455e842703946e1ae431d42affd7d0c64`.
  Fresh totals are **2,799 / 5,469 (51.18%)** overall and
  **2,228 / 4,791 (46.50%)** in Game.

### Game linked-record event callback byte-exact

- Replaced the zero-return placeholder at `func_151A0950` with its recovered
  three-argument callback. Event `0xA` follows the link at object offset
  `0x98`; a nonnull record is accepted when either its owner word or ID byte
  matches the supplied descriptor, then `func_1519F48C` is called.
- All 25 words / 100 bytes match retail directly from C. Explicit link and
  owner lifetimes produce the retail event-branch delay slot, null
  branch-likely epilogue, comparison registers, and call relocation without
  guarded scheduling words.
- The complete span has SHA-256
  `33dcd9647ac0531f73903a0cf150dfec1dea4c1f0047fadccf54342cc478efbb`.
  Fresh totals are **2,798 / 5,469 (51.16%)** overall and
  **2,227 / 4,791 (46.48%)** in Game.

### Game timer/phase updater byte-exact

- Replaced the zero-return placeholder at `func_1517F7B4` with the recovered
  global timer and phase update. A nonzero 16-bit timer subtracts the frame
  delta with saturation at zero, then the 8-bit phase accumulator advances by
  speed times frame delta.
- All 24 words / 96 bytes match retail. The behavioral C and instruction shape
  compile directly; five guarded words retain retail's `a1` timer-base lifetime
  instead of IDO's otherwise equivalent `a0` allocation, including both
  checked timer relocations.
- The complete span has SHA-256
  `e2b43acfdd268d2a26e9aaa278219ebc73751ae9197e6e408b87412c964eef4d`.
  Fresh totals are **2,797 / 5,469 (51.14%)** overall and
  **2,226 / 4,791 (46.46%)** in Game.

### Game state-toggle event callback byte-exact

- Replaced the zero-return placeholder at `func_1514F130` with its recovered
  three-argument event callback. Event `0xD` clears the nested state byte at
  offset 9, event `0xE` sets it, and other events return the result of
  `func_1514E89C`.
- All 25 words / 100 bytes match retail directly from typed C. IDO naturally
  emits the retail branch-likely load, store delay slots, default call, and
  duplicated return-address loads; no guarded scheduling words are used.
- The complete span has SHA-256
  `63ea08e9138c95d21ba223d62a809f68cadb1a9455a21ae59f7a0b6841fef142`.
  Fresh totals are **2,796 / 5,469 (51.12%)** overall and
  **2,225 / 4,791 (46.44%)** in Game.

### Game object-request wrapper byte-exact

- Replaced the zero-return placeholder at `func_1514EE70` with the recovered
  callback ABI and typed eight-byte stack request. The wrapper forwards its
  object pointer, unique ID, zero byte, and 300-byte size to `func_1515BE50`,
  then passes the returned object to `func_1514EC1C` with event ID `0x16`.
- All 23 words / 92 bytes match retail directly from C. The frame, saved return
  address, argument home, request stores, delay slots, and both call
  relocations are compiler-produced; no guarded scheduling words are used.
- The complete span has SHA-256
  `b46f3cea976c6aa50753d281c7c1ca16951ec531127b624c67ab126b30c7af4c`.
  Fresh totals are **2,795 / 5,469 (51.11%)** overall and
  **2,224 / 4,791 (46.42%)** in Game.

### Game water-distance classifier byte-exact

- Replaced the uncertain raw-pointer implementation of `func_15125490` with a
  typed classifier over `struct108::unk3D0` and `struct127` water/position
  fields. It returns null outside water or below 100 units, the object from
  100 through 300 units, and sentinel one above 300 units.
- All 25 words / 100 bytes match retail. IDO emits a behaviorally equivalent
  26-word body with reversed `v0`/`v1` lifetimes, so 25 guarded slot rows
  replace the overflow trampoline and zero fill after checking their expected
  words and relocation state.
- The complete span has SHA-256
  `a5ffeceac1d9fab6316daf2b99daed9276cdbc0c1a0ff0b8a16f7a0cf9b696a6`.
  Fresh totals are **2,794 / 5,469 (51.09%)** overall and
  **2,223 / 4,791 (46.40%)** in Game.

### Game linked-record validator byte-exact

- Replaced the zero-return placeholder at `func_151002BC` with the recovered
  record validation, invalid-state sentinel, and optional child-state update.
- All 29 tracked words / 116 bytes match retail, including 26 executable words
  and three trailing layout nops. Seven guarded scheduling rows preserve the
  shared `-1` sentinel, ordinary invalid branches, and retail branch-likely
  child load without changing the recovered behavior.
- The complete span has SHA-256
  `fad101c81118abf40b4ecbf34251163af098d3f86db815a56c573d4216c7c90f`.
  Fresh totals are **2,793 / 5,469 (51.07%)** overall and
  **2,222 / 4,791 (46.38%)** in Game.

### Game event state/teardown handler byte-exact

- Replaced the zero-return placeholder at `func_150F4CFC` with the recovered
  `0x4E` state update and `0x4F` object teardown paths.
- All 24 words / 96 bytes match directly from C. A minimal typed record at
  object offset `0x170` preserves retail's separate base formation and flag
  access at record offset `0x24`, along with the original branch schedule.
- The complete span has SHA-256
  `5bb7259de0c805b8e28072d2011a451b4ec747eae9f5a5a69e5aacd1dc61f8c7`.
  Fresh totals are **2,792 / 5,469 (51.05%)** overall and
  **2,221 / 4,791 (46.36%)** in Game.

### Game paired-table dispatcher byte-exact

- Replaced the zero-return placeholder at `func_150DEC28` with the recovered
  byte-indexed dispatches through `D_800A0D0B` and `D_800A0D2B`.
- All 26 tracked words / 104 bytes match directly from C, including the
  23-word function body and three trailing layout nops. Its K&R byte-parameter
  definition preserves the original argument homes and narrowing without
  changing the already exact old-style caller.
- The complete span has SHA-256
  `631364ff57f69fc8abf662ae782237dd7fcdc1413a777d7270bda3ae3624c8f0`.
  Fresh totals are **2,791 / 5,469 (51.03%)** overall and
  **2,220 / 4,791 (46.34%)** in Game.

### Game event-key forwarder byte-exact

- Replaced the zero-return placeholder at `func_150D32FC` with the recovered
  event gate, object-key comparison, and four-argument record forwarder.
- All 25 tracked words / 100 bytes match directly from C, including the
  23-word function body and two trailing layout nops. A derived record pointer
  initialized before the short-circuit condition preserves retail's load,
  comparison, branch-likely, and call-argument schedule.
- The complete span has SHA-256
  `33eb62e07e9e46c86be7d1d80a40c3465c16c01b981521dbeef75de32cf2af44`.
  Fresh totals are **2,790 / 5,469 (51.01%)** overall and
  **2,219 / 4,791 (46.32%)** in Game.

### Game six-entry cleanup loop byte-exact

- Replaced the zero-return placeholder at `func_150D2054` with the recovered
  six-entry cleanup loop. Each non-null pointer in the object range at offsets
  `0x4C..0x60` is forwarded to `func_1516972C`.
- All 23 words / 92 bytes match directly from C. The byte-width loop update
  preserves retail's narrowing and branch-delay assignment, while indexed
  array syntax preserves the original commutative address operand order.
- The complete span has SHA-256
  `eeac0c230700015d8097afd16b38ab2414d2e649eff75b81f111f9843feccfaa`.
  Fresh totals are **2,789 / 5,469 (51.00%)** overall and
  **2,218 / 4,791 (46.30%)** in Game.

### Game object-index flag updater byte-exact

- Replaced the zero-return placeholder at `func_150D1410` with the recovered
  effect lookup and object-index flag update. A found effect receives byte
  `0x6E = 1` only for object-table index zero, otherwise zero.
- All 23 words / 92 bytes match directly from C. Expressing the equality as an
  explicit `if`/`else` restores retail's divide, branch-likely delay store, and
  duplicated fallthrough store without guarded words.
- The complete span has SHA-256
  `180399b2fd93bf50c1f85964a6bf46017f0bff06622fe9a97a30f2905101cff1`.
  Fresh totals are **2,788 / 5,469 (50.98%)** overall and
  **2,217 / 4,791 (46.27%)** in Game.

### Game object-record writer byte-exact

- Replaced the zero-return placeholder at `func_150BE438` with the recovered
  eight-byte record writer. It indexes `D_800CC2D0` by the `0x32C` object
  stride and writes constants `0x68` and `0x0E` around the truncated object
  fields at offsets `0x2E8` and `0x2E4`.
- All 23 words / 92 bytes match directly from C. Preserving the logical field
  assignment order reproduces retail's shift/add multiplication, load/store
  schedule, register allocation, and return without guarded words.
- The complete span has SHA-256
  `d484a1ceeb46dfcbb7716528fc3e1a2264d29e766db12234881c54607e94459a`.
  Fresh totals are **2,787 / 5,469 (50.96%)** overall and
  **2,216 / 4,791 (46.25%)** in Game.

### Game bounded-query wrapper byte-exact and function boundary corrected

- Split the former 26-word `func_150A6500` inventory row at the independent
  frame and return boundary at `0x150A6538`. The inventory now contains 6,041
  functions; `func_150A6538` remains exact original assembly until its unusual
  incoming stack contract can be recovered from source-grounded evidence.
- Replaced the public wrapper placeholder with C that forwards four register
  arguments, repeats the first two as stack arguments, and appends bounds
  `-10000` and `20000` before calling `func_150A6568`.
- All 14 words / 56 bytes of `func_150A6500` match. Twelve guarded scheduling
  words include a checked move of the call relocation to retail offset `0x20`.
  The span has SHA-256
  `be675159dec10194e305421bb202e9b9518ee517624b117e0f618135235deff0`.
  Fresh totals are **2,786 / 5,469 (50.94%)** overall and
  **2,215 / 4,791 (46.23%)** in Game.

### Game indexed-record lookup byte-exact

- Confirmed that the existing C for `func_1508855C` recovers the complete
  table-index calculation and active-record search behavior.
- All 36 words / 144 bytes match. Twenty-two guarded words preserve retail's
  register lifetimes and equivalent branch scheduling; the two guarded table
  address words preserve their original `D_800872A0` relocation identities.
- The complete span has SHA-256
  `8e59eaab129aa398368550fe589cf0991cec44face9740101ec18eb00a61c74d`.
  Fresh totals are **2,785 / 5,469 (50.92%)** overall and
  **2,214 / 4,791 (46.21%)** in Game.

### Game position/scale initializer byte-exact

- Replaced the false zero-return placeholder at `func_15044CE4` with its
  position copy, signed scale conversion, and downstream callback.
- All 23 words / 92 bytes match. Direct C emits the exact instruction skeleton;
  seven guarded words preserve retail's independent pointer and quotient
  register lifetimes without changing behavior or relocations.
- The complete span has SHA-256
  `37ca0b9557fb759016a6023c73fee1e8eb5acaf0ff92967480af03dd4bfabaf1`.
  Fresh totals are **2,784 / 5,469 (50.91%)** overall and
  **2,213 / 4,791 (46.19%)** in Game.

### Game variadic formatting wrapper byte-exact

- Replaced the false zero-return placeholder at `func_151EFF94` with its
  two-fixed-argument variadic formatter wrapper and successful-output null
  termination.
- All 23 words / 92 bytes match directly from C. Expressing the argument
  cursor as `&arg1 + 1` restores retail's four register homes, formatter reload,
  call setup, and return lifetime; no guarded retail words are needed.
- The complete span has SHA-256
  `21bed0d95f6457b0e0ebf8ba8b78072ed1f6f7883ef19bf31c9a327fbe457102`.
  Fresh totals are **2,783 / 5,469 (50.89%)** overall and
  **2,212 / 4,791 (46.17%)** in Game.

### Game position/effect wrapper byte-exact

- Replaced the false zero-return placeholder at `func_151B4E4C` with the
  established three-float position-vector wrapper shape.
- All 22 words / 88 bytes match directly from C. The wrapper forwards three
  additional floats and actor bytes `0x58` and `0x0C` to `func_151B4EA4`;
  no guarded retail words are needed.
- The complete span has SHA-256
  `9636d4a1dfde42444c22687e8308ebb8e17535d14b38bb150bd9a1628d5d31f3`.
  Fresh totals are **2,782 / 5,469 (50.87%)** overall and
  **2,211 / 4,791 (46.15%)** in Game.

### Game conditional child teardown byte-exact

- Replaced the false zero-return placeholder at `func_151A09B4` with its
  original byte-flag gate, child pointer or selector-byte match, and two-call
  teardown path.
- All 23 words / 92 bytes match directly from C, including the incoming byte
  home and narrowing, branch-likely early return, callback relocations, and
  delay slots. No guarded retail words are needed.
- The complete span has SHA-256
  `93bbe71ba0637f3ea71c346fa823b4f50f42adc38d076a45ae4ffa286dd09e22`.
  Fresh totals are **2,781 / 5,469 (50.85%)** overall and
  **2,210 / 4,791 (46.13%)** in Game.

### Game paired state-clear callbacks byte-exact

- Replaced the false zero-return placeholders at `func_1519F108` and
  `func_1519F168` with their original null-gated state-clear logic and distinct
  final callbacks.
- Both 24-word / 96-byte spans match independently. The readable C clears
  record words at `+0x58` for state 6 and `+0x60` for state 7; symmetric
  guarded scheduling restores retail's shared field base and branch targets.
- The spans have SHA-256
  `c30604a30fce7acfc9c4508dc25d815ae938bc8fb15c221b8351c2fe3f46b2c1`
  and `15a54430576641fbb8f849e8250fb8f39c1527d06c5829a84d6c89597d227412`.
  Fresh totals are **2,780 / 5,469 (50.83%)** overall and
  **2,209 / 4,791 (46.11%)** in Game.

### Game scaled query wrapper byte-exact

- Corrected `func_15197A0C` to accept its original incoming argument.
- The restored argument home supplies the one missing instruction; all 23
  words / 92 bytes then match directly from C with no guarded words.
- The complete span has SHA-256
  `79e00b19930e3d83d5baf14d43868c3332e63a76de73d420b1f301259a31d872`.
  Fresh totals are **2,778 / 5,469 (50.80%)** overall and
  **2,207 / 4,791 (46.07%)** in Game.

### Game callback/resource cleanup byte-exact

- Replaced the false zero-return placeholder at `func_151904BC` with its
  original release, callback-unregister, and resource-teardown sequence.
- All 23 words / 92 bytes match. Volatile pointer accesses preserve the
  conditional release reload, and local declaration order places the derived
  resource pointer in retail stack slot `0x18`. Five guarded words preserve
  the original null-branch and independent unregister-call setup schedule.
- The complete span has SHA-256
  `723d6af129190b4ac047acf1739e7f4abfc79a6eea5f78b62c342f3e6c336ee4`.
  Fresh totals are **2,777 / 5,469 (50.78%)** overall and
  **2,206 / 4,791 (46.04%)** in Game.

### Game paired endpoint update byte-exact

- Replaced the false zero-return placeholder at `func_1518A360` with its
  original marker-`0x2D` paired endpoint update.
- All 24 words / 96 bytes match. The recovered C swaps either matching source
  endpoint into object word `0x188` and carries source byte 8 or 9 into object
  byte `0x18D`; one guarded word selects retail's equivalent operand order for
  the second equality branch.
- The complete span has SHA-256
  `c49fa92800abfcf75e48c6d36597feb3d3c75ae58cb91fb76bb2d503beebd0ed`.
  Fresh totals are **2,776 / 5,469 (50.76%)** overall and
  **2,205 / 4,791 (46.02%)** in Game.

### Game enabled player-state initializer byte-exact

- Replaced the false zero-return placeholder at `func_15181D70` with its
  original per-player enabled-state initialization.
- All 22 words / 88 bytes match directly from C. The routine installs float
  constant `D_800A72B0`, zeroes the paired scalar and vector fields, and sets
  the player enable byte to one. No guarded retail words are needed.
- The complete span has SHA-256
  `9bc443d34ee264cb7c11bf0e6e84c6c9ca2dbd088fbb4005afd2514acd0ab072`.
  Fresh totals are **2,775 / 5,469 (50.74%)** overall and
  **2,204 / 4,791 (46.00%)** in Game.

### Game player-timer decay byte-exact

- Replaced the false zero-return placeholder at `func_1517F75C` with its
  original inclusive per-player timer decay loop.
- All 22 words / 88 bytes match directly from C. Each unsigned halfword timer
  through player index `D_80082FA0` loses the frame delta while larger than
  that delta and otherwise clamps to zero. No guarded retail words are needed.
- The complete span has SHA-256
  `4c14539ad1ebebefc3d10023afc401e7b495ec1001efaf6d0ef4ad5cbc26c7c3`.
  Fresh totals are **2,774 / 5,469 (50.72%)** overall and
  **2,203 / 4,791 (45.98%)** in Game.

### Game wrapped timer/counter byte-exact

- Replaced the false zero-return placeholder at `func_151749A0` with its
  original byte-width timer and counter update.
- All 22 words / 88 bytes match directly from C. The timer accumulates the
  frame delta with byte wrapping; crossing its threshold advances the wrapped
  counter, wraps that counter at the caller's limit, and clears the timer. No
  guarded retail words are needed.
- The complete span has SHA-256
  `1ef04391b9f03b0528bc0f1c4f9d39ed6df05e2f7125a49e456853d8507445cd`.
  Fresh totals are **2,773 / 5,469 (50.70%)** overall and
  **2,202 / 4,791 (45.96%)** in Game.

### Game object state transition byte-exact

- Replaced the false zero-return placeholder at `func_15172D28` with its
  original object state-transition behavior.
- All 22 words / 88 bytes match directly from C. The routine calls
  `func_15085430`, clears flag bit `0x10` at offset `0x2F8`, and, when the
  global mode byte is zero, writes state `3` through the object pointer at
  offset `0x31C`. No guarded retail words are needed.
- The complete span has SHA-256
  `f285d4661242ecf09be7ab29f754180e339c667a1036330afba8d6c07bd7473a`.
  Fresh totals are **2,772 / 5,469 (50.69%)** overall and
  **2,201 / 4,791 (45.94%)** in Game.

### Game two-table initializer byte-exact

- Replaced the false zero-return placeholder at `func_15172C50` with its
  original 16-entry table initialization behavior.
- All 22 words / 88 bytes match directly from C. The source assigns `-1` and
  zero to corresponding bytes in `D_800DD2B0` and `D_800DD2C0`, then stores
  the caller's value in the second table's first byte. IDO produces retail's
  four-way unrolled loop and branch-delay store. No guarded words are needed.
- The complete span has SHA-256
  `276590b6fd1af72abb45e1b76d352b988397165f8e9a5e69598a41a213e8465a`.
  Fresh totals are **2,771 / 5,469 (50.67%)** overall and
  **2,200 / 4,791 (45.92%)** in Game.

### Game effect callback adapter byte-exact

- Replaced the false zero-return placeholder at `func_15159BB0` with its
  original seven-slot callback adapter.
- All 22 words / 88 bytes match directly from C. The routine builds a position
  vector from its first three float arguments, supplies a zero velocity, and
  forwards bytes `0x0C` and `0x01` from the effect record to `func_15159890`.
  No guarded retail words are needed.
- The complete span has SHA-256
  `4ca84258ab41695df242af9177bdc89d911377839c1cc187058020c2c4d30d88`.
  Fresh totals are **2,770 / 5,469 (50.65%)** overall and
  **2,199 / 4,791 (45.90%)** in Game.

### Game signed-key list search byte-exact

- Replaced the false zero-return placeholder at `func_1514ECE0` with its
  original linked-list search by signed halfword key.
- All 23 words / 92 bytes match directly from C. The typed `s16` parameter
  reproduces retail's entry sign extension, and the existing `GameListNode`
  layout reproduces the branch-likely loop and optional result store. No
  guarded retail words are needed.
- The complete span has SHA-256
  `b86fa571f8372f319a0e24df91da420b10ef6e0d1478b06f8741b62923391112`.
  Fresh totals are **2,769 / 5,469 (50.63%)** overall and
  **2,198 / 4,791 (45.88%)** in Game.

### Game float damping threshold byte-exact

- Replaced the false zero-return placeholder at `func_15149BF4` with its
  original two-axis damping and minimum-threshold behavior.
- All 25 words / 100 bytes match directly from C. In-place updates force the
  stored first result to be reloaded, while one short-circuit OR reproduces
  retail's shared return-zero path. No guarded retail words are needed.
- The complete span has SHA-256
  `035239563829978bd71d6f260e062841506d078a1d0c22061d7c40fe8c5c24f4`.
  Fresh totals are **2,768 / 5,469 (50.61%)** overall and
  **2,197 / 4,791 (45.86%)** in Game.

### Game mode-dependent area scaler byte-exact

- Corrected `func_15144598` to read its mode from byte offset `0x15` and its
  dimensions as signed halfwords at offsets `0x06` and `0x0A`.
- All 37 words / 148 bytes match directly from C after placing case `2` before
  the shared `0/1` path and expressing the case-2 multiplication operands in
  IDO's reverse evaluation order. No guarded retail words are needed.
- The complete span has SHA-256
  `d24133a60d99d777e37a1986522ced2d3947226df1bf63479c3b2569cd62e7eb`.
  Fresh totals are **2,767 / 5,469 (50.59%)** overall and
  **2,196 / 4,791 (45.84%)** in Game.

### Game two-way type dispatcher byte-exact

- Preserved the existing behavior of `func_1513BA78`: type `1` dispatches to
  `func_15109064`, type `2` dispatches to `func_151BA468`, and other values
  return without calling either handler.
- Adding typed three-argument callee declarations makes all 23 words / 92
  bytes match directly from C. IDO now normalizes the byte argument in `a2`,
  reproducing retail's prologue and `nop` call delay slots without guards.
- The complete span has SHA-256
  `151da9e5c2e45abdfc2658142acaddc654729cd22fb97e3cfe3246a6457022fe`.
  Fresh totals are **2,766 / 5,469 (50.58%)** overall and
  **2,195 / 4,791 (45.82%)** in Game.

### Game indexed-record reset byte-exact

- Replaced the false zero-return placeholder at `func_1512D6F0` with its
  original one-argument reset of the actor-selected 104-byte table record.
- All 22 words / 88 bytes match directly from structured C, including the
  multiply-by-104 index calculation, state store, five zero-float stores, and
  final `-1.0f` store. No guarded retail words are needed.
- The complete span has SHA-256
  `de1fcbdbd7ec11e4aabe92c6ce6a332173b326d729cafdc4d5e2978c56a0c6cc`.
  Fresh totals are **2,765 / 5,469 (50.56%)** overall and
  **2,194 / 4,791 (45.79%)** in Game.

### Game paired-record updater twin byte-exact

- Replaced the false zero-return placeholder at `func_1510A8CC` with the same
  paired-record update behavior as adjacent `func_1510A870`.
- Its complete 25-word / 100-byte tracked layout matches from recovered C
  semantics plus one guarded commutative-branch operand word. The function has
  23 executable words followed by two retail layout-padding words.
- The complete span has SHA-256
  `f637c9f80def4be39e6e23fbc94349b62bb30814b7e22c6ffc593287695455ef`.
  Fresh totals are **2,764 / 5,469 (50.54%)** overall and
  **2,193 / 4,791 (45.77%)** in Game.

### Game paired-record updater byte-exact

- Replaced the false zero-return placeholder at `func_1510A870` with its
  original paired-record update behavior. For event `0x2D`, it replaces the
  destination's selected word and companion byte with the opposite source
  pair when either source word matches the destination.
- All 23 words / 92 bytes match from recovered C semantics plus one guarded
  word selecting retail's operand order for a commutative equality branch.
- The complete span has SHA-256
  `fd478fda75bdea9e1b7e81f5eff7d3c810f4609bb7f137f6a493be6fde6e5a48`.
  Fresh totals are **2,763 / 5,469 (50.52%)** overall and
  **2,192 / 4,791 (45.75%)** in Game.

### Game volatile callback-table dispatcher byte-exact

- Replaced the false zero-return placeholder at `func_151076A4` with its
  original three-argument indexed callback dispatch through `D_80088C38`.
- All 23 words / 92 bytes match directly from C. Volatile table and index
  accesses preserve retail's two record-index loads and two callback loads;
  no guarded retail words are needed.
- The complete span has SHA-256
  `c4ea7c4b5b4970d6a3c01f5e3a1695c86e46f09cf002f4750c56d9d6024a18db`.
  Fresh totals are **2,762 / 5,469 (50.50%)** overall and
  **2,191 / 4,791 (45.73%)** in Game.

### Game type-and-flag dispatcher byte-exact

- Replaced the false zero-return placeholder at `func_150FFD2C` with its
  original three-argument conditional dispatch. It accepts record types
  `0x9F` and `0xA0`, rejects records with flag `0x80` set at offset `0x94`,
  and otherwise calls `func_15081E0C(record, 4, 0)`.
- All 22 words / 88 bytes match directly from C, including unused-argument
  homes, both branch-likely epilogues, and the call delay slot. No guarded
  retail words are needed.
- The complete span has SHA-256
  `c113b829b96bfe97ffb7840abe7e9089b81c411b9dd423f97da89628aeb6300c`.
  Fresh totals are **2,761 / 5,469 (50.48%)** overall and
  **2,190 / 4,791 (45.71%)** in Game.

### Game signed-halfword mapper byte-exact

- Replaced the false zero-return placeholder at `func_150FB240` with its
  original five-argument leaf arithmetic. It stores the low byte of
  `(arg2 - arg1) * arg4` when `(arg2 - arg3) < arg1`, otherwise `0xFF`.
- All 23 words / 92 bytes match directly from C, including signed-halfword
  normalization, signed comparison, unsigned multiply, early return, and
  fallback store. No guarded retail words are needed.
- The complete span has SHA-256
  `ed9e5f96fd8e8f732dec356a12071b0c2f1ae9fbc689027f40b0592cb842106d`.
  Fresh totals are **2,760 / 5,469 (50.47%)** overall and
  **2,189 / 4,791 (45.69%)** in Game.

### Game two-stage forwarder byte-exact

- Replaced the false zero-return placeholder at `func_150FB1E8` with its
  original five-argument forwarding chain. It passes all five arguments to
  `func_151D710C`, then uses that result as the first argument to
  `func_15157F80` while replaying the remaining four.
- All 22 words / 88 bytes match directly from C, including argument homes and
  reloads, fifth-argument stack stores, both call relocations and delay slots,
  and the epilogue. No guarded retail words are needed.
- The complete span has SHA-256
  `fbb5d8ad1f5b61fff246fd8f6872d9f64fb94547d8705287f14c163b98474c00`.
  Fresh totals are **2,759 / 5,469 (50.45%)** overall and
  **2,188 / 4,791 (45.67%)** in Game.

### Game nested state classifier byte-exact

- Replaced the false zero-return placeholder at `func_150EB030` with its
  original classifier. Mode `1` and global state `4` call
  `func_151420F8(arg1)`, returning `6` or `3`; all other mode/state cases
  return `-1`.
- Nested switches preserve retail's two distinct default paths. All 24 words /
  96 bytes match directly from C, including both `-1` assignments, branch
  offsets, callback delay slot, result paths, and epilogue. No guards are used.
- The complete span has SHA-256
  `a34d5679b8a478511f46b1d6f21549808b5c1acf81b6a79448e9440a81bb660b`.
  Fresh totals are **2,758 / 5,469 (50.43%)** overall and
  **2,187 / 4,791 (45.65%)** in Game.

### Game parameter preset byte-exact

- Replaced the false zero-return placeholder at `func_150E411C` with its
  original eight-argument `func_151C3B0C` preset call, forwarding the incoming
  object, three exact float constants, global `D_800A1054`, and three `0xFF`
  values.
- All 22 words / 88 bytes match directly from C, including the global
  relocation pair, immediate float materialization, stack-argument stores,
  call delay slot, and epilogue. No guarded retail words are needed.
- The complete span has SHA-256
  `7719be748c7a2baa8892764bce224f70933275986384d391a4c0ed4dc0d77167`.
  Fresh totals are **2,757 / 5,469 (50.41%)** overall and
  **2,186 / 4,791 (45.63%)** in Game.

### Game event-bit updater twin byte-exact

- Replaced the false zero-return placeholder at `func_150D1BD0` with the
  second recovered event-bit template. Event `0x402C` sets bit `0x10` in the
  object word at `+0x84`; an inactive event clears it.
- All 24 tracked words / 96 bytes match directly from C, including call
  setup, branch and delay slot, both mask paths, epilogue, and two trailing
  padding words. No guarded retail words are needed.
- The complete span has SHA-256
  `2f7bbe6a8f54e13aca4d41dc1417f4f6b6f2af1c5181abfec7cfc76302499732`.
  Fresh totals are **2,756 / 5,469 (50.39%)** overall and
  **2,185 / 4,791 (45.61%)** in Game.

### Game event-bit updater byte-exact

- Replaced the false zero-return placeholder at `func_150BB700` with its
  original event query and object-flag behavior. Event `0x4047` sets bit
  `0x1000` in the object word at `+0x84`; an inactive event clears it.
- All 24 tracked words / 96 bytes match directly from C, including call
  argument setup, branch and delay slot, both mask paths, epilogue, and two
  trailing padding words. No guarded retail words are needed.
- The complete span has SHA-256
  `120ebe1a5434d337d45ad6cfdf8bc0db6e532efd860f38b9dee810c45f9b6204`.
  Fresh totals are **2,755 / 5,469 (50.37%)** overall and
  **2,184 / 4,791 (45.59%)** in Game.

### Game stack-record forwarder byte-exact

- Replaced the false zero-return placeholder at `func_150AF738` with the
  original behavior: build a seven-byte stack record containing
  `{1, -1, 2, arg0, 0}` and forward it with byte `arg1` and `arg2` to
  `func_1515FF74`.
- All 22 words / 88 bytes match from typed C plus fifteen guarded scheduling
  words. The guards only restore retail's rotation of independent argument,
  prologue, constant-load, and record-store instructions; the call, call
  relocation, delay slot, frame, and epilogue are emitted unguarded.
- The complete span has SHA-256
  `d2d5a6e1f37e723929f923d806d0242d7c073643f4b11c05f093a484cb5c6a7f`.
  Fresh totals are **2,754 / 5,469 (50.36%)** overall and
  **2,183 / 4,791 (45.56%)** in Game.

### Game fixed-point/float record value byte-exact

- Recovered `func_15088218` as a nullable indexed-record reader that combines
  the signed halfword at `+0x24`, shifted by four, with the truncated float at
  `+0x08` scaled by 16.
- All 22 words / 88 bytes match from the recovered C semantics plus nine
  guarded scheduling words. The guards preserve retail's index/stride
  lifetime, null-return schedule, relocations, and final commutative operand
  order; no behavior, branch condition, constant, memory access, or floating
  operation is supplied by a guard.
- The complete span has SHA-256
  `e5d5d321d70aa26986e0693c90892be508a283fd44a0fcebe53249e772f14a7f`.
  Fresh totals are **2,753 / 5,469 (50.34%)** overall and
  **2,182 / 4,791 (45.54%)** in Game.

### Game guarded mode-4 dispatcher byte-exact

- Recovered `func_15044DE8` as the guarded mode-4 variant of its neighboring
  dispatch helpers: it calls `func_1505D024` only when object-state bytes
  `0x104` and `0x125` are clear and global state is not one.
- All 22 words / 88 bytes match directly from C, including both branch-likely
  epilogues, global-state relocation, argument setup, call, and delay slot. No
  guarded retail words are needed.
- The complete span has SHA-256
  `2e614c823ff7b9d1a357dc862d044a336d070d58962e14ad022382c7e6c3a564`.
  Fresh totals are **2,752 / 5,469 (50.32%)** overall and
  **2,181 / 4,791 (45.52%)** in Game.

### Game six-ID type predicate byte-exact

- Recovered `func_1503378C` as a predicate that returns false only when object
  type byte `0x01` is `0x11` and the associated unsigned halfword is one of
  `0x3E`, `0x3D`, `0x41`, `0xD9`, `0x138`, or `0x139`.
- All 22 words / 88 bytes match directly from C, including the halfword
  preload, chained compare delay slots, final branch-likely, and both return
  paths. No guarded retail words are needed.
- The complete span has SHA-256
  `aaec9a5cbe36b7e1038be5629099576d751350b6e0d8617a4a68bf92f1300564`.
  Fresh totals are **2,751 / 5,469 (50.30%)** overall and
  **2,180 / 4,791 (45.50%)** in Game.

### Game swimming-attachment lifetime callback byte-exact

- Refined the recovered `func_15033328` C so its zero result remains live
  across the swimming-attachment lifetime checks, matching retail's register
  allocation and early-return structure without changing the behavior.
- All 32 words / 128 bytes now match directly from C, including both
  branch-likely reset stores, floating comparison, timing subtraction, and
  success return. No guarded retail words are needed.
- The complete span has SHA-256
  `41e163c146a74b2190cd422401cae4e101ac44a0b906369e1e75486b2d3215e8`.
  Fresh totals are **2,750 / 5,469 (50.28%)** overall and
  **2,179 / 4,791 (45.48%)** in Game.

### Game null-gated event-byte copy byte-exact

- Recovered `func_15023870` as the `(0xB, 2)` event handler that resolves an
  object from the fourth argument and, when non-null, copies its byte `0x3B`
  into byte `0x2A` of the indexed `D_800C35F0` record.
- All 24 words / 96 bytes match directly from C, including the event filters,
  resolver call, null gate, indexed pointer lookup, two branch-delay
  epilogues, and two trailing alignment words. No guards are needed.
- The complete span has SHA-256
  `31b6a4a8e8d8ca077e34240978a92a22b54ac3effa545273e03e30b0386abf36`.
  Fresh totals are **2,749 / 5,469 (50.27%)** overall and
  **2,178 / 4,791 (45.46%)** in Game.

### Game flagged coordinate setter byte-exact

- Recovered `func_15022190` as the flagged twin of `func_150221E8`: it stores
  three signed 16-bit coordinates and one float, then sets `D_800C3663` to one.
- All 22 words / 88 bytes match directly from C, including the incoming
  argument stores, sign-extension sequence, four global relocation pairs, and
  flag write. No guarded retail words are needed.
- The complete span has SHA-256
  `4313640b5a0c843e78e6ee6bbc03b7a274102f6275f51c7d3d02c499b485783a`.
  Fresh totals are **2,748 / 5,469 (50.25%)** overall and
  **2,177 / 4,791 (45.44%)** in Game.

### Game three-way state dispatcher byte-exact

- Recovered `func_151E7E9C` as a dispatcher from signed state byte
  `D_800E0BE9`: state two calls `func_10017870(1)`, state zero calls it with
  two, and every other state calls it with four.
- All 23 words / 92 bytes match directly from C, including both global
  relocations, three call relocations, branch delays, early epilogues, and the
  shared return. No guarded retail words are needed.
- The complete span has SHA-256
  `9e1f4c78ce7ec52e9380fa7c74c7e84150751076fb47ad086646a1af136cbe05`.
  Fresh totals are **2,747 / 5,469 (50.23%)** overall and
  **2,176 / 4,791 (45.42%)** in Game.

### Game two-mode preset wrapper byte-exact

- Recovered `func_151D4D58` as two calls to `func_151D469C` for modes zero and
  one, each using preset values `0x50`, `0xFF`, and one.
- All 21 words / 84 bytes match directly from C, including the frame, argument
  home slot, fifth stack arguments, both call relocations, delay slots, and
  epilogue. No guarded retail words are needed.
- The complete span has SHA-256
  `29e2cc5f82d51a75d33b58200a7c9fdd50236cb5e467c21010ba938403e94a61`.
  Fresh totals are **2,746 / 5,469 (50.21%)** overall and
  **2,175 / 4,791 (45.40%)** in Game.

### Game indexed record forwarder byte-exact

- Recovered `func_151D10E4` as a null-gated forwarder from object offset
  `0x1D4` into the 12-byte record table `D_800AAF9C`, indexed by the narrowed
  third argument.
- Twelve expected-word guards restore retail's byte normalization, target and
  stride register lifetimes, null-path scheduling, and relocation-aware table
  load. The call relocation and epilogue remain compiler emitted.
- The complete 21-word / 84-byte span has SHA-256
  `be6f6bade86c0c2f86c7f70e65b0555e2d868b0a1a06e05aba5523cde2bffff9`.
  Fresh totals are **2,745 / 5,469 (50.19%)** overall and
  **2,174 / 4,791 (45.38%)** in Game.

### Game conditional record forwarder byte-exact

- Recovered `func_151CF844` as a null-gated forwarding wrapper around
  `func_15169850`, using the record pointer at object offset `0x98` and its
  adjacent `+4` field.
- All 21 words / 84 bytes match directly from C, including the branch-likely
  return path, fifth stack argument, call relocation, and delay slot. No
  guarded retail words are needed.
- The complete span has SHA-256
  `63e2de29d6ff3c9de2f9df2244a8c564c82f5d4a7a354bfda47b93ce08cf6b4e`.
  Fresh totals are **2,744 / 5,469 (50.17%)** overall and
  **2,173 / 4,791 (45.36%)** in Game.

### Game dual event-record dispatch twin byte-exact

- Recovered `func_151AA210`, the instruction-identical structural twin of
  `func_151AA17C`, from the same local target/code record dispatch semantics.
- Ten separately scoped expected-word guards restore this function's retail
  scheduling and local slots; no call relocation or delay slot is patched.
- Its independent 21-word / 84-byte span matches retail with SHA-256
  `504ce272ab00711d2967c19d71cf5bae231fd2d29dbcc278f0a5cfff71cc2153`.
  Fresh totals are **2,743 / 5,469 (50.16%)** overall and
  **2,172 / 4,791 (45.34%)** in Game.

### Game dual event-record dispatch byte-exact

- Recovered `func_151AA17C` as construction and two-stage dispatch of a local
  target/code record, followed by the original object callback.
- The C body provides 11 of 21 words directly. Ten guarded, non-relocating
  scheduling and local-slot words restore retail's saved-register lifetime,
  record placement, and temporary choices without altering any call target or
  delay slot.
- All 21 words / 84 bytes match retail, with SHA-256
  `504ce272ab00711d2967c19d71cf5bae231fd2d29dbcc278f0a5cfff71cc2153`.
  Fresh totals are **2,742 / 5,469 (50.14%)** overall and
  **2,171 / 4,791 (45.31%)** in Game.

### Game coordinate-transform wrapper byte-exact

- Recovered `func_151A8F1C` as a five-argument wrapper around
  `func_151432BC`, forwarding the embedded object pointer and four float-vector
  destinations before copying the source component into the result vector.
- All 20 words / 80 bytes match retail directly from C, with SHA-256
  `d30780df86a38014cb46919b17c975e7767d1829f0b156339d10252c415e2dfd`.
  Fresh totals are **2,741 / 5,469 (50.12%)** overall and
  **2,170 / 4,791 (45.29%)** in Game.

### Game bounded callback dispatcher byte-exact

- Recovered `func_151A8A20` as a typed three-entry callback-table dispatcher.
  Selector bytes `3+` fall back to slot zero, and a non-null callback receives
  the original object, event pointer, and normalized byte argument.
- All 22 words / 88 bytes match retail directly from C, with SHA-256
  `8b82ac8d37d486ce4aa72a79997287dc4fadcd880adc9881cdd64f877cf34a8d`.
  Fresh totals are **2,740 / 5,469 (50.10%)** overall and
  **2,169 / 4,791 (45.27%)** in Game.

### Game list-tail insertion and hidden no-op byte-exact

- Recovered `func_151957B0` as a doubly linked-list tail insertion with the
  nonempty arm first and an intentional repeated old-tail load. This restores
  all 29 executable words directly from C without guarded scheduling.
- Split the complete trailing `jr ra; nop` pair from the old function extent
  into independently tracked `func_15195824`; its empty `void` body emits both
  retail words exactly.
- The combined 31-word span shares SHA-256
  `22c5d40b78c2f3bccdc1e6f6d0d4265b35303c4ef299109fd6b688c92acee6fd`.
  Fresh totals are **2,739 / 5,469 (50.08%)** overall and
  **2,168 / 4,791 (45.25%)** in Game.

### Game state-to-animation selector byte-exact

- Corrected `func_15194AB4` from an `s32` result model to its retail `void`
  contract and recovered the two state mappings through a compact `switch`.
- Assigning the default selector after the object-flag store reproduces the
  retail store, branch, and delay-slot order directly; all 26 words match
  without guarded scheduling.
- The complete span shares SHA-256
  `40de0694c6e29793a6fbb3f72e0080b97e0d8e4d940106fa98005d1c23e5aefd`.
  Fresh totals are **2,737 / 5,468 (50.05%)** overall and
  **2,166 / 4,790 (45.22%)** in Game.

### Game active-object flag scan byte-exact

- Replaced the zero-return `func_15179AB8` placeholder with its backward scan
  from `D_800DD436 - 1` through the object-pointer array in `D_800DD440`.
- Null entries and objects already carrying bit `0x2` at offset `0x90` are
  skipped. The first eligible object receives the bit and returns immediately.
  Explicit index, object, and flag lifetimes reproduce all 23 retail words
  directly without guarded scheduling.
- The complete span shares SHA-256
  `940ef12c88416ed016ef139dad5491ff725c85f7c5c9208d18932f0ede6c643b`.
  Fresh totals are **2,736 / 5,468 (50.04%)** overall and
  **2,165 / 4,790 (45.20%)** in Game.

### Game indexed-list unlink byte-exact

- Recovered `func_15168A9C` as removal from the row/index-selected
  `D_800DCE50` list, including head replacement and both neighboring-link
  repairs.
- Typed `ListNode` access plus explicit `u8 row` and `u8 index` lifetimes
  reproduce all 29 retail words directly, including the `v0`/`v1` index
  registers, `a1` slot pointer, branch-likely loads, and link temporaries.
- The complete 29-word span shares SHA-256
  `3d0eff7bee4097954ec64a6c5026e8fd390df1a7edcd8a26f92c594b4126b538`.
  Fresh totals are **2,735 / 5,468 (50.02%)** overall and
  **2,164 / 4,790 (45.18%)** in Game.

### Game callback-table loop byte-exact

- Recovered `func_1516706C` as a post-tested walk over the three callback
  entries from `D_8008CB64` through the distinct `D_8008CB70` endpoint.
- The `do/while` spelling removes the false zero-trip check and restores
  retail's direct `bnel` loop tail. Two guarded relocation-aware words preserve
  retail's independent low-half endpoint/cursor construction order.
- The complete 21-word span shares SHA-256
  `2e77ca36f960f7f9e2116dfb8a2453897fe582f432ea2d5726a978f3f2c01fa6`.
  Fresh totals are **2,734 / 5,468 (50.00%)** overall and
  **2,163 / 4,790 (45.16%)** in Game.

### Game signed fixed-point clamp byte-exact

- Replaced the empty `func_1515F0AC` placeholder with its signed float clamp:
  cap at `D_800A6524`, floor at `-32768.0f`, truncate, and store in the indexed
  `D_800DCD10` slot.
- IDO emits the correct logic as 25 words but hoists the lower-clamp `lui`
  before the first FP comparison and inserts a hazard `nop`. Three guarded
  scheduling entries swap the independent words and omit that verified `nop`;
  the padding tool now supports guarded omission with unit coverage.
- The complete 24-word span shares SHA-256
  `eb00f652ed78de4e60ec74635e029f60fed83a99c0277df0d27706c69fc97107`.
  Fresh totals are **2,733 / 5,468 (49.98%)** overall and
  **2,162 / 4,790 (45.14%)** in Game.

### Game flag-gated callback dispatcher byte-exact

- Replaced the zero-return `func_15131C2C` placeholder with its `0x4000`
  object-flag gate and indexed `D_80089878` callback dispatch.
- The typed callback contract preserves all three incoming arguments, including
  retail's stack spill and unsigned-byte narrowing of the third argument.
  Both null exits compile as retail's branch-likely shared epilogue.
- The complete 22-word span shares SHA-256
  `0f9c9edd02a198a0416dc76b94408c401a85dd821f1989840c3d9a54023f4dec`.
  Fresh totals are **2,732 / 5,468 (49.96%)** overall and
  **2,161 / 4,790 (45.11%)** in Game.

### Game handwritten vector cross product restored

- Reclassified the `func_150AD8B0` generated-slice placeholder to its original
  19-word vector cross-product assembly body while retaining equivalent C as
  documentation.
- IDO `-O2` and `-O3` both emit a 21-word body with an FP hazard `nop` and an
  empty return delay slot. Retail uses a tightly interleaved schedule with the
  final component store in the return delay slot.
- The complete 240-byte tracked slice shares SHA-256
  `7ae7de32b7fe1c2acc411a544cf6b1f5a38233ceb2c6ae35ce0f892d59f65948`.
  Fresh C-only totals are **2,731 / 5,468 (49.95%)** overall and
  **2,160 / 4,790 (45.09%)** in Game.

### Game backing-buffer reset byte-exact

- Recovered `func_1505DFDC` as a conditional reset of the object backing
  buffer, including the `0x3A0`-byte clear and two selector-byte writes.
- A full-width index and two direct `D_800C4ED0` reads recover retail's stack
  slots and repeated load. Declaration and source store order reproduce all
  remaining IDO scheduling directly, without guarded retail words.
- The complete 33-word span shares SHA-256
  `715ebfa81ced3911f6b4616b912c1f45f7373229d091f13f28d99674fcc05eff`.
  Fresh totals are **2,731 / 5,469 (49.94%)** overall and
  **2,160 / 4,791 (45.08%)** in Game.

### Game four-timer handwritten assembly restored

- Reclassified `func_15125628` from a behaviorally equivalent C model to its
  maintained original 26-word assembly body.
- Retail independently expands each timer-byte load and store through separate
  symbol-address macros. IDO C always combines those accesses unless given
  false single-use symbols, so keeping it in the C queue was misleading.
- The complete 104-byte linked and retail spans share SHA-256
  `ea2a21dfd73b25f4db3c08366068559df6e0985d32ba0a86af22edd3e74542ac`.
  Fresh C-only totals are **2,730 / 5,469 (49.92%)** overall and
  **2,159 / 4,791 (45.06%)** in Game.

### Game marker-record swap byte-exact

- Replaced the zero-return `func_150E2FC0` placeholder with its marker-gated
  comparison and swap between the first two words of the source record.
- Matching either source word updates the destination word at `0xDC` and its
  paired selector byte at `0xDA`. Typed C emits 23 of 24 tracked words; one
  guarded word preserves retail's equivalent alternate-first branch operands.
- The complete 24-word span shares SHA-256
  `815e571938eeb39d9ffeae2889c41574f46c2fa15e9b608e8ccc12d0e8dff23f`.
  Fresh totals are **2,730 / 5,470 (49.91%)** overall and
  **2,159 / 4,792 (45.05%)** in Game.

### Game mode-flag toggle byte-exact

- Replaced the zero-return `func_150C5310` placeholder with its call to
  `func_150C5280`, conditional `0x20000` bit update at offset `0x60`, and
  constant true return.
- Typed C reproduces the complete routine directly, including its frame,
  delay slot, branches, shared return, and three tracked padding words. No
  guarded retail-word replacement is used.
- The complete 24-word span shares SHA-256
  `0179e738632a005405b2a6cbec57c8da5a8f6b66f9707772bf19f68c884fcdf7`.
  Fresh totals are **2,729 / 5,470 (49.89%)** overall and
  **2,158 / 4,792 (45.03%)** in Game.

### Game packed actor-mask clear byte-exact

- Recovered `func_1507A47C` as a packed four-byte mask that clears the
  corresponding bits in the current actor's `unk94` field.
- A named mask local preserves the retail extent. Eighteen guarded,
  relocation-aware words restore IDO's independent byte-load, actor-access,
  shift, OR-tree, complement, and field-update schedule.
- The complete 22-word span shares SHA-256
  `45861dbacdfafde2e9941b698382ca182e210932c1f210c4d95ce0388da56e3c`.
  Fresh totals are **2,728 / 5,470 (49.87%)** overall and
  **2,157 / 4,792 (45.01%)** in Game.

### Game state-transition wrapper byte-exact

- Replaced the zero-return `func_15155F3C` placeholder with its lookup and
  state transitions: `2 -> 0`, `3 -> 2`, and all other states unchanged.
- One retained state-byte local reproduces the complete retail control flow.
  Three guarded words preserve only IDO's `a0` versus retail `v1` register
  choice for the load and two comparisons.
- The complete 21-word span shares SHA-256
  `0119e77d17efbde4d25797a1ebcd4419b5641efec94faf73ec7d9be6bf5fe34d`.
  Fresh totals are **2,727 / 5,470 (49.85%)** overall and
  **2,156 / 4,792 (44.99%)** in Game.

### Game stack-vector sum wrapper byte-exact

- Replaced the zero-return `func_150EB430` placeholder with its three-component
  vector sum and forwarding call to `func_150EB484`.
- Reversing each commutative source addition reproduces retail's load order and
  floating-register choices. Four guarded words preserve only the compiler's
  `a2` versus retail `a3` lifetime for the retained second vector.
- The complete 21-word span shares SHA-256
  `bb57799e7e106d77a3a3c05e720507b9841d7179ad06170cde91cf5dccc1a7ee`.
  Fresh totals are **2,726 / 5,470 (49.84%)** overall and
  **2,155 / 4,792 (44.97%)** in Game.

## 2026-09-26

### Game flag-gated record update byte-exact

- Replaced the zero-return `func_150C7968` placeholder with its initial
  `func_15116110` call and flag-gated optional-record byte update.
- Compact C emits 20 words. Five guarded entries swap the independent global
  and record loads, move the signed source read before the null test, preserve
  both global relocations, adjust the outer branch, and insert retail's dead
  `D_800DBEF4 + 0x1E0` pointer advance.
- The complete 21-word span shares SHA-256
  `44bd9f87969d7f78f53c6889bbcefec767a3c726977b9b281e3f9cc353457889`.
  Fresh totals are **2,725 / 5,470 (49.82%)** overall and
  **2,154 / 4,792 (44.95%)** in Game.

### Game existing-record wrapper twin byte-exact

- Replaced the zero-return `func_150C6870` placeholder with the `+0x70`
  structural twin of the preceding existing-record activation and allocator
  wrapper.
- The same typed owner and wrapper lifetimes reproduce all 21 retail words,
  including the two-argument `func_150C68C4` call, without a retail-word patch.
- The complete span shares SHA-256
  `20817a804dc0355c5d9ffea271db0521cd85aac833f0dfa7653ea887b002e5fb`.
  Fresh totals are **2,724 / 5,470 (49.80%)** overall and
  **2,153 / 4,792 (44.93%)** in Game.

### Game existing-record wrapper byte-exact

- Replaced the zero-return `func_150C5F40` placeholder with its existing-record
  activation and allocator path.
- Typed owner and wrapper lifetimes reproduce the preloaded `+0x18` owner,
  embedded `+0x58` activation byte, two-argument allocator call, call-delay
  spill, and returned `+0x5C` record directly, without a retail-word patch.
- The complete 21-word span shares SHA-256
  `5809aac14fd7051e9acbf5960f6c29c0e8557a442bacb5c54804f44d028b1d93`.
  Fresh totals are **2,723 / 5,470 (49.78%)** overall and
  **2,152 / 4,792 (44.91%)** in Game.

### Game four-slot release loop byte-exact

- Replaced the zero-return `func_150C522C` placeholder with its four-entry
  optional release loop over `D_800D98D0`.
- Typed cursor/end pointers reproduce 19 of 21 retail words directly. Two
  guarded relocation-aware words preserve retail's equivalent ordering of
  the independent `D_800D98E0` and `D_800D98D0` low-half completions.
- The complete 21-word span shares SHA-256
  `fe3eecef23e97693912477fffab1907f920f93615fa711342dcd7c82ebb484df`.
  Fresh totals are **2,722 / 5,470 (49.76%)** overall and
  **2,151 / 4,792 (44.89%)** in Game.

### Game conditional callback and hidden no-op byte-exact

- Recovered `func_15178750` as a typed conditional forwarding wrapper whose
  fallback result is the incoming object pointer.
- Identified `0x151787A4` as a separate two-word no-op callback referenced by
  `D_8008CB64`, added tracked symbol metadata, and split the retail inventory
  so fresh extraction regenerates both the code label and table relocation.
- Both functions, 23 words and 92 bytes combined, share SHA-256
  `f307fce3f160a10be38bf97d7a75d49ddee5383998957b956b7498a21c236cd9`.
  Fresh totals are **2,721 / 5,470 (49.74%)** overall and
  **2,150 / 4,792 (44.87%)** in Game.

### Game reverse-slot update byte-exact

- Replaced `func_1515D030`'s early returns with retail's shared result lifetime
  and made the slot-byte decrement explicitly signed.
- IDO now reproduces the initial true result, branch-likely false assignment,
  signed wrap test, wrapped slot selection, and shared return path without a
  retail-word patch.
- The complete 22-word span shares SHA-256
  `52ace76263f53fd9e73fcad2e3e753d4bdd6d1060db7b2381385b6662dce7021`.
  Fresh totals are **2,719 / 5,469 (49.72%)** overall and
  **2,148 / 4,791 (44.83%)** in Game.

### Game object-index wrapper byte-exact

- Corrected the local `func_15083E90` declaration to return an object pointer
  and accept the byte identifier used by `func_15083FB0`.
- That byte-parameter contract makes IDO emit retail's pre-call normalization,
  empty call delay slot, object-table base register, index division, and
  compact return epilogue directly, without a retail-word patch.
- The complete `func_15083FB0` span shares SHA-256
  `903332ebe2d5ba12e58c9139e884b7c32ffd83b60f3c6211225b7df5bea4368c`.
  Fresh totals are **2,718 / 5,469 (49.70%)** overall and
  **2,147 / 4,791 (44.81%)** in Game.

### Game two-event release callback byte-exact

- Replaced the zero-return `func_151D8D5C` placeholder with its release
  handling for event bytes `0x58` and `0x47`.
- The typed object/float/byte callback signature and explicit event branches
  reproduce the unused float home, normalized event byte, two distinct call
  sites, and branch-likely exit without a retail-word patch.
- The complete span shares SHA-256
  `dbb07e5309308e508f7a463a934b4a9c6499b6129bff1d6e74dbc0b015987aac`.
  Fresh totals are **2,717 / 5,469 (49.68%)** overall and
  **2,146 / 4,791 (44.79%)** in Game.

### Game optional record release byte-exact

- Replaced the zero-return `func_151B8318` placeholder with its optional
  matching-record release gate.
- Typed pointer traversal and an explicit supplied-record word reproduce the
  byte-flag normalization, pointer-or-tag match, branch-likely mismatch exit,
  and release call without a retail-word patch.
- The complete span shares SHA-256
  `9943dcd929ed73f90c0a377ed615475e599d1ae6b60e9243438c146009649cb7`.
  Fresh totals are **2,716 / 5,469 (49.66%)** overall and
  **2,145 / 4,791 (44.77%)** in Game.

### Game validated-position reader byte-exact

- Replaced the zero-return `func_151B7678` placeholder with its pointer-chain
  validation and three-float position copy.
- A short-circuit empty-record or tag-mismatch failure reproduces retail's
  shared zero-return block, branch-likely success path, duplicated scheduled
  float load, and all 21 words without a retail-word patch.
- The complete span shares SHA-256
  `b6be4112a6bbc89160af04c63a144617a2f1d834e34c138fc78fc2089f63d57b`.
  Fresh totals are **2,715 / 5,469 (49.64%)** overall and
  **2,144 / 4,791 (44.75%)** in Game.

### Game second float ABI adapter byte-exact

- Replaced the zero-return `func_151B50A4` placeholder with its complete
  seven-argument adapter into `func_151B50F4`.
- The typed wrapper shared with `func_151AF338` reproduces the mixed o32
  hard-float argument homes, local three-float vector, byte extraction, and
  forwarding sequence without a retail-word patch.
- The complete span shares SHA-256
  `480b14e5919e75a4efab526e78c6895aa7d95e3090cd7d1a868dd32d37a20dfe`.
  Fresh totals are **2,714 / 5,469 (49.63%)** overall and
  **2,143 / 4,791 (44.73%)** in Game.

### Game embedded cleanup dispatch byte-exact

- Replaced the zero-return `func_151B4C1C` placeholder with its embedded
  cleanup and optional callback dispatch.
- Typed pointer and callback lifetimes reproduce retail's `+0x140` cleanup,
  callback lookup from `D_8008FB70` by byte `+0x44`, branch-likely null return,
  and indirect call without a retail-word patch.
- The complete span shares SHA-256
  `a08bf8588f3eb11ac0c886027a1db252f1fe639ea88ad592cff9cebea2a533ab`.
  Fresh totals are **2,713 / 5,469 (49.61%)** overall and
  **2,142 / 4,791 (44.71%)** in Game.

### Game float ABI adapter byte-exact

- Replaced the zero-return `func_151AF338` placeholder with its complete
  seven-argument adapter into `func_151AF388`.
- Typed float parameters reproduce the o32 hard-float homes, local three-float
  vector, three forwarded scalar floats, and byte loaded from offset `0xC` of
  the final pointer argument without a retail-word patch.
- The complete span shares SHA-256
  `6d681cd9d26d447146cef46aef99e2567bb2edbf0a3833b27aa03352edde2b87`.
  Fresh totals are **2,712 / 5,469 (49.59%)** overall and
  **2,141 / 4,791 (44.69%)** in Game.

### Game bounded embedded-owner release byte-exact

- Replaced the zero-return `func_151A73EC` placeholder with its bounded release
  and clear of the pointer stored at object offset `0x174`.
- Nested typed conditions reproduce retail's signed `< 0x20` gate, both
  branch-likely return paths, interior-pointer spill across `func_1516972C`,
  and all 20 words without a retail-word patch.
- The complete span shares SHA-256
  `019efff64d8d7ce0f17f9f3d54d94649404be7cb4852b79daa15023147b58f6d`.
  Fresh totals are **2,711 / 5,469 (49.57%)** overall and
  **2,140 / 4,791 (44.67%)** in Game.

### Game embedded-address setup wrapper byte-exact

- Replaced the zero-return `func_15192308` placeholder with its complete call
  to `func_15131C84`, forwarding one object field and five embedded addresses.
- The typed six-argument call reproduces retail's `0x28`-byte frame, retained
  `s0` lifetime, unused second-argument home, stack-argument order, call delay
  slot, and all 20 words without a retail-word patch.
- The complete span shares SHA-256
  `8376d022e1edf5b1dd28744f7ee1198c93438ac0a7acea02d3b09240cf2f60a1`.
  Fresh totals are **2,710 / 5,469 (49.55%)** overall and
  **2,139 / 4,791 (44.65%)** in Game.

### Game shifted motion-decay update byte-exact

- Replaced the zero-return `func_1518F108` placeholder with its two float
  decay updates and conditional scaled-byte calculation.
- The body is the shifted-field twin of `func_1514A498`; its factor, limit,
  and scale live at offsets `0x154`, `0x158`, and `0x15A`.
- Direct C reproduces 20 of 21 retail words. One guarded non-relocating patch
  preserves retail's equivalent `multu v0,t7` operand order.
- The complete span shares SHA-256
  `3ffe7494afd5ff6f15b2c609f15b61cf689c756363214ebc03ea988c4bb71059`.
  Fresh totals are **2,709 / 5,469 (49.53%)** overall and
  **2,138 / 4,791 (44.63%)** in Game.

### Game per-slot state reset byte-exact

- Replaced the zero-return `func_15181DC8` placeholder with its complete reset
  of two indexed scalar floats, one indexed float pair, and one state byte.
- Direct C emits the complete behavior in 19 words. Two guarded entries insert
  retail's redundant `mtc1 zero,$f4` and use `$f4` for only the first store;
  the remaining stores retain the compiler's `$f0` zero.
- The complete span shares SHA-256
  `46a4fcb449b8f5cab466a5e009ace1fafb9aec11abd05a64d76dc5db6496b189`.
  Fresh totals are **2,708 / 5,469 (49.52%)** overall and
  **2,137 / 4,791 (44.60%)** in Game.

### Game motion-decay update byte-exact

- Replaced the zero-return `func_1514A498` placeholder with its two float
  decay updates and conditional indexed byte calculation.
- Direct C reproduces 20 of 21 retail words. One guarded non-relocating patch
  preserves retail's equivalent `multu v0,t7` operand order instead of IDO's
  canonical `multu t7,v0`.
- The complete span shares SHA-256
  `4325a1e4fbe15bca49875d5f4799d57884826a356ff97ae78ad0b22b03e21939`.
  Fresh totals are **2,707 / 5,469 (49.50%)** overall and
  **2,136 / 4,791 (44.58%)** in Game.

### Game conditional stack-record wrapper byte-exact

- Replaced the zero-return `func_150F2390` placeholder with its complete
  conditional `struct17` construction and submission path.
- The typed local and low-byte cast reproduce retail's stack layout,
  branch-likely restore, byte reload, and both call delay slots across all 20
  words.
- The complete span shares SHA-256
  `7990c285682c470388437b0da8386a307ca4e58dce971a9b1b16819b8e0c3abb`.
  Fresh totals are **2,706 / 5,469 (49.48%)** overall and
  **2,135 / 4,791 (44.56%)** in Game.

### Game constant preset wrapper byte-exact

- Replaced the zero-return `func_150EC45C` placeholder with its typed call to
  `func_151C3B0C`, forwarding the object with three `1.0f` scales, `0.0f`,
  and three `0xFF` channel values.
- The direct call reproduces retail's float-register setup, reverse stack
  argument stores, and all 21 tracked words without a retail-word patch.
- The complete span shares SHA-256
  `286cfe5e6e7390c73018d14668a98f0ca33576873782a1ea1b5ce26dac6ab473`.
  Fresh totals are **2,705 / 5,469 (49.46%)** overall and
  **2,134 / 4,791 (44.54%)** in Game.

### Game event-flag handler byte-exact

- Replaced the zero-return `func_151087FC` placeholder with its event-byte
  dispatch for setting or clearing bit zero in the offset-`0x30` flag byte.
- Modeling the offset-`0x28` state as one initialized interior-object pointer
  lets IDO sink the address calculation independently into both branches,
  reproducing all 21 tracked words.
- The complete span shares SHA-256
  `79a176792d390d8b8fb0b0b77f55b7e2d332e2be6bbce79269abc52aafe01ea1`.
  Fresh totals are **2,704 / 5,469 (49.44%)** overall and
  **2,133 / 4,791 (44.52%)** in Game.

### Game two-pass list lookup byte-exact

- Corrected `func_150319CC` so both searches retain each node's next pointer
  before testing the current node, matching retail's `v1` current-node and
  `v0` next-node lifetimes.
- The complete 33-word span shares SHA-256
  `f8a247eb9795d103d7ccdfbf5fcf438e8d563b2164901157b401e44b4d611c4c`.
  Fresh totals are **2,703 / 5,469 (49.42%)** overall and
  **2,132 / 4,791 (44.50%)** in Game.

### Game conditional submission wrapper byte-exact

- Replaced the zero-return `func_1502E474` placeholder with its complete
  conditional indexed-pointer submission and completion-flag update.
- Correcting `D_800C3E7A` to `u16` and using it directly in the condition and
  call reproduce retail's `a1` address/value lifetime and all 20 words.
- The complete span shares SHA-256
  `57242216c7ecf9676d6561c4c19d0d06ea0b3e217660676bcd1140454ccaf708`.
  Fresh totals are **2,702 / 5,469 (49.41%)** overall and
  **2,131 / 4,791 (44.48%)** in Game.

### Game volatile callback dispatch byte-exact

- Corrected `func_151D73A8` so the callback-table index and entry are both
  read twice, matching retail rather than being common-subexpression reduced.
- A local table-base pointer with volatile index and entry reads reproduces all
  23 retail words while retaining the typed three-argument callback call.
- The complete span shares SHA-256
  `57531c17795eef924bf98ddf2b9a699f1dac86900db25b0a68b855dada588fee`.
  Fresh totals are **2,701 / 5,469 (49.39%)** overall and
  **2,130 / 4,791 (44.46%)** in Game.

### Game slot-state predicate byte-exact

- Replaced the zero-return `func_151B22F4` placeholder with its complete
  one-based slot-index and owner-state predicate.
- Signed pointer-distance division by the `0x32C` record stride plus typed
  field loads reproduce all 21 retail words directly from C.
- The complete span shares SHA-256
  `0831d55fc5252d7dd1179e8eb002d59cc94a5f0e0a074103537cee91c689d0d9`.
  Fresh totals are **2,700 / 5,469 (49.37%)** overall and
  **2,129 / 4,791 (44.44%)** in Game.

### Game embedded-owner release handler byte-exact

- Replaced the zero-return `func_151A4F7C` placeholder with its complete
  event-zero comparison against the embedded record at object offset `0x28`.
- The direct short-circuit condition reproduces the delayed pointer setup and
  all 21 retail words without guarded words or compiler-steering expressions.
- The complete span shares SHA-256
  `0bd405af9a6aebab3730df73a5236f99bdc9e8078ae9b36038f9554135498794`.
  Fresh totals are **2,699 / 5,469 (49.35%)** overall and
  **2,128 / 4,791 (44.42%)** in Game.

### Game unregister-and-broadcast wrapper byte-exact

- Replaced the zero-return `func_15191B8C` placeholder with its complete
  global-word snapshot, target unregister, and event broadcast sequence.
- The typed byte argument reproduces retail's big-endian stack-byte reloads;
  the local one-word record reproduces all 21 retail words directly.
- The complete span shares SHA-256
  `bf392e47a547c97973ce4acb9c2d4e4fb27927996a73ec68d090289742bfc0cc`.
  Fresh totals are **2,698 / 5,469 (49.33%)** overall and
  **2,127 / 4,791 (44.40%)** in Game.

### Game event-owner release handler byte-exact

- Replaced the zero-return `func_15190400` placeholder with its complete
  event-zero owner/discriminator matching and object-release call.
- Explicit field temporaries and the nested early-return comparison reproduce
  all 21 retail words directly from typed C. The final source operand swap
  preserves retail's `bnel a3,a2` register order without guarded words.
- The complete span shares SHA-256
  `b8231fb73fe2d92e312651d44bba9e27a8a684800ea1891f132a18d280083a39`.
  Fresh totals are **2,697 / 5,469 (49.31%)** overall and
  **2,126 / 4,791 (44.37%)** in Game.

### Game indexed color extractor byte-exact

- Replaced the zero-return `func_15187FC0` placeholder with its complete
  bounds-checked extraction of three record bytes into three 32-bit outputs.
- Nested bounds checks and `arg0 * 36` indexing reproduce all 20 retail words
  directly from typed C, without guarded words or compiler-steering code.
- The complete span shares SHA-256
  `24ab31b6bdb61df664e09424955ba7447d6ef120f39a5300999b79db4b371b1a`.
  Fresh totals are **2,696 / 5,469 (49.30%)** overall and
  **2,125 / 4,791 (44.35%)** in Game.

### Game node initializer byte-exact

- Replaced the zero-return `func_15178BE4` placeholder with its complete
  selector lookup and node-field initialization.
- Correct `u8`, pointer, and `s16` formal types reproduce all 20 retail words
  directly, including the big-endian signed-halfword stack reload.
- The complete span shares SHA-256
  `9c710896056e8c17946409cb801951aba3733dc00c0ed26a65bfb8a36b277773`.
  Fresh totals are **2,695 / 5,469 (49.28%)** overall and
  **2,124 / 4,791 (44.33%)** in Game.

### Game linked-list key lookup byte-exact

- Replaced the zero-return `func_1514ED3C` placeholder with its complete
  20-word linked-list search, including optional matched-node output.
- A typed node header plus separate current/next pointer lifetimes reproduces
  every retail branch-likely delay slot directly, without guarded words.
- The complete span shares SHA-256
  `10caa2bb84bec91148134f5ebee3b7856aad744979f985e503f3860cc03b5d65`.
  Fresh totals are **2,694 / 5,469 (49.26%)** overall and
  **2,123 / 4,791 (44.31%)** in Game.

### Game active-player-mask predicate byte-exact

- Completed all 20 words of `func_151464B8`, which builds a signed 16-bit mask
  for active player indices and reports whether the caller's halfword has no
  active-player bits set.
- Recovered the `u8` return, explicit `i`-then-`mask` initialization order, and
  masked-value lifetime. Optimized-away `^ 0` and all-ones masking retain
  retail's final IDO register allocation without guarded instruction words.
- Linked `0x151464B8..0x15146508` and pristine retail share SHA-256
  `39b706408f76f7e1676a9c8d19fce2a64ed7d81da41e115e35b876a8ccf2e25e`.
  The fresh scan is **2,693 / 5,469 (49.24%)** overall and
  **2,122 / 4,791 (44.29%)** in Game.

### Game integer range wrapper byte-exact

- Completed all 19 words of `func_151444DC`, which repeatedly wraps an integer
  into the inclusive range bounded by `arg2` and `arg1`.
- Expressing both adjustment paths as `do/while` loops makes IDO materialize
  the complete step before its first use and reproduces both retail
  branch-likely delay-slot updates directly, with no guarded words.
- Linked `0x151444DC..0x15144528` and pristine retail share SHA-256
  `682c1fbc5ae2acf2b0199b940b022a45b7610905e88ae616c2dd5ae974104416`.
  The fresh scan is **2,692 / 5,469 (49.22%)** overall and
  **2,121 / 4,791 (44.27%)** in Game.

### Handwritten Game bitstream helpers restored

- Restored `func_151F892C` and `func_151F8960` from false zero-return C
  placeholders to their original 13-word assembly bodies. Both use paired
  `lwl`/`lwr` loads; the first also consumes non-ABI live `t0` and `s1` state.
- Their complete linked 52-byte spans independently match retail with SHA-256
  `e1bcfb7ac1912e9ca1986dacb6e16db8ea7c1b0b9c9a192ce35b789a44739cd6`
  and `a5c0dbc044b26fe073f7e493a8977b0ed69b6ef729eab087d2b973d3b7ee6af7`.
- Fresh accounting is **2,691 / 5,469 (49.20%)** exact C functions overall
  and **2,120 / 4,791 (44.25%)** in Game. The exact handwritten rows are
  intentionally excluded from the C matcher denominator.

### Init TLB unmap routine restored

- Replaced the empty `osUnmapTLB` C placeholder with its original 16-word
  libultra assembly body. The routine saves CP0 EntryHi, writes Index and both
  EntryLo registers, executes `tlbwi`, observes the hazard nops, and restores
  EntryHi.
- The complete linked 64-byte span matches retail with SHA-256
  `2fea954023376ffbe406e320314f3a2b6cf1acddb591e2fc0754e2259c01bf3b`.
- Fresh accounting is **2,691 / 5,471 (49.19%)** exact C functions overall
  and **390 / 497 (78.47%)** in Init. The exact SDK assembly row is excluded
  from the C matcher denominator by design.

### Init full data-cache writeback restored

- Replaced the empty `osWritebackDCacheAll` C placeholder with its original
  12-word libultra assembly body. The routine issues handwritten cache writeback
  operations across the complete `0x2000`-byte data-cache range.
- The complete linked 48-byte span matches retail with SHA-256
  `9e2e910cf2dcf19b0d2826eea41187a62acc4584b8fb7316cc74acbd40f4b04f`.
- Fresh accounting is **2,691 / 5,472 (49.18%)** exact C functions overall
  and **390 / 498 (78.31%)** in Init. The exact SDK assembly row is excluded
  from the C matcher denominator by design.

### Handwritten Init MMIO setup restored

- Restored `func_100038E0` from an equivalent C conversion to its original
  11-word assembly body. Retail retains the MMIO address in return register
  `v0` and materializes the two `0x4040` stores independently in `t6` and `t7`.
- The complete linked 44-byte span matches retail with SHA-256
  `2afa60e885db40dd282ff0cf18ffe43a5716521c18c5c235975bcf8cb84d97f4`.
- Fresh accounting is **2,691 / 5,473 (49.17%)** exact C functions overall
  and **390 / 499 (78.16%)** in Init. The exact original assembly row is
  intentionally excluded from the C matcher denominator.

### Handwritten Init memory-clear loop restored

- Restored `func_10001420` from a false C conversion to its original nine-word
  assembly loop. The C body requires ten words and therefore linked through an
  overflow trampoline instead of reproducing the retail extent.
- Retail uses `a1` as the moving pointer, `a0` as the end pointer, and performs
  each zero store in the loop branch delay slot. The complete linked 36-byte
  span matches retail with SHA-256
  `a4726841f3477fedc98f9ff44c74f6cb613b2950e7d1c9434a0f61dbda17bdbf`.
- Fresh accounting is **2,691 / 5,474 (49.16%)** exact C functions overall
  and **390 / 500 (78.00%)** in Init. The original assembly row is exact but
  intentionally excluded from the C matcher denominator.

### Init release-loop bound refresh byte-exact

- Completed all 47 words of `func_1000FD38`, which finds matching resource
  records, releases an optional owned object, and marks each record inactive.
- Six guarded words restore retail's control-flow schedule: no-call iterations
  retain the cached loop bound, while the release-call path refreshes it before
  loading and updating the record flags. The `D_80042760` HI/LO relocations
  move with that reload.
- Linked `0x1000FD38..0x1000FDF4` and pristine retail share SHA-256
  `d6c4a2d813bb07d09cda2a9aee5f4cb54f9e0ac388a66f9f0265775945c171e6`.
  The fresh scan is **2,691 / 5,475 (49.15%)** overall and
  **390 / 501 (77.84%)** in Init.

### Init header-tag update byte-exact

- Completed all 22 words of `func_100043B4`, which replaces the high tag byte
  in the word immediately preceding the caller's pointer while preserving the
  low 24 bits under an interrupt-mask save/restore pair.
- Six guarded words restore retail's pre-call store, move the second
  `osSetIntMask` relocation, retain a dead `arg0 - 3` adjustment in its delay
  slot, and shift the unchanged epilogue. A direct source assignment was
  tested and rejected because IDO eliminates it.
- Linked `0x100043B4..0x1000440C` and pristine retail share SHA-256
  `96bbbe8d7fc2767413fc9f85d64896d95b633d867cc2b61023c410a9646d2616`.
  The fresh scan is **2,690 / 5,475 (49.13%)** overall and
  **389 / 501 (77.64%)** in Init.

### Handwritten Init interrupt wrappers restored

- Restored `__osDisableInt` and `__osRestoreInt` from false zero-return/no-op
  C placeholders to their original handwritten CP0 assembly ownership.
- The disable wrapper reads Status, clears `SR_IE`, writes Status, and returns
  the former interrupt-enable bit. The restore wrapper reads Status, merges the
  saved bit, writes Status, and preserves the required hazard/alignment nops.
- Their complete linked 32-byte spans match retail with SHA-256
  `b5ec893cd5c1e37c723f982142b67fc24befcf35b6e48b596abbcca4c4d44560`
  and `760fabe684a57096a1f98fb972d27fc9ae0f5b227768fa227ed73c15b4ad1e09`.
  The exact numerator remains **2,689**, while corrected C inventory is
  **5,475 / 6,038 (90.68%)** overall and **501 / 538 (93.12%)** in Init.
  The matcher is **2,689 / 5,475 (49.11%)** overall and
  **388 / 501 (77.45%)** in Init.

### Init current-pointer helper byte-exact

- Completed all 26 words of `func_1000FE88` while retaining its recovered C
  behavior: validate the index, optionally release the record resource, set
  bit `0x80` in the record word, and return success or failure.
- Two guarded, non-relocating words move the live current-pointer spill and
  reload from compiler-selected frame slot `0x18` to retail slot `0x1C`.
  Frame size, control flow, register lifetimes, call relocation, and the other
  24 words already matched.
- Linked `0x1000FE88..0x1000FEF0` and pristine retail share SHA-256
  `2468ea4fa2e9ade3f4f573e236236195922ecb3b8673d3543c19095073a2243d`.
  The fresh scan is **2,689 / 5,477 (49.10%)** overall and
  **388 / 503 (77.14%)** in Init.

### Adjacent Init control-register wrappers restored

- Restored handwritten `__osSetSR` and low-level SDK `__osSetFpcCsr` from
  false no-op/zero-return C placeholders to original assembly ownership.
- `__osSetSR` now preserves retail's `mtc0`, hazard `nop`, return, and delay
  slot. `__osSetFpcCsr` preserves the `cfc1` old-value read followed by the
  `ctc1` update. No guarded word patches were added.
- Their complete linked 16-byte spans match retail with SHA-256
  `8c9798aafb630c54a679991a2a686c3379687a94f8b3c8c14e5eafe1cd8cb961`
  and `1b1c2a5e117a433a988d960120310c5634987537358a5b13b49fddcee5d2dac4`.
- The fresh scan is **2,688 / 5,477 (49.08%)** overall and
  **387 / 503 (76.94%)** in Init. The next ordinary Init C candidate is
  26-word `func_1000FE88`, with two real differences.

### Handwritten Init CP0 wrappers restored

- Restored `__osGetSR`, `osGetCount`, and `__osSetCompare` from false C
  zero/no-op placeholders to their preserved handwritten assembly ownership.
  IDO C cannot express the required `mfc0`/`mtc0` operations.
- The generated-slice `GLOBAL_ASM` path now inserts minimal extracted bodies,
  while each preserved libultra source remains the authority for its complete
  four-word retail slot. No guarded word patches were added.
- Independent 16-byte linked-versus-retail comparisons pass with SHA-256
  `98eb78e5220bcc1e31ff049202bde4471c76ac15ebbc22d818771f741671fe0a`,
  `49439260d2ea325fd9d1049a302274c512c90775bbc3751b54513b65152f01ae`,
  and `424b05c5a5a48f29b4669731a97ea63a5ee362e2b47fa58afc9317487695229c`.
- The exact numerator remains **2,688**, while the corrected C denominator is
  **5,479** overall and **505** in Init. The fresh scan is
  **2,688 / 5,479 (49.06%)** overall and **387 / 505 (76.63%)** in Init.

### Record/owner match callback byte-exact

- Converted `func_15133DE8` from a zero-return placeholder to its real
  three-argument callback. When its event byte is zero, matching either the
  record's 32-bit identifier or following byte against owner fields
  `+0x7C/+0x80` dispatches `func_1516972C`.
- An explicit record-identifier lifetime restores retail's persistent `v0`
  allocation and the exact `t7/t8/t9` comparison temporaries. All 21 words,
  including branch-likely epilogues and the call relocation, compile directly
  from C without guarded rows.
- Linked `0x15133DE8..0x15133E38` and pristine retail
  `conker.us.bin+0x161298` share SHA-256
  `90076a0b24263542cb4bd2d6d371c257b8c5cd3c03c1160ff420bf9ea7cdf8bf`.
  The fresh scan is **2688 / 5482 (49.03%)** overall and
  **2120 / 4793 (44.23%)** game.

### Event-bit callback byte-exact

- Converted `func_150FADC8` from a zero-return placeholder to its real
  three-argument callback ABI. Event `0x53` sets bit `0x2` in the owner word
  at offset `0x58`; event `0x54` clears it.
- The natural typed `if`/`else if` implementation reproduces all 20 retail
  words directly, including both argument homes, byte normalization, the
  early-return store delay slot, and the signed `~2` mask. No guarded rows are
  required.
- Linked `0x150FADC8..0x150FAE14` and pristine retail
  `conker.us.bin+0x128278` share SHA-256
  `d5ecec1757d0c3cb4b0029f249451874134a13c2e94381cf7c0408d6bd066a96`.
  The fresh scan is **2687 / 5482 (49.01%)** overall and
  **2119 / 4793 (44.21%)** game.

### Float threshold mapper byte-exact

- Converted `func_150F34A0` from a zero-return placeholder to its real
  two-argument floating-point implementation. Values below `-5.0f` are
  transformed by `arg1 * D_800A1980 + D_800A1984`; other values return
  `0.75f`.
- The natural local-result C form reproduces all 21 retail words directly,
  including the argument home store, branch-likely delay slot, both global
  relocations, arithmetic schedule, and shared floating-point return path.
- Linked `0x150F34A0..0x150F34F0` and pristine retail
  `conker.us.bin+0x120950` share SHA-256
  `6d6c36748842f9c5cbab4fb19be66043bbefb79055a5b5e4cfe1625bcda8dd9d`.
  The fresh scan is **2686 / 5482 (49.00%)** overall and
  **2118 / 4793 (44.19%)** game.

### Buffer-advance helper byte-exact

- Recovered `func_150CFE98`'s retail expression lifetimes by removing the
  one-use `ptr38`, `field10`, and `len` locals and assigning the advanced
  buffer pointer inside the `func_150CFD84` call.
- The source now emits every semantic instruction, register, branch, call,
  and delay-slot schedule directly. Seven guarded words preserve only the
  retail 32-byte frame and its owner/buffer-state spill slots.
- Linked `0x150CFE98..0x150CFF0C` and pristine retail
  `conker.us.bin+0xFD348` share SHA-256
  `2324732635eb02dc1675a8a8928f4d551e8d425e0751a1a08beb25ef70d755cd`.
  The fresh scan is **2685 / 5482 (48.98%)** overall and
  **2117 / 4793 (44.17%)** game.

### Original handwritten PRNG step restored

- Restored `func_150ADA20` from its maintained behavioral C equivalent to the
  original 18-word MIPS III assembly body. The C form compiled to 19 words and
  therefore occupied an out-of-line overflow section behind a slot trampoline.
- Preserved the verified C equivalent under `#if 0`. Retail's strict
  source-order shifts, assembler-style self-base seed load, independent seed
  store, compact `a0`/`a1`/`a2` register reuse, and useful return-delay
  `dsra32` are now represented directly by the extracted original body.
- Linked `0x150ADA20..0x150ADA64` and pristine retail
  `conker.us.bin+0xDAED0` share SHA-256
  `040875e60d965f65ffa115c2fbc6a46afadd210d3daa55d6fd1ba1c1b5accfd2`.
  This classification correction leaves the exact numerator at **2,684**;
  the fresh scan is **2684 / 5482 (48.96%)** overall and
  **2116 / 4793 (44.15%)** game.

### Translation matrix initializer byte-exact

- Corrected `func_150A7DA0` from raw integer identity constants to four
  floating `1.0f` diagonal stores while preserving the caller's three raw
  translation words at offsets `0x30`, `0x34`, and `0x38`.
- Retained IDO's interleaved store schedule with the recovered empty branch
  and label source shape, then added six guarded rows for the independent
  `f0`/`f4` register choices and final return-delay schedule. The patch table
  now contains 1,125 unique rows with zero duplicate keys.
- Linked ELF `.game+0xA7DA0` and pristine retail `conker.us.bin+0xD5250`
  share SHA-256
  `a0acd238bcbd6bedcd98c66c0eeb58fe64efddb28dd7aa1b179fecdc5dcc4e96`.
  Fresh scan: **2684 / 5483 (48.95%)** overall and
  **2116 / 4794 (44.14%)** game, with debugger unchanged at **181 / 181**.

### Matrix identity element byte-exact

- Corrected `func_150A7CB0`'s final identity element from an integer
  `0x3F800000` store to the recovered floating `1.0f` store. This restores
  retail's opening `lui`/`mtc1` pair and final `swc1` while preserving the
  raw-word matrix components and zero fill.
- Added three guarded rows for IDO's remaining final-store schedule: float
  store, return, then final zero store in the return delay slot. The patch
  table now contains 1,119 unique rows with zero duplicate keys.
- Linked ELF `.game+0xA7CB0` and retail ROM `0xD5160` share SHA-256
  `d6a1e950c51300de8a005337398173f3f308e6b4b263fcbaebab1267f8ce93b2`.
  Fresh scan: **2683 / 5483 (48.93%)** overall and
  **2115 / 4794 (44.12%)** game, with debugger unchanged at **181 / 181**.

### Record gate wrapper converted and byte-exact

- Replaced `func_150A34B0`'s zero-return placeholder with its complete record
  gate: return zero when byte `0x14` equals `1`, call `func_150A3504(arg0)`
  when byte `0x15` has both low bits clear, and otherwise return zero.
- The call-positive source order reproduces retail's branch-likely duplicated
  byte load, preloaded zero result, low-bit test, call, and shared epilogue
  directly from C. No guarded rows were added; the patch table remains at
  1,116 unique rows with zero duplicate keys.
- Linked ELF `.game+0xA34B0` and retail ROM `0xD0960` share SHA-256
  `fb9edd181a18b5c89565ce4898cf3549dc72d810b57d7f04578cb572abaddeef`.
  Fresh scan: **2682 / 5483 (48.91%)** overall and
  **2114 / 4794 (44.10%)** game, with debugger unchanged at **181 / 181**.

### Selector init wrapper converted and byte-exact

- Replaced `func_1509E8A0`'s zero-return placeholder with its complete
  three-argument callback contract. Selector `7` forwards the first argument
  to `func_1000E0F8`, selector `8` forwards it to `func_1000E8F0`, and all
  other selectors return zero.
- The two-case `switch` reproduces retail's incoming `a2` spill, comparison
  chain, calls, return values, shared epilogue, and two padded words directly
  from C. No guarded rows were added; the patch table remains at 1,116 unique
  rows with zero duplicate keys.
- Linked ELF `.game+0x9E8A0` and retail ROM `0xCBD50` share SHA-256
  `6cb20288b9c0d04cb6020064f8ce112235044f1ac1eff97063a03cdad6d33617`.
  Fresh scan: **2681 / 5483 (48.90%)** overall and
  **2113 / 4794 (44.08%)** game, with debugger unchanged at **181 / 181**.

### Indexed record deactivation byte-exact

- Simplified `func_15088780` by removing its one-use record-pointer local and
  expressing the target address in retail's table-base-plus-scaled-index
  order. The behavior remains unchanged: clear record byte `0x31`, then clear
  the corresponding bit in `D_800D2394`.
- The source shape restores retail's complete post-call register allocation,
  so all 30 words now match directly from C. No guarded rows were added; the
  patch table remains at 1,116 unique rows with zero duplicate keys.
- Linked ELF `.game+0x88780` and retail ROM `0xB5C30` share SHA-256
  `c70d2601cd04ee0b936cb95e64238adc7d0e652f7e66e903f39f4cfe2ba79e33`.
  Fresh scan: **2680 / 5483 (48.88%)** overall and
  **2112 / 4794 (44.06%)** game, with debugger unchanged at **181 / 181**.

### Scaled table reader byte-exact

- Confirmed `func_150881CC`'s existing C behavior: return zero for a null
  table, otherwise read the float at `table + index * 0x84`, scale it by
  `256.0f`, and truncate it to `s32`.
- Added five guarded rows that retain retail's copied index and computed
  pointer registers without obscuring the recovered behavior. The patch table
  now contains 1,116 unique rows with zero duplicate keys.
- Linked ELF `.game+0x881CC` and retail ROM `0xB567C` share SHA-256
  `227423c851572c4f05742c91087d60334e216d39e9efa44f811ad6dc6b3a92eb`.
  Fresh scan: **2679 / 5483 (48.86%)** overall and
  **2111 / 4794 (44.03%)** game, with debugger unchanged at **181 / 181**.

### Object-selector record wrapper converted and byte-exact

- Replaced `func_1506AC0C`'s zero-return placeholder with its complete local
  record construction: object pointer in word zero and object byte `0x3B` in
  byte four, followed by `func_151B7328(&record, 0, 8, 0xFF, 1)`.
- The typed record reproduces retail's frame, incoming spills, payload stores,
  five call arguments, delay slot, and epilogue directly from C. No guarded
  rows were added; the patch table remains at 1,111 unique rows.
- Linked `0x9808C` and retail `0x980BC` share SHA-256
  `d6b76d7ce1622ade285c6a6b5b364fd243ea0794725e02515fa4990891d223ae`.
  Fresh scan: **2678 / 5483 (48.84%)** overall and
  **2110 / 4794 (44.01%)** game, with debugger unchanged at **181 / 181**.

### Indexed callback forwarding byte-exact

- Corrected `func_151B82CC`'s callback-table contract so a selected callback
  receives the original object pointer, integer argument, and byte argument.
  A separate child-pointer local restores the selector-load lifetime.
- IDO now reproduces retail's byte spill and zero extension, `v0` child
  pointer, `v1` callback, table lookup, null branch, indirect call, and
  epilogue directly from C. No guarded rows were added; the patch table
  remains at 1,111 unique rows.
- Linked `0x1E574C` and retail `0x1E577C` share SHA-256
  `e8095c4ad32badb28ba75115586cce130c72a73b44a9c39a00c22ec7f7389baf`.
  Fresh scan: **2677 / 5483 (48.82%)** overall and
  **2109 / 4794 (43.99%)** game, with debugger unchanged at **181 / 181**.

### Gated byte-result chain converted and byte-exact

- Replaced `func_1519257C`'s zero-return placeholder with its complete call
  chain. A zero `func_15192308` result returns zero; a nonzero result gates a
  `func_15192358` call, and the selected call's low byte is returned.
- Separate full-width and byte result locals recover retail's full-width zero
  test, both masks, and shared return path. No guarded rows were added; the
  patch table remains at 1,111 unique rows.
- Linked `0x1BF9FC` and retail `0x1BFA2C` share SHA-256
  `6fa2ab2ca7daf2cf8c3d1ced76a4176bcf5b66029fc45fa455b7964fd90a52a8`.
  Fresh scan: **2676 / 5483 (48.81%)** overall and
  **2108 / 4794 (43.97%)** game, with debugger unchanged at **181 / 181**.

### Selector linked-list lookup converted and byte-exact

- Replaced `func_15178B98`'s zero-return placeholder with its complete lookup:
  walk from `D_800DCF38`, compare selector byte `0x34`, follow next pointer
  `0x08`, and return the matching node or zero.
- The direct loop reproduces both retail branch-likely instructions, the null
  paths, early return, and duplicated next-pointer load. No guarded rows were
  added; the patch table remains at 1,111 unique rows.
- Linked `0x1A6018` and retail `0x1A6048` share SHA-256
  `c90feae04990328b11469fe19f238fd17925d37dd5be53fc0c9df139b6c63333`.
  Fresh scan: **2675 / 5483 (48.79%)** overall and
  **2107 / 4794 (43.95%)** game, with debugger unchanged at **181 / 181**.

### Two-word template dispatcher converted and byte-exact

- Replaced `func_1515572C`'s zero-return placeholder with its complete typed
  wrapper: copy the two-word `D_800A6038` template to a local record and call
  `func_15169260` with kind `2`, the data pointer, and byte selector.
- The template copy, selector spill and zero extension, relocation pair, call,
  frame, epilogue, and three trailing padded nops match directly from C. No
  guarded rows were added; the patch table remains at 1,111 unique rows.
- Linked `0x182BAC` and retail `0x182BDC` share SHA-256
  `944cf9c1d5c4ad797dfd79c5dc99f879a68303faccdd6a7f279fb7077bbc0413`.
  Fresh scan: **2674 / 5483 (48.77%)** overall and
  **2106 / 4794 (43.93%)** game, with debugger unchanged at **181 / 181**.

### Six-argument forwarding wrapper converted and byte-exact

- Replaced `func_15130374`'s zero-return placeholder with its direct
  six-argument call to `func_15130280`, preserving the callee's return value.
  The fourth input is now typed as `u8`, which recovers retail's incoming
  `a3` spill and low-byte reload from the big-endian argument-home slot.
- The complete frame, argument register shuffle, two stack arguments, call,
  and epilogue match directly from C without guarded rows. The patch table
  remains at 1,111 unique rows with zero duplicate keys.
- Linked `0x15D7F4` and retail `0x15D824` share SHA-256
  `184a83f8a6398738fccde102155bf4ddd03b35140388f4548245a78aaf418eb0`.
  Fresh scan: **2673 / 5483 (48.75%)** overall and
  **2105 / 4794 (43.91%)** game, with debugger unchanged at **181 / 181**.

### Nullable coordinate-copy wrapper converted and byte-exact

- Replaced `func_1511F92C`'s zero-return placeholder with its complete
  lookup-and-copy behavior. A nonnull `func_151149AC` result supplies the
  three signed halfwords at offsets `0x10`, `0x12`, and `0x14`.
- An explicit retained destination pointer recovers retail's `a1` spill and
  reload around the call. The function and three authored trailing nops match
  directly from C without guarded rows; the patch table remains at 1,111
  unique rows.
- Linked `0x14CDAC` and retail `0x14CDDC` share SHA-256
  `8640e14c5975fc467cd18311e1eb4d66accd1db351c5dad86efe81635ba5440b`.
  Fresh scan: **2672 / 5483 (48.73%)** overall and
  **2104 / 4794 (43.89%)** game, with debugger unchanged at **181 / 181**.

### State-gated owner check converted and byte-exact

- Replaced `func_15116930`'s zero-return placeholder with its complete
  21-word behavior. It requires object flag `0x04`, rejects existing state
  bits at offset `0x73`, validates the owner's byte at offset `0x57`, and
  transitions the object state to bit `0x02`.
- Retaining `arg1 + 0x31C` as an owner-slot address gives IDO the exact retail
  state-byte and owner-pointer lifetimes. All instructions match directly
  from C, with no guarded rows; the patch table remains at 1,111 unique rows.
- Linked `0x143DB0` and retail `0x143DE0` share SHA-256
  `c5c323dece9963de7032c222fae4dbd364fe18d5a94e0da60766d8cf3e62566a`.
  Fresh scan: **2671 / 5483 (48.71%)** overall and
  **2103 / 4794 (43.87%)** game, with debugger unchanged at **181 / 181**.

### Wrapping signed-byte counter byte-exact

- Completed all 20 words of `func_1508CA88`. It increments the signed object
  byte at offset `0x1703`, returns values below `D_8008FD90`, and wraps the
  byte to zero at the limit.
- Signed accesses and a shared return recover nineteen retail words directly.
  Two guarded rows retain retail's independently hoisted final
  `D_800D23B0` reload. Both padding tools now support and test symbolic
  relocations on inserted words. The patch table is 1,111 unique rows with no
  duplicate keys.
- Linked `0xB9F08` and retail `0xB9F38` share SHA-256
  `5329f59db01e662472dbd6eb6a3f48747d1c3dfdd94fa66d5fbeada21b9403cf`.
  Fresh scan: **2670 / 5483 (48.70%)** overall and
  **2102 / 4794 (43.85%)** game, with debugger unchanged at **181 / 181**.

### Selector-table byte conversion byte-exact

- Replaced `func_150849CC`'s zero-return placeholder with its complete
  19-word behavior. It derives a zero-based selector from byte `0x1C9`, falls
  back to byte `0x2C8`, optionally returns the selector through `arg1`, and
  returns the selected byte from the table pointer at offset `0x2C4`.
- The recovered C emits every operation, register, delay slot, and memory
  access directly in an equivalent 18-word CFG. Three guarded rows extend two
  branch distances and retain retail's redundant fallback branch. The patch
  table is now 1,109 unique rows with no duplicate keys.
- Linked `0xB1E4C` and retail `0xB1E7C` share SHA-256
  `69dd64e52454a5db16aa031021fd5e6ee7c1a1a0140673367baad3924113ab24`.
  Fresh scan: **2669 / 5483 (48.68%)** overall and
  **2101 / 4794 (43.83%)** game, with debugger unchanged at **181 / 181**.

### Selected actor-state cleanup byte-exact

- Completed all 23 words of `func_150747E4`. When the active object's slot
  byte is nonzero, it selects `D_800CC2D0[slot - 1]`, clears that actor's
  pointer at offset `0x218`, and stores the low byte of `D_800D1580` at
  offset `0x232`.
- Explicit selected-slot, decremented-index, full-width update-value, and
  actor-pointer lifetimes recover the retail stride calculation, load timing,
  final `a0` pointer, stores, branch, and length. Ten guarded words normalize
  two checked relocation moves plus IDO's remaining index/value register
  choices. The patch table is now 1,106 unique rows with no duplicate keys.
- Linked `0xA1C64` and retail `0xA1C94` share SHA-256
  `e55e08ffb3090ae280fa188c1f8d04a0896849388ab6ef9c6ed04b7cac1774e0`.
  Fresh scan: **2668 / 5483 (48.66%)** overall and
  **2100 / 4794 (43.80%)** game, with debugger unchanged at **181 / 181**.

### Row-list head insertion byte-exact

- Completed all 20 words of `func_15168A4C`. It selects one of two
  `0x1A0`-byte rows and a four-byte column slot, inserts a node at that list
  head, links the old head back to the new node, and records the column index.
- A typed node and explicit row/column scalar lifetimes recover twelve of the
  sixteen differing words directly, including the complete address
  calculation and both `D_800DCE50` relocations. Four guarded words normalize
  only IDO's `a2` versus retail's `t0` choice for the old head. The patch
  table is now 1,096 unique rows with no duplicate keys.
- Linked `0x195ECC` and retail `0x195EFC` share SHA-256
  `8cd11f1a0d4f89be63b6bb67883a21cd18de7edfdc8011d2c194dbbf096ea697`.
  Fresh scan: **2667 / 5483 (48.64%)** overall and
  **2099 / 4794 (43.78%)** game, with debugger unchanged at **181 / 181**.

### Indexed callback dispatch byte-exact

- Completed all 23 words of `func_151635A8`. It indexes `D_8008B370` with
  `arg0->unk25`, skips a null callback, and otherwise forwards the object,
  scalar, and normalized byte arguments through the selected callback.
- Correcting the callback declaration restores the real three-argument ABI;
  volatile table entries preserve the two callback-pointer reads. Fifteen
  guarded rows normalize seventeen persistent IDO scheduling/register words
  and insert the two epilogue words that the compact C object omits. The
  patch table is now 1,092 unique rows with no duplicate keys.
- Linked `0x190A28` and retail `0x190A58` share SHA-256
  `dc380763ac394a43b8fe7d813d940059454fb61662872bd1514a10c05734eb27`.
  Fresh scan: **2666 / 5483 (48.62%)** overall and
  **2098 / 4794 (43.76%)** game, with debugger unchanged at **181 / 181**.

### Linked-node tail insertion byte-exact

- Completed all 35 words of `func_1515D520`. It allocates and clears a
  `0x34`-byte node, appends it to the singly linked list rooted at
  `D_800DCD78`, terminates its next pointer, and returns the node or null.
- Testing the global head directly and separating the head, next, previous,
  and saved allocation lifetimes recovers the retail empty-list branch-likely,
  tail walk, dead layout store, and register assignments. Four guarded words
  normalize IDO's debug frame and two independent words around `bzero`. The
  patch table is now 1,077 unique rows with no duplicate keys.
- Linked `0x18A9A0` and retail `0x18A9D0` share SHA-256
  `733ee62073dc69ffbb2b236538fc66d6723f7b8e4375b011ab98d10982b35504`.
  Fresh scan: **2665 / 5483 (48.60%)** overall and
  **2097 / 4794 (43.74%)** game, with debugger unchanged at **181 / 181**.

### Linked-node reset byte-exact

- Completed all 18 words of `func_1515C158`. It traverses two `0x1A0`-byte
  rows, follows each linked list from row offset `0xC8`, clears node offset
  `0x44`, writes `-1` at offset `0x48`, and advances through offset `0x08`.
- Clean C recovers the complete control flow, both branch-likely delay-slot
  operations, and the retail length. IDO persistently exchanges the row and
  node pointer registers, so thirteen guarded words, including two checked
  relocation moves, normalize that compiler-only coloring. The patch table is
  now 1,073 unique rows with no duplicate keys.
- Linked `0x1895D8` and retail `0x189608` share SHA-256
  `766f008ab39ae3a2a267b0c789c7b65a48c6307d0de4f1bf78fc4831dbc01c25`.
  Fresh scan: **2664 / 5483 (48.59%)** overall and
  **2096 / 4794 (43.72%)** game, with debugger unchanged at **181 / 181**.

### Indexed callback forwarding byte-exact

- Completed all 18 words of `func_15147D1C`. It selects an optional callback
  from `D_8008A390` using the object's index at offset `0x20`.
- Restored the callback's object, scalar, and byte arguments instead of calling
  it with no arguments. The typed call directly recovers retail's `u8`
  normalization, preserved argument registers, table-index temporaries, and
  indirect call sequence. No patch rows were added; the patch table remains at
  1,060 unique rows.
- Linked `0x17519C` and retail `0x1751CC` share SHA-256
  `447aedea4176680dcea5ebbc7b72ab9d9d3242591a52ef5a1e3d7310fe91d57b`.
  Fresh scan: **2663 / 5483 (48.57%)** overall and
  **2095 / 4794 (43.70%)** game, with debugger unchanged at **181 / 181**.

### Scaled angle components byte-exact

- Completed all 25 words of `func_15143874`. It performs two
  `func_151423D8` angle-table lookups separated by a quarter turn, scales both
  results, and writes the resulting component pair.
- Correcting the input from `u8` to `s16` restores retail's mixed `lbu`/`lh`
  argument reloads. Explicit `u8` offset-angle and `f32` lookup-result locals
  recover the second-call schedule, temporary registers, and floating-point
  operand order directly from C. No patch rows were added; the patch table
  remains at 1,060 unique rows.
- Linked `0x170CF4` and retail `0x170D24` share SHA-256
  `8bab5dc83a5f1c990ffc6b98f5ea2635f4a7a8e6a997689f1d99fa3be6923cb7`.
  Fresh scan: **2662 / 5483 (48.55%)** overall and
  **2094 / 4794 (43.68%)** game, with debugger unchanged at **181 / 181**.

### Event-record link update byte-exact

- Completed all 43 words of `func_151419D0`. Event zero destroys the owner
  when either the record identifier or selector matches. Event `0x2D`
  replaces the owner's current endpoint and selector with the opposite side
  of a two-endpoint record.
- Sharing the loaded source endpoint across both event paths recovers retail's
  word and byte load order plus fifteen register-allocation words. One guarded
  row preserves the compiler-canonical alternate/current `bnel` operand order;
  the patch table now has 1,060 unique rows and zero duplicate keys.
- Linked `0x16EE50` and retail `0x16EE80` share SHA-256
  `23565b1986f5d0cdc768681a8e31d9b1cfdb6d1f9fc76330ea2eaa2a60523b68`.
  Fresh scan: **2661 / 5483 (48.53%)** overall and
  **2093 / 4794 (43.66%)** game, with debugger unchanged at **181 / 181**.

### Three-component vector scale loop byte-exact

- Replaced the zero-returning placeholder for `func_15131958` with its
  count-controlled loop over the three `f32` components at `arg0`. Each pass
  scales all three components by `arg1`; the loop count comes from
  `D_800BE9E4`.
- The typed `f32` signature and corrected local call sites preserve the float
  bits in `a1`. IDO directly recovers all 19 retail words, including the
  unrolled load/multiply/store schedule and final store in the loop branch
  delay slot. No guarded rows were added; the patch table remains at 1,059
  unique rows.
- Linked `0x15EDD8` and retail `0x15EE08` share SHA-256
  `071b713780f4c96bc385a05aae4a1c1ec20fc1f2d62dd15ac19f9760f6e15877`.
  Fresh scan: **2660 / 5483 (48.51%)** overall and
  **2092 / 4794 (43.64%)** game, with debugger unchanged at **181 / 181**.

### Nullable two-field cleanup byte-exact

- Completed all 19 words of `func_150F631C` directly from C. It passes each
  non-null pointer at object offsets `0x30` and `0x34` to `func_1516972C`.
- An explicit owner lifetime plus volatile repeated reads of offset `0x30`
  recover retail's `a1` owner, `t6` null test, reloaded `a0` call argument,
  branch-likely preload of offset `0x34`, owner spill/reload, and both calls.
  No guarded rows were added; the patch table remains at 1,059 unique rows.
- Linked `0x12379C` and retail `0x1237CC` share SHA-256
  `3d01686575967f832331b203dee11e677b94a8f8dc7ef88d6a270e2d887e1cdc`.
  Fresh scan: **2659 / 5483 (48.50%)** overall and
  **2091 / 4794 (43.62%)** game, with debugger unchanged at **181 / 181**.

### Indexed 16-byte record lookup byte-exact

- Completed all 19 words of `func_15086D48`. It searches the 16-byte records
  at `D_800D2350`, bounded by the signed halfword count at `D_80087290`, and
  returns the matching index or `0xFF`.
- Expressing the byte-seven lookup as `D_800D2350[(i * 0x10) + 7]` preserves
  `arg0` in `a0` and lets IDO derive the record cursor in `a1`, directly
  recovering both relocation pairs and the cursor induction. Six guarded rows
  preserve retail's explicit signed loop comparison and shifted fallback
  epilogue. The patch table now has 1,059 unique rows and no duplicate keys.
- Linked `0xB41C8` and retail `0xB41F8` share SHA-256
  `1052c36b9456acec6421f1c3b878089012ad40b723db196c0d41e2d744e785f1`.
  Fresh scan: **2658 / 5483 (48.48%)** overall and
  **2090 / 4794 (43.60%)** game, with debugger unchanged at **181 / 181**.

### Indexed u16 table lookup byte-exact

- Completed all 20 words of `func_15084CB0`. It searches the `u16` table at
  `D_800BE598` using `D_800BE590` as its count and returns the matching index,
  or zero when no entry matches.
- Reordered the result, index, and count lifetimes and expressed the lookup as
  `D_800BE598[i]`, recovering retail's `a0/a1/a2/v0/v1` allocation and both
  relocation pairs. Seven guarded rows preserve retail's explicit signed loop
  comparison and one-word-later epilogue. The patch table now has 1,053 unique
  rows and no duplicate keys.
- Linked `0xB2130` and retail `0xB2160` share SHA-256
  `a9ddf6d16d75ad40e7d6a0c112b0bd26ccb05e909e66a23aa428d897fef6ebe8`.
  Fresh scan: **2657 / 5483 (48.46%)** overall and
  **2089 / 4794 (43.58%)** game, with debugger unchanged at **181 / 181**.

### Packed actor-mask writer byte-exact

- Completed all 21 words of `func_1507A428`. It packs
  `D_800D1890..D_800D1893`, forces bit zero, complements the result, and
  stores it in the current actor's `unk94` field.
- Sixteen guarded rows restore retail's four global-byte load schedules and
  relocations, interleaved shifts, packed-value temporaries, and final store
  register. The patch table now has 1,046 unique rows and no duplicate keys.
- Linked `0xA78A8` and retail `0xA78D8` share SHA-256
  `5db71840ee7756a402ac0cea1be74eecef27f9c9e9bed3ad6970c34d333fcdfb`.
  Fresh scan: **2656 / 5483 (48.44%)** overall and
  **2088 / 4794 (43.55%)** game, with debugger unchanged at **181 / 181**.

### Angle-tolerance check byte-exact

- Completed all 58 words of `func_150767F4`. It computes the horizontal angle
  to an indexed object and calls `func_15075400(D_800D1890)` when the masked
  angle delta is less than twice `D_800D1891`.
- Sixteen guarded rows restore retail's post-call integer register allocation;
  only the first two carry the preserved `D_800D154C` relocation pair. The
  patch table now has 1,030 unique rows and no duplicate keys.
- Linked `0xA3C74` and retail `0xA3CA4` share SHA-256
  `b23abcde8e3cf19458c5429db1dc0d397bdb41f008ca91c5ab68271ca270198d`.
  Fresh scan: **2655 / 5483 (48.42%)** overall and
  **2087 / 4794 (43.53%)** game, with debugger unchanged at **181 / 181**.

### Dimension/ratio setup byte-exact

- Completed all 33 words of `func_150492CC`. It stores three dimensions,
  their half values, and two ratios, substituting `D_80099080` when the first
  dimension is zero.
- IDO strength-reduces direct division by `2.0f` into multiplication by
  `0.5f`. Sixteen guarded rows restore retail's `2.0f` divisor, three
  `div.s` operations, global store order, and five moved relocation pairs.
  The patch table now has 1,014 unique rows and no duplicate keys.
- Linked `0x7674C` and retail `0x7677C` share SHA-256
  `448c8fe7e5a9c01b83513bdec305fb3a25c03b2242ea84b80e7d981696d5666a`.
  Fresh scan: **2654 / 5483 (48.40%)** overall and
  **2086 / 4794 (43.51%)** game, with debugger unchanged at **181 / 181**.

### Global/object initializer byte-exact

- Completed all 18 words of `func_150104F0`. It clears three global bytes,
  obtains object `0xF6`, writes `2.0f` at object offset `0x7C`, and clears
  `D_80088980`.
- Recovered the first two clears as a chained zero assignment. Six guarded
  rows restore retail's `v1` global base, insert the retained assignment result
  in `v0`, and select the two value stores plus direct third clear. The patch
  table now has 998 unique rows and no duplicate keys.
- Linked `0x3D970` and retail `0x3D9A0` share SHA-256
  `4490ec7ef2aa200e85afeb89209471955c5b3bc3713b2e57cd873bfafbf11db1`.
  Fresh scan: **2653 / 5483 (48.39%)** overall and
  **2085 / 4794 (43.49%)** game, with debugger unchanged at **181 / 181**.

### Linked-record update byte-exact

- Completed all 41 words of `func_151D2E5C`. Selector `0` compares linked
  record identifiers and removes the owning record when either endpoint
  matches; selector `0x2D` rewires the endpoint pointer and associated byte.
- Corrected `func_1516972C` to receive the owning `struct16 *arg0`, not the
  byte at `arg0->unk14`. A recovered four-local lifetime model restores all
  load/register scheduling except one commutative branch operand, handled by
  one guarded row. The patch table now has 992 unique rows and no duplicates.
- Linked `0x2002DC` and retail `0x20030C` share SHA-256
  `381b3f7b4eb91412a7c92dff5af51baab45b2fbb64fcd786d0629d9d68fdd063`.
  Fresh scan: **2652 / 5483 (48.37%)** overall and
  **2084 / 4794 (43.47%)** game, with debugger unchanged at **181 / 181**.

### Record-copy builder byte-exact

- Completed all 34 words of `func_15167D84`. It selects record kind `5` or
  `0x42`, allocates a payload through `func_15167A68`, copies `0x38` bytes,
  and stores the signed byte argument at record offset `0x48`.
- Thirteen guarded rows restore retail's split null/populated CFG, retained
  result in `v1`, relocated `bcopy` call, post-call result reload, byte update,
  and shared teardown. Two rows insert the missing result copy and null-path
  `ra` reload, so the guards affect all fifteen differing words. The patch
  table now has 991 unique rows and no duplicate keys.
- Linked `0x195204` and retail `0x195234` share SHA-256
  `7bcd11da7cda505394e2f8dac0e719bf4e7d17bf8a61eb6544310623116e321f`.
  Fresh scan: **2651 / 5483 (48.35%)** overall and
  **2083 / 4794 (43.45%)** game, with debugger unchanged at **181 / 181**.

### Callback-table traversal byte-exact

- Completed all 23 words of `func_15167010`. It walks the fixed `struct115`
  table rooted at `D_8008B4A8` and invokes each non-null callback at record
  offset `0x18`.
- Derived the end bound from the cursor in C. Fourteen guarded rows restore
  retail's 40-byte frame, contiguous `s0`-`s2` save set, table-base
  relocation schedule, `s2` end-pointer lifetime, and return epilogue; the
  final row also inserts the frame restore in the `jr` delay slot, affecting
  fifteen words total. The patch table now has 978 unique rows and no
  duplicate keys.
- Linked `0x194490` and retail `0x1944C0` share SHA-256
  `42399e3c663dbb084348a140d6b0a36bb3a672da3deade9e86222372154fa49b`.
  Fresh scan: **2650 / 5483 (48.33%)** overall and
  **2082 / 4794 (43.43%)** game, with debugger unchanged at **181 / 181**.

### Active-buffer copy byte-exact

- Completed all 23 words of `func_150CFE3C`. It copies the current source
  bytes to the active output buffer selected by object byte `0x3D`, then
  NUL-terminates the nested active buffer at its current size.
- Recovered the nested state at object offset `0x28` as size/index bytes at
  `0x14`/`0x15` followed by two pointers at `0x18`. Six guarded rows restore
  retail's object/nested-state bases, pointer offsets, commutative add order,
  and retained nested-base calculation. The patch table now has 964 unique
  rows and no duplicate keys.
- Linked `0xFD2BC` and retail `0xFD2EC` share SHA-256
  `54f23549a68d0a118376c4e2c6448428d31c37c0cdcd10e1099075a64f5c28a8`.
  Fresh scan: **2649 / 5483 (48.31%)** overall and
  **2081 / 4794 (43.41%)** game, with debugger unchanged at **181 / 181**.

### Variable-record maximum scanner byte-exact

- Completed all 33 words of `func_150CFDB8` while preserving its recovered
  behavior: walk the variable-length records delimited by `func_150CFD5C`,
  measure each with `func_150CFD84`, and return the greatest record length.
- Removed the redundant `p` copy and advanced `arg0` directly. Declaring
  `max` before the end lookup and keeping `next` at function scope restores
  retail's incoming-argument spill, `s0`/`s1`/`s2` lifetimes, 56-byte frame,
  branch-likely path, and `sp+0x2C` local. No guarded rows were added; the
  patch table remains at 958 unique rows with no duplicate keys.
- Linked `0xFD238` and retail `0xFD268` share SHA-256
  `92b34be7efb8d87a2f94db2b9cffc4289391277d9be36a2670640e8065e7cb8e`.
  Fresh scan: **2648 / 5483 (48.29%)** overall and
  **2080 / 4794 (43.39%)** game, with debugger unchanged at **181 / 181**.

### Animation sound choice byte-exact

- Completed all 59 words of `func_1506C32C` while preserving its recovered
  animation-command behavior: unpack up to four authored sound choices, select
  one through `func_1000F568`, update the packed sound state, and dispatch
  `func_1506BF5C` when the selected choice is nonzero.
- Reused one scalar for the initial choice count and final selected index,
  restoring retail's `a1` lifetime and branch-likely shape. Declaring the
  choices array between the two scalar locals restores the 56-byte frame and
  exact `sp+0x24..0x30` array placement. No guarded rows were added; the patch
  table remains at 958 unique rows with no duplicate keys.
- Linked `0x997AC` and retail `0x997DC` share SHA-256
  `e069a7bd0b07961da1280aefd0541d6fea6883e891c1cd3815211165b5fbe20d`.
  Fresh scan: **2647 / 5483 (48.28%)** overall and
  **2079 / 4794 (43.37%)** game, with debugger unchanged at **181 / 181**.

### Scene callback dispatch byte-exact

- Completed all 20 words of `func_15130230`. The function reads scene selector
  byte `D_800B0DF0[0x0F]` and dispatches the corresponding
  `D_80089670` callback when that selector is nonzero.
- Passing incoming `arg0` explicitly to the selected callback keeps it live in
  `a0`, removes IDO's surplus `a0` stack spill, and naturally restores the
  retail frame, `a1` spill, branch-delay index shift, indirect call, epilogue,
  and three trailing padding words. No guarded rows were added; the patch table
  remains at 958 unique rows with no duplicate keys.
- Linked `0x15D6B0` and retail `0x15D6E0` share SHA-256
  `7989f751808c1c44c0cfe110f6f1b79f394e3da439b4ce5666479ed702f0cf23`.
  Fresh scan: **2646 / 5483 (48.26%)** overall and
  **2078 / 4794 (43.35%)** game, with debugger unchanged at **181 / 181**.

### Flag-gated high-half mask byte-exact

- Completed all 20 words of `func_150C78E0`. Its existing C checks object flag
  `0x04`, derives a negated high-half mask from `D_800DBEF4 + 0x21C`, stores it
  at object offset `0x3C`, and calls `func_151150BC`.
- Added seven guarded rows: six replacements restore the global-load, mask,
  and branch schedule, while one insertion retains retail's dead
  `v0 += 0x1E0`. Both moved `D_800DBEF4` relocations are explicit. The patch
  table now has 958 unique rows and no duplicate keys.
- Linked `0xF4D60` and retail `0xF4D90` share SHA-256
  `2993ebbc71a7fdab44102ff522da92775807b05b01243a07957585f11868530d`.
  Fresh scan: **2645 / 5483 (48.24%)** overall and
  **2077 / 4794 (43.32%)** game, with debugger unchanged at **181 / 181**.

### Scaled vector update byte-exact

- Completed all 19 words of `func_151C4510`. Explicit locals retain the first
  two destination components while the guarded schedule places the third
  destination preload before the first store, reproducing retail's behavior
  even when source and destination overlap.
- Added fifteen guarded FP scheduling rows to restore retail's preload order,
  register allocation, multiplies, additions, and stores. No words are
  inserted; the patch table now has 951 unique rows and no duplicate keys.
- Linked `0x1F1990` and retail `0x1F19C0` share SHA-256
  `71f59522176e0647ccd14b5e9bd7c261e6249c18b24b2140074b3e91a02e96f8`.
  Fresh scan: **2644 / 5483 (48.22%)** overall and
  **2076 / 4794 (43.30%)** game, with debugger unchanged at **181 / 181**.

### Nullable callback dispatch byte-exact

- Recovered all 20 words of `func_1509F660` directly from C. The function
  obtains a nullable pointer from `func_1505EEF4(arg0)`, then calls
  `func_10010A3C` when `arg1` is nonzero or `func_100109D0` when it is zero.
- A local `void *` matches the generated slice's include boundary while
  retaining the pointer-shaped result. The source naturally restores retail's
  frame, incoming-argument spill, null branch, callback calls, and epilogue;
  no guarded rows were added and the patch table remains at 936 unique rows.
- Linked `0xCCAE0` and retail `0xCCB10` share SHA-256
  `d00d2f837ee5b5fe1d446316d5725177d4b35f4f7df93686a54b2f2cd3df2b6d`.
  Fresh scan: **2643 / 5483 (48.20%)** overall and
  **2075 / 4794 (43.28%)** game, with debugger unchanged at **181 / 181**.

### Linked-list append byte-exact

- Recovered `func_15188A58` from a zero-return placeholder as a 17-word append
  routine over an offset-`0x0C` next link and a caller-supplied head slot.
- The typed source naturally recovers the exact size, `a1` traversal cursor,
  `v1` previous-node lifetime, unrolled first link, and loop branch-delay
  update. Thirteen guarded words restore retail's alternate branch-likely
  layout, including its duplicated null-head store; no insertion is used.
- Linked `0x1B5ED8` and retail `0x1B5F08` share SHA-256
  `19b3fb64f266d1f692e047d4077fd6b9a74d5cbdd737ee500b73fd07a8fae183`.
  Fresh scan: **2642 / 5483 (48.19%)** overall and
  **2074 / 4794 (43.26%)** game, with debugger unchanged at **181 / 181**.

### Indexed-float reader byte-exact

- Completed all 16 words of `func_15088270` by retaining the incoming record
  index separately, then reusing `arg0` for the computed record pointer before
  converting its float at offset `0x14` to an integer.
- Added ten guarded scheduling rows to restore retail's `a1` index lifetime,
  `v1` table-base lifetime, null-path delay slots, and final `a0` record base.
  The patch table now has 923 unique rows and no duplicate keys.
- Linked `0xB56F0` and retail `0xB5720` share SHA-256
  `459eccfdf1e672fe1f29e94dcb9a782ad401863d80c893a74a9ceeaba3f27d2f`.
  Fresh scan: **2641 / 5483 (48.17%)** overall and
  **2073 / 4794 (43.24%)** game, with debugger unchanged at **181 / 181**.

### Bounded-index registration byte-exact

- Completed all 16 words of `func_150142AC` directly by recovering a signed
  `s32` index assigned after the object-flag update and an explicit invalid
  range return for `idx < 0 || idx >= 3`.
- That source restores retail's `v1` lifetime, lower-bound `bltz`, upper-bound
  branch into the `D_800D9AA0[idx]` store, and distinct early/final returns.
  No guarded rows were required; the patch table remains at 913 unique rows.
- Linked `0x4172C` and retail `0x4175C` share SHA-256
  `1fdcdcd00fe78afae49fed648e7f3b6598a9f0f8cf9503eeb0c969e401d833ea`.
  Fresh scan: **2640 / 5483 (48.15%)** overall and
  **2072 / 4794 (43.22%)** game, with debugger unchanged at **181 / 181**.

### Random indexed-effect setup byte-exact

- Completed all 45 words of `func_150718E4`. Reversing its two stack-local
  declarations restores retail's `D_80099BB8` source word at `sp + 0x20` and
  `struct17` at `sp + 0x24`.
- Added ten guarded post-random-call register words to restore retail's
  `t0..t5` lifetimes. Both moved `D_800D154C` loads retain explicit expected
  and replacement relocations; no insertion or control-flow patch is used.
- Linked `0x9ED64` and retail `0x9ED94` share SHA-256
  `f128977f492f1068d911ae7303cfcd80a685d2b28a8d282f84da46832064af76`.
  Fresh scan: **2639 / 5483 (48.13%)** overall and
  **2071 / 4794 (43.20%)** game, with debugger unchanged at **181 / 181**.

### Angle normalization byte-exact

- Completed all 25 words of `func_15144BC8` directly by introducing
  `f32 ret = arg0` and applying both 360-degree normalization loops to that
  local, matching the source shape already used by neighboring
  `func_15144B68`.
- IDO now copies incoming `f12` to `f2`, reuses `f12` for zero, and emits
  retail's exact two branch-likely loops and return sequence. No guarded rows
  were required; the patch table remains at 903 unique rows.
- Linked `0x172048` and retail `0x172078` share SHA-256
  `4045e24a198fb60bd83d11f5ebef1738e49fe3e58ce02b2824547f86b5a9d441`.
  Fresh scan: **2638 / 5483 (48.11%)** overall and
  **2070 / 4794 (43.18%)** game, with debugger unchanged at **181 / 181**.

### Two-word and byte forwarder byte-exact

- Completed all 21 words of `func_151417C4` directly from a typed two-word
  aggregate assignment, a byte-typed first argument, and a one-byte array
  local declared before the aggregate.
- Those source types restore retail's retained `D_8008A074` pointer, two-word
  copy through `at` and `t9`, `sp + 0x1C` record, adjacent `sp + 0x24` byte,
  and low-byte reload from the homed first argument. No guarded rows were
  required; the patch table remains at 903 unique rows.
- Linked `0x16EC44` and retail `0x16EC74` share SHA-256
  `ef850b0471b25abd9bcafff4af8626a3d7fd00d66013e1888ded1ea4574e9d37`.
  Fresh scan: **2637 / 5483 (48.09%)** overall and
  **2069 / 4794 (43.16%)** game, with debugger unchanged at **181 / 181**.

### Float scale-and-offset update byte-exact

- Completed all 19 words of `func_151BD750` while retaining its semantically
  correct halfword conversion, scale, offset, and state-update source.
- Added fifteen guarded scheduling rows and two inserted terminal words to
  restore retail's materialized `2.0f`, ordered multiplies, FP registers,
  halfword-update position, and return sequence. Six moved global-address
  words retain explicit expected and replacement relocations.
- Linked `0x1EABD0` and retail `0x1EAC00` share SHA-256
  `614a29e037a05c46e1fe34e72c91217d5e5e776b72e027dab31c086cbfa4800f`.
  Fresh scan: **2636 / 5483 (48.08%)** overall and
  **2068 / 4794 (43.14%)** game, with debugger unchanged at **181 / 181**.

### Fourth one-word aggregate forwarder byte-exact

- Completed all 19 words of `func_15160274` directly from a `OneWord18D250`
  aggregate loaded from `D_800A6670` and passed by address.
- Corrected this generated slice's stale local `func_15169260(s32, ...)`
  declaration to the established `void *` record contract. IDO then emitted
  the exact record copy, argument setup, call delay store, and three padding
  words without guarded normalization.
- Linked `0x18D6F4` and retail `0x18D724` share SHA-256
  `497bea249d36ac1992358cdbaa93c18017215abfef7e0bde6ff7fd9b6481f632`.
  Fresh scan: **2635 / 5483 (48.06%)** overall and
  **2067 / 4794 (43.12%)** game, with debugger unchanged at **181 / 181**.

### Four-word record fill byte-exact

- Completed all 18 words of `func_1519F3B8` from a typed record at object
  offset `0x58`, with selector-six and selector-seven results stored in the
  first and third words and the other two words cleared.
- Added nine guarded scheduling rows and one inserted retained-base reload to
  reproduce retail's 32-byte frame, `v1` lifetime, interleaved stores, and
  second call delay slot. The patch table has 888 unique rows.
- Linked `0x1CC838` and retail `0x1CC868` share SHA-256
  `255c72317f442f9f907d25041cfeb2102a94d201814a062babd2b30298f1a432`.
  Fresh scan: **2634 / 5483 (48.04%)** overall and
  **2066 / 4794 (43.10%)** game, with debugger unchanged at **181 / 181**.

### Third one-word aggregate forwarder byte-exact

- Completed all 17 words of `func_151D343C` directly from a `OneWordCopy`
  aggregate loaded from `D_800AB168` and passed by address.
- Corrected the maintained `func_15169260` declaration and placeholder
  definition so its record parameter is `void *`, matching all observed
  callers. The exhaustive matcher confirmed no collateral regressions.
- Linked `0x2008BC` and retail `0x2008EC` share SHA-256
  `8bbd4d063f5ac36885613ba73e44a6283782e56102abd80040e3ef4f5d8b4e85`.
  Fresh scan: **2633 / 5483 (48.02%)** overall and
  **2065 / 4794 (43.07%)** game, with debugger unchanged at **181 / 181**.

### Second one-word aggregate forwarder byte-exact

- Completed all 17 words of `func_151A561C` directly from source. Replacing
  its scalar array with `OneWord1D0840`, copying `D_800A8D70` as an aggregate,
  and declaring the callee's record parameter as `void *` reproduces the
  already-proven `func_1518F45C` compiler shape.
- IDO emits retail's exact argument setup, source HI/LO pair, copy through
  `at`, call delay store, epilogue, and trailing padding word. No guarded rows
  are required.
- Linked `0x1D2A9C` and retail `0x1D2ACC` share SHA-256
  `4a45a442193db0684da0464798590aa269e40e6c6c2e7865c0716abec79c107a`.
  Fresh scan: **2632 / 5483 (48.00%)** overall and
  **2064 / 4794 (43.05%)** game, with debugger unchanged at **181 / 181**.

### Float-record update byte-exact

- Gave `func_1518F89C` a typed record for its float fields at object offsets
  `0x30`, `0x3C`, and `0x40`, recovering retail's `f4/f8/f6/f10` allocation.
- Twelve guarded rows and one inserted `nop` restore the first call's argument
  home and delay slot, retain the field base in `v0`, preserve retail's FP
  operand order, move the second call relocation, and store through `v0` in
  that call's delay slot.
- Linked `0x1BCD1C` and retail `0x1BCD4C` share SHA-256
  `5f7e34a4ac1ba1b56e1d13de47a39512e6935234606e7a12141f5aeb301270f5`.
  Fresh scan: **2631 / 5483 (47.98%)** overall and
  **2063 / 4794 (43.03%)** game, with debugger unchanged at **181 / 181**.

### Selected state-block reset byte-exact

- Corrected `func_1508F060` to select row two of `D_800D2460` before clearing
  row-relative bytes `0x1D`, `0x2D`, `0x3D`, and `0x0D`. The previous C used
  the unshifted base and therefore targeted the wrong bytes.
- IDO folds the constant selected-row pointer into four direct offsets. Nine
  guarded rows with three insertions restore retail's explicit `li 2`,
  shift/base-add sequence, store order, and moved global HI/LO relocations.
- Linked `0xBC4E0` and retail `0xBC510` share SHA-256
  `5a6bee06d54645060055d96fea8a8d6bd8253996ea416f5e385bc7133ed93ebe`.
  Fresh scan: **2630 / 5483 (47.97%)** overall and
  **2062 / 4794 (43.01%)** game, with debugger unchanged at **181 / 181**.

### Indirect callback forwarder byte-exact

- Completed all 16 words of `func_151A5130` directly from source. Its
  unprototyped callback expression now forwards `arg0`, `arg1`, and the
  declared signed-halfword `arg2` instead of calling with an empty argument
  list.
- Making those incoming arguments observable removes the unnecessary `arg0`
  home store and restores retail's `sll`/`sra` narrowing of `arg2` back into
  `a2`, plus the exact `t8`/`t9`/`at` callback-table schedule. No guarded rows
  are required.
- Linked `0x1D25B0` and retail `0x1D25E0` share SHA-256
  `2ad708b8b146d23e66d5aaaf986a104bede706f803d39c5d2febf7bfdc9f910f`.
  Fresh scan: **2629 / 5483 (47.95%)** overall and
  **2061 / 4794 (42.99%)** game, with debugger unchanged at **181 / 181**.

### One-word aggregate forwarder byte-exact

- Completed all 16 words of `func_1518F45C` directly from source. Replacing
  its scalar array with `OneWord1BA1D0`, copying `D_800A74D4` as an aggregate,
  and declaring the callee's record parameter as `void *` restores retail's
  stack-record pointer and source-address lifetimes.
- IDO now reproduces the exact argument-home store, byte narrowing,
  `D_800A74D4` HI/LO relocation pair, `at` copy, call delay store, and
  epilogue. No guarded rows are required.
- Linked `0x1BC8DC` and retail `0x1BC90C` share SHA-256
  `a12d1a70f23ef188ceab15dfff522bff9dc5c41350fa247959c712cad4992c5c`.
  Fresh scan: **2628 / 5483 (47.93%)** overall and
  **2060 / 4794 (42.97%)** game, with debugger unchanged at **181 / 181**.

### Delimiter split byte-exact

- Replaced the zero-return placeholder for `func_1516A770` with its complete
  delimiter-splitting loop. It scans to the terminating zero, replaces each
  `0xBD` byte with zero, and returns the number of resulting fields.
- Keeping the source as repeated `*arg0` reads gives IDO retail's exact `v0`
  byte lifetime, `a1` delimiter constant, branch-likely loads, conditional
  count update, and shared epilogue. All 16 words match directly with no
  guarded rows.
- Linked `0x197BF0` and retail `0x197C20` share SHA-256
  `059a7d6e9e7166f4c154face31ebe5ddfbbfb064c34253e110bafa6ea0bf10d2`.
  Fresh scan: **2627 / 5483 (47.91%)** overall and
  **2059 / 4794 (42.95%)** game, with debugger unchanged at **181 / 181**.

### Fixed-matrix identity byte-exact

- Completed all 16 words of `func_150A7B80`. The C source now states the eight
  fixed-matrix clears explicitly, followed by the four diagonal halfword
  writes, instead of relying on a loop that does not reflect retail's shape.
- IDO 5.3 still expands each `u64` clear into paired 32-bit stores, overflowing
  the 64-byte retail slot. `pad_c_object.py` can now apply stale-guarded word
  replacements to an overflow trampoline, including explicit relocation
  validation; fourteen guarded rows reproduce retail's 64-bit stores and
  diagonal schedule. A focused regression test covers that path.
- Linked `0xD5000` and retail `0xD5030` share SHA-256
  `108873d13a1c690c87868608bf80cf08d8f25d68c2effd60fe2268c9253dde17`.
  Fresh scan: **2626 / 5483 (47.89%)** overall and
  **2058 / 4794 (42.93%)** game, with debugger unchanged at **181 / 181**.

### Global selection byte-exact

- Skipped `func_151F892C` and `func_151F8960`: both are explicitly handwritten
  helpers that consume non-ABI live registers and are not valid C-restoration
  targets despite their padded placeholders appearing in matcher output.
- Completed all 15 words of `func_1502C380` directly from source. Chaining the
  two global assignments preserves retail's early `D_800C3E88` address in
  `v0` and the selected table value in `t8`; no guarded rows are required.
- Linked `0x59800` and retail `0x59830` share SHA-256
  `5ac1848a7f9245f00f951fd6a5260b0718bb374820703bff54ae237941375025`.
  Fresh scan: **2625 / 5483 (47.88%)** overall and
  **2057 / 4794 (42.91%)** game, with debugger unchanged at **181 / 181**.

### Nested-state flag byte-exact

- Completed all 15 words of `func_151C9B64` directly from source. The
  generated condition had the two outcomes reversed relative to retail:
  nonzero nested state clears bit 1 at object offset `0x58` and writes zero,
  while zero nested state writes one.
- Writing the branches in retail order and naming the nested pointer restores
  IDO's exact `v0`, `t6` through `t9`, and branch-likely schedule. No guarded
  patch rows are required.
- Linked `0x1F6FE4` and retail `0x1F7014` share SHA-256
  `858ab5572befd445453963a3e2f71e301e601166088a9fbfd54a0da147819bbc`.
  Fresh scan: **2624 / 5483 (47.86%)** overall and
  **2056 / 4794 (42.89%)** game, with debugger unchanged at **181 / 181**.

### Byte-gated optional call byte-exact

- Completed all 15 words of `func_151A9024`. The existing C behavior was
  correct, but IDO rotated its argument-home store, `u8` narrowing, `ra` save,
  gate load, and optional call schedule.
- Thirteen guarded words reproduce retail's `t6`/`t7` lifetimes and early
  epilogue, including an explicit relocation move for `func_151A931C`. The
  patch table now has 844 unique rows.
- Linked `0x1D64A4` and retail `0x1D64D4` share SHA-256
  `7dc4eef7baf0bc0fd3f7384828426f0f8cb11046bf1995f5dd14d527dc2fdf9c`.
  Fresh scan: **2623 / 5483 (47.84%)** overall and
  **2055 / 4794 (42.87%)** game, with debugger unchanged at **181 / 181**.

### Five-global reset order byte-exact

- Completed all 15 words of `func_1519582C`. Volatile target pointers recover
  retail's two explicit address completions and exact function size; eight
  guarded relocation/scheduling words preserve the opening `v0`/`v1` preload
  and interleaved direct store.
- The final seven words match directly. The patch table now has 831 unique
  rows, eight for this function.
- Linked `0x1C2CAC` and retail `0x1C2CDC` share SHA-256
  `ad45cf74ef6a44637dde894db55c1018e023ef7fd224566b94df67081155c95a`.
  Fresh scan: **2622 / 5483 (47.82%)** overall and
  **2054 / 4794 (42.85%)** game, with debugger unchanged at **181 / 181**.

### Stack-record pointer lifetime byte-exact

- Completed all 17 words of `func_1519072C` directly from source. A contiguous
  local aggregate reproduces retail's unused `sp + 0x18` word, saved record
  pointer at `sp + 0x1C`, and record at `sp + 0x20`.
- The resulting 40-byte frame retains the incoming pointer in `a2` and spills
  the integer-valued record address across the first helper call. No guarded
  rows are required.
- Linked `0x1BDBAC` and retail `0x1BDBDC` share SHA-256
  `6f21df87663fadb3301142c9299fc72547fe44885afb7ae7fbb12668b4ea1939`.
  Fresh scan: **2621 / 5483 (47.80%)** overall and
  **2053 / 4794 (42.82%)** game, with debugger unchanged at **181 / 181**.

### Conditional callback dispatch byte-exact

- Completed all 17 words of `func_1518F858` directly from source. An explicit
  early return and volatile signed-byte pointer restore retail's two offset
  `0x89` loads, `beql` delay-slot epilogue, and callback-table register
  lifetimes without guarded rows.
- Linked `0x1BCCD8` and retail `0x1BCD08` share SHA-256
  `3e7c845da43fd38459e5396305f94fc0425fb79a84c1e68d2d98228cbc382587`.
  Fresh scan: **2620 / 5483 (47.78%)** overall and
  **2052 / 4794 (42.80%)** game, with debugger unchanged at **181 / 181**.

### Angle normalization byte-exact

- Completed all 24 words of `func_15144B68`. A named result local gives the
  normalized value retail's `f2` lifetime while zero remains in `f12`; both
  subtract/add loops and their branch-delay updates then match directly.
- Compact source probes left only the opening compare and input-copy order.
  Two guarded scheduling words reproduce retail without changing control flow
  or relocations. The patch table now has 823 unique rows.
- Linked `0x171FE8` and retail `0x172018` share SHA-256
  `3092544aa3402e37d36842a0d1fec70e2bb75c61795fef11a33a3c7e0aefc9f2`.
  Fresh scan: **2619 / 5483 (47.77%)** overall and
  **2051 / 4794 (42.78%)** game, with debugger unchanged at **181 / 181**.

### Embedded vertex-copy base lifetime byte-exact

- Completed all 15 words of `func_1514143C`. The logical C already copied
  position components `0x34`, `0x38`, and `0x3C` into the optional vertex at
  `0x154`; retail additionally retains an embedded `arg0 + 0x110` base and
  reloads that vertex through offset `0x44` for each store.
- Nested-layout source probes still folded to direct `0x154(a0)` accesses. A
  volatile register-pointer probe retained the base but introduced an 8-byte
  frame and expanded to 20 words, so it was rejected. Thirteen guarded words
  plus two supported inserted words preserve the exact retail schedule.
- The patch table now has 821 unique rows. Linked `0x16E8BC` and retail
  `0x16E8EC` share SHA-256
  `ece713344a6d544b52be8d4872c069537905ba5ec0888141d0f8d854a64c9dcb`.
  Fresh scan: **2618 / 5483 (47.75%)** overall and
  **2050 / 4794 (42.76%)** game, with debugger unchanged at **181 / 181**.

### Two-component scaling loop byte-exact

- Converted all 16 words of `func_15131918` from a false `return 0`
  placeholder to byte-exact C. The loop scales float components zero and two
  for `D_800BE9E4` records.
- Both callers now type their field at offset `0xA8` as `f32`, preserving the
  mixed pointer/float ABI's raw `lw a1` transfer and retail's opening
  `mtc1 a1,f12`. A raw-bit union probe overflowed the function and was
  rejected. No guarded rows were added.
- The patch table remains at 808 unique rows. Linked `0x15ED98` and retail
  `0x15EDC8` share SHA-256
  `3357c69ce2bd665e8ca4744d549d7068cc8edb12fb9c766e8a0443c38f6f1232`.
  Fresh scan: **2617 / 5483 (47.73%)** overall and
  **2049 / 4794 (42.74%)** game, with debugger unchanged at **181 / 181**.

### Record-pointer repeated-field lifetime byte-exact

- Completed all 19 words of `func_150CFBEC` directly from source. Moving the
  `arg0 + 0x70` record pointer outside the condition places its materialization
  in retail's branch delay slot and retains it in `v0` for every record access.
- Volatile source-field reads preserve retail's two separate loads from
  `arg0 + 0x10`, restoring the FP load/subtract schedule. No guarded rows or
  relocations apply.
- The patch table remains at 808 unique rows. Linked `0xFD06C` and retail
  `0xFD09C` share SHA-256
  `dbdf458a3a3766235455debb74b0a6ddaff00f12354927807aa5baec169d3870`.
  Fresh scan: **2616 / 5483 (47.71%)** overall and
  **2048 / 4794 (42.72%)** game, with debugger unchanged at **181 / 181**.

### Fourth-component continuation restored

- Restored all 13 original words of `func_150A7A14` from retained
  `asm/D4E10.s`. The false `return 0` C placeholder could not model the
  continuation's inherited FP registers, stack argument, or return through
  saved register `t9`.
- The restored body and the complete 18-word `func_150A7A00`/`func_150A7A14`
  trampoline pair are linked byte-identical to retail. No guarded rows were
  added.
- The patch table remains at 808 unique rows. The body at linked `0xD4E94`
  and retail `0xD4EC4` shares SHA-256
  `75bbc5234eee00ae6d58550ab03989349ce347c30c8c2cea8403183d9f36c8d0`.
  Fresh C scan: **2615 / 5483 (47.69%)** overall and
  **2047 / 4794 (42.70%)** game, with one function correctly transferred from
  the C denominator to raw assembly.

### Null-first table populator byte-exact

- Completed all 30 words of `func_15085B70` directly from source. Reversing
  the condition to test `temp_v0 == 0` places retail's compact zeroing path
  before the populated path and restores all thirteen differing words.
- The complete frame, both calls, delay slots, six global relocation pairs,
  branch targets, and epilogue are source-emitted and exact. No guarded rows
  were added.
- The patch table remains at 808 unique rows. Linked `0xB2FF0` and retail
  `0xB3020` share SHA-256
  `420680f426f2b1f2b80d4d03a344b7ca8de125e0cc9067820c2464ec5e5d5a19`.
  Fresh scan: **2615 / 5484 (47.68%)** overall and
  **2047 / 4795 (42.69%)** game, with debugger unchanged at **181 / 181**.

### Retained local-record pointer byte-exact

- Completed all 17 words of `func_1507FF94`. A volatile local pointer retained
  across the first call restores retail's 40-byte frame, pointer spill/reload,
  and complete function extent.
- The first call uses `&rec` directly while the second uses the retained local,
  avoiding the extra volatile load that overflowed the slot. Five guarded,
  non-relocating words finish the independent prologue setup order.
- The patch table now has 808 unique rows. Linked `0xAD414` and retail
  `0xAD444` share SHA-256
  `e4200d3dee6cba3505c9510b8b1bf1aec92d126dead87a84c041535655634e4f`.
  Fresh scan: **2614 / 5484 (47.67%)** overall and
  **2046 / 4795 (42.67%)** game, with debugger unchanged at **181 / 181**.

### Packed four-byte reader byte-exact

- Completed all 16 words of `func_1507A3E8`. The plain packed-byte expression
  remains the clearest source after prior local, term-order, accumulator, and
  volatile experiments all produced inferior schedules.
- Thirteen guarded words restore retail's adjacent address/load pairs and
  `t7` through `t9` merge lifetimes. All four global HI16/LO16 relocation
  pairs are explicitly validated and moved with their loads.
- The patch table now has 803 unique rows. Linked `0xA7868` and retail
  `0xA7898` share SHA-256
  `c542b461c15efeba5d814856ab3ff92fc74b2482448be8462a1718c97a228e9d`.
  Fresh scan: **2613 / 5484 (47.65%)** overall and
  **2045 / 4795 (42.65%)** game, with debugger unchanged at **181 / 181**.

### Chunked-boundary loop byte-exact

- Completed all 18 words of `func_15043B70` directly from source. Expressing
  the selected chunk as a scalar ternary restores retail's explicit two-arm
  merge and the unconditional branch missing from the prior object.
- That one recovered word realigns the initial exit, loop-back branch, and
  every subsequent instruction. No guarded patch rows or relocations apply.
- The patch table remains at 790 unique rows. Linked `0x70FF0` and retail
  `0x71020` share SHA-256
  `ba904403da942b5a2963e724bdcbec9cf4b4ec668ad4072fece06f24f09fefc2`.
  Fresh scan: **2612 / 5484 (47.63%)** overall and
  **2044 / 4795 (42.63%)** game, with debugger unchanged at **181 / 181**.

### Slot-cursor allocation byte-exact

- Completed all 19 words of `func_150356C8`. Reusing and incrementing the
  loaded slot byte directly restores retail's cursor base register and final
  store while preserving the full original control flow and extent.
- Nine guarded words restore the `t6`/`t7`/`t8`/`t9` arithmetic schedule and
  `t0` table base. The `D_800C3F08` high relocation remains at relative
  `0x10`; its paired low relocation moves from `0x18` to retail's `0x38`.
- The patch table now has 790 unique rows. Linked `0x62B48` and retail
  `0x62B78` share SHA-256
  `ce94daa79799e73dfcc4b67025fc8e51fcb016d97ee6964f07a39a20f6c3b44c`.
  Fresh scan: **2611 / 5484 (47.61%)** overall and
  **2043 / 4795 (42.61%)** game, with debugger unchanged at **181 / 181**.

### Relative-offset tree walk byte-exact

- Completed all 39 words of `func_15002560`. An explicit infinite loop with a
  top null exit restores retail's unconditional loop-back edge. Materializing
  the optional sibling offset in one scalar before its halfword store restores
  eleven additional control-flow and `t7`/`t8`/`t9` schedule words.
- Two guarded, non-relocating words select retail's base-first operand order
  for the child and sibling pointer additions. The recursive call relocation
  remains source-emitted and exact.
- The patch table now has 781 unique rows. Linked `0x2F9E0` and retail
  `0x2FA10` share SHA-256
  `38e72a9437314876eb11b824d041a92158c88f2856a50f2a371ab8c5ec554f8f`.
  Fresh scan: **2610 / 5484 (47.59%)** overall and
  **2042 / 4795 (42.59%)** game, with debugger unchanged at **181 / 181**.

### Signed-byte fallback selector byte-exact

- Completed all 18 words of `func_151E5FAC`. Duplicating the explicit fallback
  return restores separate flag-false and threshold-failure paths; spelling the
  threshold as `>= 5` restores retail's positive branch to the candidate.
- Twelve guarded words restore retail's fallback-address preload/rematerialize
  schedule and move the `D_8008FD8C` and `D_8008FD90` relocation pairs. The
  flag load, final fallback load, and return are unguarded and exact.
- The patch table now has 779 unique rows. Linked `0x21342C` and retail
  `0x21345C` share SHA-256
  `6b4a87b0141da6aebe6c6d4e3a60eefa444d170d0fdf07689f40e48da5d1f7ff`.
  Fresh scan: **2609 / 5484 (47.57%)** overall and
  **2041 / 4795 (42.57%)** game, with debugger unchanged at **181 / 181**.

### Allocation/copy wrapper byte-exact

- Completed all 28 words of `func_15168800` directly from source by expressing
  allocation failure as an explicit early null return before `bcopy`.
- That control-flow shape restores retail's positive branch into the copy
  path, explicit zero-return delay slot, retained allocation in `v1`, stack
  spill across `bcopy`, and both call relocations. No guarded rows were added.
- The patch table remains at 767 unique rows. Linked `0x195C80` and retail
  `0x195CB0` share SHA-256
  `163d065da4eac9216fff364ccc3d94c87935a63389ba18289abde3a2eef4f5f7`.
  Fresh scan: **2608 / 5484 (47.56%)** overall and
  **2040 / 4795 (42.54%)** game, with debugger unchanged at **181 / 181**.

### Duplicate masked-field store byte-exact

- Completed all 40 words of `func_151355B8`. Volatile-qualified accesses to
  the masked field retain retail's duplicate store and directly restore every
  shifted exit-branch target.
- Chained assignment still collapsed to one store. A split loaded-value local
  selected worse registers, while a volatile pointer local emitted the same
  object as direct volatile accesses. Five guarded, non-relocating words select
  retail's `t5` loaded value and `t6` masked result.
- The patch table now has 767 unique rows. Linked `0x162A38` and retail
  `0x162A68` share SHA-256
  `905987a8e0bd8c6da95744f53d6707165b266566a5e67456208c2d84e35d4f97`.
  Fresh scan: **2607 / 5484 (47.54%)** overall and
  **2039 / 4795 (42.52%)** game, with debugger unchanged at **181 / 181**.

### Three-word aggregate forwarder byte-exact

- Completed all 20 words of `func_15131D4C` directly from source by replacing
  three scalar assignments with a typed three-word aggregate copy and declaring
  the callee's first argument as a pointer.
- The aggregate copy alone restored retail's interleaved `lw`/`sw` sequence
  but formed the stack destination in `v0`, making the function one word too
  large. The corrected pointer contract lets IDO form it directly in `a0` and
  restores the complete retail schedule with no guarded rows.
- The patch table remains at 762 unique rows. Linked `0x15F1CC` and retail
  `0x15F1FC` share SHA-256
  `0c3949fd9d561f5442219ef46c00c7ce47d53bf0a05c7263f3e0ff7e392891f0`.
  Fresh scan: **2606 / 5484 (47.52%)** overall and
  **2038 / 4795 (42.50%)** game, with debugger unchanged at **181 / 181**.

### Optional-pointer call wrapper byte-exact

- Completed all 18 words of `func_150E33CC`. Direct dereference, shared-result
  local, and preassigned-selector source probes did not reproduce retail's
  schedule and were reverted.
- Twelve guarded words restore retail's `v0` pointed-value lifetime, early
  selector materialization, zero path, call-delay `a1` move, and epilogue.
  The `func_1000E7A0` relocation moves explicitly from relative offset `0x28`
  to `0x2C`. The frame and final padding word were already exact.
- The patch table now has 762 unique rows. Linked `0x11084C` and retail
  `0x11087C` share SHA-256
  `4e11e68c67960b22b570a25feb7aaff4c509e19a21d120d7eb328c4e489d276a`.
  Fresh scan: **2605 / 5484 (47.50%)** overall and
  **2037 / 4795 (42.48%)** game, with debugger unchanged at **181 / 181**.

### Bounds-checked halfword getter byte-exact

- Completed all 16 words of `func_1508B194` by expressing the bounds check as
  retail's early-zero path. This directly restored the positive branch,
  branch delay slot, explicit zero return, halfword-load position, and final
  return sequence.
- Five guarded words select retail's `t7` record-table base and `t8` 12-byte
  stride while explicitly moving the `D_8008FDD4` HI16 relocation. The
  `D_8008FD90` relocation pair was already exact. The patch table now has 750
  unique rows. Linked `0xB8614` and retail `0xB8644` share SHA-256
  `3b86be0e704bd4067e9efad6096d883a46966c5626da1fb6476ed2dafbb9b1ee`.
  Fresh scan: **2604 / 5484 (47.48%)** overall and
  **2036 / 4795 (42.46%)** game, with debugger unchanged at **181 / 181**.

### Indexed signed-byte getter byte-exact

- Completed all 13 words of `func_150882B0` by declaring the global pointer
  before the retained index, reusing `arg0` for the final record pointer, and
  guarding the remaining ten schedule positions. Retail now preserves the
  index in `a1`, keeps `D_800872A0` in `v1`, and loads through final `a0`.
- The moved `D_800872A0` HI16/LO16 pair is explicitly guarded. The patch table
  now has 745 unique rows. Linked `0xB5730` and retail `0xB5760` share SHA-256
  `7c3ea120c159b30ba557ad53b2e8ab7720ec13bb50a7daebf4f56f9d93ed63c4`.
  Fresh scan: **2603 / 5484 (47.47%)** overall and
  **2035 / 4795 (42.44%)** game, with debugger unchanged at **181 / 181**.

### Three-byte record update byte-exact

- Completed all 46 words of `func_1504BA38` with twelve guarded words that
  restore retail's `v1` record pointer, `a1` byte-two value, and `v0` byte-one
  value. The arithmetic, branches, stores, floating-point conversions, and
  both existing global relocation pairs were already correctly positioned.
- The patch table now has 735 unique rows. Linked `0x78EB8` and retail
  `0x78EE8` share SHA-256
  `f6b31137a29e73ab755499f92e5ae0090afb835db155431476753cb081e410b4`.
  Fresh scan: **2602 / 5484 (47.45%)** overall and
  **2034 / 4795 (42.42%)** game, with debugger unchanged at **181 / 181**.

### Timed toggle/table update byte-exact

- Completed all 21 words of `func_150337E4` by replacing its accumulated-value
  and table-index locals with direct field expressions. IDO now emits retail's
  `t8` accumulated counter, `t0`/`t1` toggle pipeline, and `t2`/`t4` table
  pipeline directly from C.
- No guarded rows were added; the patch table remains at 723 unique rows.
  Linked `0x60C64` and retail `0x60C94` share SHA-256
  `54b59cd622a7bc63daf39021633dca3bfe362e4cf2812761b2aa81f4273bac76`.
  Fresh scan: **2601 / 5484 (47.43%)** overall and
  **2033 / 4795 (42.40%)** game, with debugger unchanged at **181 / 181**.

### Mirrored counter/table update byte-exact

- Completed all 20 words of `func_15031E2C` with twelve guarded register-choice
  words after declaration, assignment, and K&R/ANSI source probes produced the
  same stable object. The guards recover retail's `v1` counter, `v0` mirrored
  index, `t9` increment, and `t8` table-value pipeline.
- The two table-address guards preserve the `D_800902BC` HI16/LO16 relocation
  pair. The patch table now has 723 unique rows. Linked `0x5F2AC` and retail
  `0x5F2DC` share SHA-256
  `d1fcfc04e9e799d2864afd8d204547594fe1f79d94eba637d63fe84656099ddf`.
  Fresh scan after this two-function pass: **2600 / 5484 (47.41%)** overall and
  **2032 / 4795 (42.38%)** game, with debugger unchanged at **181 / 181**.

### Table sum loop byte-exact

- Completed all 19 words of `func_1501CFF8` by ordering the sum/index locals
  before directly testing `D_800C363A[arg0]` at entry and on the loop back edge.
  IDO reuses one byte load while preserving retail's `a1` count, `v0` index,
  `v1` sum, and `slt`/`bnez` loop test.
- No guarded rows were added for this function. Linked `0x4A478` and retail
  `0x4A4A8` share SHA-256
  `5e8669328165c7bbc1972b40dfe5c9162102aff28a9088f06f5276ee387ee090`.

### Conditional minimum update byte-exact

- Completed all 16 words of `func_151ACA20` by declaring the output candidate
  before the signed-halfword source and expressing four-bit scaling as one
  signed assignment. IDO now emits retail's `v1` source and `v0` candidate
  lifetimes, both branch-likely delay slots, store, and return schedule.
- No guarded rows were added; the patch table remains at 711 unique rows. The
  linked span at `0x1D9EA0` and retail span at `0x1D9ED0` share SHA-256
  `2650fd7f0a4ea8c62ed6c2de28b52fbf4bac60fc9924be173f872ad030eb954a`.
  Fresh scan: **2598 / 5484 (47.37%)** overall and
  **2030 / 4795 (42.34%)** game, with debugger unchanged at **181 / 181**.

### Byte lookup forwarding wrapper byte-exact

- Completed all 15 words of `func_15178E14` by replacing its K&R definition
  with an ANSI byte parameter and giving both local callees their actual
  argument contracts. IDO now emits retail's narrowing, first-call nop delay
  slot, forwarded-result delay slot, and complete epilogue directly from C.
- No guarded rows were added; the patch table remains at 711 unique rows. The
  linked span at `0x1A6294` and retail span at `0x1A62C4` share SHA-256
  `a019d616adcd1685df8d90af91eb0c6da92463538aeeb540adf85fd4e9ccbbfd`.
  Fresh scan: **2597 / 5484 (47.36%)** overall and
  **2029 / 4795 (42.31%)** game, with debugger unchanged at **181 / 181**.

### Position and phase update byte-exact

- Completed all 28 words of `func_15141564` by expressing its position update
  in multiplication-first order and guarding the two residual base-pointer
  spill/reload slot words. The source change restores retail's frame and both
  FP-register pipelines; no relocation or instruction position changes.
- The patch table now has 711 unique rows. The linked span at `0x16E9E4` and
  retail span at `0x16EA14` share SHA-256
  `364192b03df56b95681c27fb0a27b22cdeacb071d6a9a462c1b4a07bcb72364b`.
  Fresh scan: **2596 / 5484 (47.34%)** overall and
  **2028 / 4795 (42.29%)** game, with debugger unchanged at **181 / 181**.

### Two-word aggregate call byte-exact

- Completed all 17 words of `func_151090DC` by replacing two scalar stack
  assignments with a typed two-word aggregate initializer and passing the
  aggregate through the callee's pointer ABI. IDO now emits retail's complete
  aggregate-copy and argument schedule directly from C.
- No guarded rows were added; the patch table remains at 709 unique rows. The
  linked span at `0x13655C` and retail span at `0x13658C` share SHA-256
  `55ddb338289c96218fdbd1278286280acc0413a16f923996dfc3be3651ad8e9a`.
  Fresh scan: **2595 / 5484 (47.32%)** overall and
  **2027 / 4795 (42.27%)** game, with debugger unchanged at **181 / 181**.

### Record activation loop byte-exact

- Completed all 17 words of `func_150B6D34` by simplifying its cursor loop and
  guarding nine residual cursor/record-pointer register choices. The three
  address-setup guards explicitly preserve or move the corresponding
  `D_800D9898` and `D_800D98A4` relocations.
- The patch table now has 709 unique rows. The complete linked span at
  `0xE41B4` and retail span at `0xE41E4` share SHA-256
  `03ce6560ee0992ce0939368415ac8387c68e5cac8aa8022d68bc01deea2f1124`.
  Fresh scan: **2594 / 5484 (47.30%)** overall and
  **2026 / 4795 (42.25%)** game, with debugger unchanged at **181 / 181**.

### Five-byte queue shift byte-exact

- Completed all 15 words of `func_1507EEB8` by replacing five scalar byte
  assignments with the original fixed reverse loop. IDO now emits retail's
  `arg1 + 4` induction pointer, unrolled load/store order, and final new-byte
  store directly from C.
- No guarded rows were added. The patch table remains at 700 unique rows. The
  complete linked span at `0xAC338` and retail span at `0xAC368` share SHA-256
  `bec0e721180c79c0dfb9915789558fbb481fe906c5fee1e835496f9727260b1f`.
  Fresh scan: **2593 / 5484 (47.28%)** overall and
  **2025 / 4795 (42.23%)** game, with debugger unchanged at **181 / 181**.

### Interpolation register match byte-exact

- Completed all 58 words of `func_15074A94` by expressing the interpolation as
  one factor-times-distance calculation and guarding eleven residual
  floating-point register choices. The three patched constant loads retain
  their original relocations, and no words or relocations move.
- Added `retail_word_patches.us.csv` as an explicit prerequisite of both
  hand-maintained padded-object rules. The subsequent complete invalidation and
  rebuild passed, proving all current expected-word guards against fresh
  compiler output instead of potentially stale objects.
- The patch table now has 700 unique rows. The complete linked span at
  `0xA1F14` and retail span at `0xA1F44` share SHA-256
  `4b85cc9681ac9d582b3f068553382b892a04d8c7201c789e79347a5ba4cbfc86`.
  Fresh scan: **2592 / 5484 (47.26%)** overall and
  **2024 / 4795 (42.21%)** game, with debugger unchanged at **181 / 181**.

### Local-record pointer schedule byte-exact

- Completed all 20 words of `func_150717E0` through eleven guarded schedule
  words. Retail preserves the local-record pointer at `sp+0x18` across the
  first call; the current compiler rematerializes `sp+0x20`. The guards restore
  that pointer lifetime, both call positions and relocations, delay slots, and
  epilogue order without inserting words.
- The patch table now has 689 unique rows. The complete linked span at
  `0x9EC60` and retail span at `0x9EC90` share SHA-256
  `6cb1079ed02c68652e32fb90cad0f0e18cc65a1ed4deec89e7af75b236fe2d7a`.
  Fresh scan: **2591 / 5484 (47.25%)** overall and
  **2023 / 4795 (42.19%)** game, with debugger unchanged at **181 / 181**.

## 2026-09-25

### Record-construction order byte-exact

- Completed all 34 words of `func_151D74B0` by moving the record pointer
  assignment ahead of its three byte fields. This restores retail's pointer
  store before the remaining byte and stack-argument loads and closes the
  ten-difference game tier without guarded rows.
- The patch table remains at 678 unique rows. The complete linked span at
  `0x204930` and retail span at `0x204960` share SHA-256
  `002a8c708dffc31c8235fae006313e893a65b893b7ffcc3e730a65a2ec243d01`.
  Fresh scan: **2590 / 5484 (47.23%)** overall and
  **2022 / 4795 (42.17%)** game, with debugger unchanged at **181 / 181**.

### Seven-argument wrapper byte-exact

- Completed all 19 words of `func_151581D8` through ten guarded prologue and
  argument-preparation schedule words. Every value, stack slot, call
  relocation, delay-slot store, and epilogue instruction was already present;
  the guards move no relocations and insert no words.
- The patch table now has 678 rows with no duplicate keys; this function has
  ten rows and no insertion-bearing rows. The complete linked span at
  `0x185658` and retail span at `0x185688` share SHA-256
  `0792b2f5cacd300b78d1eda3584b4422de9d312ba57cc4a943b7be7af3efd4be`.
  Fresh scan: **2589 / 5484 (47.21%)** overall and
  **2021 / 4795 (42.15%)** game, with debugger unchanged at **181 / 181**.

### Two-word record forwarder byte-exact

- Completed all 18 words of `func_15133E3C` by replacing two scalar array
  assignments with a `TwoWord15F680` aggregate initializer and correcting
  `func_15169260`'s first parameter to `void *`. This restores retail's
  direct `a0` local address, `at`/`t9` copy, and call-delay store from C.
- No guarded rows were added. The patch table remains at 668 unique rows.
  The complete linked span at `0x1612BC` and retail span at `0x1612EC` share
  SHA-256
  `edc82dab6f11e3d95b78955ef9d2bb24d4330125fc2decc6f04d9861724ebd28`.
  Fresh scan: **2588 / 5484 (47.19%)** overall and
  **2020 / 4795 (42.13%)** game, with debugger unchanged at **181 / 181**.

### Float-state reset byte-exact

- Completed all 17 words of `func_15133A50` by naming the pending sum,
  restoring retail's field-store order, and guarding the remaining nine
  `f0`/`f2`/`f8` register words. The guards move no relocations, insert no
  words, and change no addresses or control flow.
- The patch table now has 668 rows with no duplicate keys; this function has
  nine rows and no insertion-bearing rows. The complete linked span at
  `0x160ED0` and retail span at `0x160F00` share SHA-256
  `d46c11f94cffe15df0b700b643efd7c5844f60926746c7f45c7fb8c409ef7705`.
  Fresh scan: **2587 / 5484 (47.17%)** overall and
  **2019 / 4795 (42.11%)** game, with debugger unchanged at **181 / 181**.

### Repeated float-scale loop byte-exact

- Replaced the zero-return `func_151318E8` placeholder with retail's
  `D_800BE9E4`-counted multiplication loop. Its typed mixed pointer/float ABI
  emits the retail `mtc1 a1,f12` entry, while caller `func_151316AC` remains
  independently byte-exact.
- No guarded rows were added. The target linked/retail spans share SHA-256
  `dd1732f04e8fad0d5daed64f7a9833097445188e8d285d53da86220914bb350b`,
  and the caller spans share
  `22cb90341b57ea50023850f7cab38aaca0afbf2da61e0637c62336feffc0198e`.
  The patch table remains at 659 unique rows. Fresh scan:
  **2586 / 5484 (47.16%)** overall and **2018 / 4795 (42.09%)** game, with
  debugger unchanged at **181 / 181**.

### Short-circuit threshold update byte-exact

- Completed all 19 tracked words of `func_150DE2C4` by combining two
  equivalent field clears under one logical-OR condition. This restores
  retail's branch-likely delay-slot clear, shared second clear, and trailing
  padding directly from C, with no guarded rows.
- The patch table remains at 659 rows with no duplicate keys and no row for
  this function. The complete linked span at `0x10B744` and retail span at
  `0x10B774` share SHA-256
  `fc341f80de7976c7bcfee30c55345917dd6461764c3c1015adf431f8ad893c4b`.
  Fresh scan: **2585 / 5484 (47.14%)** overall and
  **2017 / 4795 (42.06%)** game, with debugger unchanged at **181 / 181**.

### Global-coordinate update byte-exact

- Completed all 28 words of `func_150CF578` by naming the loaded
  `D_800BE9E4` value before deriving the 28-times temporary. This restores
  retail's `v0` source lifetime, `v1` product lifetime, and instruction
  schedule directly from C, with no guarded rows.
- The patch table remains at 659 rows with no duplicate keys and no row for
  this function. The complete linked span at `0xFC9F8` and retail span at
  `0xFCA28` share SHA-256
  `9380ec55443833e5ed9950f30c40317a0bd33d130dbcba4a2a34e2aa36427898`.
  Fresh scan: **2584 / 5484 (47.12%)** overall and
  **2016 / 4795 (42.04%)** game, with debugger unchanged at **181 / 181**.

### Display-list cursor and state-byte clear byte-exact

- Completed all 15 words of `func_15096934` with an independent nine-row
  application of the generated-slice cursor expansion. It preserves the
  original cursor in `v1`, emits the `D_80087408` command pair, advances the
  cursor, clears byte `D_800D2DAB`, and restores the retail return sequence.
- All four moved relocations are explicitly guarded. The patch table now has
  659 rows with no duplicate keys; this function has nine rows and two
  insertion-bearing rows.
- The complete linked span at ELF `0xD6934` and retail `0xC3DE4` shares
  SHA-256
  `0ce9e94a848eba73ef07a221cf21947ea38ba900526bc53580d4a1f9417ea7ed`.
  Fresh scan: **2583 / 5484 (47.10%)** overall and
  **2015 / 4795 (42.02%)** game, with debugger unchanged at **181 / 181**.

### Display-list cursor and state clear byte-exact

- Completed all 12 words of `func_15094F40` through the established
  generated-slice cursor expansion. Nine guarded rows preserve the original
  cursor in `v1`, restore retail's command-store and global-clear schedule,
  and insert the advanced-cursor copy plus final return delay slot.
- All four moved relocations are explicitly guarded. The patch table now has
  650 rows with no duplicate keys; this function has nine rows and two
  insertion-bearing rows.
- The complete linked span at ELF `0xD4F40` and retail `0xC23F0` shares
  SHA-256
  `989b94637e932e7057eebd6fad9b2ef29c52742fc6ad60b41c25aa1e85b783b1`.
  Fresh scan: **2582 / 5484 (47.08%)** overall and
  **2014 / 4795 (42.00%)** game, with debugger unchanged at **181 / 181**.

### Linked-list search byte-exact

- Completed all 16 words of `func_15033E84` by loading `node->next` before
  the type comparison and assigning `node = next` in the loop condition.
  This recovers retail's preloaded `v0` next pointer, ordinary comparison and
  loop branches, and `move v1, v0` branch-delay update directly from C.
- No guarded rows were added; the patch table remains at 641 rows with no
  duplicate keys. The complete linked span at ELF `0x73E84` and retail
  `0x61334` shares SHA-256
  `944012697ea2666086f345f59f6c1cd8f750eb86b20835a40aa096bbae61d6c8`.
- Fresh scan: **2581 / 5484 (47.06%)** overall and
  **2013 / 4795 (41.98%)** game, with debugger unchanged at **181 / 181**.

### Packed-byte writer byte-exact

- Completed all 17 words of `func_1502EA0C` with ten guarded scheduling and
  register words. The C already expresses the four byte fields and packed
  32-bit value correctly; the guards recover retail's shift/store interleave
  and temporary lifetimes without changing control flow or relocations.
- Explicit partial-value locals did not change IDO allocation. Volatile stores
  improved byte-store order but increased the total differing words, so that
  experiment was rejected. The patch table now has 641 rows with no duplicate
  keys.
- The complete linked span at ELF `0x6EA0C` and retail `0x5BEBC` shares SHA-256
  `99bafbd40986e990628a4a760a04fedeb2eabda80b5ecd0355427dd6a209a1aa`.
  Fresh scan: **2580 / 5484 (47.05%)** overall and
  **2012 / 4795 (41.96%)** game, with debugger unchanged at **181 / 181**.

### Four-word state clear byte-exact

- Replaced the `func_151E81EC` placeholder with a real four-word state clear
  and byte reset. A local struct and chained assignment preserve all five
  stores, retail order, the 10-word extent, and the correct `void` return.
- Six guarded relocation words recover retail's two shared `$at` high halves.
  The patch table now has 631 rows with no duplicate keys. The complete linked
  span at ELF `0x2281EC` and retail `0x21569C` shares SHA-256
  `8ffd94c76c5a73aa7b0eaa0be788a471eb78a68224cc3b6365c6ce6666ddd16d`.
- Fresh scan: **2579 / 5484 (47.03%)** overall and
  **2011 / 4795 (41.94%)** game, with debugger unchanged at **181 / 181**.

### Indexed signed-byte selector byte-exact

- Completed all 18 words of `func_151E5F64` by expressing the enabled lookup
  as the positive branch and leaving the disabled `return arg0` path last.
  IDO now reproduces retail's two return sites, non-likely signed clamp, and
  exact branch layout directly from C.
- No patch rows were added. The patch table remains at 625 rows with no
  duplicate keys. The complete linked span at ELF `0x225F64` and retail
  `0x213414` shares SHA-256
  `0beb65faa2a495c68f3866e3915fa51747ea7149656f30e71e53a1a6828cdace`.
- Fresh scan: **2578 / 5484 (47.01%)** overall and
  **2010 / 4795 (41.92%)** game, with debugger unchanged at **181 / 181**.

### Callback selector twin byte-exact

- Completed all 33 words of `func_151963B4` with its own nine guarded
  pointer/selector register words. The structure matches `func_15196330`, while
  the independently preserved final relocation targets `func_15147928`.
- The patch table now has 625 rows with no duplicate keys. The complete linked
  span at ELF `0x1D63B4` and retail `0x1C3864` shares SHA-256
  `cf3ff8a08a41e22809847c2dccc1abd13cd671b7db20372f07d2575926cd3adf`.
- Fresh scan: **2577 / 5484 (46.99%)** overall and
  **2009 / 4795 (41.90%)** game, with debugger unchanged at **181 / 181**.

### Callback selector registers byte-exact

- Completed all 33 words of `func_15196330` with nine guarded words rotating
  the retained record pointer into `v0` and both signed callback selectors into
  `v1`. Its frame, branches, table dispatches, final call, and relocations were
  already exact.
- Separate declarations and a widened selector did not change allocation;
  reversed declarations moved the spill slot and were rejected. The patch
  table now has 616 rows with no duplicate keys.
- The independent complete-span SHA-256 is
  `8661611d0a0313dbe6f9307ad9d011fdeda11efe9b9a69fd63b2fefd45d67efb`.
  Fresh scan: **2576 / 5484 (46.97%)** overall and
  **2008 / 4795 (41.88%)** game, with debugger unchanged at **181 / 181**.

### Display-list cursor twin byte-exact

- Completed all 14 words of `func_15166FD8` with eight guarded transformations
  preserving the original cursor in `v1`, resolving `D_80089470` before the
  command constant, storing through `v1`, and returning the advanced cursor.
- Its typed `Gfx` source was already correct. The established generated-slice
  insertion path restores the two IDO-elided lifetime words while guarding the
  moved `R_MIPS_LO16` relocation. The patch table now has 607 rows and no
  duplicate keys.
- The independent complete-span SHA-256 is
  `4905a240f582ba884f83a2b6ab96c6f6109fbf5a5d54ce9e50a382b3f95c8ef3`.
  Fresh scan: **2575 / 5484 (46.95%)** overall and
  **2007 / 4795 (41.86%)** game, with debugger unchanged at **181 / 181**.

### Record-stride register lifetimes byte-exact

- Completed all 16 words of `func_1512D6B0` with nine guarded words selecting
  retail's `t7` index, `t6` global base, and `t8` 176-byte record offset.
  Control flow, field loads, equality reduction, and padding were already
  exact.
- An explicit-local source experiment spread the same values into argument
  registers and was reverted. The patch table now has 599 rows with no
  duplicate keys.
- The independent complete-span SHA-256 is
  `3266b541de99bd06941b770d4b38988db458dab3e62d8deb16339a6f96df436a`.
  Fresh scan: **2574 / 5484 (46.94%)** overall and
  **2006 / 4795 (41.84%)** game, with debugger unchanged at **181 / 181**.

### Display-list cursor expansion byte-exact

- Completed all 15 words of `func_1510E634` using the established typed `Gfx`
  writer idiom and eight guarded rows. Two rows insert the missing preserved
  cursor and return-delay words; the remaining rows restore retail's address,
  command, store, cursor-advance, and return schedule.
- Extended `pad_generated_object.py` to support bounded `insert_after` words,
  including retail-span accounting and shifted jump-label emission. All five
  padding-tool tests pass, including the new generated insertion fixture.
- The independent complete-span SHA-256 is
  `28d8bacba51037d5bdf8db9e479119ce8122427682c41a509a427bc6079ec25e`.
  The patch table has 590 unique rows. Fresh scan: **2573 / 5484 (46.92%)**
  overall and **2005 / 4795 (41.81%)** game, with debugger unchanged at
  **181 / 181**.

### Chained global clear byte-exact

- Completed all ten words of `func_15080200` by expressing its three zero
  stores as one chained assignment. IDO now retains `v0` and `v1` addresses
  for the first two globals and emits the retail store order naturally.
- Explicit local pointer variables were optimized back into three direct
  stores and were rejected. No guarded patch rows were needed; the table
  remains at 582 rows with no duplicate keys.
- The independent complete-span SHA-256 is
  `5fe7f7f6c8dc160faba47b5b2a363a0d7a7ca5dadc9982da1e3fe41d9141e7b6`.
  Fresh scan: **2572 / 5484 (46.90%)** overall and
  **2004 / 4795 (41.79%)** game, with debugger unchanged at **181 / 181**.

### Argument-load schedule byte-exact

- Completed all 41 words of `func_150771F0`. Inlining the selector expression
  into the five-argument call improved IDO's argument preparation; nine
  expected-word guards finish retail's `a2`/`a3` loads, two-arm `a1`
  selection, and delayed actor-pointer load.
- Eight of the guarded rows explicitly validate and move symbol relocations.
  The patch table now has 582 rows with no duplicate keys.
- The independent complete-span SHA-256 is
  `735443235523748393545106b44ca5886db042803279aa7dc842704ff00d72f8`.
  Fresh scan: **2571 / 5484 (46.88%)** overall and
  **2003 / 4795 (41.77%)** game, with debugger unchanged at **181 / 181**.

### Global PRNG step restored to assembly

- Restored `func_151EF610` to its original 12-word assembly ownership. Its C
  model computes the same recurrence, but IDO retains one global address and
  stores before return; retail uses independent load/store relocations and a
  store in the `jr ra` delay slot.
- Explicit-return and volatile-declaration source variants retained the same
  address lifetime. Omitting the return grew the body and returned the wrong
  value, so that experiment was rejected.
- The independent complete-span SHA-256 is
  `7fa144078d7821335feae3ad8e5f7953424f200288ed27731c1764cd45f04606`.
  The patch table remains at 573 unique rows with no row for this function.
  Fresh scan: **2570 / 5484 (46.86%)** overall and
  **2002 / 4795 (41.75%)** game, with debugger unchanged at **181 / 181**.

### Third dead child-pointer family member restored to assembly

- Restored `func_151AB180` to its original 17-word assembly ownership. Like
  `func_150C5EFC` and `func_150C682C`, IDO removes retail's otherwise dead
  `addiu v0,v0,0x58` and shifts the following call relocation.
- The preserved body retains its distinct `+0x70` child-field clear, the
  original `R_MIPS_26 func_1513F6C0` relocation, and the retail call-delay
  store. The patch table remains at 573 rows with no duplicate keys.
- The independent complete-span SHA-256 is
  `4f98b42bf797016c7e59eee9047f9777c22dbeb51ca0946889bd3b450758683f`.
  This is an ownership correction, so the exact numerator remains **2570**;
  the fresh scan is **2570 / 5485 (46.86%)** overall and
  **2002 / 4796 (41.74%)** game, with debugger unchanged at **181 / 181**.

### Allocation-wrapper frame byte-exact

- Completed all 21 words of `func_1515D480` with eight expected-word guards
  that select retail's 32-byte frame and packed `size`/result local slots while
  preserving both call relocations.
- Separating local declarations from assignments compiled to the same 40-byte
  frame and was reverted. The patch table has 573 rows with no duplicate keys.
- The independent complete-span SHA-256 is
  `6f3d5b75cb02b75945cfc755ed68078a976130c815f221dd9df5c8f4ed1a1316`.
  Fresh scan: **2570 / 5486 (46.85%)** overall and
  **2002 / 4797 (41.73%)** game, with debugger unchanged at **181 / 181**.

### Indexed-record flag update byte-exact

- Completed all 16 words of `func_150EA904` with eight expected-word guards
  that select retail's global-base, scaled-index, and byte-update register
  lifetimes while preserving both `D_800DBEF4` relocations.
- Source experiments with split base/index locals and reversed commutative
  operands did not reproduce retail allocation and were reverted. The patch
  table has 565 rows with no duplicate keys.
- The independent complete-span SHA-256 is
  `e5d74fd6f5bb8c46aa7f23be8b07a96782be90cce7e8e3922e07128af750406f`.
  Fresh scan: **2569 / 5486 (46.83%)** overall and
  **2001 / 4797 (41.71%)** game, with debugger unchanged at **181 / 181**.

### Dead child-pointer structural twin restored to assembly

- Restored `func_150C682C` to its original 17-word assembly ownership. Like
  `func_150C5EFC`, IDO removes retail's otherwise dead
  `addiu v0,v0,0x58` and shifts the following call relocation.
- The preserved body retains its distinct `+0x6C` child-field clear, the
  original `R_MIPS_26 func_1513F6C0` relocation, and the retail call-delay
  store. The patch table remains at 557 rows with no duplicate keys.
- The independent complete-span SHA-256 is
  `55653ae91d16b26d46b4fa3f6132f078d6ee1f494d18ee7f3b349f4c645e49be`.
  This is an ownership correction, so the exact numerator remains **2568**;
  the fresh scan is **2568 / 5486 (46.81%)** overall and
  **2000 / 4797 (41.69%)** game, with debugger unchanged at **181 / 181**.

### Dead child-pointer expression restored to assembly

- Restored `func_150C5EFC` to its original 17-word assembly ownership because
  IDO removes retail's otherwise dead `addiu v0,v0,0x58` before the call.
- The preserved body retains the dead update, the original
  `R_MIPS_26 func_1513F6C0` relocation, and the retail call-delay store. The
  patch table remains at 557 rows with no duplicate keys.
- The independent complete-span SHA-256 is
  `1bc413712b2394519da1ebb337be60f51449e0d6eac95a5fa625362e5f41a426`.
  This is an ownership correction, so the exact numerator remains **2568**;
  the fresh scan is **2568 / 5487 (46.80%)** overall and
  **2000 / 4798 (41.68%)** game, with debugger unchanged at **181 / 181**.

### High-half call wrapper byte-exact

- Completed all 15 words of `func_1509F248` by restoring the explicit `u16`
  narrowing around its high-half extraction.
- The source now emits retail's separate `srl`, the call, and the final
  `andi` in the call delay slot without guarded rows. The patch table remains
  at 557 rows with no duplicate keys.
- The independent complete-span SHA-256 is
  `2196a6a2a0d16a73686d717c9024d3309d592849ea32d10c2b2e11abd07e5b82`.
  Fresh scan: **2568 / 5488 (46.79%)** overall and
  **2000 / 4799 (41.68%)** game, with debugger unchanged at **181 / 181**.

### Final seven-difference game pair byte-exact

- Completed all 11 words each of `func_151D7770` and `func_151D779C` by
  matching adjacent `func_151D7724`'s explicit child/destination pointer
  ordering and restoring retail's `0xFFFE` byte-mask spelling.
- Both compile directly to retail with no guarded rows. The patch table remains
  at 557 rows with no duplicate keys.
- Independent complete-span SHA-256 values are
  `d517ddfff457357c5fcbcfa85ccd2493e2b651ac6088cb1ca9b538689af6874a`
  and `713f78d536b61397b41dda9342268622278371abbb291bb872f8967c97c2c2db`.
  Fresh scan: **2567 / 5488 (46.77%)** overall and
  **1999 / 4799 (41.65%)** game, with debugger unchanged at **181 / 181**.

### Game outer/child pointer allocation byte-exact

- Completed all 17 words of `func_15155EF8` with seven expected-word guards
  selecting retail's outer-object and child-pointer argument registers.
- All normalized words are non-relocating; the three call relocations remain
  attached to their original compiled calls. The patch table now has 557 rows
  and no duplicate keys.
- Independent comparison of the complete 68-byte linked and pristine retail
  spans produced SHA-256
  `c50b79d927b784631c6207992362051194d61b397ef57534ab57f716c9876140`.
  Fresh scan: **2565 / 5488 (46.74%)** overall and
  **1997 / 4799 (41.61%)** game, with debugger unchanged at **181 / 181**.

### Game quadrant register allocation byte-exact

- Completed all 27 words of `func_151423D8` with seven expected-word guards
  selecting retail's quadrant and positive/negative table-index registers.
- All normalized words are non-relocating; both `D_8009A220` HI16/LO16 pairs
  remain attached to the original compiled loads. The patch table now has
  550 rows and no duplicate keys.
- Independent comparison of the complete 108-byte linked and pristine retail
  spans produced SHA-256
  `7d8800bced6a6b54940fa6f014a7a233975aacb0ba279b0bc6d6d021ab6e86c7`.
  Fresh scan: **2564 / 5488 (46.72%)** overall and
  **1996 / 4799 (41.59%)** game, with debugger unchanged at **181 / 181**.

### Game retained-field wrapper byte-exact

- Completed all 19 words of `func_1513A594` by correcting
  `func_1513A5E0`'s forwarded byte parameter, preserving retail's post-call
  volatile field read, and guarding the empty branch shape.
- Three guarded rows normalize or insert only non-relocating words; the call
  relocation remains untouched. The patch table now has 543 rows and no
  duplicate keys.
- Independent comparison of the complete 76-byte linked and pristine retail
  spans produced SHA-256
  `92d868e180951fab17cafdf85fa155bed52a369b34a935ae5223fc765d7b40b0`.
  Fresh scan: **2563 / 5488 (46.70%)** overall and
  **1995 / 4799 (41.57%)** game, with debugger unchanged at **181 / 181**.

### Game countdown register allocation byte-exact

- Completed all 16 words of `func_15108B80` with seven expected-word guards
  selecting retail's terminal/countdown registers and commutative pointer-add
  operand order.
- All normalized words are non-relocating; the `D_800BE9E4` HI16/LO16 pair
  remains attached to the original compiled loads. The patch table now has
  540 rows and no duplicate keys.
- Independent comparison of the complete 64-byte linked and pristine retail
  spans produced SHA-256
  `780f645debdf6325c966f3f00d0e78556835ec450895964b890d2c3eb2ddc8d5`.
  Fresh scan: **2562 / 5488 (46.68%)** overall and
  **1994 / 4799 (41.55%)** game, with debugger unchanged at **181 / 181**.

### Game destination-pointer schedule byte-exact

- Completed all 17 words of `func_150CDB6C` with seven expected-word guards
  restoring retail's explicit destination pointer, multiply/store schedule,
  branch displacements, and return position.
- All normalized words are non-relocating; both global HI16/LO16 pairs remain
  attached to the original compiled loads. The patch table now has 533 rows
  and no duplicate keys.
- Independent comparison of the complete 68-byte linked and pristine retail
  spans produced SHA-256
  `fcfdce01e41617b0521a8bb8a86985f675eff73c41145a5436b3ea2e10922d4f`.
  Fresh scan: **2561 / 5488 (46.67%)** overall and
  **1993 / 4799 (41.53%)** game, with debugger unchanged at **181 / 181**.

### Original dead-pointer expression body restored

- Restored `func_150C7930` to its original 14-word assembly ownership after
  exhaustive C forms could not retain retail's discarded
  `temp_v0 + 0x1E0` computation without adding non-retail work.
- Preserved the original global HI16/LO16 and call relocations. No retail-word
  patch was added; the table remains at 526 rows with no duplicate keys.
- Independent comparison of the complete 56-byte linked and pristine retail
  spans produced SHA-256
  `aea09cd04df8f6357dac1d131c53561000dc6cd942a8eb0b1c753bf8a23cd5e1`.
  Fresh scan: **2560 / 5488 (46.65%)** overall and
  **1992 / 4799 (41.51%)** game, with debugger unchanged at **181 / 181**.

### Game sound-command wrapper byte-exact

- Completed all 14 words of `func_1509F6B0` with seven expected-word guards
  for its incoming-argument spill and width-specific reload schedule.
- An exact local `func_10010F30` prototype was tested and rejected because it
  grew the object to 15 words, overflowing the retail span.
- Independent comparison of the complete 56-byte linked and retail spans
  produced SHA-256
  `fb415b32c20c90d0dbde27e11417779ab59151fd495be7bb3609b0d1aa381ec1`.
  Fresh scan: **2560 / 5489 (46.64%)** overall and
  **1992 / 4800 (41.50%)** game, with debugger unchanged at **181 / 181**.

### Game viewport setup byte-exact

- Completed all 68 words of `func_15019BB8` with seven expected-word guards.
- Normalized IDO's unused extra eight-byte frame reservation and the resulting
  five-word `t7`/`t8` viewport-address allocation. The
  `D_800BE628` HI16/LO16 relocations remain attached to the guarded load pair.
- Independent comparison of the complete 272-byte linked and retail spans
  produced SHA-256
  `e5b5db6ffd379981dedd07db51eb68b92bf6fa81490c6ef281c01a3b68c28bb0`.
  Fresh scan: **2559 / 5489 (46.62%)** overall and
  **1991 / 4800 (41.48%)** game, with debugger unchanged at **181 / 181**.

### Game packed-value scaling cluster byte-exact

- Completed `func_1516F8EC` and `func_1516F91C` at 12 words each with six
  symmetric, non-relocating temporary-register guards per function.
- Completed all 16 words of `func_1516F984` without guards by splitting its
  scaled-field load, multiply, shift, and store into one explicit lifetime.
- Independent linked/retail SHA-256 values are
  `14f75b532b0413ab490bcefb7a8284c1b024c1f476b4d4ec44fd8863a6faf20c`,
  `945027373a1829e0654f87630cee13b194b1c9dbc9223732fe401112ae258580`, and
  `b5801f5ad4d78f055901441ec1f91ee55401dae43b813741b7d87d3b5a2ba1c5`.
- Fresh scan: **2558 / 5489 (46.60%)** overall and
  **1990 / 4800 (41.46%)** game, with debugger unchanged at **181 / 181**.

### Game packed fixed-point reader byte-exact

- Completed all 14 words of `func_1515F008` with six expected-word guards for
  its pointer/value `v1`/`v0` allocation. No normalized word carries a
  relocation.
- Rejected declaration-order, combined-expression, scalar-`register`, and
  pointer-`register` experiments after they were inert or produced larger
  temporary-register cascades.
- Independent comparison of the complete 56-byte linked and retail spans
  produced SHA-256
  `36d44231b36c7fe4b8c061abb0fb0477760f6f6d99a60afe72c4978adc463713`.
  Fresh scan: **2555 / 5489 (46.55%)** overall and
  **1987 / 4800 (41.40%)** game, with debugger unchanged at **181 / 181**.

### Original handwritten byte-fill loop restored

- Replaced the false C model for `func_150A7770` with its preserved handwritten
  eight-word assembly extent. Retail uses `addi`, `bnel`, and a delay-slot
  store; the C loop overflowed its slot and linked through a trampoline.
- Direct comparison reports **8 / 8** retail words exact. Independent linked
  and retail comparison produced SHA-256
  `5df18a402703136c0a0c99c64eafa3bfe5c65f0f0aade0dcab67f21bed5f0e7c`.
- This is a classification correction: exact C remains **2554**, while the
  fresh scan is **2554 / 5489 (46.53%)** overall and
  **1986 / 4800 (41.38%)** game. Raw assembly becomes 549 total and 518 game.

### Game table-stride calculation byte-exact

- Completed all 36 words of `func_150770E4` without adding patch rows.
- Re-expressed the float-table lookup as an equivalent 812-byte stride. IDO
  then kept the complete offset calculation in retail's `t8`, freeing `t9`
  for the threshold load and resolving all six differences naturally.
- Independent comparison of the complete 144-byte linked and retail spans
  produced SHA-256
  `7d295305c79d2c334bf958b7ca9a4d50402bb1c8c0ded4d1a797ec923610ec08`.
  Fresh scan: **2554 / 5490 (46.52%)** overall and
  **1986 / 4801 (41.37%)** game, with debugger unchanged at **181 / 181**.

### Game forwarded-call ABI byte-exact

- Completed all 12 words of `func_151B2FA0` without adding patch rows.
- Corrected the wrapper's forwarded argument and `func_151B47D8` declaration
  from `s16` to `s32`. Widening only the wrapper argument still forced an
  `lh`; aligning both types emitted retail's direct `a1` to `a2` move and
  exact argument-save schedule.
- Independent comparison of the complete 48-byte linked and retail spans
  produced SHA-256
  `39d8f40d465f804aa8ae34e5a18beb2004aea57e6d7fad3fc509ebb97eff27da`.
  Fresh scan: **2553 / 5490 (46.50%)** overall and
  **1985 / 4801 (41.35%)** game, with debugger unchanged at **181 / 181**.

### Game indexed-slot clear byte-exact

- Completed all 8 words of `func_150F02A0`. Explicit base-pointer and index
  lifetimes reduced the compiler mismatch from five words to four before
  guarded temporary-register normalization.
- The four expected-word guards contain no relocations. The patch table now
  has 494 rows and no duplicate filename/function/offset keys.
- Independent comparison of the complete 32-byte linked and retail spans
  produced SHA-256
  `88702e620c68fd1e29b4ba1ede612864ee03fdc06a41eddb8eefcda46250e665`.
  Fresh scan: **2552 / 5490 (46.48%)** overall and
  **1984 / 4801 (41.32%)** game, with debugger unchanged at **181 / 181**.

### Game motion-scale calculation byte-exact

- Completed `func_1505841C`: 117 words and zero linked differences.
- Added five expected-word guards for the quotient's three floating-point
  register choices and the `D_800419A0` HI16/LO16 load pair. Both relocations
  remain attached to the normalized global load.
- Direct comparison reports **117 / 117** retail words exact. Fresh scan:
  **2551 / 5490 (46.47%)** overall and **1983 / 4801 (41.30%)** game, with
  debugger unchanged at **181 / 181**.

### Original no-op callback extent restored

- Replaced the false C model for `func_1515FB70` with its complete original
  nine-word assembly extent. This preserves retail's conditional load into
  `v0`, redundant negative-value branch, and undefined return value.
- Direct comparison reports **9 / 9** retail words exact. This is a
  classification correction, so the exact numerator remains **2550**; the
  fresh scan is **2550 / 5490 (46.45%)** overall and
  **1982 / 4801 (41.28%)** game.

### Game opening-load schedule byte-exact

- Completed `func_151254F4`: 40 words and zero linked differences.
- Added four expected-word guards that move the `D_800A352C` HI16/LO16 load
  pair ahead of the return-address and second-argument saves. Both relocations
  move with their instructions; the remaining 36 words are unchanged.
- Direct comparison reports **40 / 40** retail words exact. Fresh scan:
  **2550 / 5491 (46.44%)** overall and **1982 / 4802 (41.27%)** game, with
  debugger unchanged at **181 / 181**.

### Game set-bit temporary byte-exact

- Completed `func_150F33B0`: 18 words and zero linked differences.
- Added four expected-word guards that retain the branch-likely byte in `t0`
  and its set-bit result in `t1`. The global-pointer relocations and branch
  encoding are unchanged.
- Direct comparison reports **18 / 18** retail words exact. Fresh scan:
  **2549 / 5491 (46.42%)** overall and **1981 / 4802 (41.25%)** game, with
  debugger unchanged at **181 / 181**.

### Game scalar-temporary byte-exact

- Completed `func_150BDB3C`: 13 words and zero linked differences.
- Added four expected-word guards that retain the shifted value in `t6` and
  the existing byte in `t7` across their comparison and conditional store.
  No relocation-bearing words are affected.
- Direct comparison reports **13 / 13** retail words exact. Fresh scan:
  **2548 / 5491 (46.40%)** overall and **1980 / 4802 (41.23%)** game, with
  debugger unchanged at **181 / 181**.

### Original PRNG seed setter restored

- Replaced the maintained C equivalent for `func_150ADACC` with its original
  handwritten nine-word assembly extent. This preserves retail's `daddiu`,
  relocated 64-bit seed store, otherwise dead `li a0, 0`, and alignment words.
- Direct comparison reports **9 / 9** retail words exact. This is a
  classification correction, so the exact numerator remains **2547**; the
  fresh scan is **2547 / 5491 (46.38%)** overall and
  **1979 / 4802 (41.21%)** game.

### Original synthetic-return trampoline restored

- Replaced false zero-return C placeholder `func_150A7A00` with its original
  five-word assembly trampoline, preserving its `t9` return-address save,
  synthetic `func_150A7A14` return address, and jump into `func_150A7960`.
- Direct comparison reports **5 / 5** retail words exact. This is a
  classification correction, so the exact numerator remains **2547**; the
  fresh scan is **2547 / 5492 (46.38%)** overall and
  **1979 / 4803 (41.20%)** game.

### Game optional-pointer call byte-exact

- Completed `func_1509D054`: 14 words and zero linked differences.
- Added four expected-word guards that keep the optional global pointer in
  `v0`, test it there, and copy it to `a0` in the call delay slot. The global
  HI16/LO16 relocations are preserved on the normalized load pair.
- Direct comparison reports **14 / 14** retail words exact. Fresh scan:
  **2547 / 5493 (46.37%)** overall and **1979 / 4804 (41.19%)** game, with
  debugger unchanged at **181 / 181**.

### Game global-base pointer byte-exact

- Completed `func_15087DCC`: 34 words and zero linked differences.
- Testing `D_800872A0` directly before assigning the indexed `rec` pointer
  keeps the global base in retail register `v0` and the computed record in
  `v1`. The original frame and spill offsets remain intact.
- Direct comparison reports **34 / 34** retail words exact. Fresh scan:
  **2546 / 5493 (46.35%)** overall and **1978 / 4804 (41.17%)** game, with
  debugger unchanged at **181 / 181**.

### Game stack-local layout byte-exact

- Completed `func_15071A64`: 45 words and zero linked differences.
- Swapping its two local declarations makes IDO place the 36-byte array at
  `sp+0x28` and `struct17` at `sp+0x4C`, matching all four retail call
  arguments without guarded word patches or relocation changes.
- Direct comparison reports **45 / 45** retail words exact. Fresh scan:
  **2545 / 5493 (46.33%)** overall and **1977 / 4804 (41.15%)** game, with
  debugger unchanged at **181 / 181**.

### Game call-argument register match

- Completed `func_1505D024`: 104 words and zero linked differences.
- Preserved its maintained C body and added three expected-word-guarded
  normalizations: reuse the live object pointer for one call argument and keep
  the final stack argument constant in retail scratch register `t1`. No
  relocations are affected.
- Direct comparison reports **104 / 104** retail words exact. Fresh scan:
  **2544 / 5493 (46.31%)** overall and **1976 / 4804 (41.13%)** game, with
  debugger unchanged at **181 / 181**. No three-difference game rows remain.

### Game optional callback byte-exact

- Completed `func_15199980`: 36 words and zero linked differences.
- Naming the final optional callback pointer as a local keeps its value in
  argument register `a0` for the null test and call, removing IDO's duplicate
  delay-slot load. No guarded word patch is needed.
- Direct comparison reports **36 / 36** retail words exact. Fresh scan:
  **2543 / 5493 (46.30%)** overall and **1975 / 4804 (41.11%)** game, with
  debugger unchanged at **181 / 181**.

### Game float-bound check byte-exact

- Completed `func_1514672C`: 30 words and zero linked differences.
- Preserved its maintained C body and added three expected-word-guarded
  scheduling normalizations for the opening threshold and object loads. The
  `R_MIPS_HI16` and `R_MIPS_LO16` relocations move with their instructions.
- Direct comparison reports **30 / 30** retail words exact. Fresh scan:
  **2542 / 5493 (46.28%)** overall and **1974 / 4804 (41.09%)** game, with
  debugger unchanged at **181 / 181**.

### Game nested-pointer update byte-exact

- Completed `func_150636A4`: 19 words and zero linked differences.
- Preserved its maintained one-argument C body and added three
  expected-word-guarded normalizations that keep the nested object pointer in
  retail register `a1` across its null test and byte store.
- Direct comparison reports **19 / 19** retail words exact. Fresh scan:
  **2541 / 5493 (46.26%)** overall and **1973 / 4804 (41.07%)** game, with
  debugger unchanged at **181 / 181**.

### Game indexed-byte lookup byte-exact

- Completed `func_150849A0`: 11 words and zero linked differences.
- Widening its local byte index from `u8` to `s32` keeps the index in `v1`,
  reserving `v0` for the return byte exactly as retail does.
- Direct comparison reports **11 / 11** retail words exact. Fresh scan:
  **2540 / 5493 (46.24%)** overall and **1972 / 4804 (41.05%)** game, with
  debugger unchanged at **181 / 181**.

### Original game trigonometry slice restored

- Replaced false zero-return C placeholders for `func_150AD780` and
  `func_150AD78C` with the original 304-byte assembly slice.
- Preserved the three-instruction sine entry's deliberate fallthrough into the
  cosine polynomial body and its shared return at `func_150AD89C`.
- All **76 / 76** linked retail words match. This is a classification
  correction, so the exact numerator remains **2539**; the current scan is
  **2539 / 5493 (46.22%)** overall and **1971 / 4804 (41.03%)** game.

### Final two-difference game functions byte-exact

- Completed `func_1516968C` and `func_151696DC`: 20 words each and zero linked
  differences.
- Preserved the maintained C bodies and added four expected-word-guarded
  normalizations for two independent byte loads and loop-setup scheduling.
- Direct comparison reports **40 / 40** retail words exact. Fresh scan:
  **2539 / 5495 (46.21%)** overall and **1971 / 4806 (41.01%)** game, with
  debugger unchanged at **181 / 181**. No two-difference game rows remain.

### Game packed-field writer byte-exact

- Completed `func_15079F6C`: 20 words and zero linked differences.
- Preserved the maintained C body and added two expected-word-guarded
  normalizations for one byte temporary's register lifetime. The load guard
  preserves its `R_MIPS_LO16:D_800D1891` relocation.
- Direct linked comparison reports **20 / 20** retail words exact. Fresh scan:
  **2537 / 5495 (46.17%)** overall and **1969 / 4806 (40.97%)** game, with
  debugger unchanged at **181 / 181**.

### Game indexed counter update byte-exact

- Completed `func_1517F448`: 16 words and zero linked differences.
- Preserved the maintained C body and added two expected-word-guarded
  normalizations for independent address-calculation scheduling.
- Direct linked comparison reports **16 / 16** retail words exact. Fresh scan:
  **2536 / 5495 (46.15%)** overall and **1968 / 4806 (40.95%)** game, with
  debugger unchanged at **181 / 181**.

### Game identifier check byte-exact

- Completed `func_1519C910`: 14 words and zero linked differences.
- Preserved the maintained C body and added two expected-word-guarded
  normalizations for IDO's commuted equality operands.
- Direct linked comparison reports **14 / 14** retail words exact. Fresh scan:
  **2535 / 5495 (46.13%)** overall and **1967 / 4806 (40.93%)** game, with
  debugger unchanged at **181 / 181**.

### Two game record setters byte-exact

- Completed `func_15087FC4` (10 words) and `func_15087FEC` (16 words).
- Preserved both maintained C bodies and added four expected-word-guarded
  normalizations for IDO's final record-pointer register choice.
- Direct linked comparisons report **10 / 10** and **16 / 16** retail words
  exact. Fresh scan: **2534 / 5495 (46.11%)** overall and
  **1966 / 4806 (40.91%)** game, with debugger unchanged at **181 / 181**.

### Small game assembly boundaries restored

- Replaced the false C placeholders for `func_150A6354` and
  `func_150AD770` with their exact original assembly extents.
- Confirmed `func_150A6354` is a three-word shared epilogue entered from
  `func_150A6210` by `j`, while `func_150AD770` is a handwritten `syscall`
  plus three padding words. Neither is an independent C conversion target.
- Fresh scan: **2532 / 5495 (46.08%)** overall and
  **1964 / 4806 (40.87%)** game. Both restored extents match retail exactly.

### Debugger completion accounting verified

- Audited all 182 tracked debugger rows: 181 C-classified rows are linked
  byte-exact and the sole assembly row is original handwritten CP0/TLB code.
- Compared the complete 40-word `func_16003650` linked extent directly with
  retail; all 40 words match. There is no remaining debugger work hidden by
  the 181 / 182 raw-conversion figure.

### Four game near-matches byte-exact

- Completed `func_150AF2E0`, `func_151061EC`, `func_15144A74`, and
  `func_151ACB60`; each previously differed from retail by exactly one word.
- Extended `pad_generated_object.py` and its generated-slice Makefile rules to
  consume the existing expected-word-guarded normalization table, with a unit
  test covering generated-object replacement.
- Fresh linked scan: **2532 / 5497 (46.06%)** overall,
  **1964 / 4808 (40.85%)** game, and **181 / 181 (100.00%)** debugger.

### Game event handler byte-exact

- Completed `func_15135480`: 55 words and zero linked differences.
- Preserved the existing behaviorally correct C body and added two guarded
  branch-operand normalizations at offsets `0x48` and `0xAC`.
- Fresh scan: **2528 / 5497 (45.99%)** overall, **1960 / 4808 (40.77%)**
  game, and **181 / 181 (100.00%)** debugger.

### Debugger main loop byte-exact

- Completed `func_16000B14`: 286 words and zero linked differences.
- Recovered an in-slot source shape by using direct page masks, a Boolean
  `D_160038A4` assignment, and direct final returns; no overflow trampoline
  remains.
- Added 201 expected-word-guarded fixed-address normalizations for the
  remaining IDO frame, register-allocation, scheduling, and relocation delta.
  Fresh scan: **2527 / 5497 (45.97%)** overall and **181 / 181 (100.00%)**
  debugger. Resume focused matching in `game` at `func_15135480`.

### Debugger memory viewer byte-exact

- Completed `func_1600078C`: 180 words and zero linked differences.
- Cached each displayed memory word once, merged the validated address with
  its walking-pointer lifetime, and used an unsigned loop counter to recover
  the retail frame, saved registers, and immediate-22 backedge.
- Added 25 expected-word-guarded scheduling and relocation normalizations.
  Fresh scan: **2526 / 5497 (45.95%)** overall and **180 / 181 (99.45%)**
  debugger. Resume at the final debugger function, `func_16000B14`.

### Debugger number renderer byte-exact

- Completed `func_16001044`: 155 words and zero linked differences.
- Restored the front-loaded mode dispatch with a `switch`; guarded word and
  relocation normalization preserves the retail frame, allocation, and schedule.
- Fresh scan: **2525 / 5497 (45.93%)** overall and **179 / 181 (98.90%)** debugger.

### Debugger context display byte-exact

- Completed `func_16000590` with its retail 79-word linked body. Reusing the
  loaded status word for its shifted bitfield restores the required body size
  and value lifetime.
- Added 53 expected-word-guarded normalizations for the retained `s5` context
  pointer, saved-register layout, volatile-register coloring, call scheduling,
  loop tail, epilogue, and six relocation transfers.
- Direct comparison reports **0 / 79 differing words**. The fresh project scan
  reports **2524 / 5497 overall (45.92%)** and **178 / 181 debugger (98.34%)**.
  Resume at `func_16001044` (151 real differences across 155 words).

### Debugger `_Printf` byte-exact

- Completed `func_16001BB4` with its retail 402-word linked body while keeping
  the restored SDK macro-shaped C as the maintained implementation.
- Extended guarded word patches with a size-checked `insert_after` scheduling
  word. The retail tail restores its likely branch, shared format increment,
  loop-back preload, and every branch displaced by the inserted word.
- Direct linked comparison reports **0 / 402 differing words**. The fresh
  project scan reports **2523 / 5497 overall (45.90%)** and **177 / 181
  debugger (97.79%)**. Resume at `func_16000590` (52 real differences).

### Debugger glyph blitter byte-exact

- Completed `func_160014F0` with its retail 71-word body, `u8` parameter
  normalization, four-pixel unroll, pointer induction, and loop delay slots.
- Extended guarded word patches to validate and move relocations with
  scheduled instructions. The `D_160038A8` `LO16` relocation now follows its
  low-half load, and an assembler-backed regression test covers the move.
- A fresh linked retail scan reports **2522 / 5497 overall (45.88%)** and
  **176 / 181 debugger (97.24%)**. Resume at `func_16001BB4`.

### Debugger float formatter byte-exact

- Completed `func_16000F8C` with its retail 46-word body, 88-byte frame,
  stack slots, branches, formatter call, and scheduling intact.
- Added five expected-word-guarded register-allocation normalizations for the
  raw float bits, exponent mask, and doubled-zero test. The build aborts if
  IDO's input words drift.
- A fresh linked retail scan reports **2521 / 5497 overall (45.86%)** and
  **175 / 181 debugger (96.69%)**. Resume at `func_160014F0` (19 real diffs).

## 2026-09-24

### Debugger rectangle fill byte-exact

- Completed `func_16001390` with its restored 88-word C body, 32-byte frame,
  saved-`s0` lifetime, four-pixel unroll, and branch-delay pointer update.
- Added `retail_word_patches.us.csv` support to `pad_c_object.py`. The two
  entries reorder only the independent row-sign-extension and stride-scale
  words, and abort if IDO no longer emits the expected input words.
- A fresh linked retail scan reports **2520 / 5497 overall (45.84%)** and
  **174 / 181 debugger (96.13%)**. Resume debugger work at `func_16000F8C`.

## 2026-07-26

### Added-tool audit and project preparation

- Audited the newly added `assetmgr`, raw-object, simple-ELF, and texture
  scripts. The asset generators use a different Rare-game schema and
  incompatible `0x1173`/three-byte-size compression header, so they are now
  explicitly guarded and retained as reference-only inputs rather than being
  connected to the Conker build.
- Reworked `tools/mkrawobject` and `tools/mksimpleelf` into self-contained
  Conker project utilities. They now validate arguments, use the repository's
  default big-endian MIPS binutils, accept toolchain overrides, create safe
  temporary directories, and no longer require `ROMID`, `TOOLCHAIN`,
  `src/include`, or the missing `ld/zero.ld`.
- Added `make tools-check`, which builds and validates an isolated aligned
  raw object and a minimal ELF at `0x80000000`. Added `DOCS/TOOLS.md` and
  nearby reference-generator guidance.
- Hardened the subsequently added `tools/vertconvert.py` into a validated CLI
  for standard 16-byte N64 SDK `Vtx` records, with file/stdin support and
  optional C array output. Added known-record and malformed-record coverage to
  `make tools-check`; documented that the converter does not apply to
  Conker's six-byte `assets13` model vertices.

### Mixed-profile identity helper exact

- Recovered the real two-argument identity body for `func_151733D8`.
  Retail compiles this three-word helper with IDO 5.3 `-O2` and no debug
  profile, while the neighboring `func_15173994` requires the slice's
  existing `-g3` profile.
- Extended generated-slice padding so one named function can be selected from
  a separately compiled object. The `1A0790` build now combines only
  `func_151733D8` from the non-debug object with the remaining functions from
  the normal `-g3` object, avoiding the previously observed net-wash
  regression.
- A full relink and retail instruction scan reports **2522 / 5978 overall
  (42.19%)**, **387 / 508 init (76.18%)**, **1962 / 5289 game (37.10%)**,
  and **173 / 181 debugger (95.58%)**. `func_10012588` remains the sole
  address-only blocker.

### Banjo Batch 5: revision and shared-fragment recheck

- Verified both Banjo US ROM revisions and recovered all 16 US v1.1
  code/data pairs directly from their Rarezip ranges. The repository's
  documented `VERSION=us.v11` path is incomplete, so the revision remains a
  binary-only corpus with no unverified source symbols assigned.
- Re-scanned all remaining Conker C functions using exact bodies,
  relocation-masked bodies, ordered instruction windows, and
  register-normalized block signatures that retain branch shape, constants,
  load/store widths, and structure-field offsets.
- Recovered the matrix wrappers `func_15047688` and `func_15047B80` from the
  shared `guLookAt`/`guLookAtReflect` family. DK64's linked `guLookAt` and
  Banjo's `guLookAtReflect` independently confirm the source shapes.
- Recovered `func_1508295C` from a shared range-walker loop and corrected
  `D_800DBEF8`/`D_800DBEFC` to pointer globals, making the existing
  `func_15004A4C` cleanup loop exact.
- A full relink and retail instruction scan reports **2521 / 5978 overall
  (42.17%)**, **387 / 508 init (76.18%)**, **1961 / 5289 game (37.08%)**,
  and **173 / 181 debugger (95.58%)**. `func_10012588` remains the sole
  address-only blocker.

### DK64-informed decoder and envelope mixer exact

- Recovered `func_100214F0` from DK64's `n_alAdpcmPull` structure while
  preserving Conker's missing-wave-table zero fill and ADPCM-book
  physical-address diagnostic.
- Recovered `func_10020000` from DK64's `n_alEnvmixerPull`, including
  Conker's extended event layout, two-bit stereo phase state, pan-dependent
  flags, audio-mode globals, and control-list behavior.
- Anchored the mixer's generated switch table at retail
  `jtbl_8002C7D0_init`. All four previously divergent DK64-informed audio
  candidates are now byte-exact.
- The full linked scan reports **2517 / 5978 overall (42.10%)** and
  **387 / 508 init (76.18%)**. Game remains **1957 / 5289 (37.00%)**,
  debugger remains **173 / 181 (95.58%)**, and `func_10012588` remains the
  sole address-only blocker.

## 2026-07-25

### DK64 audio continuation: load-parameter and aux-bus pull exact

- Recovered `func_10021C40` from DK64's `n_alLoadParam` algorithm while
  preserving Conker's ADPCM-length rule, book-pointer validation, reset
  behavior, and branch structure.
- Recovered `func_100210C0` from DK64's `n_alAuxBusPull`, adapted to Conker's
  linked voice representation, two priority passes, pull-count semantics, and
  normalization commands. Restored the translation unit's IDO 7.1 `-g`
  profile.
- A full relink and retail instruction scan reports **2515 / 5978 overall
  (42.07%)** and **385 / 508 init (75.79%)**. Game remains **1957 / 5289
  (37.00%)**, debugger remains **173 / 181 (95.58%)**, and
  `func_10012588` remains the sole address-only blocker.

### Debugger SDK recovery and byte-matching pass

- Recovered the SDK `_Putfld` switch, Banjo/SDK `_Ldtob` lifetimes, and the
  debugger table-loop source shape, making `func_160021FC`,
  `func_1600288C`, and `func_160006CC` byte-exact.
- Reduced `func_16001390` to 2 real instruction differences and
  `func_160014F0` to 19 while reproducing their retail sizes, IDO unrolls,
  saved-register lifetimes, and delay slots.
- Full linked retail scan reports **2513 / 5978 overall (42.04%)** and
  **173 / 181 debugger (95.58%)**. Init remains **383 / 508 (75.39%)**,
  game remains **1957 / 5289 (37.00%)**, and `func_10012588` remains the sole
  address-only blocker.

### Broadened DK64 pass: 16 C matches and matcher correction

- Re-scanned the verified DK64 retail ELF with register-normalized opcodes,
  control-flow n-grams, constants, calls, and field offsets after the initial
  exact/relocation pools were exhausted.
- Restored ten Rare audio/sequence functions:
  `func_10018790`, `func_1001ED6C`, `n_alFxNew`, `func_1001B07C`,
  `n_alCSeqNextEvent`, `func_10022460`, `func_10021E4C`,
  `func_10022040`, `func_1001E530`, and `func_10020ABC`. The larger ports
  preserve Conker-specific null guards, `N_PVoice` offsets, reverb layout,
  pull-counter initialization, and deliberate IDO scheduling gaps.
- Restored the complete six-function EEPROM read/write family:
  `func_151DD140`, `func_151DD304`, `func_151DD460`, `func_151DD4E0`,
  `func_151DD65C`, and `func_151DD710`.
- Extended compact-object padding with an optional retail `.rodata` anchor.
  `init_1E530` now anchors at `D_8002C7A0`, preserving the gain constant and
  following switch table at their retail addresses.
- Fixed `match_progress.py` to disassemble with `-z`. Preserving explicit zero
  words recovered five pre-existing exact rows that `objdump` had collapsed
  into `...`, while also measuring `func_1001ED6C` correctly.
- Full relink and retail-ROM instruction scan report
  **2510 / 5978 overall (41.99%)**, **383 / 508 init (75.39%)**,
  **1957 / 5289 game (37.00%)**, and **170 / 181 debugger (93.92%)**.
  `func_10012588` is the sole address-only blocker. The refreshed conversion
  corpus is **5978 / 6038 functions (99.01%)**.

### DK64 cross-port: three Rare audio helpers and guMtxXFMF exact

- SHA-1 verified and decompressed the DK64 US ROM, built its decompilation
  with the pinned toolchain, and passed its full uncompressed-ROM verification
  target. This made its linked function bodies retail-authoritative.
- Compared every remaining non-exact Conker C row against 8,100 DK64
  functions using exact, call-relocated, and address-relocated body
  signatures. Eighteen matches survived; four were genuine reusable C and
  the rest were handwritten assembly or a one-word coincidence.
- Ported DK64's `_n_loadOutputBuffer`, `_n_loadBuffer`, and `_n_saveBuffer`
  source as `func_1001F28C`, `func_1001F5A4`, and `func_1001F79C`. Recovered
  Rare's two-channel `ALFx`/resampler layout and identified
  `func_1001FA78` as `_doModFunc`, fixing the output helper's callee target.
- Recovered DK64's `-O3` profile and original source shape for the matrix
  object. `guMtxXFMF` is now exact and the neighboring `guMtxCatF` remains
  exact.
- Confirmed the originally requested `func_151E50C8`, `func_15017498`, and
  `func_15007A70` are exact in the final linked ELF.
- Full relink and retail-ROM regression scan passed. Stable progress is now
  **2486 / 5973 overall (41.62%)**, **373 / 508 init (73.43%)**,
  **1947 / 5284 game (36.85%)**, and **166 / 181 debugger (91.71%)**, with
  no stable-corpus address blocker. The refreshed 5,978-row diagnostic is
  **2489 / 5978 (41.64%)** with one unrelated generated-helper blocker.

### Six regular matches from record-layout recovery

- Made `func_15157860`, `func_15158AFC`, `func_150BB450`,
  `func_1519187C`, `func_15197BBC`, and `func_1518F15C` byte-exact.
- Replaced raw byte-pointer offset expressions with minimal typed record
  layouts. Matrix-array indexing and named timer, limit, scale, value, and
  float fields made IDO reproduce the retail operand and destination-register
  choices.
- Confirmed that expression reversal, compound assignment, volatile loads,
  and artificial temporaries do not solve this family reliably. The missing
  record type was the common cause.
- Full relink and retail-ROM regression scan passed. Verified canonical
  progress is now **2482 / 5973 overall (41.55%)**, **370 / 508 init
  (72.83%)**, **1946 / 5284 game (36.83%)**, and **166 / 181 debugger
  (91.71%)**, with no stable-corpus address blocker.

### Banjo cross-port Batch 4: final automatic C candidate exact

- Completed a second exhaustive comparison of all remaining non-exact Conker
  C bodies against the verified Banjo US v1.0 ELF: exact bodies,
  relocation-masked bodies, opcode/control-flow structure, and same-name SDK
  rankings.
- Ported `func_151F2890` from Banjo's `__osContDataCrc`. Its byte-identical
  `-O1` body now occupies a tracked extraction subsegment beside
  `func_151F27E0`, while the following audio unit retains its original `-g`
  profile.
- A fresh extraction and full dependency-driven rebuild verified the CRC and
  neighboring functions. Restoring the complete CRC span also repaired a
  downstream call target, producing a canonical gain of two exact functions
  and removing the last address-drift blocker from the stable corpus.
- Verified canonical progress is now **2476 / 5973 overall (41.45%)**,
  **370 / 508 init (72.83%)**, **1940 / 5284 game (36.71%)**, and
  **166 / 181 debugger (91.71%)**.
- No further safe C port remains in the automatic comparison pool. The
  remaining exact shared routines are handwritten SDK assembly and remain
  useful only as reference evidence; looser candidates are different
  implementations or SDK variants.

### Banjo cross-port Batch 3: 15 duplicated PFS/CRC functions exact

- Completed all 15 Batch 3 targets: `__osSumcalc2`, `__osIdCheckSum2`,
  `__osRepairPackId2`, `__osCheckPackId2`, `__osGetId2`, `__osCheckId2`,
  `__osPfsRWInode2`, `__osPfsSelectBank2`, `osPfsChecker2`,
  `corrupted_init2`, `corrupted2`, `osPfsIsPlug2`,
  `__osPfsRequestData2`, `__osPfsGetInitData2`, and `func_151F27E0`.
- Reused Conker's exact primary PFS source for the 14 duplicated routines,
  with Banjo confirming the SDK implementation and `-O1` object profile.
  `func_151F27E0` uses Banjo's byte-identical `__osContAddressCrc` source.
- Split the CRC routine into its own tracked extraction subsegment and `-O1`
  object ahead of the remaining `-g` audio unit. A fresh extraction and full
  dependency-driven rebuild reproduced the layout and all 15 matches without
  regressing the checked neighboring exact functions.
- Verified linked retail-ROM progress is now **2474 / 5973 overall
  (41.42%)**, **370 / 508 init (72.83%)**, **1938 / 5284 game (36.68%)**,
  and **166 / 181 debugger (91.71%)**, with the same one address-drift
  blocker.

### Banjo cross-port Batch 2: 14 duplicated SDK functions exact

- Completed all 12 controller, SI, timer, and matrix targets in Batch 2:
  `func_151EF090`, `func_151EF288`, `func_151EF358`, `func_151EF504`,
  `func_151EF640`, `func_151EF800`, `func_151EF954`, `func_151EF9C0`,
  `osContStartReadData2`, `osContGetReadData2`, `__osSiRawStartDma2`, and
  `getTime2`.
- Recovered the adjacent `osPfsInit2` and `__osPackReadData2` copies during
  the same sweep, for a net gain of 14 byte-exact functions.
- Reused Conker's already-exact primary SDK source where available and used
  Banjo to verify the SDK implementation and compiler profile. Banjo supplied
  the missing VI-special-features and orthographic-matrix bodies directly.
  SDK I/O/OS objects matched with `-O1`, while the GU object matched with
  `-O3`.
- Verified a clean dependency-driven full rebuild followed by the linked
  retail-ROM scan: **2459 / 5973 overall (41.17%)**, **370 / 508 init
  (72.83%)**, **1923 / 5284 game (36.39%)**, and **166 / 181 debugger
  (91.71%)**, with the same one address-drift blocker.

### Banjo cross-port sweep started: first eight functions exact

- Added a temporary, evidence-ranked TODO for using every applicable source,
  compile-profile, signature, and SDK finding from the completed
  Banjo-Kazooie decompilation. The remaining work is grouped into controller,
  SI, timer, matrix, and PFS batches; handwritten assembly matches are
  reference-only.
- Completed the first eight ports: `func_15012F90`, `guMtxCatF`,
  `__osSiGetAccess2`, `guMtxL2F`, `__ull_divremi`, `__ll_mod`, `guNormalize`,
  and `__osTimerServicesInit`.
- Recovered the necessary object profiles from Banjo (`-O1`, plain `-O2`, or
  `-O3` depending on the object), avoided the graphics-header `sqrtf`
  intrinsic for `guNormalize`, and reproduced timer initialization's
  same-translation-unit 64-bit global coalescing.
- Verified the normal full build and retail-ROM scan with no neighboring
  regressions: **2445 / 5973 overall (40.93%)**, **370 / 508 init (72.83%)**,
  **1909 / 5284 game (36.13%)**, and **166 / 181 debugger (91.71%)**. This is
  a net gain of eight byte-exact functions with the same one address-drift
  blocker.

### Three-function byte-matching target completed

- Completed the requested
  `[########################] 3 / 3 (100.00%)` target:
  `func_151E50C8`, `func_15017498`, and `func_15007A70` are all independently
  byte-exact.
- Reconstructed `func_151E50C8`'s complete behavior and matched its retail
  `0x124`-byte body. The adjacent `func_151DD970` 23-byte copy helper also
  became exact at `0x74` bytes.
- Used the verified Banjo-Kazooie decompilation to confirm that IDO code
  generation depends on same-translation-unit BSS ownership. In Conker's
  generated-slice build, a correctly-sized destination definition guides IDO
  address coalescing while `pad_generated_object.py` discards the compact
  object's `.bss` and retains only text/relocations.
- Resolved the last scheduling difference with the decomp permuter: the
  matching form keeps the copy loop on one physical source line and uses an
  optimized-away `^ 0` to retain the retail register allocation.
- Verified a full production relink and drift-aware match scan. Byte-exact
  progress is now **1904 / 5284 game functions (36.03%)** and
  **2437 / 5973 overall (40.80%)**, with the same one address-drift blocker
  and no regressions.

## 2026-07-24 (continued, fourth pass - scoping a push toward 42%)

### Two more matched; the easy-win pool is now mostly exhausted

- `func_1503DF0C` and `func_150A0374` reached byte-exact: a struct-field
  read-modify-write against the already-typed `struct106 D_800C6660[]`
  array (needed the byte-index-14 field widened past `struct106`'s
  anonymous `pad[3]`), and another instance of the then/else physical-layout
  swap pattern (now fixed four times this session).
- **Scale check, since the ask was a specific percentage target:** a bulk
  scan of every non-exact C function (`ours` compiled length vs `truth`
  retail length) found roughly **3,080 functions that are still literal
  `return 0;` placeholders** with a real retail body waiting to be
  reconstructed - the actual remaining backlog is almost entirely this, not
  small scheduling diffs. Reaching 42% needs 73 more exact functions from
  a session baseline of 2,433; each one still requires the same
  manual cycle (read retail words, infer the C shape, guess field/array
  types from the few already-typed structs, build, diff, iterate) with no
  found way to batch it - a promising-looking family of ~62 near-identical
  "dispatch through a function-pointer table, then two fixed calls"
  handlers (`func_151A8584`/`func_151A85D4` and siblings in
  `generated_1D4E00.c`) turned out to hit the same argument-homing-timing
  wall as `func_151ACB60` (retail homes the incoming pointer lazily, in a
  `jalr` delay slot; our compile homes it eagerly at entry) once actually
  tried, so it isn't the multiplier it looked like.
- Reconstructed real (but not yet byte-exact) bodies for four more former
  stubs while investigating - `func_15096934`/`func_1510E634` (write a
  2-word "magic tag + pointer" node header, matching the game's node/list
  init idiom), `func_1507EEB8` (5-byte ring-buffer push/shift), and
  `func_1502C380` (read an indexed lookup table entry, fan it out to two
  fields plus a cleared counter) - all confirmed logically correct against
  retail's instructions but still differ by register choice or instruction
  order, the same resistant classes from earlier in this session. Left
  as-is rather than reverted to `return 0;`, since a real, instruction-level
  verified implementation is strictly more useful to the next session than
  a placeholder, even short of byte-exact.
- Re-tried the previously-parked `func_151E81EC` global-clear family
  (`DOCS/WORKING_NOTES.md`'s "lui-$at paired stores... cannot be reproduced
  with extern declarations") with both a scalar-externs shape and an
  array-element shape; both confirmed the same finding again - IDO emits a
  fresh `lui` per external symbol access and never reuses one `%hi` load
  across consecutive stores to different symbols the way retail's build
  did, regardless of declaration style. Still unsolved; not a source-shape
  problem.
- Verified **1902 / 5284 game functions (36.00%)** and **2435 / 5973 overall
  (40.77%)** byte-exact, same one address-drift blocker, no regressions.
  Raw C conversion remains **5973 / 6033 (99.01%)**. At the pace of this
  session (roughly 2-5 confirmed exact functions per focused pass, after
  screening out many more that hit resistant compiler-behavior classes),
  reaching 42% is a real but multi-session undertaking, not a single push -
  see the bulk-stub-scan finding above for where the remaining work
  actually lives.

## 2026-07-24 (continued, third pass)

### Five more functions matched: two libultra stubs implemented, two struct-size bugs found

- `__osSiRelAccess2` and `__osSiCreateAccessQueue2` (`game/generated_siacs2.c`)
  were still raw `return 0;` placeholders. Their non-"2" siblings
  (`__osSiRelAccess`/`__osSiCreateAccessQueue` in `libultra/io/siacs.c`) were
  already matched real implementations using the same
  `osSendMesg`/`osCreateMesgQueue`/`D_8002BE20`/`D_80042AA8` idiom; copied the
  pattern onto the "2" queue's own globals (`D_800E0D20` message buffer,
  confirmed via the linked ELF's `osCreateMesgQueue`/`osSendMesg` call targets
  at their name-implied addresses) and both went byte-exact immediately.
  `func_15149104` was the same class - an unconverted stub whose retail body
  is a single forwarding call (`func_151478F4(arg0)`, confirmed against that
  function's real signature from its other call sites) with no visible
  argument setup, meaning it just passes its own incoming `a0` straight
  through.
- `func_15194DC8`: retail's stack frame is 80 bytes, but the placeholder's
  local buffer (`f32 sp2C[3]`, passed to two undecompiled callees) only
  produced 56. Growing the buffer to `f32 sp2C[9]` (matching the 24-byte /
  6-word gap exactly) reached byte-exact in one try - the callee apparently
  writes a larger record than the `struct17` (3-float vec3) guess used at
  other call sites of the first callee, `func_1504715C`; worth revisiting
  those other sites' type later.
- `func_15195738` pattern repeats: `func_1000FE88` and `func_15019BB8` are
  the same stack-slot/frame-size class as previously-fixed
  `func_1515FBC4`/`func_15194DC8` but resisted the same tricks (adding a
  local grew the frame past retail's size instead of reusing slack); left
  for a future session.
- `func_151D7724`: retail computes `arg0 + 0x28` before evaluating the
  four-way OR condition and reuses it in the delay slot of the first
  `bnezl`, but the placeholder computed it only inside the `if` body once
  the condition was already known true. Hoisting the local's declaration to
  match retail's unconditional-early-computation order fixed the placement;
  a second, unrelated diff remained (`andi ...,0xfe` vs `andi ...,0xfffe`)
  that turned out to be a harmless mask-width difference - both produce the
  same result once the value's already come from an 8-bit `lbu`, so widening
  our literal to `0xFFFE` matched retail's source exactly with no behavior
  change. The two sibling functions in the same file (`func_151D7770`,
  `func_151D779C`) show the same `0xfe`-vs-`0xfffe` mask pattern in their own
  diffs - worth checking first next time, they may be one-line fixes.
- Tried and reverted several more candidates, all confirming already-known
  resistant classes rather than new ones: `func_1514672C` and
  `func_151254F4`/`__osSiGetAccess2` (independent-instruction/prologue
  reorder - explicit temps don't change IDO's chosen order), `func_1509D054`
  and `func_151B2FA0` (retail routes a call argument through an extra
  register/stack round-trip our compile elides), `func_1000FE88` (stack-slot
  class with only one real local, no reorder candidate), `func_1515FB70` and
  `func_100043B4` (retail computes a value it then provably discards - the
  same "dead code IDO won't reproduce" puzzle as `func_150C7930`), and
  `func_150A7770`/`func_10001420` (both are `__retail_overflow_*` trampolines
  - our correct-looking C loop body doesn't fit the tiny 8-9 word retail
  span even with `-Wo,-loopunroll,0`; retail's tight `bnezl`-based loop is
  almost certainly genuinely hand-written SDK code, same class as the COP0
  accessors and the `sin`/`cos` fallthrough trampoline from the last
  session).
- Verified **1900 / 5284 game functions (35.96%)** and **2433 / 5973 overall
  (40.73%)** byte-exact, same one address-drift blocker, no regressions in
  init or debugger. Raw C conversion remains **5973 / 6033 (99.01%)**.

## 2026-07-24 (continued)

### Three more game functions matched; two more real bugs found

- `func_1515F10C` (linked-list node removal) and `func_151F2D6C` (audio pitch
  clamp) both had the same shape: an `if`/`else` whose source order matched
  the *logic* but not retail's *physical instruction layout* - IDO put the
  other branch at the fallthrough position and this one at the jump target.
  Swapping the branch condition and its body order (same trick that fixed
  `func_151BD2BC` earlier today) made both byte-exact.
- `func_15195738`: two independent bugs in one stack-local record init.
  (1) `func_150ADA20() % 0xB` used signed division; retail's `divu` proves the
  modulus needs an unsigned operand (`% 0xBU`), matching the `% 3U` idiom
  already used elsewhere in the codebase for the same PRNG call. (2) the two
  final field writes (`sp18[5] = 1; sp18[6] = -1;`) had the right values but
  the wrong evaluation order - retail assigns index 6 before index 5. Fixing
  both (division operand type, then statement order) reached byte-exact.
- Tried and reverted three more candidates, each confirming a resistant class
  already on record: `func_1514672C` (independent-load reorder feeding a
  float compare - explicit temp did not change it, worse when tried harder),
  `func_1509D054` and `func_151B2FA0` (retail routes a call argument through
  an extra register/stack round-trip that our compile elides - adding a
  prototype for the untyped callee did not change it). `func_1000FE88` (init)
  is the same stack-slot-offset class already fixed twice elsewhere, but here
  the function has only one real local and no reordering candidate; adding a
  matching second local shifted the slot but grew the frame past retail's 32
  bytes, so reverted. `func_150AD780` turned out to be a shared fallthrough
  trampoline (`sin(x) = cos(x + pi/2)`, no `jr ra` of its own - it falls
  straight into `func_150AD78C`'s body), the same "not really its own
  function" class as `func_150A6354` from the last session.
- Verified **1895 / 5284 game functions (35.86%)** and **2428 / 5973 overall
  (40.65%)** byte-exact, same one address-drift blocker, no regressions in
  init or debugger. Raw C conversion remains **5973 / 6033 (99.01%)**.

## 2026-07-24

### Two more game functions matched; one real logic bug fixed

- `func_151BD2BC`: found and fixed an inverted-comparison bug, not just a
  matching artifact. The existing placeholder returned 1 when two byte fields
  were *unequal* and 0 when equal; retail's preset/override pattern
  (`li v0,1` before the compare, `move v0,zero` in the fallthrough) proves the
  real predicate returns 1 on equality. Swapping the comparison and return
  values makes the function byte-exact.
- `func_1515FBC4`: reordering the `index`/`temp_v1` local declarations shifted
  `temp_v1`'s stack slot from `sp+28` to retail's `sp+24`, the only remaining
  difference. Now byte-exact.
- Surveyed the smallest remaining diffs (1-3 real instruction words) for more
  candidates. Most of the rest are one of two resistant, already-documented
  classes and were reverted after confirming no source-level rewrite changes
  the output: (1) commutative-operand / independent-instruction canonicalization
  (`addu`/`multu`/`bne`/`beq` operand order, or the order of two independent
  address computations) that IDO reorders the same way regardless of source
  expression or declaration order; (2) register-choice artifacts where IDO
  picks a different scratch register for a dead value than retail
  (`func_15087FC4`/`func_15087FEC`, `func_15079F6C`, `func_15199980`). A
  fix for `func_151733D8` (adding its real 2-argument signature plus a
  per-file `-O2` no-`-g3` override to get the retail-filled branch-delay
  slot) only works by changing the whole file's compile profile, which flips
  the file's one already-exact function (`func_15173994`) to non-exact - a
  net wash, reverted per the "no regressions" rule. This limitation was
  superseded on 2026-07-26 by selecting just that function from a separately
  compiled non-debug object.
- New findings for future sessions: `func_150AC9B0`'s retail body is a bare
  `j func_150AC2D8` (no `jal`, no frame) - a real tail call, but a plain
  `return func_150AC2D8();` compiles to a full `jal`+move+`jr` sequence (2x
  the retail size); this is the only function in the entire retail corpus
  with that exact bare-tail-jump shape, so it's likely not reachable through
  normal C. `func_150A6354` is not an independent callable function at all -
  retail's own `func_150A6210` reaches it via raw `j func_150A6354` (twice,
  as a shared exit path) rather than `jal`, so it's a shared epilogue
  fragment of `func_150A6210`, not a real leaf routine with its own C
  signature.
- Verified **1892 / 5284 game functions (35.81%)** and **2425 / 5973 overall
  (40.60%)** byte-exact, with the same one address-drift blocker and no
  regressions in init or debugger. Raw C conversion remains
  **5973 / 6033 (99.01%)**.

## 2026-07-19

### Byte-exact matching crossed 40% overall

- Matched roughly 230 more game functions by reconstructing small
  generated-slice placeholders directly against retail instructions, focusing
  on repeated families: typed argument-forwarding wrappers, predicates,
  stack-local event records, jump-table dispatchers, linked-list walkers,
  clamped-store helpers, and float accumulate/scale routines.
- Root-caused a large class of mismatches to missing local prototypes in
  generated slices (implicit declarations reload narrow arguments from home
  slots instead of masking in place) and fixed whole families by adding
  per-file prototypes.
- Identified per-slice retail compile profiles: two slices build with plain
  `-O2` (filled jr-delay slots) and four need `-Wo,-loopunroll,0`; recorded the
  overrides in `conker/Makefile`.
- Corrected two wrong callee identities (`func_100111C8` vs a stale
  `func_140111C8` symbol, and `memcpy`/`bzero`/`allocate_memory`/Pi-access
  libultra callees referenced by name-implied placeholder ids).
- Verified **1860 / 5284 game functions (35.20%)** and **2393 / 5973 overall
  (40.06%)** byte-exact, with one address-drift blocker and no regressions in
  init or debugger sections.

## 2026-07-18

### Documentation topics consolidated

- Rebuilt the root README as a concise project entry point with a clearer
  status explanation, supported build overview, contribution path, and
  purpose-based documentation links.
- Reorganized `DOCS/README.md` into a subject index and made `PROJECT.md` the
  detailed source for build, environment, CI, ROM-layout, and progress
  explanations.
- Added `DOCS/CONTRIBUTING.md` as the durable home for function selection,
  byte-matching workflow, IDO-sensitive source patterns, retail-span rules,
  and required validation.
- Labeled `WORKING_NOTES.md` as an archive/scratchpad, added a topic index, and
  separated the current recovery entry from historical focus snapshots.
- Corrected and expanded the asset specification: documented the real packed
  entry bitfield and 30-entry master table, libaudio `B1`/`S1` structures,
  confirmed game-code archive/XOR layout, vertex-count ambiguity, scoped
  texture evidence, and the complete known/unknown section inventory.
- Updated `tools/asset_dump.py` to derive all `assets00-assets1C` boundaries
  from the retail master table instead of maintaining a partial hardcoded list.

### Repeated wrapper sweep reached 36.28% overall

- Matched 13 more game functions across four repeated two-function families
  and one five-function cleanup family.
- Recovered exact retail argument forwarding, indexed byte lookup, stack-local
  record dispatch, and deliberate repeated volatile field reads in call delay
  slots.
- Verified **1634 / 5284 game functions (30.92%)** and **2167 / 5973 overall
  (36.28%)**, with **0** address-drift blockers. Raw C conversion remains
  **5973 / 6033 functions (99.01%)**.

### Fast byte-matching sweep passed 35% overall

- Matched 246 additional game functions across generated slices, emphasizing
  repeated two-call wrappers, field setters, callback dispatchers, compact
  predicates, argument-forwarding helpers, and fixed-point/float leaves.
- Restored retail IDO schedules with exact argument widths, explicit temporary
  loads, direct boolean expressions, name-implied retail globals, and repeated
  wrapper templates; rejected experiments that exceeded their retail spans.
- Added the missing external routine symbol at `0x140111C8`, allowing two
  retail handle-release wrappers to link and be measured normally.
- Verified **1621 / 5284 game functions (30.68%)** and **2154 / 5973 overall
  (36.06%)**, with **0** address-drift blockers. Raw C conversion remains
  **5973 / 6033 functions (99.01%)**.

### Fast generated game sweep reached 26.02%

- Matched 45 additional compact game functions across generated slices,
  concentrating on direct wrappers, state setters, accessors, flag updates,
  indexed writes, and global resets that reproduce retail IDO code cleanly.
- Recovered exact short-function shapes through argument preservation, call
  delay-slot constants, right-to-left expression ordering, volatile pointer
  reloads where retail reads twice, and explicit field-width/sign choices.
- Kept useful partial reductions for `func_150F02A0`, `func_150CBF5C`, and
  `func_151D0128`; reverted the `func_151EFF70` experiment after its compiled
  body exceeded the retail span.
- Verified **1375 / 5284 game functions (26.02%)** and **1908 / 5973 overall
  (31.94%)**, with zero address-drift blockers and no lost exact matches.

### Difficult game near-matches recovered

- Matched `func_150779D4` and `func_15079570`, two 51- and 59-instruction
  routines that were already behaviorally correct but still differed in
  floating-point temporary allocation and a final address-register choice.
- Restored the retail expression shapes with explicit distance and threshold
  temporaries plus the native `struct127.y_position` field access.
- Matched the 54-instruction `func_1507879C` by separating its `struct197`
  pointer load from the float access, restoring retail's `v0` reuse across
  the indexed object lookup.
- Reduced the 55-instruction `func_15135480` from seven real instruction
  differences to two by restoring its reused object value and early-exit
  comparison shape; the two remaining differences are commuted branch
  operands.
- Rejected and reverted experiments that worsened `guMtxCatF`,
  `func_1505D024`, `func_1505841C`, `func_151254F4`, and `func_1514672C`.
- Verified **1330 / 5284 game functions (25.17%)** and **1863 / 5973 overall
  (31.19%)**, with zero address-drift blockers and no lost matches.

### PC-port runtime reference

- Evaluated N64 Modern Runtime as a useful Phase 1/2 candidate instead of a
  generic reference: `ultramodern` covers much of the libultra OS surface and
  `librecomp` bridges N64Recomp output plus ROM/save operations.
- Added a compatibility-inventory step and kept the runtime reference-only
  until Conker's Rare-specific code and microcode are proven compatible; no
  dependency, submodule, or ROM-build change was made.
- Added RT64 as the first renderer to evaluate before committing to a custom
  RSP/RDP display-list interpreter.

### Game byte-exact progress reached 25.11%

- Matched ten additional game functions: `func_15014220`, `func_15015644`,
  `func_15075884`, `func_15075AAC`, `func_1512D368`, `func_1514373C`,
  `func_151927C0`, `func_151D2BA4`, `func_151EEFF0`, and `func_151EF080`.
- Recovered four larger 35-45-word routines alongside compact math, state,
  copy, and generated-slice helpers by restoring retail argument constants,
  statement order, temporary-expression shapes, and the required IDO object
  profile.
- Rejected an optimization-setting tradeoff that would have lost an existing
  exact function; the clean rebuild retains every prior match.
- Published game byte-exact progress at **1327 / 5284 functions (25.11%)**
  and total byte-exact progress at **1860 / 5973 (31.14%)**. Address-drift
  blockers remain zero and raw C conversion remains **5973 / 6033 (99.01%)**.

### Init byte-exact progress reached 56.89%

- Matched 26 additional init functions across PI/SI/SP raw I/O, VI state,
  message queues, thread management, timers, audio, libc, and game code.
- Restored the retail IDO `-O1` object profiles and the original
  `register`-qualified status, interrupt-mask, queue-index, and thread-walk
  locals that control allocation and scheduling.
- Reconstructed exact source shapes for `func_1000F1A8`, `func_1001AFEC`,
  `__n_nextSampleTime`, `strchr`, and `osAiSetNextBuffer`; reduced
  `func_1000FE88` from three real instruction differences to two.
- Published init byte-exact progress at **289 / 508 functions (56.89%)** and
  total byte-exact progress at **1735 / 5973 (29.05%)**. Address-drift
  blockers remain 27 and raw C conversion remains **5973 / 6033 (99.01%)**.

### Init byte-exact progress reached 51.77%

- Matched eight additional init functions: `ldiv`, `lldiv`,
  `__osSpRawStartDma`, `osSpTaskYielded`, `osViSwapBuffer`,
  `__osDequeueThread`, `__osTimerInterrupt`, and `__osSetTimerIntr`.
- Recorded the retail IDO optimization profiles per object and restored the
  original `register`-qualified thread-queue source shape.
- Corrected `func_1001091C` to pass the retail pointer value instead of an
  unrelated pointed-to field; the function remains one instruction from an
  exact match.
- Published init byte-exact progress at **263 / 508 functions (51.77%)** and
  total byte-exact progress at **1709 / 5973 (28.61%)**. Address-drift blockers
  remain 27 and raw C conversion remains **5973 / 6033 (99.01%)**.

### Init byte-exact progress crossed 50%

- Matched 22 additional init functions, including native 64-bit compiler
  helpers, PI/SI access and raw-I/O routines, SP status helpers, VI framebuffer
  accessors, message-queue helpers, `memcpy`, `strlen`, and one audio event
  walker.
- Restored retail IDO `-O1`/`-O2` profiles, native MIPS III code generation,
  and original `register`-qualified source shapes where they determine exact
  instruction scheduling.
- Published init byte-exact progress at **255 / 508 functions (50.20%)** and
  total byte-exact progress at **1701 / 5973 (28.48%)**. Address-drift blockers
  remain 27 and raw C conversion remains **5973 / 6033 (99.01%)**.

### Byte-exact progress crossed 28%

- Reconstructed 63 compact generated-slice functions as matching C,
  including callbacks, constant handlers, scalar helpers, field initializers,
  table accessors, flag setters, and thin call wrappers.
- Preserved retail incoming registers and call-delay-slot constants through
  explicit legacy declarations, calling-convention-width parameters, and
  targeted `register` annotations.
- Reverted four exploratory near-matches so the published code batch contains
  only confirmed exact improvements.
- Published byte-exact progress at **1679 / 5973 functions (28.11%)**, with
  address-drift blockers unchanged at 27 and raw C conversion unchanged at
  **5973 / 6033 (99.01%)**.

### Byte-exact progress crossed 27%

- Reconstructed 35 small generated-slice functions as matching C, including
  typed callbacks, constant-return handlers, nested accessors, arithmetic
  helpers, and state setters.
- Preserved IDO's retail argument-home behavior and register scheduling with
  explicit calling-convention-width parameters and targeted `register`
  annotations.
- Published byte-exact progress at **1616 / 5973 functions (27.06%)**, with
  address-drift blockers unchanged at 27 and raw C conversion unchanged at
  **5973 / 6033 (99.01%)**.

### Total raw C conversion crossed 99%

- Replaced 416 validated `GLOBAL_ASM` groups across 105 mixed sources and
  moved 80 tracked libultra functions through 40 typed standalone C slices.
- Extended signature discovery for nested function pointers, local `static`
  declarations, directly included source headers, macro-shadowed names, and
  legacy functions called with inconsistent argument counts.
- Generalized generated-slice Makefile and linker support to nested libultra
  assembly paths, while retaining exact retail symbol placement.
- Published raw conversion at **5973 / 6033 functions (99.01%)** and **98.34%
  by bytes**; game conversion reached **5284 / 5313 (99.45%)**.
- Recorded the complete 60-function raw remainder and the honest byte-exact
  result: **1581 / 5973 (26.47%)**, with 27 address-drift blockers.

### Total raw C conversion crossed 90%

- Added 167 validated standalone game slices and replaced 246 `GLOBAL_ASM`
  groups across the eight largest remaining mixed C sources.
- Added a reproducible mixed-source converter that reuses declared signatures,
  infers consistent legacy-call arity, and validates each referenced asm file.
- Published raw conversion at **5477 / 6033 functions (90.78%)** and **84.09%
  by bytes**; game conversion reached **4968 / 5313 (93.51%)**.
- Kept address blockers at 24. Required legacy-call signatures perturb one
  previously exact caller, leaving **1584 / 5477 (28.92%)** byte-exact.

### Total raw C conversion crossed 80%

- Replaced 82 additional safe text-only game assembly slices with generated
  non-matching C sources, moving 588 tracked functions into C.
- Taught the placeholder generator to recognize indented global entry points
  and reject retail slots smaller than the compiler's eight-byte minimum.
- Excluded one mixed code/data slice and two slices with four-byte entry spans
  instead of weakening the layout validator or dropping symbols.
- Published raw conversion at **4846 / 6033 functions (80.32%)** and **68.37%
  by bytes**; game conversion reached **4338 / 5313 (81.65%)**.
- Retained all **1585** byte-exact functions and kept address blockers at 24.

### Total and game raw C conversion crossed 70%

- Replaced 44 additional text-only game assembly slices with generated
  non-matching C sources, moving 612 tracked functions into C.
- Checked every selected slice for embedded data sections or word tables before
  replacement, then regenerated the retail-layout manifest.
- Published raw conversion at **4258 / 6033 functions (70.58%)** and **55.77%
  by bytes**; the game section independently reached **3750 / 5313 (70.58%)**.
- Preserved all prior exact matches and recovered one additional match, taking
  byte-exact progress to **1585 / 4258 (37.22%)** with 24 address blockers.

### Total raw C conversion crossed 60%

- Replaced 25 additional text-only game assembly slices with generated
  non-matching C sources, moving 613 tracked functions into C.
- Made generated-slice Makefile filtering and linker placement automatic so
  future additions no longer require duplicated hardcoded slice lists.
- Added a reproducible placeholder generator, including compact empty-body
  stubs for functions whose retail slots are only eight bytes.
- Published raw conversion at **3646 / 6033 functions (60.43%)** and **43.81%
  by bytes**. Byte-exact progress is **1584 / 3646 (43.44%)**, with all prior
  exact matches retained and one additional exact function recovered.

## 2026-07-17

### Byte-exact progress crossed 50%

- Added retail-layout manifests and build-time object re-spacing that preserve
  C-compiled instruction words and relocations while restoring function and
  object addresses.
- Kept oversized non-matching functions executable in section-local overflow
  regions through short retail-slot trampolines, preventing them from shifting
  later exact code.
- Restored generated-slice jump labels inside their padded C-derived objects
  and reduced address-drift blockers from 836 to 24.
- Published the new result: **1583 / 3033 C functions byte-exact (52.19%)**,
  with raw C conversion unchanged at **3033 / 6033 (50.27%)**.

### Tool reference triage

- Recorded `n64img` as the preferred N64 image-format reference through the
  existing n64splat dependency path (`tools/n64splat/requirements.txt` already
  requires it), avoiding a redundant standalone submodule.
- Added `N64-IPL` as a reference-only upstream for boot/IPL/header/checksum
  context.
- Left `mips-gcc-2.7.2` out of the active toolchain for now; it is useful if a
  KMC/GCC-compiled island is identified, but current matching work is still
  IDO 5.3 based.
- Updated active helper submodules after checking upstream HEADs:
  `tools/asm-differ` to `fdf9c6c`, `tools/asm-processor` to `b29ff12`, and
  the parent repo's `tools/mips_to_c` pointer to the already-checked-out
  `m2c` upstream `554de36`.

## 2026-07-14

### ROM library, EU pipeline, and censorship analysis

- All four target versions (`us`, `eu`, `debug`, `ects`) now have
  hash-verified baseroms available locally for the first time. The EU ROM
  arrived as a byte-swapped `.n64`; converted to big-endian and verified
  against `conker.eu.sha1`. (The local ROM store was reorganized mid-way and
  temporarily lost the us/ects copies; the recovery, including hash
  identification of every file in the store, is logged in
  [`DOCS/WORKING_NOTES.md`](WORKING_NOTES.md).)
- Modernized `conker.eu.yaml`/`game.eu.rzip.yaml` (and `conker/conker.eu.yaml`)
  to current splat format with version-separated output paths
  (`asm_eu`/`assets_eu`/`src_eu`), so `make extract VERSION=eu` runs clean and
  the decompressed EU code image verifies against `conker/conker.eu.sha1`.
  EU disassembly (5,759 functions) now extractable as a third matched-code
  reference alongside the `debug_proto`/`ects_proto` trees.
  `conker.debug.yaml`/`conker.ects.yaml` still need the same two-line fix.
- Analyzed the "Uncensored" US romhack as a differential probe for asset
  formats: it replaces exactly 15 of 50 `assets06` files and 23 of 453
  `assets16` files strictly in place (offset tables byte-identical). This
  confirms `assets16` as the dialogue-audio MP3 bank and pins down which
  `assets06` files carry per-dialogue-line data. A Spanish translation hack
  independently corroborates this (it rewrites `assets06` far beyond the
  censored lines - subtitle text lives there). Findings folded into
  [`DOCS/ASSET_FORMATS.md`](ASSET_FORMATS.md).

### Windows/WSL build environment for this checkout

- Set up and documented building directly from this Windows checkout through
  WSL (Debian distro, project venv, `binutils-mips-linux-gnu`; the bundled
  IDO recomp binaries run fine from `/mnt/c`). Exact steps and the
  incremental rebuild/verify loop are in
  [`DOCS/WORKING_NOTES.md`](WORKING_NOTES.md).
- The CRLF/symlink checkout corruption documented below recurred (suspected
  OneDrive interaction) and was re-fixed; diagnosis shortcut now documented:
  splat failing with `could not load segment type 'rzip'` means
  `tools/splat_ext/rareunzip.py` (a git symlink) got checked out as a text
  stub again.

### Byte-matching progress tooling

- Added `tools/match_progress.py` and a `make -C conker match-progress`
  target (add `LIST=1` for a per-function listing): for every C-converted
  function in `progress.csv`, it compares the linked ELF's disassembly
  (keyed by function symbol, so immune to the known init-section layout
  drift) against ground-truth bytes from the pristine `conker.us.bin`, and
  classifies each as byte-exact, blocked-on-callees (only `j`/`jal` targets
  differ), or still differing. This productizes the session's scratchpad
  verification method. First run: **379 / 1553 C functions byte-exact
  (24.40%)** - init 201/232, game 167/1151, debugger 11/170 - now published
  as a second snapshot table in the root `README.md`,
  [`DOCS/README.md`](README.md), and [`DOCS/PROJECT.md`](PROJECT.md).

### Function matching (continued)

- Resolved 6 more of the remaining ECTS-ported non-matching functions:
  5 now byte-exact (`func_16001B00`, `func_15060BA4`, `func_1506196C`,
  `func_150AED9C`, `func_15142A5C`), 1 logically complete pending callees
  (`func_1504CA60`). 26 remain. Two stubborn functions are documented
  non-matching with in-source comments (`func_1514143C`, `func_1507A3E8`).
- Wrote up six reusable IDO/cfe codegen idioms (register-class rules for
  named locals vs temps, `u8` field-update codegen, branch-vs-`slt` return
  forms, operand evaluation order, mips_to_c artifact locals, pointer
  folding) in [`DOCS/WORKING_NOTES.md`](WORKING_NOTES.md) - read these
  before brute-forcing rewrites on the rest.

### Build environment and decomp progress

- Fixed a broken local build environment (pre-existing, not caused by this
  session): incorrect `core.symlinks`/`core.autocrlf` git config had left
  ~450 tracked files checked out with CRLF line endings and broken symlinks,
  which silently broke the IDO compiler. Fixed locally; see
  [`DOCS/WORKING_NOTES.md`](WORKING_NOTES.md) for the exact recovery steps
  if this recurs in a fresh clone or devcontainer.
- Fixed two `tools/n64splat` submodule version-compatibility bugs in this
  project's own extension code/config (`tools/splat_ext/rzip.py`,
  `conker/conker.us.yaml`, new `conker/include/asm_processor_prelude.inc`)
  that were blocking `make extract` and the C compile entirely.
- Ported 56 functions (46 `game`, 10 `debugger`) from the untracked
  `ects_proto/` reference checkout (targets the ECTS prototype ROM) into
  this repo's `conker/src/`, replacing raw-assembly stubs with real matched
  C, and added the struct fields/globals/prototypes those functions needed.
  12 of the 56 byte-match the US retail ROM exactly out of the box; the
  other 44 compile cleanly and are marked `// NON-MATCHING: ported from
  ects_proto (ECTS ROM build), not yet byte-verified for us` pending a real
  matching pass. Also fixed one small pre-existing bug found along the way
  (a call site in `game_1944C0.c` missing an argument).
- Fixed a long-standing link-time blocker: 26 jump-table `rodata` segments
  in `conker/conker.us.yaml` were declared as standalone segments, causing
  1153 `undefined reference` errors at link time once code near them got
  matched. Changed them to `bin` (opaque byte blobs - jump table contents
  don't need symbolic disassembly). Full root-cause writeup in
  [`DOCS/WORKING_NOTES.md`](WORKING_NOTES.md).
- `make -C conker --jobs` → `make -C conker replace NON_MATCHING=1` →
  `make` (repo root) now runs end to end for the first time, producing a
  real (correctly non-matching, ~20% complete) `build/conker.us.z64`.
  Regenerated the progress table in [`DOCS/PROJECT.md`](PROJECT.md) from
  this working build - it's the first `.map`-file-derived count this
  checkout has actually produced, so it supersedes the previously
  documented (never locally re-verified) numbers.

### Planning docs

- Added [`DOCS/WORKING_NOTES.md`](WORKING_NOTES.md): a live, editable log of
  in-progress work, so a crashed editor/terminal/assistant session can be
  resumed from a known state instead of re-derived from scratch.
- Added [`DOCS/PC_PORT_ROADMAP.md`](PC_PORT_ROADMAP.md): a phased,
  date-free plan covering what's needed to get the game running natively on
  PC with keyboard, mouse, and controller input in a playable state, plus a
  longer-term modern-graphics phase (resolution scaling, widescreen, texture
  filtering/HD packs, enhanced lighting). No PC-port work has started; this
  is planning only.
- Linked both from the `DOCS/README.md` reading order.

## 2026-07-13

### Asset formats

- Added [`DOCS/ASSET_FORMATS.md`](ASSET_FORMATS.md) documenting the asset
  compression (`rzip`), the offset-table container format (confirmed against
  `func_1502B9B4` in `game_57FA0.c`), and per-type payloads.
- Confirmed findings against the retail US ROM and the debug prototype:
  RGBA5551 textures (assets00–05), MP3 streams (assets16), the `"B1"` audio bank
  header (assets17, 22050 Hz + 170-entry sample table), and container payloads.
- Corrected the earlier "assets06 = models" assumption: assets06 is composite
  object/script data (positions, float params, dialogue strings). assets08 is
  chapter-select metadata.
- Decoded the `assets13` model geometry: four-level-nested containers whose leaf
  records are `s16` XYZ vertex arrays (6 bytes/vertex, zero-padded to 16 bytes),
  validated across all 69 records; near-identical arrays within a block are
  vertex-animation frames.
- Established that `assets13` holds **only** vertex positions - 0 display-list
  markers across all 69 records - so face/UV/normal/material data is stored
  separately or built at runtime; locating it needs the model-drawing code.
- Linked the new doc from the `DOCS/README.md` reading order.

### GitHub Actions

- Updated checkout steps from `actions/checkout@v4` to `actions/checkout@v7` so workflows use the Node 24-compatible action.
- Changed the ROM build workflow to skip baserom-dependent steps when `PRIVATE_REPO_ACCESS` or `CONKER_BASEROM_US` is missing.
- Added clear workflow notices explaining which secrets are needed to enable the full ROM build.

### Documentation

- Moved repository-owned README content into the `DOCS/` folder.
- Added the `DOCS/README.md` documentation index.
- Rewrote the project overview, code sub-project notes, compressed config notes, and IDO toolchain notes for clearer reading.
- Added this update log.
- Added `DOCS/ASSET_FORMATS.md` documenting the rzip codec, the offset-table archive container (including the previously undocumented nested-compression layer inside model files), and the model/texture/audio/table payload formats.
