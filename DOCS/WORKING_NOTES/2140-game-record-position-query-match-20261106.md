# Record-position query matched with two commutative address guards

Date: 2026-11-06. Continues [Note 2139](2139-game-actor-state-command-selector-match-20261106.md)
from consumer `f6555d88abc5207eff9f7f54134af9aee1b60d62` and tools
`fa41f55a5a1932668de1b845f19ca15922a01848`, toward the active80% goal.

## Recovered query, interface and live state

`func_150A3194` in `conker/src/game/generated_CDE80.c` now matches all
**72 words / 288 bytes after two operand-order guards**. Raw C remains two
words different. VA `0x150A3194..0x150A32B4`, ROM `0xD0644..0xD0764`, no
alignment tail. The default O2/g3/MIPS2/O32 profile is unchanged. All27 compact
and padded neighbors, five relocation bindings, original0x378-byte frame,
S0..S6/RA lifetimes and every floating-point instruction remain fixed.

The five arguments are full-word kind/subtype filters and signed32 x/y/z
coordinates; z arrives in the fifth incoming home. A real **struct127 query,
812 bytes**, receives seven float32 fields: x/y/z, old_x/old_y/old_z and
unk180=y. The fields are initialized once, even for an empty table. The rest
of the object is not zeroed. It remains one escaped object across provider
calls, so legitimate provider mutations must survive subsequent iterations.

The unsigned view of D_800D3094 bounds a record counter, while a separate byte
offset advances by52. Each iteration reloads the D_800D3098 base pointer.
Only a zero status byte, flags>>2 equal to the full kind, and subtype byte
equal to the full subtype invoke func_150A1DA0(query,address,0). Every nonzero
provider result continues; the first zero returns the current base plus that
offset. The base is reloaded after success too, preserving callback changes.
The count reload after failed/filtered records preserves growth and shrinkage.

The provider already takes the record address as s32. Expressing its address
as offset+(s32)D_800D3098 recovers the original integer expression and avoids
the first draft's common-pointer-address reuse. Native32 uses bounded tables
whose pointer representations plus offsets fit signed32. Arbitrary guest
pointer arithmetic and unbounded counts are outside that portable C claim.

## Genuine frame recovery and two derived guards

The first complete draft had72 words/frame888 but27 differences. Placing the
query first gave SP+0x4C; placing it last displaced it in the other direction.
The ordinary declaration order **u32 index, struct127 query, s32 offset** gives
the original **SP+0x48** query and all seven store homes. Integer address
expressions recover the original register use. No fake padding or unused
locals were introduced. Register hints and commutative source operand order
changes did not improve the final compiler output and need not be repeated.

The full raw body SHA and all five bindings are checked before deriving only
these changes:

| Offset | Raw | Guarded | Derivation |
| --- | --- | --- | --- |
| 0xB4 | 0x00702821 | 0x02032821 | a1=v1+s0 becomes a1=s0+v1 |
| 0xD8 | 0x01501021 | 0x020A1021 | v0=t2+s0 becomes v0=s0+t2 |

Both are nontrapping ADDU instructions. The normalizer swaps only rs/rt bits;
opcode, destination, operation, timing and every other bit remain fixed.
Neither word has a relocation. The retail words are an independent oracle,
not derivation inputs. All32-bit operand values retain the same modulo32 sum,
and raw/normalized/retail guest executions agree in their complete literal
states. The manifest appends exactly two expected-word rows, with no insertion,
omission or relocation changes, preserving the inherited file as a byte prefix.

The raw owner gains only recovered S6 use: .reginfo and .options GPR masks
A33FFFFE to A37FFFFE. Other raw loaded pools and register metadata stay fixed;
all padded pools/register metadata are identical to the predecessor. Discarded
raw debug/symbol data is not claimed byte-identical.

## Qualification

Eight methods pass before and after installation in both tools configurations.
The first completed mounted run is banked with its eight fresh method receipts
and exact module/helper fingerprints. The sibling runs the new modules through
a disposable overlay using its own existing helpers; its dirty files are
preserved.28 core snapshots and80 include-header snapshots remain checked.

- **1,690 guest cases per body**, across raw C, normalized C and retail, cover
  all256 status/flags/subtype bytes, full-word filters/unsigned counts,
  signed32-to-float32 rounding boundaries, first success, live tables/counts
  and mutable queries. Every reachable root word is visited; duplicate count
  load word55 is unreachable and remains emitted.
- **192 alias/home cases per body** cover query/table, base/count globals and
  overwritten incoming homes. **187 fired access cuts** compare all three
  literal states. Full812-byte guest query observations retain seeded private
  bytes; portable native code checks only initialized fields.
- **56 connected cases per body** execute the original401-word provider as
  applicable for box geometry2 and stationary-plane geometry3. Independent
  references check box boundaries and stationary-plane rejection. Observed
  query reads are exactly offsets14,18,1C,2C,30,34,180. The literal zero third
  argument avoids the optional E4 read. Other geometry modes, full provider C
  reconstruction and hardware/FCSR acceptance are not claimed. The provider's
  current C zero-return placeholder is never used as an independent oracle.
- **128 caller cases per body** cover all four JALs: ROM AD4EC,AD528,B4154,
  C7D2C. Original windows have15,13,19,23 words, including the complete19-word
  table wrapper. Float truncation, signed16 table coordinates, all five
  arguments, pointer returns, null branches and the record-index/-1 consumer
  are checked. Saved integer registers, GP, SP and FP stay fixed. The large
  parent routines remain outside these windows' acceptance claims.
- **Six GNU links**, three layouts and36 cases per body qualify all five
  bindings, signed-low16 carries, JAL regions and standalone tails.
- SDK native32 at **O0/O2/O3 with UBSan** runs **1,690 cases per profile**.
  Actor/record/pointer sizes and query offsets have compile-time ABI checks.
  All eight controls fire: stride, kind, subtype, old-z field, narrowed x,
  inverted provider result, cached count and cached base. High-count positive
  fixtures succeed on the first record; negative controls are bounded to eight
  records so their rejection does not depend on invalid memory access.
- **288 byte corruptions, five binding corruptions and six full-image
  corruptions** fail closed. The zero-return stub and initial query layouts are
  rejected. Both tools copies pass fresh smoke checks; three unchanged shared
  regression receipts are fingerprinted and explicitly reused.

```sh
python3 -m unittest tools.tests.test_game_record_position_query_match -v
make -C conker -o retail_word_patches.us.csv -o Makefile --output-sync=target -j4 build/conker.us.elf progress.csv
make -C conker -o retail_word_patches.us.csv -o Makefile all
make -C conker -o retail_word_patches.us.csv -o Makefile match-progress NON_MATCHING=1
```

## Production and resume boundary

Only generated_CDE80.c recompiles, once, with no C diagnostics or profile
changes. Actual owner and ELF equal independent predictions: **220 changed
ELF bytes**, confined to the body and symbol size12 to288, with **zero excluded
ranges**. All **6,052 function addresses**, conversion rows, progress.csv and
**189,088 protected Game bytes / 720 owners** stay fixed. The existing duplicate
generated_12D630 recipe warning and expected unfinished-image checksum failure
remain. No live hardware or gameplay was exercised.

| Section | Byte-exact | Drift | Still different |
| --- | ---: | ---: | ---: |
| Total | 4,209 / 5,512 (76.36%) | 0 | 1,303 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 3,536 / 4,839 (73.07%) | 0 | 1,303 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

**201 more** matches reach the current4,410 threshold for80%.

- ELF: `f045bea0e577eb05309cbb9b1d5d41dd750e0f0f0e01c479a94deb9d0888d13b`.
- Owner: `ae2ec62ef1aac5e42b71aae025bc6accfefd76e7a569a7b0a35afc39da798864`.
- Code binary: `d8ff1dd52cf4f18c2a8ede8abbbae82214b8c8f56597089d9be6ac6dee4b0115`.
- Guard CSV with two derived rows: `10fbf973fdc0c43c675645f651ed61592f4d5e6d8c5613080fecd3a989411af8`.
- Unchanged Makefile: `509371c33a6266fa242b20212c16cf42d4b61575a8773b053bfad43d0778ae1b`.

Evidence: `conker/build/game-record-position-query-150A3194-match/`.
Tools commit precedes source/guards/docs/pin. Graphify is refreshed with old-node
retention checks, without claiming full-corpus extraction. Root README receives
aggregate rows only. Claude calls: zero; local source/ABI evidence suffices.

Next: **func_15133588**, generated_15F680,72 words/frame0x30, VA
0x15133588..0x151336A8, ROM0x160A38..0x160B58. Recover its byte-event ABI,
0x1B/type0x22 helper path, event0x2D pair toggles, event0 clear, and nullable
callback-table dispatch. Inspect callers before deciding the return contract.
It remains uninstalled/uncredited. Preserve handwritten func_150A6FA0 and
func_150A76F0, private inputs/saves, unrelated work and frozen host Release.
Keep the complete80% matching goal active.
