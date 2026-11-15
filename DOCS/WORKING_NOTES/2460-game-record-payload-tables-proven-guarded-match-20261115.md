# Game record payload tables: proven guarded match

Date: 2026-11-15. `func_15017114` is adopted as semantic C and matches its
complete **121-word body**, with the original **two alignment words** retained
in the **123-word slot**, VA **0x15017114..0x15017300**, ROM
**0x445C4..0x447B0**. The original **frame 0x48**, **six S0..S5 saves** and
**metadata output SP+0x40** are preserved. Ten expected-word/binding guards
restore the captured-count schedule; there are no inserted or omitted words.

This completes **all three functions in `generated_43D00`** after
[Note 2459](2459-game-category-record-initializer-proven-guarded-match-20261115.md).
Actual production recount: **4,498 / 5,515 (81.56%)** total,
**3,825 / 4,842 (79.00%)** Game, zero drift and **1,017** different.
Init stays **492 / 492**, Debugger **181 / 181**. Converted counts/bytes are
unchanged. The 85% goal remains active: **190** more matches reach 4,688.

## Source behavior and the native sequencing correction

The routine captures the byte-sized record count, allocates a pointer table
and status bytes, clears both using the captured lengths, allocates/clears a
16-byte payload for each player and sets its status to 2. It then loads optional
category metadata and resolves appended records' relative offsets/statuses.
`RecordPayloadMetadata15017114` names the two 32-bit metadata fields. The
recovered interface is `void func_15017114(s32 category)`; the original
address-named symbol and semantic comment are retained.

The first signed-count draft emitted 120 words. Recovering `u8 count` and its
declaration position produces **121 words**, original saves and the original
SP+0x40 output home. The full raw body has **21 binding sites** and SHA-256
`0bba44a9eebb3f0da289846a6d8c0c90e74fb293ba14a57f51989d596784f10c`.
Both other raw owner functions and their 336-byte literal pool are unchanged.

Native testing found a substantive source issue even though IDO's MIPS output
already had the right memory order. In
`D_800D2104[index] = allocate_memory(...)`, GCC O0 evaluated the destination
table address before calling the allocator. A provider that rebinds the table
then left the following clear using the wrong table. The owned debugger run
stopped in `bzero`, `candidate_0`, case 264, call 6. This was a private candidate
failure, with no production installation or match credit.

The corrected source first captures `playerPayload`, then reads the live table
and stores it. This makes the provider-before-destination order explicit in C.
It changes **none of the 121 emitted MIPS words**, frame or homes. Fresh
O0/O2/O3 validation passes after this correction. The owner header is also
updated to describe recovered code rather than placeholders.

## Scheduling proof and stale-input controls

- [x] The pure normalizer pins all 121 source words and 21 bindings. It
  reorders the first allocation's argument/copy schedule, uses S0 for the
  captured byte count and retains that count in S3 through the second clear.
  All **142** raw-word/binding corruption controls reject changed inputs.
- [x] An independent symbolic prefix executor compares ordered public reads,
  writes and opaque helper packets, every private home, saved entry values,
  live GPRs and FPR/status state. Four-register helpers own only SP+0..0xF;
  the saved S0 at SP+0x14 is protected.
- [x] The **85-word suffix is identical**. Two control-flow cuts prove that
  differing incoming S3/S4/RA values are overwritten before use. This closes
  the entire function from the equal live state without modeling a different
  metadata loop or assuming mutable public arrays/globals are disjoint.
- [x] Three supported-instruction controls reject the wrong count read,
  captured-count copy and clear length. A second valid allocation using S4
  for the temporary also passes, independently of the retail register colors.

The normal-execution contract uses valid mapped storage and ordinary o32
arguments. Providers may change mutable public data and caller-saved state;
they do not inspect implementation code/PC, implicit register inputs or
unpassed private locals. The later explicitly exposed metadata output and its
alias behavior keep their original instruction suffix and stack home. Full raw
fault state, helper internals and general C portability are not claimed.

## Guest, native and original caller qualification

- [x] **424 cases / three streams** pass: original retail, independently based
  raw C and actual normalized owner code. All **121 retail words execute**.
  Cases include all 256 count bytes, signed player bounds, provider table/count
  changes, zero/nonzero metadata offsets, absent output writes and three
  alias forms. One alias modifies the explicitly passed private metadata pointer
  through the status destination; its subsequent reload is checked.
- [x] Complete public bytes and helper-entry SHA snapshots agree, as do saved
  GPR/FPR state and SP. Three effective guest controls reject the missing
  output initialization, wrong clear length and pointer destination.
- [x] Fresh GNU native32 **380 cases per O0/O2/O3**, with **six effective C
  controls per profile**, pass with undefined-behavior traps. SHA snapshots
  cover all **21,025 public bytes**, including unused bytes, globals/padding,
  both pointer/status/metadata backings, payload buffers and the marker.
  Two known SHA-256 vectors and a null-pointer canonicalization check pass.
- [x] Native storage holds 256 records, 128 player buffers and 1,024 metadata
  records per backing. Native excludes the three guest alias forms; guest
  alias/physical-address behavior is not inferred from these native runs.
  The enclosing tests verify all frozen include inputs as well.
- [x] Native receipts pin candidate/model/fixture/SHA-helper/reader/writer/
  compiler, exact profiles, generated C and executable hashes. Changed-profile
  and changed-executable controls reject stale receipts. The final mounted
  suite runs native freshly; the sibling overlay explicitly reuses matching
  receipts rather than claiming another fresh native run.
- [x] The aligned census finds one direct call at ROM **0x43F80**, no literal
  function pointer. **48 original four-word caller windows / two streams**
  preserve the category stack load, count addition and count-store call delay.
  Two caller mutations are rejected.
- [x] The original continuation at **0x15016AD8** reaches
  `allocate_memory -> func_10003C6C`. A **30-instruction** checked prefix proves
  old V0 is overwritten at **0x10003CA8**, before any read. Forwarded-result
  and removed-overwrite controls reject. Full parent/allocator execution is
  outside this bounded interface proof.

The fixture checks also caught and corrected a public metadata arena that
overlapped the simulated stack, and a null/private-output address-map collision.
The accepted layout asserts disjoint initial public/stack ranges; superseded
private reports are retained and do not supply qualification credit.

## Build, image, preservation and commits

- [x] Both complete-owner padders agree across **12 GNU links / four layouts**,
  including independent code/data rebases and low-half carry cases. All three
  owner functions, bindings and the two final alignment words are retained.
- [x] Three actual Make recipe commands reproduce the independent owner.
  Private whole-image prediction and production Make produce the same ELF:
  **366 changed bytes, zero metadata permutations, zero exclusions**.
- [x] All **6,051 function addresses** stay fixed; only this target body/extent
  changes. Of **698 objects**, only `generated_43D00.c.o` changes, in `.text`,
  `.rel.text`, `.symtab` and `.strtab`, matching the predicted object. Both
  owner neighbors and padded pools are fixed.
- [x] All old guard bytes remain an exact prefix, with ten rows added only
  for this target. Makefile, conversion rows and the other **808 / 812 frozen
  inputs**, including **80 headers and two include files**, remain fixed.
- [x] All **189,088 protected bytes / 720 data owners** are exact, SHA-256
  `0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

Production ELF SHA-256:
`28c1c612e534766e74d3b6f37c4aa93a93178fb229d973fd17883e2c6c1e134e`.
Canonicalizing one final blank line rebuilds to the same predicted object and
complete ELF. The final installed suite passes in **109.727 s**, including
fresh native profiles; `make tools-check` and scoped Git whitespace checks pass.

An ignored sibling overlay contains **11 byte-identical files**: nine task
files and two unchanged shared proof/SHA dependencies. It passes **76 guest
cases / three streams**, **48 caller cases / two streams**, proofs and both
padders. Native receipts are reused with exact fingerprints. Windows Git
records unchanged sibling HEAD `ddbdd16b53ce60b054fb6e11bf0649a41f48375a`,
**2,434 dirty paths**, and byte-identical before/after status with SHA-256
`a3712de44f2fc37079df4a789a5015f134f6ab977a2c2da90a3fde1851606cd9`.
This checkpoint uses Windows Git counts, rather than the older WSL snapshot;
no files in the real sibling checkout are overwritten or committed.

Tools commit **`495f553a12f0d1e7d2d87fac1c4e004a225e3e2b`** precedes the
consumer source/guard/pin commit. Detailed snapshots and receipts remain in
`conker/build/game-record-payload-tables-15017114-private/`, including
`qualified-private-match/`, the earlier 120-word draft and the pre-sequencing
candidate/debugger result. No push and no host build/Release action.

Graphify refresh is a scoped AST merge of **11 files**, retaining all
**61,316 old IDs**, zero loss; **61,316 nodes / 115,163 links**. This is not
full-corpus extraction. Routine Claude calls: zero. README changes are only
the two updated aggregate matching rows.

## Resume

The next small mismatch is **`func_151F8870`**, 47 words in
`generated_225D20`. It reads custom T0/S0/S5 state and updates A0/T0/T1 as well
as V0. Audit its handwritten assembly classification and callers before
choosing a C representation or restoration. Similar custom/shared-entry code
also appears in `func_150A613C`, `func_150AE280` and `func_150183D0`; shortest
word count alone does not make these ordinary o32 C candidates.

The common particle updater stays private and uncredited. Continue toward the
full 85% goal, with 190 more matches currently required.
