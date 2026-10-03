# Init Retail Page DMA and Exception Core Address Qualification

Date: 2026-10-03. Baseline: `26df0087`.

## Decision

The retail Game-page input DMA does not overlap the exception decoder workspace.
This resolves a numerical overlap concern, not the workspace's allocation
ownership, full exception context, or a production C conversion. The exact
assembly remains the production owner; Init stays at 492/539 C functions.

## Reproducible Evidence

`tools/tests/test_init_decompressor_retail_pages.py` verifies the original US
ROM SHA-1 `4cbadd3c4e0729dec46af64ad018050eada4f47a` before reading its encrypted
page-offset table. It uses the startup code's 507-page count, ROM table base
`0x42450`, and XOR key `0x8039CCCA`. Compressed pages occupy ROM
`0x42C50..0x186B50`. No ROM data is added to the repository.

All 507 raw-deflate streams terminate and match the corresponding pristine
decompressed Game bytes. The first 506 output 4,096 bytes each; the final page
outputs 304 bytes. Comparison uses each page's actual header length, not an
assumed final 4,096-byte output.

The largest compressed span is page 169: 3,058 bytes, rounded to a 3,072-byte
DMA. Input begins at `0x80033330`; workspace begins at `0x800340E8`.
Their separation is 3,512 bytes, leaving 440 bytes after the largest observed
DMA. None of the 507 rounded transfers overlaps workspace. This is narrower
than claiming arbitrary compressed input is safe at these addresses.

## Retained Core Model

Three selected pages execute the actual retained core words through the
existing bounded integer/low-FPR-word model. Fixed tables are bootstrapped
independently before placing input, output, workspace and SP for the core call.
Output is a synthetic page slot at `0x80050000`; input contains the actual
rounded ROM transfer, including its trailing bytes.

| Page | Returned/output bytes | Workspace write span | Exclusive last workspace write |
| --- | ---: | ---: | --- |
| 0 | 4,096 | 3,416 | `0x80034E40` |
| 169 | 4,096 | 3,276 | `0x80034DB4` |
| 506 | 304 | 0 | No workspace writes |

All three outputs match. The call returns its byte count, not the inner
stream's zero success status. Input bytes are not written; caller SP returns
to `0x80032A10`, with the retained core frame based at `0x80031F88`.
The final page takes a fixed-table path and needs no dynamic workspace writes.

Observed workspace spans do not establish an owned allocation capacity.
The nearby absolute symbol `D_800354F8` is only a comparison boundary in this
model, not an array-size declaration. Tests deliberately exclude CP0, real DMA,
cache behavior, output-page ownership and full 64-bit FPR save/restore.
The unconditional exception `f0` load remains an open context gate.

## Verification

- Three new test methods pass, including all 507 independent zlib comparisons
  and the three selected retained-core executions.
- All 98 Init tests pass (30.903 seconds).
- All 573 project tool tests pass (102.239 seconds); the final strengthened
  workspace-span assertions also pass in the targeted three-test rerun.
- `git diff --check` passes.
- Production source, assembly and README aggregates are unchanged.

## Next

Continue the connected exception/adapter contract: qualify full FPR behavior
and prove stack/workspace ownership independently of symbol gaps. The
frame-backed C still emits 5,312/5,600 bytes against 3,984 retail bytes and
introduces ordinary nested C frames. Neither numerical DMA separation nor
host-model parity removes those production conversion gates. The two smaller
ordinary C candidates remain `func_10005BE0` and `func_100038E0`; the remaining
SDK and privileged assembly should retain their explicit original contracts.
