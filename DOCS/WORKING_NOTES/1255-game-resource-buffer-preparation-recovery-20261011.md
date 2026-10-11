# Resource Buffer Preparation Recovery

Verified 2026-10-11. Consumer baseline
d5fe8f0cab97c18b97d30beb533be6dc9ebaa2b2; mounted tools baseline
e2237b9260e1aed8d8958a00088425c88cfc3b9d. New tools
7f64ce9950cadca48c980cf3b4276f3f1192af78 committed first. No push.
Single Codex writer, zero Claude calls; [agent workflow](../AGENT_WORKFLOW.md).
The previous turn directly matched the identity selector. This turn recovers
the complete next routine, but does not claim it is byte-exact or close the
wider Game goal.

## Complete Recovery, Matching Still Open

Recover func_15084044, VA 0x15084044..0x1508434C,
ROM 0xB14F4..0xB17FC, in conker/src/game/generated_AEB40.c.
Replace the zero-return placeholder with s32 (u8 *actor, s32 channel).
The original spans 194 words/776 bytes. The complete semantic C emits 192
words/768 bytes in the existing O2/g3 profile and fits the same slot with two
padding words. The frame is retail 0x60; saved S0..S5/RA, failure local at
SP+0x48, and reference-pointer spill at SP+0x30 are recovered. There are
130 real word differences, not two isolated scheduling differences. No new
guards, pools, compiler profiles, layout or symbol assignments.

- Read unsigned parent byte +0x65. A nonzero parent selects the config pointer
  at D_800CC0E8 + parent*812; this is the one-based actor pool's +0x144 field.
  A zero parent selects actor+0x144. The local 812-byte ResourceParent15084044
  type describes the existing alias; it does not allocate another actor pool.
- Read resource identity through actor+0x2C4 and the word channel argument.
  Config NULL defaults to mode zero; config+0x10 is masked by three. Identity
  zero forces mode two, including when the config requested mode three.
- The channel pair is at actor+channel*8+0x28C/+0x290. Read the config and
  identity before the complete-pair gate. A pair with both pointers present
  returns zero without reading the resource/count/size tables. An absent
  D_800D19A0[identity] also returns zero.
- Mode zero shares the cached resource pointer into both slots and increments
  the live byte reference count by two, preserving byte wraparound.
- Mode one preserves an existing private first pointer and mirrors it into
  the second slot. Otherwise, zero references share both slots/count+2;
  nonzero references allocate 16*u16 units, publish first before testing the
  result, and copy the live resource pointer. Allocation failure returns one
  and mirrors NULL. Keep the repeated slot load and fallback branch.
- Mode two traverses the two buffer words. It replaces NULL/shared pointers,
  and splits a second pointer that equals the first after the first update.
  Each iteration reads the live reference count and unsigned size. First
  allocation failure stops without clearing the pre-existing second slot.
  Second allocation failure frees a private first pointer, or decrements its
  shared byte count, then clears first. Preserve helper-induced mutations and
  cleanup order rather than replacing this with an idealized two-allocation
  algorithm.
- Mode three leaves incomplete pairs alone and returns zero. Calls retain
  allocate_memory(size,1,2,2), bcopy(source,destination,size), and
  func_10004074(first). No shared declaration/header or caller body changes.

The early draft emitted 191 words/frame 0x70/179 differences. Local source
experiments recovered the 0x60 frame and private slots without word patches.
Physical declaration order matters for the failure local. The selected body
is QUALIFIED in tools/experiments/game_resource_buffers_candidates.py;
default compile/install and CLI select it, while --variants retains bounded
reproducible alternatives, including rejected over-slot bodies.

## Fresh Qualification

tools/tests/test_game_resource_buffers.py has eleven final passing tests:

- 7,424 independent-reference cases/14,848 original-C guest executions:
  every identity and reference byte independently, all modes, nine slot
  patterns, four allocation-result patterns, byte-count boundaries and two
  stack phases. The boundary product reaches 172 original words. Do not
  claim execution coverage of all 194 words or asynchronous fallback paths.
- 896 cases/1,792 executions cover parent 0/1/26/128/255, channels 0/1/3,
  config high bits/NULL, resource NULL, zero and unsigned halfword size
  boundaries, and allocator/copy/free mutations to tables and slots. Copies
  above 64 bytes use an explicit record-only callback; large payload copying
  is not validated by that size-argument check.
- All 3,632 access-fault pairs in the selected traces fire the requested gate
  and compare complete partial memory, access order and helper receipts.
  The hook-backed original/C runs compare full private memory and access
  order; return-time saved-register/GP/FPR checks use the proven guest runner.
  Fault-prefix behavior is an emitted-instruction property, not portable C
  fault semantics.
- Twenty-seven fresh original/compiler/padded links, three independent normal
  symbol sets and 43 reference cases exercise rebases, count/resource aliases
  into actor slots, and a complete-pair gate with tables unmapped. The initial
  alias fixture omitted relinking to its alias symbols; that was corrected,
  not accommodated by relaxing unmapped-read gates.
- Eight freshly compiled effective negatives discriminate the zero-ID mode
  override, count increment, allocation flags, copy size, failure result,
  freeing, clearing, and a wrongly cached source after allocator mutation.
- Actual native32 complete C and independent state reference pass 12,288
  cases each at O2 and O0, 24,576 total. Compare all actor/arena/count bytes,
  size/resource tables and complete call arguments. All identity/count bytes,
  parent-byte values, channel samples, widths and canaries are checked. A
  wrong shared-count increment fails. Native copies here are bounded to 32
  bytes and do not claim invalid-index, asynchronous or hardware behavior.
- Copied owner preprocessing/compilation/postprocessing gives no diagnostics.
  All 30 neighbors retain exact bodies, extents, relocations and normalized
  pools. Both real generated/layout padding routes retain all bytes and
  relocations outside this slot; guard history is unchanged.
- 144 cases/288 executions connect actual linked Init allocate_memory and
  bcopy code: 207 mapped helper words, 72 dynamically reached. Compare memory
  and traces after normalizing only the actual wrapper's saved continuation
  PCs, which differ because this Game body is nonmatching. A strict fixture
  initially tried raw equality of those return-address bytes. It now tracks
  actual wrapper save addresses/values; nothing else is normalized. The real
  wrapper forwards (size,1,2,0,2) to the bounded allocation core, not the
  earlier fixture's (size,1,2,2,0) assumption. Core/free remain callbacks;
  this does not qualify the actual heap or hardware.
- 576 cases/1,152 executions map the complete 104-word retail caller
  func_1503DA9C, VA 0x1503DA9C..0x1503DC3C, ROM 0x6AF4C..0x6B0EC.
  Sixty caller words are reached within present/missing-resource and
  zero-extra-count paths. Verify 576 actual callee invocations per form,
  actor/channel forwarding and failure propagation. Resource loading is a
  bounded callback; current generated_6A3D0.c caller remains a placeholder.
  No complete resource initialization or gameplay claim.

Pre-install full suite: eleven tests pass in 26.588s. Final post-install
suite: eleven tests pass in 26.772s. Earlier failures were fixture shape/
coverage expectations, alias-link omission, an oracle dispatch mismatch,
wrapper argument/return-PC assumptions and the overly strict linked symbol
order assumption described below; no shared oracle gates were disabled.
Shared consumer make tools-check and mounted standalone check_project_tools.py
both pass in WSL. The older standalone mirror's check_project_tools.py and
py_compile of the two new files also pass. No Claude calls, dependency
installation, broad regression re-run or runtime launch.

## Linked And Data Audit

make -C conker -j4 build/conker.us.elf progress.csv succeeds. Only the
relevant owner is compiled and postprocessed; no new owner diagnostics. The
known generated_12D630 duplicate recipe warnings remain. Do not call this
a warning-free full build.

ELF length stays 3,261,160 bytes. The complete file audit accounts for every
changed byte: 582 in this 776-byte slot and 38 in .symtab/.strtab, 620 total.
New references reorder existing symbols/strings. Existing structured ELF
metadata parsing verifies identical headers/section descriptors and complete
symbol/name multisets except func_15084044's size 12 -> 768. All other named
symbol values/extents/attributes stay exact. After checking that permitted
metadata ordering, every other ELF byte is exact. This is not a claim that
the raw symbol/string tables are byte-identical.

- Final ELF SHA-256: e8a9504c87c628ce552d6f752fe26c27f4fcaaf1651612a37f998c80ba8bf690.
- Owner SHA-256: 0f28b2e2a9e881932c7896087406cc359bfe7d70ad707caf5eda712abd472b95.
- Protected data: all 189,088 bytes/720 owners exact; SHA-256
  0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670.
- Guards unchanged: 5e50f8952c0e5d4ba39b7e9054b7ac5727517d021ba8e92d3b10c8a2f07b2f19.
- Conversion census unchanged: 32045cb144c96ede05faaa343ad9b6bae1c4de6c0d961973cfeda6e16e14bf5c.
- Rodata source, layout, tracked symbols and ignored auto assignments remain
  byte-identical. Baselines/receipts stay in ignored
  conker/build/game-resource-buffers-test; never replace baseline.json.

Fresh make -C conker match-progress NON_MATCHING=1:

| Section | Byte-exact | Address Drift | Different |
| --- | ---: | ---: | ---: |
| Total | 3,459 / 5,495 (62.95%) | 0 | 2,036 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 2,786 / 4,822 (57.78%) | 0 | 2,036 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

No matching or converted-function credit: this was already a C placeholder.
The root README's aggregate rows are already correct and remain unchanged;
all recovery narrative stays here and in concise documentation indexes.

## Ownership And Graph

Only two new tools files, the recovered owner, consumer gitlink and scoped
documents change. No shared parser/oracle/compiler/build edits. The older
standalone tools HEAD remains ddbdd16b53ce60b054fb6e11bf0649a41f48375a.
Copy only the two absent new paths, with hashes checked; its dirty entries
increase 279 -> 281, without overwriting or committing older work. Existing
game_owner_pool.py and node-effect test hashes remain unchanged.

Native graphify query func_15084044 --budget 650 succeeds. After code edits,
native graphify update . extracts two files but protectively refuses an
unsafe graph shrink from 39,699 to 17,917 nodes; retain the 19,398 nodes from
2,972 excluded-but-existing files. Preserve version/zero-node warnings;
no force, purge or installation. Consumer commit's detached rebuild is a
separate checkpoint: verify fresh log byte/UTC growth, a Rebuilt tail and
zero actual workers before ending the turn.

No sibling 64CBFDOGL change is applicable to this retail-only C recovery.
Release, saves, editor state and private inputs remain untouched.

## Continue Matching This Function

1. Keep the complete function and the eleven qualification gates; do not
   return to a stub or jump to an easier target to count a win.
2. Recover the retail opening allocation: actor retained in A2, mode in V1,
   config in V0 and cached source in A0. Current reuse assigns them
   differently and affects many instruction positions.
3. Match the mode-one post-copy common join and the mode-two cursor setup.
   Retail recomputes actor+channel*8; current IDO reuses the pair pointer.
   These control-flow/CSE differences account for the two-word length gap,
   but the measured 130 differences are not all independent schedules.
4. Preserve the already recovered frame/private offsets, live table loads,
   count/size widths, failure cleanup and original one-based parent alias.
   Do not use broad word replacement to make a semantic body appear exact.
5. Screen bounded source/lifetime/profile alternatives, then rerun the whole
   focused suite, linked/data audit and fresh matcher before counting a match.
   The complete caller/resource loading/heap/hardware/gameplay work stays
   separate and open. Keep the full Game goal active and keep authorized
   checkpoints committed tools-first, without pushing.
