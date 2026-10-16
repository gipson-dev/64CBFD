# Record Random Drag Guarded Byte Match

Date: 2026-10-15. Resume from consumer **e7277787**, tools **d585639**,
both initially clean. Tools **bce2d08** is committed first. Restore
**func_151707E0**, all **117 retail words** exact after checked register
normalization. It is **not a raw compiler match**. The complete additional-
source/Game objective remains active.

## Steps

1. [x] Audit the entire original, additional-source body, actual callback table and current helper ABI before importing any source.
2. [x] Recover the byte fields, full-word fade/completion, both RNG contracts, live post-provider reads and repeated-X threshold without undefined signed overflow or negative left shift.
3. [x] Screen expression types/layouts, recover 117 words / frame 0x28 and check the remaining register-only plan with effective dependency controls.
4. [x] Qualify literal/public state, faults/aliases, native32, independent rebases, actual slot-6 helper chains and all protected inputs/archive fingerprints.
5. [x] Replace only the target stub, append the 117 closed guards, rebuild and match the entire initial ELF prediction without exclusions.
6. [x] Pass all 15 final tests, refresh aggregate documentation and bank tools before consumer source/pin/docs, preserving the older mirror.
7. [ ] Continue func_151709B4 and the full remaining Game/additional-source, caller and inherited-stack queues.

## Recovered Behavior

**func_151707E0**, VA **0x151707E0**, ROM **0x19DC90**, is **468 bytes /
117 words**, frame **0x28**, in
[generated_19A8B0.c](../../conker/src/game/generated_19A8B0.c).
Its address name is retained. The comment describes the record fade and
randomized scaling, explicitly disclosing register normalization. Its ABI is
`s32 func_151707E0(u8 *record)`, not a truncated byte pointer or a no-argument
stub. The original table at **D_8008CBA0 + 24** selects it as **slot 6**,
not slot 8; verify [231660.rodata.s](../../conker/asm/data/231660.rodata.s).

Read the byte at 0x1F into a full signed word. While the lifetime byte 0x24
is nonzero, an initially zero value calls zero-argument **func_150ADA20**,
treats its result as unsigned and stores `% 25 + 200` into lifetime. Keep
the original fade snapshot through that provider; do not reload a changed
0x1F. Read the global step after the provider, add its wrapped left-six
projection and clamp signed values >=255 to **254**, not 255. Value 254
skips that step read and store entirely. While lifetime is zero, subtract
the wrapped left-four step and clamp negative full-word results to zero.
Narrow only the byte store, not the local value used for completion.

The full-word distinction is observable: inactive value 16 and delta -15
produce **256**, store byte zero, but continue instead of returning 1.
Return 1 only when the re-read lifetime and full-word value are both zero.
Otherwise call **func_1516F864(record)** before reading live mode/velocity.

If byte 0x2F is nonzero, make two zero-argument signed **func_151EF610**
calls, each followed by X or Z scaling using `% 32 + 230`. The factors
are full words and can exceed 255. Otherwise load signed high byte 0x26
and unsigned low byte 0x27. Retail deliberately computes the same packed
**X velocity twice**, sums both low-word squares and compares the signed
wrapped result against 2001. Do not substitute X/Z or a widened positive
norm: X=-32768 yields wrapped **0x80000000** and skips this branch. The
selected C uses defined unsigned word arithmetic and a range-safe signed
multiply-by-256 expression to preserve both original square operations.
When the threshold passes, use two signed `% 32 + 220` factors. Continuing
paths finally clear only the halfword at 0x18 and return zero.

The frozen additional source
`Another Source/CBFD-Recompiled/conker/conker/src/game/game_19A8B0.c`
remains reference-only and unchanged. Its wide/unaligned field accesses,
byte-truncated fade local, byte-cast record pointer and invented RNG inputs
are corrected against original assembly, not accepted as-is.

## Compiler And Guards

The first corrected body emits **111 words / frame 0x30 / 41 length-inclusive
differences**, because IDO merges the identical square operations. Twenty-
three expression/type/layout screens identify a meaningful spelling that
keeps both squares. Named first/second temporaries reach 117 words but
retain frame 0x30. Inlining those real expressions recovers **117 words /
frame 0x28 / 13 differences**, no diagnostics or data pool. Wider local
types regress the frame; no artificial locals, volatile workaround, fixed
register, extra argument or profile change is adopted.

The [experiment](../../tools/experiments/game_record_random_drag.py) pins
the complete raw stream to SHA-256
`30113f5570a2cecb768221f05ac20b958067c946dad9d0923ef3f7f7950af76d`
and all **14 relative relocation bindings**. Normalize only register
fields at word 51 and the packed-square region 74..87. The symbolic
ordered threshold graph, HI/LO values and preserved ABI registers agree;
neither return path consumes the changed caller-saved scratch values.
No provider may inspect unpassed physical GPRs. Raw scratch return bits
are not claimed equal. Six effective dependency mutants fail; replacing
one identical square operand with the other is a valid positive control,
not an effective negative.

Word **74**, the second signed high-byte load, is unreachable: the branch-
likely at 50 targets 75 after executing load 51, while the other path jumps
from 72 past the threshold. Keep and fingerprint word 74 anyway. All **116
reachable words** execute in the qualification, with no false coverage
claim for this duplicate.

There are **117 appended rows**: **104 identity fingerprints** and **13
register transformations**. Every compiled word and binding is closed.
No instruction is inserted, omitted or moved; no opcode, constant,
branch distance, private home, frame or relocation changes. The complete
old guard file remains a byte-identical prefix. No shared header, compiler
profile, table owner or unrelated function body changes.

## Final Qualification

All **15 final tests pass in 80.861 seconds**, exit zero:

```sh
python3 -m unittest tools.tests.test_game_record_random_drag tools.tests.test_game_record_random_drag_installed -v
```

- **4,032 cases** compare normalized/retail literal model state and independently check raw/public memory, calls and result. Cover both fade paths, extreme word steps, byte modes, signed RNG zero/nonzero remainder branches, two stack phases and provider mutations. Store-side lifetime flips and incoming-home writes are guest-only probes, not portable C behavior.
- **444 fired memory-fault prefix pairs** and **six bounded aliases** compare literal state. Value 254 skips the step read; flagged mode skips the packed velocity loads, confirmed with those bytes unmapped. These are bounded guest order checks, not native fault guarantees or hardware exception evidence.
- Reject **117 raw-word flips, 117 production-padder word flips and 117 production-padder binding flips**, all fourteen changed external bindings and a changed guard predecessor. Preserve all 29 owner neighbors, their sizes/relative relocations and pools.
- **Nine compiled guest negatives** fail effectively: byte fade, byte completion, signed startup remainder, unsigned drag remainder, wrong clamp/threshold, substituted X/Z norm, wide clear and cached pre-movement mode.
- **Native32 O2 and O0, 1,048,578 cases each**, exercise all 65,536 packed velocity bit patterns, all byte fade/flag values, both lifetime paths, wrapping deltas, provider mutations and the full-word-256 boundary. The one-pointer callback type is checked, selected C uses UBSan traps, and all nine compiled native negatives fail effectively. Individual value coverage is not every possible cross-product or hardware acceptance.
- **Three independently assembled original/raw/normalized rebase sets**, including signed-low relocation carry, pass **192 cases**. All normalized original words and all call/step bindings agree; raw scratch registers are intentionally outside the public claim.
- **960 connected cases** run the actual slot-6 table, current 48-word wrapper and 69 current movement/X-scaler/Z-scaler/RNG words. Independent references check seed transitions, both coordinate/fraction updates, scaling, lifetime/completion and wrapper removal selection. The lifetime RNG and removal provider remain opaque, not falsely represented as restored engine internals or full gameplay acceptance. Negative RNG values in other tests are opaque ABI-provider cases, not possible outputs of this current seeded helper.
- The inherited word runner modeled only MULTU's low half. Complete HI/LO locally in the new oracle and verify five explicit golden products plus MFHI/MFLO, without editing shared/historical runners. Literal state here means the bounded 32-bit guest model, not full 64-bit CPU/CP0/hardware state.
- All **801 archive fingerprints**, all 67 frozen/live input gates, and effective capture/manifest/successor/image corruptions pass. Both tools copies pass Windows syntax and all eleven shared WSL padder tests; `make tools-check` passes.

The first suite exposed fixture issues, not production acceptance: its case
count was wrong, an identical-square operand substitution was equivalent,
and the byte-fade negative lacked the full-word-256 boundary. Correct those,
add explicit effective cases and exercise the second RNG's negative nonzero
remainder path. The final suite reruns all gates after the local HI/LO
completion and correction of an old label in the initially reused test
linker helper. New isolated artifacts now use **func_151707E0** consistently.
Do not report the initial failed suite as passing.

## Whole Image And Banking

The full guest rebuild matches its first pre-install prediction exactly:
**316 changed ELF bytes**, confined to the **468-byte target slot** and
symbol extent **12 -> 468**. Every other ELF byte and all **64 unaffected
inputs** are fixed, with no metadata exclusions or serialization exceptions.
Protected layout remains **189,088 bytes / 720 owners / zero differences**.

| Input | SHA-256 |
| --- | --- |
| ELF | ee728f280d139c4460bae5a35f2bf8e49a3de36d7a41b313973ca17756ad07b7 |
| Owner | 43ef53688e7c6b7332f94524c29a3c4146474e3a3b44c41a6ed2a264e9cb90be |
| Guards | 868ebf291c1ed092b1fda8220baea72fe34a41f17c93411e714567741289b840 |

The shared CSV prerequisite causes a broad guest rebuild. It exits zero
with inherited compiler and duplicate generated_12D630 recipe warnings;
target complete-owner qualification itself is diagnostic-free. Preserve
existing CRLF-prefix/LF-append CSV behavior, not a global newline rewrite.
Git checkout normalization requires explicit requalification of byte-frozen
working-copy fixtures.

Tools **bce2d08** contains only five new experiment/oracle/checkpoint/test
files. The older mirror retains HEAD **ddbdd16** and all **736 initial
dirty-file hashes**. Copy five absent owned files hash-equal, giving **741
final paths**; subsequent edits affect only those five owned additions.
Do not reset or commit that independent checkout.

Fresh official matching: **Game 2,910/4,828 (60.27%)**, **total
3,583/5,501 (65.13%)**, different **1,918**, drift **0**. Init 492/492 and
Debugger 181/181 remain exact. Conversions stay 5,501/6,044 (91.02%), byte
coverage 86.04%. README changes only its two aggregate matching rows;
detailed updates remain here and in documentation indexes.

Claude budget: **zero calls**. No push, gameplay/emulator qualification or
host-port/Release operation. Use the normal incremental Graphify hook,
preserving excluded-but-present nodes, not a forced smaller full scan.

Next **func_151709B4**, VA **0x151709B4**, ROM **0x19DE64**, frame **0xF8**.
It has **118 body instructions plus one trailing padding NOP**, **119 words /
476 bytes** in the retail slot ending at **0x15170B90**. Audit its signed
coordinates/count, float scale, byte flags, full-word context and complete factory
packet against assembly before adopting the additional source. Fold this
checkpoint's three successor hashes into a fresh experiment, preserving
historical fixtures and every broader Game/additional-source queue.
