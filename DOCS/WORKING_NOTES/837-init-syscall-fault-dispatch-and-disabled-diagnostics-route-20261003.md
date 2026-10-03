# Init Syscall Fault Dispatch and Disabled Diagnostics Route

Date: 2026-10-03

## Scope

Follow-up to [Note 836](836-init-retail-cleanup-callback-null-path-and-fatal-slot-20261003.md).
Trace the allocator fatal callback's syscall through the original Init exception
dispatch. Add `tools/tests/test_init_syscall_fault_route.py`; production assembly,
C, decoder experiments and conversion ownership remain unchanged.

## Retail Route

`func_150AD770` is `syscall 0` at `0x150AD770`. At `0x100073EC`, the Init
handler reads Cause, saves it at thread offset `0x120`, sets state 2, then masks
Cause with `0x7C`. Syscall code 8 yields the masked value `0x20`.

The dispatch has explicit routes for values `0x08`, `0x0C`, `0x24`, `0x2C`
and zero, but not `0x20`. The nonzero branch at `0x10007434` therefore takes
the generic fault route `func_1000777C`:

- Save the thread pointer in `D_8002BE04`.
- Set thread state at offset `0x10` to 1 and flags at `0x12` to 2.
- Save BadVAddr at offset `0x124`.
- Call `func_10007DAC` for optional diagnostics.
- Submit fault event offset `0x60` through `func_100077B8`.
- Jump to scheduler/restore entry `func_10007A38`, not to the allocator's caller.

The diagnostic routine gates its long debugger path on
`D_800E9D00 & 0x2000`. If clear, it saves SP/RA and immediately returns through
`0x10008108`. If set, it enters the diagnostic body. That body is not executed
by this checkpoint; its DMA/TLB/debugger effects remain separate work.

## Executable Evidence

The new fixture pins every modeled instruction directly against the
SHA1-validated original US retail ROM. It executes bounded instruction slices
using the existing guest branch/delay-slot runner and only locally adds seeded
CP0 Cause/BadVAddr reads. It does not synthesize a complete CPU exception entry.

Four tests establish:

1. Syscall routes to generic fault with no extra bits, pending interrupt bits,
   the BD bit, or both. The saved Cause retains those bits; dispatch uses only
   the masked exception code.
2. TLB-load, TLB-store, break, coprocessor-unusable and interrupt values select
   their distinct dispatch boundaries, preventing a syscall-only fixture from
   masking an incorrect branch implementation.
3. With diagnostics disabled and the fault-event queue pointer zero, fault
   state/flags/BadVAddr are published; diagnostics return; event offset `0x60`
   skips queue mutation; control reaches `func_10007A38`. The seeded saved EPC
   remains `0x150AD770` throughout, rather than being advanced to a return stub.
4. With diagnostic bit `0x2000` set, control enters `0x10007DD4` and does not
   take the diagnostic return shortcut.

The event helper returns through `JR s2`. To keep the model bounded, the test
stops before that instruction, asserts target `0x100077B0` (JAL PC + 8), then
continues at that verified target to the scheduler boundary. The instruction
itself is ROM-pinned but its execution is not modeled here.

## Verification

```sh
python3 -m unittest tools.tests.test_init_syscall_fault_route tools.tests.test_init_allocator_guest_free tools.tests.test_init_bitmap_allocator_contract tools.tests.test_init_page_pool_setup tools.tests.test_init_decompressor_storage_boundaries -v
make tools-check
git diff --check
```

All 32 focused tests pass in 7.692 seconds. Project tool checks and whitespace
validation pass.

## Consequences and Remaining Work

The original fatal route is not established as an ordinary returning allocator
error path. Notes 833/834's returning stubs remain useful for conditional
post-call arithmetic only, not proof that retail failure continues that way.

These tests seed an already saved thread context and do not model syscall
entry, Status changes, complete GPR/FPR saves, event delivery with a real queue,
the scheduler's selected thread, ERET, asynchronous interrupts, or debugger
resume decisions. Reaching the scheduler with a stopped/faulted thread does
not prove that no external action can ever resume it.

Next audit static stack/workspace reservations and diagnostic-enabled storage
effects. Decoder fitting still exceeds its retail slot by 896 bytes. The prior
Init inventory remains 492/539 C functions, with 47 assembly functions and
12,252 retained assembly bytes. No README aggregate or unrelated Game changes.
