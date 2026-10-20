# Actor Radial Point Direct C Match

Date: 2026-10-20. Consumer predecessor: `012e4764`; tools predecessor:
`9e5b77d`. Tools **5092f17** are committed first. No push.
This is verified progress toward the **75% total C-matching objective**,
which remains active and incomplete.

## Installed Recovery

Replace the false zero-return `func_150F2230` placeholder in
[generated_11C2B0.c](../../conker/src/game/generated_11C2B0.c) with its complete,
purpose-commented actor-offset wrapper. Keep the original address-based name.
Use the existing `struct127` actor and `struct17` three-float vector types.

VA **150F2230..150F22CC**, ROM **11F6E0..11F77C**: all **39 executable words /
156 bytes** emit directly from normal **IDO O2/g3**, with the original
**56-byte frame** and four original R_MIPS_26 bindings. The reserved retail
slot is **40 words / 160 bytes**, ending at VA **150F22D0** and ROM **11F780**.
Its last four bytes are unchanged alignment zeros, not executed instructions.
There are **no new guards or compiler-profile changes**.

Require the actor's +0x1D4 matrix pointer to be nonzero and the low nibble of
its +0x74 byte not to equal 15. A NULL matrix must skip the byte read entirely.
Initialize all three offset floats to positive zero. Take the RNG result's
low byte, pass it as a signed-short angle with radius 100 to `func_15143874`,
and let that helper fill X/Z while Y stays zero.

Only after the RNG and direction calls, reload the actor's matrix pointer
and select its **+0x4C0** transform. Transform the local offset into the
second local vector and pass that point, the zero-extended selector byte,
and the complete third argument word to `func_151C329C`. Do not repeat the
entry gates after a provider changes actor state. The wrapper consumes no
helper return value.

The original offset and result homes are **SP+0x2C** and **SP+0x20**.
The actor, byte and word parameter homes are SP+0x38, SP+0x3C and SP+0x40;
the byte reload is the big-endian low byte at **SP+0x3F**.

Express the matrix offset through explicit unsigned 32-bit address arithmetic.
The existing `struct255` is only a partial model prefix, not a complete host
allocation declaration. This recovery qualifies the prepared flat 32-bit ABI
and low-level vector views, not arbitrary-host portable ISO-C pointer layout.
Native tests use -m32/-fno-strict-aliasing and larger valid model backing.
A valid actor remains required; no new NULL-actor defensive behavior is added.

Add the matching local prototype in
[game_981E0.c](../../conker/src/game_981E0.c), whose existing C wrapper calls this
function. Preserve all **328 caller-owner functions**, bindings, pools,
linked content/metadata and normalized inherited diagnostics. Do not change
shared headers or other signatures.

## Qualification

[The focused helper](../../tools/experiments/game_actor_radial_point.py) pins
15 source/header/assembly/image/build inputs and retains the historical
predecessor files without advancing their hashes.
[Eight tests](../../tools/tests/test_game_actor_radial_point.py) pass in both
tools copies, with zero errors, failures or skips:

| Stage | Primary | Standalone Mirror |
| --- | ---: | ---: |
| Before installation | 27.914s | 20.831s |
| Installed source | 45.817s | 46.765s |

- **842 cases / 1,684 complete original-versus-C modeled phases**, including
  **1,140 active phases**, check all modeled state, independent provider
  contracts, complete output vectors and ordered actor reads.
  Execute all **39 body words**. The alignment word is not execution coverage.
- Exercise all **256 gate bytes** with present/NULL matrices, all 256 angle
  bytes, full-width RNG/parameter edges, selector narrowing, both stack
  alignments and matrix/tag changes during either/both RNG/direction calls.
  Two incoming-home redirects are explicitly guest-only probes.
- **840 native32 cases**, O0/O2/O3 with trap UBSan, check canonical field
  offsets, zeroed local vector, provider order, selector/word widths, late
  matrix selection and actor byte fences. Main providers are bounded contracts,
  not claimed native implementations of the actual transform/submission.
- **Ten compiled semantic negatives** all reach rejection code23: missing NULL
  gate, wrong nibble width/Y zero/angle/radius/output tuple/matrix offset,
  signed selector, narrowed word and early matrix capture.
  Correct a tautological first negative-control predicate instead of suppressing
  compiler warnings or treating compile failure as a semantic rejection.
- Scan all pristine functions for direct JALs and the ROM for literal pointers.
  The sole direct caller is **func_15071D08 at 15071D20**. Execute its complete
  original **12-word / 48-byte** wrapper in **64 phases / 128 executions**,
  including its delay-slot argument and current-actor global. All 12 words
  execute. The before-image caller itself is byte-exact; its typed C remains
  word/binding/pool-identical across all 328 owner functions.
- Three independent GNU call-symbol rebases pass **60 phases**, with the
  complete original/C words and output contracts agreeing.
- Execute the original **25-word direction helper** and **27-word lookup**
  in **512 phases / 1,024 executions**, covering all **52 helper words** and
  all 256 angles. An independent quadrant/index/sign reference uses the
  frozen **65-entry / 260-byte D_8009A220 table** from the predecessor ELF.
- Inspect the complete original 98-word transform and 271-word submission
  interfaces. Their full positive execution remains unclaimed.
  Seven strict-image negatives reject header, target/caller code, data,
  target extent, truncation and appended-byte corruption.
- Both shared tools checks pass; task files agree in both copies and all four
  Python files parse. Preserve all **1,490** older mirror dirty paths/statuses/
  hashes and its **ddbdd16** HEAD. Add only the two absent task files, leaving
  **1,492** dirty paths; do not commit/reset that mirror.

Actual PRNG state evolution, malformed/corrupted memory, complete transform/
submission providers, hardware FCSR/MMU behavior and gameplay/host acceptance
remain separate. Do not infer those from bounded model or native fixtures.

## Production And Progress

Preserve all **43 other target-owner functions**, bindings and pools.
The actual plain-C Make path has **three productive commands**, unchanged
O2/g3, and identical qualified padded code/metadata. The production build,
including the caller-owner rebuild, passes in **178.458s**.

Production exactly reproduces the independent strict first-link prediction:
**122 changed bytes**, comprising **121 instruction bytes and one symbol-size
byte** for the target extent change **12 -> 156**. There are **zero metadata
exclusions**. Preserve the separate four-byte alignment tail.

All **6,055 other linked bodies**, **6,056 addresses** and **189,088 protected
Game-data bytes / 720 owners** remain fixed. ROM, original assembly, shared
headers, the entire guard manifest, Makefile and conversion CSV remain
byte-identical. The inherited generated_12D630 Make warning remains.
Unchanged broader suite receipts are reused through this strict source/image
proof, not called fresh reruns.

ELF SHA-256:
`1456838d3fcc804c1e3d8fe89e54dae6245a31a7a85d36c084ed0692e4d8178f`.

Fresh full matcher: **3,704/5,505 exact (67.28%)**, Game
**3,031/4,832 (62.73%)**, **1,801 different / zero drift**. Init remains
492/492; Debugger 181/181. Converted counts/bytes are unchanged.
The 75% threshold is 4,129: **425 more matches** remain.
The refreshed ELF-pinned queue contains **1,667 placeholders,
125 semantic/other definitions and nine unlocated entries**. It is triage,
not authority to install unqualified C.

Next **func_150F7F8C**, VA **150F7F8C..150F802C**, ROM **12543C..1254DC**:
**40 words / frame 48**. Qualify its two float RNG calls, first result's stack
lifetime, float32 expressions 3*first+9 and 70*second+70, exact **3F030C35**
constant, seven-argument mixed ABI, post-helper argument reload and second
submission, real helper/caller interfaces and full owner/image. It remains
**queued, uninstalled, without a draft or matching credit**.
Keep the larger `func_1508CAD8` stub queued too.

Root README gets aggregate rows only; detailed progress belongs here and in
concise indexes. Commit tools before the consumer pin, with no push. Verify
the existing post-commit graph hook's terminal processes and old-node retention
in the ignored final checkpoint. No host source, real save/configuration or
frozen Release artifact is changed.
