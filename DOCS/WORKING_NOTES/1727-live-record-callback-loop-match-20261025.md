# 1727 - Live Record Callback Loop Match - 2026-10-25

Adopted and recounted from the actual Native ELF:3,803/5,505 exact (69.08%),
Game3,130/4,832 (64.78%), zero drift,1702 different.326 more matches reach75%.

## Recovered behavior

`func_15013000`, owner `game_40490`, occupies VA `0x15013000..0x150130B4`
and VROM `0x404B0..0x40564`:45 words/180 bytes with a40-byte frame. Its old
12-byte zero-return C stub did not clear or process any records.

The recovered pass clears the word accumulator `D_800DCDC4` and float accumulator
`D_800DCD90`. It walks52-byte records through the pointer stored at `D_800D3098`,
using an unsigned full-word bound from `D_800D3094`. The upper six bits of each
record's byte at+15 select `D_80082E30`; nonnull callbacks receive the current
record. Callbacks can replace the base, change the count, alter future type bytes
or alter the table. The next iteration observes those changes.

The local `DispatchRecord40490` view names `kindFlags` and preserves the0x34
stride. This owner hides the legacy inline-array declaration around
`variables.h`, following the existing pointer view in `game_16EE20.c`; shared
headers and the data label stay intact. Other retail consumers independently
load the base pointer. `func_15017930` passes its address to the data loader and
divides the returned length by0x34 to establish the count.

The pass returns `void`. The sole aligned retail direct call is at VA15008074 /
VROM35524 in `func_15007B3C`; its following `lw v0,0x2C(sp)` discards the pass's
register result. The callback type returns `s32`, and the pass discards it.

## Matching recipe

An ordinary type-byte local recovers the original loop roles and instructions.
The complete semantic C body emits45 words with14 opening differences and12
bindings under the owner's existing O2/g3 profile. All words from+50 through
the epilogue already agree. The frame and saved-register lifetime agree.

Fourteen relocation-aware expected-word rows restore a closed permutation of
the existing instructions at+18..+4C. The BEQ moves from+34 to+3C; its immediate
changes from18 to16, preserving the same exit at+98. The recipe adds or omits
no instructions and makes no frame change. It preserves actual relocations,
including signed HI16/LO16 carry behavior. This is guarded C, not a direct
compiler-only match. The production manifest's entire older prefix is retained.

The actual ordinary padder and GNU assembler reproduce all45 retail words.
All31 raw and padded neighbors, their bindings, owner pools and retail positions
are preserved. The complete GLOBAL_ASM preprocessing/postprocessing route runs.
The actual five-command Make shadow uses the unchanged normal profile.

## Fresh qualification

Both tools copies pass eight fresh pre-install and eight fresh installed
tests, zero errors, failures, skips or reused checks. Separate shared-tools
checks pass in both copies. All32 target test-method executions are fresh.

- 1990 guest phases/5970 instruction runs compare retail, normalized and raw C;
  all45 words execute. Normalized complete private state agrees literally.
- SDK/native32 O0/O2/O3 each pass76800 cases with trap UBSan. Eight effective
  compiled negatives exit23, including stale count/base and negative-zero reset.
- The authentic26-entry table has nine nonnull entries. Exhaustive256-byte
  selection tests use an explicitly synthetic64-entry table; they do not prove
  that every synthetic kind is a valid game record.
- The full426-word caller is independently GNU-assembled and retail-locked.
  Its actual eight-word call/return window passes120 phases, including saved
  V0 values with their high bit set and callback clobbers/mutations.
- Twenty-eight guest stack/global record-alias phases pass. All582 fired root
  access prefixes compare complete state, real dispatch PC/word and delay slot.
- Nine independent GNU rebases pass, including signed-low carries, with216
  rebased guest phases. All57 raw word/binding corruptions,14 padder word and10
  binding corruptions are rejected.
- Five strict-image and12 installed-input negatives fail as expected. The
  complete valid installed map passes; the stale predecessor object is rejected.
  The actual old12-byte target stub also fails the recovered behavior.

Large guest counts are deliberately terminated by the first callback. Portable
native tests use backed arrays. Guest aliases/fault prefixes are instruction
evidence, not portable C fault semantics. Whole-caller/provider/hardware/gameplay
acceptance remains separate; the old caller's production stub is not credited.

## Strict image and artifact identity

The independently linked ELF is
`db5035cc1f56562d05beae6098ce11e3e97ff4db9f6cacfffcb06c6926727dac`.
It differs in exactly149 bytes:148 target code bytes and one target-size byte,
with zero metadata exclusions. Actual production Make reproduces it exactly
in0.609s. The inherited duplicate generated_12D630 recipe warning remains;
no new target compiler diagnostics are introduced.

The first harness link used `qualified-padded.o` as its basename, which changed
a synthesized local FILE symbol and shifted the string metadata. The corrected
independent link uses identical object bytes under `link-input/game_40490.c.o`,
matching production's basename. The complete image comparison remains literal.

A first test wrapper correctly rejected an artifact change: its setup was
recompiling an already qualified raw owner. A controlled repeat isolates126
changed `.mdebug` bytes while code, bindings and pools remain equal. Setup now
verifies the frozen qualified objects. Both complete suite fingerprints hold.
The rejected link and wrapper receipts are preserved; neither receives credit.

The canonical raw object is frozen at
`f5d831da466fa3bea2421b6cfe03c8d311160a2a6822213f3a6a9e5fe16b2a1f`.
Padded object:
`e0b029857780217c9ecf1bed8b6f20cb011f0f0fa25093c1a3c392819a421594`.
Proposed source:
`fe5e93c04b9d072f9249d99876ae2074ecdc2e2e86931893e40fe983ddf0bded`.
Proposed manifest:
`01c02d32f3c22688893b69c5716a2c348ef2fe7ca00462a23cb9cc84cc472bbb`.

## Checkpoint and continuation

Baseline consumer7b79c30 / toolsca1a655, prior Native ELF7686274a. Tools
`a90bd4e6d5d182b356bab71d85c43fa91cc7c3a8` are committed first; this note
accompanies the consumer checkpoint. Native adoption verifies all16074 sealed
inputs before/after with exactly four declared source/CSV/object/ELF overrides.
All6055 function addresses and6054 other bodies stay fixed. All720 protected
data owners/189088 bytes match, SHA0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670.
The older tools mirror's1664 preexisting dirty paths and history are preserved.
The graph closeout uses separate owned AST-extract and fresh build processes,
eight changed C/MD files and explicit retention/unique relocation of all44239
old nodes. Outside-scope manifest rows retain their historical freshness.

Codex owns implementation and validation; routine Claude calls:zero. No host
port, editor or Release work is part of this function. Keep the75% goal open;
the accepted live-ELF queue removes onlyfunc_15013000 and selects the next
ordinary placeholderfunc_150228E4, still uncredited. It retains the unresolved
void-pointer NULL factoryfunc_1518F5D0 as a placeholder.1573 placeholders,120
semantic/other and nine unlocated source screens remain; these are triage,
not automatic C/ABI qualification.

Prepared-checkout target tests:

```sh
python3 -m unittest tools.tests.test_game_record_callback_loop_match -v
```

The qualifier module owns the frozen predecessor, actual Make shadow, derived
guards and strict image gates. Retain its qualified artifacts when rerunning
tests; recompiling the raw owner requires fresh artifact fingerprints.
