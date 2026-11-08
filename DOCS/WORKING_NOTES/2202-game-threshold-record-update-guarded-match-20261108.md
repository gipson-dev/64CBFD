# Threshold Record Update Guarded Match - 2026-11-08

`func_151A24A8` replaces its false zero-return placeholder with the complete
**78-word / 312-byte**, frame-free effect callback. Its semantic C preserves
six ordered lifetime gates, live wrapped growth, a callback/colour transition,
and the original one-shot sentinel. **33 expected-word guards** derive the
retail schedule and temporary register allocation; this is a guarded match.

Production: Total **4,271 / 5,513 (77.47%)**, Game **3,598 / 4,840 (74.34%)**,
Init **492 / 492**, Debugger **181 / 181**, zero address drift. **1,242**
converted functions remain different. **140** more exact functions reach
4,411 / 5,513 and the active 80% goal. Conversion rows are unchanged.

## Retail behavior and callback contract

Source `conker/src/game/generated_1CC440.c`, original `asm/1CC440.s`.
VA **151A24A8..151A25E0**, ROM **1CF958..1CFA90**. Reuse the nearby,
already-qualified lifetime callbacks from Notes 1713 and 2089, plus their
MIPS/native32, caller-window and independent-link helpers.

```c
void func_151A24A8(u8 *effect);
```

The record is writable and word-aligned. The signed lifetime is the halfword
at +0x38, and fourteen signed halfword parameters begin at +0x50. All six
comparisons are strict and independent; a later active gate can override an
earlier result:

1. Parameter2 < lifetime: store the low byte of
   parameter0 * (parameter1 - lifetime) at +0x3F.
2. Parameter5 < lifetime: store the low halfword of
   parameter3 * (parameter4 - lifetime), at +0x36 then +0x34.
3. Lifetime < parameter8: overwrite +0x3F with parameter9 * lifetime's low byte.
4. Lifetime < parameter10: multiply parameter11 by the **live** 32-bit timestep
   `D_800BE9E4`; read both signed size halfwords, add the same low-word delta,
   store +0x34 then +0x36, and reload the lifetime. The unsigned increment
   expresses the original wrapped product/additions without signed C overflow.
5. Lifetime < parameter6: read unsigned flags at +0x44; set callback selector
   +0x2F to 0x13; OR flags with 0x101; compute parameter7 * lifetime; store
   word 0x00520003 at +0x14, then its colour byte at +0x42, +0x41 and +0x40.
   Slot 0x13 is the already-banked `func_151A25E0` in the authentic registry.
6. Lifetime < parameter12: copy parameter13 to +0x32, then replace parameter12
   with **-9999**. Lifetimes below -9999 can trigger this again; do not clamp.

The sole aligned pointer is ROM **2314D0**, VA **8008CA10**,
`D_8008C9C8[18]`, in the original 22-entry table. An aligned full-ROM census
finds no direct J/JAL entry or interior references. The two real dispatcher
windows pass only A0 and ignore the return register:

- `func_15167E0C`: VA15167E80..15167EC4, 17 words, selector +0x2F,
  observed post-callback halfword +0x38, parent frame0x20.
- `func_15168870`: VA151689D4..15168A08, 13 words, selector +0xB2,
  observed post-callback halfword +0x98, parent frame0x18.

These windows skip signed -1 and NULL entries, preserve the owner/home,
invoke the selected callback, then reload the observed halfword. The emitted
routine's incidental V0 table pointer is preserved without inventing a C
return-value contract. Complete parents and other callbacks remain outside
this bounded qualification.

## Compiler and normalization provenance

The private first draft was 78 words with 39 differences. An ordinary local
colour value gives the selected 78-word stream with **33** differing words;
no volatile declaration, inline assembly, extra profile or instruction
insertion is used. Retail O2/g3, MIPS2/O32 and the existing GLOBAL_ASM owner
recipe remain unchanged. There are no compiler diagnostics.

The normalization pins the complete raw stream and two original relocation
identities (HI16 at +0x68, LO16 at +0xA0 for `D_800BE9E4`). It derives:

- Fifteen temporary-GPR lifetimes, each bounded from definition to last use.
- The independent lifetime LH at +0xB0 moving after MFLO, two ADDUs and the
  disjoint +0x34/+0x36 stores, to +0xC4. Its +0x38 address cannot overlap them.
- Swapped commutative MULTU operands at +0x7C and +0xF8.

Every branch, opcode, arithmetic association, memory offset, public store
order and relocation identity is retained. No instructions are inserted or
omitted. After binding, all 78 normalized words equal retail. All 312 one-byte
raw corruptions, malformed relocation maps, three changed guard expectations
and whole-image corruptions are rejected. Raw private scratch registers and
fault PCs are not equated with retail; fitted/retail literal state is checked.

## Validation evidence and limits

Eight focused checks pass before and after installation, using mounted tools
and a read-only overlay for the sibling tools checkout:

- **6,912 cases per body** compare retail, raw C and fitted C against an
  independent byte-memory model. Signed lifetime boundaries, all 64 feasible
  gate masks and all 78 visited retail words are covered.
- **1,120 alias cases per body**, with 28 word-aligned timestep placements,
  plus 18 repeated sentinel updates. Earlier writes may change a global that
  overlaps the record; an early global load is therefore incorrect.
- Native32 O0/O2/O3, trap UBSan, defined wrapping and canaries: **65,536 direct
  plus 65,536 typed table-callback cases per profile**. All 16 semantic controls
  are effective. Guest-compiled controls add a live-alias/unmapped-global
  counterexample for early timestep loading. Global aliases are guest-only.
- **1,104 caller cases per body** exercise both original windows, all 22 real
  slots, NULL and -1, post-callback reloads and owner homes. Other callbacks
  use bounded providers; full-parent/gameplay correctness is not claimed.
- **730 fired fault prefixes** compare complete retail/fitted private state;
  the inactive timestep global may be unmapped. These qualify emitted MIPS
  access order, not portable C fault behavior.
- **Nine GNU links /36 rebased cases per body** independently bind original,
  raw and padded objects, including HI/LO sign-carry edges and timestep aliases.

The complete owner has 39 functions. Isolated/owner words and relocations
agree; all 38 raw and padded neighbours, pools and register-union metadata
are checked. Both padders and the actual **five-command Make recipe** agree.
The strict independent whole-ELF prediction changes **227 bytes**, with zero
exclusions or symbol metadata permutations. All 6,052 disassembled function
entries keep their addresses; only this target body and extent change.
All 720 protected data owners /189,088 bytes remain exact. Existing guard rows
are a literal prefix;33 rows are appended for this function only.

Production object/ELF equal the prediction, and the authoritative linked
recount yields the totals above. The existing whole-ROM checksum mismatch
still makes `make all` exit 2; target build/link/progress and recount pass.
The inherited duplicate generated_12D630 Make warning is unchanged.
Fresh shared tool smoke passes in both copies; three unchanged regressions
per copy are reused by exact helper/test fingerprints, not called fresh.

## Bank and next boundary

Receipts: `conker/build/game-threshold-record-update-151A24A8-match/`.
Original assembly, ROM, build profiles, shared headers, conversion CSV and
unrelated work are preserved. The sibling tools checkout retains its 2,434
inherited dirty paths unchanged. Host Release stays frozen.

Next: **func_151B5E94**, owner `generated_1E30A0`, the next78-word unmatched
Game routine in the measured queue. It remains uncredited; inspect the
complete original body, ABI/callers and profile before drafting or installing.
Tools commit before the consumer pin. The scoped Graphify refresh retains
existing unscanned nodes with evidence; it is not a full-corpus extraction.
The 80% goal remains active.

Production ELF SHA-256: `28d2e33ba736b8a0be461b480b3f1ca690fb6f4e9ac9be6a276f8d5313b45b50`.

Production guard SHA-256: `91532bffe1fe4ec3981ec41d5a7bd63ede1a02a78b2bdf4b36d67b067aecd770`.

Raw C SHA-256: `38d47ae9ecd65e51e057d858c178b18c0e8cb38bda2c6519b8ae6586151dd688`.
