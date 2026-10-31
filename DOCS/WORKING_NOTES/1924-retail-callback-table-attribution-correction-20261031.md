# Retail callback table attribution correction

2026-10-31. Correct the caller attribution recorded in Notes 1922 and 1923.
The recovered C, target instructions, relocations, guards and production ELF
are unchanged. Exact C remains **4,000/5,506 (72.65%)**, Game
**3,327/4,833 (68.84%)**, with zero drift and **130** more needed for 75%.
This correction does not award another matching function.

## Physical mapping and corrected tables

The earlier attribution used a Game-data ROM start of `0x2274D0`, which was
`0x110` too early. The authoritative layout in `conker.us.yaml` and
`load_game_data_layout` starts at ROM **`0x2275E0`**, VA **`0x80082B20`**.
Both oracles now derive pointer VAs from that layout and check the physical
retail pointer before constructing their caller fixture.

| Target | Pointer ROM | Pointer VA | Actual table slot |
| --- | --- | --- | --- |
| `func_15073B38` | `0x22B0E4` | `0x80086624` | `D_800863FC[138]` (`0x8A`) |
| `func_151638E0` | `0x22FBF0` | `0x8008B130` | `D_8008B0F0[16]` |

The prior `D_800863FC[206]` and `D_8008B208[14]` attributions are invalid.
The six-word command-dispatch window for the packed attached-state decoder
remains the correct window; it now dispatches through the physical slot 138.

## Actual sampled-byte caller and result contract

The sampled-byte callback is called by **`func_151603FC`**, whose original
41 words occupy ROM `0x18D8AC..0x18D950`, VA `0x151603FC..0x151604A0`.
It reads the signed callback selector at owner+0xF and calls
`D_8008B0F0[selector]` with the owner pointer. This caller consumes the result:
returning 1 keeps the owner alive when the timer gate permits the callback;
returning zero causes `func_1516972C(owner)`.

The corrected suite executes 48 callback cases and two timer-expiry cases.
The timer-expiry path skips the callback and invokes the free helper. Forty
of the 41 caller words are reachable while this target returns 1; the other
word is the zero-result assignment. An independent target-return-zero control
exercises that path and confirms that it frees the owner. The free helper is
an explicit ABI hook, not a recovered helper implementation.

The previous 23-word `func_15161804` fixture and claim that this target's result
was ignored do not qualify its actual caller. Those old receipts remain
historical and are superseded by this correction. The callback's original
return value 1 was already recovered and remains unchanged in C and machine code.

## Revalidation and preservation

- Both targets pass eight fresh tests in both tools copies: **32 target tests**
  total, plus both shared tools checks. The corrected physical table proof is
  part of each guest suite. All existing native and effective semantic controls
  are rerun; no compiler/oracle failure is accepted as a semantic witness.
- The sampled-byte suite runs against the current production inputs. The older
  packed-decoder suite runs against its complete recorded checkpoint: three
  files in the owned Linux compiler cache are temporarily restored to that
  checkpoint, then restored to current bytes in `finally`. This avoids excluding
  the later sampled-byte source/object/image changes from its old image audit.
  All 17,354 current inputs are checked before and after the fixture, and the
  Windows production tree is untouched by that temporary cache fixture.
- The production ELF remains byte-for-byte identical at SHA-256
  `8c4b9914475e824e2d55b072ba7cba66b551b586d751835dc8dc84903deee91b`.
  All source files, compiler objects, function bodies/addresses, layout and guard
  manifests, and protected Game data remain unchanged by this correction.
- Existing bounded FP qualifications remain explicit: the sampled-byte guest
  model is nontrapping round-to-nearest without full arithmetic exception flags
  or full FCSR modeling; native tests use written scalars and defined conversions.
- Existing unrelated edits and the older tools mirror's inherited dirty work
  are retained. Only the two owned oracle/test pairs change in that mirror.
  No push or host-port/Release changes are included.

Tools correction commit: `44366b252284e26208c88237aa1166b5b1a3ed88`.
New correction receipts are under ignored
`conker/build/game-sampled-record-byte-151638E0-caller-correction/`, with fresh
test receipts retained in each target's original build directory. Earlier
attribution receipts are not reused as acceptance evidence.

The scoped graph refresh updates the corrected validation metadata for both
functions. Future callback attribution must use the physical ROM/VA layout;
inserting a target into a synthetic table alone does not establish its retail slot.
