# Selected impact sprite and effect submission matched

Date: 2026-11-07. Continues [Note 2146](2146-game-selected-vertex-sprite-and-initializer-match-20261107.md)
from consumer `2ff5fe8fdc22d76940569d347b2a34005a254b01` and tools
`fa2616d44b0276d1f9d78d32b7bf3c9623ccc3b3`, toward the active 80% goal.
The previous goal turn adopted two functions; this turn adds one further match.

## Complete callback and explicit C sequencing

`func_1518C69C` in `conker/src/game/generated_1B8F40.c` now has its complete
**109-word / 436-byte** C body. VA `0x1518C69C..0x1518C850`, ROM
`0x1B9B4C..0x1B9D00`. Twenty-one checked guards reproduce all retail words;
raw C remains 21 words different. No words are inserted or omitted. The ordinary
O2/g3 profile, shared headers and Makefile are unchanged.

The interface is `s32 (u8 *, f32, f32, f32, f32, void *)`, matching the existing
D_8008A450 table declaration. The sole aligned pointer literal is slot1,
VA8008A454 / ROM22EF14; there are no direct JAL or tail sites. The actual
19-word dispatch/result window is executed, including its zero-selector skip,
fifth stack float, sixth context pointer and return-one branch delay. This
does not claim a new recovery of the complete parent.

The first phase uses the 168-byte SelectedVertexSprite descriptor recovered in
Note2146. It retains the original owner and position-table pointers, truncates
the signed-index x/z and float height, chooses an unsigned random lifetime35..55,
initializes white vertices, and submits the sprite. Allocation failure still
continues. The captured owner's byte+20 becomes4 before the second phase.

After the constructor, the actor's signed index is read again for each x/z
coordinate, using the originally retained table pointer. The fifth incoming
float supplies the second phase's y without integer truncation. The real
12-byte vector is captured before selector and float-RNG calls. The returned
selector byte survives the float call; magnitude is `(randomFloat*40.0f)+100.0f`
with separate float32 rounding. The final seven-argument call receives selector,
magnitude, alpha255, the sixth callback argument, the vector, and freshly read
actor category/row bytes. The callback returns1 and performs no final mark write.

The selected C stores the float draw/calculation in a separate `magnitude`
statement before reading the actor bytes in the submission argument list.
Native O0 exposed that a nested RNG call allowed GCC to evaluate those bytes
too early. The explicit statement fixes that sequencing while producing the
same complete IDO instruction body and relocation bindings. An effective
native control deliberately captures the bytes too early and is rejected.

## Checked frame and schedule derivation

Raw IDO emits109 words with a256-byte frame; retail uses248 bytes. The source
contains real descriptor/vector/scalar locals, with no fabricated padding object.
The eight bytes at raw SP+248..255 are unused. The derivation audits every
SP-relative use before allowing compaction:

- All31 private memory accesses end within248 bytes. Saved S0/RA remain at
  SP+28/+2C. The descriptor begins at SP+50 and its real168-byte extent ends
  exactly at248; the vector begins at SP+38 and occupies12 bytes.
- The only three local address formations are descriptor, descriptor, vector.
  No address escapes into the unused tail. There are no intermediate stack
  adjustments.
- Eight frame/home guards adjust entry/exit and all six incoming-home accesses
  together. Absolute caller-home addresses are preserved when SP moves by8.
- Four guards exchange only commutative ADDU operands. Six guards close a
  seven-store descriptor/alpha permutation. Three move the independent stride
  constant before the mark/index operations while retaining their public
  store-then-read order. No call or relocation changes position.

Full-body hashes and all six JAL bindings fail closed. Independent controls
reject a live frame-tail access, an escaping tail address and a wrong incoming
home. The actual padder output equals the derivation and complete retail body.
Raw C is tested against its own256-byte frame/seeded packet holes; it is not
claimed private-byte/fault-identical to the normalized248-byte body.

All eight other owner functions and their relocations remain fixed before and
after padding, including both preceding recoveries. All padded allocatable
pools/register fields are fixed. The raw .reginfo/.options FPR mask changes
only from0xD0DD0 to0xF0DF1; all other fields/pools remain fixed apart from the
.options file offset following object geometry. Both predecessor and qualified owners compile
without diagnostics. Exactly21 guard rows are appended to the unchanged CSV
prefix; previous guards are preserved byte-for-byte.

## Qualification evidence

Eight methods pass pre/post installation in both tools configurations:

- **1,304 guest cases per body**, retail/raw C/padded C, cover all256 signed
  indices, integer versus float heights, unsigned lifetimes, NULL allocation,
  retained table pointers, live indices, provider mutations, incoming homes,
  selector capture and ordered float32 arithmetic. All109 root words are visited.
- **96 additional connected cases per body** execute308 retained helper words:
  integer RNG18, float RNG25, vertex initializer105, sprite constructor28,
  selector19 and effect service113. Both RNGs and the service's three optional
  draws share the64-bit seed. Installed ELF helper bytes equal retail; the
  actual768-byte palette is used (SHA256
  `b04bfb61b1be673d66b77194d0bfc89d12aba9de0c92a08ef285ff2fc77b5e6d`).
  Both effect branches, defined descriptor fields and all14 low-level arguments
  are checked. Allocation, bcopy, query and low-level emitters remain bounded
  providers. Three unwritten service bytes are omitted only from semantic
  packet observation; no ELF range is excluded. No extra helper C is credited.
- **443 fired access cuts**, including35 delay-slot cuts and all owned64-bit
  RNG memory accesses, compare complete emitted state, private bytes, trace,
  PC and delay markers. Incoming height/context and vector-home mutations
  are guest checks; portable C alias/FCSR/hardware acceptance is not claimed.
- **16 original caller-window cases per body** include enabled and skipped
  callback paths. **Six independent GNU links** carry all six JAL bindings
  through three layouts; nine rebased execution cases per body pass.
- SDK **native32 UBSan** passes O0/O2/O3 with796 cases each. All17 semantic
  controls fire, including early actor-byte capture, live table/owner reloads,
  delayed marking, wrong position height, scale/context/alpha changes and the
  former stub. Typed callback/service interfaces, complete initialized packets
  and owner fences are checked. The bounded initializer checks defined inputs
  before filling only unwritten holes; no portable value is assigned to the
  indeterminate production bytes.
- All436 raw-byte, six binding, three frame-extent and six whole-image
  corruptions are rejected. All114 core/header snapshots remain checked.

Both tools configurations run fresh shared smoke checks. Three unchanged shared
regression receipts are reused only with exact helper/test fingerprints.
The sibling uses its own compiler/parser/padder/base oracle/native command.
Its missing pool auditor, tracked64-bit RNG executor and newly committed vertex
fixture dependencies use explicitly recorded, fingerprinted mounted modules
read-only. New modules use a disposable overlay. Windows Git verifies the
unchanged2434 dirty sibling paths; WSL's three inherited submodule/file-mode
reports are preserved separately, without changing any checkout configuration.
Claude calls:0.

## Production checkpoint and next function

Actual Make recompiles only generated_1B8F40.c once, under O2/g3 with zero C
diagnostics. The linked ELF equals the literal **329-byte prediction**, with
**zero exclusions**. Only the complete target body and symbol size12 to436
change. All6,052 addresses, other bodies, progress.csv and189,088 protected
Game bytes across720 owners stay fixed. The inherited duplicate12D630 recipe
warning and expected unfinished-ROM checksum exit2 remain.

| Section | Byte-exact | Drift | Still different |
| --- | ---: | ---: | ---: |
| Total | 4,217 / 5,512 (76.51%) | 0 | 1,295 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 3,544 / 4,839 (73.24%) | 0 | 1,295 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

**193 more** matches reach the current4,410 threshold for80%.

- ELF: `179206d917663ba74e403486ca6fa037b6f195ddcd6e10329b56b965178083f3`.
- Binary: `774ecdd13cc042e8ca35d0d62ccdb75f878815c94f7e398768c90f7635e6a298`.
- Guard CSV: `a1d33e60900a06e6821361960dc1e6f3bfec2d850c8a916e7ad511103c0ec45f`.
- Unchanged Makefile: `11a4fb98a37a39f0778ea9bb9b9d883d0a0d717b562065017d305a84456b1bea`.

Reproduce with `python3 -m unittest tools.tests.test_game_selected_impact_sprite_match -v`.
Receipts live in `conker/build/game-selected-impact-sprite-1518C69C-match/`.
Actual Make freezes unchanged shared dependencies with
`-o retail_word_patches.us.csv -o Makefile`, then runs ELF/progress, expected
unfinished-image `all`, and `match-progress NON_MATCHING=1`.

Tools commit precedes source/guards/docs/pin. README receives aggregate rows
only; historical status-index text is checked against HEAD as UTF-8. Graphify
retains nodes outside changed paths in a scoped/fail-closed refresh, not full
re-extraction. Next is **func_1518BA90**, the89-word owner-record lookup/
constructor in this same source, still a zero-return placeholder. Inspect both
row scans, owner/tag matching, the jump table and its existing constructor
before recovery. Preserve handwritten func_150A6FA0/func_150A76F0, unrelated work,
private inputs/saves and frozen host Release. Keep the full80% goal active.
