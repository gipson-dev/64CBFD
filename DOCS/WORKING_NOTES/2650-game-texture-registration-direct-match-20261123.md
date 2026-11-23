# 2650 - Texture registration direct match

Date: 2026-11-23. The total 85% matching goal remains active.

`func_15195DD4` replaces the zero-return placeholder in
`conker/src/game/generated_1C2C60.c`. The complete **119 words / 476 bytes /
96-byte frame** emit directly from the existing IDO O2/g3 profile, including
all symbolic bindings. **Zero new guards, insertions or omissions.** The
guard CSV, compiler profiles, layouts and shared padders remain unchanged.

Fresh production: **4,631 / 5,528 (83.77%) total**, **3,958 / 4,855 (81.52%)
Game**, zero address drift, **897 different**, **68 more matches to 85%**.
Init remains 492/492 and Debugger 181/181. Conversion rows are unchanged.

Original `conker/asm/1C2C60.s:471`, VA `15195DD4..15195FB0`, ROM
`1C3284..1C3460`. The initial graph query identified the placeholder and
its previously recovered helpers; the complete original routine and caller
provided the reconstruction evidence. No external donor was imported.

## Recovered behavior and ABI

The interface has seven full words and a full-word result:

```c
s32 func_15195DD4(s32 displayList, s32 assetId, s32 doubleSize,
                  s32 occurrence, s32 separate, s32 field12, s32 field13);
```

`displayList` carries the 32-bit guest address, consistent with the existing
owner relay. The result carries the final record address in the same ABI.
The helper's role is display-list texture registration; the earlier informal
bank-request interpretation is superseded by the recovered scanner, packed
layout constructor and association updater.

The routine returns zero for a null display-list address or nonzero
`D_800BEAC0`. Occurrence -1 starts at zero and continues searching until
failure; other occurrence values perform one attempt. A successful search
provides a command index and tile count through `func_15195868`.

An initially zero asset ID reloads `D_800E08F0`. The nonzero override flag
selects key -1 for the first list lookup; otherwise the full asset ID is
compared against each record's signed 16-bit key at +0x08. The list starts
at `D_800E08E8` and follows pointers at +0x04.

For a missing record, `func_15195984` receives the asset ID, command word 1,
command word 0 and full double-size parameter. Allocation failure returns
zero. Success stores the low bytes of the final two parameters at +0x12
and +0x13. Existing records use `func_15195A84`, whose first parameter and
result preserve the signed 16-bit command-index conversion. After either
success path the override flag is cleared.

The byte at +0x14 increases only when it is below the signed tile count,
with the original byte truncation. `func_15195D00` associates the record,
display-list address, selected index and full tile count. The final token
comparison reloads `D_800E08F0` and decrements it when equal to the retained
asset ID. Field names +0x12/+0x13 remain opaque.

The source census finds only the existing `func_15195FB0` relay as a direct
reference. The aligned literal JAL census agrees: ROM `1C3488`, VA
`15195FD8`. The complete original 16-word relay loads owner +0x1C, forwards
all seven words and returns the complete result. No other C prototype
needs changing. This census does not exclude computed/materialized references.

## Source recovery and the original first-miss bug

The first complete C body already had 119 words. Separate early-return
statements, command-word snapshots and the original byte-pointer arithmetic
recover the branch topology and register schedule. Ordering the seven real
locals recovers the frame, tile-count slot at SP+0x50 and record home at
SP+0x44. No padding variable, volatile, register directive or profile change
was introduced. A byte view of record fields permits typed native link/key
objects without pretending an opaque byte prefix is a pointer member.

Retail loads the uninitialized record home at SP+0x44 before the first
search. If that search fails, the final return uses that word. The recovered
C deliberately leaves `record` uninitialized on this path, with an explicit
source comment. **This path has no portable C return-value guarantee.**
The emitted guest instructions match retail exactly; 122 seeded-stack cases
measure the original word return, and a separately compiled zero-initializer
control fails that comparison. No native or host semantic guarantee is
claimed for this undefined C path, and it was not silently repaired.

## Fresh qualification

The nine task tools reuse the existing compiler/object, MIPS instruction,
native32, padding, data-layout and ELF helpers. All five focused gates run
fresh in each pre-install and installed setup:

| Stage | Elapsed | Tests |
| --- | ---: | --- |
| preinstall-primary | 107.096s | 5 fresh / 0 reused |
| preinstall-sibling | 129.752s | 5 fresh / 0 reused |
| installed-primary | 96.908s | 5 fresh / 0 reused |
| installed-sibling | 101.485s | 5 fresh / 0 reused |

- **816 cases per raw/padded/original stream** compare full modeled RAM,
  GPR/FPR/HI/LO state, condition, ordered access trace and calls. An independent
  reference checks public bytes, call arguments and the full result. All
  119 target words execute. Cases include repeated searches, first/later
  misses, allocation failure, list head/middle/tail/no match, signed key
  comparisons, index 32768, byte truncation, gates and helper-side mutations.
- **177 fired own-access cuts** compare complete state/trace prefixes across
  all three streams, including the first-miss seeded stack read.
- **102 cases per stream** execute the complete original 16-word owner relay,
  checking seven word arguments, the owner-bank/display-list load and the
  full return. Complete outer gameplay callers are not claimed.
- **694 native32 cases at each O0/O2/O3** use the actual recovered C with
  SDK32 types, ordinary typed link/key objects, strict aliasing and trap-mode
  UBSan. All public record bytes, display-list words, global token, full
  return and ordered service arguments match independent vectors. The 122
  first-miss undefined C cases are explicitly excluded. GCC's known local
  uninitialized warning is retained without treating it as a compile error;
  no other diagnostics are waived for the subject.
- **Eight effective native output controls** detect a gate error, omitted
  repeated mode, unsigned record key, wrong override key, narrowed index,
  wrong +0x13 byte, reversed tile comparison and reversed token decrement.
  A separate O0/O2/O3 gate-control counterexample executes one successful
  existing-record search with an initialized result; its mismatch therefore
  does not depend on the mutant entering the first-miss undefined C path.
- **12 independent GNU links / 96 guest rebase runs**, across four independent
  code/callee/global arrangements, include a low-half carry and a different
  J26 region. Direct instruction words and relocation bindings remain exact.
- Both full-owner padders preserve all **68 other function payloads**, pools
  and diagnostics. Both target-only padders match. Four wrong-word/binding
  comparisons fail. The generated padder rejects an oversized body; the
  generic padder preserves it as explicitly unmatched overflow.

Helpers in these target tests are bounded ABI providers. Their complete
semantics, hardware/MMU environments, unrestricted pointer aliases and
whole-game/host acceptance are not newly qualified. Finite test results
remain separate from the exact original instruction-and-binding proof.

The independent tools setup is a disposable overlay: **1,519 files**, 349
from identical sibling files, 1,160 explicit primary fallbacks, nine task
files and one bootstrap. The real sibling's HEAD, existing dirty state and
353 inspected dependency hashes remain unchanged. This is not a clean
standalone-sibling compatibility claim. Shared `make tools-check` passes.

## Actual Make and complete image

The private replay executes the actual Make rule's three productive commands:
IDO compilation, existing padding and GNU assembly. Its entire padded owner
equals the independent owner, preserving the 68 neighbors and every pool.
Only the target's definition extent grows from 12 to 476 bytes.

The reference image is built from frozen **old C and old guards**, first
reproducing the exact old whole owner, then replacing only the target with
independently assembled original ASM. Every named symbol and string is
reconstructed from the frozen image. There are **zero metadata permutations**.
The actual C image and production Make output equal that complete prediction:

```text
ELF SHA-256  370aca4f81e5197454282894dae2680d22f39bb10b442396fab8277cec9c5927
owner SHA   c64570c049c4272289793ab5076edf5638779c7a2ab709556384e7f6cfac8eba
```

Exactly **370 image bytes** change, with **zero exclusions**. All other
definitions/addresses/extents stay fixed. The **189,088 protected Game-data
bytes across 720 owners** remain exact. Conversion rows, original assembly,
guards, layouts, Makefile, headers, private inputs and frozen prior snapshots
are unchanged. The source, actual owner, image and task tool fingerprints
are checked again before banking the next immutable baseline.

## Documentation, graph, host and next target

Root README changes only its aggregate Total/Game status rows. This detailed
note and concise current indexes carry the narrative. Graphify's native update
is followed by a scoped AST/qualification merge with explicit old-ID retention;
it is not described as a full-corpus extraction. Actual post-commit producers
must be observed terminal before the final graph/baseline snapshot is banked.

Read-only host applicability is audited at the existing `64CBFDOGL` path.
Its inspected scene configurations consume binary artifacts, with no direct
reference to this C owner and no complete host Git/CMake root at that path.
No host build, Release artifact, save or runtime was changed or qualified.

Codex is the sole writer. Claude calls: **zero**; the direct word/binding,
semantic and full-image evidence resolve this routine without a second writer.
Tools are committed first, then the consumer pin/source/docs. Nothing is pushed.

Next retained target: **`func_15195AA8`**, the 150-word routine immediately
before the association updater. Its original fragment and exact span are
retained in `conker/build/game-bank-request-dispatch-15195dd4-private/`.
No candidate for that next target is installed or credited. Continue the
full 85% goal with **68 more qualified matches required**.
