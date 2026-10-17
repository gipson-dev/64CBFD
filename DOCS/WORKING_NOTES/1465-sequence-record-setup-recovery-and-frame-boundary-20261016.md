# Sequence Record Setup Recovery And Frame Boundary

Date: 2026-10-16. Consumer predecessor **95c0589d**, tools predecessor
**b7775f4**. Continue the same target selected by
[Note 1464](1464-sequence-state-reset-installed-guarded-match-20261016.md).

## Recovery, Not Installation

Recover the complete **func_1501D348** as a research candidate in
tools/experiments/game_sequence_record_setup.py. The production owner
conker/src/game/generated_49D30.c still contains its zero-return stub.
The recovered interface is:

```c
void func_1501D348(s32 scene, s32 sequence, s32 slot,
                  s32 hook, s32 parameter);
```

Retail occupies **473 words / 1,892 bytes**, VA
**0x1501D348..0x1501DAAC**, ROM **0x4A7F8..0x4AF5C**, frame **0x78**.
The complete selected C emits **471 words / 1,884 bytes**, frame **0xA8**,
with **405 length-aware word differences** against the linked retail slot.
This includes the two-word length gap; it is not a 405-word scheduling fix.
Preserve the existing **O2/g3/no-unroll** owner profile.

**Do not install, pad, truncate or guard this candidate. No matching credit.**
The complete body, all 89 relocation bindings and empty private pools are
pinned. It compiles without diagnostics and leaves all **56 raw owner
neighbors** identical, including the installed reset, maximum scan, loader
and graphics-task submission. The production source, caller, guard manifest,
ELF, conversion and matching CSVs, Makefile and root README remain unchanged.

Raw candidate text SHA-256:
**0449520a1d8dccf7146bd689a066643509537fc0d183fdcf6758c516b3ec6000**.
Sorted relocation-map SHA-256:
**1bf30d7917bda0cc768cc13c0c307f5c6bb42fe72c3dee9d84960877357eb74c**.

## Recovered Contract

The behavior below is recovered from all 473 original instructions, not
accepted from the additional-source draft without comparison:

- Cache the selected status byte. Return without publication when it is
  exactly one or the shared unsigned request gate is nonzero. Publish the
  hook's low byte and full parameter only after that gate.
- A different full-word scene requests a transition with five arguments.
  Publish the low byte of unsigned sequence-plus-one, then reread the live
  status after the provider before publishing the completion flag. The
  unsigned expression preserves wrapped addition without signed overflow.
- In the current scene, publish the sequence byte and preserve the cached
  status-two branch. Call the already installed void reset, then the resource
  provider. A zero resource result returns; no new allocation-failure checks
  are invented.
- Cache the resource bundle and its header. Recover an **8-byte header of
  four u16 counts**, **8-byte descriptors with full u32 byte lengths**, and
  **64-byte runtime records with pointer fields at +4 and +0x38**. Correct
  the draft's scaled indexing and word/halfword confusion.
- Allocate the enabled halfword array and prefill it from descriptor lengths
  shifted right three, then truncated to u16. Allocate and clear fallback
  and preferred arrays using the unsigned maximum of their count and the
  active count. Preserve zero-size allocations and their call order.
- Allocate auxiliary pointers, runtime records, per-enabled-entry item and
  0x194-byte scratch blocks, a count-times-0x44 record bank, and one 0x10-byte
  block per active entry. Reload the runtime pointer cell **after each
  allocator returns**, before publishing its field. An explicit allocation
  temporary preserves that provider boundary.
- Clear the first active-count entries of all three halfword arrays, publish
  the low-byte active count, then republish enabled counts and pointer rows.
  Pointer rows use the original **30 entries / 0x78-byte slot stride**.
- After the first active group, publish bundle[cursor].data and skip another
  **activeCount** descriptors before fallback publication. This apparently
  unusual skip is present in retail. Continue with fallback, preferred and
  auxiliary descriptor groups; do not silently remove it.
- Invoke the optional four-word table callback using the actual hook index.
  Preserve the sum helper's full result until low-16 truncation, publish its
  halfword, then allocate **unsigned low16 times twelve** bytes.
- Preserve all subsequent provider packets and order. The processing loop
  rereads the live byte count after each provider, passes index before
  incrementing it, and rechecks the count after the later helpers before
  the empty-path call. Publish status/shared flags and the final byte-four
  store at their original boundaries.

The allocator declaration follows its actual Init definition:
**s32 allocate_memory(s32, s32, s32, s32)**, with explicit pointer casts.
Already recovered later void functions keep their real return types.
Other opaque providers retain the owner's existing no-prototype convention;
this is not an unrelated global-header rewrite. Keep address-based symbols
and the proven behavioral comments rather than speculative renames.

## Frame And Home Boundary

The save set and save offsets already match: **S0-S5 and RA at SP+0x1C
through SP+0x34**. The first ten words after the frame adjustment match
retail. The outstanding frame problem is private homes, not extra saved
registers. Measured SP-relative locations:

| Home | Retail | Selected C |
| --- | --- | --- |
| Cached bundle | 0x70 | 0x9C |
| Runtime pointer-cell address | 0x54 | 0x50 |
| Per-record 0x10-allocation cursor | 0x48 | 0x7C |
| Status pointer | 0x5C | 0x5C |
| Slot-times-four | 0x58 | 0x58 |
| Fallback / preferred / auxiliary cells | 0x44 / 0x40 / 0x3C | 0x44 / 0x40 / 0x3C |
| Runtime-loop byte-offset spill | 0x48 | 0x48 |
| Incoming A0 / A1 / A3 homes | 0x78 / 0x7C / 0x84 | 0xA8 / 0xAC / 0xB4 |
| Incoming fifth argument | 0x88 | 0xB8 |

Five bounded source screens preserve the selected body and do not recover
the frame. All compile without diagnostics or private pools; each receives
two guest witnesses, **not full alternative qualification**:

| Screen | Words | Frame | Length-Aware Differences |
| --- | --- | --- | --- |
| Shared byte-offset cursor | 471 | 0xA8 | 407 |
| Byte runtime view | 471 | 0xA8 | 405 |
| Scoped preferred cursor | 471 | 0xA8 | 405 |
| Global total expression | 472 | 0xA8 | 413 |
| Explicit total address | 471 | 0xA8 | 407 |

The byte-runtime and scoped-cursor forms emit the exact selected raw hash.
SELECTED remains INITIAL. Do not repeat these screens as new progress.

## Fresh Qualification

All **five final tests pass in 100.001s**, including explicit saved-FPR
assertions. The qualification contains:

- **242 fixtures at two stack phases = 484 two-way guest cases**. Execute
  the complete original and actual compiled C against an independent ordered
  reference. Visit every one of the 473 original and 471 candidate words;
  compare full public memory, allocations, call packets and **31 explicit
  lanes at each provider boundary**. Check saved GPRs, FPRs and SP.
- **Eight positively fired diagnostic gates**: cached bundle/header,
  runtime-cell reload, wide capacity, live transition status, hook count,
  late count, live loop count and empty-after-helper. These controlled
  provider mutations are not claims about retail allocator/helper behavior.
- Cover empty/mixed groups, both valid slots, cached states, nonzero gates,
  load failure, callback indices, full-u32 descriptor lengths including
  0xFFFFFFFF/0x80000000, u16 capacities 65535, low16 sums and signed-INTMAX
  deferred sequence. Large-capacity cases shrink the later loop count in
  an explicitly fired diagnostic provider after computing capacity.
- **60 native32 cases each at O2 and O0 with UBSan**, no fwrapv and no LTO.
  Compile the actual complete candidate, actual restored reset C, and the
  typed caller/providers as separate units. Check **756 canonical fields**,
  complete bank padding/canaries, the entire used allocation arena including
  gaps and sixteen-byte guards, packets, snapshots and fired counters.
- All **eight native controls** build and execute, then fail functionally
  with exits **21/22**, not signals or sanitizer failures: truncated
  descriptor length, missing descriptor-group skip, wrong capacity stride,
  stale runtime pointer, increment-before-process, signed total,
  stale request status and wrong callback parameter.
- Independently assemble all 473 original words and compare them with ROM.
  Verify all **136 frozen production inputs** unchanged. Corrupt each input
  independently and require the freezer to reject it.

The guest reset provider uses its independent ordered reference. Native
checks execute the actual restored reset with a bounded clear helper. Other
providers, allocations and bzero are bounded contracts, not their complete
retail implementations. Allocations are valid/non-null, including unique
zero-size results; NULL allocation failure, arbitrary cross-object aliases,
full caller/gameplay, hardware and host-port acceptance remain unqualified.
Private stack/fault equality and independent rebases are **not qualified**
for this mismatching candidate. Fixture addresses are disjoint from guest
stack; native entry uses explicit stack realignment for the freestanding
GCC/SSE harness. Neither harness correction is a production game fix.

## Bank And Resume

Tools **332b6ba** banks the five new experiment/reference/native/test files
before the consumer pin. Both copies have identical task files, **ten
ASCII/AST checks**, all **eleven WSL padder tests per copy** (active
**0.040s + 0.024s**, mirror **0.030s + 0.019s**), and passing consumer
tools-check. Preserve mirror HEAD
**ddbdd16b53ce60b054fb6e11bf0649a41f48375a**, all **957 initial dirty-file
hashes**, and its independent history; **962 final dirty paths**. No mirror
commit/reset, push, Claude call, REA reinstall, dependency change or frozen
host Release action.

No production rebuild or aggregate remeasurement is needed for this
research-only change. Last installed measurements remain **Note 1464**:
Game **2,939/4,828 (60.87%)**, total **3,612/5,501 (65.66%)**, different
**1,889**, zero drift, converted **5,501/6,044 / 86.04% bytes**. These are
the unchanged previous measurements, not fresh credit for this candidate.
The frozen ELF is still
**17e327a95fcf43c50ac2611a19461980ad1d44664a3c3a218d593f35e26cd4ab**.

Reproduction in the prepared consumer checkout, sequentially:

```sh
python3 -m tools.experiments.game_sequence_record_setup
python3 -m unittest tools.tests.test_game_sequence_record_setup \
  tools.tests.test_game_sequence_record_setup_native -v
make tools-check
```

- [x] Recover the complete five-word interface, typed groups and ordered providers.
- [x] Qualify public behavior, both guest phases, native32 and effective controls.
- [x] Preserve all 56 raw neighbors and 136 production inputs; bank research only.
- [ ] Fit this same function's frame/private homes and full instruction/relocation shape without unsafe guards.
- [ ] Qualify actual caller/helper boundaries, private/fault/rebase behavior and an independent complete-image prediction as required by the eventual fit.
- [ ] Only then install, rebuild, audit and measure fresh matching progress.

Resume **func_1501D348**, not a different easier stub. Compare the cached
bundle, runtime-cell and per-record cursor homes/lifetimes with retail under
the unchanged profile. Timing's 141 differences and wider Game/additional-
source recovery remain separate open work.
