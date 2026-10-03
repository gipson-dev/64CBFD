# Init Debugger Entry Frame and Seeded Resume Footer

Date: 2026-10-03

## Scope

Follow-up to [Note 842](842-init-post-diagnostic-page-state-cleanup-and-continuation-20261003.md).
Add `test_init_debugger_entry_contract.py` for retail `func_16000B14` entry,
early exits and conditional footer behavior. The function is already represented
in matched/guarded C; this checkpoint does not recover or convert another function.

Read its complete 286-word (`0x478`-byte) retail slot directly from the
SHA1-validated original US ROM's uncompressed Debugger payload. Execute only
the bounded entry/early-return and footer paths using the existing guest model.
No compiled C, guard application, interactive UI or hardware acceptance claim.

## Entry and Frame Evidence

- Prologue allocates `0x50` bytes, saves s0..s7, s8 and RA, and stores a0 in
  its caller home cell at the original SP. GP is unchanged on these paths.
- For the diagnostic placement from Note 841, SP `0x80135958` gives frame
  low `0x80135908`. The image ends at `0x80134960`, leaving `0xFA8` bytes
  between image end and this frame. The caller home cell also writes four
  bytes at original SP; the fixture fences that cell explicitly.
- With `D_8002AC5C != 0`, entry returns zero without resetting the debugger
  flag or framebuffer pointers.
- With either framebuffer missing, entry clears `D_16003888`, sets both
  framebuffer pointers to `0x80350000`, and returns zero.
- With both framebuffers present, entry reaches the first helper boundary
  `0x16000B9C` with the expected bounded frame. The helper is not executed.
- All completed paths restore saved registers, original SP and RA. Lower
  frame and upper home-cell guards remain untouched.

## Footer Premises and Results

The UI and TLB scan are deliberately skipped. After executing the real
prologue, the test seeds `D_16003AF0`, `D_160038A4`, saved Cause and EPC, then
executes the original footer from `0x16000F00` through the return delay slot.

| Seeded Premises | Return | State/Flags | EPC |
| --- | --- | --- | --- |
| `D_16003AF0=0` | 1 | 4/0 | unchanged |
| `D_16003AF0=1`, Cause `0x20`, recognized-fatal flag 1 | 0 | preserved 1/2 | unchanged `0x150AD770` |
| `D_16003AF0=1`, Cause `0x20`, fatal flag 0 | 1 | preserved 1/2 | `0x10007DA0` -> `0x10007DA4` |
| `D_16003AF0=1`, Cause `0x24`, fatal flag 0 | 0 | preserved 1/2 | unchanged |

The runnable branch takes precedence over the syscall predicate. These are
conditional footer contracts, not proof that arbitrary premise combinations
are produced by the live UI/TLB scan. In particular, do not turn the tested
recognized-fatal case into an unconditional claim that no allocator-fault
context can ever be resumed.

Note 842 separately establishes that a nonzero debugger return selects the
thread-requeue continuation, while zero preserves fault continuation. This
checkpoint does not execute the combined debugger/cleanup/scheduler chain.

## Verification

```sh
python3 -m unittest tools.tests.test_init_storage_literals tools.tests.test_init_allocator_guest_free tools.tests.test_init_exception_storage tools.tests.test_init_syscall_fault_route tools.tests.test_init_decompressor_storage_boundaries tools.tests.test_init_diagnostic_storage tools.tests.test_init_bitmap_allocator_contract tools.tests.test_init_diagnostic_cleanup tools.tests.test_init_debugger_entry_contract
make tools-check
git diff --check
```

All 62 focused tests pass in 8.536 seconds. The new standalone suite passes
four tests. Project tool and whitespace checks pass.

## Next Work

The bounded lifetime audit now covers allocation/free, tag sweeps, the real
cleanup callback null path, fault dispatch, static reference candidates,
startup table writes, diagnostic placement, cleanup and debugger entry/footer.
Full reservations, actual hardware effects, UI-generated predicates and thread
resume are still not proven. Return to the concrete decoder fitting problem
with these constraints retained; the qualified candidate remains 896 bytes
over the retail group. Do not infer capacity or remove privileged assembly
from these tests alone.

Production C/assembly, decoder/adapter, README aggregates and unrelated Game
work remain unchanged. Prior Init inventory remains 492 C / 539 total, with
47 retained assembly functions (12,252 bytes).
