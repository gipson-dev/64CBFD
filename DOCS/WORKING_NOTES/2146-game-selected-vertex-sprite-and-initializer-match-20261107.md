# Selected-position sprite and vertex initializer matched

Date: 2026-11-07. Continues [Note 2145](2145-game-damped-record-lifetime-direct-match-20261107.md)
from consumer `1c1500b3bc6c98916f9931700de16c23380c39af` and tools
`5927272198259f2d55c6dd28bf213bde78924339`, toward the active 80% goal.

## Two complete recoveries

| Routine | Owner | VA / ROM | Words / frame | Expected-word guards |
| --- | --- | --- | ---: | ---: |
| func_1518C57C | generated_1B8F40 | 1518C57C..1518C69C / 1B9A2C..1B9B4C | 72 / 224 bytes | 10 |
| func_1516865C | game_1944C0 | 1516865C..15168800 / 195B0C..195CB0 | 105 / 8 bytes | 14 |

Both former zero-return placeholders are now complete semantic C. Their linked
instructions match every retail word after 24 narrowly checked guards. Raw C
still differs at ten and fourteen words, respectively; this is guarded matching,
not direct compiler identity. No instructions are inserted or omitted. Both owners
retain the ordinary O2/g3 profile; no Makefile or shared header change is needed.

The callback builds a real 168-byte descriptor containing eight SDK Vtx entries
and effect parameters. It truncates x/z from the signed-byte selected 20-byte
position record and y from the fifth float argument. An unsigned random word
modulo21 plus35 supplies both signed16 lifetime fields. Texture18, flags12,
mode0, tag-1 and the original height initialize the remaining written fields.
The color initializer receives white RGBA; the constructor receives actor[0xC]
and actor[1] reloaded after that call. Finally the originally saved owner at
actor+0x98 receives byte4 at+0x20, and the callback returns1 even when the
constructor returns NULL. The position table at actor+0x94 is snapshotted across
both signed-index reads before RNG; its two index loads remain distinct.

The interface is `s32 (u8 *, f32, f32, f32, f32, void *)`, matching the existing
D_8008A430 table declaration in generated_175250.c. The only aligned literal
is D_8008A430[2], VA8008A438 / ROM22EEF8; there are no direct JAL/tail sites.
The original 19-word dispatch/result window is executed, including the fifth
stack float, sixth context pointer and return-one branch delay. The complete
parent is not claimed here.

The initializer interface is `void (void *, u8, u8, u8, u8)`. The actual fifth
alpha byte is read from its incoming o32 home. It clears flags and assigns RGBA
for eight vertices in two explicit groups of four. Texture-table dimensions
at+6/+8 produce signed16 wrapped UV endpoints `(dimension+256)*32`, with8192
as the other endpoint. Descriptor flag bits0x80/0x100 flip V/U. Each flip reloads
the texture index and pointer. The two quads receive identical coordinates;
descriptor halfwords88/9C/9E are cleared. Positions and other retained data are
preserved. Seven original JAL sites were inspected (ROM E91E4,111DB0,1A6AF0,
1A710C,1B9B10,1B9C34,1C0920); each passes the fifth alpha word and ignores
the return. No literal/tail references exist. These other complete callers
remain unchanged and are not claimed as new recoveries.

## Derivation, owners and image

The callback guards cover two commutative ADDU operand orders, a paired private
height spill/reload at SP+28 versus retail SP+2C, and six words in a closed
seven-store descriptor/alpha schedule. Its complete 224-byte frame, descriptor
at SP+38, saved S0/RA, helper-call positions and three JAL bindings already match.
The private home pair remains disjoint from the descriptor and outgoing args.

The initializer guards cover the final UV/clear store schedule and a short-lived
scratch register assignment. Its complete frame, saved S0 lifetime, color loop,
flips and table HI16/LO16 bindings already match. A symbolic LH/SH pass over
arbitrary register/descriptor halfword tokens proves the final memory writes
identical. The root store permutation, commutative operations and paired home
replacement are checked independently before deriving any guard output.
Full-body hashes and exact bindings fail closed before normalization.

All eight other generated-owner bodies and41 other helper-owner bodies are
identical before and after padding, with relocations retained. Every padded
allocatable pool/register field is fixed. The raw callback .reginfo/.options
change only the expected FPR mask from0 to0xD0DD0; .options file offset follows
ordinary object geometry. All other raw pools/option fields remain fixed.
The callback has zero diagnostics; the helper owner retains its same seven
pre-existing warnings with no additions/removals.

The literal full-image predictor permits only the two complete retail bodies
and their symbol sizes12 to288/420. Actual Make equals the **553-byte ELF delta**
with **zero excluded ranges**, no symbol/string permutations, all6,052 function
addresses fixed, and all189,088 protected Game bytes across720 owners exact.
The inherited guard CSV is retained byte-for-byte as a prefix; exactly24 rows
are appended. progress.csv is unchanged because both routines already had C
placeholders. Actual Make recompiles exactly the two owners under O2/g3.
The inherited duplicate12D630 recipe warning and expected unfinished-ROM
checksum exit2 remain; there are no compiler/link failures.

## Qualification

Eight methods pass before and after installation in both tools configurations:

- **568 root cases per body** compare retail, raw C and padded C against the
  independent byte reference. All256 signed indices, signed/truncated heights,
  full-word unsigned remainders, allocation success/failure and helper mutations
  are covered. All72 root words are visited. Connected cases execute the
  original105-word initializer,28-word constructor and18-word RNG, separately
  and together; allocation and bcopy remain bounded providers. The 64-bit RNG
  model explicitly uses low32 operands for DIVU, as the instruction requires.
- **600 initializer cases per body** compare every byte across texture indices
  0/18/255, both flips, dimension wrapping, distinct RGBA values and retained
  positions. All105 words are visited.
- **321 fired access cuts** across five layouts compare complete emitted state,
  private bytes, PC/delay markers and traces. A texture-table/vertex overlap
  exercises the flip's invalid-pointer reload prefix. These are guest checks;
  raw C's private schedule is not claimed fault-identical or portable alias C.
- **12 original dispatch-window cases per body** check the actual six-argument
  callback and its result branch. **12 independent GNU links**, three layouts
  per routine, carry all five relocation bindings, including signed-low16
  carries;18 rebased execution cases per body pass.
- SDK **native32 UBSan** passes O0/O2/O3 with448 root and200 helper cases per
  profile. All11 root and8 helper negative controls fire, including both former
  stubs, signedness/stride/height/lifetime/texture/color changes, early argument
  capture, live-owner reload, missing flips and incorrect alpha/clears.
  SDK layout asserts168-byte descriptors/16-byte vertices. Fully initialized
  helper packets and fences are compared. The bounded root initializer checks
  all defined input fields before initializing only previously unwritten holes;
  it does not assign portable values to indeterminate production bytes.
- All708 raw-byte, five binding and ten full-image corruptions are rejected.
  All113 core/header snapshots remain checked. No hardware rendering or
  gameplay acceptance is inferred from these code and model checks.

Both tools configurations run fresh shared smoke checks. Three unchanged
shared regression receipts are reused only under exact helper/test fingerprints.
The sibling uses its own compiler/padder/parser/base oracle/native command;
its missing allocatable-pool module uses the explicitly fingerprinted mounted
helper read-only. New modules use a disposable overlay. The sibling's2434
dirty paths remain untouched. Claude calls:0.

## Production checkpoint and next target

| Section | Byte-exact | Drift | Still different |
| --- | ---: | ---: | ---: |
| Total | 4,216 / 5,512 (76.49%) | 0 | 1,296 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 3,543 / 4,839 (73.22%) | 0 | 1,296 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

**194 more** matches reach the current4,410 threshold for80%.

- ELF: `eb7bf8d4743637447c3828453d66ce32a6302c1278cb9da46b582686e481cfcc`.
- Binary: `8133b907648256dd4c97e12030fd5b0c805ea0584aff28cefc3ac19da5dc01d5`.
- Guard CSV: `7279941acba7f0702468e833e5918a31209722e4ce3479f3a0e8b964b1a5c725`.
- Unchanged Makefile: `11a4fb98a37a39f0778ea9bb9b9d883d0a0d717b562065017d305a84456b1bea`.

Reproduce with `python3 -m unittest tools.tests.test_game_selected_vertex_sprite_match -v`.
Receipts live in `conker/build/game-selected-vertex-sprite-1518C57C-match/`.
Actual Make uses `-o retail_word_patches.us.csv -o Makefile` to freeze the unchanged
shared inputs while rebuilding both edited owners, then ELF/progress, expected
unfinished-image `all`, and `match-progress NON_MATCHING=1`.

Tools commit precedes source/guards/docs/pin. README receives aggregate rows
only. Historical status-index bodies are checked against HEAD in UTF-8.
Graphify is refreshed over the changed paths with old-node retention checks;
this is a scoped AST refresh, not full-corpus extraction.

Next is **func_1518C69C**, the109-word adjacent callback in generated_1B8F40.
It shares this descriptor/initializer path but also submits additional effects;
inspect its complete body and D_8008A450 callback contract before recovery.
It remains a zero-return placeholder and is uncredited. Preserve handwritten
func_150A6FA0/func_150A76F0, unrelated work, private inputs/saves and frozen
host Release. Keep the full80% goal active.
