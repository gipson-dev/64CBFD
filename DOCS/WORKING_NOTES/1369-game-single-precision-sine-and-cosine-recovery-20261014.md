# Game Single-Precision Sine And Cosine Recovery

## Scope And Baseline

Continue the full additional-source adoption and Game matching goal from
consumer `afba10d0` and tools `46da39b`. Both active repositories are clean.
The independently dirty older tools mirror and frozen host Release remain
outside the implementation boundary. No source archive edits or push.

The additional archive retains GLOBAL_ASM for Game `cosf` and `sinf`; it
does not supply C donors for them. Retail instructions and constant tables
are authoritative. Init `__sinf` uses double precision and different tables;
it is a structural reference only, not a substitute for these Game routines.

| Function | VA | ROM | Slot | Code | Current Owner |
| --- | --- | --- | --- | --- | --- |
| cosf | 0x15047C00 | 0x750B0 | 88 words | 85 words | src/libultra/gu/cosf.c |
| sinf | 0x15047D60 | 0x75210 | 104 words | 104 words | src/libultra/gu/sinf.c |

Both production owners initially contain false zero-return C placeholders.
Neither retail routine allocates a frame; each spills F12 into the caller's
incoming argument home at SP+0. The sine owner is intentionally unpadded in
the existing Makefile. Do not change that layout policy merely for a match.

The immutable target fixtures are in
`conker/build/game-single-precision-trig/`, with baseline ELF SHA-256
`79eb4f3261dcc2cff366d6e1dcddef48cb1c6e6b923821272d3b56c709a82e10`.
Capture owner/assembly/header/Makefile/progress/guard hashes once; never
recapture them to accommodate a production or test mismatch.

## Steps

1. [x] Inspect complete retail routines, archive owners, constant tables and compiler/layout profiles.
2. [x] Screen complete float C reconstructions without changing production.
3. [x] Qualify sine's exact104-word body, float ABI, coefficient loads, boundaries and native32 behavior.
4. [x] Run connected frustum tests with real sine and separately identified retail cosine, not trig-return mocks.
5. [x] Install only a fully qualified match and prove the complete image/extent/metadata boundary.
6. [x] Extend exact-hash history projections and run affected regression/negative controls.
7. [x] Refresh measured aggregates, indexes and graph; bank tools before the consumer group.
8. [ ] Continue cosine's actual85-word shape and register schedule; no claim that production trig dependencies are finished.
9. [ ] Continue the remaining failed donors, binding recovery, codec dependencies and original Game matching.

## Initial Measurements

Four arithmetic-order forms per function compile under existing O2/g3,
without diagnostics. Sine's ordinary form emits416 bytes and matches all
104 words directly; exchanging the last polynomial add operands changes28
words and is rejected. Exchanging only the final result add emits identical
words. No word guards or compiler profile changes are needed for sine.

Cosine's ordinary form emits336 bytes and differs at78 compared words.
Absolute-value control-flow screens include split/copy/early/parameter and
separate-local forms. The parameter-mutating form emits340 code bytes but
adds stores into the argument home and still differs at58 words; it is not
an acceptable retail replacement. Further local-lifetime screens stay
private. An unsupported asm-processor O1 trial terminates before compilation;
it is not evidence of an O1 code match or a production profile requirement.

The coefficient arrays at80098D70/80098D90 contain identical float words,
including BE2AAAA6,3C088769,B94FB7FD,362EDEFA. The separate Game reduction
constants are3EA2F984,40490FDC,330885A3. Preserve these retail values; do not
replace the split pi approximation with a host math-library implementation.

All16 separate-absolute local-order/declaration/reduction screens emit336
bytes and differ at71 compared words. These are unsuccessful measurements,
not matches. Short object tails are explicitly counted as uncompared slot
words; a prefix-only comparison cannot qualify a routine.

## Sine Qualification

The new complete-owner compile emits104 words, no frame adjustment, no pools
and no compiler warnings. The unchanged production profile is O2/g3, with
the existing unpadded owner rule. Both private padders retain all104 words.
Independent retail assembly and C links agree at original addresses and a
0x9000 code/data rebase. No production guard or shared header is changed.

The boundary corpus covers3,348 input words, both stack phases, all512
nine-bit exponent classes, adjacent threshold/half-period values, signs,
signed zeros, subnormals, finite extremes, infinities and NaN payloads.
All6,696 paired MIPS cases agree with an independently ordered binary32
reference and the full available instruction-model state. All103 reachable
words fire; offset0xCC is an unreachable duplicated branch-delay operation,
which remains byte-checked. All96 fired memory prefixes preserve actual PC,
delay identity, access order and available state. No FCSR/exception-mode claim.

Native32 O2 and O0 each check3,348 inputs. Effective cutoff/parity/pi-tail/
NaN controls fail as intended. This is freestanding SSE2 binary32 arithmetic,
not host libm substitution. Initial test-fixture repairs use the actual
normalized-pool API shape and existing freestanding flags, not dependency
installation or warning suppression. The zero-return float placeholder's
public extent is20 bytes, independently recompiled and matched to baseline;
the generic12-byte integer-placeholder assumption was rejected.

The i386 ABI has a separate measured boundary: the first NaN input7F800001
returns retail7F810000 in MIPS, but native7FC10000. Disassembly shows the
external float return passes through x87 FLDS/FSTPS. An independent public
return-only/no-IPA probe must reproduce that conversion under both profiles,
while verifying the global still contains raw7F810000. Native expected values
project exactly that observed ABI conversion; MIPS tests still require the
unaltered retail word. A private static probe initially used a GCC SSE return
convention and correctly failed; it was not treated as an x87 control.

All48 connected frustum cases execute real sine instructions and separately
identified retail cosine assembly, compare all12 plane stores and all four
F12 calls, and preserve full available state. They do not use fixed trig
return mocks. Production cosine is still a stub: no functioning production
camera/culling, hardware/FCSR parity or full gameplay acceptance is claimed.

## Closed Image And History

The production rebuild succeeds. Only316 bytes in the416-byte sine slot and
its20-to416-byte public extent change in executable ownership. The linker
also changes exactly six referenced data symbols from NOTYPE to OBJECT:
D_80085EB0/EB4/EB8/EBC,D_80098D90,D_8002C920. Names, values, sizes and section
bindings remain fixed. Two adjacent symbol/string groups exchange positions:
(D_800A5698,D_800A1398) and (D_800A569C,D_800A139C), preserving definitions.
The expected image validates complete prior tuples and string adjacency,
constructs only those exact changes, and equals the complete serialized ELF.
No generic metadata exclusion or address mask is used.

All other ELF bytes, protected data189,088 bytes/720 owners, original
assembly, cosine owner, shared headers, Makefile, guards and progress are
fixed. Original snapshots are not recaptured. The new sine inverse accepts
only exact complete-input hashes, feeds the existing frustum-to-constructor-
to-codec/donor history chain, and leaves unknown/corrupt inputs unchanged.
Installed/frozen/capture corruption controls actually fire. The old rectangle
literal-image fixture stays separately stale, as proven in Note1368; no claim
that the entire legacy suite passes.

| Input | SHA-256 |
| --- | --- |
| Final ELF | e7966de8419027fba66c6d9ae8a2853ec5b3d0ce756303a823daa4b24e8e9fe9 |
| Sine owner | ae271497692ea1a00abd96bcfed9209458cf8ea694b0df385aa5dddf9fc1a679 |
| Unchanged progress | 005fd7682d37802a2b7591cfb023648b6a083c8df6b957bdfedd737222cad68e |
| Unchanged guards | b0f5425a5a3fbe2a1a44898f5c5499b781cf0598532b595dae1c81c7534b4d99 |

The final42-check scoped suite passes66.813s:9 sine gates,2 pure screens,
9 frustum checks and22 affected history checks, including19 donor bodies and
742 copied neighbors. Project tools checks pass. Standalone mirror byte-
compilation of all six task files and two namespace-bound pure tests pass;
the initial unqualified standalone package name fails without consumer layout.

## Progress And Banking

Fresh match-progress reports Game2,875/4,831 (59.51%), total3,548/5,504
(64.46%), different1,956, zero drift. Executable-only total3,408/5,364
(63.53%); the README convention still includes140 debugger data labels.
Conversions remain5,504/6,044 (91.07%), converted bytes86.09%; Game remains
4,831/5,323 (90.76%),85.46% bytes. Init/Debugger tracked C rows remain exact.

Tools c293b24 is committed first. Copy only six task files to the older
mirror after proving its two existing task baselines match the active HEAD.
Keep its independent ddbdd16 history and509 unrelated fingerprints intact.
All801 original archive file hashes remain unchanged. No push or host work.

`graphify update .` fails closed on19,064 nodes versus the existing40,839;
preserve19,398 nodes from2,972 still-present excluded files. Never force the
smaller graph. Await the source commit's incremental worker before closing.

## Next

Continue cosine's85-word/frame0 body and three NOPs with actual absolute-
value and rounded-period lifetimes. Do not install the parameter-writing
340-byte form or normalize broad register differences without qualification.
Retain all private failed-screen receipts; they are evidence, not completion.
Then continue the full failed-donor/binding/codec/original-Game queues and
the separate rectangle historical gate. The active goal remains unfinished.

## Post-Bank Verification

Consumer d1a326eb banks the source, tools pin, aggregates and documentation.
All19 post-bank checks pass38.973s. Incremental build reports ELF/progress
up to date and retains e7966de8/005fd768. Main and active tools are clean
before this receipt commit. Older mirror HEAD stays ddbdd16, with exactly
six task changes/four additions and509 unrelated fingerprints preserved;
all515 final dirty-path hashes are retained. No mirror history duplication.

The source commit's incremental graph worker finishes at40,850 nodes /
81,030 edges, preserving the curated/excluded-file boundary and skipping
only oversized HTML visualization. The prior full scan's fail-closed result
was not overridden. No push, archive edits, host build or Release operation.
Cosine and the separately stale rectangle historical image gate remain open.
