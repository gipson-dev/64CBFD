# 1760 - Ballistic billboard motion direct C match

Verified: 2026-10-28. Target func_1514AF74, owner generated_176A00.
VA1514AF74..1514B034; retail ROM178424..1784E4.

## Complete direct C and arithmetic order

Replace the zero-return placeholder with s32 func_1514AF74(u8 *actor).
The first semantic candidate matches all 48 words /192 bytes directly under
the existing normal O2/g3 profile. Frame zero, two HI16/LO16 bindings for
f32 D_800BE9A4, zero guards, no added words, padding fields or profile changes.
Use the opaque byte-pointer interface already used by neighboring callbacks.

1. Capture old vertical velocity+0x50 and acceleration+0x4C before the
   extent stores. Damp billboard extents+0x2C/+0x30 as x-x*factor+0x150,
   preserving the separately rounded multiply and subtraction.
2. Use one current clock value for linear=oldVelocity*step and the sequence
   quadratic=((0.5f*acceleration)*step)*step. Add linear+quadratic first,
   then add that sum to position+0x38 and store the position.
3. Reread D_800BE9A4 after the position store. Advance the captured old
   velocity by acceleration*lateStep and store velocity+0x50.
4. Return zero if either damped extent compares less than 10.0; return one
   otherwise. Keep ordered rejection, including its unordered NaN behavior.

The velocity store is in the first size-test branch-delay slot, so it
occurs on both return paths. Store order is+2C,+30,+38,+50. All48 words
are dynamically exercised. The two clock loads preserve record/global
aliases, particularly when the clock aliases the newly written position.
There is no position-limit test and field+0x15C needs no mapping.

Do not integrate position using already advanced velocity, remove one
clock factor, fold the damping algebra, regroup the two additions or cache
the clock across the position store. Native controls include an explicit
cancellation witness: position 1e20, velocity -1e20, acceleration 6, step 1.
The recovered grouping produces 0; adding position+linear first produces 3.
These operations must retain their original float32 rounding boundaries.

Raw selected/original SHA256:
~~~text
8112df3b7e4f877bf49a0a730270b565b7248c21834ec8db2c2ea5f85e095d65
~~~

## Callback ABI and original dispatcher scope

The aligned retail census finds no direct JAL/tail J and one pointer at
ROM22E890 /VA80089DD0, slot28 of the 44-entry D_80089D60 table. The complete
retained table remains byte-exact. Original func_1513CFE4 indexes it using
actor+0x71, passes the actor in A0 and treats the result as a boolean that
can request post-callback processing or cleanup.

The current dispatcher C/ELF definition remains an unchanged three-word
zero-return placeholder. Keep original execution and production-stub
evidence separate; no dispatcher restoration or additional credit is claimed.
The full 195-word original body is checked against frozen ASM and retail.
1,536 connected cases exercise 116 of those words with animation-rate zero:
active/timer gates, signed lifetime, optional pre-callback mutations/results,
the actual slot28 call, both color flags, optional post-callback rescue and
release. Other animation paths and provider bodies remain outside this
bounded integration; no live gameplay acceptance is inferred.

## Fresh focused qualification

Both tools copies pass eight fresh canonical_v2 methods and shared project
tool checks in 4.387s /4.368s. An initial generated
receipt expression had an extra parenthesis and stopped at import, before
any tests ran. Correct it, check both modules with ast.parse through
structured process arguments, preserve the failed receipt, and retain the
strict compiler flags. The recovered C and prepared objects are unchanged.

- 912 guest cases cover signed zero, subnormals, infinities, quiet NaNs and
  values below/equal/above 10.0. Independent GNU links alias the clock to
  all 88 aligned record words. Compare complete private RAM/GPR/FPR/HI/LO,
  condition, events, calls, visits and traces with retail and an independent
  separately rounded reference. Verify all 48 target words, both clock reads
  and the position-before-velocity store order.
- Native32 O0/O2/O3 with trapping UBSan each pass 182,272 positive cases.
  Use valid float storage and byte views, all 88 clock aliases plus a separate
  global, raw patterns, complete storage fences and an explicit cancellation
  witness. Twelve wrong C variants fail effectively. Only the four output
  cells allow NaN-class comparison; all other cells stay bit-strict. No
  MIPS NaN payload, FCSR, EPC or exception-hardware emulation is claimed.
- 324 fired access-prefix pairs preserve full private state, trace, fault PC
  and branch-delay ownership. A missing+0x15C mapping confirms the absent
  height-limit dependency. Three independent GNU layouts pass 24 cases,
  checking both address bindings and signed low-half carries. Three raw/
  binding and six whole-image corruptions fail closed.
- An actually compiled cached-clock variant is rejected under a real GNU
  alias at actor+0x38. The recovered routine writes velocity 7.0 while the
  cached-clock variant writes 3.0 after the position changes the live clock.
  The negative fails by value, without an unmapped-read shortcut.

Installed copies pass two fresh owner/image methods and reuse six semantic
methods only after exact input/module/qualified-artifact identity. Routine
Claude calls: zero. Preserve the source’s complete integer return contract
without claiming the unfinished production dispatcher works.

## Actual Make, image and progress

The owner contains 36 compact functions, including one unchanged GLOBAL_ASM
func_1514C678. Preserve all 35 other bodies, relocation bindings and pools.
The actual five-command asm-processor/IDO/postprocess/padder/GNU Make route
reproduces the qualified object byte-for-byte. Production exits zero in
0.575s. Selected diagnostics are empty; the complete owner’s old
func_1514BF50(arg0) pointer/integer warning only moves 196->205. Its wording
is unchanged after normalizing source label and line number. The inherited
duplicate generated_12D630 Make recipe warning remains.

The entire adopted ELF equals the independent 139-byte prediction:
138 target-code bytes and one size byte12->192, zero exclusions. All 6,056
function addresses, 6,055 other bodies and every other named definition stay
fixed. Protected Game data remains exact across 720 owners /189,088 bytes.
The current caller’s 12-byte placeholder, map, inventory CSV, shared headers
and guard manifest are unchanged.

ELF SHA256:
~~~text
d677fb3c7d9e215e98dacfe782aa87813510f6516715e95b6be6b1f8fdd730fe
~~~
Native CRLF guard SHA256 (Git-normalized LF unchanged):
~~~text
f867c3817abab6b6ef822343afa48a4b188e7067ce1d4c69a078b54a6f4b4c40
~~~

Seal 16,227 Native/cache inputs and 216 focused inputs. The first recount
correctly printed the new live totals, then caught a stale expected count
in its saved assertion. Preserve its script/log/receipt and rerun the
corrected recount_v2 against the same captured Native ELF. No production
source or object changes were needed. The actual measured result is:

| Section | Exact C functions | Different | Drift |
| --- | ---: | ---: | ---: |
| Total | 3,838 /5,506 (69.71%) | 1,668 | 0 |
| Init | 492 /492 (100.00%) | 0 | 0 |
| Game | 3,165 /4,833 (65.49%) | 1,668 | 0 |
| Debugger | 181 /181 (100.00%) | 0 | 0 |

Only func_1514AF74 becomes exact. Converted totals stay fixed. Threshold
4,130 leaves 292 more matches to 75%. Remaining source shapes: 1,539
placeholders, 120 semantic/other definitions and nine unlocated entries.
Typed func_151725FC and NULL factory func_1518F5D0 remain uncredited.

Predecessor consumer 4d04295df2618e11cb70c5d3d9fa6095e6bc2748 and tools
39c63ca7ce3538967db54f5ea0824fcdcdd0ce17. Tools are banked first at
4e8fbb1e7c38d582c7e7407db10dac562ee5dea6, then source, consumer pin and
measured documentation. Preserve the older mirror’s 1,730 inherited dirty
paths plus two new tools files. No push. Root README changes only its two
aggregate matching rows and snapshot verification date for the October 28
rollover. Detailed recovery notes remain here.

Refresh ten changed C/Markdown/tool sources structurally and preserve every
prior node and valid directed confidence/context relationship. Validate
the s32 return, u8-pointer parameter and leaf body against source/object
evidence; add no synthetic dispatcher/helper call. Outside freshness and
communities remain historical, with no full-corpus extraction or global
clustering/centrality claim. Receipts and the independent final audit live
under conker/build/game-ballistic-billboard-gate-match/.

Next inspect func_151DD3A0 with a fresh frozen predecessor and caller/ABI
audit. Keep func_1514E920 private and uncredited. The 75% goal remains active.
