# Capture Request Inline Copy Reconstruction

## Scope And Steps

Continue the full additional-source/Game goal from consumer `3765311a` and
tools `d98b8d8`, after [Note 1385](1385-selected-view-render-pass-dispatch-match-20261015.md).
That checkpoint installed a real match. This checkpoint recovers and qualifies
another complete C body, but does **not** install it or claim another byte match.

1. [x] Recheck the current clean checkout and reopen actual binding/pseudo-operation failures from the whole-source audit.
2. [x] Recover `func_151745F0`'s three-record layout, mixed FP/O32 arguments and optional inline 36-byte copy.
3. [x] Compile 54 bounded controls: 45 complete owners and nine isolated profile controls. Retain the 39-word/22-difference seed.
4. [x] Qualify public guest/native behavior, negative controls and explicit private-state/fired-prefix mismatches.
5. [x] Pass 15 final top-level checks in 45.771 seconds, preserve all production/archive inputs and bank tools `10ccd75` first.
6. [ ] Bank the consumer tools pin/docs, verify the bank and await the incremental graph worker without forcing a smaller scan.
7. [ ] Continue THIS function's cursor/end allocation and stack-input/copy-setup schedule before installation or match credit.

## Actual Source And Layout

The whole-draft survey previously stopped this 40-word candidate at the
unresolved `M2C_MEMCPY_ALIGNED` pseudo-operation. Its archive source is
`Another Source/CBFD-Recompiled/conker/conker/src/game/game_1A11B0.c`, SHA-256
`ea8d7f14f995b088ae0fa96dcb415d9a56cbb57581482d192863deeedee12791`.
Check that fingerprint rather than editing the archive or inventing a memcpy
binding. Retail has no call in this leaf function: it copies inline.

The active owner `conker/src/game/generated_1A11B0.c` still contains the original
zero-return C stub. Both other owner functions are also stubs; this work does
not recover or qualify those callers. The original `asm/1A11B0.s` is pinned at
`91d5b8f5d542245b976a9515019a337a34b1e2ce1e83bbd543186c1416e2553c`.

Retail scans from `800DD348` to `800DD3FC`, three records of `0x3C` bytes:

| Offset | Recovered Access |
| --- | --- |
| `00/04/08` | Three `f32` position words, copied without FP arithmetic |
| `0C` | Unsigned byte state; zero is free, insertion writes 3 |
| `0D..0F` | Preserved padding |
| `10..33` | Optional 36-byte payload, nine words |
| `34` | Signed byte callback value |
| `35..37` | Preserved padding |
| `38` | Final 32-bit caller value |

Use private typed `CaptureRequest1A11B0` and `CapturePayload1A11B0` views and
meaningful parameter names in the experiment. Keep the public address name.
The first two floats arrive in `f12/f14`; the third arrives as A2 bits and is
homed at caller SP+8. The signed fifth argument is loaded at SP+13, and the
last word at SP+14 (hex offsets). Return 0 after inserting into the first free
record, or 1 when all three state bytes are nonzero.

The draft's word-sized state/callback accesses and float-to-integer assignments
are not reliable recovered types. Reconstruct the actual byte/FP accesses from
retail. A typed `request->payload = *payload` emits the real three-iteration,
three-word copy loop, including its final branch-delay store. No pseudo-call,
fake symbol, manual word replacement, production guard or shared header change.

## Bounded Matching Evidence

`tools/experiments/game_capture_request_slot.py` provides seven original/loop,
ten schedule, eight byte-address, nine interface, six global-layout, five
return/cursor and nine isolated profile controls. All 54 have zero diagnostics;
none is byte-exact. The private profiles do not change production flags.

Ordinary do/while and while forms trigger IDO unrolling and grow to 110/112
words. The explicit back-edge keeps the small leaf. The selected
`order-x-y-z-state-callback-value` form emits 39 real words, no frame, no calls
and no pools under unchanged `-O2 -g3`. It has 22 genuine word differences over
the complete 40-word retail slot. The final retail word is separately proven
alignment NOP, not an invented substitute for a missing nonzero instruction.

The existing generated-slice padder emits its real 156-byte symbol plus that
alignment word and retains all 22 differences. It does NOT make the candidate
match. Both other raw function bodies retain bytes, sizes and relative
relocations; normalized pools stay fixed.

The remaining differences are concentrated in the base/end V0/V1 allocation,
the ordering of parameter-home reloads and stores at `+20..+54`, and the scan
updates at `+84..+8C`. The nine-word inline copy at `+58..+78` and the successful
return at `+7C/+80` already match. Preserve the best seed; do not rerun these
unchanged 54 controls or confuse equal length with matching.

The isolated compiler helper's generic frame calculation initially interpreted
the opening A2 home store as a stack adjustment. Report frame size only when
the first word is an actual SP addiu; regenerate all nine profile receipts.
Their O2 leaf frames are zero; O1/g3 uses an eight-byte frame and is not selected.
An attempted no-unroll option through the assembly preprocessor was rejected;
the existing direct pure-C compiler helper performs these private controls
without altering the shared wrapper or production recipe.

## Semantic Qualification And Limits

All complete public memory and results agree with an independent reference
across 14,336 paired-SP guest cases. Exercise 64 representative occupancy triples
from state bytes 00/01/80/FF, seven callback-narrowing patterns, four FP bit
triples and null/external/self/other-record payloads. Include NaN/infinity and
signed-zero bit patterns in the guest copy model, with no FP arithmetic claim.
Both raw candidate and retail preserve all padding, untouched records, external
payload bytes and the expected caller-home effects. Neither makes a call.

Native32 runs the actual selected C in 2,048 cases per O2/O0 profile with zero
diagnostics, finite FP cases, explicit type-offset checks and all 212 bytes of
the guarded three-record bank checked. The native bridge binds both original
symbols to one real three-record array. It also checks the external payload
is unchanged. This is not MIPS private-frame, endian, arbitrary-FP, FCSR,
concurrency, hardware or gameplay acceptance. Payloads are disjoint or exactly
self-copying; arbitrary partially overlapping struct objects are not qualified.

Three independently compiled controls alter state 3 to 2, store Y instead of Z,
or copy only the first payload word. Each returns the expected function result
but wrong memory in the guest, and native status 2 under both profiles. No crash
is counted as a successful negative control. The Z control explicitly annotates
its now-unused parameter only in the native harness; warnings remain errors.

There are **8,288 complete private-state mismatches**, despite public agreement.
Among 322 paired, fired access prefixes, 306 remain private-state different.
Keep those failures visible. They are not normalized away or used to justify
installation. This is a bounded low-word execution model, not a hardware
exception or complete VR4300 emulator.

Coverage reaches all 38 normally reachable body words. Retail's duplicate
increment at `15174674` is unreachable under the normal return ABI: the preceding
JR returns, and the taken scan branch targets `15174678`. The alignment NOP at
`1517468C` is also not executed. Both words still count for byte matching.

The initial harness exposed unsupported LB, negative callback literal formatting
and the incorrect 39-word coverage expectation. Add a local signed-byte opcode
implementation with five ROM-free boundary checks, mask emitted callback
literals to 32 bits, and assert the two exact unreachable addresses. Do not
weaken memory checks or suppress warnings to make those harness failures pass.

## Preservation And Reproduction

All 15 final top-level checks pass in 45.771 seconds: three ROM-free candidate/
LB checks, seven new qualification checks and five current installed-image
gates. Those installed gates also run eight embedded actor/matrix history gates.
Every one of the 26 captured production inputs remains byte-identical, including
the stub, ELF, progress, guards, Makefile and headers. All 26 frozen-input
corruption controls fire. All 801 original archive fingerprints remain fixed.

The normal N64 build is up to date. Fresh match-progress remains Game
2,886/4,829 (59.76%), total 3,559/5,502 (64.69%), different 1,943, zero drift.
Root README and conversion counts are untouched. ELF stays
`f3a09d0a11e36aceab1f2124653c63091ef14d4033c4953e983bbeb014397e75`;
progress stays `3ad7466c067bdb27e92248b8b237fb3dff392097ef3cd5d9a337d8268fbda091`.

Gate all 592 initial dirty mirror fingerprints and its independent `ddbdd16`
HEAD before copying only the three new owned tool files. Verify all copied
hashes, standalone syntax and three ROM-free checks. The mirror now has 595
expected dirty paths, with every older fingerprint/HEAD preserved. Tools
`10ccd75` is banked before the consumer pin. No mirror commit, reset, push,
advisory call, host edit/build/launch or frozen Release operation.

Seven-document validation checks 4,891 relative links with zero broken links.
The full graph update refuses 19,251 nodes against the 41,024-node curated
graph and retains 19,398 nodes from 2,972 excluded-but-present files. Preserve
that fail-closed result; await the consumer's incremental commit worker instead
of forcing the smaller scan.

Reproduce from the decomp root using the existing local inputs:

```sh
python3 -m tools.experiments.game_capture_request_slot
python3 -m tools.experiments.game_capture_request_slot --schedules
python3 -m tools.experiments.game_capture_request_slot --addresses
python3 -m tools.experiments.game_capture_request_slot --interfaces
python3 -m tools.experiments.game_capture_request_slot --layouts
python3 -m tools.experiments.game_capture_request_slot --returns
python3 -m tools.experiments.game_capture_request_slot --profiles
python3 -m unittest tools.tests.test_game_capture_request_slot_candidates tools.tests.test_game_capture_request_slot tools.tests.test_game_view_pass_dispatch_installed -v
```

Next, investigate the selected seed's optimizer allocation and block scheduling
at the exact offsets above. Finish its private-state, rebase and installed-image
gates before match credit. Other failed-source/binding cases, handwritten Init
hardware assembly and the separate unmatched scanner remain open; this new seed
does not complete the full additional-source/Game goal.
