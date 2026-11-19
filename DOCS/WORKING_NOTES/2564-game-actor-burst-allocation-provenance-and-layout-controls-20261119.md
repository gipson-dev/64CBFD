# Actor burst allocation provenance and layout controls

Date: 2026-11-19. Continue `func_150BBB5C` from Note2563. Fingerprint-locked
compiler observations now locate the descriptor address in UOPT's constant
allocation and confirm already-assigned S4 register nodes in UGEN. The
canonical591-word/frame624 source is unchanged and uninstalled. **Zero new
matching credit.**

## Compiler provenance

The existing qualified UOPT mode5/mode6 and UGEN load-node observers are
adapted to the complete owner under its unchanged O2/g3 profile. Each run
uses a newly owned compiler child, checked cc/uopt/ugen fingerprints,
completed driver/child exits and the observer's required cleanup markers.
Text, functions, relocations and pools remain identical to independently
compiled baseline objects; all eight neighboring functions are preserved.
The target remains591 words with raw SHA-256
`ed52a6efaa49f8b77cd93ab52d9f49f605329dd5ac3b0cff60eef23a1c7e5773`.

Inside the target's scoped mode5 allocation records, descriptor address
identity`43|1`, expression499, is a constant for procedure771/stack offset
-124. Its internal color is18, with forbidden colors1..6 and14..17.
Its live-range records span both factory-call phases and intervening blocks.
These are measured integer records; internal color18 is not asserted to
universally mean architectural S4.

UGEN's input load-node observer sees296 events for the complete owner,
including three already-assigned register-class nodes with raw offset80
(register20/S4). A target-stub control preserves all eight neighbors but
reduces the events to121 and has zero such S4 nodes. The emitted target
independently contains the S4 save/restore, two SP+0x1F4 initializations and
two argument copies recorded in the previous physical audit. Node visits
are not claimed to correspond one-to-one to emitted instructions.

This locates an already-made allocation choice before UGEN load handling;
it does not exhaust backend decisions or derive a fitting rewrite. The
UOPT real-number printer is suppressed. **Diagnostic timing/cost numbers
are invalid and are not used to explain the allocation.**

## Source and option controls

Ordinary and register-qualified descriptor-pointer carriers retain S4 and
shift the vector homes by four bytes. A volatile pointer carrier removes
S4, but produces590 words/frame616. Moving its existing vector declarations
recovers the passed addresses and a five-path complete normal trace for
one count pair, but the frame is still wrong. It is not adopted. Height
qualification adds nothing; width qualification regresses the ordered FP
trace. No padding object, public qualifier or physical register binding is
introduced into production.

Diagnostic options found in the pinned compiler's own option table were
also screened privately:

| Option | Target result | Scope decision |
| --- | --- | --- |
| `do_opt_saved_regs` |592 words/frame624; eight neighbors unchanged | Larger body; no installation |
| `noheurAB`, `no_r23` |Same591-word target | No improvement |
| `norlodrstropt` |589 words/frame624; eight neighbors/pools unchanged; one count-pair normal trace passes | Changes branch/constant scheduling; remains private and unmatched |
| `noprecolor` |Same target, but changes `func_150BB760` | Reject whole-owner change |

The589-word option result changes ordinary/likely branch families and its
LUI/NOP instruction counts. A shorter body alone does not establish retail
correspondence. The normal profile and canonical complete-normal source
remain unchanged. The first profile-screen wrapper stopped on the expected
neighbor-change ValueError; its corrected second run records the rejection
and completes all five screens. No claim is based on that aborted run.

## Validation and handoff

Both local tool configurations freshly run four focused diagnostic tests:
scoped UOPT records and complete-object identity; assigned UGEN S4 nodes
with the stub control; fail-closed diagnostic validation; and exact reuse
of the unchanged semantic receipts. The three rejection controls cover a
failed driver, missing driver-exit marker and changed emitted target text.

Both focused suites pass with zero failures/errors/skips and55 imported tool
hashes each; runner times are91.028s primary and98.336s sibling.
The895-file overlay contains339 matching sibling files,553 primary fallbacks,
two task files and one bootstrap. `make tools-check` passes.

The prior five-test suites from Note2563 are **reused, not freshly rerun**:
their341 imported tool hashes and task fingerprints are checked against
the1,879 frozen inputs, and the new compiler observations independently
reproduce the same target object. Those receipts retain the80-path complete
normal relation,274 guest cases/all587 retail words,384 native SDK32 cases
each at O0/O2/O3,13 relation controls and3,072 relevant caller cases.

Production source/object/ELF, original ASM, profiles, guards, protected data,
progress and root README remain unchanged. Sibling tools HEAD/dirty status
and343 dependency hashes are preserved. Detailed observations, source
screens and receipt hashes are retained in
`conker/build/game-next-150bbb5c-physical-private/`.

Total remains **4,558 / 5,514 (82.66%)**, Game **3,885 / 4,841 (80.25%)**,
zero drift; **129** more matches reach85%. No source/profile installation,
normalizer, production Make/recount or host/Release/save change is claimed.

Continue the same physical matching from the complete-normal manifest in
Note2563. Target the address-constant lifetime and remaining branch/NOP
layout while preserving the verified normal relation. Do not promote the
frame616 carrier or589-word diagnostic option merely from their smaller
counts. Padding, private-layout, strict image, actual Make, installed checks
and recount gates remain open. Keep the85% goal active and commit tools
before the consumer; no push or automatic pause.
