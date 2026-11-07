# Position draw queue matched

Date: 2026-11-07. Continues [Note 2143](2143-game-cached-vector-basis-direct-match-20261106.md)
from consumer `ec122e29efee15438f182e410acd62662a7e9de9` and mounted tools
`0821b56cb5068b0b8bde04c9abdc04ef11559221`, toward the active 80% goal.

## Recovered queue drain

`func_1517D690` in `conker/src/game/generated_1A89B0.c` now matches all
**72 words / 288 bytes**, with the original **0x50 frame** and five saved S
registers plus RA. VA `0x1517D690..0x1517D7B0`, ROM
`0x1AAB40..0x1AAC60`. Semantic C emits 72 words with 20 scheduling differences.
Twenty expected-word guards reproduce retail. There are no inserted words,
alignment tail or profile changes; the owner remains O2/g3/MIPS2/O32.

The interface is `Gfx *(Gfx *displayList, u16 *pixels)`. The function saves
the 32-bit allocation index D_800DDD58, advances byte D_800DDD1C by five
with byte wrap, then subtracts 200 once if the wrapped value is at least 200.
It consumes D_8008CEB0[0] backwards. NULL pixels still drain the queue.
Each enabled entry submits its three signed16 coordinates, raw float angle,
two unsigned16 values promoted to full words, constants 16/32 and
`pixels + row * 640` to func_1517D074. Its latest returned Gfx pointer is
chained into the next request. The count and records remain live across calls.
The original allocation index is restored before returning the latest Gfx.

The real producer func_1517D578 limits the queue to three 16-byte records.
The existing PositionQueueEntry type is reused without changing shared headers.
Its float word at offset 0xC is an angle: the renderer multiplies it by a
constant and passes it to cosf/sinf. The following full-word parameters are
the two half extents; the final constants are texture dimensions. The typed
helper names reflect those uses. Its integer coordinate parameters retain
their full-word call ABI; the queue supplies sign-extended16 coordinates.

## Closed argument schedule and full dependent-function audit

Only the argument block at offsets 0x8C..0xDC is rescheduled. The source and
retail contain the same complete instruction multiset. The derivation reads
the frozen raw C words, verifies the complete raw hash and eleven bindings,
and permutes existing words. It preserves all ten register/HI/LO dependency
edges, the JAL at 0xD8 and every relocation binding. Record reads and outgoing
argument stores address separate objects under the ordinary C contract.
Raw C is checked independently for complete call/return/state semantics;
its original memory-access order is not claimed identical to retail's.
The normalized body is checked literally, including access/fault prefixes.

The helper's typed declaration also requires typing its existing zero-return
placeholder. **func_1517D074 remains unfinished and receives zero credit.**
Its compact body changes from three words to seven: four incoming A0..A3
home stores followed by its unchanged zero return. Those exact seven words,
zero relocations, the complete padded footprint and symbol extent12 to28
are checked explicitly. Twelve other compact and padded neighbors stay fixed.
No dependent function or image range is excluded from comparison.

Old and typed helper stubs preserve queue, call and return behavior in sixteen
cases per body; their private-memory differences are confined to the four
argument homes. The typed stub is also exercised through its real ten-argument
SDK native interface and still returns NULL. No renderer recovery is credited.

Raw .reginfo and .options add only F4 to the FPR mask, 0x1000 to 0x1010.
Every other allocatable pool/metadata field and all padded pools/register
metadata remain fixed. Raw debug and section file offsets may move.

## Qualification evidence

Eight methods pass before and after installation in both tools configurations:

- **3,492 guest cases per body** check all 256 phase bytes, all 256 NULL-pixel
  count bytes, wrapping and threshold boundaries, reverse order, signed
  coordinates, unsigned record values, NULL/chained return pointers, live
  count refills, record/phase mutations and final index restoration. Every
  root word is visited. Raw C is separately checked against the independent
  semantic reference. Float bits include signed zero, subnormals, infinities
  and quiet/signaling NaNs, moved without arithmetic in the drain/model.
- **128 alias cases per body** place each global in incoming homes.
  **883 fired access cuts** compare complete literal states, fault PCs and
  delay markers. NULL pixels require no record data, even with count 255.
  These are guest memory/fault checks, not portable stack-alias claims.
- **576 connected cases per body** run the original 321-word renderer on its
  capacity-rejection path; the rejected call returns its incoming Gfx pointer.
  **80 producer cases** run the complete original 33-word func_1517D578, check
  truncation, queue capacity and the resulting drain. The renderer's drawing
  path and complete caller parent are outside this qualification.
- A full ROM census finds exactly one JAL at ROM0x1AACC8 / VA0x1517D818 in
  func_1517D7B0 and no literal pointers or tail entries. **192 cases per body**
  execute its original four-word call/result-store window, including the
  D_800DDD24 pixel load in the delay slot and the returned Gfx store.
- **Six independent GNU links**, three layouts and 48 cases per body check
  all eleven bindings, signed low16 carries and standalone zero tails.
- SDK **native32 with UBSan at O0/O2/O3** runs **2,640 cases per profile**,
  7,920 positive executions. It uses the real three-record bound and checks
  record/Gfx/pointer sizes, offsets, all ten arguments, pixel stride, complete
  initialized state, helper observations and returned pointers. All ten
  controls fire: cycle increment, wrap comparison, queue order, skipped NULL
  drain, unsigned coordinate, signed record value, stride, index restoration,
  lost Gfx chaining and the old stub.
- **288 raw-byte, eleven binding and ten full-image corruptions** fail closed.
  The former drain stub's missing phase update and false return are rejected.

The 105 core/header snapshots remain checked. Both tools configurations pass
fresh shared smoke checks. Three unchanged shared regressions are reused with
exact helper/test fingerprints. The sibling supplies its compiler, parser,
guest oracle, native command and metadata serializer. Its missing
game_player_status_accessor_match.py uses the explicitly fingerprinted mounted
allocatable-pool auditor read-only. New modules use a disposable overlay;
the sibling's 2434 dirty status paths remain unchanged. Claude calls: 0.

## Production and resume boundary

Actual Make recompiles only generated_1A89B0.c once, with zero C diagnostics,
and equals the independent **249-byte complete ELF prediction**, with **zero
exclusions**. The prediction includes the drain body, its symbol size12 to288,
the complete typed helper stub and its symbol size12 to28. There are no
symbol/string permutations. All 6,052 addresses, other function bodies,
Makefile, progress.csv and 189,088 protected Game bytes across 720 owners
remain fixed. The inherited duplicate 12D630 recipe warning and expected
unfinished-ROM checksum exit 2 remain. No hardware or gameplay acceptance
is claimed.

| Section | Byte-exact | Drift | Still different |
| --- | ---: | ---: | ---: |
| Total | 4,213 / 5,512 (76.43%) | 0 | 1,299 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 3,540 / 4,839 (73.16%) | 0 | 1,299 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

**197 more** matches reach the current 4,410 threshold for 80%.

- ELF: `de1aad0c43aae018edc66254bc066e44e2b8bd9b7bf5eb2c72167e3076714bb4`.
- Owner: `6e3f1b5a4512ba33de8114bf7a81c0fe029efbee22022ddf8e0cad0010ac8e17`.
- Binary: `6f3b9d3c906d7d72c0032a547ae11ed11953759ecd1ee24f41cef2f06e9bcf06`.
- Guard CSV: `72ad5715645cd16dfcfedaba1dd530570e9a3eaa07c8746f81ce20a2d908ef7d`; inherited rows preserved, twenty appended.
- Unchanged Makefile: `509371c33a6266fa242b20212c16cf42d4b61575a8773b053bfad43d0778ae1b`.

Reproduction: `python3 -m unittest tools.tests.test_game_position_queue_drain_match -v`.
Actual Make uses `-o retail_word_patches.us.csv -o Makefile`, followed by
ELF/progress, expected unfinished-image `all`, and
`match-progress NON_MATCHING=1`. Receipts are retained in
`conker/build/game-position-queue-drain-1517D690-match/`.

Tools commit precedes source/guards/docs/pin. Root README receives only its
aggregate counts and verification date. Graphify retains nodes outside changed
paths and the legacy fail-closed corpus; this scoped refresh is not full
extraction. Next is **func_15187978**, generated_1B1600, 72 words, still a
zero-return placeholder. Inspect its complete routine and caller contract
before recovery. Preserve handwritten func_150A6FA0/func_150A76F0, unrelated
work, private inputs/saves and frozen host Release. Keep the full 80% goal active.
