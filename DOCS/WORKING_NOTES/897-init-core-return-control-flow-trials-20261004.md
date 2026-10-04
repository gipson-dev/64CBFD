# Init Core Return Control Flow Trials

Date: 2026-10-04. Starting HEAD: `50da9cba`.

## Hypotheses

The core returns zero on stream failure and the final produced count on
success. Two isolated source shapes test whether that decision can emit a
smaller epilogue without changing conditional state reads:

1. Success-first early return: `if (init_decode_stream(...) == 0) return s->produced; return 0;`.
2. Shared zero-initialized result: call the stream, assign produced only on
   success, then return the local result.

Both use the complete packed scan-deficit configuration. They do not alter
header sampling, limit calculation, stream execution or state publication.

## Measurements

Columns: whole core text / public entry words / entry frame / core call bound.

| Form | O2/g3 | O1 |
| --- | ---: | ---: |
| Qualified scan-deficit baseline | 4,384 / 52 / 24 / 392 | 5,792 / 86 / 56 / 352 |
| Success-first return | 4,384 / 52 / 24 / 392 | 5,792 / 86 / 56 / 352 |
| Shared result local | 4,400 / 56 / 48 / 416 | 5,792 / 86 / 64 / 360 |

Success-first offers no measured improvement. The shared result grows O2
whole text sixteen bytes and both nested call bounds. Reject both before
semantic qualification; no changed candidate receives corpus credit.

Ignored receipts:

- `conker/build/init-core-success-first-return-trial-20261004`
- `conker/build/init-core-shared-result-trial-20261004`

## Restoration And Checks

Original error-first return restored exactly. Scoped experiment diff is empty;
blob `42b4a7d418964cb81900a6206fb31096e9089bd4` matches Notes 893/894.
Ten ledger, retained packed size, masked success/early-failure and native
header/alignment/limit/error tests pass in 18.822 seconds, no skips. These
qualify the restored baseline only. Project tool and whitespace checks pass.
No full guarded corpus, production build or hardware qualification is rerun.

Qualified packed O1 stays 5,984 linked; best default O2 stays 4,576 / 592 excess.
Production, defaults, guards, README and unrelated Game work remain untouched.
Further fitting requires a different whole-core or shared-helper hypothesis;
these return shapes are not prospective savings in the measured profiles.
