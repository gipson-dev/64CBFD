# Randomized Point Burst Direct C Match

Date: 2026-10-20. Consumer predecessor: `d77d4298`; tools predecessor:
`d106360`. Tools **9e5b77d** are committed first. No push.
The wider **75% total C-matching objective remains active**, not complete.

## Installed Recovery

Replace the false zero-return `func_150CA930` placeholder in
[generated_F5800.c](../../conker/src/game/generated_F5800.c) with the complete,
purpose-commented point-burst wrapper. Retain the original address-based name.
VA **150CA930..150CA9D0**, ROM **F7DE0..F7E80**: all **40 words / 160 bytes**
emit directly from normal **IDO O2/g3**, including the original **64-byte frame**.
There are **no new instruction guards or compiler-profile changes**.

Use the existing `struct17` three-float point. First call the existing signed
integer RNG, reinterpret its complete result as unsigned, take **modulo 21**,
add **10**, and store the resulting **10..30** count in a signed short.
Then call the float RNG and compute single-precision **random * 59 + 170**,
with separate multiply/add rounding. Read the point's X/Y/Z only after both
calls, and submit twelve arguments to `func_1514C678`:

```text
x, y, z, scale, 0, 255, count, 0x13, 0, 0.0f, NULL, 255
```

The first two floating arguments use F12/F14; Z/scale use A2/A3 and the
remaining eight words are stack arguments. The original count home is
**SP+0x3E**, loaded as a signed halfword. Preserve the argument pointer in
its incoming home and reload it after the RNG calls.

Inspect the complete original 120-word submission helper and its signed-short,
byte, word, float and pointer stack reads before declaring the local interface.
The wrapper and its callers consume no return value; its local void use does
not assert a meaningful downstream V0 result. The helper's indirect callbacks
and full positive behavior are not executed or recovered by this change.
No shared header, original assembly, ROM or host-port source is changed.

## Qualification

[The focused helper](../../tools/experiments/game_point_random_burst.py)
freezes the exact source, original routines, shared headers, ELF, guard
manifest, Makefile, ROM and conversion rows. Historical pins stay unchanged.
[Seven tests](../../tools/tests/test_game_point_random_burst.py) pass without
errors, failures or skips in both tools copies:

| Stage | Primary | Standalone Mirror |
| --- | ---: | ---: |
| Before installation | 5.960s | 5.720s |
| Installed source | 7.759s | 21.965s |

- **423 cases / 846 complete original-versus-C modeled phases**, both stack
  alignments, compare all modeled state and independent twelve-word packets.
  Visit all **40 target words** and every output count 10..30. Include full
  unsigned RNG edges, all modulo residues, signed zero, finite float values,
  point changes during either/both RNG calls and aggressive provider clobbers.
- **421 native32 cases** at O0/O2/O3 with trap UBSan, explicit float32
  multiply/add and typed point/fence checks. Expected packets are generated
  independently, not calculated by the tested C expression. The two incoming
  argument-home redirects are guest-only probes, not portable C alias claims.
- **Ten compiled semantic controls** all reach the expected rejection code23:
  signed modulo, wrong modulus/base/scale/offset/X/type/count/alpha and early
  point capture. Two actual guest instruction controls reject signed division
  and the wrong short home.
- Scan every pristine function for direct JALs and the ROM for literal target
  pointers. There are **two direct callers**: `func_150265CC` at **150287F0**
  and `func_150CA150` at **150CA878**. Execute their actual argument/store
  windows plus the complete target in **56 phases / 112 executions**.
  Both models fire an explicit stop at the first post-return PC, respectively
  **150287F8** and **150CA880**. Seed the original caller's point/FP values;
  do not claim either complete large parent routine was executed.
- Three independent GNU call-symbol rebases pass **45 phases** with matching
  original/C words and packets. All three original R_MIPS_26 bindings remain.
- Seven strict-image negatives reject unrelated header/code/data, target size,
  truncation and appended bytes.
- Both shared tools checks pass. The two task files agree in both copies and
  all four Python files parse. Preserve all **1,488** older mirror dirty
  paths/statuses/hashes and its **ddbdd16** HEAD; add only these two absent
  task files, leaving **1,490** dirty paths. Do not commit/reset that mirror.

The first fixture attempt exposed missing nested C initializer braces and the
second direct caller. Correct the fixture and add the actual second window;
do not suppress warnings or reinterpret a setup failure as a semantic control.
The post-return boundary explicitly owns the stopped PC and must actually fire.

The models bound external providers and finite valid point memory; they are
not hardware/FCSR/MMU emulation. Malformed input, arbitrary NaN behavior,
complete parent/helper execution and gameplay/host acceptance remain separate.

## Production And Progress

Preserve all **18 other raw/padded owner functions**, bindings and pools.
The real plain-C Make path has **three productive commands**, unchanged O2/g3
and identical padded code/metadata. Production rebuild passes in **21.032s**.

The linked ELF equals the independent strict first-link prediction byte-for-byte:
**120 changed bytes**, comprising **119 instruction bytes plus one size byte**
for the target extent change **12 -> 160**. There are **zero metadata exclusions**.
All **6,055 other linked bodies**, **6,056 addresses**, and **189,088 protected
Game-data bytes / 720 owners** stay fixed. The ROM, original assembly, shared
headers, entire guard manifest, Makefile and progress CSV remain byte-identical.
The inherited duplicate generated_12D630 Make recipe warning remains.

ELF SHA-256:
`36e0666a72ffef1d745ead26517a1e9b5a3072e5366d44c5977615bade991c49`.

Fresh full matcher scan: **3,703/5,505 exact (67.27%)**, Game
**3,030/4,832 (62.71%)**, **1,802 different / zero drift**. Init remains
492/492; Debugger 181/181. The 75% threshold is 4,129: **426 more matches**.
Converted counts/bytes do not change. Refresh the ELF-pinned queue:
**1,668 placeholders, 125 semantic/other definitions and nine unlocated entries**.
Reuse unchanged source shapes only through the strict source/whole-image proof;
the queue is triage, not C/ABI qualification. Unchanged broader suite receipts
are reused, not represented as fresh reruns.

Next is **func_150F2230**, VA **150F2230..150F22D0**, ROM **11F6E0..11F780**:
a **40-word slot**, including a trailing alignment word, with a **56-byte
frame**. Qualify its actor +0x1D4/low-nibble gates, byte RNG angle, zeroed local
vector, original helper interfaces, post-RNG actor/matrix reload, byte argument,
callers and full owner/image. It remains **queued, uninstalled and uncounted**.
Keep the larger `func_1508CAD8` stub queued too.

Root README receives aggregate rows only. Preserve current user/editor/save
state and the frozen host Release. Commit tools before the consumer pin,
then verify the existing post-commit graph hook's terminal processes and
old-node retention in the ignored final checkpoint. No push.
