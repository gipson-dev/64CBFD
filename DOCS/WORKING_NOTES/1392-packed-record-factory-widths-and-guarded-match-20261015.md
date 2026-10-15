# Packed Record Factory Widths And Guarded Match

Verified 2026-10-15. The previous goal turn made a committed C-wrapper recovery;
this checkpoint replaces its still-empty factory. The whole additional-C /
Game goal remains active, not complete.

## Target And Recovery

| Item | Value |
| --- | --- |
| Function / owner | func_1516D99C / generated_19A8B0 |
| VA / ROM | 0x1516D99C / 0x19AE4C |
| Complete slot / frame | 125 words, 500 bytes / 0x20 bytes |
| Allocation wrapper | func_15167A68, existing 28-word C routine |
| Consumer / tools predecessor | fd31e8b2 / f0e67c2 |
| Profile | Existing O2/g3, unchanged |

The archive `game/game_19A8B0.c` supplies the overall allocation/initialization
shape, but its field reconstruction is unsafe: many overlapping 32-bit writes
stand where retail uses SB and SH. Recover signed halfword and unsigned byte /
halfword parameters from every complete original load/store, all 49 incoming
homes, the full-word kind/context arguments, null path and conditional arg41
clamp. Keep unproven parameter names address/argument-based; use meaningful
`record` and `kind` locals plus purpose and ABI comments.

Use the allocator's actual private signature, including its two u8 parameters.
Factory argument 47 stays s32 at the visible caller ABI; its big-endian low
byte is read explicitly through a u8 home view. A u8 factory formal lets IDO
remove the already-matching caller's byte load, changing one caller word.
The explicit home view avoids that change without volatile or a guard that
changes load width. No shared headers, allocator source or other owner bodies
are edited. The existing 78-word func_1516F1C0 caller remains raw byte-exact.

Bounded full-owner screens: all-word form 125 words / 53 differences;
narrow-formals form 125 / 6 plus one caller difference; explicit casts 125 /
71; all-home views 126 / 47; corrected wire-byte form 125 / 6, caller exact.
Two named preload locals do not change those six words. These screens do not
prove that every possible direct C form is impossible. The older isolated
archive screen's 158 words / 140 differences remains historical lead evidence,
not adoption proof.

## Six Scheduling Guards

The corrected raw C has the complete retail frame, body length, registers,
branches, fields and calls. Only two independent three-word schedules differ:

- Offsets 0x144/0x148/0x14C: move the arg26 byte load before the two stores
  using the already-loaded arg31 halfword. Closed permutation `[2, 0, 1]`.
- Offsets 0x188/0x18C/0x190: place arg38's halfword store and arg39's byte load
  before the separate zero-byte store. Closed permutation `[1, 2, 0]`.

All six guards are expected-word checked and have no relocations. Preserve
the complete prior guard-file bytes; append only these rows. The normalizer
pins the full raw object hash and the sole call relocation, rejecting every
one of 125 individual raw-word flips and a changed call binding.

This is a **guarded C match**, not direct compiler identity. Raw/guarded heap
results agree but access order differs. Only the guarded guest body receives
the retail alias/access-fault ordering qualification; do not generalize that
claim to raw C or portable C faults.

## Fresh Qualification

All **14 focused checks pass in 45.597 seconds** across the three
`test_game_record_factory`, `_candidates` and `_installed` modules.

- 2,048 guest cases cover all fields, null/success, high bits/sign boundaries,
  both stack phases, post-provider incoming-home mutations, live arg44 reload,
  byte arg41 clamp and full-word allocation inputs. Included are 1,024 backed
  stack-alias cases. An independent semantic memory/store reference agrees.
- 456 paired, fired guest access-fault prefixes match the full retail body.
  Saved RA/register/frame lifetimes and the null-check delay load are retained.
- Actual selected C runs 4,096 native32 cases per O2/O0 profile. Flag argument
  47 has repeated bytes in these host fixtures, making the explicit big-endian
  home-byte read endianness-invariant; arbitrary flag high bits are covered by
  the guest tests instead. Native tests do not claim stack alias or N64 runtime
  acceptance. Six compiled semantic negatives fail in both guest and native
  fixtures: wrong kind, allocation size, byte source, halfword source, clamp
  boundary and missing zero clear. Mutants receive no matching guards.
- Independently assemble the complete original routine for three text/callee
  rebase pairs. The guarded relocated output matches all 125 words each time.
- 128 cases connect the actual 78-word wrapper, recovered 125-word factory and
  unchanged exact 28-word allocator. Verify the real five-word heap call,
  registration call and returned record fields, including null propagation.
  Only the lower heap and registration providers remain opaque. This is not
  full gameplay acceptance or a claim that all providers were recovered here.
- All 29 other functions in the copied owner keep raw bytes, extents, relative
  relocations and normalized pools. The actual generated-owner padder is used.

Initial fixture failures exposed omitted outgoing stack words in the semantic
reference, a mixed-shape event filter and an intentional negative's unused
parameter warning. Correct the fixtures and rerun the complete passing suite;
none required weakening the production byte or field checks.

## Literal Image And Counts

The guard dependency triggers the normal broader generated-owner/SDK rebuild;
it completes successfully. Construct the entire expected ELF independently
from the pinned predecessor, 500 retail bytes and only symbol extent
`12 -> 500`. The installed ELF equals it: **374 changed bytes**, target slot /
extent only, no metadata allowances. Every other ELF byte and all **189,088
protected bytes / 720 owners** remain fixed. Known duplicate generated_12D630
recipe warnings remain; this is not a warning-free-project claim.

| Input | SHA-256 |
| --- | --- |
| ELF | dffd6489132224328ba1b709b24cb87d7b07556d81d8ccdc4f48cb72169ae82c |
| Owner | 647b591a5a4afd82be8b37884fcdfd07df1987312c9580d232d95aafc2d65a08 |
| Guards | 5d5daf3748fdb04f64d3bc337f875552b6f6e6a3dd870b74095f01d0d232eb73 |
| Unchanged progress CSV | 595443d0129e7d6ccd1f824b050854d5759c0f45c1af5b0818ef7cde682528ee |

Check all **43 inputs**: three changed, 40 fixed. Corruption controls cover
every input, source text, five physical ELF locations and all before/after
captures. Exact-input inverses do not participate in current image or connected
chain acceptance. Reuse unchanged earlier broad-suite receipts explicitly;
do not call those fresh tests. All **801 original archive fingerprints** are
freshly checked and fixed. Progress CSV remains ignored, not force-added.

Fresh matcher: Game **2,891/4,828 (59.88%)**, total **3,564/5,501 (64.79%)**,
different **1,937**, zero drift; Init 492/492 and Debugger 181/181 exact.
Conversions stay total **5,501/6,044 (91.02%), bytes 86.04%** and Game
**4,828/5,323 (90.70%), bytes 85.41%**. The previous zero stub was already
classified C: add one exact body, not another converted function. Root README
changes only two aggregate rows; function detail stays in this note.

## Banking And Next Work

Bank tools **49b76f0** before the consumer pin/source/guards/docs. Shared tools
checks, standalone five-file syntax and all three ROM-free checks pass. The
independent older mirror stays at ddbdd16: all **623 initial dirty fingerprints**
remain fixed; copy only five absent owned paths and verify all **628 final
fingerprints**. No mirror commit/reset, push, host source/build/launch,
save/configuration or frozen Release action. Claude calls: zero. Ignored
receipts live under `conker/build/game-record-factory/`.

The full Graphify update refuses 19,307 nodes against 41,086 curated nodes,
retaining 19,398 nodes from 2,972 excluded-but-present files. Do not force it;
await the incremental consumer-commit worker.
Seven documents / 4,942 relative Markdown links validate with zero broken.

Next recover **func_1516D4E8**, the still-stubbed 100-word / 0x34-byte factory
in this same owner. Retail selects kind 0x67/0x12 and uses packed stores plus
an optional secondary call. Its older archive screen is 120 words / 106 real
differences, so re-establish its widths and complete active ABI before any
adoption. The wider additional-source/binding queue, handwritten Init hardware
routines and func_1510BF60 remain open.

## Post-Bank Verification

Consumer **f3b01c10** banks the source, six guards, tools 49b76f0 pin, README
aggregates and detailed working documentation. All **14 post-bank checks pass
in 36.854 seconds**, including the complete independent current image, all 43
input states and fresh hashes for all 801 archive files. Normal ELF/progress
build is up to date. Raw C still has six differences; only the guarded slot is
byte-exact, and the existing caller remains direct C exact.

Both active checkouts are clean before this receipt. All 628 final older-mirror
fingerprints, including the 623 initial fingerprints and independent ddbdd16
HEAD, remain fixed. The source commit's incremental graph worker completes at
**41,095 nodes / 81,191 edges / 3,831 communities**, without forcing the refused
smaller full scan. No push or host/Release operation. Continue the wider goal
at func_1516D4E8; do not declare the additional-C / Game queue complete.
