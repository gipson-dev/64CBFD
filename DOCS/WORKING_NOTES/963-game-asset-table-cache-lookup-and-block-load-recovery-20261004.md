# Game Asset Table Cache, Lookup And Block Load Recovery

Date: 2026-10-04. Starting HEAD: `d13d95be`.

Follow-up: [Note 993](993-game-block-loader-direct-output-size-and-frame-match-20261005.md)
directly matches all 86 block-loader words with the retail 0x30 frame on
2026-10-05. The original recovery measurements below remain historical;
cache installer and cached lookup still differ.

## Decision

Finish the in-progress resource-loading recoveries following
[Note 962](962-game-variadic-resource-loader-and-offset-relocation-recovery-20261004.md).
Replace three already-counted C placeholders with semantic bodies. All fit
their original slots without new word guards, compiler overrides, data owners
or address changes. They remain non-matching; fitting is not byte matching.
The requested remaining Init assessment is separately refreshed in
[Note 964](964-init-remaining-assembly-current-conversion-decisions-20261004.md).

| Function | C body / retail slot words | C / retail frame | Raw differing words |
| --- | ---: | ---: | ---: |
| `func_1502AB04` cache installer | 87 / 97 | 0x20 / 0x28 | 93 |
| `func_1502AC88` cached table lookup | 158 / 159 | 0xA0 / 0xA0 | 156 |
| `func_1502B350` block loader | 77 / 86 | 0x38 / 0x30 | 78 |

## Recovered Contracts

`D_800C3D68` is a sixteen-entry array of sixteen-byte records: address,
generation, offset and descriptor. `D_800C3E58` aliases its last element,
not another allocation. Production C uses one array declaration. Generation
counter `D_800C3D60` retains its established symbol; no new data is defined.

The installer shifts surviving records with original `bcopy`, then consumes
the supplied word pairs. Counts 1 through 16 are qualified; count sixteen
still calls `bcopy` with zero length. Count zero neither copies nor reads the
pair pointer. Address and generation preserve full unsigned bits, including
address wrap. The bounded alias fixture checks input reads occur after the
shift. Negative or greater-than-sixteen counts remain outside qualification;
no protective clamp or new behavior was invented.

Lookup forms `(base + (u32)index * 8) | 0x80000000` and finds the first matching
record. A hit snapshots the complete record, shifts only following entries,
appends to index fifteen, stamps the current generation, writes the descriptor
and then reads the return offset. This ordering matters when the output aliases
that offset. Hits do not increment the counter or perform DMA.

A miss increments generation before DMA. The destination is sixteen-byte
aligned; source is `key & 0x7FFFFFF0`, size is `((key & 0xE) + 31) & ~15`.
The pair pointer adds the low four key bits. Offset is captured before the
descriptor-output write and actual installer call. The installer receives the
fresh generation after DMA/output effects and inserts two pairs for key/key+8.
Tests cover word-aligned low offsets 0/4/8/12, signed index bits, clock/address
wrap, DMA mutation, output/cache aliases, all hit positions and duplicate keys.
They do not qualify unaligned guest word loads or a NULL output pointer.

The block loader allocates the even-rounded low twenty-eight descriptor bits,
then DMAs a separately sixteen-rounded size. First allocation failure returns
NULL without changing the size output. Only masked mode `0x10000000` selects
decompression; bit 31 does not change that selection. Expanded size masks bit
31 of the fetched first word, is published before the second allocation, and
must be in 1..999999. Rejection or second allocation failure frees the compressed
temporary and returns NULL with final size zero.

A successful second allocation uses fresh `D_8003809C` for `func_10006240`.
Decoder return bits become final size after the temporary free. A non-NULL
expanded allocation is returned even if decoding reports zero or a negative
size; no extra validation or free-result path is added. Tests check allocation
arguments, header boundaries, exact mode flags, output/header aliases, scratch
mutation, free callback mutation and operation order. The DMA callback result
is ignored, as in retail.

## Verification

Fourteen new tests execute the actual extracted production C bodies in strict
32-bit host fixtures. One connects actual cache lookup, installer, plain block
load, variadic loader and offset relocation across a miss and a hit. DMA,
allocation/free and decompressor implementations are fixtures, not guest hardware
execution. Constructor connections already qualified in Note 962 are retained
as separate bounded tests, not claimed as a newly unified all-body pipeline.

An independent IDO O2/g3 compilation and MIPS link reproduce the three complete
production slots including zero padding. The test records the internal-call
relocation explicitly; it does not normalize arbitrary instruction differences.
Full padded slot SHA-256:

| Function | SHA-256 |
| --- | --- |
| `func_1502AB04` | `9411056ee2483732bfd3b404b7ab27b514a0af4c614b62c554dbe125f1b0719a` |
| `func_1502AC88` | `1bb0909b45c22e6029c8100583e55835d0cea88a3a28efe38ba65524a7f2ca28` |
| `func_1502B350` | `17346d32c5e8ee8010b24eaf718d6d34eb9a1e802ee61ec8f2f226d3d3825ab4` |

All **188 combined tests pass in 36.988 seconds, no skips**, including the
fourteen new checks. Fresh production compile/padding/link/progress/matcher
succeeds. Complete Init code (164048 bytes), Init data (17376 bytes), Game data
(189088 bytes / 720 owners), previous recoveries and exact callers remain intact.
The separate Init assessment passes 102 checks in 64.464 seconds, no skips;
these suites overlap and must not be summed as distinct coverage.

```sh
make -C conker NON_MATCHING=1 build/conker.us.elf progress match-progress -j4
python3 -m unittest tools.tests.test_game_asset_table_lookup_and_block_load -v -f
make tools-check
git diff --check
```

The complete combined suite is Note 962's command plus
`tools.tests.test_game_asset_table_lookup_and_block_load`. No new word guards,
new profile overrides, data layout changes or warning cleanup are bundled.

## Sibling Boundary And Next

Read-only sibling audit confirms CMake still compiles `recomp_out/.c` as C.
It already contains cache installer at line 202014, lookup at 202256 and block
loader at 203390, alongside the prior loader/relocator and diagnostic support.
These bodies were not replaced or rebuilt. No host source, save, binary,
Release or runtime change is included; source presence is not PC acceptance.

- [x] Recover and fit cache installer, metadata-writing lookup and block loader.
- [x] Qualify cache ordering, bounded aliases, allocation failure and decoder-result handling.
- [x] Connect actual lookup/block load/variadic loader/relocator in bounded fixtures.
- [x] Preserve full Init code/data, Game data, previous recoveries and exact callers.
- [x] Subsequently recover deeper setup `func_1510CE60`, resolver `func_1510D0EC`
  and attachment `func_15168E54` in
  [Note 965](965-game-texture-resource-setup-resolver-and-attachment-recovery-20261004.md).
- [ ] Recover expanded-size metadata loading and cache maintenance and qualify lifecycle.
- [ ] Qualify actual guest DMA/decompression, cache lifecycle and natural effects.
- [ ] Pursue raw byte matching separately; fit alone is not retail instruction parity.
- [ ] Synchronize still-stubbed PC child routines through guest/RDRAM interfaces.

Init remains 492 C / 47 assembly. Game stays 2609 and total 3282 byte-exact C
functions, zero drift. All three edited routines were already counted as C,
so README aggregates stay unchanged. Detailed progress belongs in these docs.
No complete resource pipeline, hardware/gameplay acceptance, compressed-ROM
promotion or push is claimed.
