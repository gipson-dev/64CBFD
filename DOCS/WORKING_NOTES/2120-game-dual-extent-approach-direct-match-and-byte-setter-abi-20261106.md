# Dual-extent approach direct match and byte setter ABI

Date: 2026-11-06. Continue the 80% matching goal from consumer
`c4f979593ea5a3159193adb3d6ff19fdf7686291` and mounted tools
`ac223bdccd448678b42d024f0e21168870e5829b`.
This completes the next target in
[Note 2119](2119-game-dual-point-weighted-motion-match-and-private-weight-lifetime-20261106.md).

## Installed result

`func_1514A380`, owner `generated_176A00`, emits its complete 70-word,
280-byte retail body directly from C: VA `0x1514A380..0x1514A498`,
ROM `0x177830..0x177948`, frame `0x20`, saved RA at SP+`0x1C`.
All nine relocations match. No new guards or compiler profile are needed.
The source uses descriptive names and the actual SDK `struct171` setter type.

The callback approaches extent X at `0x2C` toward target `0x118`, then
independently approaches extent Y at `0x30` toward target `0x128`.
Both use the retail single-precision factor `0x3F333333` (about 0.7).
Each axis sets its byte flag at `0x74` (masks 2 and 8) only when the
ordered comparison `target * 0x3F733333 < updatedExtent` succeeds.
Already flagged axes skip their update. Equality and unordered NaN comparisons
remain incomplete. Failure of X does not suppress Y. The callback returns 1
even when either axis is incomplete.

When both axes complete, it calls
`func_1513F680(owner, owner[0x70], 4, owner[0x72], owner[0x73])`.
The fifth unsigned byte travels through SP+`0x10`; the existing setter writes
bytes `0x70..0x73`. The original registry is `D_80089D60[5]`, whose sole aligned
retail pointer is ROM `0x22E834`. Selecting slot 4 hands off to `func_1514A19C`.
The SDK prefix is `0x80` bytes and labels `0x74` as a word, but this callback
uses LBU/SB there. The recovered explicit byte view preserves that distinction
and the extended owner tail, whose last float ends at `0x12C`.

## Qualification

Run from the prepared consumer root:

```sh
python3 -m unittest tools.tests.test_game_dual_extent_approach_match -v
```

All seven checks pass before installation and in both installed tools
configurations. The dirty standalone sibling is exercised through an ignored
overlay: its actual compiler fixture, object parser, timing/FP engine and
native32 command builder are selected and fingerprinted. Only the five new
modules are overlaid; mounted fallbacks for absent dependencies remain explicit.
The sibling's six tracked edits and 2,428 untracked files are preserved.

- **13,312 cases per guest body**, original/raw/padded, check an independent
  rounded reference, all 256 flag values, independent axes, signed zero,
  subnormals, infinities, ordered NaNs, return 1 and saved-register ABI.
  Public paths cover 68 words; the two unreachable duplicate zero assignments
  at offsets `0x7C` and `0xE4` remain part of the complete 70-word literal match.
- **2,400 constant/owner alias cases per body** exercise all 75 aligned owner
  offsets and both stack phases. Five private terminal comparisons and
  **83 own-access fault prefixes** preserve literal instruction state.
  These bounded guest probes do not claim portable C fault semantics.
- The complete original **195-word parent** executes 64 success/skip cases per
  body, covering 47 parent words. The connected **16-word original setter**
  executes all its words, including the fifth-argument byte load. A false-return
  control reaches the parent's cleanup call; its body remains opaque.
- **Nine independent GNU links** cover all four HI16/LO16 pairs, carry
  boundaries and the helper R26 binding; 192 rebased cases per body pass.
- **12,288 native32 positive calls** run direct and compatible callback paths
  at O0/O2/O3 with SDK headers, real float storage, independently chosen constant
  aliases, sentinels and UBSan. Seven effective controls reject a false return,
  short-circuited Y, accepted equality/NaNs, wrong Y target, wrong next selector
  and wrong fifth argument. NaN results are compared by class, not payload/FCSR.
- Fail-closed checks reject 280 raw-byte corruptions, nine altered bindings,
  five whole-image corruptions and the previous zero-return stub.

Both tools smoke checks are fresh. Prior shared progress, word-guard and PC16
regression receipts are reused only after verifying unchanged helper hashes;
those broad suites are not represented as freshly run.

## Production closure

The 99 frozen inputs cover the original owner/assembly, headers, caller,
registry, build inputs and prior image. All **35 raw and padded neighboring
functions**, compact allocated pools/register metadata and padded pools remain
unchanged. Adding the real SDK header/prototype does not disturb the preceding
weighted-motion match. Existing Warning 712 at the unrelated `func_1514BF50`
call is unchanged apart from its shifted source line.

The independent whole-ELF prediction accounts for **325 changed bytes**:
the target slot, its symbol extent from 12 to 280, and three closed GNU
hash-chain permutations involving eight named symbol records and their complete
name blocks. Every definition and byte position is checked; **zero bytes are
excluded**. All 6,052 function addresses remain fixed and this is the only
changed function body. All **189,088 protected data bytes in 720 owners** match.

Actual `make -C conker -j4 build/conker.us.elf progress.csv` equals that exact
prediction. `make -C conker all` retains the expected checksum exit 2 because
the wider decomp image remains unmatched. The fresh `match-progress` recount is:

| Section | Byte-exact | Drift | Still different |
| --- | ---: | ---: | ---: |
| Total | 4,189 / 5,512 (76.00%) | 0 | 1,323 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 3,516 / 4,839 (72.66%) | 0 | 1,323 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

Conversion rows and guard CSV bytes are unchanged. There are **221 more**
matches to the current 4,410-function threshold for 80%.

- ELF SHA-256: `3d69279f0ee7f0d34f39a9a60f5d0a3aa5070fcf05f9be994af27770ec5e7134`.
- Owner SHA-256: `3236c6b2560f8b3584f53ad963b8b7115a8cb7344cb91fedde9e1511e475b498`.
- Code binary SHA-256: `1d7bccbc08d95a18ee2f2c3f9e515effb8b13d50fa2b903573ccd15faecc0257`.
- Unchanged guards: `b53721d727660eca66ed2771ba8fd8597642b08a123168033628a26ff92fd46b`.

Ignored evidence is under `conker/build/game-dual-extent-approach-1514A380-match/`:
the screen/frozen inputs, exact owner/image predictions, per-gate receipts,
dual-copy installed/helper manifests, production logs and scoped graph audit.
Graphify receives a scoped refresh with old-node retention accounting; this is
not a full-corpus re-extraction. The package/skill version warning is unchanged.

## Review and next work

Codex is the only writer. Claude calls attempted/completed: **0/0**; literal
direct compilation and local discriminating tests settled the routine.
Tools are committed before the consumer pin, source, aggregate README rows and
this note's concise indexes. No push, tool upgrade or host-port change is part
of this checkpoint. No emulator/gameplay acceptance is claimed.

Next: `func_1515A974` in `generated_185560`, a 68-word callback with the
original `0x88` frame, an embedded `0x2C`-byte payload and factory/copy calls.
Its current placeholder is uncredited. Confirm the unsigned byte selector,
table registration, retained private bytes, complete factory ABI and live
owner reloads before choosing C types. Keep handwritten `func_150A76F0` in its
separate assembly workstream and preserve the earlier documented boundaries.
The 80% goal remains active.
