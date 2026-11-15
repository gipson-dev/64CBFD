# Note 2475: Actor/effect binding register roles and byte match

Date: 2026-11-15. Consumer baseline
`4c63a933e7b17751ef33dd4d07c24e4a494ae178`, tools baseline
`de154c556ed11c749e9348c70b06e338833cd0ad`.
Continues [Note 2474](2474-game-actor-effect-binding-private-recovery-and-frame-20261115.md).

`func_150C4120` is installed as typed C and matches all **225 words / frame
0xF0**, using **70 expected-word guards**: 68 register-allocation words and
two accesses to a private pointer cache. Actual production Make, both tools
paths, the installed suite and the strict full-image gate pass. All **698
production objects and the complete ELF remain byte-identical** to baseline.
The progress change is one **900-byte routine classified ASM -> C**.

Fresh actual recount is **4,507 / 5,515 total exact C (81.72%)**, Game
**3,834 / 4,842 (79.18%)**, Init **492 / 492**, Debugger **181 / 181**, zero
address drift and **1,008 still different**. Converted totals are **5,515 /
6,048 (91.19%) / 86.20% bytes**; Game **4,842 / 5,327 (90.90%) / 85.58%
bytes**. Both exact numerator and C denominator increase by one, so the total
percentage still rounds to 81.72%. At the current denominator, **181 further
matches** reach 4,688 / 5,515 and the active 85% goal.

## Installed source and compiler boundary

Owner `conker/src/game/generated_F15D0.c`; VA `0x150C4120..0x150C44A4`, ROM
`0xF15D0..0xF1954`; **900 bytes**, no alignment tail. The signature remains
`void func_150C4120(u8 *actor, s16 requestedLifetime, u8 priority, s32 context)`.
The recovered payload, definition, random parameters, palette and vector are
28, 112, 16, 16 and 12 bytes. The payload's +0x0C field is now a typed effect
pointer, with the destination declared as a payload pointer.

The complete C body retains the allocation-failure paths, signed lifetime
sentinel, actor-type selector, seven full-width integer random draws, two
floating draws, palette snapshot, vector-copy timing and final coefficient
load described in Note 2474. The effect pointer is stored at primary+0x34
even when the second allocation fails. Padding fields are explicitly named;
their portable C contents are not prescribed. Original external symbol names
remain intact, with descriptive local types and a semantic function comment.
No alternate-source implementation, shared declaration, compiler profile,
Makefile or constant-pool change is imported.

The first-flag ternary improves the private 78-word discrepancy to 72. The
typed effect field and declaration order reduce it to the selected **70**.
Raw body SHA-256:
`c20a4c21238ca29a334d53130c339685fa5f354c491b6f3f303be2a787cabe04`.
All **23 relocation binding locations** are pinned independently.

The 68 allocation guards preserve opcodes, immediates, shift/function fields,
branches and relocation locations. Word 55 changes `0xAFA40038` to
`0xAFA40030`; word 214 changes `0x8FA30038` to `0x8FA30030`. These exchange
the nonescaping pointer cache at raw SP+0x38..0x3B with retail SP+0x30..0x33,
and the corresponding unused four-byte home in the opposite direction.
The complete bijection covers eight bytes; SP+0x34's first flag, saved RA,
outgoing arguments and aggregate locations remain fixed. There are no inserted
or omitted instructions and no floating operation or schedule changes.

## Register, memory and caller qualification

The symbolic role audit reaches all 225 words, **72 abstract returns** and
**2,580 transfer steps**. It checks every actual operand read, memory input,
o32 argument and ABI output, including physical V0. Opaque calls preserve
callee-saved roles and refresh caller-saved roles. A wrong-source control
passes the instruction-shape gate and is rejected by the read-role gate.
Literal identity of dead caller-saved GPRs is explicitly uncredited.

Guest checks pass **512 cases across retail, raw C and normalized streams**,
visiting all 225 retail words. They compare all seven copied padding bytes:
binding offsets 5/6/7/0x17 and definition offsets 0x67/0x6A/0x6B.
**2,782 fired memory-access prefixes across 12 complete routes** compare mapped
private/public RAM, actual read values, floating registers, HI/LO, saved and
argument state, PC/delay state, calls and packet snapshots with the qualified
cache mapping. **48 modeled exceptional-FP cases** cover both NaN-selection
rules; hardware FCSR behavior is not claimed. All **248 body/binding
corruptions** are rejected.

The retail call census closes the previous return-use handoff:

- `func_150265CC` directly calls the root at ROM 0x54DF4 / VA 0x15027944.
  Its branch-delay instruction at 0x15027950 replaces V0 with 1.
- The second root call is in the complete ten-word wrapper `func_1514F568`
  at ROM 0x17CA28, with fixed lifetime -1, priority 255 and context 1.
- `func_15065A5C` calls that wrapper at ROM 0x97778 / VA 0x1506A2C8.
  All 44 following CFG nodes before `move V0,S3` at 0x1506A5BC contain no
  return-value read. Branch-delay and branch-likely behavior are included.
- The loaded wrapper pointer is **D_8008AA70[49]** at ROM 0x22F5F4 /
  data VA 0x8008AB34. The nearby D_8008AACC symbol is not this table's base.
  The three indexed callback routes in `func_1514D15C` also discard V0
  before a use; the exact sinks are retained in `caller-report.json`.

**1,536 connected cases / three streams** execute the direct root window,
wrapper parent window and registry window, including the complete wrapper
on its two routes. Guest padding compares literally; **nine V0 poison
controls** are overwritten by the direct caller. The known retail callers
support the void interface. Whole execution of the large parent routines
remains uncredited.

Native32 passes **512 cases at each O0/O2/O3** with UBSan and **nine effective
controls per profile**. All seven native padding bytes remain uncredited.
The existing native fixture still accepts its original default-source API;
that path was rechecked without changing its retained source/executable
fingerprints. The old private recovery suite's frozen ASM baseline is
historical; the new installed match suite is the adoption gate.

## Build, image and preservation audit

Both padders preserve the **six owner functions / five neighbors**, all pools
and the complete target slot. **140 corrupt expected-row controls** fail;
**12 GNU links across four code/data carry layouts** pass. The actual Make
shadow uses five commands and the owner's generic `pad_generated_object`
recipe; the independent target tests also cover `pad_c_object`.

Fresh complete suites pass in **118.237 s before installation**, **128.385 s
through the sibling overlay** and **119.998 s after installation**. Fresh
`make tools-check` passes. The production command is:

```sh
make -C conker -j4 -o Makefile -o retail_word_patches.us.csv build/conker.us.elf progress.csv
```

The independent strict-image prediction and production audit report **zero
changed ELF bytes, zero exclusions and zero metadata reorderings**. All
**6,051 function bodies, addresses and extents** agree. All **189,088 protected
bytes / 720 owners** agree, SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.
The ELF remains
`f6500a14961e2c876619e1491b0245c7b5ec2f81fd7efe43f58ab345ef229939`.

Of **859 frozen production inputs**, exactly three change: the owner C file,
the guard CSV (70 appended rows) and the progress CSV (one ASM -> C row).
**856 inputs remain identical**; all 698 objects remain identical. Separate
section progress receipts show only the same Game classification change;
Init and Debugger are unchanged. The existing duplicate generated_12D630
recipe warning, two neighboring pointer/integer warnings and Git CRLF notices
are retained; no warning-free build is claimed.

## Checkpoint and continuation

Tools commit **`074dfa4925bfed6c4235eef835fff95104c73122`** precedes the consumer
source/guards/docs/tools-pin commit. The eleven-file ignored sibling overlay
leaves sibling HEAD `ddbdd16b53ce60b054fb6e11bf0649a41f48375a`, all **2,434
dirty paths** and status SHA-256
`a3712de44f2fc37079df4a789a5015f134f6ab977a2c2da90a3fde1851606cd9` unchanged.
Scoped AST extraction covers **11 files**, retains all **61,943 prior IDs**
and records **61,988 nodes / 116,123 links**, zero lost IDs. This is a scoped
refresh, not full-corpus extraction; post-commit heading aliases retain old
document IDs when the hook moves their line locations.

Five DOCS indexes receive one concise entry with all old bytes retained.
The root README changes only four aggregate rows. No host-port source/build
applies; frozen Release, saves and private inputs remain untouched. No push.
Claude calls: **zero**, using existing compiler, oracle and image tools.

Evidence is retained in
`conker/build/game-actor-effect-binding-150c4120-match/`: the frozen production
baseline, raw source/object, 70 proposed guards, binding manifest, role/guest/
native/caller/padder reports, three suite receipts, archived preinstall
qualification, actual Make commands, strict image, production audit, recount,
conversion statistics, sibling snapshots and graph receipts. The prior private
recovery folder remains retained as historical evidence.

Next: **`func_150A613C`**, the current 53-word / 212-byte zero-return C
placeholder in `conker/src/game/generated_D3040.c`, VA
`0x150A613C..0x150A6210`. The actual recount reports 53 real word differences.
It is already counted as C, so matching it can increase the numerator without
adding to the denominator. Requalify its complete retail/caller/owner contract
before adoption. The 85% total matching goal remains active.
