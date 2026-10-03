# Init Context Neighbor Guard And First Shadow Corpus

Date: 2026-10-03. Baseline: `b03d17a`.

## Guest Layout And Protected Boundary

The isolated `init_decompressor_context_layout.c` probe compiles against the
repository's libultra headers using IDO O32, in both O2/g3 and O1. A linked
big-endian ELF exposes compiler-evaluated sizes and offsets, rather than host
ctypes or a guessed host ABI:

| Quantity | Guest measurement |
| --- | ---: |
| Pointer / long | 4 / 4 bytes |
| `__OSThreadContext` | 400 bytes / 0x190 |
| SDK `OSThread` | 432 bytes / 0x1B0 |
| `OSThread.context` | 0x20 |
| `OSThread.context.sp` | 0xF0 |
| `OSThread.context.fp0` | 0x130 |
| `OSThread` alignment | 8 bytes |
| Retail-compatible prefix plus 32 FPR slots | 560 bytes / 0x230 |

The SDK sizeof is not the full retail storage footprint. Retail saves all 32
FPRs at `0x130 + 8*i`: `0x1000736C..0x100073E8` writes f0-f31, and
`0x10007B2C..0x10007BA8` restores them. The final eight-byte slot at 0x228
requires an exclusive end of 0x230, 128 bytes beyond the SDK header. New
instruction-word tests pin every save/load slot and compare all 64 words with
the locally present pristine ROM. The guest probe measures an
isolated prefix-plus-32-FPR storage view as 0x230, without changing SDK headers.
The adjacent thread bases `D_800318B0` and `D_80031AE0` are also 0x230 apart.

`D_80031AE0` is therefore a live retail thread storage region through
`0x80031D10`, not merely through the SDK-derived `0x80031C90`.
Startup creates thread 3 in it; Init paths stop that thread; the debugger can
use it as its context pointer. These source references establish a concrete
neighbor that must be preserved, not a general scratch-space allocation.

Contract tests pin the retail stack switch instructions at `0x10005E1C` and
the two 0x80/0x88 context allocations. They also pin the symbol addresses and
derive core caller SP `0x80032A10` from top `0x80032B18`.

Shadow fixtures now make the entire neighboring thread object read-only and
restrict their context-stack write allowance to start at `0x80031D10`.
Negative tests reject a word within the object and a store crossing its end.
These are private model buffers; they neither alter a real thread object nor
prove the whole intervening address range belongs to the decompressor.

The top-to-neighbor span is 3,592 bytes. After the 264-byte wrapper context,
the remaining span is 3,328 bytes. Previous worst observed/bounded core-call
descent is 3,272 bytes, leaving only 56 bytes above this known neighbor;
packed/remaining O2 descends 3,256 bytes, leaving 72 bytes. The compiler/call
bounds and explicit write guards matter more than the apparent address gap.

## Opt-In Corpus Gate

`test_init_decompressor_shadow_corpus.py` freshly compiles all six shadow images
and defaults to all six when enabled. The optional profile selector accepts
one exact shape/profile and rejects unknown selections. Ordinary discovery
skips this expensive corpus test unless explicitly enabled.

This checkpoint runs all 507 retail pages for packed/remaining O2/g3 with CU1
set and the neighbor guard enabled. Every page uses its actual rounded DMA
span and its pristine-image output slice. The shared comparison requires the
compiled core/adapter, forbids the retail core, and compares complete final
GPR/FPR values and known-bit masks, Status writes, wrapper save/load addresses,
pre-wrapper f0-f11, result/state, scratch prefix and output/workspace writes.
Compiled fixed-table initialization is part of each guest fixture setup.

This is a full-page corpus gate for one profile and one CU1 mode, not a claim
that all six profiles or both modes have completed full-corpus qualification.

An initial 507-page run passed in 714.503 seconds with the weaker SDK-derived
0x80031C90 guard, before the original 32-FPR footprint was identified. Its
terminal text/descent/low-SP receipt is 4,896 / 3,256 / 0x80031D58. The reported
200-byte margin was to the wrong neighbor end; the retail margin is 72 bytes.
That run is compatibility evidence only for the weaker guard. A fresh run with
the corrected guard is required and reported separately below.

The fresh corrected-boundary run passes all 507 pages in 710.134 seconds.
Its terminal receipt is packed/remaining O2/g3: text 4,896 bytes, core-call
descent 3,256 bytes, lowest SP 0x80031D58, and 72-byte margin to 0x80031D10.
All 507 compiled context comparisons pass with the stronger neighbor guard;
the source snapshot for this run already includes that corrected boundary.

```sh
CONKER_INIT_SHADOW_CORPUS=1 CONKER_INIT_SHADOW_CORPUS_PROFILE=packed-remaining/o2g3 python3 -m unittest tools.tests.test_init_decompressor_shadow_corpus -v -f
```

Omit `CONKER_INIT_SHADOW_CORPUS_PROFILE` to qualify all six images. That broader
gate remains open until its own terminal evidence exists.

## Conversion Boundary

No semantic decoder or adapter code changes are made in this checkpoint.
Smallest combined text remains 4,896 bytes, 912 over the retained 3,984-byte
region. Production Init assembly ownership and README aggregates stay unchanged;
unrelated pending Game changes are preserved.

The measured thread end and tested non-overlap are stronger than the raw-gap
inference in Note 824. They are still not a complete original allocation-owner
proof: other aliases/writers, hardware interrupt/reentrancy behavior, and the
startup reservation boundary require separate evidence. No production build
or hardware execution is claimed.

## Final Verification

- Corrected-boundary full-page corpus: 507 packed/remaining O2/g3 CU1-set
  context comparisons pass in 710.134 seconds.
- Combined layout/guard/shadow/default-adapter/provenance suite: all 23 tests pass
  in 229.267 seconds. The bounded shadow domain still contains 348 comparisons
  across six profiles and both CU1 modes, now with the retail-footprint guard.
- After adding the direct-ROM checks, the three final layout tests rerun and
  pass in 1.850 seconds; all 64 save/restore words agree with the pristine ROM.
- The ordinary corpus invocation is checked to skip unless explicitly enabled.
- Fresh compiler/assembler/linker logs are empty; root `make tools-check`,
  Python syntax checks and `git diff --check` pass.
- Current CSV still has 492 C / 47 assembly Init rows, with 151,796 / 12,252
  bytes respectively. No new production build, all-project suite, full six-
  profile shadow corpus or hardware test is claimed.

## Next

- [x] Measure nearby OSThread size/alignment/offsets with the guest compiler.
- [x] Recover the larger retail footprint from all 32 original FPR save/load slots.
- [x] Pin original context top and caller-SP derivation to retail instructions.
- [x] Protect the live neighboring thread object in shadow fixtures.
- [x] Complete all 507 pages for packed/remaining O2/g3, CU1-set, with the
  corrected retail-footprint boundary and complete context comparisons.
- [ ] Complete full shadow corpus on the remaining five profiles and CU1-clear.
- [ ] Establish complete stack/state/workspace ownership and reentrancy bounds.
- [ ] Fit corrected semantic code and adapters before production conversion.
