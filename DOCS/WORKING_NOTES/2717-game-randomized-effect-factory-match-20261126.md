# Randomized effect factory direct match - 2026-11-26

`func_150D278C` replaces the zero-return placeholder in
`conker/src/game/generated_FFBA0.c` with a typed randomized effect factory.
**All 102 words / 408 bytes and all 21 binding positions emit directly from C,
with frame 168 and zero guards.** Function and slot coincide at VA
`0x150D278C..0x150D2924`, ROM `0xFFC3C..0xFFDD4`. No insertion, omission,
alignment tail, compiler-profile or Makefile change. The complete guard CSV,
five raw/padded neighbors and all pools stay unchanged. Both callers compile
identically after correcting the local forward prototype and including the
existing SDK structure types.

Production: **4,696 / 5,528 (84.95%) total**, **4,023 / 4,855 (82.86%) Game**,
Init 492/492, Debugger 181/181, zero drift, 832 still different.
**Three more accepted matches reach 85%.** One new match; conversion rows and
denominators stay fixed. No additional caller/helper/host matching credit.

The observed interface is `void (u32 command, const void *parameters,
u8 priority, s32 context)`. Both measured callers ignore the result register.
The 96-byte payload holds the command at 0, six computed/zero float fields
through 0x18, 64 parameter bytes at 0x1C, three colour bytes at 0x5C, and an
originally unwritten byte at 0x5F. Descriptive field names are inferred.
The selected source does not initialize that final byte or assign it a known
meaning. Its original stack value remains part of the retail 96-byte copy.

Three float draws compute `(r+r)*D_800A099C`, the rate
`r*D_800A09A0+D_800A09A4` and its reciprocal, then
`r*D_800A09A8+D_800A09AC`. These five pinned coefficients are approximately
pi, 0.4, 0.3, 0.13000001 and 0.3. One integer draw conditionally flips the
speed's sign. The parameter copy precedes a nine-byte local snapshot of
`D_800A0990`; the next unsigned draw selects one of its three RGB entries
(white/red/green in the original data). Changes to the global palette after
that snapshot do not affect the chosen local colour. The third unsigned draw
produces lifetime `draw % 101 + 100`, recovered as an **s16 local**. The factory
receives `(lifetime, -1, 50, -1, 1, 0, 96, priority, context)` through its
existing typed ABI. A successful result gets the full payload at record+0x28.
No original RNG implementation or allocator behavior is replaced here.

The first C shape produced frame 176 and101 words. Scoping the palette work
recovered all 102 positions/bindings but retained frame 176. Recovering the
signed16 lifetime as its own value before the nine-argument call produced the
original frame 168 and every raw word without guards. Source ordering, ordinary
register hints and shallow layout alternatives were rejected privately.
No physical register binding, dummy local, stack normalizer or instruction
patch is used. The selected frame saves RA at SP+0x2C, holds the palette at
SP+0x38 and the payload at SP+0x48. The priority is reloaded as an unsigned
byte at SP+0xB3; the full context word is SP+0xB4.

Both complete original callers already match the frozen ELF/ROM:
`func_150D26F0`,39 words/frame 32, updates an enabled timer and invokes this
factory when it becomes negative; `func_150D32FC`,23 words/frame 24, invokes
it for event0x34 with the matching record byte. They forward command,
64-byte parameter storage, priority and context. The timer caller draws a
fourth integer afterward and reloads its range/base, including when the
allocated record aliases the original owner. Both ignore the child's V0.
The complete aligned ROM census finds exactly two direct JAL patterns at
`0xFFBF0/0x1007F0` and no aligned function pointers. No new parent credit.

Validation:

- Both complete production padders and the actual three-command Make recipe
  produce the same owner, with zero diagnostics, unchanged five neighbors and
  pools, and the entire guard file unchanged.
- Guest: 1,680 cases per each of five identical streams,101 reachable target
  words and476 access-cut quintuples. The remaining word is the unreachable
  divide-by-constant3 break7. Full raw/literal memory, private frame, GPR/FPR,
  HI/LO, FP operation order, FCSR and fault states agree. An independent model
  compares public memory, call/snapshot order, all 96 payload bytes and FCSR.
  It preserves the original guest stack byte at payload0x5F. Four rounding
  modes, finite nonzero-divisor arithmetic, signed zero, unsigned RNG bounds,
  null/success, input/output aliases, live scalar/parameter mutation, palette
  snapshot mutation, incoming homes and caller stack inputs are covered.
  The original11-word memcpy also executes on nonmutating-provider paths.
  Private-home probes are separate from portable C; hardware FP acceptance
  and original RNG/allocator execution are not claimed.
- Native: actual selected C, separate typed services and an independent byte
  construction reference in three TUs. All 4,096 cases pass at O0/O2/O3 with
  strict aliasing/FP, UBSan traps and LTO type checks. **Native compares the95
  initialized payload bytes. Exactly the originally unwritten destination
  byte is canonicalized in the capture only**, with no source/runtime change
  and no defined-value claim for it. All other arena/canary bytes, metadata,
  palette/scalar values and MXCSR agree. Four rounding modes, existing flags,
  full unsigned draws and allocated-output aliases over the input array are
  exercised. Eight semantic controls complete with comparison exit42; no
  compiler failure, trap or signal counts as rejection. The early/live palette
  control and parameter-source shift discriminate actual snapshot behavior.
- Callers:512 tick and128 event cases per original/raw stream, with160/32
  connected children. All38 reachable tick words and all23 event words run;
  only its zero-divisor break33 is outside the valid test domain. Full literal
  private states agree. An independent semantic leaf-provider counterpart
  agrees publicly, preserving post-child range/base reloads under owner alias.
  Six poisoned child returns leave caller behavior unchanged. Wrong timer
  reset and event selector are rejected by complete executions. Provider
  private-stack identity and void return-register values are not equated.
- Both scoped padders expose all 204 word and 42 binding corruptions. Twenty
  GNU links and 100 guest rebases independently move service, scalar and
  palette symbols through jump regions and signed-low carry seams. Generic
  oversize is visible; generated oversize rejects.
- The existing18-word handwritten RNG,25-word float wrapper,49-word record
  factory,11-word copy loop,12-byte palette slot and five scalars are pinned
  to original ROM/frozen ELF. These static pins grant no new helper credit.
- Independent old-C plus original-ASM prediction equals the complete private
  and production ELF: **397 changed bytes, zero exclusions**. All 189,088
  protected Game-data bytes across 720 owners remain fixed. ELF SHA-256:
  `d568bb38d9c1761f667f3d07e20a461df2389694803cc4030f72efaf7a07671c`. The native indeterminate-byte boundary above is not
  an exclusion from this complete-image comparison.

| Phase | Elapsed | Tests |
| --- | ---: | --- |
| preinstall-primary | 157.708 s | 5 fresh / 0 reused |
| preinstall-sibling | 116.519 s | 5 fresh / 0 reused |
| installed-primary | 106.451 s | 5 fresh / 0 reused |
| installed-sibling | 110.486 s | 5 fresh / 0 reused |

All 20 packaged target tests are fresh with matching primary/isolated-sibling
source, task, import and data fingerprints. Shared tools-check passes;
unchanged broad suites are not called fresh. Frozen inputs:
3960; snapshots:2893. The separately dirty
real sibling remains intact. Tools commit:
`a2e985e6f40417432dfb2ef596c76151623f38b2`. Baseline consumer:
`9f83ec050e6a5ae64fa8bbbbb120cc034840e154`. Receipts:
`conker/build/game-randomized-effect-factory-150d278c-private`.

One bounded tools-disabled Sonnet advisory reviewed ABI, palette and unwritten
tail limits after the natural direct match was found. Unsigned DIVU, lifetime
range and byte forwarding were independently confirmed. Its baseline-prototype
concern does not describe the selected owner, whose corrected prototype and
both callers compile unchanged; the claim of a cross-TU mismatch in this
single owner was rejected. Caller binary execution proves ignored V0. Static
instruction equality is not a measurement of runtime stack garbage, nor does
absence of a caller-side store by itself prove arbitrary callee noninterference.
The seeded guest tail check, native 95-byte boundary, palette mutation tests
and actual original helper pins establish the stated limits. Review grants
no matching credit. No subagents or second advisory call.

The historical generated host target is an empty stub; active host applicability
is unqualified. No host transfer/build/launch, Release change, push, gameplay
or hardware acceptance. Scoped Graphify refresh audits all six owner definitions,
retains old IDs/qualification metadata and observes actual hook termination.
README receives aggregate/date rows only. Goal 85% remains active.
