# Game Palette Color Emitter: Byte Match And Segment Connection

Date: 2026-10-04. Starting HEAD: `104ce180`.

## Decision

Finish the interrupted `func_1510CDB8` recovery preserved by
[Note 971](971-init-pause-resume-remaining-assembly-decision-20261004.md).
Replace its zero-return placeholder with the actual SDK `gDPSetPrimColor` and
`gDPSetEnvColor` commands and the correct `Gfx *` return interface. The entire
**42-word / 168-byte slot is raw byte-exact**, frameless, without expected-word
guards, a compiler override, address drift or changed data ownership.

This closes the color-emitter -> queued-writer source connection requested by
[Note 970](970-game-queued-segment-writer-and-big-endian-alias-qualification-20261004.md).
It does not recover the palette generator or full renderer, establish RSP/RDP
acceptance, or synchronize any host stubs. Production Init remains unchanged.

## Color Contract

The four arguments are a display-list cursor, two 32-bit alpha inputs and a
signed 32-bit palette index. `D_800D9B68[4][3]` and `D_800D9B78[4][3]` supply
primitive/environment unsigned RGB bytes. Each row has a three-byte stride;
the twelve-byte tables start sixteen bytes apart. No data is defined or moved.

Emit two consecutive eight-byte commands:

1. Header `0xFA00F200` and primitive RGB packed into the high three bytes,
   with `arg1 & 0xFF` in the alpha byte. The SDK primitive parameters are
   `m = 0xF2`, `l = 0`.
2. Header `0xFB000000` and environment RGB packed the same way, with
   `arg2 & 0xFF` in the alpha byte.

Return the initial cursor plus sixteen bytes. The emitted IDO/retail words
store each header before reading that palette's bytes, in B/R/G order. Output
overlapping a palette therefore changes subsequent reads and packed colors.
The exact generated words, not a little-endian host alias experiment, establish
that observed ordering. No NULL, capacity or palette-bound check is invented.

Ordinary complete palette qualification covers rows 0..3. Invalid indices below
are only compiled-instruction prefixes in a bounded memory model, not defined
out-of-bounds C semantics, graceful handling, or physical N64 fault behavior.

## Verification

Six added tests extend
[`test_game_queued_segment_writer.py`](../../tools/tests/test_game_queued_segment_writer.py)
from ten to sixteen checks. They extract the actual production bodies and the
actual SDK macros from local headers, rather than duplicate the implementation.

- Strict 32-bit native fixtures cover all four rows and every pair of low alpha
  bytes: **262144 cases**, using high-bit/signed 32-bit arguments. They assert
  independent expected RGBA words, cursor advancement, palette/queue retention
  and output fences. Another fixture connects actual append -> color -> writer.
- **676 complete paired big-endian traces** cover all four rows and a thirteen-
  value alpha edge matrix, complete ordered reads/stores, independent command
  values and every instruction address in both 42-word bodies.
- **86 complete paired traces** cover palette/output overlaps, including two
  independently asserted header-before-read results. At the primitive table,
  row-zero primitive output becomes `0xFA00F2AA`. Eight bytes later, the
  environment header overwrites its RGB source, producing `0xFB0000BB`.
- **50 complete paired routine traces** connect actual color -> writer for
  counts 0/1/8, all four palette rows and ordinary/high-bit keys, plus a queue-
  output alias workflow. The alias creates key `0xFA00F200`, segments 0x93/0xB0
  and data words `0x314253AA`/`0xFB000000`, then emits the expected two segment
  commands at the returned cursor while changing the later queue entry.
- Three paired invalid-index prefixes stop at an unmapped first RGB read after
  the primitive header store. They assert no subsequent command/data store;
  they do not qualify complete invalid-index execution or memory safety.
- Independent fresh IDO O2/g3 compilation and MIPS linking reproduce the exact
  complete production slot. ROM checksum, assembly annotation words, symbol
  address, trailing padding and absence of word guards are checked separately.

The new tests add **812 complete paired traces** to Note 970's 898. The complete
module receipt records **1710**: reset 1, append 9, writer 913 and color 787;
the three prefixes are separate. The bounded low-word oracle compares complete
mapped memory, ordered reads/stores, return cursor and saved-register contracts.
It is not a general MIPS emulator or hardware execution.

Receipt: ignored `conker/build/game-queued-segment-color-qualification.json`.
Partial test selections report their actual counts instead of full-corpus credit.

**All 243 combined checks pass in 48.767 seconds, no skips**, including the
complete module, connected cache/child/loader regressions, layout tooling and
Init ownership/bitmap checks. The prior 243-check run passed in 45.620 seconds
before adding the measured receipt; the final run above follows the forced
production rebuild and includes it. These are repeat runs, not 486 tests.

The forced build recompiles only the affected generated source, then pads,
links, regenerates progress and runs the matcher. Existing duplicate
`generated_12D630` recipe warnings remain; no new source warning.

```sh
make -C conker NON_MATCHING=1 --what-if=src/game/generated_139FC0.c build/conker.us.elf progress match-progress -j4
python3 -m unittest tools.tests.test_game_queued_segment_writer -q -f
make tools-check
git diff --check
```

| Complete Slot | Words / Differences | SHA-256 |
| --- | ---: | --- |
| `func_1510CDB8`, C and retail | 42 / 0 | `a1b386a82d28205880c5f04ac0e29057a9f2836f6b607d682b106490da0c2bc4` |
| Queued writer C, unchanged | 44 / 38 | `f3a227545fc8d35dd017430e12f6fd1da0512c5746e400423358eee3a9566feb` |
| Exact reset, unchanged | 4 / 0 | `e81b7668246b58e182518ea12697cbf47014a01b764ea1a2dc2f1e8ce2d55a31` |
| Exact append, unchanged | 19 / 0 | `5ca5af947408d6055c1fdf4ce2c517d915c75c052975430b17056b22969beffb` |

Complete linked Init code (164048 bytes), Init data (17376), Debugger code
(19800) and Game data (189088 / 720 owners) remain raw retail-exact. Their
SHA-256 values remain:

```text
Init code 34372ebc8b2e56b5b6c02c8b88ce33a1558d5d329397fdc6e9e984333df6d4bf
Init data a3d3d56157fd9f9feb00a48a526c50ec51227b5a5afc277aa9a4b765c8fc6239
Debugger f619cd1afa30c26f6b6e91cb597689b52a74e8c072002dbf7b30789e4df0facf
Game data 0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670
```

Fresh matcher: total **3283 / 5463 (60.10%)**, Game **2610 / 4790 (54.49%)**,
Init 492 / 492 and Debugger 181 / 181; zero drift, 2180 differing C functions.
README changes only these aggregate matching rows. Conversion counts and byte
coverage do not change because the placeholder was already counted as C.
Recovery narration stays in working documentation, not README.

## Sibling And Next

Read-only sibling audit finds active `recomp_out/.c` line 820834 already has
the complete original recompiled `func_1510CDB8`, through the returned cursor
at `0x1510CE54`. A scoped host `src`/CMake search finds no named override.
No host source, build, save or frozen Release change is required by this guest
source recovery, and the existing host body is not fresh rendering acceptance.

Next upstream source target: **`func_1510CB10`**, the 170-word palette updater
immediately preceding this emitter. Its retail body writes both RGB tables,
has a per-slot enable gate and a three-channel phase/interpolation path, and
calls `func_150489B0`. Its current DECOMP body is still a zero-return placeholder.
Recover and qualify its actual table/state/callback contracts before claiming
the palette-generation -> color -> segment pipeline is complete.

The full caller `func_151137D4` remains a placeholder and unqualified. Retail
calls color at `0x15113AC8`, then passes the result to writer at `0x15113AD4`.
The bounded leaf connection here does not establish full caller or real
RSP/RDP/natural effect behavior. Staged texture producer recovery and PC
immediate-release stub synchronization remain separate tasks.

- [x] Finish the pending emitter with actual SDK macros and pointer return.
- [x] Match all 42 retail words directly, without guards or profile override.
- [x] Qualify alpha/RGB values, palette aliases and every emitted instruction.
- [x] Connect actual color -> queue writer in normal and alias fixtures.
- [x] Pass all 243 combined checks and retain complete exact Init/Debugger/data.
- [x] Update README aggregate matching rows, keeping narration in docs.
- [ ] Recover/qualify palette updater `func_1510CB10` and its color connection.
- [ ] Recover/qualify full render caller and real RSP/RDP/natural effects.
- [ ] Match queued writer's remaining 38 raw differences separately.
- [ ] Identify/qualify staged texture producer and synchronize pending PC stubs.

No ROM promotion, push or broad Init conversion is included.
