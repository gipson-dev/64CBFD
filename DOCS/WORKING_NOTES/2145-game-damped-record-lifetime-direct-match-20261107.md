# Damped record lifetime directly matched

Date: 2026-11-07. Continues [Note 2144](2144-game-position-queue-drain-match-20261107.md)
from consumer `cf47e40305503eb770f002a82ef4dc4f776295fd` and mounted tools
`619752da1d0aac5244331c55d09702c2056654b2`, toward the active 80% goal.

## Direct recovery and compiler profile

`func_15187978` in `conker/src/game/generated_1B1600.c` emits all
**72 words / 288 bytes directly from semantic C**, with the original
**24-byte frame and zero guards**. VA `0x15187978..0x15187A98`, ROM
`0x1B4E28..0x1B4F48`; four relocation bindings, no alignment tail.

The ordinary O2/g3 profile unrolls the twelve-record loop twice and emits
110 words, exceeding the retail slot. The retail no-unroll profile
`-O2 -g3 -Wo,-loopunroll,0 -mips2 -o32` emits the complete exact routine.
The Makefile adds one owner-specific OPT_FLAGS assignment and its comment.
All 32 predecessor functions are unchanged when switching profiles, and
all 31 other functions remain unchanged after source recovery. This makes
the owner-wide setting safe without changing any other owner or introducing
a second object-selection rule. The normal-profile 110-word control fails
the actual padder's slot bound.

Raw .reginfo and .options add only T2 to the GPR mask,
0xA37FFBFE to 0xA37FFFFE. Every other allocatable pool and register field,
all .options header fields except its file offset, and every padded pool/
register field remain fixed. Raw debug geometry is not claimed identical.
The inherited guard CSV is byte-identical.

## State and exact update order

The interface is `void (struct102 *input)`, matching the SDK struct115
callback. A local TimedDampedEffect1B1600 view names the actual 0xAC-byte
prefix, and DampedEffectRecord1B1600 names each real 0xA0-byte record.
The opaque bytes describe retained object data; no artificial frame object
was added. Offsets below are hexadecimal.

| Object | Offset | Field |
| --- | --- | --- |
| Actor prefix | A4 | Record buffer pointer |
| Actor prefix | A8 / AA | Signed16 age / lifetime |
| Each record | 8C / 90 | Float base increment / accumulated value |
| Each record | 94 / 96 | Signed16 elapsed / duration |

An age already negative at entry calls func_10004074(buffer), then
func_1516972C(input). The buffer may be NULL. The actor argument is kept in
its incoming home across the first call and reloaded for the second.
Otherwise the age receives the live D_800BE9E4 word with signed16 storage
wrap. If the stored result exceeds the signed lifetime, age becomes -10.
That call performs no buffer release; cleanup occurs on the following call.
A wrapped negative age also bypasses the record loop on the current call.

For each of twelve records, elapsed must be below duration before updating.
The signed16 elapsed receives a fresh clock word and is clamped only when
the wrapped stored result exceeds duration. The record pointer is reloaded
after the timer store and again after a clamp. The accumulated float receives:

`baseIncrement - ((baseIncrement / 3.0f) * (f32)elapsed) / (f32)duration`

Every division, multiply, subtraction and final addition rounds as a single
precision operation. The unsigned casts on the clock additions define the
32-bit wrap before signed16 storage without changing any emitted instruction.
No defensive NULL or zero-duration branch was added to the retail routine.

## Qualification evidence

Eight methods pass before and after installation in both tools configurations:

- **1,588 guest cases per body** cover signed16 actor/record wrap, negative,
  zero and positive lifetimes, threshold/clamp boundaries, live clocks,
  twelve-record traversal, helper mutations and incoming-home redirection.
  All reachable root words are visited. Word 15 is the unreachable duplicate
  clock load retained after retail's branch-likely split. Raw and padded C
  are identical to retail.
- **168 clock-alias cases per body** include actor timer words, incoming
  homes, increment/accumulator fields and timer words in records0/5/11.
  **245 fired memory access cuts** compare complete state, fault PC, delay
  markers and private bytes. The target's expiry path requires no clock or
  record-data reads. Guest overlaps/home redirection are separate from
  portable C alias claims.
- **192 connected cases per body** run the original 119-word Init allocator
  release, 28-word actor release, 20-word active-slot scan and eight-word
  adapter. They check NULL and single allocated-block frees, free-list
  head/tail and largest-block updates, live iteration-slot repair, category
  gates and injected optional callback/default branches. The retained
  helper bytes equal the current installed ELF. osSetIntMask and the final
  unlink remain bounded providers; no extra helper C recovery is credited.
- The callback appears once at ROM 0x2300A0 / VA 0x8008B5E0, category 6 of
  D_8008B4A8 with 52-byte records. A full aligned ROM census finds no direct
  JAL or tail entry. **72 cases per body** execute the original eleven-word
  dispatch window in func_151670C0, including the queued next node and its
  repair during release. The current whole dispatcher remains its stub.
- **Six independent GNU links**, three layouts and 54 cases per body verify
  both JALs and the clock HI16/LO16 pair, including signed low16 carries.
- SDK **native32 with UBSan at O0/O2/O3** runs **1,150 cases per profile**,
  3,450 positive executions. Canonical struct115 callback typing, pointer/
  record/actor offsets and sizes, complete actor storage, both twelve-record
  buffers and provider observations are checked. Native active arithmetic
  uses finite values; inactive NaNs retain their raw bits. All eleven
  controls fire: zero-age expiry, eager cleanup, wrapped-negative update,
  clamp, eleven records, stride, damping constant, float association,
  reversed cleanup, omitted buffer free and the former stub.
- **288 raw-byte, four binding and six full-image corruptions** fail closed.
  Model checks also include active NaNs, infinities and zero-duration
  arithmetic; they do not claim hardware/FCSR behavior or gameplay acceptance.

All 108 core/header snapshots remain checked. Both tools configurations pass
fresh shared smoke checks, with three unchanged shared regression receipts
reused only under exact helper/test fingerprints. The no-unroll compiler
helper, parser, guest base oracle, native command and metadata serializer
come from each selected tools checkout. The sibling's missing
game_player_status_accessor_match.py uses the explicitly fingerprinted mounted
allocatable-pool auditor read-only. The new modules use a disposable overlay;
the sibling's 2434 dirty status paths remain unchanged. Claude calls: 0.

## Production and next target

Actual Make recompiles only generated_1B1600.c once with the intended
no-unroll flag and zero C diagnostics. It equals the complete independent
**224-byte ELF prediction**, with **zero excluded ranges**. Only the target
body and its symbol size12 to288 change. There are no symbol/string
permutations. All 6,052 function addresses, other bodies, progress.csv and
189,088 protected Game bytes across 720 owners remain fixed. The Makefile
change is limited to the audited owner profile. The inherited duplicate
12D630 recipe warning and expected unfinished-ROM checksum exit 2 remain.

| Section | Byte-exact | Drift | Still different |
| --- | ---: | ---: | ---: |
| Total | 4,214 / 5,512 (76.45%) | 0 | 1,298 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 3,541 / 4,839 (73.18%) | 0 | 1,298 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

**196 more** matches reach the current 4,410 threshold for 80%.

- ELF: `400ecfbb8e617f55d2f17adf449d5d4387a48718922e5267baeef0fc6a650ca3`.
- Owner: `f7d86a1425024b44d04254e94b173af158b6690d1ceebf555eb83bbfbd3fe4a6`.
- Binary: `b4b705a09ad6fffcd96afae5b7ba660223cd3d6da595b85f83a7b9527d4885fa`.
- Unchanged guard CSV: `72ad5715645cd16dfcfedaba1dd530570e9a3eaa07c8746f81ce20a2d908ef7d`.
- Audited Makefile: `11a4fb98a37a39f0778ea9bb9b9d883d0a0d717b562065017d305a84456b1bea`.

Reproduction: `python3 -m unittest tools.tests.test_game_damped_record_lifetime_match -v`.
Actual Make uses `-o retail_word_patches.us.csv -o Makefile`, followed by
ELF/progress, expected unfinished-image `all`, and
`match-progress NON_MATCHING=1`. Receipts are in
`conker/build/game-damped-record-lifetime-15187978-match/`.

Tools commit precedes source/profile/docs/pin. Root README gets aggregate
rows only. Status-index history is checked against the predecessor in UTF-8.
Graphify retains nodes outside changed paths and the legacy fail-closed corpus;
this scoped refresh is not full extraction. Next is **func_1518C57C**,
generated_1B8F40, 72 words, still a zero-return placeholder. Inspect its complete
routine and caller contract before recovery. Preserve handwritten
func_150A6FA0/func_150A76F0, unrelated work, private inputs/saves and frozen
host Release. Keep the full 80% goal active.
