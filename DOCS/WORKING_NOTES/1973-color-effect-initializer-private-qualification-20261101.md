# 1973 - Color-effect initializer private qualification and scheduling gap

`func_15187EC0` now has a qualified private semantic candidate with **52 words,
frame 24 and 25 retail word differences**, improved from 36. It is **not installed
and receives zero matching credit**. A sparse argument-read counterexample also
remains. Production source, headers, objects, guard CSV, map, progress CSV and
ELF are unchanged. Fresh Native actual-ELF recount confirms **4,040/5,507
(73.36%)**, Game **3,367/4,834 (69.65%)**, zero drift and 1,467 different.
The 75% threshold remains 4,131: **91 more** matches; the wider goal stays active.

## Scope and recovered behavior

Baseline is the committed Note 1972 checkpoint, consumer
`05afb20c6a3558a6709e8a6be4879c50040b1fa8`, tools
`613aa33ebade9861840dacc00589b4bc66191496`. All 1,079 focused inputs were
explicitly rebased from that checkpoint. Target VA `0x15187EC0..0x15187F90`,
ROM `0x1B5370..0x1B5440`, owner `generated_1B5370`.

The signed counter `D_800DF7B4` is adjacent to the 180-byte, five-record pool
`D_800DF700`. A count below five selects a 36-byte record. The constructor stores
six incoming bytes as start RGB (+0..2), target RGB (+3..5), and duplicated current
RGB (+6..8). It preserves padding +9..11 and blend +12, writes the complete mode
word at +16 and raw rate float at +20, then uses `bzero` to clear 12 state bytes
at +24. It reloads the global count, increments it and returns its prior value.
For valid pool counts this is the appended index. Counts at least five return -1.
The original does not reject negative counts; no guessed lower-bound guard is added.

`ColorEffectRecord`, named RGB/mode/rate/state fields and parameter names describe
this private experiment. Renaming and the byte-array owner declaration retain
instruction identity with the screened source. The copied owner keeps its existing
`extern u8 D_800DF700[]`; a private cast provides the typed view. No production
header is changed. The current public header still declares the two register-byte
arguments as s32; actual incoming masks and all original callers are qualified,
while final C header integration remains part of any future adoption.

## Compiler investigation and advisory

The earlier 64 screens recovered the correct length/frame but left 36 differences.
Additional source/profile, donor, pointer-address, const and diagnostic qualifier
screens remain in the ignored stage. O1/g3 and O2/g2 are longer non-matches;
O2/g0 is also rejected. Its first-instruction frame heuristic is not a valid
frame measurement. No production compiler flags are changed.

One bounded Claude Code Pro advisory used the existing claude.ai/firstParty
route, safe mode, disabled tools, empty strict MCP configuration and no session
persistence. The captured init confirms `tools=[]`, `mcp_servers=[]`, and zero
tool-use events; one call was attempted and completed. Packet/reply hashes,
reported usage and the review record are retained. Reported cost is provider
metadata, not evidence of an additional subscription charge.

Codex independently tested all three suggestions. Moving the mode store after
the target RGB stores removes the A0-to-A1 copy, restores a stack-home reload and
improves **36 to 25 differences**, without volatile qualifiers or guards. Moving
mode earlier or rate later gives 37 differences. This confirms the source lever,
not a unique causal explanation of the allocator. The advisory's claim that a
small set of failed experiments could prove no source match exists is rejected.
Volatile diagnostic forms remain unadopted. Const parameter forms do not improve
the natural candidate. The candidate still hoists the third-byte load before the
full-pool rejection and delays other byte loads; retail groups them after the gate.

## Qualification and explicit limits

- **11,256 guest cases / 33,768 executions** compare original, earlier 36-word-
  difference and improved 25-word-difference programs at three GNU link layouts.
  Public memory, result and call order agree on that mapped corpus. All **52
  original words** execute. All six byte fields cover 0..255 with poisoned upper
  argument bits; mode words, raw float payloads, stack phases and negative mapped
  counts are covered. Full GPR/FPR/private-state or access-order equality is not
  claimed for these non-matching programs.
- The original **40-word bzero** is equal to its retained production slot and is
  connected on its reachable aligned 12-byte route. It is also checked against a
  bounded semantic stub with caller-saved clobbers. No claim covers every bzero path.
- Two wrapped negative indices select the adjacent counter as a record. The
  independent reference reloads the counter after field stores; RGB writes can
  alter the value returned/incremented, including unsigned machine wrap. These
  are mapped guest probes, not valid native array indices.
- **Sparse counterexample:** with count five, remove the third-byte argument's
  mapping. Retail returns -1; both private candidates perform an extra `lbu` and
  fault in the bounded model. This expected failure is asserted in the public
  suite. Passing public-value cases does not close this access-order gap.
- Native32 O0/O2/O3 each pass **1,760 cases / 15,840 executions**, checking all
  **288 pool/guard bytes**, return and count with UBSan. Eight effective controls
  reject a sixth-record append, narrowed mode, wrong rate field, missing current
  red, wrong target green, wrong stride, short clear and next-index return.
  Only valid native table bounds are exercised; negative guest probes stay separate.
- All **three aligned direct JALs** are identified: ROM `0x370CC`, `0x37178`,
  `0x37478`. No aligned direct J or pointer literal targets the constructor.
  **120 caller cases / 240 executions** cover complete original parents
  `func_15009BD0` (43 words), `func_15009C7C` (43), `func_15009F74` (45), all their
  words, real eight-slot argument setup and float words. Original bzero and the
  11-word memcpy are connected. The later factory's success/null results are
  modeled; no complete factory/gameplay proof is claimed. Factory failure does
  not roll back the pool append, and full-pool -1 propagates into the actor packet.
  Parent C returns remain void.
- Complete copied raw and padded owners preserve **five neighbors** and pools;
  diagnostics remain **0 to 0**. The real three-command generated-owner recipe
  produces the identical private padded object.
- The complete private ELF equals an independent prediction changing only its
  208-byte target slot and symbol extent **12 to 208 bytes**, with zero exclusions.
  All **6,052 addresses**, **6,051 other bodies**, named definitions and normalized
  map remain fixed. All **189,088 protected Game bytes / 720 owners** stay exact.
  This proves private ownership, not retail matching. Its actual ELF recount still
  reports **4,040/5,507**, with the target at **25 real differences**.
- Both tools checkouts pass **five new private tests plus shared checks**. One
  refactor attempt failed on a quoted source-split marker; the corrected version
  passes both complete runs. The test API explicitly refuses adoption and credit.
  No unchanged broad semantic suite is rerun.

## Artifacts and continuation

Stage `conker/build/game-five-record-initializer-15187EC0-match/` retains 27
canonical prepared-artifact pins, frozen inputs, original/private objects and
links, source screens, guest/native/caller/owner/Make/image receipts, advisory
packet/reply, test logs, fresh Native production recount, graph proof and handoff.
The production ELF remains:
`860997333f77ca8592380dc62a6be70141037cd54e8ae01e8455036e0d9e68fe`.

Next target **`func_1513DF9C`** is independently confirmed unmatched in the current
ELF. Its private screen recovers all **53 code words / frame24** and the **52-byte
switch table**. The isolated .rodata has a separate 12-byte alignment tail, which
is not claimed as original table data. Candidate/table evidence is retained in
`next-dispatch-screen/`; there is no adoption or credit yet. Rebase its qualification
from this research commit, then inspect actual callbacks/callers, copied owner,
rodata ownership, actual Make, complete image and production gates. Preserve the
initializer's 25-difference/sparse-read gap for later compiler work.

Only focused tools and these research docs are committed. Root README aggregate
numbers remain correct and unchanged; it receives no function narrative. Preserve
original assembly, all private experiments, current and older archives, the dirty
older tools mirror, WSL cache and frozen host Release. Tools commit first; no push.
