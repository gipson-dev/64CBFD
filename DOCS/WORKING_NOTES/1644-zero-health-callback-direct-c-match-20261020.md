# Zero-Health Callback Direct C Match

Date: 2026-10-20. Consumer predecessor: `e9da6619`; tools predecessor:
`ac05ac7`. Tools **41229dd** are committed first. No push.
The **75% total C-matching objective remains active**, not complete.

## Recovered Routine

Target `func_15195698` in
[generated_1C1150.c](../../conker/src/game/generated_1C1150.c).
VA **15195698..15195738**, ROM **1C2B48..1C2BE8**,
**40 words / 160 bytes**, **48-byte frame**, three call bindings,
normal **IDO O2/g3**. Preserve the address-based name and add a purpose comment.

Use the existing `struct127` fields: unsigned `health` at +0x1CA,
unsigned `unk127` at +0x127 and unsigned `id` at +4.
When the second actor's health is zero and its selector is not 0xFF, call:

1. `func_15136C3C(actor, 1, 1, 1, 1, 0, 0xFF, 1)`.
2. `func_15145A50(actor)`.
3. `func_1507CD64(actor, 6)`.

Only then read the first actor's ID; clear its health if the ID is 0x47.
The helper calls are not individually re-gated after the initial test.
Helper-side mutations and legal same-object aliasing must remain visible.

The callback returns **void**, not the old stub's false constant zero.
Its third argument is an **unused byte pointer**, not an integer flag:
both actual callers pass a stack-byte address. Preserve the incoming pointer
homes even though the callback never dereferences that third argument.
Keep existing helper return declarations compatible with their current
owners; their return values are ignored here.

ANSI and K&R probes both emitted the complete retail body directly.
Select the ANSI definition with the correct pointer argument and normal
compiler profile. **No new guards, dummy locals, register binding or
compiler-profile changes.** The whole existing guard manifest remains pinned:
`016466c90030bca35c3b27892833265d62314b8b8156145fd9c2eae7c3e37623`.

## Actual Callers

The complete direct-JAL and aligned-ROM-pointer screen finds **no direct JAL**
and one target pointer at **ROM 22B1DC / VA 8008671C**.
This is **entry 34 of D_80086694**, not the earlier neighboring D_80086150
table. The physical 39-word table includes two trailing zero words.

Two known original dispatcher windows use this table:

- `func_1505B9C4`: **1505BD5C..1505BDA0**, 17 words,
  ROM **8920C..89250**. Preserve the selector fallback, 0x27 byte skip,
  A0 from parent SP+0x68, A1 from S0, and A2 = parent SP+0x67.
- `func_1505C1E4`: **1505C6DC..1505C6FC**, eight words,
  ROM **89B8C..89BAC**. Preserve A0 from S1, A1 from S0,
  and A2 = parent SP+0x54.

Execute the windows through the callback and stop at real join fetches.
These bounded windows do not prove the complete dispatcher parents or all
possible indirect callers. Other callback selections remain outside this fit.

## Qualification Work

[The module](../../tools/experiments/game_zero_health_callback.py) freezes
24 source/header/assembly/table/image/build inputs.
[The focused suite](../../tools/tests/test_game_zero_health_callback.py)
covers all byte-valued gates, late reads/mutations, legal same-actor aliasing,
typed native32 callback calls, negative controls, rebases and actual helpers.

The isolated and whole-owner C have **zero differences / three bindings**.
Preserve **28 other raw/padded owner functions**, pools and inherited
diagnostics. The generated source slice contains five existing GLOBAL_ASM
bodies; retain all five.

The first whole-owner fixture omitted this slice's existing retail jump-table
binding. Correct the fixture to pass **jtbl_800A8258_game**, exactly as the
unchanged Makefile does. Do not replace data, suppress link errors or add an
undefined .rodata anchor. Actual Make uses five productive preprocessing,
compiling, postprocessing, padding and assembling commands. All five pass;
their raw/padded code and metadata equal the independently qualified objects.

The independent first link exactly matches the closed body/size prediction:
**125 changed bytes = 124 code bytes + one symbol-size byte**, target extent
**12 -> 160**, **zero metadata exclusions**. No symbol/string permutation is
needed. ELF SHA-256:
`62088fce9f6ac115c8e6830813795ad02f8092c596c573183d42dd2d079039d4`.

Helper preflight executes **all 34 original state-helper words** in 80 phases.
It also executes the final helper's **15-word NULL path** in six phases,
not all 253 words. The original state helper clears **one byte** at
state+0x78; the first fixture incorrectly expected a word clear. Verify the
original SB before correcting the expectation, preserving adjacent canaries.
The first 197-word helper and lower state provider remain bounded providers.

The basic byte-gate, alias, dispatcher-window and lazy-read preflights pass.
The native preflight passes 896 cases at O0/O2/O3 with trap UBSan and rejects
all 12 compiled semantic negatives. Both shared smoke checks pass.
The formal eight-test suite passes in both copies before and after installation,
with no failures/errors/skips:

| Stage | Primary | Older Standalone Mirror |
| --- | ---: | ---: |
| Before installation | 46.214s | 25.466s |
| Installed source | 28.950s | 31.464s |

All 40 target words execute in **1,792 modeled phases / 896 cases**. The
actual compiled predecessor stub fails the semantic checks. Both original
dispatcher windows pass **80 phases / 160 fired join boundaries**, including
the selector fallback and 0x27 skip; 48 phases actually enter this callback.
Three independent GNU rebases pass **60 phases**, preserving all three call
bindings. Seven strict-image negatives reject code/header/data/extent/length
changes. Lazy-selector and invalid-pointer checks qualify guest instruction
behavior only; no defensive NULL behavior or portable C faults are added.
Hardware/MMU, invalid-memory C behavior, larger helper
internals, complete parents and gameplay/host acceptance remain separate.

The older standalone tools mirror stays at `ddbdd16`. Preserve all **1,500
pre-existing dirty statuses/hashes**, add only the two absent task files and
verify both copies byte-identical and all four Python files AST-valid. Its
dirty count is now **1,502**. Never commit/reset/stash/clean that mirror.

## Production And Progress

Production passes in **87.381s**, reproducing the exact first-link prediction.
All **6,055 other bodies**, **6,056 addresses**, and **189,088 protected
Game-data bytes / 720 owners** remain fixed. ROM, original assembly/tables,
shared headers, Makefile, progress CSV and the entire guard manifest are
byte-identical. The one inherited pointer/integer compiler warning in
`func_15194DC8` and duplicate generated_12D630 recipe warning remain;
do not call this warning-free. No hardware/gameplay/host acceptance is claimed.

Reuse unaffected objects with the documented pinned-manifest dependency flag:

```sh
make -C conker -j4 -o retail_word_patches.us.csv build/conker.us.elf progress.csv
```

This rebuilds the changed owner and performs the complete link. No Makefile,
compiler flags or timestamps change. Unrelated objects are not claimed freshly
recompiled. Broader unchanged suites are reused through the pinned inputs and
strict whole-image proof, not represented as fresh reruns. A later ordinary
Make may rebuild more objects because of earlier manifest timestamps.

After the fresh production build and installed audit, invoke the literal
standard Make matcher recipe directly, avoiding a redundant dependency scan:

```sh
cd conker
python3 ../tools/match_progress.py progress.csv build/conker.us.elf conker.us.bin --version us --objdump mips-linux-gnu-objdump
```

It passes in **2.322s**; the independently refreshed queue agrees:
**3,709/5,505 exact (67.38%)**, Game **3,036/4,832 (62.83%)**,
**1,796 different / zero address drift**. Init remains 492/492; Debugger
181/181. Converted counts/bytes are unchanged. Threshold 4,129 leaves
**420** more matches. Queue source shapes: 1,662 placeholders, 125
semantic/other and nine unlocated. These are screens, not qualification.
Routine task: **zero Claude calls**. Keep the 75% checkbox open.

## Next Target

Queue `func_151A4FD0`, `generated_1D0840.c`, VA **151A4FD0..151A5070**,
ROM **1D2480..1D2520**, **40 words / frame32**. Recover the eight-input
type-0x5A factory, wrapping size-plus-0x20 request, 0xFF/one flags, NULL path,
late incoming argument reloads and exact byte/word stores at +0x10..+0x1A.
The seventh incoming argument is loaded as a byte at SP+0x3B; do not flatten
all inputs to bytes or assume the size addition has defined signed C overflow.
Graphify/full-retail inspection is a read-only screen, not ABI/C qualification.
No draft, installation or matching credit. Keep `func_1508CAD8` separately queued.
