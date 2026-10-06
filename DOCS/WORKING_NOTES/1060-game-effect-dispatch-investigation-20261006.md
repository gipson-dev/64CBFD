# Game Effect Dispatch Investigation

Date: 2026-10-06
Baseline: `e5bf72e0` ([Note 1059](1059-game-position-projection-match-20261006.md)).
Projection match banked after the paused regression run finished successfully.
Continue the full Game matching goal. This next-function work is not installed.

## Retail Contract

`func_15141A7C`: **100 words / 400 bytes**, frame **0x48**, VA
**0x15141A7C..0x15141C0C**, ROM **0x16EF2C..0x16F0BC**, owner
[`game_16EE20.c`](../../conker/src/game_16EE20.c). The known caller
`func_15071DC8` forwards actor `D_800D154C` and context `D_800D1580`, ignoring
the result. Investigate an effect-only void ABI; do not infer a native scalar
return from incidental guest V0.

If byte `D_800BE616` is nonzero, skip all dispatch. Otherwise:

1. Classify actor through `func_15141C0C`, then test the corresponding
   `D_8008A084` callback. If present, read the live actor+0x184 word, mask it
   through `func_1510F8CC`, and classify it through `func_15141CC0`. Reload the
   callback entry and call it with classification and actor.
2. Unless its signed result is -1, test the matching `D_8008A0B4` callback.
   Positive signed count calls `func_15141E38(actor,index)`; otherwise reload
   the callback and call it with actor, context and zero. No extra bounds or
   second null checks absent from retail.
3. Read the live actor+0x2F4 list head. Search for key **0x1A**, passing the
   address of the private cursor at **SP+0x3C** to `func_1514ECE0`.
4. For each returned node, read its record pointer at +0x10. Read the record's
   selector at +0x28 to test its callback, then **read the selector again**
   for the actual callback lookup. Forward actor, context and **signed s16**
   record+0xE. Counts do not gate this list-dispatch path.
5. After the callback, reload the live cursor/node and its next pointer at
   +0x14, update the cursor, and repeat the search. Preserve callback changes
   to links, record fields, tables and actor head; do not cache these values.

Retail data in `asm/data/22EB40.rodata.s` has **12 classifier callbacks** and
**21 callback/count entries**. Existing SDK declarations use s32 words and
`struct32`, not typed callbacks. Keep shared declarations and data unchanged;
adapt owner-local views/casts during future integration. The existing local
count helper is `s32 func_15141E38(s32,s32)`: reconcile the experiment's typed
pointer call locally rather than silently rewriting that helper's contract.

## Compiler Controls And Derivation

All experiments are ignored under
`conker/build/game-position-projection-test/next-effect-dispatch/`:

- `next-effect-dispatch.py`: table/record volatile reads and while/do-loop
  shapes, four SDK profiles: **32 controls**. Cached record selector emits
  **94 words/frame0x48/62 differences**. Repeated live selector gives
  **99/frame0x48/26 differences**; O2 gives98/97, O1/g3 gives109/frame0x38/108.
- `next-effect-views.py`: typed node/record and explicit table-pointer views,
  four profiles: **32 controls**. Typed views do not improve99/26. Named table
  locals instead expand the frame to0x50; this is not a retail-frame match.
- `next-effect-cursor.py`: head/tail assignments in call arguments and unsigned
  next-pointer representation, four profiles: **32 controls**. Best stays99/26.
- `next-effect-cursor-access.py`: private cursor write/read and next-field
  volatile access, two profiles: **16 controls**. Volatile cursor **write only**
  gives **100 words/frame0x48/21 differences** under O2/g3. Also forcing cursor
  argument reads gives101/55. No wholesale volatile-cursor qualification.

**112 control compilations**, empty diagnostics; overlapping forms are not
claimed as112 unique source shapes. The scratch compiler is borrowed from the
projection driver: standalone objects still label the screened body
`func_1514182C`, but link it at **0x15141A7C** with the correct retail helpers.
This does not edit or replace production projection source. Rename the label
and parameterize an actual maintained driver before integration.

Selected ignored source: `cursor-access-100-o2g3.c`. It explicitly writes the
next pointer through `*(u8 *volatile *)&node`, retaining all100 body words.
`next-effect-derive.py` derives all retail words from this compiled body:

- Swap S0/S1 only over **0x90..0x170**, after the category/classifier lifetime
  ends and before the unchanged epilogue restores saved registers.
- Restore three prefix branch/delay pairs at0x50/54,0xA4/A8,0xC8/CC, including
  their correctly adjusted branch destinations. Move the single actor-head
  load into the shared initial-query block without changing its live read.
- Permute initial-query words0xE4..0xF8 to the retail table/cursor/argument order.
- At0x160, store the cursor through SP+0x3C rather than its equivalent saved
  cursor-address register. At0x168, copy the live T8 next pointer to A0 rather
  than reloading the just-written private cursor slot.

The complete linked sequence equals **all100 retail words**: **79 direct /
21 proposed normalizations**. `derivation.json` records every expected/retail
word. This is **not an installed guard recipe**: HI16/LO16 metadata for moved
table-address pairs, actual object padding and owner integration remain.
No copied assembly, instruction insertion, source omission or guard-file edit.

## Bounded Guest Qualification

`next-effect-probe.py` independently compares full external storage, calls,
ordered accesses and saved-register/SP/RA state in compiled and retail bodies.
**13824 cases per two-body pairing**: every category, selected -1/0/5/20,
count -1/0/1, four list shapes, gate0/1, six mutation modes and two SP phases.
Mutations exercise changed links, actor heads, callback/count entries and record
selectors. Payload endpoints include -32768/-1/0/32767. The actual **3-word
mask** and **23-word list search** execute: **26 mapped /24 reached**.

Original99-word source passes with identical **full** traces and reaches99
candidate/100 retail words. The100-word source's first invocation fails the
full trace check at **case4**, after state/call agreement: it adds one private
cursor reload per advance. Do not describe that invocation as green.

The revised probe isolates only opcode **0x8FA4003C** at owner offset0x168:
each read must be exactly at initialSP-12 (frame0x48 plus cursor0x3C), and its
loaded bits must equal live **T8**, the value retail copies. Remove only that
proven extra read from trace comparison; all other reads/writes/calls must
agree. No blanket stack filtering. The100-word pairing then passes all13824
cases, reaches **100/100 target words**, and binds **13764 extra private reads**.
This is a narrowly explained compiler-access difference, not raw trace identity.

`next-effect-classifiers.py` connects original **45-word actor classifier** and
**57-word context classifier**, using their unchanged fixed switch tables from
verified Game data. The independent reference maps identity groups and world
overrides; it does not execute the candidate's classification instructions.
Initial **12288 cases** cover all identity bytes, six flags and eight world
values. Expanded **69632 cases** cover all256 identity bytes, all32 masked
contexts plus two high-bit inputs, and worlds0/2/20/25/39/47/66/0x80000000.
The99-word pairing passes; **128 helper words mapped /122 reached** in the
expanded run. Initial six-flag receipt is preserved separately. The100-word
pairing also **passes all69632 cases** with the same explicit private-read
boundary: **110976 extra private reads** bound to the cursor slot and live T8.
All other full traces, external storage and calls agree. It reaches **99/99
target words** in this connected run; the disabled-gate delay word is not
reached here, but the13824-case run separately covers all100 words.
Both terminal successful receipts are inspected before checkpointing.

Classifier callbacks, positive-count work and final effects remain bounded
mutation models, not restored implementations, native C or gameplay acceptance.
The switch/list instruction proof does not restore their own placeholder C.
These are ignored investigation scripts, not maintained acceptance tests.

## Current Audit And Resume

`next-effect-audit.py` verifies against **e5bf72e0**: all **6059 slots unchanged**,
all **10760 guards unchanged**, all four protected sections unchanged. Next
owner, projection source/tool/tests, shared headers and Makefile unchanged.
Production remains Game **2662/4791 exact (55.56%)**, **2129 different**,
zero drift; total **3335/5464 (61.04%)**. Converted counts/bytes unchanged.

**42 documents /3461 relative links /zero broken**; syntax and diff checks
pass. All required investigation sessions are terminal before checkpointing.

Continue with the100-word cursor-write candidate and21-word closed derivation:

1. Keep the completed raw/private-read/normalized proofs separate. Add
   maintained source/profile controls and actual-object relocation
   checks; use the real target label and existing SDK declarations.
2. Qualify actual32-bit native C, live table/record/list aliases, signed payloads,
   connected caller ABI, bounded loops/invalid targets and compiled negatives.
3. Prefer further direct source recovery where it preserves the retail contract.
   Otherwise derive relocation-aware expected-word guards from the proven closed
   transformations, not literal post-link addresses or inserted instructions.
4. Only then install the owner-local body/prototype, rebuild explicitly to the
   ELF, audit all slots/data/sections/warnings, run post-link retained tests,
   update aggregate progress and detailed DOCS, and commit the qualified match.

No source installation/count change, sibling source/build/save/frozen Release,
runtime launch, host adoption, hardware/gameplay acceptance or push change.
