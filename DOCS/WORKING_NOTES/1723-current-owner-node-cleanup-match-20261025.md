# Current-Owner Node Cleanup Direct C Match

2026-10-25. Qualified, installed and adopted. The actual Native-ELF recount is
3,799 / 5,505 byte-exact C functions (69.01%), with zero address drift.

## Recovered Routine

The recovered `func_150AFDB0` replaces its zero-return placeholder in
`conker/src/game/generated_DC6B0.c` with a deletion-safe linked-list walk.
All 45 words / 180 bytes emit directly from normal IDO O2/g3, with frame 0x20,
19 original bindings, no alignment tail and **zero new guards**.

- VA: `0x150AFDB0..0x150AFE64`; VROM: `0xDD260..0xDD314`.
- Interface: `void func_150AFDB0(void)`. The original caller ignores V0.
- Preserve signed-byte depth `D_800DD190`, head pointer `D_800DCE94`, six
  iterator slots at `D_800DD198`, and unsigned current-object byte `D_800C3E78`.
- Increment the depth even when the head is null. Preserve retail's early head
  read, before the incremented depth byte is stored.
- Save each node's next address in the current iterator slot before checking
  its owner. The canonical node is `struct102`, size 0x1D8: `unk8` is the
  32-bit next-node address; `pad3E[1]` is the owner byte at +0x3F.
- Call `func_1516972C(node)` only when the unsigned owner matches the live
  current-object byte. A callback may change future owners, the current object,
  the iterator slot, or the depth. Reload depth and slot after the call.
- Decrement the live depth at the end, not a saved entry value. Preserve S0's
  current-object-address lifetime, RA, branch-likely loads and frame teardown.

Both natural `while` and guarded `do/while` forms match. The simpler `while`
form is selected. Raw direct-C SHA-256:
`483ed4239082edc00e7a45e6d3b03f4bfe18a2adcd567f3b454da7986942a523`.

## Types And Existing Code

Use the existing canonical node rather than introducing an incompatible
private record. Explicit pointer conversion preserves the existing 32-bit
guest address in `unk8`. The typed cleanup-helper declaration also requires one
matching pointer cast in neighboring `func_150B02C0`; all 17 neighbors retain
their raw/padded words, bindings, pools, extents and addresses.

The owner retains its one `GLOBAL_ASM` routine and its normal five-command
Make recipe, including assembly preprocessing/postprocessing. No shared header,
compiler profile, original assembly or guard CSV changes. The two existing
Warning 712 diagnostics in `func_150B02F0`/`func_150B031C` and the duplicate
`generated_12D630` recipe warning remain; the build is not warning-free.

The complete aligned ROM scan finds one JAL at VROM `0x9B584`, with no aligned
literal target pointers. This does not rule out arbitrary computed calls.
Original `func_1506DE84` is 154 words at VROM `0x9B334`; its 14-entry table at
`0x80099D54` selects this walk in mode 13. The current C caller is still a
12-byte stub. Its source/object remain unchanged and receive no recovery credit.

The existing release helper first invokes iterator repair `func_151696DC`.
Tests connect that actual 20-word body, the 28-word `func_1516972C`, and its
eight-word default tail `func_15169804`. Type-specific callbacks and the final
release provider remain bounded providers, not full heap/gameplay acceptance.

## Qualification

Both tools copies pass six fresh pre-install checks, with zero errors,
failures, skips or reuses: primary 35.819 seconds; older mirror 56.842 seconds.
Both shared checks pass, in 0.323 and 0.299 seconds respectively.

- 1,920 guest phases cover live owner, next-pointer, iterator and depth changes,
  all 256 current-owner values and all 256 empty signed-depth byte patterns.
  Every target word executes, with complete modeled GPR/FPR/RAM/event agreement.
- Native32 O0/O2/O3 with trap UBSan each pass 2,560 cases. These use canonical
  `struct102` objects, valid six-slot backing, full node/guard-byte checks, and
  actual C re-entry. Six effective owner/filter/unwind/cached-next controls fail
  as expected. These are bounded combinations and exhaustive individual axes,
  not all possible Cartesian inputs or native out-of-range/alias guarantees.
- 576 full original-caller phases cover mode 13 and unsigned out-of-range
  modes, nested frames and caller-saved clobbers. Other caller modes are not
  qualified by those cases.
- 120 actual helper-chain phases cover signed iterator counts, matching and
  nonmatching saved slots, record kinds 0/1/2/7/255, callback/default branches,
  and both stack phases. All 56 connected helper words execute.
- Seventeen independent GNU links cover 19 bindings and HI/LO carries:
  nine normal/rebased links plus eight links for four explicit guest aliases.
  Eighty-one rebased phases agree. The alias fixtures relink both instruction
  images to the chosen global addresses; changing fixture addresses alone was
  correctly rejected by the first run.
- 166 fired target-access fault prefixes agree in complete state, PC,
  delay-slot context and dispatched word. This is guest instruction-order
  evidence, not portable C fault semantics, an MMU or hardware acceptance.
- All 45 word corruptions, 19 binding corruptions, nine strict-image controls,
  six frozen-input mutations, the stale stub and a wrong symbol definition are
  rejected.

## Exact Image Accounting

The independent full image differs by exactly 162 bytes: 151 target code bytes,
one symbol-size byte (12 to 180), and ten bytes in one closed GNU symbol/string
serialization permutation. `D_80095BC0` and `D_8009EFC0` exchange their adjacent
records/strings. Their names, values, sizes, bindings, visibility and sections
remain identical. Exact preconditions and the existing bounded serializer
account for the permutation; no whole metadata section is excluded.

The first prediction rejected those extra ten bytes. The corrected prediction
still compares every image byte and verifies named-definition equality.
Expected ELF SHA-256:
`66bdd012b8d94c6d1d998f3ee6392703b21ae99f754e637efde85078084cc838`.

## Recovery And Evidence

An interrupted launch wrote its runner but did not start a worker; live process
inspection confirmed that before retrying. A later launch found the old `/tmp`
WSL cache missing after session restart. Native inputs and frozen evidence were
intact. A verified stream recreated 16,058 inputs in a fresh `/var/tmp` cache,
with executable bits restored without content changes and no project reads via
DrvFS. All content hashes matched. The original cache was not deleted.

Qualification was rerun in the new cache. A subsequent alias-fixture correction
did not change the C, its source module or its four qualified artifacts; those
identities and all 36 frozen inputs are checked before reusing owner/Make
evidence. Both complete semantic suites were then rerun fresh. Failed capture,
image, missing-cache and alias receipts remain separate from accepted results.

## Production And Progress

Tools commit `0fa6f1aec51450b411589c361acf9df1855a4640` precedes the consumer
pin and source. Actual production Make exits zero and reproduces the independent
162-byte full-image prediction, with no exclusions. All 6,055 linked functions
retain their addresses; the other 6,054 bodies remain fixed. All 720 protected
Game-data owners / 189,088 bytes remain exact, SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

Each tools copy then passes two fresh installed checks. Four unchanged semantic
checks are explicitly reused only after the complete input, module and qualified
artifact fingerprints match; they are not reported as fresh tests. Native
adoption verifies all 16,058 sealed inputs before and after copying the qualified
outputs. Only the target source, target object and linked ELF differ from the
sealed baseline. The guard CSV remains unchanged.

The recount uses the actual adopted Native ELF, streamed to the verified cache.
Total: **3,799 / 5,505 (69.01%)**; Game: **3,126 / 4,832 (64.69%)**;
Init: **492 / 492**; Debugger: **181 / 181**. Zero address drift, 1,706 still
different. Reaching 75% requires 4,129 matches, **330 more**. Only this target
leaves the preceding mismatch queue. Adopted ELF SHA-256:
`66bdd012b8d94c6d1d998f3ee6392703b21ae99f754e637efde85078084cc838`.

## Handoff

The next ordinary placeholder is `func_1518E524`, owner `generated_1BA1D0`,
45-word retail slot. Its queue entry is not a qualification. Keep existing-C
`func_15014094` and parser-missed
`Gfx *func_1510D8C0` separate; screened candidates remain uncredited.

Baseline consumer `bedb3e2b7e11dff7d4e584e249f8bd7207dafd62`, tools
`283d45faaac49a6f0777657d8b082cc05686d6d2`. The capture normalizes the preceding
three adoption overrides and preserves the older mirror's 1,656 changed paths
and HEAD, adding only the two owned modules. No mirror commit/reset/stash.
Local receipts: `conker/build/game-current-owner-node-cleanup-match/`.

Claude calls: zero. No host/editor/Release, dependency, global configuration or
gameplay changes. Nothing is pushed. The wider 75% goal remains active.
