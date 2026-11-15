# Radial effect guarded match and compiler frame provenance

Date: 2026-11-15. This closes the private recovery and frame boundary in
[Note 2466](2466-game-radial-effect-private-recovery-and-frame-boundary-20261115.md).
`func_150C29F0` is installed as semantic C in `conker/src/game_EF410.c` and
matches all **132 words / 528 bytes**, VA **0x150C29F0..0x150C2C00**, ROM
**0xEFEA0..0xF00B0**, with no alignment tail. Its original **0x88 frame**,
RA save at **SP+0x1C**, owner argument home at **SP+0x88** and packet at
**SP+0x3C** are restored. Eleven checked word normalizations complete the
match; this is a guarded C match, not a direct compiler-only match.

The production recount is **4,502 / 5,514 (81.65%) total**, Game
**3,829 / 4,841 (79.10%)**, Init **492 / 492**, Debugger **181 / 181**,
zero address drift and **1,012** still different. **185** further C matches
are required for at least 85%; that goal remains active. Conversion counts
and converted-byte percentages are unchanged.

## Source and ABI

The recovered routine submits a randomized radial effect and refreshes its
owner's timer. It preserves the nine-call sequence, byte angle and quarter-turn
offset, unsigned random remainder calculations, late owner-byte reads and
ignored constructor return. The timer becomes `random % 51U + 25`.

The named local `RadialEffectPacket150C29F0` preserves the original 72-byte
layout and all 69 initialized bytes. Bytes **0x35..0x37** remain uninitialized
padding and receive no defined-value credit. Unresolved codes and fields use
neutral local names. The constructor remains a pointer-returning function with
`u8 / u8 / s32 / u8 / s32` parameters after the packet pointer. Shared headers,
Makefile profiles and the conversion/classification CSV are unchanged.

`void func_150C29F0(u8 *volatile owner)` gives the local argument object a
volatile view so IDO preserves the observed argument-home reload lifetime.
This is an implementation choice supported by the emitted code, **not evidence
that the historical source used volatile**. The top-level parameter qualifier
does not alter the caller's pointer ABI. Existing float variables first receive
their random sample and then perform arithmetic in a separate assignment.
The `position` snapshot has a named local and the original phase-specific
owner lifetime; it is not an arbitrary padding object or register binding.

## Compiler observation and source fit

Owned, fingerprint-locked CFE/UOPT/UGEN observation completed for the retained
canonical, frame-0x88 diagnostic and split-assignment forms. All producer and
driver exits pass, both deliberately unfired/missing-exit controls reject, and
normal versus observed text, relocations and pools agree. Full object identity
is not claimed because debug metadata geometry differs.

| Retained form | Words | Frame | Saved / outgoing / locals |
| --- | ---: | ---: | --- |
| Canonical plain C | 129 | 0x98 | 16 / 24 / 112 |
| Frame-0x88 diagnostic | 133 | 0x88 | 8 / 24 / 104 |
| Split assignments to existing float locals | 134 | 0x88 | 8 / 24 / 104 |
| Accepted complete source | 132 | 0x88 | Original save and frame layout |

Canonical UGEN events show frame sizes **0 -> 16 -> 40 -> 152**; CFE reserves
104 local bytes and UOPT 108. The extra anonymous floating temporary at
**M-104**, level 1, begins at the inline random-radius multiplication. Splitting
assignments to the existing radius/scale locals removes that temporary: CFE
reserves 100 bytes, UOPT 104 and the final frame is 136 bytes. The owner lifetime
view removes the S0 save. Declaration order, bounded position snapshots and
the natural X/Y/Z packet stores finish the 132-word fit.

The original 48 screens and their 96 C/object fingerprints remain retained.
Further lifetime/home/position/order/coordinate screens remain ignored
diagnostics. The sibling overlay also completed the owned canonical observer
API, with identical code/relocations/pools and both effective controls. Its
frozen private CLI remains intentionally tied to the pre-adoption inputs.

## Eleven guarded words in five groups

The accepted raw body SHA-256 is
`c97d541c809848d9175d2f9c9445826a81acefcb4352973fbaa0a5dcf59c0566`.
Its 25 relocation bindings are independently pinned against assembled original
code. The normalizer checks the complete raw hash, complete relocation set,
each expected word and absence of a relocation at each changed site. No word
is inserted or omitted.

| Word indices | Checked adjustment | Boundary |
| --- | --- | --- |
| 6, 7, 8 | Angle byte-home store and subtract/mask schedule | A0 equals V0 after their common move; symbolic block state agrees |
| 22 | Radius multiply operand order | Restores source sample-first order and original `mul.s F2,F0,F4` |
| 27, 28 | Two disjoint halfword stores | SP+0x5C and SP+0x5E, with identical block effects |
| 39, 52 | One isolated pointer home, SP+0x84 to SP+0x20 | Only its store/load pair names either home; frame, packet and RA lifetime stay fixed |
| 104, 115, 117 | Closed owner scratch role, V1 to V0 | One owner load and two byte reads; no hidden use before the constructor's first JAL |

The private-home pair is explicitly a storage normalization, not merely an
independent instruction schedule. SP+0x20 is outside outgoing arguments,
packet storage and RA save; SP+0x84 is immediately beyond the packet. Neither
home is exposed to helpers. The defined owner domain excludes aliasing the
callee's private frame. Thirty-six corrupt-word/relocation controls reject.

The radius guard is also not justified by finite commutativity. With distinct
quiet NaNs and an explicit left-operand selection model, original/normalized
produce `7FC00001` while raw produces `7FC30002`. Under the explicit right
selection model those payloads reverse, and original/normalized still agree.
This closes the ordered instruction boundary; native exceptional payloads,
physical FCSR/traps and full 64-bit floating-register behavior remain outside
the qualification claim.

## Focused qualification

- **512 finite cases / three streams** compare original, raw semantic C and
  normalized MIPS, including all byte angles, unsigned random boundaries,
  owner/global mutations and two stack phases. Raw physical-stack equality
  is not credited. The actual **27-word** trig helper executes against its
  original 65-float table at ROM **0x23ECE0**.
- **114 exceptional cases / two streams** compare original and normalized
  full modeled state under explicitly selected NaN rules. **195 fired access
  prefixes** compare GPRs, FPRs, HI/LO, memory, calls, packet observations,
  traces, PC and delay-slot state. Every cut must actually fire.
- SDK32 native **O0/O2/O3** each compile the installed semantic body and execute
  **512 cases with eight effective source controls**, with UB traps. All
  128 owner bytes, eight global words and 69 defined packet bytes are checked.
- The original **45-word `func_15149264`** parent connects for **32 cases /
  three streams** through **D_8008A4C0[5]**, JALR **0x151492E8**. The expiry
  route visits 31 words and the refreshed positive timer prevents its free
  call. Other lifecycle routes and full caller physical-state parity are not
  claimed. Random and constructor providers remain modeled.
- Both production padders process the complete **18-function owner** and
  preserve all **17 neighbors** and normalized pools. Twelve independent GNU
  links cover four code/data layouts, including HI16/LO16 carry boundaries;
  every target link equals independently assembled original code. All **22**
  expected-word corruption controls reject in the two padders.

Fresh complete suites pass mounted before installation in **111.904 s**,
through the sibling overlay in **85.503 s**, and installed in **68.777 s**.
Each executes the current native profiles. `make tools-check` passes.
The native helper's optional control override is backwards compatible: its
default private-source harness was rerun, preserving its generated-source
and O0/O2/O3 executable hashes. Historical progress labels printed by reused
helpers are corrected in the enclosing stored report; they are not fresh
claims that installed code is private or that three streams are two.
Routine Claude calls: zero.

## Actual Make, strict image and preserved inputs

Actual production Make passes. Its independently reproduced five-command
chain covers the assembly processor, IDO, postprocessor, padder and assembler.
The final ELF equals the independent prediction byte for byte. Its **556
changed bytes** are completely accounted for with **zero exclusions**,
including eight closed symbol/string ordering groups involving 18 names.
No named definition changes are allowed by that metadata accounting.

All **6,051 function addresses** remain fixed. Only this target's body and
extent change, from the 12-byte placeholder to 528 bytes. Of **698 production
objects**, only `game_EF410.c.o` changes; its section differences are confined
to `.text`, `.rel.text`, `.symtab` and `.strtab`. Its ten newly referenced names
are exactly the original target's eight coefficient globals, trig helper and
constructor. No existing name disappears.

All **80 headers / 82 include inputs** stay fixed. The **189,088 protected
data bytes / 720 owners** remain identical, SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.
Of the 842 frozen inputs, only source, guard CSV, owner object and final ELF
change; the remaining **838** are byte-identical. All old guard CSV bytes
are preserved and exactly eleven target rows are appended. No classification
changes manufacture a new C count.

Production ELF SHA-256:
`6ead78c1257966a133ada96e0272f1ce476fb9eb167b5ded57091e56ce87628d`.
Fresh recount uses this actual ELF. Existing duplicate `generated_12D630`
Make-recipe and CSV line-ending notices are retained; no broad warning or
line-ending cleanup is included.

## Commit, graph and next target

Tools commit **`1e32e3c8a4440a41b7f06572233c7cdb9631e0a7`** precedes the
consumer source/guards/docs/pin commit. The unrelated sibling tools checkout
is preserved at **`ddbdd16b53ce60b054fb6e11bf0649a41f48375a`**, with all
**2,434 Windows-Git dirty paths** and raw status SHA-256
`a3712de44f2fc37079df4a789a5015f134f6ab977a2c2da90a3fde1851606cd9`
unchanged. The eight task files are tested through an ignored overlay.

Scoped Graphify AST refresh covers eight files, retains all **61,577 old IDs**
and records **61,601 nodes / 115,541 links**, zero lost IDs. This is not a
full-corpus extraction. Evidence is retained in
`conker/build/game-radial-effect-150c29f0-match/`; pre-install qualification
receipts are archived there separately. Compiler observations remain in
`conker/build/game-radial-effect-150c29f0-private/frame-observation/`.

Root README receives only its two aggregate matching rows; detailed changes
remain here and in concise index links. The `64CBFDOGL` path currently contains
only scratch `.codex` / `recomp_scene` directories and no Git/build root.
No host adoption is made and the frozen Release is untouched. No push.

Next target: adjacent **`func_150C2C00`**, **243 words / original frame 0xE8**
in the same owner. Recover its complete packet/loop and helper sequencing,
then qualify ABI, callers, native/guest behavior, guards, owner padding, actual
Make and the whole image before another match is counted.
