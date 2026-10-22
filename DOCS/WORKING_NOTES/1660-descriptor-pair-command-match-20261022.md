# Descriptor-Pair Command Callback Guarded C Match

Date: 2026-10-22

## Result

Recover `func_150F07E4` in `conker/src/game/generated_11C2B0.c` from
its zero-return placeholder. Complete semantic C emits **42 words, frame24
and one call binding**. One checked guard swaps only the two registers of
a commutative `bnel`; the padded/linked routine matches all42 retail words.
This is guarded C, not compiler-only matching. No inserted instructions,
dummy locals, profile change or handwritten function emitter.

VA150F07E4..150F088C / ROM11DC94..11DD3C, ends exclusive.
Preserve the original `conker/asm/11C2B0.s` and callback-table data.
Raw unlinked C body SHA-256:
`dab79f4636f22700ae9848faf934e8c853bb6de256551d9ff4a7e2892e15e84c`.

The old body was three words/12 bytes in a168-byte retail slot. Replacing
the placeholder does not add another converted-C row or change the denominator.
Keep the address-based public symbol and use descriptive locals/purpose comment.

## Recovered Contract

Use `void func_150F07E4(u8 *owner, s32 eventAddress, u8 command)`.
The existing dispatcher's second parameter is a32-bit address word; retain
that callback interface and cast to a local byte-pointer view. The callback
has no meaningful return value and the complete caller does not consume one.

Read the descriptor pointer at owner+0x60 before testing the command.
Command zero reads event+0, then descriptor+0. Release the owner through
`func_1516972C` if these full words match, or otherwise if descriptor byte+4
matches event byte+4. Preserve short-circuiting: a word match skips both byte
reads. Do not replace this OR with an AND or narrow the word keys.

For command0x2D, capture event word+0 before reading the current descriptor
word. If the first word matches, copy event word+4 to the descriptor, then
read event byte+9 and store it at descriptor+4. Otherwise, if event word+4
matches the captured descriptor word, copy the captured first word and then
read/store event byte+8. When both words match, the first path takes precedence.
Keep those byte reads after the word stores; aliases can make that order
observable. Other command bytes do not follow the descriptor or event pointer.
The owner itself must still be readable for the unconditional +0x60 access.

Preserve the full incoming command word at original SP+8 before its low-byte
mask. Guest argument-home probes are physical ABI tests, not portable C
parameter-storage assertions. Do not pre-mask the stored word or introduce
volatile accesses to force the shape.

An ordinary shared signed local, initially the promoted command byte and later
the comparison word, reduces the first42-word form from15 register differences
to one. Unsigned-local and control-flow variants do not close the remaining
branch operand order. The historical spelling is not uniquely established.

Add the canonical `void func_1516972C(struct102 *);` file-scope declaration.
Make the two existing calls in `func_150F15F8` and `func_150F1684` explicit
pointer casts. IDO rejects the initial block-scope declaration when its later
implicit calls are encountered. All43 neighboring functions, raw/padded pools
and diagnostics remain identical; both old/new compiler diagnostics are empty.
There is no shared header or caller-source change.

## Guard And Binding

| Body Offset | Expected | Retail Replacement | Treatment |
| --- | --- | --- | --- |
| 0x084 | 0x546A0005 | 0x55430005 | Swap rs3/rt10 in the same bnel |

Both words have opcode21, displacement5 and the same target150F0880.
Equality/inequality of the two full registers is commutative. No register,
immediate, opcode, relocation, delay instruction or control-flow edge changes.
Derive the replacement from that field swap, pin the complete raw body and
bindings, and reject changed inputs. Append just one CSV row, preserving the
entire previous manifest prefix byte for byte. No insertions or omissions.

The sole binding is `R_MIPS_26 func_1516972C` at body offset0x40.
All42 static words match. Public paths visit41; the duplicate load at
150F0864 is statically unreachable and reproduced, not dynamically exercised.

## Caller And Helper Bounds

The aligned prepared retail input has one literal target pointer at ROM234428:
slot1 of `D_8008F964` at8008F968. The table is `[NULL, func_150F07E4,
func_151A8A78]`. No direct target JAL is present in that aligned input scan.
Treat this as literal-reference evidence, not a claim about every possible
computed runtime target. Graph query finds the three relevant nodes and54
adjacent edges; source, table and retail instructions establish the calls.

`func_151A8A20` is already exact,22 words/frame24 at ROM1D5ED0..1D5F28.
It reads owner byte+0x5C, clamps indices>=3 to zero, loads the callback, skips
NULL and forwards owner/address/byte-command to its void indirect call.
Execute all22 words across160 phases, including slots0/1/2/3/255 and poisoned
command upper bits. Slot2 remains an explicitly bounded provider; this work
does not restore or qualify that other handler's implementation.
Compile the actual, unchanged C dispatcher in the native fixtures as well.

Connect all28 original/current `func_1516972C` words at ROM196BDC..196C4C
across32 phases. Its first helper may mutate the owner type; verify the
post-helper byte reload, type<2 gate, stride52 callback lookup, callback and
fallback paths. `func_151696DC`, `func_15169804` and the indirect release
callback remain providers. Do not claim complete allocation/free behavior,
interrupts, hardware or natural gameplay from these bounded executions.

## Qualification

Tools: `experiments/game_descriptor_pair_command.py` and
`tests/test_game_descriptor_pair_command.py`, identical in both copies.

| Actual Run | Active Tools | Older Mirror | Errors / Failures / Skips |
| --- | --- | --- | --- |
| Full pre-install suite | 8 tests,369.649s | 8 tests,370.805s | 0 / 0 / 0 |
| Fresh installed checks | 2 tests,1.812s | 2 tests,1.783s | 0 / 0 / 0 |

Explicitly reuse the other six pre-install checks per copy only under strict
source, raw/padded object, helper, input and whole-image identity. They are not
fresh installed executions. Both shared project-tool checks pass.

- 12,288 guest phases sweep all256 command bytes, four relation patterns,
  six full-word patterns, provider mutations and two SP phases. Another224
  phases cover seven descriptor/event/home alias arrangements. Compare exact
  root access order, public state/calls and full modeled GPR/FPR/HI/LO/RAM/
  events between original, raw C and guarded C, including volatile clobbers.
- 147,456 native32 cases per O0/O2/O3 use trap UBSan, real pointer fields,
  32-bit word-backed records, byte aliases and complete arena fences. Exercise
  the real C dispatcher, all command bytes, signed-width poisons, branch
  precedence and provider effects. Native aliases use separate records or
  event views at state/state+4; deliberate guest argument-home aliases are
  not claimed as portable native layouts.
- All eight compiled wrong-C controls return the expected failure code23:
  command, OR/AND gate, forward word/byte, reverse word/byte, word width and
  alternate state pointer. Their records/pointers remain backed; no control
  depends on an undefined out-of-bounds access. The old stub is also rejected
  by an actual observable descriptor update.
- Six independent GNU links /96 phases qualify the call binding at three
  anchors. Check632 fired root-access fault prefixes, excluding provider
  accesses. These are emitted guest-state/order tests, not portable C fault
  or hardware MMU guarantees. Six guard and five strict-image corruption
  controls fail as required; there are zero metadata exclusions.
- Pin27 historical/current inputs and the old padded object. Preserve43
  neighbors and every other linked body/address. Actual Make shadow has
  three productive commands under existing O2/g3, with all44 raw functions
  and the complete padded code/metadata equal to independent qualification.

Do not count failed setup attempts. The first declaration form failed whole-
owner compilation; the corrected declaration/casts pass without changing any
neighbor. A premature test read during input copying was rejected by its hash
gate before executing any tests; the final runs are sequential after verified
copy completion.

The commit whitespace gate later removed two EOF-only blank lines from the
new Python module. Verify the full original-to-final SHA chain, identical AST
including positions, and byte-identical compiled Python code before reusing
the two complete pre-install runs. The final installed checks are fresh under
the final file bytes. This is an explicitly recorded formatting-only rebase,
not another full-suite execution or an allowance for executable source changes.

## Production And Preservation

Verify all15,810 live/cache files and all1454 linker objects using the existing
sealed Linux build copy. The only new guard row applies to this changed owner;
mark the independently verified manifest old for other Make dependencies to
avoid unrelated recompilation. Preserve all other object/input bytes.

Actual production Make exits zero in0.485s. The installed ELF exactly equals
the independent prediction: **113 changed bytes =112 instruction bytes +one
target symbol-size byte**, zero exclusions. Target extent changes12->168 bytes
inside its original slot; ELF length stays3,257,124. All other6054 function
bodies and all6055 addresses remain fixed. No overflow body is moved/removed.
The inherited duplicate generated_12D630 recipe warning remains; compiler
diagnostics for the changed owner are empty.

Installed ELF SHA-256:
`f8c55e69ec6b971d1d6c8b9178ad99763ec468034df57481dbfc1c3eaf587138`.
Installed owner object SHA-256:
`1ce1dbc5cbf5736ec084c0ee542fdd826a68b44683c1df82b6d3196d38bd6f93`.
Protected Game data remains exact:189,088 bytes /720 owners, SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

Recheck live inputs before/after adopting only the target object, ELF,
generated linker script and progress CSV. Source/guard edits are checked
against the qualified reconstruction, never overwritten by adoption.

Tools commit `9b32c4ebe0246d7170f86e8819b9a6657d4c268e` precedes the
consumer source/CSV/docs/pin commit. Preserve all1532 old mirror dirty statuses
and hashes; add only two task files, totaling1534 paths. Do not commit, reset,
clean or stash that older mirror. No push, Claude call or host change;
Release stays frozen. Root README changes only two aggregate rows.
Refresh Graphify, wait for its actual processes and audit every old node's
retention/unique relocation. Do not call the filtered scan a full re-extraction.

## Measured Progress And Resume

The literal standard matcher exits zero against the adopted live ELF:

| Section | Byte-Exact Converted C | Address Drift | Still Different |
| --- | ---: | ---: | ---: |
| Total | 3,728 / 5,505 (67.72%) | 0 | 1,777 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 3,055 / 4,832 (63.22%) | 0 | 1,777 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

The75% threshold remains4129; **401 more exact functions** are required.
The goal remains unfinished. The refreshed ELF-pinned queue has1646
placeholders,122 semantic/other definitions and nine unlocated entries.

Next: `func_1514F640`,42 words/frame40, existing placeholder/39 differences,
in `conker/src/game/generated_17CAF0.c`, original `conker/asm/17CAF0.s`.
VA1514F640..1514F6E8 / ROM17CAF0..17CB98, ends exclusive. Establish caller/
helper ABI, output tag2, source+0x20 snapshot, three output-vector pointers,
helper-success gate, float-return sign test and ordered XYZ negation.
Preserve saved S0, the real SP+0x24 pointer home, source incoming home,
aliases, NaNs and signed zeros before fitting. Screen only: no source edit,
compilation, adoption or matching credit. Keep the862-word `func_1508CAD8`
owner stub queued separately.

Private snapshots, probes, native fixtures, images, queues, format receipts
and audits remain under `conker/build/game-descriptor-pair-command/qualified/`.
