# Actor Effect Dispatch And Owner Completion

Date: 2026-10-16. Resume from consumer **e3387b25**, tools **20f2701**,
both initially clean. Bank tools **166a8a1** before consumer source/pin/docs.
Continue [Note 1429](1429-rectangle-preset-dispatch-direct-byte-match-20261016.md):
restore **func_15171BF4**, all **42 executable words / 168 bytes**, frame
**0x28**, plus its original separate **one-word padding nop**. The complete
retail slot is **43 words / 172 bytes**. No target instruction guards.

## Steps

1. [x] Freeze live source/ELF/tools and audit the whole original routine, caller and four helper ABIs, including ignored return values.
2. [x] Recover the unsigned actor selector, byte-formal flags, effect/sound order and signed/unsigned audio arguments; qualify all 42 body words independently of the terminal padding.
3. [x] Pass ten pre-install tests, including native32, effective negatives, all selectors, aliases/faults, independent rebases, original caller and actual muted sound-wrapper paths.
4. [x] Predict the full linked image before installation, rebuild production and reproduce every byte without exclusions.
5. [x] Verify all nine owner slots / 4,368 bytes, remove its last zero-return placeholder and obsolete generic header, and preserve earlier guard-backed matches unchanged.
6. [x] Pass thirteen final checks, refresh aggregate README/status/roadmap rows, preserve the older tools mirror and commit tools before consumer C/pin/docs. No push.
7. [x] Recover func_1516D400 in [Note 1431](1431-four-byte-saturation-direct-byte-match-20261016.md): all 58 words direct after qualifying its counter array, conditional increment and current callback/result contract.
8. [ ] Restore the three external effect helpers and caller func_150265CC; retain func_15169C70, func_1511C638, inherited-stack func_1516FE1C and all broader Game/additional-source/raw-matching queues.

## Recovered Contract

```c
void func_15171BF4(u8 *actor, u8 flags);
```

The executable span is VA **0x15171BF4..0x15171C9C**, ROM **0x19F0A4**.
The padding nop at **0x15171C9C**, ROM **0x19F14C**, extends the retail slot
to **0x15171CA0**. Its actual function symbol grows **12 -> 168 bytes**,
not to the full 172-byte slot length.

Read the unsigned byte **actor[4]** once. Cases **0x13/0x23** call
`func_150AEEB0(actor, flags)`, then unconditionally submit
`func_10010154(0x69, actor, 0x7D00, 200, 2000)`. Cases **0x1E** and **0x54**
call `func_150BD740(actor, flags, 1)` and `func_150CDBB0(actor, flags, 1)`
respectively. Other selectors make no call. Do not reread a selector changed
by a helper or skip the sound based on the ignored first-helper result.

Recover minimal helper declarations. The audio wrapper is the existing
five-input `s32(u16, void *, u16, s16, u16)` routine, with its return ignored.
The effect helpers save/read the flag's low byte; the two three-input
helpers save their third argument but do not use it in the preserved bodies.
Retain the passed word 1 without claiming an observed mode behavior.
The actual entry ABI normalizes flags once to a byte before dispatch.

The reference's actor-field expression uses a word load followed by a cast;
the original is an actual byte read. Its word-formal flags and temporary
mask also do not recover the original compiler schedule with the real
narrow helper prototypes. The selected byte formal does.

## Direct Body And Padding

The first complete word-formal candidate emits **45 words**, frame 0x28,
with repeated helper masks and 36 reported differences. Four bounded
source/prototype screens distinguish byte formal, repeated explicit mask,
word temporary and word-helper prototypes. The accepted byte formal with
no redundant source mask emits all **42 original executable words directly**.

The generic screen initially reports a single length difference because
its canonical comparison includes the separate 43rd padding word. Do not
call this a real instruction mismatch or insert a source operation to fill
it. Require the exact 168-byte compiler body, four call bindings and the
original terminal word zero. The existing layout padder retains that nop;
the qualifier reports body and slot lengths separately. The padding-flip
control bypasses fixture hashing and explicitly fires the terminal-padding
gate. No body instruction is inserted, omitted or replaced.

Raw body SHA-256:
`e79b7e5b12f85c709d0c21c3ecc05916859a2ee81e623346ce15947664b25f54`.
All eight neighbors retain their words, lengths and relative relocations.
The inherited 32-byte pool, Makefile/profile, pool alias and complete prior
guard manifest remain fixed. No guard row is added for this target.

## Fresh Qualification

All **10 final pre-install tests pass in 55.043s**. After production
installation, all **13 final checks pass in 75.277 seconds**, exit zero:

```sh
python3 -m unittest tools.tests.test_game_actor_effect_dispatch tools.tests.test_game_actor_effect_dispatch_installed -v
```

- **3,072 paired cases** cover all 256 selector bytes, canonical/high-bit flag patterns, both stack phases and effectful helpers that mutate the selector and clobber caller-saved registers. All 42 body instructions execute; the terminal padding does not.
- **Native32 O2/O0, 1,536 cases each**, separate translation units and selected-C UBSan, verify every selector and effect/sound call order. All ten compiled guest/native negatives reject: halfword/wrong-offset selector, missing second kind, wrong helper, lost flag bit, wrong mode word, wrong sound ID, swapped distance words, missing sound and reversed effect/sound order.
- **64 fired fault-prefix pairs** and **eight guest-only argument-home aliases** compare complete literal guest state. They do not establish portable C fault/alias behavior or native FP-environment equivalence.
- All **42 raw-word, four call-binding and 32 inherited-pool byte corruptions** reject. The separate padding corruption reaches its dedicated gate. Three independently assembled original rebase sets / **120 paired cases** change all four call bindings.
- **Six original caller captures** execute func_150265CC's 0x1502993C window: actor comes from T9 and flags from SP+0x773. The current caller remains a zero-return placeholder, with the 16-byte call window zero-filled. Use `rg --no-ignore` inside the ignored original assembly tree; a default directory search misses this evidence.
- **Eight actual current sound-wrapper connections** execute the restored 124-word Init routine after the bounded first helper sets actor state 0 or 5. Only its muted early-return paths are qualified. The three effect helpers remain current placeholders, the active sound paths are not tested here, and no audible sound/gameplay completion is claimed.
- All **89 frozen/live input keys**, capture/initial-prediction/successor controls and physical code/callee/data/symbol/string/padding corruption tests pass. All **87 unaffected inputs** remain fixed. Protected data stays exact across **189,088 bytes / 720 owners**.

Both tools copies pass Windows syntax and all eleven shared WSL padder
tests; consumer `make tools-check` passes. No shared helper is changed.
Prior unchanged neighbor-suite receipts remain prior evidence, not newly
rerun suites. Routine Claude calls: zero.

## Completed Owner

The installed owner is
[generated_19E040.c](../../conker/src/game/generated_19E040.c). Its entire
**4,368-byte / 1,092-word** retail text slice now matches, with all nine
slots checked together against the original image:

| Function | Retail Words | Linked Result |
| --- | ---: | --- |
| func_15170B90 | 205 | Exact; earlier guards retained |
| func_15170EC4 | 34 | Exact |
| func_15170F4C | 158 | Exact |
| func_151711C4 | 15 | Exact |
| func_15171200 | 256 | Exact |
| func_15171600 | 127 | Exact |
| func_151717FC | 61 | Exact; earlier guards retained |
| func_151718F0 | 193 | Exact; earlier guards retained |
| func_15171BF4 | 43 | Exact; 42 body words plus separate padding |

No zero-return placeholders remain. Replace only the now-obsolete generic
placeholder header with a reconstruction header. Earlier guard-backed
routines are not reclassified as direct raw compiler matches, and this
owner milestone is not whole-game C or runtime completion.

## Image And Progress

Before production changes, capture the old link script and padded object.
The baseline full link reproduces the frozen predecessor exactly. A full
link with only the qualified owner selector equals the slot/extent
prediction. Production then reproduces every byte: **127 changed bytes**,
zero extra serialization changes, every other ELF byte fixed, no exclusions.

```text
before ELF 5877233ddf6a78bc55b80b102f47d8736e8678351e5937e3ba1b3e77066a8533
after ELF  acbf49495584a4d1f9b4917596f9cbea3e5a16535ea09d183e480223c8629c44
after C    0ea4c5fbafeb1f192de22cd173a17ca82a4b5a396bc270fd923e032f0a24f2b6
```

Fresh official totals: **Game 2,917/4,828 (60.42%)**, **total 3,590/5,501
(65.26%)**, different **1,911**, drift **0**. Init 492/492 and Debugger
181/181 remain exact. Conversions stay 5,501/6,044 (91.02%), converted
bytes 86.04%. Root README changes only aggregate matching rows. The old
duplicate generated_12D630 recipe warning recurs; the guest build exits zero.

Tools **166a8a1** banks five experiment/oracle/checkpoint/test files first.
Preserve the older mirror's **ddbdd16** HEAD and all **782** initial dirty
file hashes, copying only these five absent files for **787** final dirty
paths. Do not commit/reset that mirror. Bank consumer C/tools pin/docs
separately, with no push. Let the normal incremental Graphify commit hook
finish; do not force a full scan or drop retained excluded nodes. No host
build/launch or frozen Release action occurs. The wider matching goal stays open.
