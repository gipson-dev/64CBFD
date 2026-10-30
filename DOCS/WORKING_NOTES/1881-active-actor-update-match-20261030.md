# Note 1881: active actor update loop match

2026-10-30. `func_1502378C`, owner `generated_49D30`, replaces its zero-return
placeholder with `void func_1502378C(void)`. Its **54-word /216-byte body** at
VA `0x1502378C..0x15023864`, ROM `0x50C3C..0x50D14`, matches after two guarded
independent initialization words are rescheduled. The complete slot is **57 words**:
three existing alignment words through VA `0x15023870`, ROM `0x50D20`, also remain
exact. There are no instruction insertions or omissions. Tools commit: `585829b51a4d23e97b17615955fb18ba1027da21`.

## Recovered update sequence

When `D_800C3654[0]` is nonzero, call `func_1504A730` and leave the ordinary scan.
Otherwise, walk exactly 25 `struct127` records in `D_800CC2D0`, at stride `0x32C`.
For each record whose `interaction_state` is nonzero:

1. Write its index to the byte `D_800C3E78` before the first helper call.
2. Call `func_15022998((s32 *)actor)`, then `func_1507E73C(actor)`.
3. Test `func_150229E4(actor)` for any nonzero result, including a negative word.
4. On success, call `func_1502178C(actor, 0, -1)`, `func_150627D4(actor)` and
   `func_1507FEA0(actor)`, then write 1 to the existing `unk2FF` field.

Inactive records still advance both the counter and pointer. The ordinary path
finishes with `func_15061B4C()`. Helpers may change later records, the current
index and mode byte; the next record's activity is read at its own iteration.
The mode is selected only at entry. The update-byte store remains after the
last helper, so it overwrites a helper's earlier write to that byte.

The no-argument, void interface follows the original caller: it discards V0,
and the routine has no defined result assignment. The 48-byte frame saves
S0/S1/S2/S3/S4 at SP+24/+28/+32/+36/+40 and RA at SP+44. All incoming callee-saved
registers, GP, SP and preserved floating registers survive the modeled calls.

## Compiler fitting and normalization

The owner already uses `-O2 -g3 -Wo,-loopunroll,0 -mips2 -o32`; that profile and
all shared headers remain unchanged. The initial default-profile owner screen
failed an existing neighbor's span check. Repeating under the actual Make profile
reproduces the complete owner, all 56 neighbors and their pools.

The initial semantic draft has seven register/scheduling differences. A byte-sized
loop bound recovers the saved-register allocation and reduces this to words 19/20:

| Word | Raw C | Retail |
| --- | --- | --- |
| 19 /offset `0x4C` | `addiu s2, zero, 25` | `addiu s4, zero, 1` |
| 20 /offset `0x50` | `addiu s4, zero, 1` | `addiu s2, zero, 25` |

These independent writes initialize different registers, and both complete before
the first loop read or call. The remaining 52 body words and all 14 relocations
already agree. Two exact-word guards swap only these initializations. Four actual
padder controls reject wrong preimage words and bindings. This is a normalized
match, not direct raw-C byte identity.

## Qualification

Ignored evidence: `conker/build/game-active-actor-update-1502378C-match/`.

- Guest: **792 cases /2,376 executions** compare original, raw C and normalized
  code against independent public-memory, call-argument, call-order and live-index
  expectations. Complete cross-image RAM, register state and access traces agree.
  Coverage includes every target word and all 19 words of the original
  `func_15022998` dispatcher, including null table entries and type-4/type-27
  callbacks. Other update helpers and callback bodies use explicit opaque effects;
  their complete game implementations are not claimed as qualified.
- Prefixes: **95 access cuts**, including two delay-slot cuts, retain identical
  normalized/original state and actual PC/delay context. These qualify emitted
  instruction order, not portable C fault behavior. **18 guest alias cases**
  overlap the global index with actor storage or the mode byte. **36 rebase
  cases** use three GNU-linked symbol layouts, including signed-low-half carries.
- Caller: the sole aligned JAL is ROM `0x462F4`, VA `0x15018E44`; there are no
  aligned literal pointers. The original 13-word window at
  `0x15018E28..0x15018E5C` in `func_15018DFC` passes **144 cases**. It covers the
  gate exit at `0x15018E68`, selector 0/1/255, alternate helper path, target mode,
  actor patterns, helper effects and both stack phases. The current caller in
  `conker/src/game_45B80.c` corroborates the no-argument, ignored-return interface.
  The complete parent and its other helpers are not executed or credited here.
- Native32: **396 cases per O0/O2/O3 profile** pass with trapping UBSan and the
  real SDK `struct127`. Assertions verify stride `0x32C` and field `0x2FF`.
  Every pool byte, the 26th canary record, neighboring mode bytes, global index,
  call arguments and ordering are checked. Guest-only global aliases are excluded.
- **13 IDO and 13 native semantic controls** are effective: wrong mode, short/long
  scan, wrong stride/activity/index, missing index, inverted query, wrong reset
  argument, wrong/early update byte, missing final helper and reordered calls.
  Each fails through an actual semantic mismatch; build/interpreter failures are
  not accepted as successful controls. Both tools copies pass eight fresh canonical
  checks and shared tool checks. Production repeats two installed checks per copy
  and reuses six unchanged checks only under complete input/module/artifact
  fingerprints, including the existing no-unroll compiler adapter.
- Owner/Make: all **56 neighbors** and pools remain fixed, and the actual
  **three-command Make recipe** reproduces the padded object. Target, owner and
  command diagnostics are empty. Inherited duplicate-`generated_12D630` warnings
  appear in the dry-run plan. Two mechanical test-template length/count errors
  were corrected before canonical qualification; production code was unaffected.
- Image: the independent whole-image prediction equals the private link and
  production ELF: **171 changed bytes =170 code +1 symbol extent**, metadata 0,
  exclusions 0. All **6,055 other bodies** and all **6,056 addresses** stay fixed.
  Protected Game data remains exact across **189,088 bytes /720 owners**. The C
  inventory CSV and all inherited guard rows remain unchanged.

Raw C SHA-256: `4c2483c85c70abd830138f1cb4f7a0490a49fcb3baf07731a07192ec196df0d8`.
Owner source SHA-256: `c60d92ff3272ecc7ba7bd08f9bf6ee78fd2c562f6c52e9374a4d678020d52661`.
Padded owner SHA-256: `b75d8bba8b241bfb8bf988e27bfcd2b684de2899df5feaf0b1c19e5a3d9694f6`.
Adopted ELF SHA-256: `6a177d64e494d6059d313a8114d060a5c0d3247d2680071c9661bd81a5575572`.

The fresh adopted-image recount is **3,958/5,506 (71.89%)** total exact C and
**3,285/4,833 (67.97%)** Game, with zero drift. Init stays 492/492 and Debugger
181/181. The 75% goal remains active: **172 more** matches are needed to reach
4,130/5,506. Next private screen: `func_1500727C`. The README changes only its two aggregate
matching rows. Detailed updates stay here and in concise status indexes. Graphify
uses the scoped eleven-file AST refresh, preserving old nodes and still-valid
relationships while retiring the obsolete s32 return-type edge. No full-corpus
extraction, global clustering, gameplay or hardware acceptance is claimed.
