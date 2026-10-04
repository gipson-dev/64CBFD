# Game Curve Update Direct Match And Data Placement Gate

Date: 2026-10-04. Starting HEAD: `a3e59dbe`.

## Result And Boundary

`func_150E7C9C` now has its semantic update body instead of a zero-return
placeholder. All **212 words / 848 bytes** emit directly from C and match
retail, with the original **0xA8 / 168-byte frame** and zero instruction
guards. Its builder `func_150E7994` still matches all 194 words directly.

This is an instruction-exact recovery, **not current guest-runtime acceptance**.
A physical data check found the pan coefficient displaced in the linked
Game-data section. Fixing/qualifying that layout is the next priority before
another conversion batch; see the measured gate below.

## Callback And Payload Contract

Retail reference: `conker/asm/113D60.s`, `0x150E7C9C..0x150E7FEC`,
ROM `0x11514C..0x11549C`. Recovered signature is `void func_150E7C9C(u8 *record)`.

The retail table `D_8008A4E8` places this callback at index 16, address
`0x8008A528`, ROM `0x22EFE8`; see `conker/asm/data/22EF80.rodata.s`.
The builder requests callback index 16 through `func_151491F4`.
`func_15149264` dispatches that table using record byte +0x11 and subsequently
removes records whose signed lifetime at +0xE is negative. These are retail
connectivity references, not proof that the current linked table is correctly
placed or that the entire dispatch path has runtime acceptance.

The twelve-byte payload at record +0x28 is now confirmed as a float rate,
float progress, signed count and signed cursor. Rename its formerly unknown
`fieldA` to `cursor` in the shared type, builder and builder fixtures; size
and offsets are unchanged. Point pairs begin sixteen bytes after the payload,
at record +0x38; the intervening four bytes remain untouched.

The update performs:

1. `progress += value * D_800BE9A4` once, before the loop.
2. While progress is **strictly greater than one** and cursor differs from
   count, snapshot the current X/Y pair before any random callback.
3. Sample a float, integer bit for flag 0x04, integer bit for flag 0x02,
   then another float. Preserve that order, including high-bit integer words.
4. Call the positioned helper with scale `sample * 12 + 30`, ID 300,
   combined flags, unsigned-converted duration `sample * 25 + 100`, opacity
   255, sizes 1/255, null pair, mode zero, record byte +0xC and record byte +1.
   Its result is ignored.
5. Submit sound 0x360, volume 0x7FFF, byte pan from the snapshotted local X
   times the retail coefficient plus 64, and zero remaining arguments.
6. Reload callback-visible progress/cursor, subtract one, and increment the
   signed cursor. Recheck current progress/count/cursor for the next point.
7. Set signed record lifetime at +0xE to -1 when cursor is at least count,
   even if no emission occurred during this update.

No new null, count or cursor sanitization gate is inserted. The builder's
valid record contract supplies storage; tests do not intentionally execute
out-of-bounds cursor/count combinations with an active emission loop.

## Compiler And Literal Recovery

The initial separate point cursor and mutable-global coefficient shape
exceeded the retail slot by five words. Header-relative point indexing reduced
that to two, but the compiler retained an extra saved register for the global
address. Array/struct scratch and while/do shapes did not resolve it.

The pan coefficient is actually a retail literal pool word:
`D_800A1350`, ROM `0x245E10`, bits **0x3EDCEE77** (`0.4315068424f`).
Recovering the literal removes the loop-invariant global address. The existing
Makefile `RETAIL_RODATA_SYMBOL` mechanism binds this slice's single generated
float pool to the original symbol, without replacing instructions or data.
An independent build checks the pool bytes against pristine ROM and confirms
there is no second nonzero pool value requiring another placement decision.

A three-float scratch allocation restores the original frame extent and
X/Y stack offsets. Only its first two floats are initialized/read; the third
stays unwritten. This is a compatible C storage shape proven by emitted code,
not proof that the original source declared the same three-element array or
that a Z coordinate exists in this two-dimensional emitter contract.

## Tests And Final Link

New suite: `tools/tests/test_game_curve_record_update.py` (six tests).

- Strict progress threshold, signed terminal comparisons, NaN progress with
  no emission, and already-exhausted infinite progress.
- All four flag combinations, multi-point exhaustion, one-time accumulation,
  argument forwarding, trace `FIIFES` per point and cursor 32766 -> 32767.
- Fractional casts in the valid conversion range, point snapshots before
  mutation, byte metadata reloads and state changes during helper/sound calls.
- The actual positioned helper: mutating its copied descriptor does not
  change the update's local position used by sound.
- The actual builder -> update -> positioned-helper chain, including all
  four generated points and terminal lifetime. Other dependencies are fixtures.
- A warning-clean independent IDO O2 build compares all 212 words to pristine
  retail and checks the single literal's value and reference address.

Host arithmetic uses the existing freestanding 32-bit SSE harness, no FMA and
stack realignment. These fixtures do not simulate FPCSR exception behavior,
invalid float-to-integer inputs, arbitrary corrupted records, hardware or
whole-game visuals. The independent MIPS word comparison includes the complete
retail unsigned-conversion/FPCSR sequences, not merely normal-input shortcuts.

```sh
python3 -m unittest tools.tests.test_game_curve_record_update tools.tests.test_game_random_curve_record tools.tests.test_game_random_edge_emitter tools.tests.test_game_positioned_emitter_descriptor tools.tests.test_game_random_dispatch tools.tests.test_game_fixed_random_parameters -q -f
make -C conker NON_MATCHING=1 build/conker.us.elf progress match-progress -j4
```

All **32 tests pass in 4.482 seconds**, no skips. Makefile dependencies caused
a broader rebuild, which completed and linked successfully; warnings came
from other unchanged source slices. Fresh ELF measurements show entries
`0x150E7C9C` and `0x150E7FEC`, 212 body / 212 slot words, original 168-byte
frame, zero different word positions and zero guard rows. Builder remains
194 / 194 words, 200-byte frame, zero differences/guards.

| Section | Byte-exact / C functions | Address drift | Still different |
| --- | ---: | ---: | ---: |
| Total | 3,278 / 5,463 (60.00%) | 0 | 2,185 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 2,605 / 4,790 (54.38%) | 0 | 2,185 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

Conversion counts/bytes are unchanged: this routine was already represented
by a C placeholder. README updates are limited to aggregate matching rows.
No Init ownership change, full Init decoder corpus rerun, sibling build,
Release change, ROM promotion or push.

## Measured Game-Data Gate

The matcher compares function instruction words. Its zero address-drift
column does **not** prove the physical placement of `.game_data` contents.

Fresh `objdump -s` reads from the final linked ELF show:

| Physical Address | Linked Word | Meaning |
| --- | --- | --- |
| 0x800A1350 | 0x4675E800 | Wrong word at the instruction's retail load address |
| 0x800A2910 | 0x3EDCEE77 | Correct coefficient, displaced by 0x15C0 bytes |

The map places `build/asm/data/245C90.rodata.s.o` at **0x800A2790**;
retail's owner starts at **0x800A11D0**. Its coefficient is +0x180 within the
owner. `undefined_syms_auto.txt` still defines `D_800A1350 = 0x800A1350`.
Thus correct instruction references and correct input-object data can coexist
with a wrong physical load in the current linked artifact.

No Game-data owner source was edited during this recovery. This turn has not
compared a disposable previous-HEAD link, so the issue's introduction point
is **not established**. Do not call the layout correct, or claim guest behavior
from the independent pool/host tests.

## Handoff

- [x] Recover the callback, cursor meaning and builder/table connectivity.
- [x] Match all 212 instruction words directly and preserve the builder match.
- [x] Qualify focused host contracts and the independent retail literal pool.
- [x] Check final physical coefficient placement; record the failed data gate.
- [ ] Audit current Game data/rodata owner order, spans and alignment against
  retail, including a bounded previous-HEAD comparison where needed.
- [ ] Correct physical placement without replacing unmatched code or changing
  frozen sibling artifacts. Recheck data bytes, table entries and all matching
  counts before any guest/runtime claim or another conversion batch.
- [ ] Once that gate is resolved, inspect adjacent retained assembly
  `func_150E7FEC` and its callers for the next semantic recovery.
