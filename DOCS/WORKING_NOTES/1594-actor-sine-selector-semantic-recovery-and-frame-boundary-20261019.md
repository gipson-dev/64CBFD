# Actor Sine Selector Recovery And Frame Boundary

Historical pre-installation checkpoint. Superseded by the complete, qualified
[saved-lifetime match in Note1595](1595-actor-sine-selector-saved-lifetime-match-20261019.md).
The raw compiler boundary below remains real; the later note proves the
complete normalization and rejects a frame-only patch.

Verified: 2026-10-19. **Complete experimental C recovery, not installed and not
byte-exact.** Continue func_15089F9C, generated_B3020, VA15089F9C..1508A1BC,
ROM B744C..B766C, retail136 words /544 bytes, frame112. Consumer predecessor
**fcb2b9a8**, tools predecessor **2728516**. Bank tools **0df9f7e** before
the documentation/tools-pin checkpoint. No push.

## Complete Behavior

The candidate uses an explicit signed32 slot parameter and meaningful state,
mask, distance and score names. Keep the address-based function name; no
original source names or record layout are invented.

1. Capture the initial context, its state rows at+0xE64, signed count at+0x10
   and full-word active mask at+0x14. Read the per-slot flag at+0x15C.
2. Select distance range750..3500 for flag0, or1500..8000 otherwise. Start
   with selected=-1 and best=-1000000. Nonpositive count returns-1 without
   loading the phase or calling sine.
3. For positive count, capture phase bitsBFC90FDB (-pi/2) once. Scan the
   original state rows, excluding state3 and inactive bits. Reload the global
   context's per-slot+0x16C0 eligibility mask for each candidate that reaches
   that gate. The required bit is(1U<<index)<<16, not the low active bit.
4. For eligible candidates, freshly read coefficient bits40C90FDB (tau) and
   compute factor=tau/(maximum-minimum) with float32 rounding. Compute X/Z
   distance from candidate to the input slot, or32000 for a zero computed
   actor address. Clamp first to the upper bound, then the lower bound.
5. Compute sinf((distance-minimum)*factor+cachedPhase)+1 in the original
   float32 order. Update only when best<score, preserving the first exact
   tie. This is a band-weighted score, not a nearest-actor query.

Callbacks can change the current context/mask, original count/active fields,
original state rows, coordinates or coefficient memory. The reference and
modeled-provider tests distinguish the cached values from the fresh reads.
Coefficient/phase mutation cases are explicit provider stress; the real
retained sinf leaf does not perform those mutations.

## Actual Sine And Data

Reuse the existing single-precision Game sine reference and the actual
104-word sinf at15047D60 /ROM75210, not host libm. Freeze its C, preserved
assembly and supplying2275E0.data.s,23D850.rodata.s and2C920.rodata.s alongside
the already-frozen selector constants in2424E0.rodata.s.

The current production ELF's complete416-byte sine body matches retail.
Fifteen supplying selector/sine constant words also match the actual
.game_data bytes. The frozen sine source remains:

```text
ae271497692ea1a00abd96bcfed9209458cf8ea694b0df385aa5dddf9fc1a679
```

The connected tests cover the selector's bounded clamped-angle domain,
visiting91 of104 sine words. They do not rerun or claim the earlier full
trig/exponent/FCSR qualification; the remaining exceptional sine paths are
outside this fresh subset.

## Measured Matching Boundary

| Source form | Words | Frame | Differences |
| --- | ---: | ---: | ---: |
| Initial complete body, phase read in loop | 136 | 120 | 133 |
| Cached phase before loop gate | 138 | 128 | 72 |
| Selected positive-count do/while, cached phase | 138 | 128 | 77 |
| Literal tau | 135 | 112 | 107 |
| Literal phase and tau | 135 | 112 | 108 |
| All six float literals | 135 | 112 | 113 |

The selected body retains the guarded phase read and all recovered mutable
read contracts. Raw, unrelocated function digest:

```text
9b36dd52ce1411f49bae251814c8a252900c479b10c8c7e22e2eed05d14afbc3
```

This is **not**77 independent scheduling words. Retail retains the cached
active mask in FP/S8 and rematerializes the tau address at its eligible use.
The current extern-coefficient candidate retains that address in FP/S8 and
spills/restores the mask around sine, with the larger private frame. The
first fired private-store gate confirms the physical mismatch: retail saves
RA at STACK-4, raw C at STACK-20. Do not patch the frame to hide this.

Replacing tau with a float literal restores frame112 and the saved mask, but
caches tau in a saved FP register and rematerializes the null-actor fallback.
Retail instead saves the fallback32000 and rereads tau per eligible iteration.
Literal forms also introduce compiler .rodata storage that needs independent
provenance/relocation qualification. None is accepted solely for its frame.

Signed/unsigned mask, source-coordinate temporaries, explicit row cursors,
reused FP locals, register hints, const/array declarations, nested/continue
gates and early actor-address forms do not resolve the selected allocation.
The normal-unroll literal screens emit identical code to the no-unroll forms;
no production profile change is justified by that experiment.

One bounded Claude Code Sonnet advisory call used --safe-mode, disabled tools,
medium effort and no session persistence. It received only the relevant
source/assembly-role packet. Its allocation-weight explanation is a hypothesis,
not a measured compiler cause. Two useful structural suggestions were tested;
the three nested-gate/early-address combinations reproduce the same selected
raw digest. A suggested discarded/no-op use was rejected and not implemented.
No second advisory, agents, repository tools or setup/install work.

## Fresh Qualification

All **nine tests pass in14.190 seconds**, without skips:

- **105 fixtures/two phases:210 public-result pairs** compare complete
  experimental C and original retail against the independent reference.
  Check every public byte, ordered sine argument bits, callback stores,
  selected result and ABI-preserved GP/FP registers. Ordinary fixtures visit
  134 of136 retail words; the zero-actor branch is separately exercised below.
  This is not private stack/GP identity or literal-match credit.
- Native32 **O0, O2 and O2+UBSan** each pass105 full translated-buffer cases.
  Normal providers execute the retained Game sine C; forced-return/mutation
  cases are clearly modeled. Six effective negatives change tie equality,
  excluded state, mask-bit lane, cached count, cached state base or cached
  phase. Each exits21..26, not a signal or compilation failure.
- **88 actual-sine fixture pairs** connect the original104-word helper.
  Check the selected index, public buffers and exact ordered argument bits;
  the independent polynomial reference agrees. Helper exceptional paths and
  full hardware FP state remain outside this bounded acceptance claim.
- A completed backed, zero-linked actor-array pair exercises the original
  computed-null branch. A separate modeled NaN sine-result pair checks
  ordered comparison and first valid winner. Neither is a native null-array
  or hardware-FCSR claim.
- **20 actual returning-caller runs** retain JAL/full-word A0 delay load from
  A2+8, branch/RA delay load and SP/JR/NOP epilogue. The aligned ROM scan finds
  only CB968 /VA1509E4B8, inside func_1509E3DC. Its24-byte caller frame and
  saved RA are explicit live-ins; upstream switch execution is not claimed.
- **Three independent GNU maps /27 executed public pairs** rebase code,
  every selector global, contexts, actors and modeled provider entrypoint,
  including HI/LO carry boundaries. Both distinct bodies still agree with
  the reference; code bytes and private frames explicitly remain different.
- Both full-owner compiler profiles have empty diagnostics and preserve72
  other routines and normalized pools. The actual padder correctly rejects
  the552-byte candidate against the544-byte retail slot. A private pad with
  **only the original target retained** reproduces all73 baseline bodies,
  pools and addresses. This is not acceptance of the oversized target.
- Every frozen production input stays byte-identical. The fired first-store
  mismatch is retained as a negative matching result, not suppressed by the
  public tests or converted into a guard recipe.

Initial test-harness issues were corrected: mixed CALL/store event arities,
unused locals left by two negative controls, and the incorrect expectation
that an oversized target could pass padding. The corrected tests explicitly
assert that rejection. No production defect was inferred from those failures.

## Production And Resume

No production C, assembly, guard, Makefile, ELF, data or progress CSV edit;
no production build or new matching credit. README stays unchanged. Fresh
measurement remains **Game3006/4832 (62.21%)**, **total3679/5505 (66.83%)**,
**1,826 different/zero drift**, owner **58/73 exact,15 still different**.

The previous installed baseline remains ownerfaf1daec..., guardsbc019c19...,
ELF3010db54.... Full hashes are in the candidate's INPUTS. Three new task files
are mirrored identically while preserving all1,363 older dirty-file hashes
and the standalone mirror's old HEAD. Syntax checks pass in both copies; no
standalone mirror commit. No host-port or frozen Release changes or push.

Commands from64CBFD under WSL:

```sh
python3 -m unittest tools.tests.test_game_actor_sine_selector_recovery -v
python3 -m tools.experiments.game_actor_sine_selector_candidates --literals
python3 -m tools.experiments.game_actor_sine_selector_candidates --advisory
python3 -m tools.match_progress conker/progress.csv conker/build/conker.us.elf conker/conker.us.bin
```

Complete screen sources, commands, diagnostics, objects, qualification JSON,
native fixtures and advisory output/stderr remain ignored under
`conker/build/game-actor-sine-selector/`.

Next steps:

1. Continue the coefficient-storage and saved-lifetime recovery for this
   same function. Distinguish observed allocation from hypotheses about CFE/
   UOPT weighting. A bounded owned-compiler trace is preferable to treating
   more register-hint variants as evidence of the original source.
2. Recover frame112, the saved active mask, original fallback/one/phase FP
   lifetimes and the per-eligible tau load without dummy effects, volatile
   declarations or physical-register bindings. Qualify any literal pool and
   its canonical data anchors before proposing a relocation recipe.
3. Require exact private/access prefixes, the actual complete target fitting
   its136-word slot, independent rebases and a strict linked-image prediction
   before installation. The first RA-store mismatch must genuinely disappear.
4. Then rebuild, audit all other bodies/data/addresses, remeasure and update
   README aggregates. The broad Game decomp/matching goal remains active.
