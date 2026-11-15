# Game view reset proven guarded match

Date: 2026-11-15. `func_15017640` is adopted as a complete, correctly typed
`void func_15017640(void)` view/projection reset in `conker/src/game_44A90.c`.
Its **82 body words / two alignment words** are now byte-exact, with the
original **0x28-byte frame** and RA save at **SP+0x24**. The full slot remains
`0x15017640..0x15017790`, ROM `0x44AF0..0x44C40`.

This closes the private recovery in
[Note 2462](2462-game-view-reset-private-recovery-and-prefix-proof-20261115.md)
and earns **one new exact C match**. The source replaces the zero-return stub
and removes the obsolete commented draft. It clears all six record flags,
rather than the old draft's four, and uses accurate owner-local storage types
for the matrix, normalization halfword, scale/vector arrays, records and
192-byte scratch area. Shared declarations and compiler profiles are unchanged.
The owner's other routine, `func_150175E0`, is preserved; owner **2 / 2 exact**.

## Thirteen checked scheduling words

The pointer-scale form emits all 82 semantic instructions directly from C.
Thirteen append-only, expected-word/relocation guards normalize the opening
motion-vector register choice and independent address-setup order. There are
no inserted or omitted instructions, arithmetic replacements or other-owner
guards. The remaining 48-word suffix is identical before normalization.

The closed 34-word prefix proof from Note 2462 is applied to the exact raw
and normalized streams. It compares arbitrary symbolic input halfwords and
incoming register/FPR values, ordered memory accesses, saved RA and final
state. A2 is the only different GPR at the join; the suffix does not read it
before its overwrite, and the intervening bzero takes only A0/A1. Providers
observe declared arguments/public memory, not unpassed register junk.

The same proof passes in four code/data layouts, with the motion address,
bzero target and entry address explicitly rebased. Original storage aliases
and adjacent array bounds retain their retail relationships. Twelve GNU
links compare the complete 84-word slot across retail and both full-owner
padders, including low-half carry cases and independent code/data moves.
The non-generated owner has no flat assembly file: its alternate padder
layout fixture is independently reconstructed from both ROM slots and
checked against the production CSV inventory.

All **118 raw instruction/binding corruption controls** reject unknown input.
Raw payload SHA-256:
`49ca7bef582aee1c617ef230bef9a97ba6a54f28917b8213384cda86fd714d80`.
The normalizer also pins all **36 binding sites**, body length and frame.

## Guest, native and original-call evidence

Fresh pre-install and installed qualification compare retail, raw C and
normalized/padded C across **3,456 guest cases / three streams**. Every one
of the 82 instructions is visited. Checks include complete public memory,
both provider-entry snapshots, argument packets, preserved saved registers,
stack phases, signed coordinate boundaries and mutable provider effects.
The far-plane remains a live read after bzero. Guest packet-copy cases also
retain the previously tested signaling-NaN bit pattern; this is not a claim
about portable C/FCSR behavior for signaling NaNs.

Native32 executes the actual pointer-loop C body under **O0/O2/O3**, with
undefined-behavior traps enabled and **232 finite-input cases per profile**.
Correctly sized typed storage and endian-normalized snapshots cover all
**532 public bytes**, both provider-entry states and the final state. Five
compiled C controls fail in every profile: four record flags, unsigned
defaults, short scratch clear, early far-plane capture and wrong aspect.
The fixture's byte/halfword/word layout is checked at compile time.

Two native-fixture issues were diagnosed before acceptance. The SDK's native
Mtx alignment is four bytes, so the trailing guard region was sized from the
measured struct layout. GDB then located an O2 startup fault at a `movaps` in
the harness `_start`, with ESP misaligned for the assumed C entry convention.
Explicit entry-stack realignment fixes that harness boundary. Final O0/O2/O3
executions all pass; neither correction changes the recovered game C body.

The only original direct caller is `func_15007B3C` at **0x15008130**, ROM
**0x355E0**. Its literal two-instruction JAL/delay window passes **48 cases
through three streams**. A separate result-use proof follows four feasible
continuation paths, each **23..27 instructions**, into `func_1501CC3C` and
proves first V0 overwrite at **0x1501CC9C**, before any read of the old result.
Controls reject forwarding the old V0, removing its kill, and changing the
caller target. The aligned retail code census finds one JAL and no aligned
literal pointers to this function.

Another **16 connected cases / three streams** execute the original
**40-word bzero slot** (39 body words / one alignment word) on this aligned
192-byte destination and the original **23-word guPerspective wrapper slot**.
The wrapper forwards its stack/float
arguments to bounded providers at **0x15047F00** and **0x150A7790**, and its
temporary matrix is checked through the conversion boundary. A removed
original zero-store control fails the public-memory check. Complete parent
lifecycles, the inner SDK trigonometry/fixed-point conversion, hardware FCSR
and visual/gameplay acceptance are not claimed.

## Actual Make and strict production image

The independent three-command owner build uses the existing plain-C Make
recipe, pad_c_object and assembler. Production selects the same recipe.
Its ELF equals the independently predicted image exactly:

- **286 changed ELF bytes**, zero exclusions and no metadata permutations.
- All **6,051 function addresses** remain fixed. Only this routine's body
  and expected extent change from the old 12-byte stub to 328 bytes.
- Only `game_44A90.c.o` changes among **698 production objects**. Its changes
  are confined to `.text`, `.rel.text`, `.symtab` and `.strtab`; register info
  is unchanged and agrees with the independent assembler output.
- The one owner neighbor and normalized pools remain fixed. All **189,088
  protected data bytes / 720 owners** are unchanged.
- All **80 headers / 82 include inputs** are fixed. The audit preserves all
  **813 non-adoption inputs** from the 817-input production freeze, plus
  five separately frozen SDK/caller source and assembly inputs.
- Existing guard rows are unchanged; exactly **13 rows** for this function
  are appended. Conversion CSV bytes are identical to the baseline.

Production ELF SHA-256:
`eef1a0cb6545b7bbca22d0df382956bb06e142c98bf048ab7893492bc757fa54`.
Protected-data SHA-256:
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

Fresh full qualification passes **42.725 seconds** pre-install, **37.377
seconds** through the sibling overlay, and **36.384 seconds** installed.
Native checks are executed freshly in each suite. `make tools-check` passes;
the existing duplicate `generated_12D630` recipe warning remains.

The ignored sibling overlay contains ten task/dependency files. The actual
sibling tools checkout retains HEAD `ddbdd16b53ce60b054fb6e11bf0649a41f48375a`
and all **2,434 Windows-Git dirty paths** byte for byte. Before/after status
SHA-256 is `a3712de44f2fc37079df4a789a5015f134f6ab977a2c2da90a3fde1851606cd9`.
The installed scoped Graphify refresh extracts ten Python/C files, retains
all **61,402 previous node IDs**, and yields **61,432 nodes / 115,324 links**.
It is not a full-corpus extraction.

## Actual recount and resume boundary

Fresh actual-ELF recount: **4,499 / 5,514 total exact C functions (81.59%)**;
Game **3,826 / 4,841 (79.03%)**; Init **492 / 492**, Debugger **181 / 181**;
zero address drift and **1,015 different C functions**. Converted counts and
byte percentages are unchanged. **188** additional C matches reach 85% at
this denominator. The root README changes only its two exact-match rows.

Next ordinary C target: **`func_1504A140`**, quaternion-to-rotation-matrix
overlay in `generated_770F0.c`, **89 body words / three alignment words**.
Recover the component ordering and operation grouping, preserve translation
elements left untouched by retail, then qualify aliases, callers, floating
boundaries and complete owner/image gates before credit. The smaller custom
register/shared-entry routines still require separate assembly ownership audits.

The `64CBFDOGL` path contains only scratch `.codex` / `recomp_scene`
directories, without a host Git/CMake checkout. No host adoption is claimed;
the frozen Release is untouched. Artifacts remain in ignored
`conker/build/game-view-reset-15017640-private/`.

Tools commit: `245bbc9b62b8de14b8e422619cd7ae9580e34fae`.
Commit source, guards, documentation and the consumer pin afterward. No push
is performed; the wider 85% goal remains active.
