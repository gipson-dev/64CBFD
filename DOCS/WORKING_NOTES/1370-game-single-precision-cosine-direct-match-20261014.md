# Game Single-Precision Cosine Direct Match

## Scope And Baseline

Continue the full additional-source and Game matching goal from consumer
`f4a50dec`, tools `c293b24`, ELF `e7966de8`. Both active repositories are
clean before task edits. Preserve the independently dirty older tools mirror,
original archive, source assembly, private fixtures and frozen host Release.
No push or host transfer/build is part of this Game matching task.

Game `cosf`: VA0x15047C00, ROM0x750B0, 88-word/352-byte slot, comprising
85 code words/340 bytes plus three alignment NOPs. Frame0; F12 float argument
spilled to the caller's SP+0 argument home, F0 float return. The existing
owner is `conker/src/libultra/gu/cosf.c`, built with normal O2/g3 and the
existing C-object padder. Sine's prior104-word direct recovery is retained.

The additional source retains GLOBAL_ASM for cosine, not a C donor. The local
SDK reference `tools/ultralib/src/gu/cosf.c` preserves a separate absolute
angle and copied reduction accumulator. It is double precision and a
structural reference only; retail Game words and float constants govern
the recovered source. SDK files and upstream pins remain read-only.
Reference SHA-256: cosf.c27dfef60a126a427d6ad9080949819a404d88307ecdfeaf24c429adc5015b7d2,
guint.h1d418dde15224d2c57c26195b292b76c7642fb07cecd8ba943ecfa3407bb0c2c.

Immutable before fixtures live in
`conker/build/game-single-precision-cosine/`. Every expected source/header/
image/guard/progress/Makefile hash is pinned; do not recapture failed inputs.

## Steps

1. [x] Inspect complete retail/SDK/source evidence and resume the unsuccessful cosine screens.
2. [x] Screen18 complete copy/literal-type forms; find two whole-slot direct matches.
3. [x] Qualify selected integer-zero absolute comparison, float-zero rounding comparison, separate accumulator copy and all85 code words/three NOPs.
4. [x] Check MIPS/native boundaries, negative coefficient paths, fired faults, rebases and effective controls.
5. [x] Execute the frustum with both recovered trig bodies; keep model proof distinct from gameplay acceptance.
6. [x] Install the qualified body and close every image/code/data/metadata change independently.
7. [x] Extend pinned history projections, run affected regressions, update aggregates and bank tools before the consumer group.
8. [ ] Continue the next actual Game body, failed donor/binding/codec queues and separately stale rectangle image gate; the broader goal remains active.

## Initial Evidence

The selected form preserves `absolute = angle > 0 ? angle : -angle`,
`reduced = absolute`, float period arithmetic and a0.0f rounding comparison.
The integer-zero/float-zero comparisons are mathematically equivalent to
same-typed zeros, but their compiler expression identities retain retail's
two independent zero-register definitions and schedule. The SDK-style copy
also keeps absolute and reduction lifetimes separate. Do not explain this as
a behavior change or add volatile accesses, argument-home writes or guards.

All18 O2/g3 screens compile with no warnings. Configurations2 and6 emit340
code bytes and all352 slot bytes match directly. Configurations0/8 merge the
zero lifetimes and emit336 bytes; removing the copy with the selected zero
types emits340 bytes but differs at15 words. Double-zero comparison forms
emit348 bytes and remain non-matching. Prefix-only/short-tail comparisons
cannot qualify a routine. Receipts retain every configuration.

## Qualification

All11 cosine/pure gates pass23.507s after installation. Selected C emits85
code words/frame0 plus all three original alignment NOPs. Complete owner
and both actual padders agree, no pools/guards/warnings/profile/header changes.
The old20-byte float placeholder is independently recompiled and matched to
the saved baseline. Independent original/C links match at original and0x9000
rebased code/data addresses; no fake unresolved-symbol binding is used.

All13,392 paired MIPS cases cover3,348 input words, two stack phases and
normal/negated inverse-pi coefficients. The latter is an explicitly mutated
data fixture, not a claim of ordinary retail input: it fires the negative
period path that a positive absolute angle and normal coefficient cannot.
Independent binary32 reference values and full available model state agree.
All82 reachable code words fire; offsets0x4C/0x84/0x12C are unreachable branch
duplicates and remain byte-checked. All280 memory prefixes actually fire,
with current PC, integer/FP branch-delay identity and complete available state.
No exception-mode/FCSR/hardware acceptance is inferred from this bounded model.

Native32 O2/O0 each check6,696 cases, with actual public cosf name and separate
cosine constants. Reuse the sine fixture's freestanding SSE2 setup and public
no-IPA return-only control. MIPS NaN return remains7F810000; i386 x87 quiets
it to7FC10000 as independently measured. Only that explicit ABI conversion
is projected in native expectations. Absolute/half-period/parity/pi-tail/NaN
controls all fail as intended under both profiles. No host libm replacement.

All48 paired frustum cases execute compiled recovered cosine and retained
compiled recovered sine, with no trig-return mocks. All four F12 calls and12
plane stores match the independent reference; available states match original
retail instructions. This closes these two math dependencies, not full camera/
culling/gameplay behavior. The next99-word view updater remains a C stub.

## Closed Image And History

The production O2/g3 C-object/padder build succeeds. Independent expected
image changes exactly258 target bytes in352-byte slot and the20-to340-byte
public code extent. Two checked adjacent symbol/string groups reorder:
(D_80098D70,D_80090B50,D_800A6BF0) becomes(1,2,0), and
(D_80085EA8,D_8008ADA8) becomes(1,0). Prior complete symbol tuples, section
bindings and string adjacency are asserted before applying this serialization.
No non-target symbol definition, type annotation or address changes. Unlike sine's
unpadded owner, the existing cosine padder retains relocation words without
introducing raw-object data-type annotations. Do not assume five new types.

Every other serialized ELF byte, all720 protected-data owners/189,088 bytes,
headers, guards, Makefile, original assembly, sine source and progress bytes
remain fixed. No global section, symbol mask or generic metadata exclusion.

The cosine inverse accepts only exact complete-input hashes for ELF/owner,
feeds sine then frustum/constructor/codec/donor history, and passes unknown
or corrupt inputs through unchanged. Original before/after snapshots stay
immutable; do not recapture any old fixture. Current/frozen/capture corruption
controls actually fire. The old rectangle literal-image gate remains separately
stale as proven before these math recoveries; not a fully green legacy suite.

| Input | SHA-256 |
| --- | --- |
| Final ELF | b87dd5bcf0d6549080560feb1122f90d7b57614bdd220c29eaa75e2d0fc0cf0b |
| Cosine owner | 8947b41f56a8854981be155231dfbb5d4f0b885c4c60d4cdc7bba069f8841b09 |
| Retained sine | ae271497692ea1a00abd96bcfed9209458cf8ea694b0df385aa5dddf9fc1a679 |
| Unchanged progress | 005fd7682d37802a2b7591cfb023648b6a083c8df6b957bdfedd737222cad68e |
| Unchanged guards | b0f5425a5a3fbe2a1a44898f5c5499b781cf0598532b595dae1c81c7534b4d99 |

All53 focused/history gates pass85.827s:11 cosine gates,11 sine/pure gates,
nine frustum gates and22 affected history checks, including19 direct donors
and742 copied neighbors. The sine native fixture is reused through explicit
function/reference/constant parameters, with all its original defaults and
controls intact. Project tools checks pass. Tools2a1c847 banks qualification.

One label-only historical sine receipt correction follows in98db41f: say
its fixture uses retained retail cosine assembly rather than claiming the
current production cosine is still a stub. Its connected test freshly passes
1.881s; no code/acceptance gate changes. The source commit pins98db41f after both commits.

Standalone mirror compilation of all six task files and two namespace-bound
pure cosine checks pass. Its two existing task baselines match active HEAD
before copying; only six owned paths change/four additions. Preserve the
independent ddbdd16 history and513 unrelated fingerprints. All801 original
archive file hashes remain unchanged; no upstream/host/Release edits or push.

## Progress And Next

Fresh match-progress: Game2,876/4,831 (59.53%), total3,549/5,504 (64.48%),
different1,955, zero drift. Executable-only total3,409/5,364 (63.55%); the
README retains its140 debugger data-label convention. Conversion counts/bytes
stay5,504/6,044 (91.07%),86.09% total, Game4,831/5,323 (90.76%),85.46% bytes.
Init/Debugger tracked C counts remain exact. Root README gets aggregate rows only.

Full `graphify update .` fails closed at19,077 nodes versus the existing
40,851, preserving19,398 nodes from2,972 still-present excluded files. Do not
force a smaller graph; await the consumer commit's incremental worker.

Next func_1501B0A0: VA1501B0A0, ROM48550,99-word slot, frame0x50, two integer
indices, four trig calls, two func_150484A0 float-helper calls and a final
func_1510B128 view command. Both source and archive currently select stub/ASM,
respectively. Recover its full body/interface and qualify helper contracts,
cached/reloaded view state and linked owner before installation. Then continue
all failed donor/binding/codec/original-Game matching and the separate rectangle
history reconciliation. No whole-goal completion or gameplay claim.

Subsequently completed the 99-word func_1501B0A0 body with thirteen checked
prologue scheduling guards in [Note 1371](1371-view-fov-transfer-reconstruction-20261014.md).
Its final func_1510B128 command remains a production stub and is the next
target; earlier cosine qualification does not establish that command's behavior.

## Post-Bank Verification

Consumer f71d2c96 banks source, tools pin, aggregates and documentation.
All30 post-bank checks pass41.855s; incremental build reports ELF/progress
up to date and preserves b87dd5bc/005fd768. SDK reference hashes and the
prior ae271497 sine owner remain unchanged. The source commit's incremental
graph worker completes at40,861 nodes/81,042 edges, preserving excluded/
curated nodes and skipping only oversized HTML visualization. No forced scan.

Receipt-only tools820566f makes the existing boundary explicit: non-target
symbol definitions are unchanged, while cosine's20-to340-byte extent is
already accounted for. The exact same image gate freshly passes2.114s; its
assertions and all production bytes are unchanged. The final receipt commit
pins820566f. Only the owned cosine test file is recopied after matching the
mirror to the preceding tools HEAD. Older mirror history and513 unrelated
fingerprints remain preserved. No archive edits, push, host or Release work.
