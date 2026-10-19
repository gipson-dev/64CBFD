# Actor Sine Selector Saved-Lifetime Match

Verified: 2026-10-19. Complete semantic **func_15089F9C is installed and its
linked 136 words are byte-exact**, frame112. VA15089F9C..1508A1BC,
ROM B744C..B766C, generated_B3020. Consumer predecessor98d7bfc8, tools
predecessor0df9f7e. Tools **3457d8d** are committed before the consumer pin.
No push, host-port edit or frozen Release change.

This is a **guarded match, not direct compiler identity**. The complete C
still emits138 words/frame128 with77 differences. The production padder
applies138 expected-word/relocation guards, removes three dead words and
inserts one state-cursor move. The resulting544-byte body fits its actual
retail slot. Do not describe the77 differences as independent scheduling.

## Source And Allocator Evidence

Keep the meaningful signed slot, selected index, state cursor, count, active
mask, eligibility bit, distance bounds, factor, phase and strict-best names.
The source retains the complete behavior qualified in [Note1594](1594-actor-sine-selector-semantic-recovery-and-frame-boundary-20261019.md),
including cached initial count/active/state rows/phase versus freshly read
eligibility, coordinates and per-eligible coefficient. Formatting fixes the
guarded do/while indentation; it does not change emitted words or bindings.

Owned, fingerprint-locked mode6 and native mode5 UOPT captures complete with
all four children and driver exit0, fired diagnostic probes, cleanup and
identical normal/traced text, definitions, relocations and pools. Native
mode5 observes105 events in one owned allocator table. Expression9 is the
active-mask local M-12 of procedure755; expression158 is the coefficient
address. Their observed save bits are3FEAAAAB (about1.8333334) and40000000
(2.0). The address takes color22/FP-S8 first; the mask finishes in color4/A1.
This explains the observed current allocation conflict. It is **not** a
capture of the original retail source or allocator decision. Suppressed
printed real-number timings/costs are not evidence for those numeric values.

Pointer declarations and cursor/literal/source-order screens do not directly
recover the complete retail body. Moving the factor after distance can emit
136 words, but still frame128. Named literal constants reproduce the earlier
wrong saved-FP allocation. Global no-constant-register/saved-register options
also fail. No production compiler/profile/declaration change follows from
those negative controls. No Claude call, compiler patch or dependency setup
was added in this continuation.

## Closed Lifetime Recipe

The recipe in [game_actor_sine_selector_layout.py](../../tools/experiments/game_actor_sine_selector_layout.py)
requires the exact complete raw-body and19-binding fingerprints. It derives
the normalized words from their source origins, not from a copied ROM body:

1. Exchange the selected-index and slot-offset saved colors S5/S6 without
   exchanging physical save/restore slots. Capture the active mask directly
   in FP/S8 and retain it across sine, eliminating its A1 call spill/reload.
2. Move the coefficient HI relocation from its saved-address initializer to
   the eligible use, using AT. Transfer the LO relocation from the dead
   address ADDIU to the original LWC1. The coefficient remains a fresh float
   read on each eligible iteration, with no compiler literal pool introduced.
3. Split the original state-cursor ADDIU into an early V1 computation and a
   later S1 move, preserving the originally captured state rows across all
   helpers. Schedule bounds/phase/constants and retain the guarded phase
   load. The else branch must enter its moved LUI, not skip directly to LWC1.
4. Remove only raw offsets C4,19C,1B4: the redundant coefficient-address low
   initializer and the two dead active-mask spill words. Retain135 unique
   source words and insert one cursor move:138-3+1=136.
5. After that lifetime contraction, recover frame112 and adjust the paired
   incoming-A0 home accesses to SP+112. All saved GP/FP frame-relative slots,
   FP arithmetic/conversion/register fields and memory widths stay fixed.
   Recalculate branch targets through the actual origin map and retain all
   19 relocations. No volatile declaration, dummy use, inline assembly or
   physical-register C binding is introduced.

The frame-only negative is essential: changing only the entry/exit frame
size still returns the expected selected index but overwrites the caller's
STACK+4 word with the surviving active-mask spill. The qualified recipe
leaves that word A5A5A5A5 and passes every tested private-access prefix. It
does not hide Note1594's first-store mismatch by editing only the frame.

Raw SHA256:

```text
9b36dd52ce1411f49bae251814c8a252900c479b10c8c7e22e2eed05d14afbc3
```

Normalized, unrelocated SHA256:

```text
d700e03ab127756ccfcb925d990cc167c093674913bcda10b137db54785b3394
```

## Fresh Qualification

**Eight installed tests pass in33.082 seconds**, no skips:

- 105 fixtures/two phases give210 completed retail/normalized/raw triples.
  Compare the independent selected result, complete public buffers and
  ordered sine argument bits. Retail/normalized also agree on the complete
  private memory, GP/FP/LO/condition state and ordered events.
- 1,192 fired access-cut pairs across ten edge/mutation profiles and two
  phases agree at the exact requested address/width, all private/public
  bytes, registers and event prefixes. Raw compiler private-frame identity
  is deliberately not claimed.
- 88 actual-sine pairs connect the retained104-word Game helper and agree
  on complete private state, public buffers and exact arguments. This is
  the bounded selector domain, not full hardware/FCSR or gameplay parity.
- Native32 O0, O2 and O2+UBSan each pass105 full-buffer fixtures using the
  actual retained sine C on ordinary providers. Six effective semantic
  negatives cover ties, excluded state, mask lane and cached count/rows/phase.
- 30 actual returning-caller runs retain the full-word slot delay load,
  original24-byte caller frame and branch/RA/SP/JR epilogue. Normalized and
  retail private states agree; raw public results also agree.
- Four independent GNU maps include HI/LO carry boundaries and a backed
  actor-base-zero map. Every normalized byte agrees with independently
  assembled retail. Thirty-six executed raw/normalized pairs rebase code,
  all globals, contexts, actor storage and modeled provider entrypoint.
- Corrupting each of138 source words or each of19 bindings is rejected.
  The real padder rejects stale expected words/relocations. Four strict
  whole-image corruptions are rejected. Canonical symbols differ only in
  the intended target size12->544, not names, addresses or other definitions.

Both complete-owner profiles have empty target diagnostics and preserve
72 other routines/pools. Actual padding preserves all73 addresses. Expanded
Make's seven commands reproduce the same raw bindings, primary functions and
padded object metadata. Existing unrelated SDK/source and shadow-Make recipe
warnings remain; no target warning was suppressed or new build flag added.
`make tools-check` passes; Python syntax checks pass in both tools copies.

An initial first-link check correctly rejected unpredicted symbol ordering.
Its diagnosis remains archived. Thirteen named definitions in four bounded
serialization runs are now explicitly predicted, with canonical equality
and strict corruption controls; no blanket symbol/string-table exclusion.
One installed-suite attempt was started before the production build had
finished and correctly rejected the predecessor ELF. The final full suite
above runs after the owned production build and audit terminate successfully.

## Complete Production Audit

Production ELF SHA256:

```text
a0cce96c2ae430f94f8f717f94a10b9d46d37c90faa725929c5ff7bdc962ea78
```

The exact first-linked prediction and production image agree byte-for-byte:
619 changed bytes =433 target-code bytes +2 target-size bytes +75 symtab
serialization bytes +109 strtab serialization bytes. All6,056 other function
bodies and every address are fixed. The protected189,088-byte Game data from
720 owners remains exact with zero changed bytes. No assembly, Makefile,
global data, conversion count or unrelated guard-prefix change.

Installed owner SHA256:

```text
5d8b6cbccee79b0db84aaaac92d5533d213bebee62bf683686ad1f2379eee0f37
```

Installed guard CSV SHA256:

```text
b200d8dc1c2d3a753e1865f20524c8fcc69ee922e8d12c27bf544f8dd9d27fcc
```

Fresh matching: **Game3007/4832 (62.23%)**, **total3680/5505 (66.85%)**,
**1,825 different, zero drift**. Init492/492 and Debugger181/181 stay exact.
The owner now has **59/73 exact,14 still different**. Root README changes
only its two matching aggregate rows. Working updates stay in these docs.

The standalone mirror's older HEAD is untouched. Its predecessor candidate
is checked against primary HEAD before the intentional task-only update;
three new files and the formatted candidate are mirrored identically.
All1,365 other pre-existing dirty-file hashes are preserved. No standalone
commit, stash/reset/clean, host work or push.

## Resume

Next is **func_1508B9BC**, VA1508B9BC..1508BC20, ROM B8E6C..B90D0,
153 words/frame96, currently145 real differences:

1. Freeze the new baseline and audit its actual caller. Recover its cached
   initial context/count/table pointers before func_1508C5B8(0,1-or-4) and
   func_1508A1BC; preserve the context reloads after those helpers.
2. Recover the16-entry sentinel search and unsigned byte weight conversion,
   optional current-target multiplier and strict minimum. Keep original
   table caches distinct from freshly reloaded publication/distance contexts.
3. Qualify target and fallback publication, truncated X/Z distance, empty
   count, ties, masks, helper mutations, private lifetimes and complete
   linked-image preservation before installing the next body.

Commands from64CBFD under WSL:

```sh
python3 -m unittest tools.tests.test_game_actor_sine_selector_match -v
python3 -m tools.experiments.game_actor_sine_selector_integration --audit
python3 -m tools.match_progress conker/progress.csv conker/build/conker.us.elf conker/conker.us.bin
make tools-check
```

Experimental sources, compiler traces, original first-link diagnosis,
qualification JSON, exact prediction, production-build log and remaining-owner
inventory are ignored under `conker/build/game-actor-sine-selector/`.
The broader Game decomp/matching goal remains active.
