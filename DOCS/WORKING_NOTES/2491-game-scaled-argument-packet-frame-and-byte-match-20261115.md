# Game scaled argument packet frame and byte match - 2026-11-15

`func_151A1010` now matches its complete **111-word / frame 0x78** retail slot.
The production zero-return placeholder is replaced with the recovered typed
28-argument submission. The independent source/FP/stack proof, both padders,
symbol rebases, actual Make, strict full-image audit and production checks pass.

A fresh actual-ELF recount is **4,515 / 5,514 (81.88%)** total and **3,842 / 4,841
(79.36%)** Game, with Init **492 / 492** and Debugger **181 / 181** exact. Address
drift is zero; 999 converted functions still differ. The active 85% goal needs
**172** further verified matches. Conversion rows and byte percentages are
unchanged. Root README receives only the two affected aggregate matching rows.

## Source and frame recovery

This continues [Note 2490](2490-game-scaled-argument-packet-recovery-and-ordered-fp-proof-20261115.md)
at consumer `f6778f38a01cdab7dfa55d64dba22b6c20700a4f` and tools
`9b7ba3f44fc87236a828c24f48798486af6e8579`. Owner remains
`conker/src/game/generated_1CC440.c`; retail VA `0x151A1010..0x151A11CC`, ROM
`0x1CE4C0..0x1CE67C`. The original 887-input freeze from the preceding production
checkpoint remains immutable; the intervening recovery commit changed docs/tools.

The accepted source computes `finalSpan = (s32)span + 16` **before** the clamp,
after the signed-short `span -= 32` and independent clamped-span copy. This ends
the modified formal's live range before the clamp. IDO no longer keeps it in S0,
so the saved-register pair disappears and the frame returns from 0x80 to retail
**0x78**. All packet FP expressions retain their original argument positions.

The resulting raw C is **106 words / frame 0x78**, with 64 positional differences.
It emits the complete retail **17-operation FP sequence**: nine multiplies and
eight truncations, with identical ordered operands and FCSR transitions. It
keeps original `D_800A8D28` (1500.0f), all 38 raw owner neighbors and normalized
16-byte pools unchanged. No profile change or physical-register source binding
is used. The function's numeric width/sign behavior is as recovered in Note 2490:
four reused results narrow after s32 truncation, while 90/20/15/10 products retain
full signed words; the last span argument uses the original wrapped span + 16.

Raw source SHA-256:
`b2ac3241502e4c7ede30704616c3683ba3989f233421ecf3eaa5eb2d0eeabe8f`.
Relocation-neutral normalized SHA-256:
`a642f80119553eef05c586362a392ba9c2fef2a4f44c2ab5f6951500c9b65cca`.

## Five short-result copies and source provenance

The normalization retains every one of the **106 compiled operations exactly
once**, with **five inserted short-view copies and zero omissions**. Copy offsets
in the retail output are `0x34`, `0xC8`, `0x100`, `0x134`, `0x14C`. They restore
the original span view and the four narrowed extent views in retail registers.
Each inserted OR-copy is derived from an actual source `sra ...,16` result;
the projected producer and its unbroken lifetime to the copy are checked.

The permutation is derived from independently executed instruction effects on
both clamp paths, with opcode, literal and relocation identity retained. The
span setup also uses the exact identity `short(short(v)) == short(v)` when
selecting the input to a repeated sign extension. This is more than a claim of
register renaming: the independent low-16 symbolic reduction proves that
equivalent input. All **17 FP instruction words** remain unchanged and in order.
No floating commutation, invented arithmetic, binary payload substitution or
instruction omission is used by the normalizer.

The **106 relocation-aware expected-word rows** fail closed on every compiled
word and all three source bindings. Both the strict retail-assembly padder and
layout padder emit all 111 original words, preserving the other 38 functions
and pools. Three independent constant/provider rebases pass, including signed
low-half carry boundaries. There are **109 raw-word/binding corruption controls**
and **16 actual stale-CSV rejections** across the two padders.

## Independent transfer, frame and return-register checks

The whole instruction checker proves both clamp paths with the real six-word
callee and with an opaque o32 provider. It covers all **106 raw / 111 retail
reachable words**, the complete 28-argument call, exact ordered FP/FCSR effects,
original incoming homes, saved ABI and return-address custody. Six effective
instruction corruptions are rejected; an independent T0/T1 allocation swap is
accepted without consulting the normalization template.

The stronger frame checker also compares the complete private word image at
the call and return, plus the original caller homes. A valid aligned write to
the unused four-byte gap below saved RA passes the earlier public/ABI checker
but is rejected by this stronger relation. This is an effective private-storage
control rather than a malformed instruction or deliberately invalid address.

Both **V0 and V1 incidental result values** agree in the raw and retail streams
under both provider contracts. The type remains an inferred void submission,
consistent with the neighboring wrappers; no known C/header caller or aligned
retail direct call/pointer literal references this entry. Computed runtime
references are not disproved. Preserving the result-register pair closes the
emitted return-ABI concern without inventing a promised return API. The installed
111-word body is literally byte-exact.

These are mapped, non-faulting normal-execution proofs with immutable literals
and providers unable to inspect code/return PCs or unpassed private bytes.
Full intermediate register/private-state identity, hardware faults, portable C
undefined-input behavior, complete dynamic reachability and gameplay acceptance
are not claimed. Boundary private-word images are distinguished from arbitrary
instruction-prefix states.

## Fresh validation and review disposition

The five-test suite passes before installation, through the sibling overlay,
and after production installation: **75.899 s**, **99.306 s** and **72.774 s**,
including process startup. All three runs use the same eight task-file hashes.
Each freshly compiles the complete owner and qualifies:

- **528 guest cases per three streams** (retail, raw fitted C, guarded C), real
  callee execution, all 256 variant bytes, both stack phases, short boundaries,
  selected high-bit argument words and wider full-s32 products.
- **496 guest-checked native vectors plus all 65,536 signed-short inputs** per
  O0/O2/O3 and strict/no-strict-aliasing profile: **66,032 cases x six profiles =
  396,192 native cases per run**, with UBSan and float-cast-overflow traps.
- Four effective source negatives, both symbolic checkers, exact padding,
  independent rebases and stale input controls described above.

An initial native negative changed a call argument and left `finalSpan` unused;
the compiler rejected that fixture before execution. The corrected negative
computes the wrong clamped offset after the clamp, compiles, and fails on its
actual packet result. The failed receipt and original two checker files remain
archived; the three successful runs above are fresh after correction and the
added V0/V1 gate. `make tools-check` also passes. No unchanged broad neighbor
semantic suite is called a fresh test.

One difficult-lifetime Claude call was attempted/completed through the existing
claude.ai/firstParty Pro route, with no account/model override. Current init
reported **tools=[] / mcp_servers=[]**, and the stream contains zero tool uses.
Packet-only review addressed the frame/span-lifetime experiment, not repository
actions. Packet SHA-256:
`bde7ac688bd0ffa5cead163e5b95f3c9a5d3cfcae10c28bf8165af39b02c1dca`;
answer SHA-256:
`7bb9ce85a3f15c354675384044c6ed20014535d7c6ab5c6be7a5e6fc3ee5a956`.
The predicted independent-cast +2-word fit is rejected by compilation: it emits
the prior 109-word / wrong-FP body. The second proposal duplicates an already
tested post-subtraction condition. Verified retail short-view/S0 observations
are retained; neither source proposal is adopted. The final-span lifetime fix
and five-copy derivation are independently investigated and validated by Codex.
Packet, response and disposition remain under the ignored frame-2491 receipts.

## Production image, preservation and continuation

Isolated actual Make and the real production Make compile this semantic owner,
read the real guard CSV and link. No qualified prebuilt object is substituted.
`-o retail_word_patches.us.csv -o Makefile` prevents a global timestamp rebuild;
the changed source still runs its real owner recipe. The existing duplicate
generated_12D630 recipe warnings remain unrelated.

The actual production ELF equals the independent prediction across the whole
file. All **401 changed bytes** are accounted for with **zero exclusions**:
the exact target instructions/size and two closed GNU symbol/string permutations,
with equal named definitions. All **6,050 other functions and addresses**, 697
other objects and 38 owner neighbors remain fixed. The 189,088 protected data
bytes stay exact, with SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

Of 887 frozen inputs, only C, CSV, owner object and ELF change; **883 remain
unchanged**. The four planned overrides are separate from the immutable baseline.
Old guard bytes and all progress classification rows remain unchanged. Earlier
accepted-function semantic receipts are reused with unchanged inputs and the
fresh complete owner/linked image audit, not rerun under stale whole-owner pins.

Production ELF SHA-256:
`44b11be552ab908f609bf3e994c4cb94a50a7264c61d0a74a39be4bff90a19e7`.
The sibling remains `ddbdd16b53ce60b054fb6e11bf0649a41f48375a` with all **2,434**
dirty paths and their Windows status fingerprint unchanged; only an eight-file
disposable overlay supplies this task. Host Release artifacts and saves remain
untouched. Graphify uses guarded native/scoped updates and post-hook old-ID
retention, with no force, upgrade or full-corpus extraction claim.

Maintained files use the `game_scaled_argument_packet_151a1010_` prefix in tools.
Fresh receipts are at
`conker/build/game-scaled-argument-packet-151a1010-private/frame-2491/`;
the prior Note 2490 receipts remain intact in its parent stage.

```sh
python3 -m unittest tools.tests.test_game_scaled_argument_packet_151a1010_recovery -v
make tools-check
# From 64CBFD/conker:
python3 ../tools/match_progress.py progress.csv build/conker.us.elf conker.us.bin --version us --objdump mips-linux-gnu-objdump
```

Next: qualify the complete `func_151A11E4` update/emission routine in this owner,
starting from its original retail window and caller ABI. The wider 85% goal
remains active; this completed function contributes exactly **one new match**.
