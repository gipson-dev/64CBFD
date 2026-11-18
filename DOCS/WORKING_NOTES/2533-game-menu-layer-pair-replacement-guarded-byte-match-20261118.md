# Menu layer pair replacement guarded byte match - 2026-11-18

`func_150B77A8` now replaces its zero-return placeholder with the complete
menu-layer replacement routine. Semantic C emits **93 words / 372 bytes** in
the original **0x60-byte frame**. **Six checked scheduling guards** move one
integer constant setup before five independent setup instructions. There are
no inserted/omitted words, frame changes, new compiler profiles or embedded
retail instruction ranges.

Fresh production recount: **4,543 / 5,514 total exact (82.39%)**, Game
**3,870 / 4,841 (79.94%)**, Init **492/492**, Debugger **181/181**. Drift is
zero and **971** converted functions remain different. Conversion inventory
and byte percentages are unchanged. **144 further matches** reach the active
85% target at this denominator. Root README refreshes its snapshot date and two aggregate
matching rows; function narratives remain in DOCS.

## Interface, descriptor and provider boundaries

Owner `conker/src/game/generated_E4070.c`; original `conker/asm/E4070.s:866`.
VA `0x150B77A8..0x150B791C`, ROM `0xE4C58..0xE4DCC`.
Baseline consumer `a11f6fc83cd3718e0ec6e62544c7ab173aa6d287`, tools
`e1c6d4fa0dbca7820e12e51b59c9103da7a86781`.
The recovered signature is **`void func_150B77A8(void)`**; its existing local
forward declaration is repaired accordingly. Its real menu dispatcher
ignores the result. No shared header or other source owner changes.

The shared `MenuRecordDescriptorE4070` remains **60 bytes**. Its first four
reserved bytes are identified as a second pointer, `secondaryAsset`, with
the remaining reserve starting at offset8. The complete owner qualification
proves this local type repair preserves all **20 other compact functions**,
their bindings and normalized pools. These are descriptive field names, not
claimed recovered debug names.

The descriptor has **44 initialized bytes** and **16 unwritten bytes** at
offsets8..19,26..27,58..59. Its literal guest home is **SP+0x24**, ending at
the incoming SP. Saved S0/RA occupy SP+0x18/+0x1C. The independent proof
compares all **112 private/incoming bytes** at every call and return.
Native checks credit only the44 defined descriptor bytes.

The routine performs the following ordered work:

1. If pointer slot1 at `D_800D9898+4` is nonnull, release it and clear that
   slot after the release. Provider writes to the remaining slots are live.
2. Initialize the descriptor with primary/secondary assets
   `D_800918F4` / `D_80091900`, position floats60/170, three zero shorts,
   signed short-2048, short9, scale shorts4096/4096, dimensions64/64 and
   bytes `(4,0,255,0,0,255,13,18,2,3)` at0x30..0x39.
3. Release nonnull slot4 at global+0x10, create a record from this descriptor,
   and store the returned pointer in slot4. Null allocation is retained as null.
4. Reuse the same descriptor, changing its asset to `D_800918E8`, two shorts
   to zero, dimensions to88/64, byte0x30 to0, and bytes0x36..0x38 to7/17/1.
   Every other byte inherits its current value, including helper mutations.
5. Reload slot8 at global+0x20, release it when nonnull, create the second
   record, store that result in slot8 and select command/state byte3.

The first constructor may retain and mutate the descriptor; the later
release can mutate it again after the second field updates. Those bytes must
reach the second constructor unchanged except for the specified C stores.
Reinitializing the whole descriptor or caching slot8 before earlier providers
would change behavior. Factory return values do not suppress the second
replacement or the final state update.

Current `func_15169968(void *)` and its `func_15169900` body independently
confirm pointer return and a60-byte descriptor copy into the new record.
Those source/assembly interfaces are frozen. The new routine's providers are
modeled in its focused tests; no full allocator/destructor/gameplay claim is made.

## Derived schedule and complete proof

Raw SHA-256:
`58a9993d4537b901f9dc31c0c2797b539015c012df2dd3963ae71ca663773242`.
The source differs only at words16..21. Retail moves the last word in that
block, `LUI AT,0x432A`, before five ADDIU instructions. AT is disjoint from
all five instructions' input/output registers. The block has no memory,
FP, call, branch or trapping-overflow operation, and preserves every GPR bit.
All87 other words are already literal matches.

The independent normalizer derives the rotation `[5,0,1,2,3,4]` from the
source stream and moves its two LO16 relocation identities with their words.
It checks the complete raw hash and binding map before normalization. The
retail assembler is an independent comparison, not the source of replacement
instruction ranges. The frame, every instruction opcode/operand, all private
homes, FP registers, FCSR transitions and helper order are otherwise fixed.

An instruction-driven proof covers all **eight complete paths**, all **93
words** on both sides, all112 private/incoming bytes, ordered public effects,
read epochs, call observations, saved registers and FCSR. Public stores and
providers invalidate read epochs; providers may arbitrarily mutate public
memory and the previously exposed60-byte descriptor. Unpassed locals and
implementation PCs remain outside the provider contract. This is normal
execution equivalence under mapped/aligned ordinary memory and private-stack
separation, not unrestricted interrupts or a whole-game hardware proof.

## Fresh qualification and production evidence

Eight maintained files use the `game_menu_layers_150b77a8` stem. Both final
tools configurations pass **six fresh tests**, without skips/errors:
**77.068s primary / 79.964s private sibling
overlay**. Each run fingerprints **334 observed imported tool files**.

- The complete owner uses its existing **O2/g3/no-unroll** profile and retained
  `jtbl_8009FD00_game` binding. A default-profile exploratory compile changes
  two unrelated loops; it is rejected as a production owner. Under the actual
  profile, the target raw stream is identical and all20 neighbors stay fixed.
- Both actual whole-owner padders match the retail target and preserve all20
  neighbors/pools. **12 independent GNU rebases** cover low16 values0,
  0x7FFC,0x8000,0xFFFC. **108** raw/binding corruptions and **48** real CSV
  expected/replacement/omission/relocation controls are rejected.
- Retail, raw C and normalized C each pass **256 guest cases**, covering all93
  words, every call argument, all60 descriptor bytes, public bytes and saved
  GPR/FPR/SP/RA. **171 exact memory-access prefixes** additionally compare
  registers, private/public memory, trace, PC and dispatched instruction for
  all three streams. This guest prefix claim is separate from the proof's
  FCSR model; the guest runner does not model hardware FP exception state.
- Native32 O0/O2/O3 each pass **256 cases** with strict aliasing and UBSan.
  Six effective semantic negatives reject a wrong cleared slot, secondary
  asset, dimension, lost inherited byte, final state and inverted release gate.
  Every negative uses the controlled failure exit, not arbitrary-crash credit.
- The original **52-word func_150B6BC0** and ten-entry retail table at
  **VA0x8009FD00 / ROM0x2447C0** are verified in ROM and ELF. Command8's entry
  targets the genuine call at **0x150B6C58**. **256 complete parent cases per
  stream** cover21 parent words, one invocation and return without redispatch.
  Other command paths retain their earlier qualification; they are not rerun.
- Both configurations independently build and link the prediction through
  three real Make-derived commands. Four full-image corruption controls reject
  undeclared data/code/symbol changes. The two predicted ELF files are identical.
- Actual production Make compiles only this owner, relinks and regenerates
  progress, with no prebuilt object copied. Its ELF exactly equals the prediction.
  The existing duplicate generated_12D630 recipe warning remains unchanged.
- The strict image audit accounts for **296 changed bytes**, including a closed
  two-name symbol/string permutation of `D_800918F4` and `D_800A31F4`, plus the
  target's symbol-size update. There are **zero exclusions**. All **6,050 other
  linked bodies**, all addresses, all **189,088 protected data bytes** and the
  conversion CSV stay fixed. Only one of the698 frozen objects changes.
- Installed-source compilation reproduces all21 compact functions. Fresh
  production/raw/normalized guest and parent checks pass. Unchanged native,
  proof/padder/rebase receipts are reused with explicit exact fixture hashes.
  Required tools checks and actual-ELF recount pass.

Production ELF SHA-256:
`91efc29db612dad4eca61c4850e34214c9710f8265f07ad0570a3e5d5448719d`.
The freeze contains **1,664 inputs**; exactly source, guard CSV, owner object
and ELF change. The actual sibling's **2,434 dirty paths** and343 scoped
dependency hashes are preserved. The private overlay uses339 exact sibling
files,366 pinned primary fallbacks and eight task files. Host Release, saves,
runtime sources and builds remain untouched. No Claude call is needed for
this routine qualification; no push is requested.

## Continuation

Graphify's native attempt and scoped AST update have separate receipts; all
prior IDs are retained and the manifest is linked to the installed function.
This is not a full-corpus re-extraction. Commit tools first, then source,
guards, aggregate README rows, this note/indexes and the consumer pin.

The private `func_151B118C` work also found
`scalar-homes-moveX100`: **187 words / frame0x98 /114 positional differences**,
with one retained blend-coefficient load. It is not installed or credited;
its new scalar qualifier still needs independent qualification. Keep Note2532
and its two fully tested drafts. `func_151B0B88` likewise remains unfinished.

Next inspect **`func_150B791C`**, the adjacent menu constructor, using the now
qualified descriptor layout/provider boundaries. Keep the full85% goal active;
this adoption contributes one match and leaves144 required.
