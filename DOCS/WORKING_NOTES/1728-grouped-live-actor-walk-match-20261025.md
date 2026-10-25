# 1728 - Grouped Live Actor Walk Match - 2026-10-25

Adopted and recounted from the actual Native ELF: 3,804/5,505 exact (69.10%),
Game 3,131/4,832 (64.80%), zero address drift, 1,701 different. Another 325
matches reach the current 75% threshold.

## Recovered behavior and ABI

`func_150228E4`, owner `generated_49D30`, occupies VA
`0x150228E4..0x15022998` and VROM `0x4FD94..0x4FE48`: 45 words/180 bytes
with a 48-byte frame. Its old 12-byte zero-return C placeholder did no work.

The recovered `void func_150228E4(s32 group)` reads the group's unsigned byte
count at `D_800C3510[group]`, walks its 25-byte row in `D_800C3518`, and uses
each unsigned byte as an index into the 0x32C-byte actor array `D_800CC2D0`.
It calls `func_15060F28(actor, 0)` for a nonzero `interaction_state` word.
The helper may change the count, future row entries and actor states. The next
iteration observes those changes; inactive entries retain the existing count
without another helper call.

Use the existing SDK `struct127` and named `interaction_state` field. The helper
already has `void func_15060F28(struct127 *, s32)` in `functions.h` and its
provider owner. Add only the local actor-array declaration and helper prototype
beside the existing count/row declarations. No shared header or profile changes.

The sole aligned retail direct call is at VA `0x1501EB74`, VROM `0x4C024`,
inside `func_1501EA18`. Its delay slot passes the saved group word. The following
call to `func_150227BC` reloads that word from the original caller home and
discards this routine's register result. The caller's production C placeholder
is unchanged and uncredited.

## Four derived scheduling guards

The complete semantic body emits all 45 words with the original 48-byte frame,
seven relocation bindings and four independent setup differences under the
existing `-O2 -g3 -Wo,-loopunroll,0` owner profile.

Four expected-word rows derive two closed instruction swaps: `+0x30 <-> +0x38`
and `+0x50 <-> +0x54`. The first exchanges count-index initialization and
group-offset subtraction across an independent branch delay slot. The second
exchanges independent cursor and actor-base address updates, moving the existing
LO16 binding with its instruction. No opcode, branch target, frame, instruction
count, saved-register lifetime or loop instruction is invented or omitted.
This is a guarded C match, not compiler-only matching.

The actual ordinary padder and the actual generated-owner Make padder both
reproduce the complete retail routine. All 56 raw and padded neighboring
functions and their bindings/pools are preserved. The actual generated-owner
Make recipe has three commands; it keeps the existing no-unroll flag.

## Qualification

Both tools copies pass eight fresh pre-install and eight fresh installed
checks, zero errors, failures, skips or reused checks. All 32 test-method
executions are fresh and their complete artifact fingerprints agree. The
canonical suites include these independently checked boundaries:

- 1,968 guest phases/5,904 runs compare original, normalized and raw C;
  all 45 instructions execute and complete terminal state agrees.
- 588 fired own-access prefixes compare complete state and real dispatch
  PC/word and branch-delay metadata.
- SDK/native32 O0/O2/O3 each pass 102,400 cases with trap UBSan. Six effective
  compiled negatives exit 23: positive-only state, masked index, wrong helper
  flag, wrong actor argument, missing gate and cached count.
- The authentic 136-word caller is independently GNU-assembled and retail
  locked. Its actual nine-word window passes 180 phases, including helper
  clobbers, skipped child calls and live incoming-home changes.
- Twenty-eight deliberately rebased guest alias phases compare literal state.
  Saved-slot overlap that corrupts saved s0 is observed at the executed return
  delay slot, not claimed as ABI preservation. Normal/caller cases keep their
  ABI gates.
- Nine independent GNU rebases cover signed-low carries and the direct call
  relocation. Another 216 guest phases/432 original/normalized runs execute
  those rebases privately. Canonical suites freshly execute all three bodies
  in 216 phases/648 runs, including the raw C rebase.
- Forty-five raw-word and 14 binding mutations are rejected, as are four
  actual padder word mutations and two padder relocation mutations.

Exhaustive byte indices use explicitly synthetic 256/257-actor backing.
Native groups and rows are valid and bounded. Full-word selectors, faults and
deliberate saved-slot/global aliases are guest-only evidence, not portable C
fault behavior. Full-caller/provider/hardware/gameplay acceptance is separate.

## Strict image and artifact identity

The independent and reproduced production ELF is
`08f3110edeb2864ff15ffb896bbfb76573dcd62bcfcb31bf569af0e3511a5820`.
Its literal delta is 144 bytes: 143 target code bytes and one target
symbol-size byte, with zero exclusions. All 720 protected Game data owners /
189,088 bytes remain exact, SHA
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.
Actual production Make reproduces it in 4.652s. The inherited
duplicate generated_12D630 recipe warning remains; no new target compiler
diagnostics are introduced.

Raw code SHA:
`43a8219a93b386a4e1e08f07a7f9c68cc28b16eb559d13e1b5c4fa9d1b5acac7`.
Proposed source:
`7475b4acd1e1984979c5de36359bf3568a3d3828bcb6433a39ad0ce5bacbc885`.
Proposed guard CSV:
`3e824bc7b855f611e262a233050f0caad0e21af1386deca9965a740258e1b588`.
Padded object:
`cfe87c00391bec27bda5a8be3f96c1987256564a781281b8d551c813a4c6fafe`.

Preparation correctly rejected a generated duplicate C-body string whose
multiline indentation changed during wrapping. The canonical routine now uses
one `SELECTED` body constant. This fixture correction changes neither the
qualified source nor the retail recipe. The rejected receipt/source is retained.
Qualified raw objects are frozen once; test setup verifies them without
recompilation, preserving their exact IDO debug bytes.

## Checkpoint and continuation

Baseline consumer `0da7021c` / tools `a90bd4e`, Native ELF `db5035cc`.
All 16,078 current inherited/owned inputs are sealed, with 58 focused inputs.
The independent older tools mirror's 1,666 preexisting dirty paths and history
are preserved; only this function's two new canonical files are added there.
Tools `e33826535e5901d8515b07d4318bd97f12dc8366` are committed first; this note accompanies the consumer
checkpoint. Native adoption verifies all 16,078 inputs before and after the
four declared source/CSV/object/ELF changes. All 6,055 function addresses and
6,054 other bodies remain fixed. The accepted ELF queue removes only this
function; 1,572 placeholders, 120 semantic/other and nine unlocated screens
remain. Its next ordinary placeholder is `func_150AEDF8`, still
uncredited. These classifications are triage rather than C/ABI qualification.
The scoped graph closeout retains or uniquely relocates all 44,247 old nodes
while refreshing only eight changed C/MD files; outside manifest rows retain
their historical freshness.

Codex owns implementation and validation. Routine Claude calls: zero.
Keep the 75% goal active and derive the next function and remaining count from
the adopted Native ELF queue. No host port, editor or Release work is included.

Prepared-checkout focused tests:

```sh
python3 -m unittest tools.tests.test_game_group_live_actor_match -v
```

Keep the qualified artifacts frozen between suites. A new raw compilation
requires new fingerprints; arbitrary compiler debug-byte differences are not
excluded from the artifact checks.
