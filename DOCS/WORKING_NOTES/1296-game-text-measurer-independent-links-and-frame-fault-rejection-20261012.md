# Game Text Measurer Independent Links And Frame Fault Rejection

Date: 2026-10-12. Continue func_150428D4 in
conker/src/game/generated_6E770.c, original VA 0x150428D4..0x15042C40,
ROM 0x6FD84..0x700F0: 219 words / 876 bytes, frame 0x80. This checkpoint
adds independent relocation/link proof and a fired partial-state rejection
gate after [Note 1295](1295-game-text-measurer-flag-lifetime-and-owner-qualification-20261012.md).
It is not a match or installation. Production stays at the zero-return
placeholder/199 differences; no matching/conversion credit. Keep the same
target and the full Game goal open.

## Baseline And Bounded Source Screen

Consumer 9bde559641fdeae18eb089c5d449ea628889e8c7 and mounted tools
ce4cc1a796a7fc9a38fa3903c34ebb7b798f4157 were clean at entry. Codex sole
writer, zero Claude calls. Verify live checkout/notes and query the existing
graph. No OGL/Release change/build, ROM/save/config or editor/debugger
mutation, compiler/package/account/bridge installation or push.

Screen scoped/initialized flags, signed/unsigned and register/subword forms,
branch-result predicates, explicit promotion lifetimes and source-local
helper callbacks under the unchanged profile. None is an accepted original
fit; do not replace the preferred capture-declaration-after-record candidate
just because a longer form improves positional word score.

| Form | Words | Frame | Differences | Finding |
| --- | --- | --- | --- | --- |
| capture-declaration-after-record | 218 | 0x80 | 174 | Previous preferred qualified baseline, still extra S7 |
| flag-scope-boolean-reload | 220 | 0x80 | 152 | Two extra normalization operations, still saved flag |
| flag-scope-post-normalize | 219 | 0x80 | 212 | Length fits but lifetime/save layout does not |
| flag-branches-captured | 222 | 0x80 | 146 | Too long, not selected/qualified |
| flag-width-indexed-u8/s8/u16/s16 | 216 | 0x78 | 203 | Wrong frame, no accepted improvement |
| callback-lifetimes-2 | 220 | 0x88 | 160 | Wrong frame/length, not selected |
| eligibility-logical | 226 | 0x88 | 213 | Wrong frame/length, not selected |

Volatile/register forms add memory accesses rather than recovering the
original register-only flag between calls. Explicit predicates/callbacks
also do not justify new production flags or dummy state. Current preferred
body remains 218/frame0x80/174, with S0..S7/RA instead of S0..S6/RA, and
S3 flag/S4 glyph instead of retail S3 text/glyph and T0 flag.

## Independent Assembly And Links

Add test_14_independently_linked_original_candidate_helpers_and_real_pools
to tests/test_game_text_measurer_recovery.py. Assemble the full original
219-word routine and both actual helper bodies from frozen ASM, using the
existing asm-processor prelude for jump-label macros. Preserve the normalizer's
three original zero words outside its 65-word body, for the complete 68-word
slot. Metrics remains the complete 115-word routine.

Compile the captured C candidate, then run the actual generated-object padder
without any target guards. Link original and candidate separately with shared
assembled helper/data objects, not manually patched words or helper hooks.
Build the 19-entry table from its original ROM offsets using R_MIPS_32 entries
to the linked metrics function. Retain the actual five float bit patterns and
96 lookup bytes: 95 searched bytes plus original alignment. Font-pointer and
scale cells are controlled fixtures, not claimed original data values.

Use three independent ELF layouts:

| Measurer Entry | Lookup Bytes | Metrics Pool | Font Cell | X/Y Scale Cells |
| --- | --- | --- | --- | --- |
| 0x150428D4 | 0x80085930 | 0x80098AB0 | 0x80085994 | 0x800380A0 / 0x800380A4 |
| 0x15287FFC | 0x80107FFE | 0x80327FFC | 0x80407FFC | 0x80507FFC / 0x80508000 |
| 0x15318004 | 0x80218004 | 0x80318004 | 0x80418004 | 0x80518004 / 0x80518008 |

Helper code entries move by the same delta as the measurer. Lookup's first
four byte-label references and the scale pair cross a low-half boundary;
all table pointers follow linked code and all float-global relocations follow
the actual linked pool. At retail addresses, rebuilt original219 and both
full helper slots are byte-exact against ROM. At every layout, both ELFs have
identical helper/table/float payloads, verified before execution.

Run 512 all-byte/two-phase cases and six bounded private flag-home cases at
each layout: 1,554 complete original/candidate pairs. Compare public memory
and actual helper-call sequences against the independent reference; private
SP+0x68 output triples agree in the six named cases. No all-private/FCSR/
hardware or word-match claim follows from these results.

The first harness assembly lacked the existing jlabel macro prelude. After
adding it, the first link correctly rejected default .text's 16-byte tail
rounding: it overlapped the fixed next helper by four bytes. Use dedicated
four-byte-aligned .text.measurer sections, retaining all 219 slot words,
rather than changing helper addresses or weakening baseline byte checks.
The padder uses a .section directive, not bare .text; assert and rewrite that
single section declaration in the disposable assembly. No padder/library
source or production layout was changed.

## Fired Frame Rejection

Add test_15_fired_frame_fault_rejects_extra_saved_register_lifetime using
the existing access-fault oracle. Two phases and two fault positions give
four pairs. Confirm the exception fires and the access counter equals the
requested index before interpreting partial state.

Before the first access, complete partial RAM/events/GPR/FPR state agrees.
After the first completed store, it does not: original frame SP+0x38 contains
incoming S6 (register22), candidate incoming S7 (register23). This is observed
with ordinary A and canonical public output pointers; it does not depend on
synthetic private output aliases. Public final-output equivalence is not
sufficient to claim the original saved-register lifetime.

This is a rejection witness at the earliest frame divergence, not a complete
fault sweep or a native/portable hardware-fault result. Do not check off full
fault or private equivalence. Retain the six flag-home witnesses and the
earlier effective late-reload negative when selecting the next source fit.

## Verification And Bank

Fifteen final focused tests pass in 53.503 seconds, no skips. Receipts:
conker/build/game-text-measurer-recovery-test/independent-links.json and
frame-fault-rejection.json, alongside all earlier native/public/owner gates.
Consumer/mounted/older ROM-free tool checks and Windows py_compile pass.
No source/ELF production build or installation is performed.

All nine frozen inputs remain byte-exact: source, entire ELF, guards, progress
CSV, Makefile, original slice ASM, lookup data, metrics pool and retail layout.
Protected data stays 189,088 bytes/720 owners, zero differences, SHA-256
0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670.
Source 802b4d27659c80620c2ca509df4c3da84d136c5c92b758d7a6390c4428d2273d,
ELF 978d39eab009d4134e5c03d4bdd2d433010812544a5be599c823fdff1ce2aa14,
guards 3f12cf872b84100963934734de2e67f5f07073ce3112ccbd2e5c4cb8af84666e.
Preserved counts: Game 2,813/4,823, total 3,486/5,496, Init 492/492,
Debugger 181/181, zero drift / 2,010 different. These are unchanged prior
measurements, not additional matching credit. Root README remains unchanged.

After updating the indexes, the two frozen-production/corruption gates pass
again in 1.485 seconds. All 4,457 relative links in the six updated documents
and unchanged root README resolve; git diff --check passes.

Bank mounted tools 44bec83c849fa072ca6d64c75fd7dbe1fa5929eb first, then
consumer docs/exact gitlink, no push. Preserve older standalone HEAD
ddbdd16b53ce60b054fb6e11bf0649a41f48375a and all 78 other hashes; verify
the two known files before identical updates. No new mirror files, final80
hashes/dirty357 unchanged; no older history commit/reset. Require clean active
repos and a fresh terminal post-consumer-commit Graphify Rebuilt receipt,
advanced log bytes/UTC and zero native workers before final reporting.

The standalone native Graphify update exits one on protective shrink refusal:
18,308 candidate nodes versus 40,077 saved. Preserve 19,398 excluded-but-
existing nodes from 2,972 files; no force/purge or package/skill update.

## Continue This Same Function

1. Recover original S3 text/glyph reuse, T0 flag and S0..S6/RA save lifetime,
   including SP+0x68 capture/reload before width writes. The new fired-frame
   gate must stop rejecting the first completed store; do not silence it.
2. Fit all 219 original words/frame 0x80, not a 218-word compatible/padded
   substitute. Avoid dummy state, profile swaps or broad 174-word guards.
3. Re-run native/public/owner/padder and independent-link gates on the final
   selected fit, then complete full private/fired-fault and literal whole-ELF/
   old-guard-prefix qualification. Only then install, measure fresh totals,
   update README aggregate rows and bank tools before consumer source/pin.
4. Then recover the remaining 1,098-word func_150417AC formatter. Full Game
   matching, guard removal and independent hardware/FCSR/RSP/RDP/renderer/
   gameplay acceptance remain open.
