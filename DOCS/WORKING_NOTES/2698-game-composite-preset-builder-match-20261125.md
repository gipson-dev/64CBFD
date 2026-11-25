# Composite preset builder match - 2026-11-25

`func_150B5A3C` replaces its zero-return placeholder with a semantic, correctly
typed void three-argument callback in `conker/src/game/generated_E2DA0.c`.
VA150B5A3C..150B5C38 / ROME2EEC..E30E8: **127 body/slot words, 508 bytes,
frame144**. There is no alignment tail. **76 word values and bindings emit
directly; 51 expected-word guards recover register allocation and independent
register/private-store scheduling. Raw C is not byte-exact.** No private-frame
map, inserted/omitted word, dummy local, record-size or compiler-profile change
is used. All11 raw/padded neighbors and owner pools stay fixed.

Actual production is **4,677 / 5,528 (84.61%)** total, **4,004 / 4,855
(82.47%)** Game, Init492/492 and Debugger181/181. Zero address drift,
851different; **22 more verified matches to85%**. This routine earns one
match. Callers and helpers earn zero new credit, with conversion rows and
denominators unchanged.

The complete aligned pristine-ROM census finds exactly two literal direct JALs,
at ROME2E90/E2ED0 (VA150B59E0/150B5A20), both in `func_150B5950`, and no
literal entry pointers. Top-level retail ASM has the same two references.
Arguments are a valid three-float position storage pointer, unsigned8 mode and
signed32 extra. The previous unspecified-argument s32 declaration is repaired
along with the actual caller. Both sites ignore the result; retail does not
produce a meaningful result and the restored interface is void.

The established `CompositeEffectInput` layout is reused from the existing
composite-effect recoveries: **116 bytes, 112 initialized bytes and four holes**
(padding59[3] and padding6B). It retains complete real extents. The caller's
three-float local now explicitly uses a12-byte union with named `array[3]` and
`vector` members. Array helpers receive the array member, and this callback
copies the vector member. This removes the bare float-array-to-struct pointer
cast. The representation/prototype repair leaves the caller and every other
owner function byte-for-byte unchanged. Native32 strict-aliasing tests use the
same typed union; neither a resized object nor spare/dummy storage is involved.

The packet has baseCount5/countRange5 and captures all three position words
before any provider. Its first float base is20.0; three live coefficients are
`D_8009FCA0`, `D_8009FCA4`, `D_8009FCA8` at field18Range/field1CBase/
field20Range. All12 coefficient bytes are pinned to pristine ROM and frozen
ELF. Radius base/range are39.0/35.0. First base/range are0/255; second
base/range are-31/80. Header byte base/range are3/2 and short base/range20/30.
Field40=1; fixed42/43/44=4/2/3. Color bases45/46/47/48,4D/4E/4F/50 and55
are255, with all nine corresponding ranges zero. Fixed57/58=3/36,
field5C=200005,field60=60600,field64/66/68=8/31/1,field6A=0,field6C=1.0,
field70=-1,field71=0 and both tail72/73 bytes FF. The four holes stay unspecified.

`func_15152B38(&packet,mode,extra)` receives the full packet. Then
`func_150B5E34(position->array,mode,extra)` and
`func_150B6000(position->array,mode,extra)` run in that order, each reloading
the original argument homes. The first companion remains an unmatched
placeholder elsewhere in this owner; its observed three-word ABI is treated
as an opaque provider here. No end-to-end effect/gameplay claim or companion
matching credit follows from recovering this dispatcher.

Initial C emitted128words/frame144/101differences. Bounded field-order,
shared-value, signed-byte and copy-spelling probes were kept private. Moving
fixed44=3 after firstRange=255 recovers127words/53differences with matching
bindings; regrouping the independent header assignments reduces that to51.
The explicit union representation emits exactly the same raw bytes/bindings
as that best source and preserves all11 neighbors. Scalar copies emit127/109;
memcpy emits124words and adds a provider, and was rejected. No profile, layout,
padding or instruction omission was used to force the count.

The scoped symbolic proof executes all127 words and compares all three
provider boundaries, complete116-byte packet, full144-byte private frame at
every call and return, all return registers and FCSR. Public input bits and
provider epochs are symbolic. Providers can rewrite the complete passed packet
and public objects while preserving unpassed incoming homes. Four independent
rebases include HI/LO carry and different jump regions. Eight supported,
completely executed controls change count, short range, resource, position
load, mode home, control byte, coefficient binding or third-provider binding;
each is rejected. The mapped ordinary single-thread object contract includes
disjoint callee-private frame/incoming homes and the valid12-byte caller buffer.
Raw private write/fault order is not claimed equal; this is not general SMT or
all-machine-context proof. The reused core's return-one assertion was replaced
only in the local void-callback runner; that interpreter assertion is not a
negative control or matching evidence.

Both complete owner padders agree. The actual three-command Make route
replays the unchanged retail profile. An independent reference rebuild uses
frozen old C, replacing only this original508-byte ASM body through the next
function `func_150B5C38`. Complete production equals the predicted ELF:
**427 changed bytes, zero exclusions**. All189,088
protected Game data bytes across720 owners, old guards, layout and unrelated
frozen inputs are fixed. Only51 guarded rows append. All102 guarded corruptions
reject,152 unguarded corruptions remain visible, nine binding pins reject,
both oversized probes reject, and20 GNU links/40 rebased guest runs pass.

Guest qualification passes **672cases per five
streams**, four retail-equivalent plus raw, and **222
fault quads** for the normalized/original streams. It covers every mode byte,
32-bit extra boundaries, all rounding-mode settings, finite bit-copy extremes,
complete116-byte packets, provider packet/public mutation, and guest-only
incoming-home redirects. Complete private state and registers agree at return.
Only the normalized/original streams claim exact fault-prefix order.

Native SDK32 qualification passes **656legal cases
each at O0/O2/O3**, explicit SSE rounding/status settings, strict aliasing and
UBSan traps. It observes112 initialized packet bytes and52 canonical public
bytes at every boundary, excludes four unspecified bytes, and never inspects
unpassed private storage. The target has no FP arithmetic; flags are preserved
between providers. All11 wrong-source controls exit with comparison42, and
signals/traps do not count as successful controls. Ghost-home cases are guest-only.

The full original59-word parent runs **1152cases per
stream**, with104 connected children per stream. Both direct sites, stale
attachment, missing matrix, neither/first/second/both effect routes, and reloads
of mode/extra/threshold/matrix after callbacks are checked. There are58 visited
parent words; the original orphan load at150B598C is unreachable and preserved.
The original12-word `func_150B60E0` wrapper executes completely, with its source
vector and all three transform arguments checked. Transform internals remain
contracted. Two wrong-child controls complete the parent then fail comparison.
The initial uncached fixture repeatedly parsed immutable data layout; it
completed successfully before a proposed interruption, so no process was killed.
Exact-input caching now avoids those repeated reads, with unchanged case scope.

Original helper execution uses this routine's actual packet/arguments in128
cases each. The270-word composite helper visits all256 nontrap words, while
14 divisor traps remain unreachable, and emits816 child packets under bounded
RNG/vector/allocation providers. Complete24-byte headers and60-byte payload
extents are observed. The matched56-word trailing helper executes completely;
its full6-byte header (including its seeded hole) and12 coordinate bytes agree.
These helper checks make no FCSR or allocator-internals claim and earn zero credit.

| Tools execution | Seconds | Qualification |
| --- | --- | --- |
| preinstall-primary | 137.154s | 5 fresh / 0 reused |
| preinstall-sibling | 119.584s | 5 fresh / 0 reused |
| installed-primary | 105.978s | 5 fresh / 0 reused |
| installed-sibling | 113.351s | 5 fresh / 0 reused |

Both tools copies pin exact task/import/data/profile/artifact fingerprints.
Closed verified dependency files are shared immutably to avoid duplicating the
old85MB overlay; eleven task files are independent copies. Three newly used
old oracle dependencies were added to the pre-adoption freeze; existing input
hashes stay fixed. Shared `make tools-check` passes. The separately dirty tools
sibling is preserved. Claude calls for this routine: zero.

Baseline consumer `ae1968f18964449dcef0c7bb1b6e16478cdf6584`.
Tools commit `ce1013a2baccbf512250698df52f791e40288448`.
Production ELF SHA256 `d33881a54755387c1304c4cb407426f42bbcb0ca74af1fefcf2906c9a656e5e8`.
Padded owner SHA256 `28816d2cc67673a509207668c772d6532aebbaa1c9c77d548643815acbbc45d2`.
Freeze: 3710inputs/2625copies.
Receipts: `conker/build/game-composite-preset-150b5a3c-private`.

The root README receives aggregate rows/date only. Native Graphify update,
actual hook termination and scoped AST/old-ID/qualification-metadata retention
follow before banking. This is not a full-corpus extraction or host/runtime
acceptance claim. No host build/launch, Release change or push is performed.
Keep the85% objective active. Next, inspect the still-unmatched companion
`func_150B5E34` after this complete checkpoint is banked; older rejected
C9BDC/matrix/handwritten candidates remain private and uncredited.
