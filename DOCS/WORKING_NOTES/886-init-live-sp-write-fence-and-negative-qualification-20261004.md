# Init Live SP Write Fence And Negative Qualification

Date: 2026-10-04. Source baseline: `b59ef8f1`, unchanged Note 879 candidate.

## Ownership Boundary

The retail wrapper saves incoming SP at 0x80032B18, switches SP to that
address at 0x10005E28, then allocates its context frames before calling the
decoder. Startup thread contexts at 0x800318B0 and 0x80031AE0 have observed
retail extents 0x230, ending at 0x80031D10. Absolute BSS symbol assignments
and a startup clear do not establish full private-stack reservation ownership.
[Note 806](806-init-exception-storage-boundaries-and-all-retail-core-page-survey-20261003.md)
remains the evidence boundary; current SDK sizeof(OSThread) is not the full
retail context extent.

The earlier shadow model protects that neighboring context, but its allowed
stack interval can admit a write below current SP while still above the
neighbor. A stack-pointer depth bound alone does not reject such a store.
This turn adds a separate live-SP write fixture, not an allocation claim.

## New Guard

`tools/tests/test_init_decompressor_live_stack_writes.py` inherits the qualified
direct-load/callee-preserving fixture. The write fence is disabled during
fixture setup and the retail incoming-SP publication. It arms after the
executed private-stack switch `0x249D0000`, requiring SP 0x80032B18.
Once armed, a write intersecting the modeled private-stack interval
0x80031D10..0x80032B1C must start at or above current SP. Existing read-only,
neighbor and caller-buffer checks still run; unrelated buffers are unchanged.
The guard uses current SP, not the lowest historical SP.

The new bounded test subclass runs the complete inherited direct-load suite
with this fixture. A separate opt-in corpus subclass also selects it; the
existing corpus class and its previous evidence are not silently changed.

## Active Negative Gates

Across all six builds and both masked CU1 modes, the first adapter S0 save
at offset 0xA48 is replaced with `sw s0,-4(sp)` in a private fixture code copy.
That address remains above the known neighbor but is below the current
0xA88-byte frame. Every corrupted execution raises the specific live-SP
error before the write can be committed. All corresponding clean executions
pass and demonstrate the guard was armed.

A focused boundary test accepts writes starting exactly at live SP and
above it, rejects both a full word below SP and a one-byte crossing, and
accepts an output-buffer write outside the private-stack interval. Existing
callee-clobber, core-state poison and neighbor-fence gates remain active.

## Verification

```powershell
wsl python3 -m unittest tools.tests.test_init_decompressor_live_stack_writes -v -f
wsl python3 -m unittest tools.tests.test_init_exception_storage tools.tests.test_init_decompressor_storage_boundaries -v -f
```

Fresh live-SP suite: 38 tests in 263.292 seconds, 37 pass / one opt-in
full-corpus skip. Fresh storage regressions: 13 pass in 1.065 seconds, no
skips, including the current guest SDK layout and pinned retail FPR extent.
Together: 50 passes / one skip. Tool and whitespace checks pass.

| Shape/profile | Linked text | Static descent | Observed descent |
| --- | ---: | ---: | ---: |
| frame/o2g3 | 5,712 | 3,272 | 3,272 |
| frame/o1 | 6,224 | 3,208 | 3,208 |
| aligned-end/o2g3 | 4,608 | 3,232 | 3,232 |
| aligned-end/o1 | 6,016 | 3,192 | 3,192 |
| packed-remaining/o2g3 | 4,576 | 3,240 | 3,240 |
| packed-remaining/o1 | 6,016 | 3,200 | 3,200 |

Size/bounds are unchanged; packed O2 remains 592 bytes over retail. This
is bounded live-frame write qualification, not hardware timing, general
aliasing, scheduler resume or full reservation proof. Reads below live SP
are not fenced by this new write-only guard. Notes 880/881's 1,014 paired
pages remain evidence for the previous fixture without this guard.

## Remaining Gates

- [ ] All 507 live-SP-guarded packed O2/g3 masked CU1-clear pages.
- [ ] All 507 matching guarded CU1-set pages.
- [ ] Complete retail stack reservation and entry/frame ownership.
- [ ] Further fitting and hardware/context qualification.

Candidate decoder/adapter/compiler sources, production sources, profiles,
word guards and README totals are unchanged. No production conversion, ROM build or sibling-port
test is claimed. Unrelated Game source/tests are preserved and unstaged.
