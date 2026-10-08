# Game Sphere Callee Allocation Match

Date: 2026-10-07. Baseline: `0d5e224c`,
[Note 1085](1085-game-sphere-callee-frame-alias-audit-20261007.md).

`func_151452C4` is now installed as semantic sphere-intersection C in
[game_16EE20.c](../../conker/src/game_16EE20.c). Its complete 126-word slot,
`0x70` frame and original private layout match retail. The original assembly
file remains a reference. This replaces restored assembly, not a zero-return
placeholder: all 6,059 linked function slots remain byte-identical to the
baseline. The conversion and byte-exact C counts each increase by one.

## Allocation Recovery

[Allocation driver](https://github.com/gipson-dev/64CBFD-Tools/blob/master/experiments/game_sphere_callee_allocation_candidates.py)
combines the meaningful direction union recovered in Note 1084 with scalar-first
and relative-vector-last declaration order. The previous declaration-order
screen used ordinary structures: its useful offsets alone did not recover the
original frame. The combined source recovers both, without unused locals,
padding, an unused fourth component, volatile or private-offset guards.

The bundled compiler's structured `.mdebug` procedure/local records bind:

| Local | Entry-relative offset | Frame-relative offset |
| --- | ---: | ---: |
| `x`, `y`, `z` | `-4`, `-8`, `-12` | `0x6C`, `0x68`, `0x64` |
| `direction` | `-24` | `0x58` |
| `origin` | `-36` | `0x4C` |
| `projection`, `radiusSquared`, `perpendicularSquared` | `-40`, `-44`, `-48` | `0x48`, `0x44`, `0x40` |
| `root`, `first`, `second` | `-52`, `-56`, `-60` | `0x3C`, `0x38`, `0x34` |
| `relative` | `-72` | `0x28` |

The procedure frame is 112 bytes. The selected source emits 126 words with
53 aligned differences. Thirty-two maintained union/declaration/scalar-order
controls all compile without diagnostics; none is raw byte-exact. Ordinary
structure controls retain the wrong `0x68` frame. Raw and guarded code now
preserve the original private memory, including live snapshot rereads.

An exploratory `-v -keep` compiler invocation aborts in the bundled recomp's
unimplemented `fprintf` format (`libc_impl.c:812`). Retrying without `-v`
compiles successfully but keeps no intermediate files. The existing structured
`libelf`/`mdebug` parsers provide the allocation receipt instead; no compiler
implementation or production profile was changed.

## Guard Boundary

73 raw aligned words match directly. The remaining 53 expected-word guards in
[retail_word_patches.us.csv](../../conker/retail_word_patches.us.csv) normalize
floating temporary allocation, commutative operand order and one closed
33-PC permutation. The independent relative-vector address calculation moves
past the point writes; two final independent loads exchange positions.
The maintained driver asserts that the permutation is closed and each mapped
instruction preserves its opcode, function, immediate and non-register fields.

No frame/private offset, branch, insertion, omission, helper target, shared
header or compiler profile is patched. The sole call relocation remains
`0x1C0 R_MIPS_26:func_15144A74`. Guarded output matches all 504 original bytes.
The neighboring 53-word wrapper and 13-word dot helper remain unchanged.

## Qualification

[Eleven allocation tests](https://github.com/gipson-dev/64CBFD-Tools/blob/master/tests/test_game_sphere_callee_allocation_match.py)
retain the independent [full-frame reference](https://github.com/gipson-dev/64CBFD-Tools/blob/master/tests/game_sphere_frame_reference.py)
and separately execute raw C, original retail and guarded code.

- 1,404 external-alias and 1,296 private-output/incoming-home cases compare
  complete memory, ordered writes, dot pointers and status to the original
  retail layout. Early point pointers and late distance-pointer homes stay live.
- The former installation blocker now produces second-X **24.0 in both raw
  C and retail**. Historical trial 10.0 remains a negative receipt, not the
  installed body's behavior. Private offsets were recovered, not normalized.
- 1,024 additional seeded finite cases vary all three input vectors, nonzero
  origins, non-unit directions, radii and external aliases. Across these 3,724
  cases all 126 callee and 13 dot-helper words execute. Raw/retail instruction
  inputs agree through the explicit PC permutation; guarded/retail events and
  complete register state agree. Missing required storage fails closed.
- 6,318 actual 32-bit native finite-geometry calls compare full 128-float
  storage bits and status to an independent algorithm, with three origins,
  three directions, nine centers, six radii and thirteen external aliases.
  Native tests do not model guest private-frame or parameter-home aliases.
- Copied-owner checks preserve all 89 symbols, the other 88 routines' bytes
  and function-relative relocations, normalized pools and the same two owner
  warnings. The actual padder produces 504 bytes with the original or an
  alternate dot-helper target. A deliberately stale expected word is rejected.
- The stale-guard test now copies its row dictionaries before mutation. The
  first 57-test run exposed that fixture mutation in its later production
  assertion; no production word or installed guard changed as a result.

Pre-install: ten tests pass in 21.148 seconds, zero skips/errors/failures.
All 57 focused post-link allocation/frame/recovery/wrapper/projection/owner-pool
tests pass in 187.474 seconds, zero skips/errors/failures. Project-tool smoke
checks, Python syntax, whitespace and the final post-regression linked audit
pass. Documentation gate: 68 documents, 3,776 relative links, zero broken.
This is bounded finite geometry and mapped guest-memory evidence, not full
float-domain/FCSR/NaN payload, native private-frame, hardware,
complete-caller, gameplay or host-adoption acceptance.

## Linked Baseline And Progress

The US ELF rebuild succeeds. Its wider pre-existing compiler/assembler and
Make recipe warnings remain; the copied target owner specifically retains
its same two warnings. No final ROM checksum success is claimed.

The fresh linked audit preserves all 6,059 function-slot bytes, addresses and
extents, protected sections, and 720 Game-data owners/189,088 bytes. All 10,953
historical guard rows are unchanged; the 53 new rows bring the total to 11,006.
Regenerating `progress.csv` completes before the count audit.

| Section | Converted functions | Converted bytes | Byte-exact C |
| --- | ---: | ---: | ---: |
| Total | 5,466 / 6,042 (90.47%) | 1,932,072 / 2,256,728 (85.61%) | 3,355 / 5,466 (61.38%) |
| Game | 4,793 / 5,321 (90.08%) | 1,760,636 / 2,072,880 (84.94%) | 2,682 / 4,793 (55.96%) |

Conversion increases by one function/504 bytes in Total and Game. Init remains
492/539 converted and 492/492 exact; Debugger remains 181/182 converted and
181/181 exact. 2,111 converted functions still differ; zero address drift.
Only the four affected aggregate rows change in the main README. Detailed
updates and checked-off recovery work remain in DOCS.

## Resume

Next: `func_15145AD8`, an active 110-word zero-return placeholder, original
frame `0x88`, VA `0x15145AD8..0x15145C90`, ROM `0x172F88..0x173140`.
The intervening 35-, 61- and 65-word routines are already exact.

1. Recover the complete 110-word routine, its `func_1515C1A0` dependency and
   incoming ABI, preserving private vectors and optional-output home lifetimes.
2. Preserve retail's non-null incoming-output redirection to named private
   homes and the Y scales at object offsets `0xDC/0xE0`; do not assume ordinary
   null fallback behavior.
3. Extend independent guest/native/alias evidence before fitting and
   classifying words, then qualify copied owner/pools, padder, linked baseline,
   complete guard history and regression gates before narrow installation.

The existing 18-word caller setup at VA `0x15145C00`, ROM `0x1730B0`, is bounded
fragment evidence, not acceptance of the full 110-word caller. Sampler
`func_151432BC` and oriented `func_15142600` remain open. No sibling, frozen
Release, real save, runtime or push work was performed.

Ignored receipts: `conker/build/game-sphere-callee-allocation-match/`,
`conker/build/game-sphere-callee-allocation-test/`, and exploratory compiler
receipts in `conker/build/game-sphere-callee-allocation/`.
