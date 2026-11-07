# Record motion update recovered directly in C and byte matched

Date: 2026-11-07. Continues [Note 2162](2162-game-dual-record-animation-update-match-20261107.md)
from consumer `08351fa10817683bb3194b461dc26c6e871efbb0` and tools
`7a3138f447d1f42c932a78fcb53ec08e052de012`. One qualified Game recovery
advances the active 80% total goal. This change is confined to the decomp.

## Recovered source and interface

`s32 func_1513E6E8(u8 *record)` replaces the false zero-return placeholder
in `conker/src/game_169510.c`. All **85 words / 340 bytes emit directly from
semantic C**, with **zero new guards**, at VA 0x1513E6E8..0x1513E83C,
ROM 0x16BB98..0x16BCEC. It is a frame-zero leaf with no calls or saved
registers, and returns 1. The original O2/g3, MIPS2/O32 profile is unchanged.
All four HI16/LO16 relocation bindings refer to D_800BE9A4 and stay literal.

Word +0x58 selects four ordered float32 groups. Each destination adds its
source multiplied by the live float time scale D_800BE9A4:

| Flag | Destination offsets | Source offsets |
| --- | --- | --- |
| 0x20 | +0x11C | +0x13C |
| 0x40 | +0x34 / +0x38 / +0x3C | +0x118 / +0x11C / +0x120 |
| 0x80 | +0x40 / +0x44 / +0x48 | +0x124 / +0x128 / +0x12C |
| 0x100 | +0x4C / +0x50 / +0x54 | +0x130 / +0x134 / +0x138 |

The first group updates +0x11C before the second group consumes it. Each
multiply rounds to float32 before the add; time loads remain live per
component, including when a destination aliases the time scale. Always
store 255 to byte +0x5D, then return 1. Clear flags require only the flag
word and reset byte to be mapped; no float, global-time or stack access is
needed on that path. Offset views avoid speculative broad structure edits.

The selected source forms `motion = record + 0x110` before each conditional.
That source shape reproduces the retail address lifetimes and branch delay
slots. Putting the assignments inside every arm produced 82 words as IDO
folded the addresses into record-relative loads/stores. Last-two-before gave
83 words; explicit flag-phi variants gave 85 words with 36/37 differences.
Integer casts, typed motion/embedded-record views and register hints did not
fix the shorter output. A volatile-pointer control introduced an unwanted
8-byte frame and 101 words and was rejected. None of those screens was
installed or credited. The successful **all-before** shape emits all 85
words without normalization. Raw SHA-256:
`741f29a5294f07d8a1bf3df24119e55a5e93fb159aa4103ee4b65510ced72e5f`.

Only this function's obsolete commented m2c sketch is removed. Its source
and prototype round-trip to the complete frozen predecessor in qualification.
Original assembly and unrelated commented/unfinished functions remain.

## Caller, independent model and focused checks

The aligned complete retained-ROM census finds no direct JAL, exactly one
entry pointer at ROM 0x22E77C, and no interior pointers. It is index 1 of
the actual 42-word D_80089CB8 update table. The complete **195-word
func_1513CFE4** calls it with one record pointer and treats zero as a removal
request. Returning 1 therefore preserves that callback's success behavior.
The caller is already byte-exact in the frozen production ELF, independently
checked against the full retained ROM window.

Seven focused checks pass before and after installation for both tools
configurations:

* **1731 guest cases per body** compare retail and compiler output with
  an independent ordered memory/float32/return model. All 512 low flag values,
  all four motion groups, clear and combined masks, signed zeros, subnormals,
  finite rounding boundaries, and bounded nonfinite inputs are covered.
  Time aliases at the first velocity destination and first position output
  test live time reloads. All 85 words execute. Full memory, private machine
  state and the leaf's saved-register/stack invariants agree.
* **192 connected cases per body** execute the full original adopted updater
  with this actual callback body, covering disabled records, motion masks,
  expiration, second-service outcomes, exit veto and bounded live mutations.
  Other callbacks and release stay explicit bounded providers. Record banks
  extend to 512 bytes, remain disjoint, and include every read through +0x13F.
* **144 fired memory-access cuts** compare complete private memory,
  GPR/FPR/HI/LO, PC and access-prefix traces. There are no stack accesses or
  memory delay-slot cuts in this leaf. FCSR exceptions are not emulated.
* Native32 O0/O2/O3 each pass **886 cases** through the actual table's selected
  typed s32 callback slot, with SDK types, pointer32 assertions and trapping
  UBSan. Check round-to-nearest mode with FTZ/DAZ clear. Eight compiled
  negatives reject with exit 1: stub, wrong flag, skipped velocity update,
  wrong source, destination, time scale, reset byte and return value.
* Two independent GNU links verify all four bindings, including a signed
  LO16 carry. Every altered raw instruction, changed binding/history, pool
  metadata corruption and six whole-image corruptions is rejected.

The numerical model is bounded IEEE-single arithmetic, not a FCSR or hardware
NaN-payload emulator. Native cases use finite observed results; aliases and
nonfinite numerical cases remain guest-only. The full instruction-word
match is established separately. These checks do not claim live gameplay
acceptance or restoration of the entire callback table. No Claude review
call was necessary for this direct reconstruction.

## Whole-owner and production checkpoint

All **181 frozen inputs**, **58 raw and padded neighbors**, constant pools,
register masks/options and **43 inherited compiler warnings** remain fixed.
The existing padder uses `jtbl_800A5188_game`. Actual Make recompiles only
game_169510.c and equals the independent complete-image prediction:
**266 changed bytes, zero exclusions**. They comprise 264 Game-body bytes
and two symbol-extent bytes. No symbol/string ordering change occurs; the
only changed extent grows from 12 to 340 bytes.

All **6,052 function addresses** and other bodies remain fixed. All **189,088
protected Game bytes across 720 owners** remain exact. The guard manifest,
Makefile and progress CSV are unchanged. Compilation/linking pass; the
still-nonmatching whole-ROM checksum retains expected exit 2 and the inherited
duplicate generated_12D630 recipe warning.

Fresh shared smoke checks pass in both tools copies. Three unchanged shared
regression receipts per copy are explicitly reused after exact fingerprints.
A disposable new-module overlay and hashed read-only missing-helper fallback
preserve all 2,434 inherited dirty paths in the sibling tools checkout.

| Section | Exact / converted | Percent | Drift | Still different |
| --- | --- | --- | --- | --- |
| Total | 4,233 / 5,512 | 76.80% | 0 | 1279 |
| Game | 3,560 / 4,839 | 73.57% | 0 | 1279 |
| Init | 492 / 492 | 100.00% | 0 | 0 |
| Debugger | 181 / 181 | 100.00% | 0 | 0 |

**177 more exact functions** remain to 4,410 / 80%. Root README receives
only aggregate rows; four concise index leads preserve their complete
historical content. Refresh Graphify on changed paths with fail-closed
legacy-node retention, without claiming a fresh full-corpus extraction.
Commit tools before consumer source/docs/pin, then verify the fresh hook
terminal and stable production artifacts.

| Artifact | SHA-256 |
| --- | --- |
| Production ELF | `635e1081b99cac777e9be8fd50f4ceede6f224d3c2de0d3a8b0cf24ddb9912fc` |
| Production binary | `ed935c92c690b591960e7eb1550de5cdc236c08d4011431adb5796691a2fced7` |
| Padded owner | `f48879aa04c7425126c45a8bb17c7f0230dc20b95c11daa4b274a4a8d9010682` |
| Guard manifest, unchanged | `3cac0eb5aeb58c3d77c9a52374a6707ff9bc3c8d426b8f1f1e135ead4847f776` |

Ignored receipts: `conker/build/game-record-motion-update-1513E6E8-match/`.
Private source screens: its adjacent `-private` directory.

Next: **func_1513E83C**, the 167-word record vertex callback at
VA 0x1513E83C..0x1513EAD8, ROM 0x16BCEC..0x16BF88, frame 216. Recover its
view/resource query, optional double copy, transform/scale and four-vertex
output loop, then qualify its actual dispatch interface independently.
Keep other candidates private and uncredited, the 80% goal active, and the
frozen handwritten/hidden-ABI, private-input, save and host Release boundaries.
