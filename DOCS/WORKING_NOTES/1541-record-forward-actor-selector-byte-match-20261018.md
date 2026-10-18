# Forward Record Actor Selector Byte Match

Date: 2026-10-18. Consumer predecessor **8e517bbc**, tools predecessor
**3f4b1c9**. Tools committed first as **77d9c40**. Restore **func_150883B0**,
owner `generated_B3020`, VA **0x150883B0..0x1508855C**, ROM
**0xB5860..0xB5A0C**. This completes one function, not the wider Game goal.

## Semantic Recovery

Replace the zero-return stub with **u8 *(s32 recordIndex,s32 direction,
f32 *outValue,s32 *outTag)**. The retained retail caller establishes all four
word arguments, the two output addresses and pointer consumption. Preserve
the address-based symbol and a short semantic source comment. No shared
header or caller edit is needed.

Null D_800872A0 returns null without output writes. Otherwise derive the own
0x84-byte record and signed actor ID byte+0x31. Actors are in the absolute
D_800CC2D0 array with stride0x32C, not a loaded global array pointer. Direction
>=0 uses -1.0f, direction<0 uses +1.0f. Multiply own float fields+0xC/+0x10
by that sign. Cache the signed own tag+0x2F, source actor X/Z+0x14/+0x1C and
excluded ID `(s8)(sourceActor[0x124]-1)`. The direction input is dead after
the sign choice; the C reuses it for the cached tag. Bias is the negated
ordered binary32 sum of the two source-coordinate products. Initial distance
limit is D_8009DA00 (10000.0f, bits0x461C4000).

Scan the signed D_800D2398 count. Reload the table pointer for each row. Skip
the excluded signed actor ID. Own tag0 is a wildcard; otherwise require equal
signed candidate tag. Project candidate X/Z with the same ordered two
products, sum and bias addition. Accept only **0.0f < distance < minimum**;
strict ties retain the first candidate. Quiet unordered comparisons reject
candidates, rather than being rewritten as logically negated predicates.

On acceptance, update the distance minimum, load candidate float+0 and write
**outValue first**. Reload the candidate signed tag and store its full signed
word through **outTag second**. Only then reload the selected actor ID and
signed count. The return pointer uses that freshly read ID. The compiler
caches the count between accepted stores; it does not reload on every skipped
row. No match/nonpositive count leaves both outputs untouched.

The ID/count reloads and iteration table reload are observable when guest
output addresses alias record/global bytes. Such guest byte-address behavior
is qualified separately from native C with valid aligned typed nonalias
objects. Do not claim arbitrary float/word aliasing or negative actor pointers
are portable C object accesses. Narrowing and signed-byte address arithmetic
follow the measured o32/IDO ABI; no native invalid-pointer claim is made.

## Bounded Normalization

Existing O2/g3/MIPS2/o32 and compiler-only no-unroll profile emits the correct
**107 words/frame0x20**, including S0/S1 and 64-bit F20/F22 spill pairs, with
37 register/address word differences. **Thirty-seven relocation-aware guards**
normalize these differences. This is not a direct/guard-free C match.

Words26..99 normalize raw roles T4/T5 (actor stride/base), T2 (count), A2
(actor pointer), T0 (excluded byte), T1 (iteration) and A0 (byte offset) to
retail T5/T4, T1, A0, A2, T0 and T2. Their input lifetimes have ended before
these new roles start. Words58..96 separately exchange the loop row/ID V0/V1
roles; own-record V1 dies before this region, and the final V0 return is not
renamed. At words39/69/95, exchange the two ADDU source fields to preserve
retail's commutative actor-address operand order.

All ten HI16/LO16 bindings retain their offsets, identities and values,
including register-adjusted relocation-bearing words. All FPR fields and
floating operations remain fixed. No scheduling permutation, branch opcode/
displacement/delay change, memory operation/order, literal, instruction
insertion/omission, assembly fallback, Makefile or profile change. Raw dead
GPR scratch values are not asserted identical at interruption; normalized
and retail complete bounded states are identical.

## Qualification

New tools: `experiments/game_record_forward_selector.py` and
`tests/test_game_record_forward_selector.py`. Ignored build artifacts:
`conker/build/game-record-forward-selector/`. Fifteen pinned hashes cover
owner/ELF/guard/ROM/assembly, Makefile/symbol/header inputs, four prepared IDO
components and the original/production caller files. This is the declared
input closure, not every unlisted transitive dependency. Historical views
are exact, serial and non-nesting; no prior fixtures/checks are weakened.

All **seven pre-install tests pass in75.854s** and all **seven installed tests
pass in76.827s**:

```sh
python3 -m unittest tools.tests.test_game_record_forward_selector -v
```

- **1,040 three-way raw/normalized/retail guest cases** cover all256 count
  bytes, signs and word direction boundaries, wildcard/signed tags, own
  indices0/3/127, null/no-match/tie/10000-limit/quiet-NaN/Inf/signed-zero
  profiles, both stack phases and eight output-alias patterns. Seventy-two
  additional combinations exercise signed actor ID -128/-1/0/127, excluded
  byte wrap and output bit preservation. The 72 cases are included in1,040.
  All107 words execute. Compare every public memory byte, exact interleaved
  read/write traces, pointer result, saved GPRs and all saved FPR bits.
- **5,328 native32 cases per O2/O0 profile**, UBSan traps, SSE float32 and
  contraction disabled, pass with real aligned Record/Actor fields. Python's
  independent address/bit reference supplies expected pointer/output rows.
  Compare all bytes of both complete objects and unchanged globals. Native
  cases have nonnegative in-range actor IDs and distinct output objects.
- Twelve guest negative controls produce actual public result differences:
  unsigned count, direction boundary, exclusion, tag, stride, strict zero,
  strict ties, normal field, cached selected ID/count/table and swapped
  output stores. Crashes/unmapped reads alone are not accepted. Six controls
  also exit explicitly with wrong-result status23 natively; alias, stride
  and extra exclusion probes remain guest-only.
- **Nine independent original/raw/padded links** at three placements pass
  **270 three-way rebased cases**. Exercise HI16/LO16 carry boundaries for
  all ten bindings, aliases, signed IDs and saved-register state.
- **740 access-fault prefixes across30 states** preserve public memory and
  trace prefixes for all three bodies; normalized/retail complete state
  agrees. All107 raw-word mutations, ten binding mutations, 37 guard
  expectations, 30 live/frozen input mutations and nested views fail closed.

The first fixture pass exposed an alternate table placed at the oracle stack
address, causing stack-filtered reads, and a caller fixture that overwrote
the source actor's exclusion byte. Move only the fixture's alternate bank
and use an independent caller actor for the bounded continuation. Neither
recovered body nor first prediction changes. No hardware MMU/FCSR, signaling
NaN payload/exception, flush mode or complete gameplay equivalence is claimed.

## Observed Caller

One aligned exact retail JAL to this target is at **VA0x150539F0 /
ROM0x80EA0**, in **func_150538CC**, owner `game_77AD0`. No exact target pointer
or J word was found; computed/encoded references are not excluded. The
production caller uses GLOBAL_ASM, not a zero-return C placeholder, and its
entire **4,108-byte** slot **0x150538CC..0x150548D8** equals retail.

**36 paired bounded caller windows** execute the actual setup at0x150539E0:
load index/direction from parent SP+0xDC/+0xC0, form float/tag output addresses
SP+0xC4/+0xBC, JAL with F16 store atSP+0xCC in the delay slot, run the complete
raw/normalized selector, reload F16, consume V0 into V1 and execute the real
post-call BEQ and ADDIU delay. A clearly synthetic exit begins0x15053A0C;
other parent branches/helpers and whole-parent gameplay are not executed.

## First Prediction And Installation

Before production edits, freeze first complete **3,257,636-byte ELF**, owner
source and guards using only the new padded owner in a copied link script.
Install with the existing scoped build:

```sh
make -C conker -o Makefile -o retail_word_patches.us.csv -j4 \
    build/src/game/generated_B3020.c.o build/conker.us.elf progress.csv
make -C conker -o Makefile -o retail_word_patches.us.csv match-progress NON_MATCHING=1
```

Actual whole ELF equals the first prediction, with **zero metadata
exclusions**: **330 changed bytes =312 target-code +nine symbol-table +nine
string-table encoding bytes**. Canonical symbol definitions change only
target extent12->428; metadata encoding changes do not alter other definitions.
Audit all **6,057 bodies/addresses**: only this function body changes, with
all addresses fixed. All **72 raw owner neighbors**, pools and relative
bindings are fixed; actual padded owner equals qualification. Preserve every
old guard prefix byte and append exactly37 rows. A mechanical formatting
pass changes only those new rows' LF terminators to predicted CRLF, verifying
the old prefix and exact successor hash first. No broad newline rewrite.
The Makefile remains fixed, Game data stays **189,088 bytes /720 owners /
zero differences**, and the pre-existing duplicate12D630 recipe warning is
unchanged. No new compiler diagnostic.

| Artifact | SHA-256 |
| --- | --- |
| Raw target | d1222b5cfa28fa22a0982acda75f77034daf94e5a1cdc328fcd733a74fe0a76f |
| Whole ELF | 963b19f2f16d695e93aa85ac2b1a8aaaff08f865f3af843c0f0e736d43a806d4 |
| Owner source | 478b47b1e70f3b49c9b45f8b2d5dd1a9e22570ac871e71f03318a64d553ebcb8 |
| Guards | dcdd24364339be141dc68c91756fb2450414e06b736d863109a81f80628b2a35 |
| Unchanged Makefile | 840897f11d9fea8109c4e67c57e927efa6e1686de2b399fec2c9025828b92d49 |

Shared padder/PC16 tests pass **11 per copy**, both tool smoke checks and root
tools-check pass. Four new copies parse as ASCII/Python AST; both pairs are
byte-identical. The intentionally dirty standalone mirror remains at
ddbdd16b53ce60b054fb6e11bf0649a41f48375a: all **1,208** prior dirty hashes
remain unchanged, adding only two absent task paths for **1,210** total.
No mirror commit/reset, push, host build/launch or frozen Release action.

Fresh matching totals: **Game2,979/4,828 (61.70%)**, **total3,652/5,501
(66.39%)**, Init492/492, Debugger181/181, **1,849 different /zero drift**.
Conversion counts/bytes are unchanged because the old false C stub was already
counted converted. Root README changes only its two aggregate matching rows.

## Next Work

Continue with **func_150888A8**, **88 words/frame8**, still a false C stub.
Retail ROM0xB5D58..0xB5EB8 corresponds to VA0x150888A8..0x15088A08. Audit
three narrowed arguments and seven aligned JALs at ROM0xB4674/B4688/B46D4/
B52C4/B52DC/B5F28/B5F84 before choosing types. Recover five neighbor IDs at
record+9..+0xD in the D_800D2350 0x10-byte table, candidate flag/type filtering
at+0xE/+0xF, sentinel0xFF and exact priority/last-selection rules. Preserve
saved S0, byte reads from argument home slots, the first-item peel plus
two-at-a-time loop and branch delays. Do not assume caller parents are C.
The intervening `func_1508855C` already equals all36 retail words; no new
credit is assigned. Retained150885EC/1508868C, command-parent stubs,
handwritten150A76F0, fade gaps and other wider queues remain open.

The active Game matching goal remains active. Scoped Graphify refresh reports
**42,489 nodes /82,558 links /4,009 communities**, preserving **19,398 nodes
from2,972 excluded-but-existing files**. Only three line-disambiguated old
UPDATE_LOG heading IDs shift; their labels and all other old IDs remain.
The new note contributes eight nodes. Target/next definitions resolve to
**L439/L574**. Preserve the original graph in the ignored task build folder;
graph outputs stay ignored. Do not full-scan away excluded existing nodes.
