# 2489 - Randomized short-packet callback and byte match

`func_151A0C0C` now matches all **141 words / frame 0x80**. Complete typed C
replaces its zero-return placeholder with the original 56-byte particle request:
randomized heading, velocity and sizes, selected template, colour and fractional
coordinates, then submission through the shared short-packet provider.
The original symbol is retained with a descriptive comment and recovered ABI.

Actual production recount: **4,514 / 5,514 (81.86%)**, Game
**3,841 / 4,841 (79.34%)**, zero drift and **1,000** still different.
Init remains **492 / 492** and Debugger **181 / 181** exact. Conversion totals
remain **5,514 / 6,048 (91.17%)**, **86.19%** bytes. **173 more** verified matches
reach the unchanged **85%** goal (4,687 required); it remains active.

## Source and interface recovery

The callback takes 15 o32 arguments: integer discriminator/ordinal, x/y/z float
payloads in arguments 2-4, unused origin coordinates 5-7, heading 8, unused start 9
and radius 10, full-word style 11, unused intensity 12/user 13 and unsigned mode 14.
The first two integer arguments keep x/y in A2/A3, rather than F12/F14.
It returns 1 after the submission. Explicit packet types preserve all offsets.

Four integer RNG calls retain **unsigned** modulo15/41/3/451; four u8 sine
queries and one float RNG call retain their order. Speed uses the original
immutable 503.0f/801.0f constants D_800A8D14/D_800A8D18. Referring to those
constants preserves the owner's existing 16-byte literal pool, including the
previous renderer's epsilon, rather than appending duplicate constants.

All three fractional coordinate bytes intentionally use x*256.0f. The source
makes the retail conversion explicit as float -> s32 -> s8; a direct out-of-
range float-to-byte cast fails the native sanitizer control. Fourteen packet
bytes remain unwritten, including the template word when style is neither 0
nor 1. The guest/proof preserve those incoming bytes. Native tests cover valid
template styles 0/1 and compare 42 defined bytes plus actual pointer identity;
they do not fix 14 unspecified representation bytes.

Declaration ordering restores angle at incoming-SP -58 and the four live
float homes at -64/-68/-72/-76. The exposed packet remains incoming-SP -56;
saved RA is -100, frame 128. All 38 owner neighbors and pools remain fixed.

## Whole-function relation and normalization

The selected compiler output is **140 words / frame 0x80**, with 52 positional
differences including one missing word. Its **three symbolic paths** cover all
140 raw and 141 retail reachable instructions. The instruction-driven relation
compares every helper argument/order, the complete 56-byte submission, ordered
FP opcode/operand/FCSR effects, saved registers, return value and saved-RA custody.
An independent scratch-register allocation passes. Eight effective corruptions
reject wrong unsigned divisor, magnitude, speed literal, x source, store width,
angle home, saved-return home and initialization of an unwritten packet byte.

The normalization retains **every one of the 140 compiler operations once**.
It changes only qualified GPR operand fields, branch targets and scheduling,
then adds one split-result copy. The size producer at source offset 0x16C is
scheduled at retail 0x158; retail copies T0 to A1 at 0x168 before T0 is reused.
Both original size consumers at packet offsets 0x24/0x26 use that preserved
value. Source and projected def/use checks reject an intervening kill. FP
arithmetic words and branch opcodes are unchanged; MFC1 GPR destinations may be
renamed. No source operation is omitted, and no
wholesale retail-body replacement is used.

**140 expected-word/relocation guards** emit that schedule, with one inserted
copy after input slot 0x164 and zero omissions. All 140 word corruptions and 20
changed binding maps fail closed (**160 controls**). Both owner padders match
all 141 words and preserve all 38 neighbors/pools. Three independent rebases
also pass the whole relation and both padded outputs, including coefficient
HI16 carries at800AFFFC/800B0000 and80117FFC/80118000.

The relation assumes mapped ordinary RAM, immutable literals/code, stable
unpassed argument/private homes and no public alias of private frame storage.
Opaque o32 providers may mutate public RAM/FCSR, caller registers and their
outgoing argument homes. The submission sees all56 bytes and may mutate the
escaped packet. Stable ordinary reads may commute across FP operations while
FP/FCSR order stays exact. This is not raw fault-PC/register, portable-C
undefined-input, full provider-implementation or hardware/gameplay acceptance.

## Original callers and fresh validation

The aligned ROM census finds one callback pointer at ROM 0x22F4D0, corresponding
to D_8008AA00[4] / VA8008AA10, and no direct JAL/J instructions to this target.
All four table-referencing dispatchers are exercised:

| Dispatcher | Fixture words | Current production state |
| --- | ---: | --- |
| func_1514C2F0 | 96 | Byte-exact recovered C |
| func_1514C470 | 130 | Still a zero-return stub; retail instructions used only in fixture |
| func_1514C678 | 120 | Byte-exact retained assembly |
| func_1514C858 | 138 | Still a zero-return stub; fixture includes 135 body plus 3 alignment words |

Earlier private notes had identified only the first two; the fail-closed census
found the other two before adoption. These are bounded parent executions,
not all-input proofs of the parent routines. RNG/sine/submission remain opaque
providers, with complete arguments and packet observations at their boundary.
No production credit or restoration is claimed for the two parent stubs.

Primary preinstall, sibling overlay and production-installed suites each pass
**four qualification tests**. Elapsed times including startup: **118.092 s**,
**124.821 s** and **130.512 s**, respectively. Each run freshly compiles the
complete owner, selected source and prior recovery; checks 320 guest cases per
four streams, **512 native32 cases across six compiler/alias profiles** (3,072
executions), UBSan/float-conversion traps and four source controls; and executes
**1,024 caller cases / 1,472 callbacks per stream** across all four parents.
Both padders, rebases, corruption controls and symbolic proof are also fresh.
`make tools-check` passes separately. Zero Claude calls were needed.

After the runs, two report keywords were clarified from
`production_inputs_unchanged` to `production_state_matches_audited_inputs`.
Exact source replacement and normalized AST comparison prove that only those
JSON keyword names changed. All original receipts/hashes are retained, with
explicit schema-only derived reports; no repeated broad run is claimed for
that terminology correction. Compiler C, guards and all functional checker
logic are unchanged. This distinguishes 886 audited input rows from the 882
actually unchanged rows after adoption.

## Production image and preservation

Isolated actual Make and the real production Make compile this semantic owner,
apply the new CSV rows and link. `-o retail_word_patches.us.csv -o Makefile`
avoids rebuilding unrelated objects solely for the global CSV timestamp;
the changed owner's recipe still reads the real CSV. No prebuilt object is
substituted. The existing duplicate generated_12D630 recipe warnings remain.

The production ELF exactly equals the independently predicted image. All
**630 changed bytes** are accounted for with **zero exclusions**: target
instructions/size and four explicitly closed GNU symbol/string permutations,
with equal named definitions. All **6,050 other functions/addresses**, 697
other objects and 38 owner neighbors stay fixed. All **189,088 protected data
bytes** remain exact. Of the immutable 886 inputs, only C/CSV/owner object/ELF
change; 882 stay fixed. Existing guard bytes and progress language rows are
unchanged. The preceding renderer remains 632 words exact in this linked audit;
its previous unchanged semantic receipts are reused, not rerun. Its old
whole-owner fingerprint fixture is historical after this subsequent owner change.

The sibling Tools HEAD ddbdd16b53ce60b054fb6e11bf0649a41f48375a and all 2,434 dirty
paths remain unchanged under the seven-file overlay. No host-port source/build,
Release artifact or save is changed. Native32 uses the existing freestanding
compiler fixture; no package installation or account/provider changes occurred.

Production ELF SHA-256:
`7c7e434c3e4e3e805094513bb5deb44b44f7611eb67623b4f1d134c503cceb7f`.
Protected data SHA-256:
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.
Raw 140-word source SHA-256:
`06b4d5ef32108ce47cd693d1abd1a705f4795c08e242510f2264371cc5bbdcba`.
Receipts: `conker/build/game-randomized-short-packet-151a0c0c-private/proof-2489/`.
The 886-input baseline remains immutable; four audited adoption overrides are
recorded separately. Graphify native update refused a shrinking replacement;
scoped AST refresh retains old IDs, with hook retention checked before banking.
No force, upgrade, full-corpus re-extraction, emulator or gameplay claim.

```sh
python3 -m unittest tools.tests.test_game_randomized_short_packet_151a0c0c_match -v
make tools-check
make -C conker match-progress NON_MATCHING=1
```

Next: `func_151A1010`, the next unmatched owner stub, 111 words / frame 0x78.
Qualify its complete body and callers before any new installation or credit.
