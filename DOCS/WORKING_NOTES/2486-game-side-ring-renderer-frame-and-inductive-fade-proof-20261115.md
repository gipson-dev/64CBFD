# 2486 - Side-ring renderer frame and inductive fade proof

The private `func_1519FE6C` recovery now emits **637 words / frame 0xF0**.
This recovers retail's frame and removes two words from Note 2485's selected
639-word / 0xE8 candidate. Retail remains **632 words**. The new body still
saves S0-S3 instead of S0-S2 and has **621 positional word differences**,
including its five excess words and shifted code. It is uninstalled and
earns **zero matching credit**.

Production remains **4,512 / 5,514 (81.83%)**, Game **3,839 / 4,841 (79.30%)**,
zero drift; **175** more matches are needed for the active 85% goal. The root
README's aggregate rows remain unchanged.

## Source and compiler evidence

Owner `conker/src/game/generated_1CC440.c`; VA `1519FE6C..151A084C`, image
`1CD31C..1CDCFC`. Separate forward and backward index lifetimes, separate
backward count/factor locals, and one entry pointer in the attached-point
seed reduce the body naturally. The initial forward factor is initialized
before its flag gate. No padding arrays, synthetic live values, volatile
declarations, compiler changes, or guard substitutions were introduced.

Full-owner compilation preserves all **38 neighbors** and all **13 pinned
relocations**. ECOFF storage and actual helper arguments retain the allocator
cursor at incoming-SP **-4**, sync at **-95**, texture halfwords at **-92**,
position at **-24**, and previous position at **-36**. The compact pool retains
the emitter's first twelve literal bytes and renderer epsilon; `.rodata`
continues to bind at `D_800A8CF4`.

Selected raw text SHA-256:
`4f1d014df4dccc1d394183098667e837cda18e904d9992ad952a134af72b9b0a`.
Both historical full sources remain pinned and are compiled and tested: the
initial 648-word / 0xF8 body and prior selected 639-word / 0xE8 body. Their
raw hashes and relocations remain checked independently.

Earlier retained screens established 638 / 0xF0 with separate backward state.
Address/byte views left it at 638; the float view grew to 653. Other kind-cache
and index compositions either retained extra words or enlarged the frame.
Entry-pointer/index composition produced the selected 637 / 0xF0 form.
The experiment sources, objects, diagnostics and reports remain in the
ignored `frame-2486/` directory rather than becoming conversion recipes.

## Inductive opening and fade-loop proof

`tools/tests/game_side_ring_renderer_1519fe6c_opening_proof.py` independently
executes the emitted instructions over symbolic state. It proves **six entry
paths, fourteen forward-fade step paths, and six backward-fade step paths**.
Loop cuts carry arbitrary indices, remaining counts and factors, so this
proof is not limited to a fixed number of loop iterations. Branch-likely
annulment, signed count gates, count narrowing, byte factor wrapping, public
light writes, allocator arguments and exposed output home are checked.
Saved GPR/FPR slots, return restoration and the exact private-write inventory
are checked separately from public effects and live cut values.

Public reads use stable ordinary-memory epochs; every public store and opaque
provider invalidates the epoch. This keeps arbitrary public aliases and
provider mutations within the proof domain. Private stack and code are
inaccessible through public pointers, and providers cannot inspect unpassed
locals or return PCs; the allocator may write only its exposed four-byte
slot. Its caller-saved registers/FPRs and FCSR result are otherwise arbitrary.
Mapped/aligned ordinary memory, valid o32 stack and normal instruction
execution are preconditions. Raw fault-register/PC parity and hardware FCSR
behavior are not claimed.

An independently reallocated scratch stream passes, showing the proof is
not a fixed retail-register comparison. **Ten deliberate corruptions** are
rejected: signed count, output address, forward index/count, light field,
factor wrap, backward initial wrap/count, signed count narrowing, and light
scaling. The proof stops before the six graphics providers and geometry;
**whole-function ordered FP/CFG normalization remains open**.

## Fresh qualification and preservation

- **299 guest cases per stream**, across retail, initial, prior selected and
  new selected bodies, compare complete public snapshots, helper arguments
  and returns. They visit **627 / 642 / 634 / 632 instructions**, respectively.
  All six existing guest corruption controls remain effective. Exposed-home
  and inactive/failed-allocation lazy-pointer checks pass for all four streams.
  Selected concrete FP operation order agrees in all 299 cases; this remains
  finite evidence, separate from the opening proof.
- **299 native cases per profile**, O0/O2/O3 with and without strict aliasing,
  UBSan, complete typed objects, 512-byte vertex/command windows and twelve
  source controls pass without new diagnostics.
- **128 connected cases per stream** execute the original 52-word allocator
  and 52-word dispatcher. All allocator words and 45 dispatcher words fire;
  cache/new/failure paths, both pages, signed views and returned cursor agree.
  Deeper allocation, transform and graphics providers remain bounded hooks.
- Both tools configurations run the three focused tests with identical seven
  task-file fingerprints. Primary elapsed **84.114 seconds**; sibling
  elapsed **100.909 seconds**, including process startup. The isolated
  overlay leaves all **2,434** sibling dirty paths and its HEAD/status bytes
  intact. These are fresh suites, not inherited native/guest receipts.
- All **881 frozen production inputs** remain byte-identical. No production
  source, guards, objects, layout, conversion rows or ELF was changed; no new
  production-Make or whole-image adoption pass is claimed. `make tools-check`
  passes separately. The previous checkpoint's receipts are archived.

Production ELF SHA-256 remains
`902b8b86f8ffc963c593e33b844245bf4d295dd69bd42944159f66be2b92d20e`.
No host source/build applies; frozen Release artifacts and saves are untouched.
Zero Claude calls were needed for this checkpoint. Scoped AST graph refresh
retains all prior IDs; native Graphify refuses a shrinking update and is not
forced or upgraded. Hook retention and the explicit target edge are audited
after the local commits; this is not a full-corpus extraction claim.

Reproduce in the prepared consumer:

```sh
python3 -m unittest tools.tests.test_game_side_ring_renderer_1519fe6c_recovery -v
make tools-check
```

Continue this renderer at the six graphics-provider setup, seed, texture and
geometry cuts. Resolve or prove the saved-S3 lifetime and five-word length
gap, extend ordered public/FP/FCSR equivalence over the remaining CFG, then
qualify any proposed normalization. Both padders, independent symbol rebases,
actual Make, strict full image, production recount and documentation gates
still precede installation and new match credit.
