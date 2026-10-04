# Init Startup Thread Stack Top And Constructor Contract

Date: 2026-10-04. Starting HEAD: `b100ed8b`.

## Purpose

Strengthen the neighboring-owner evidence for the private decoder stack.
Previous Notes 824/825 identified startup thread addresses and the later
32-FPR context footprint. Execute the actual startup call preparations and
retail `osCreateThread` body to pin stack arguments, context publications and
constructor writes. This does not declare the intervening gap an owned stack.

New fixture: `tools/tests/test_init_startup_thread_contract.py`.

## Executed Retail Evidence

The fixture validates original US ROM SHA1, then pins these instruction ranges
by SHA256 before executing them with the existing MIPS low-word oracle:

| Range | Scope | SHA256 |
| --- | --- | --- |
| ROM `0x10AC..0x10DC` | Thread 1 call preparation including JAL delay slot | `fb48d3f639678ca252c7dfcf5f6d3d2f647ee5c23e8b2ba2eb4d93b70ec3ce2f` |
| ROM `0x10F8..0x113C` | Thread 3 prologue and call preparation including delay slot | `8317d6527d4e4391782d77eb1d817c86046ca484daf2dd32a4ea46a369d5e8d2` |
| ROM `0x37F0..0x38B8` | Complete executable constructor body through return delay slot | `4fa02c8a7eefc1e0c6a772e9fcbb34f4d7f481cdaf4dadd41beffcf430116e15` |

Constructor slot alignment after its return is not executed. The first prefix
does not execute earlier startup initialization; the second prefix stubs
`func_10004470`'s queue setup. `__osDisableInt` and `__osRestoreInt` are stubs
with a known mask result, not hardware interrupt behavior. Both constructor
call sites and its two mask-helper sites must be visited before acceptance.

| Thread | Object | ID | Entry | Stack-top argument | Priority | Saved context SP |
| --- | --- | ---: | --- | --- | ---: | --- |
| Startup 1 | `0x800318B0` | 1 | `0x100010F8` | `0x8002D8B0` | 5 | `0xFFFFFFFF8002D8A0` |
| Startup 3 | `0x80031AE0` | 3 | `0x10001194` | `0x800318B0` | 10 | `0xFFFFFFFF800318A0` |

The constructor publishes sign-extended stack top minus sixteen, including the
high-word subtraction/borrow instructions. Argument cases zero, one and
`0xDEADBEEF` pin sign extension in context A0. Checks also cover ID/priority,
PC, cleanup return `0x10007BF8`, Status `0x0400FF03`, RCP mask `0x3F`, FPCSR
`0x01000800`, stopped state, flags, FP flag and active-queue linkage.

These tops are below the decoder's private-stack interval. This establishes
the published startup stack tops, not complete stack capacities, runtime
depths, scheduler activity or all other indirect writers.

## Constructor Extent Versus Context Extent

Executed constructor writes within the selected object end at offset `0x130`.
The entire following `0x100` bytes retain their seeded values. This is not a
smaller thread object: the later retail context save/restore transfers all
thirty-two eight-byte FPR slots at offsets `0x130..0x230` (Note 806).
The second known live thread footprint therefore still ends at `0x80031D10`.
Do not move the experimental decoder's neighbor fence down to constructor end.

For both startup call paths, the seeded private interval
`[0x80031D10, 0x80032B1C)` remains unchanged, and no executed write overlaps it.
The fixture restricts constructor writes to the selected 0x230-byte object,
synthetic caller stack and active-queue publication cell `0x8002BDFC`.
An injected constructor store at object offset `0x230` is rejected on both
paths by the specific caller-owned-buffer guard. This proves that the guard
fires; it does not turn the fixture's permitted ranges into a retail allocation
manifest.

The synthetic caller SP is `0x80060000`. Tests verify the constructor preserves
S0 and restores its caller SP; its frame is 0x20. The thread-3 prefix adds its
own 0x20 caller frame. These synthetic execution depths are not real startup
or decoder runtime stack measurements.

## Verification

Five new tests pass independently in 0.391 seconds. Combined with six existing
exception-storage and fourteen literal-census tests: 25 pass in 6.908 seconds,
no skips. Project tool and whitespace checks pass.

```sh
python3 -m unittest tools.tests.test_init_startup_thread_contract tools.tests.test_init_exception_storage tools.tests.test_init_storage_literals -v -f
make tools-check
git diff --check
```

No production/source/adapter changes are required. The qualified dynamic-order
candidate remains 4528 linked O2 bytes / 544 excess / 3248 descent. Its 80-byte
known-neighbor clearance and Notes 905/906 corpora remain prior evidence.

## Next

- [x] Execute both original startup thread call preparations and constructor.
- [x] Pin saved stack tops, argument extension, initialized fields and write extent.
- [x] Retain the full later 0x230-byte context fence and executed negative control.
- [ ] Establish complete private-stack reservation and all relevant writer lifetimes.
- [ ] Further fitting, entry/frame ownership and hardware/context qualification.

Production Init remains 492 C / 47 assembly functions. README totals, word
guards, sibling-port artifacts and unrelated Game work remain unchanged.
No ROM build, hardware run or whole-program ownership proof is claimed.
