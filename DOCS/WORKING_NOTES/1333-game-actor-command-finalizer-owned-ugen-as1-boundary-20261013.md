# Game Actor Command Finalizer Owned UGEN/AS1 Boundary - 2026-10-13

## Scope And Result

Resume consumer `4190d704` / tools `2b16f4f` from
[Note 1332](1332-game-actor-command-finalizer-primary-jitter-load-order-restoration-20261013.md).
Both active trees are clean. Previous goal turn made source progress; this turn
qualifies a new compiler-boundary discriminator. Continue the same complete
func_15034860, ABI, prepared compiler and O2/g3/MIPS2/o32 profile. Zero Claude
calls, compiler installs/changes, game/runtime/Release work or production edits.

**Production stays405 words/frame0x48/267 differences, still non-matching.**
Primary cut10 GPR7 and disabled-primary cut7 T3/T9 remain open. No guards,
profile changes, binary normalization, installation or matching credit.

## Fired Backend Observations

[Backend helper](../../tools/experiments/game_actor_command_finalizer_backend_trace.py)
adapts the existing qualified UGEN transport through scoped adapters. Prepared
cc/uopt/ugen fingerprints must match before native addresses are used. Observe
only newly owned compiler children; no existing debugger attachment, target
execution or deliberate memory/register writes.

The f_load_cse probe at native0x430480 fires200 times in each body. Additional
read-only native-entry observations fire30 times at f_emit_ri (0x431550) and38
times at f_emit_rob (0x435AB0). Capture raw argument registers/caller addresses;
do not mistake these method-call sequences for final instruction ordering.

The first adapter attempt recurses before GDB launch; fix by retaining the
original script generator before patching it. An initial64-bit branch entry
at0x43C550 is installed but unfired. Reject that route rather than interpreting
absence. The successful f_emit_rob probe observes memory operands, not branch
emission. Keep this distinction explicit.

Both drivers and every child exit0. Require probe installation, nonempty events,
UGEN exit, removal before AS1, actual AS1 capture/exit and driver exit in order.
Normal and observed objects agree in full text, functions, relocations and the
union of rodata/rdata/data/sdata/literal/bss/sbss pools. Both are non-installable
diagnostics, including the lower-score early body.

## Actual Producer/Consumer Boundary

Read the actual AS1 command line at owned exec. Copy only regular /tmp/ctm
inputs into the ignored task directory before the driver removes them. Verify
exact profile/ordinal/file provenance, lengths and SHA256; reject symlinked or
non-regular capture destinations. Inputs are the10048-byte binary-assembly
stream and its73748-byte current /73672-byte early symbol sidecar. Sidecar bytes
remain raw; path/timestamp-dependent digests are not instruction equivalence.

Decode only observed16-byte big-endian instruction records and cross-check
fields against all68 raw immediate/memory emitter events. Do not assign
unobserved opcode meanings. The argument-created lower immediate has the same
sequence index10 in both bodies, but the **actual AS1 input** differs:

| Body | Words / Frame / Differences | Lower=40 Input Record | First T4 Tag-Home Record |
| --- | --- | ---: | ---: |
| Committed current |405 / 0x48 /267|184|189|
| Rejected early lower |405 / 0x48 /261|165|189|

The unique correlated lower record is opcode41/register7/unused-register72/
word3=40. Current stream SHAcbf1bb11; early stream SHA0e08c42f. The current
record follows numeric conversion/narrowing; early lower precedes the numeric
byte load. The tag-home load appears later in both input streams, despite
AS1 moving it earlier in the final code. Thus the first observed ordering
difference already exists upstream of AS1; this does **not** prove AS1 has no
remaining scheduling role or identify every earlier pass's cause.

[Tag screen](../../tools/experiments/game_actor_command_finalizer_tag_schedule.py)
tests14 complete bodies guided by that boundary. Inline tag capture leaves267
unchanged; joined tag/lower captures reproduce261 and lose primary cut9. The
volatile-home forms overflow406 words or lose earlier represented states;
constant-operand tag captures regress278..314. No eligible production fit.

## Qualification And Bank

[Focused tests](../../tools/tests/test_game_actor_command_finalizer_backend_trace.py)
reuse existing transport controls with scoped adapters. Eight initial tests
pass44.360s. Final eight diagnostic tests plus target whole-image/protected-text
integrity/corruption tests pass together: **11 tests in10.548s**, no skips.
Effective controls reject missing/unfired/late probes, bad child/driver exits,
malformed register nodes, changed compiler fingerprints, text/functions/
relocations/every protected pool, wrong AS1 profile/ownership/length/digest,
incomplete16-byte records and disagreement with actual emitter arguments.

Both local tools checks, both Windows syntax checks and scoped whitespace pass.
The previous full15-test semantic/slot/home/owner/rebase/parent receipt in
Note1332 remains prior unchanged evidence, not a freshly rerun broad suite.
Source/ELF/guards/progress/Makefile fingerprints remain fixed. Do not rebase the
protected text ELF pin or historical manifests for this diagnostics-only turn.

Source SHA76c0c333 and ELF SHA9c75bf09 remain exact. Fresh matching stays
Game2823/4823 (58.53%), total3496/5496 (63.61%), zero drift/2000 different;
conversion5496/6044 unchanged. Root README date/aggregate rows already agree.

Tools `3fb2ea0` are committed before the consumer docs/gitlink. Mirror only
three absent task files; older HEADddbdd16b and all416 saved existing hashes
remain fixed, dirty416->419. No older commit/reset/stash or push. Verify current
relative links, terminal commit hook and post-bank integrity before closing.

Continue the same function: recover the source/optimizer/UGEN ordering between
the numeric byte, tag-home read, lower immediate and unsigned conversion,
keeping retail's first14 words and closed cut9. Then repair disabled-primary
cut7 and all267 remaining differences under complete private/fault/owner/
rebase/image gates. Do not retry the unchanged14 forms or52 prior hints as new
evidence; keep wider Game/text/translator/hardware goals open.
