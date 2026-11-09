# Game cache-maintenance candidates and frame boundary - 2026-11-09

func_1510D404 is still non-matching. This checkpoint banks the independent
behavior model, discriminating native/IDO controls and rejected compiler shapes;
it does not install candidate C, change guards/profiles or add matching credit.
The production resolver bank from Note 2223 remains byte-identical.

Total remains **4,292 / 5,513 (77.85%)**, Game **3,619 / 4,840 (74.77%)**,
Init 492/492 and Debugger 181/181, zero drift, 1,221 different. **119** further
accepted matches are needed for 80%. These numbers reuse the exact unchanged
production ELF and progress CSV; this is not a new production recount.

## Measured boundary

The API is void func_1510D404(void), VA 1510D404..1510D608, ROM
13A8B4..13AAB8. The semantic owner is conker/src/game/generated_139FC0.c,
original assembly conker/asm/139FC0.s. Note 968 records the recovered contract.

| Source shape | Raw words | Frame | Positional differences | Decision |
| --- | ---: | ---: | ---: | --- |
| Current production C | 125 | 0x40 | 119 | Preserved unchanged |
| Separate work-counter test | 126 | 0x40 | 96 | Private candidate |
| Separate counter plus explicit equal-end loop | 127 | 0x40 | 72 | Private candidate |
| 64-bit temporary diagnostic | 129 | 0x60 | 78 | Rejected shape-only fit |
| Retail | 129 | 0x60 | 0 | Reference |

Retail saves s0..s7,fp,ra at SP+0x18..0x3C. The current C saves those same
slots but has a smaller frame. Retail retains -65 in fp for the post-callback
flag clear and spills captured last+1 at SP+0x40. The current C uses immediate
mask 0xFFBF and retains the loop limit in a GPR. Retail also preloads the next
signed priority byte in a likely-branch delay slot. These are observed compiler
boundaries; they do not prove the original C declarations or qualifiers.

The wide temporary only reaches the right length/frame by storing its two
halves at SP+0x40/0x44, while retail's sole extra slot holds the loop limit.
Its call positions differ too: diagnostic/expiry-free/decode/temporary-free
indices are 41/70/95/97, versus retail 41/71/94/96. Native compilation also
rejects its integer-to-pointer casts under the existing warning policy. It is
excluded from native acceptance and is not a proposed type repair.

Fifty-one ordinary source screens cover counter gates, captured loop limits,
explicit pointer cursors, mask spellings and widths, useful local lifetimes,
character/pointer views, positive/late gates and measured BSS-ownership probes.
Thirteen other owner bodies/bindings stay fixed in these screens. Constant
mask spellings and ownership changes do not recover the required spill. The
qualifier records the measured results so equivalent rejected forms need not
be rerun. No global definition from an ownership probe is installed.
Three additional scoped volatile-byte probes also fail to recover the frame;
their results remain in observed-read-screen.json. No qualifier is installed.

Five alternative compiler profiles plus the ordinary-profile control were
measured directly on the same processed no-GLOBAL_ASM owner. The control
matches all 14 normal owner bodies and pools. Debug-0, O1, O3 and no-unroll
alternatives change neighbors; debug-2 warns that optimization is disabled.
None supplies an acceptable target match. The asm-processor rejects -g0 as
an argument, so that initial wrapper rejection is not misreported as an IDO
compile failure; the later direct compiler screen is authoritative.

## Independent behavior and rejection evidence

Six focused checks pass in each tools environment. The guest state machine is
derived from the retail contract, rather than by translating candidate lines.
It compares retail and three ordinary C bodies in **1,474 cases per body /
5,896 executions**, covering every one of the **129 retail words**. Six
symbol layouts add 36 rebased cases across those four bodies.
Callee-saved GPR/FPR lifetimes, restored SP and caller memory above SP are
checked on returning paths. This is public/ABI agreement, not literal private
frame or instruction-fault equivalence between differently compiled bodies.

Coverage includes all 256 signed priority-byte patterns, all 256 work-counter
values under both freeze states, no-work returns, captured inclusive ranges,
both valid ID endpoints, zero transitions and byte wrapping. Staged decode
retains the original temporary across callbacks, observes fresh cache/state/
scratch, ignores decoder status and clears only bit 0x40 after the free.
Callbacks mutate bounds, next-entry state, cache pointers, activity and scratch.
Captured bounds do not expand the scan after those mutations.

The diagnostic threshold stays first<0 || last>=0x1E53. Empty invalid ranges
may return from the bounded diagnostic provider; a nonempty invalid range is
checked only through a nonreturning diagnostic-call prefix, before table access.
Full native scans are limited to IDs 0..7761. ID 7762 passing the diagnostic
gate is not qualified as a safe nonempty access.

Native32 O0/O2/O3 each freshly execute nine unchanged behavioral methods from
test_game_texture_metadata_and_maintenance.py on the current, counter and
equal-end C bodies. Strict aliasing and UBSan pass. These include the full
valid-range scan and actual metadata/initializer/setup/resolver/release/
maintenance lifecycle using bounded allocator/DMA/decoder/free providers.
The whole historical suite is not claimed to pass: its full-manifest snapshot
assertion belongs to an older epoch and is not weakened here.

Thirteen compiled controls fail discriminating tests in every native profile
and in IDO guest execution: frozen active work, missing counter decrement,
unsigned priority, tightened diagnostic limit, lost first snapshot, wrong zero
transition, missing cache sentinel, wrong temporary free, stale post-callback
state, wrong cleared bit, missing maximum requeue, live last-bound scan and
stale next-entry scratch. Unsupported emulator instructions are not accepted
as semantic counterexamples.

The real caller's JAL/delay plus next JAL/delay at ROM 0x46174 / PC 15018CC4
match the static void-call interface. Source game_45B80.c declares void(void).
The check does not execute the complete parent or establish hardware behavior.

## Repository and continuation

The package freezes **630 inputs**. Production source, headers, guard bytes,
Makefile, objects, ELF, binary and progress CSV remain exactly the resolver
bank. The matching delta is zero. Both environments use their own measured
helpers; the sibling gets an isolated five-file overlay. Its 2,434 inherited
dirty paths and task-file fingerprints remain unchanged. Fresh shared smoke
checks accompany three exactly fingerprinted regression reuses per copy;
reused checks are not reported as fresh tests.

One packet-only Claude call was attempted with tools disabled and safe mode.
Its owned producer timed out after 210 seconds without returning an analysis;
no advice was used and it was not retried. Local measurements support every
decision above. Private packets, sources, logs and snapshots remain in the
ignored target directory. Host-port Release stays untouched.

Tools commit before the documentation/tools-pin consumer checkpoint; no push.
Root README aggregate bytes stay unchanged. Graphify receives a scoped AST
refresh with old-node retention, not full-corpus semantic extraction.

Continue the same function: inspect the CFE/UOPT boundary that narrows the
signed flag-clear expression and selects the saved mask versus loop-limit
spill. Use owned compiler processes and verify their exact emitted objects.
Do not repeat the 51 equivalent source screens, install the 64-bit shape-only
fit, normalize a wrong frame privately, or claim a new match on these tests.

Focused WSL check:
python3 -m unittest tools.tests.test_game_resource_maintenance_1510d404_candidates -v
Receipts: conker/build/game-resource-maintenance-1510D404-match/.
