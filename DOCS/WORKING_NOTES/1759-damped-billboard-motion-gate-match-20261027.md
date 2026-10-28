# 1759 - Damped billboard motion gate direct C match

Verified: 2026-10-27. Target func_15149C58, owner generated_176A00.
VA15149C58..15149D18; retail ROM177108..1771C8.

## Complete source and interpretation

Replace the zero-return placeholder with s32 func_15149C58(u8 *actor).
All 48 words /192 bytes emit directly from the existing normal O2/g3
profile. Frame zero, two HI16/LO16 bindings for f32 D_800BE9A4, zero guards,
no inserted words, profile changes or padding fields. The initial semantic
statement shape already matched. The final source clarifies its comment;
initial-fit/ preserves the earlier comment and corresponding outputs.

The recovered sequence is:

1. Reduce f32 fields+0x2C and+0x30 by their respective products with the
   factor at+0x150. Keep each multiply and subtraction separately rounded.
2. Add field+0x4C times the current D_800BE9A4 to field+0x50.
3. Reread D_800BE9A4, then add the updated field+0x50 times that live clock
   to position field+0x38.
4. Return zero if limit+0x15C is less than the updated position. Otherwise
   return zero if either damped extent is less than 4.0; return one otherwise.

The existing geometry routines func_15140190/func_15140410 in
conker/src/game_169510.c use+0x2C/+0x30 as the billboard width/height extents
and+0x34/+0x38/+0x3C as translation. This supports the comment and vertical
integration interpretation without inventing a new global structure layout.
The opaque u8 record interface follows neighboring recovered callbacks.

The original loads acceleration+0x4C before the extent stores, captures the
old position before the velocity store, rereads the clock after that store,
and captures the limit before writing the new position. Preserve actual
writable record/clock aliases. Do not cache the timestep, factor the damping
as x*(1-factor), or rewrite the rejection conditions as >= conjunctions:
rounding, live aliases and unordered NaN comparisons can distinguish them.

Raw selected/original SHA256:
~~~text
f1d85245314c4eaee5e7980b2cbbdaa4cfe95227c56d5888843933412c1a24ca
~~~

## Callback registration and the original dispatch path

The aligned retail census has no direct JAL/tail J and one function pointer
at ROM22E860 /VA80089DA0: slot16 of the 44-entry D_80089D60 table in
asm/data/22E730.rodata.s. That complete retained table remains retail-exact.
The original func_1513CFE4 dispatcher indexes it with the byte at actor+0x71,
passes the actor in A0 and uses the returned V0 boolean to request cleanup.

The current conker/src/game_169510.c dispatcher definition is still a
zero-return placeholder. It remains unchanged and uncredited. An initial
canonical test incorrectly assumed its full original body was retained;
the frozen ELF disproved that assumption. Correct the test to validate all
195 original words against the frozen original ASM and retail ROM, while
separately checking the unchanged three-word retained placeholder. Preserve
the failed receipt. No dispatcher restoration or extra matching credit is
included in this change.

1,536 cases map the complete 195-word original dispatcher and the retail/
rebuilt target. Cover active/timer gates, signed-short lifetime updates,
optional pre-callback changes/results, the actual slot16 indirect call,
boolean-driven death state, both color flags, optional post-callback rescue
and release. The animation-rate field is zero in this bounded integration;
116 original dispatcher words are visited. Do not claim the remaining
animation paths were executed. Pre/post callbacks and release are bounded
providers, separate from full provider or live gameplay acceptance.

## Fresh focused qualification

Both tools copies pass eight fresh canonical_v3 methods and shared project
tool checks in 4.217s /4.216s. Installed copies pass two
fresh owner/image methods and reuse six semantic methods only after exact
sealed input, module and qualified-artifact identity.

- 912 guest cases cover signed zero, subnormals, finite rounding boundaries,
  infinities, quiet NaNs, threshold equality and values around 4.0. Independent
  GNU links alias the clock to all 88 aligned record words through+0x15C.
  Compare full private RAM/GPR/FPR/HI/LO, conditions, events, calls, visits
  and ordered traces with retail and an independent rounded reference.
- All 47 feasible target words are visited. The duplicate constant load at
  VA15149CD8 is unreachable from entry but remains part of the exact 48-word
  body. Preserve both clock reads and store order+2C,+30,+50,+38.
- Native32 O0/O2/O3 with trapping UBSan each pass 182,272 positive cases using
  valid float storage and byte views. Cover all 88 clock aliases plus a
  separate global, raw float patterns and complete storage fences. Only
  the four written output cells allow NaN-class comparison; other cells
  remain bit-strict. Ten wrong C variants fail effectively, including
  factored damping, cached time and positive conjunctions. No MIPS NaN
  payload, FCSR, EPC or exception-hardware emulation is claimed.
- 378 fired access-prefix pairs preserve complete private state, trace,
  fault PC and branch-delay ownership. Three independent GNU layouts pass
  24 cases, checking both address bindings and signed low-half carries.
  Three raw/binding and six complete-image corruptions fail closed.
- An actually compiled cached-clock variant fails by its updated record
  value under a real GNU alias at actor+0x2C, without an unmapped-read
  shortcut. The target and complete owner are independently recompiled.

Routine Claude calls: zero. Full gameplay and the unrecovered dispatcher’s
production behavior remain outside this function’s matching credit.

## Actual Make, complete image and measured count

The owner contains 36 compact functions, including one GLOBAL_ASM routine
func_1514C678. Preserve all 35 other functions, their relocation bindings,
pools and the unchanged assembly routine. Its actual five-command
asm-processor/IDO/postprocess/padder/GNU Make route reproduces the qualified
object byte-for-byte. Production Make exits zero in 0.571s.

Selected IDO diagnostics are empty. The complete owner’s existing pointer/
integer warning on func_1514BF50(arg0) remains the sole warning; its line
moves 185->196 as the target expands. Compare the same diagnostic after
normalizing only the source label and line number. The inherited duplicate
Makefile generated_12D630 recipe warning remains. No new warning is added.

The entire adopted ELF equals the independent 132-byte prediction:
131 target-code bytes and one size byte12->192, zero exclusions. All 6,056
function addresses, 6,055 other bodies and every other named ELF definition
remain fixed. Protected Game data stays exact across 720 owners /189,088
bytes. The map, inventory CSV, shared headers and guard manifest remain
unchanged. The current caller placeholder remains exactly its old 12 bytes.

ELF SHA256:
~~~text
a901623f145f33570885caaa08107f880fb7ab95eab873ab53d16c88eebbfa9c
~~~
Native CRLF guard SHA256 (Git-normalized LF content unchanged):
~~~text
f867c3817abab6b6ef822343afa48a4b188e7067ce1d4c69a078b54a6f4b4c40
~~~
Seal 16,222 Native/cache inputs and 216 focused inputs, including the original
dispatcher, its retained source/object and callback table. Recount the
captured adopted Native ELF with the unchanged inventory:

| Section | Exact C functions | Different | Drift |
| --- | ---: | ---: | ---: |
| Total | 3,837 /5,506 (69.69%) | 1,669 | 0 |
| Init | 492 /492 (100.00%) | 0 | 0 |
| Game | 3,164 /4,833 (65.47%) | 1,669 | 0 |
| Debugger | 181 /181 (100.00%) | 0 | 0 |

Only func_15149C58 becomes exact. Converted totals stay fixed. Threshold
4,130 leaves 293 more matches to 75%. The remaining source screen contains
1,540 placeholders, 120 semantic/other definitions and nine unlocated
entries. Typed func_151725FC and NULL factory func_1518F5D0 remain
placeholders and uncredited.

Predecessor consumer 4b59ced6bff473609e7a9592e8787dd86e2ced46 and tools
ad559bc41fa547b59e20c3ca38d4da9210105c76. Bank tools first at
39c63ca7ce3538967db54f5ea0824fcdcdd0ce17, then the target source, consumer
pin and measured documentation. Preserve the older mirror’s 1,728 inherited
dirty paths plus two new tools files. No push. Root README changes only
its two aggregate matching rows; detailed recovery updates stay here.

Refresh ten changed C/Markdown/tool sources structurally, retaining every
prior node and still-valid directed confidence/context relationship. Verify
the target’s s32 return and u8-pointer parameter against the actual source;
it is a leaf, so do not invent a helper or production-dispatch call edge.
Outside freshness and communities remain historical, with no full-corpus
extraction or global clustering/centrality claim. Graph receipts and the
independent final audit live in conker/build/game-damped-motion-gate-match/.

Next inspect func_1514AF74 in generated_176A00 using a fresh frozen
predecessor and caller/ABI audit. Keep func_1514E920 private and uncredited.
The 75% goal remains active.
