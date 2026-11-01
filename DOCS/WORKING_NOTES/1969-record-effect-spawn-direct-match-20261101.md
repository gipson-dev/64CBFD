# 1969 - Record effect callback recovered directly from C

`func_15014094` in `conker/src/game_40490.c` now emits all **44 retail words**
with its original **104-byte frame**, five call relocations and **zero guards**.
The actual production Make, literal full-image prediction and fresh Native
ELF recount pass: **4,037 / 5,507 (73.31%)** total, Game **3,364 / 4,834
(69.59%)**, zero address drift, 1,470 still different. The 75% threshold is
4,131; **94 more** exact functions are needed. The wider goal remains active.

## Recovered behavior and interface

Retail span `0x15014094..0x15014144`, ROM `0x41544..0x415F4`, owner
`game_40490`. Set record byte `+0x16` bit 2; snapshot the record pointer,
query result from `func_15144598`, positive floating zero and the result of
`func_1510FD20` in a 0x34-byte local payload. Clear payload byte `+0x2C`.
The two coordinates passed to the latter helper are signed halfwords at
record `+0` and `+4`, read after `func_1510F800(0)` can change them.

Create a type-0x21 effect through
`func_15149130(300, -1, 33, -1, 0, 0, (struct37 *)52, 255, 1)`.
On success copy all 52 payload bytes to effect `+0x28`; on failure skip it.
Retail intentionally leaves the rest of this local payload untouched. The
previous reconstruction added `bzero` and forced `return 1`; both changed
retail behavior/code generation. Those additions and the obsolete commented
reconstruction are removed. Record/effect names and comments describe the
known fields without assigning unsupported meanings to the untouched bytes.

The existing `s32` callback declaration is retained with no explicit return.
The original dispatcher `func_1501396C` passes its live A0 and overwrites V0
with 1 after the callback. The callback result is never used on this route.
This is an ignored-result ABI recovery, not a portable guarantee of a defined
return value. Native tests ignore it. A plain void definition emits 43 words;
the retained non-void fallthrough emits the exact 44-word retail body.

Aligned ROM census: no direct JAL/J encodings, one pointer literal at
`0x2279D0` (`D_80082ECC[17]`). Source/ASM table references and the complete
16-word original dispatcher were reviewed. No arbitrary dynamic-code or
whole-game runtime coverage claim is made.

## Qualification

- Original assembled object and isolated C have identical complete raw payload
  and relocations. Raw SHA-256:
  `d12462835f7e20a840db166afe576c608aef6d4d998c67554175594c1d6841a7`.
- Full copied owner and real padded owner preserve all **31 neighbors** and
  normalized pools. Compiler diagnostics stay zero. The production guard CSV
  and shared declarations are unchanged.
- **1,728 guest cases / 3,456 executions** across three independent GNU-linked
  layouts cover all 44 target words, signed boundaries, positive/negative zero,
  helper mutations, allocation failure/success and seeded untouched payload.
  Complete public memory, call arguments/payloads, saved state, and original/C
  machine memory/register/access traces agree.
- **18 access-prefix cuts / 36 executions** compare memory and access trace.
  They do not establish portable C fault behavior or complete hardware fault
  register/PC equivalence.
- The full original dispatcher passes **576 executions** with four callback
  return poisons. Its actual argument setup and unconditional return-1 consumer
  are executed; no reliance on the callback's incidental V0 remains.
- The original **49-word factory** and **11-word memcpy** pass **128 cases /
  256 executions**. All 47 factory words reachable with this target's fixed
  arguments and all 11 copy words execute. Two alternate-allocator words are
  unreachable with arg4=0. Allocator arguments are `(35, 1, 92, 1, 255, 1)`.
- Native32 **O0/O2/O3** each pass **192 cases / 1,536 executions**, UBSan,
  complete record/destination canaries and seven effective controls: added
  clear, omitted record flag, unsigned coordinate, wrong payload flag value,
  wrong copy length, wrong effect kind and an incorrectly cached coordinate.
  Native tests check initialized payload fields, not the values of untouched
  native stack bytes. Guest-only stack mutation fixtures are excluded.
- An initial wrong-offset native control was ineffective because a reused
  stack slot could already hold zero. It is replaced by an explicit wrong flag
  value; all seven final controls are effective. Initial fixture errors in link
  alignment and dispatcher frame accounting were fixed before acceptance.
- Five fresh public tests and standalone shared tool checks pass in **both**
  tool copies before and after installation. The older mirror's existing dirty
  work remains untouched; only these four new tool files are added there.

## Actual Make and literal whole-image closure

The five actual Make compile/postprocess/pad/assemble commands produce exactly
our qualified padded object. A private full link is byte-for-byte equal to an
independent prediction derived from the frozen predecessor ELF and retail slot.
Production Make reproduces the same image. There are **zero excluded bytes**.

This removes `__retail_overflow_func_15014094` (184 bytes), its obsolete local
file symbol, and 33 string-table bytes. Seven later private definitions shift
by 184 bytes. Four existing trampolines retarget: `func_1504ADD0`,
`func_1505210C`, `func_150768DC`, `func_150A7D00`. ROM alignment moves the two
absolute overflow cursor symbols by 176 bytes. The ELF shrinks by 248 bytes.
The predictor covers all payloads, headers, program headers, symbol and string
tables and required trampoline changes. Complete named-definition multisets
are checked. All **6,045 canonical function addresses** remain fixed; **6,047
other bodies** are unchanged. The total executable inventory falls from 6,053
to 6,052 only because the obsolete private definition disappears.

The private link map is normalized only for its owned object/output paths and
must equal the actual production map. This map comparison is separate from the
independent literal ELF prediction. All **189,088 protected Game bytes across
720 owners** remain exact; no unplanned dependent objects change.

Production ELF SHA-256:
`02f7f9a233d6ef184772a7fcb9e4aeb2f18a2dab8062e32cc627e430c603e5cf`.

## Retained artifacts and continuation

Stage: `conker/build/game-record-effect-spawn-15014094-match/`.
See `production.json`, `native-install.json`, `prepared-artifacts.json`,
`private-owner-qualification.json`, `private-guest-runtime.json`,
`private-helper-runtime.json`, `private-native-runtime.json`,
`private-image-qualification.json`, `caller-census.json`, and both copies'
preinstall/installed test receipts. Public tools:
`experiments/game_record_effect_spawn_match.py` and its three test modules.
Original retail assembly is retained. Root README contains aggregate rows only.

Descriptor pointer-window screening (`screen26-results.json`) compiles all 12
forms but yields 42..43 words and 33..34 differences: none improves the retained
46-word/frame8/13-difference candidate. It stays private and uncredited.
`func_151F8870` is identified as handwritten bitstream assembly with a special
register interface and trapping ADD/SUB; defer it to assembly restoration.
Continue remaining compiler-generated Game functions, such as `func_15014144`;
its original 55-word callback is the adjacent bounded follow-up. No Claude call
was needed for this routine. Host port, editor, frozen Release and earlier
archives are unchanged. The prior goal turn completed verified build cleanup;
this turn advances the actual production match count by one.
