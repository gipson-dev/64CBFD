# Four menu record replacement guarded byte match - 2026-11-18

`func_150B791C` now replaces its zero-return placeholder with the complete
four-record menu routine. Semantic C emits **137 words / 548 bytes** in the
retail **0x60-byte frame**. **18 checked guards** normalize independent GPR
constant scheduling and three closed temporary-register roles. All three
original `TRUNC.W.S` operations remain, in order, with the original FP/FCSR
behavior. There are no inserted/omitted words or new compiler profiles.

Fresh actual-ELF recount: **4,544 / 5,514 total exact (82.41%)**, Game
**3,871 / 4,841 (79.96%)**, Init **492/492**, Debugger **181/181**.
Address drift is zero; **970** converted functions still differ. Conversion
counts and byte percentages are unchanged. **143 more matches** reach the
active 85% goal at this denominator. Root README changes only two aggregate
matching rows; all function details remain in DOCS.

## Interface and recovered descriptor

Owner `conker/src/game/generated_E4070.c`; assembly `conker/asm/E4070.s:965`.
VA `0x150B791C..0x150B7B40`, ROM `0xE4DCC..0xE4FF0`.
Baseline consumer `03b68b73d5118552647dee31ad46185cddc79a1e`, tools
`1ad9e120b616bbd6152485ccf5685bcf6bb56682`.

The recovered interface is **`void func_150B791C(void)`**. Its existing local
forward declaration is repaired; the genuine command10 caller ignores its
return. The local `MenuRecordDescriptorE4070` remains **60 bytes**. The reserve
at offsets8..19 becomes three signed words, `field08`, `field0C`, `field10`.
These offset-based names do not claim original debug names. No shared header
changes. The complete owner proves all20 other functions and pools unchanged.

The descriptor starts at SP+0x24, ends at the incoming SP and has **56 defined
bytes**. Bytes0x1A..0x1B and0x3A..0x3B are unwritten. Guest/proof checks compare
all60 seeded bytes, plus saved state; native C credits only56 defined bytes.
The proof compares all112 private/incoming bytes at every call and return.

## Complete ordered behavior

1. Release nonnull pointer slot2 at `D_800D9898+8`, then clear that slot.
2. Build a descriptor with asset `D_8009190C`, null secondary asset, words
   0/150/0, floats230/150, three zero shorts, two other zero shorts,
   scale4096/4096, dimensions64/16 and bytes
   `(5,3,255,0,0,128,7,17,1,0)` at0x30..0x39. Its Y-word conversion is
   deliberately early to recover retail's register allocation.
3. Release nonnull slot5, create a record and store its result in slot5.
4. Change half0x16/word0x08 to256, alpha byte0x35 to255, floatY to170 and
   word0x0C to the truncated Y. If slot6 is nonnull, release **the first
   created result in slot5**, then create/store slot6.
5. Change that half/word to512, alpha to128, floatY to190 and truncated Y
   to190. If slot7 is nonnull, release **the then-current slot5 pointer**,
   then create/store slot7. A provider may have retargeted slot5 by now.
6. Reuse the descriptor for asset `D_800918E8`: clear shorts0x14/16/18 and
   byte0x31, set dimensions88/64, alpha255, byte0x30=0 and floats230/170.
   Words0x08/0x0C/0x10 inherit their current values and provider mutations.
   Release nonnull slot9, create/store slot9 and select state byte3.

The mismatched gates/release targets are observed retail behavior and are
commented explicitly in C. A null first allocation and nonnull slot6 can
produce a release of NULL. Tests record this argument; they do not claim the
real destructor safely handles it. Constructors/releases can retain and
mutate the descriptor and public slots. Blanket initialization, cached later
slots or replacing the unusual release argument would change behavior.
The existing `func_15169968`/`func_15169900` factory and60-byte copy interface
remain frozen. Provider services are modeled, without whole-allocator,
destructor, gameplay or host-runtime acceptance claims.

## Derived normalization and proof

Raw target SHA-256:
`6affbd52b7184702fe13f46893aa6be9b8ece1e1c99d72a5bcf0907c77c2b954`.
The independent normalizer permutes source words14..19 as
`[19,15,14,16,17,18]`, retaining the conversion at15. Only a GPR-only LUI
moves across that conversion; no FP operand/result or FCSR access is added,
removed or reordered. It then applies three closed temporary GPR mappings:
words21..57 (9->10,10->8,8->9),69..77 (10->12,12->11,11->10) and88..96
(24->8,8->25,25->24). Each used role is defined before use, and the complete
call transfer proof closes its lifetime. ABI argument/saved/SP/RA roles stay
fixed. Two changed words retain the original asset HI16/LO16 bindings.

Normalization derives from the raw compiler stream and exact binding map;
the independently assembled original is a comparison, not a source of copied
replacement instruction ranges. All137 normalized words equal retail.
An instruction-driven proof covers **32 complete paths**, all137 words on
both sides, ordered public effects, all112 private/incoming bytes, arbitrary
retained-descriptor/public mutations, saved registers and all **three ordered
FP/FCSR conversions**. Eight transfer negatives are rejected. Its contract
assumes ordinary mapped/aligned memory and private-stack separation; it does
not qualify unrestricted interrupts or arbitrary implementation-PC inspection.

## Fresh qualification and linked production audit

Eight maintained files use the `game_menu_four_records_150b791c` stem. Both
tools configurations pass **six fresh tests**, no skips/errors:
**90.574s primary / 97.699s private sibling overlay**.
Each run fingerprints **336 imported tool files**.

- Full-owner compilation uses the existing O2/g3/no-unroll profile and
  `jtbl_8009FD00_game` binding. All20 compact neighbors and pools stay fixed.
- Both real padders match the target and preserve its20 padded neighbors.
  **12 independent GNU rebases**, **154 raw/binding corruptions** and
  **116 CSV expected/replacement/omission/relocation controls** pass/reject
  as intended. Guard rows are18; two have relocation identities.
- Retail, raw and normalized streams each pass **800 guest cases**, covering
  all137 words, every release/create, all60 descriptor bytes, public bytes and
  saved GPR/FPR/SP/RA. Cases cover32 presence masks, five allocation-failure
  masks and five provider-mutation masks. Null release arguments are observed
  440 times per stream. Raw full-register fault-prefix equality and hardware
  FP-exception acceptance are not claimed by the concrete guest runner.
- Native32 O0/O2/O3 each pass800 cases with strict aliasing, no-fast-math and
  UBSan. Eight controlled semantic negatives reject wrong clear/release
  targets, coordinate/asset/alpha, lost inherited word and final state.
- The complete original **52-word func_150B6BC0** and ten-entry retail table
  at **VA0x8009FD00 / ROM0x2447C0** are verified in ROM/ELF. Command10's
  index9 selects its genuine call at **0x150B6C78**. Each stream passes800
  complete parent cases, covering20 parent words, one call and return without
  redispatch. Other command paths retain earlier receipts and are not rerun.
- Each configuration predicts the image with three real Make-derived commands
  and four whole-image corruption controls. The predicted ELF files agree.
- Actual production Make compiles only this owner, relinks and regenerates
  progress. No prebuilt object is copied. The resulting ELF equals the
  independent prediction. The duplicate generated_12D630 recipe warning is
  pre-existing and unchanged.
- Strict audit accounts for **459 changed bytes**,
  including closed symbol/string permutations for D_8003B6A0/D_80097C08 and
  D_8009190C/D_8002C780, plus target-size metadata, with **zero exclusions**.
  All **6,050 other linked bodies**, all addresses and all **189,088 protected
  data bytes** remain fixed. Only one of698 frozen objects changes; the
  conversion CSV and guard-history prefix remain unchanged.
- Fresh installed-source compilation reproduces all21 compact functions.
  Production/raw/normalized guest and dispatcher checks pass again. Unchanged
  proof/padder/rebase/native receipts are explicitly reused by exact fixture
  fingerprints. Required tools checks and actual-ELF recount pass.

Production ELF SHA-256:
`c9792766e47fe0b99a004e58eefd964f21b82bee9de533677a24cdfd7b0d22da`.
The freeze holds **1672 inputs**; exactly source, guard CSV,
owner object and ELF change. The sibling's2,434 dirty paths and343 dependency
hashes are preserved. Its private overlay uses339 exact sibling files,
374 pinned primary fallbacks and eight task files. Host Release, saves and
runtime builds are unchanged. No Claude call or push is needed.

## Continuation

Graphify's native attempt and scoped AST merge have separate receipts. All
prior IDs are retained and an explicit manifest/function edge is recorded;
this is not full-corpus re-extraction. Commit tools first, then the consumer.

Next inspect **`func_150B7B40`**, the adjacent unfinished menu routine, with
the recovered descriptor/provider/caller boundaries. The private motion
drafts from Note2532 and pool draft from Note2531 remain uninstalled and
uncredited. Keep the full85% goal active: this adoption adds one match and
leaves143 required.
