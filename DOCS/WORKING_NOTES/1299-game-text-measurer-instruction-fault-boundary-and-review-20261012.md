# Game Text Measurer Instruction Fault Boundary And Review

Date: 2026-10-12. Continue func_150428D4 after
[Note 1298](1298-game-text-measurer-seven-save-lifetime-qualification-20261012.md).
Original VA 0x150428D4..0x15042C40 / ROM 0x6FD84..0x700F0, 219 words /
876 bytes, frame 0x80. The Game goal stays active, same target. No production
installation or matching credit; nested flag-branches-captured222/0x80/146
remains the next fitting seed, not a final accepted body.

## Baseline And Bounded Fitting

Entry consumer 4c3b13c9b345d59f94de2df3ed323a9084becc95 and mounted tools
fb5162b566040ba0038ed69ae120858aa2567f5f were clean. Previous turn was progress:
seven-save qualification changed the fitting seed. Codex remains sole writer.
No OGL/Release build/change, ROM/save/config/editor/debugger mutation, compiler
or package installation, push, reset or independent older-history commit.

Compare complete original/candidate instructions with mnemonic alignment to
locate zero-assignment/branch-delay/read-order differences. Alignment is not
word-match proof. All 25 new source screens use the unchanged owner profile
-O2 -g3 -Wo,-loopunroll,0. None is an accepted original fit.

| Screen | Words / Frame / Differences | Finding |
| --- | --- | --- |
| Normalize through existing extent; four subword flags; non-escaping struct flag | 218 / 0x80 / 174 | No improvement |
| New post-call scalar and comma form | 220 / 0x88 / 133 | Extra frame/save, not selected |
| Branched post-call merge | 224 / 0x88 / 141 | Wrong frame/length |
| Reuse index for post-call capture | 218 / 0x80 / 211 | Wrong roles, not selected |
| Array flag | 222 / 0x80 / 164 | Unwanted SP+0x4C traffic |
| Switch capture / branches | 218 / 0x80 / 173; 222 / 0x80 / 151 | No original fit |
| Drop unreachable out-of-range zero assignment | 223 / 0x80 / 193 | Worse roles/length |
| Named font record or explicit unsigned casts | 222 / 0x80 / 146 | No change to fitting seed |
| Staged font reads, volatile or plain | 222 / 0x90 / 156 | Read order recovered, frame wrong |
| Outer staged font locals | 222 / 0x90 / 151 | Still wrong frame |
| Reuse flag/extent in font payload | 222 / 0x88 / 174 | Wrong frame, metrics homes shift |
| Automatic scalar spill, five/six-field record | 216 / 0x88 / 206 | No accepted spill/layout |
| Reuse font inputs, narrow/wide | 220 / 0x80 / 216 | Wrong roles |
| Reuse input parameter through font payload | 221 / 0x80 / 178 | Wrong roles/length |

The first aggregate generator accidentally renamed the record member
declaration as well as the scalar. Protect both the field declaration and
references during replacement, then recompile both aggregate forms cleanly.
Do not interpret that initial syntax failure as compiler-allocation evidence.
Read-order screens are only isolated measurements, not transferred public/
private/native/owner qualification. No profile swaps, dummy state or broad
retail-word guards are added.

## All Instruction Access Cuts For Named Calls

Add test 19 using the same complete actual helpers and original data fixtures.
Compile/link the current222 seed at diagnostic entry 0x152428D4. Independently
GNU-assemble and link the complete original219 at that same entry, retaining
the helper/global addresses. Assert all 219 original words still equal ROM.
Both target bodies are away from the fixed normalizer, with no overwritten
code maps, manual instruction projection or helper hooks.

Sharing the target code base prevents a simple rebase from making every
post-call RA value look different. At each first rejection below, explicitly
assert RA equality before attributing the difference to T0.

Run the complete original/candidate/reference normally for A, space, newline
and A8, at phases 0/8. Public memory/calls agree and both bodies have the same
number of actual memory accesses. Then inject a fired fault at every access
ordinal, compare RAM/events/GPR/FPR/FP-condition state and verify fault counts.
Also execute each terminal ordinal as a no-fault control. There are 768 fired
pairs, covering all cuts of these eight named executions, not all inputs.

| Input | Accesses Per Execution | First Different Cut | Original / Candidate T0 |
| --- | ---: | ---: | --- |
| A | 56 | 26 | 0 / 50 |
| Space | 38 | 15 | 0 / 1509949448 |
| Newline | 136 | 110 | 0 / 50 |
| A8 | 154 | 110 | 0 / 50 |

At every first difference, complete RAM/events still agree and RA is equal.
Only GPR8 differs for A/space/newline. A8 also differs in GPR10/11/12 because
the outgoing-argument/flag-store schedule differs. Dispatched instructions:
A/newline original 0x924F0000 versus candidate 0x924D0000; space 0x8E290000
versus 0x8E280000; A8 0xAFAC0014 versus 0xAFA00068.

The actionable boundary is before the first post-normalizer memory access:
retail resets the normalizer's remaining T0 value, while the late-V1 seed
does not. Merely reproducing seven saves and the first13 words is insufficient.
The 28 early equal fault pairs in Note 1298 remain true, but do not qualify
the later flag lifetime. This is an effective rejection, not a full private/
FCSR/hardware-fault or matching claim. PC/EPC and complete FCSR are not modeled
by this comparison.

## Observer Control And Fixture Correction

InstructionFaultMeasurer only records the word dispatched to execute. Keep
the inherited argument observer: RendererOracle.arguments already uses
non-gated peek, so call-argument inspection is not a guest memory operation.

The first test20 incorrectly expected that existing observer to fire an access
fault; its focused/full runs fail, including the 80.508-second full run.
Inspect the actual inheritance, remove the redundant observer override and
correct the negative control. Test20 now verifies six-argument observation
does not alter memory/events/registers/FP-condition or consume access zero.
Deliberately replace peek with gated get in a disposable instance; that bad
observer fires before any instruction is dispatched. The real instance fires
only at the original first saved-register store. Both final new tests pass.
No shared oracle implementation or production defect is claimed/fixed.

## One Packet-Only Review

Decision: one unresolved source-lifetime question, budget 1, attempted 1,
completed 1. Existing Claude Code 2.1.218 auth status confirms claude.ai /
firstParty / Pro, with no API-key/provider overrides. No account, provider,
billing or model switch. Use the existing default model; emitted init reports
claude-opus-4-8, tools=[] and mcp_servers=[]. Safe mode, strict MCP selection,
plan permissions, disabled tools/skills/browser and no session persistence.
No permission bypass, bridge installation or reviewer repository access.

An ignored one-shot runner assembles the fixed packet from complete target
ASM/C plus the exact delta and prior rejected cases. Packet/answer/stream/
receipt live under conker/build/game-text-measurer-review-20261012/.
Packet SHA-256 be88872908af44b4513d8f93297b3b2dcf8f5091e1bb6066aaa53753600b283b.
The receipt reports one turn, no tool-use/server requests and 137430 API ms.
Reported usage: input2, cache-created8323, output9478, cache-read0 tokens.
CLI total_cost_usd is 0.326614; it is not a verified billed API charge on the
existing OAuth subscription. No retry or persistent automated integration.

Accept the review's directly verifiable T0 lifetime description and existing
failure modes. It proposes no new edit. Reject its stronger claim that the
tested forms exhaust all sound C transformations or prove an allocator-policy
gap: it supplies no exhaustive proof. The new fault test independently locates
the real missing reset. No review suggestion is installed by agreement.

## Verification And Bank

Final 20 focused tests pass in 78.829 seconds, no skips. New 19/20 pair passes
in 2.406 seconds after correcting the fixture. Consumer/mounted/older ROM-free
tool checks and Windows py_compile pass. All nine frozen production inputs
and 189,088 data bytes/720 owners remain exact; source/ELF/guard/Makefile and
matching/conversion aggregates are unchanged. Root README unchanged.

Bank mounted tools faec3b7044986f0c0a0b51ccc36556c20da0e014 before consumer
docs/workflow/exact gitlink. Older HEAD ddbdd16b53ce60b054fb6e11bf0649a41f48375a,
dirty357 and all 80 fingerprints are checked before two task-file copies;
78 other hashes and old history remain preserved. No older commit or push.
Final reporting requires clean active repos and a fresh terminal post-consumer
Graphify Rebuilt receipt, advanced log bytes/UTC and zero native workers.

Post-documentation immutable/corruption checks pass in 1.580 seconds; all
4,477 relative links across eight checked documents resolve. Standalone
Graphify update exits one on protective shrink refusal (18,325 candidate /
40,103 saved nodes); retain 19,398 excluded-but-existing nodes from 2,972 files.
No force/purge or package update.

## Continue Same Target

Recover shared T0 zero initialization before the measured post-normalizer
read/store boundary, its call-only SP+0x68 spill and the full219 original
control flow/load/scheduling. Keep nested222/0x80/146 as the fitting seed and
captured218 as the previous reference. No broad word-copy, profile, padding
or overflow substitute. Requalify the final private/fault/native/full-owner/
padder/independent-link/rebase/literal whole-ELF/data/old-guard-prefix gates
before installation and fresh README numbers. Then func_150417AC, 1,098 words.
Full Game matching and independent hardware/FCSR/renderer/gameplay remain open.
