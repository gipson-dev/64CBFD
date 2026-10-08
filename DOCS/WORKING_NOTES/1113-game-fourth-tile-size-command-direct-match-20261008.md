# Game Fourth Tile-Size Command Direct Match

Date: 2026-10-08

## Result

`func_15031E7C` replaces its zero-return placeholder with complete semantic
C. All **83 words / 332 bytes** match retail directly at existing IDO 5.3
`-O2 -g3`, MIPS2/o32. **No stack frame**, guards, padding, instruction
insertion/omission, compiler-profile, Makefile or shared-header changes.
The previous placeholder had **77 real word differences**, now zero.

Production: [generated_5D2C0.c](../../conker/src/game/generated_5D2C0.c).
Retail: [5D2C0.s](../../conker/asm/5D2C0.s), VA `0x15031E7C..0x15031FC8`,
ROM `0x5F32C..0x5F478`.
Continues [Note 1112](1112-game-node-cleanup-dispatcher-direct-match-20261008.md).

## Recovered Contract

1. Read actor+0x2D0; if null, return zero without touching node/list/type/progress.
2. Read node+0x24's container pointer, then its first word as `Gfx *commands`.
   A null list returns zero. The container itself is required, not newly gated.
3. Read the unsigned actor type at+0x84. Type0x55 forces factor1; type0x56
   forces factor0. Both skip source progress and the scale global.
4. Other types read source+8 as binary32. Inclusive `0 <= progress <= 120`
   uses `factor = progress * D_800970DC; factor = 1 - factor`. Out-of-range,
   infinities and quiet NaNs select zero in the bounded numeric model.
5. Scan signed first bytes of eight-byte SDK `Gfx` commands for opcode
   `(s8)G_SETTILESIZE`, **-14 / 0xF2**. Advance past the first three matches;
   leave the index on the **fourth match**, not the following command or last match.
6. Update **only words.w0** of that fourth command to
   `0xF2002000 | (trunc(binary32(binary32(25 * factor) + 2)) & 0xFFF)`.
   All other command first words and every second word remain untouched.
7. Return zero on every path; no calls or private frame are needed.

SDK `Gfx`, `G_SETTILESIZE` and `_SHIFTL` express the actual tile-size first
word without an opaque instruction array or extra full-command write. No
display-list terminator, scan cap, container null gate or recovery policy is
invented. A malformed list remains a required-storage fault in the bounded oracle.
The preserved scale at **0x800970DC** is exactly **0x3C088889**.

## Source Fit

The first complete SDK form already emitted 83 words and the exact GP/scan
topology but had eleven FP register/scheduling differences. A single expression
`1 - progress * scale` made IDO load the one constant before the product.
Splitting the multiplication and subtraction into the two semantic assignments
recovers every FP word directly, including downstream allocation.

SDK `Gfx` indexing matches the retail scaled-index loop. Raw byte indexing
emits a complete 77-word alternative with different loop/address allocation;
it is an ordinary-effect control, not a matching replacement or padded promotion.
O2 without g3 is also raw exact, but production retains its existing profile.

## Qualification

[Driver](https://github.com/gipson-dev/64CBFD-Tools/blob/master/experiments/game_node_tile_candidates.py) and
[seven tests](https://github.com/gipson-dev/64CBFD-Tools/blob/master/tests/test_game_node_tile_match.py):

- Seven pre-install tests pass in **29.428 seconds**, zero skips/errors/failures.
  Strengthened alias/fault checks pass separately in **3.194 seconds**.
- **13,152 selected guest cases**, eight unsigned actor types, **137 float
  bit patterns**, six scan layouts and two SP phases.
- Float patterns include signed zero, small normal/subnormal values, negative
  and maximum finite values, infinities, quiet NaNs, the inclusive120 boundary
  and adjacent representable values around all24 interior truncation thresholds.
- Layouts include adjacent matches, gaps, a late fourth match and a fifth match
  proving that only the fourth is selected. Nonmatching opcode bytes include
  0x00/0x7F/0x80/0xF1/0xF3/0xFF; signed-byte load support is local to this oracle.
- Independent semantic reference agrees with C and retail on defined V0,
  exact ordered reads/stores and every memory byte. Selected guest C/retail
  also agree on all GP/FP registers; saved registers/SP/RA are checked.
- **79 of 83 words** execute. Indices5/11/25/44 are unreachable duplicate
  instructions from branch-likely scheduling, not missing source or padding.
  All83 words are byte-exact, including those duplicates.
- Five lazy fixtures prove the null gates and skipped progress/scale reads.
  Ten required-storage faults plus four missing-sentinel faults preserve
  exact public prefixes and partial effects; no new scan bound is introduced.
- Five valid guest aliases cover node/actor identity, a self-container,
  source/node and source/actor identity, and progress overlapping the selected
  command. Required reads occur before the sole final store.
- **19,728 actual native32 C executions**, all command words/input object
  bytes and the scale unchanged except the selected first word. Independent
  precomputed binary32 expected coordinates are embedded into the native test.
- Native fixtures assert 32-bit pointers, binary32 and eight-byte Gfx layout;
  raw opcode bytes are explicitly seeded for **host endian**. This verifies
  the complete C's byte scan and numeric word result, not native big-endian
  graphics-runtime handling. Full FCSR, hardware and PC-port/rendering are not claimed.
- **12 source/profile controls / 960 ordinary executions**, five raw exact
  forms. Other forms qualify return/public effects, not all GP/FP or read order.
- Four compiled effective negatives catch third-match selection, incorrect
  default factor, inverted factor arithmetic and wrong coordinate multiplier.
- Copied complete owner preserves **39 other functions**, pools and
  relocations, with zero strict diagnostics. Target bytes/relocations equal
  the isolated SDK body. Actual padder yields332 bytes without padding/data.
  Scale HI/LO remains symbolic under independent entry and carry-boundary rebases.

All **73 installed tile/cleanup/action/attachment/lookup/key-fit/resolver
regression tests pass in 433.831 seconds**, zero skips/errors/failures. Both
actual matrix-wrapper connections and existing alias/home/native/owner/padder
gates remain green. Tools, Python syntax, CLI and whitespace checks pass.
Documentation validation covers **95 documents / 4,090 relative links / zero
broken links**. No full FCSR/callee/hardware/graphics-runtime/PC-port claim.

The initial oracle run lacked `LB`; local signed-byte execution support was
added and tested by the varied opcode scan fixtures. No production workaround
or shared oracle refactor was introduced.

```sh
make -C conker -j4 build/conker.us.elf progress.csv
python3 -m unittest tools.tests.test_game_node_tile_match tools.tests.test_game_node_cleanup_match tools.tests.test_game_node_action_match tools.tests.test_game_attachment_copy_match tools.tests.test_game_attachment_progress_match tools.tests.test_game_matrix_parent_lookup_match tools.tests.test_game_matrix_pair_resolver_key_fit tools.tests.test_game_matrix_pair_resolver_recovery -v
make tools-check
```

## Linked Audit

Against Note1112's authoritative `conker/build/game-node-cleanup-test/after.json`:

- **6,058 linked symbols / 6,042 retail slots / sixteen overflow symbols**.
- Only `func_15031E7C` changes; **6,057 other symbol bodies / 6,041 other
  retail slots** unchanged, all addresses/extents unchanged.
- `.init`, `.init_data`, `.debugger`, `.game_data` unchanged.
- All **720 Game-data owners / 189,088 bytes** exact; SHA256
  `0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.
- All **11,063 guards** and conversion CSV hash unchanged. Target has no guards.
- Matching total **3,370/5,467 (61.64%)**, Game **2,697/4,794 (56.26%)**,
  **2,097 different / zero drift**. Conversion counts/bytes do not change
  because this placeholder was already counted as C.
- Root README changes only aggregate matching rows; thumbnails are preserved.

The normal ELF/progress rebuild succeeds. Existing duplicate `generated_12D630`
recipe warnings remain; target isolated/copied-owner compilation is clean,
not a whole-repository warning-free-build claim.

Ignored receipts: `conker/build/game-node-tile-test/{slot,guest,gates,controls,native,owner,padder,installed,audit}.json`.
Authoritative next baseline: **`conker/build/game-node-tile-test/after.json`**.

## Next Dispatcher

Next local placeholder is **`func_15031FC8`**, full **1,148 words / 4,592 bytes**,
frame **0x48**, VA `0x15031FC8..0x150331B8`, ROM `0x5F478..0x60668`.
It has **1,119 placeholder differences** and two call sites:
`func_1503F5B8` at 0x150330DC and `func_1505E060` at 0x1503311C.

Read-only `next-dispatcher-audit.py` / `next-dispatcher.json` inventory all
seven original tables and group their exact target labels/indices:

| Table | Entries |
| --- | ---: |
| 0x800970E0 | 35 |
| 0x8009716C | 43 |
| 0x80097218 | 29 |
| 0x8009728C | 16 |
| 0x800972CC | 463 |
| 0x80097A08 | 78 |
| 0x80097B40 | 10 |
| Total | **674** |

All targets lie inside the complete dispatcher slot and retain original
Game-data ownership. This is **static inventory, not semantic recovery or execution**.

1. Partition actor/model/type and node-action dispatch from the original seven
   table groups and equality branches; recover the complete selection body.
2. Preserve the initial required actor+0x2D0 read before node attachment null
   gate, incoming node home and private choice/source/flag lifetimes around
   both calls; the tail copies progress and conditionally copies state halfwords,
   then applies the inclusive end-minus-one clamp.
3. Measure the complete copied owner's pools before any table-anchor binding.
   Existing useful tables occupy412 packed bytes, but this dispatcher's first
   original table starts at anchor+416: the **four-byte scalar at0x800970DC**
   intervenes. Do not assume the prior end-alignment word will persist between
   newly emitted tables, change original data, or mask a wrong pool addend.
4. Qualify all dispatch routes, store/callback-induced rereads, halfword/float
   boundaries, private homes and actual owner/padder/relocations before installation.

The broader Game goal stays active. Resolver C84/frame0x20/40 differences,
matrix wrapper/basis/translator/sampler and complete callee/hardware/PC-port
acceptance remain open. No sibling Release, save, runtime or push action.
