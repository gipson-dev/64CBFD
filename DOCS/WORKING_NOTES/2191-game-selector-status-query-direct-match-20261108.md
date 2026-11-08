# Selector Status Query Direct Match - 2026-11-08

`func_1509C7C8` emits all **77 words / 308 bytes directly from semantic C**,
with **no frame and zero instruction guards**. Its existing six-entry jump
table is retained through one scoped Make binding. The guard manifest is
byte-for-byte unchanged. No compiler-profile or shared-header change.

Production recount: Total **4,260 / 5,513 (77.27%)**, Game **3,587 / 4,840
(74.11%)**, Init **492 / 492**, Debugger **181 / 181**, zero address drift.
There are **1,253** different converted functions and **151** additional
exact functions needed to reach 4,411 / 5,513 and the active 80% goal.
Conversion rows and denominators remain unchanged.

## Source and selector behavior

Owner: `conker/src/game/generated_C98F0.c`; original slice `asm/C98F0.s`.
VA 0x1509C7C8..0x1509C8FC; ROM 0xC9C78..0xC9DAC. The recovered interface:

```c
s32 func_1509C7C8(u32 identity, u32 selector, u32 *record);
```

The registered caller supplies the record pointer as argument three.
This query does not dereference it; IDO retains its incoming SP+8 spill.
The full identity and selector words remain intact.

- Selector 1 rejects a nonzero D_800C35C4 byte. Otherwise mode zero returns
  one; nonzero mode returns whether the full identity differs from the
  unsigned byte at D_800C3C98. Keep this ordered gating/read behavior.
- Selector 2 requires mode exactly one and identity equal to that comparison byte.
- Selectors 3 and 6 require mode exactly one and identity equal to the
  unsigned byte at D_800C35E8.
- Selector 4 returns whether the mode byte differs from one.
- Selector 5 returns the complete unsigned D_800C3672 byte, including
  values 128..255. It is not a boolean conversion.

## Out-of-range selector boundary

The initial next-target handoff predicted a zero default. Complete word
inspection corrected that assumption: selector-minus-one is checked
unsigned, and out-of-range values reach JR RA / NOP **without assigning
V0**. The original machine path preserves the incoming V0 word.

The recovered switch therefore has no trailing C return. Selectors 1..6
have defined C results; other selectors have no defined portable C return
value. Do not add a default-zero return or claim portable C preserves V0.
An actually compiled default-zero control grows to 80 words and returns
zero for an input where the original returns the incoming 0xDEADBEEF.

Guest checks qualify the entire emitted machine routine, including invalid
full-word selectors, arbitrary incoming V0 values and the original caller's
result propagation. Native C tests use selectors 1..6 and disable GCC's
return-type warning for this preserved source shape. No invalid-selector
native result or cross-compiler portability claim is made.

## Original registered caller

The pristine aligned census finds no direct entry/interior JAL and exactly
one entry pointer, ROM **0x22CF58** / VA **0x80088498**, D_80088498[0].
Six interior pointers are the original jump-table cases, not independent
entry registrations. The six targets at **jtbl_8009E458**, ROM **0x242F18**,
are relative body offsets 40,120,172,224,244,256.

The original **31-word** dispatcher window, VA **0x150AE118..0x150AE194** /
ROM **0xDB5C8..0xDB644**, loads the full selector from record+4 and passes
the record pointer as argument three. It decodes the handler nibble from
record word zero, selects registration slot zero, allocates a 16-byte
outgoing home, and calls through the original JALR at **0x150AE180**.
The delay slot clears only identity bits 12..15, preserving its high bits.
The wrapper uses its original S7/RA convention and returns the query's V0.

**324 connected cases** compare an independent reference, the original
body, raw C and bound C through this window. They cover high identity bits,
valid/invalid full selectors, raw byte results, incoming V0 poison, both
stack phases, third-argument spill and final SP/RA restoration. The larger
script interpreter and full gameplay reachability are not claimed.

## Compiler, table and owner evidence

Actual Make confirms O2/g3 MIPS2/O32 before screening. Both unsigned and
signed selector declarations produce the retail words; the selected
unsigned view matches the raw record packet. Full-owner and isolated
compilation agree across all **77 words and 24 bindings**, with empty C
diagnostics. The final pointer-typed interface was freshly requalified
after the initial word-typed unused-argument screen.

The generated 32-byte compiler pool contains six case relocations and
eight padding bytes. Its two code references are bound to the existing
retail table through the sole new Make row:

```make
$(BUILD_DIR)/$(SRC_DIR)/game/generated_C98F0.c.o: RETAIL_RODATA_SYMBOL := jtbl_8009E458
```

Both padders agree on all three function bodies and preserve **12**
original case/interior labels. The actual **three-command** Make recipe
produces the same three-function object. Both raw/padded neighbors, the
exact register-mask union, original table contents and all other pools
are preserved. Corruption controls reject every raw word, every binding,
all 72 register-metadata byte changes, all 32 generated-pool byte changes
and each of the six changed case relocation targets.

## Fresh execution and literal image proof

Six focused checks pass before and after installation in both tools copies,
with four final sequential runs and identical source/dependency fingerprints.

- **4,765 guest cases**, all **77 words reached**, all **256 raw status
  byte values**, and **21 invalid-selector cases**. Independent complete
  memory/results/read order agree. Original and bound C have identical
  literal states and instruction/access traces.
- **44 guest-only home/table/global alias cases** and **225 exact fault
  cuts** qualify the original SP+8 spill and subsequent conditional reads.
- **4,744 native32 cases per profile**, O0/O2/O3 with trapping UBSan and
  all eight effective semantic controls. Every global stays unchanged.
  Native fixtures cover only the defined selector domain.
- Three independent GNU links and **24 rebased executions** cover every
  selector and both invalid boundaries, including low-half address carries.

The independent whole-ELF predictor changes only this 308-byte body and
its symbol extent from 12 to 308 bytes: **223 changed bytes, zero exclusions
and zero metadata permutations**. Actual Make produces the identical ELF.
All **6,052** disassembled entries retain their addresses; every other
body, extent and metadata byte is unchanged. Protected data remains exact
across **720 owners / 189,088 bytes**, including the original jump table.
Five corruption controls cover header, body, extent, general data and that
specific table. The regenerated progress CSV is identical.

Both shared tools smoke checks are fresh. Three prior helper regression
checks per copy are reused with exact unchanged helper/test fingerprints.
The sibling's **2,434 existing dirty paths** are preserved with a private
three-file overlay. Source baseline consumer `2db0719336bf9c22d40cb532c0d454d7fcc0935e`,
tools `a3878834e7e0db5449f8fcab6871f6ce2ba89a8e`; **103 frozen inputs**.
Claude calls: **0**, because local compiler/caller/oracle/image evidence
settled the recovery. Existing whole-ROM checksum failure (make all exit2)
and duplicate generated_12D630 recipe warning remain; no new C warnings.

ELF SHA-256: `ad4ca11544662ecbafe0e09850fdfab2fc3f46d0a116d1d3eaa856695c328963`.
Binary SHA-256: `44ff05e8394fed100f587df8ff20489e62a5c77e4031ee537eb3fc8a3afb9cdb`.
Owner SHA-256: `56333e9947fad1316fb0530f9ceec3243c7bad0ea06ec1ef9dd9bbf23d340a34`.
Guard CSV SHA-256: `f67f8d18908dc6db9ba58dfa2db4b4204a7202104e67173c35213711333f4dd9`.
Makefile SHA-256: `8e676e04318f8645e6b277ed60ed9f221d8901a5e6a02efd279d478d46a615f8`.

## Resume boundary

Next: **`func_151872B0`**, still an uncredited placeholder in
`conker/src/game/generated_1B1600.c`. Its original body is **77 words /
308 bytes**, VA 0x151872B0..0x151873E4 / ROM 0x1B4760..0x1B4894, no frame.
Recover the ordered mixed word/byte/FP defaults at D_800DE01C..D_800DE041,
then overrides for full-word argument values 0x14,0x21,0x22,0x29. The
0x3F800000 store is an exact 1.0f payload. Preserve live original address
lifetimes, repeated stores, branch-delay byte updates and the unreachable
duplicate immediate at relative +0x118. Audit all declarations, original
callers, owner/compiler profile and protected data before compilation.
Graphify currently supplies placeholder/owner relationships, not a prior
qualified recovery. Apply the complete normal adoption gates before credit.

Current receipts: `conker/build/game-selector-status-1509C7C8-match/`.
Tools are committed before the consumer pin. The scoped Graphify refresh
includes old-node retention evidence and retains existing unscanned nodes;
it is not a new full-corpus extraction. The host Release checkpoint remains
frozen. The 80% goal remains active.
