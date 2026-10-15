# Texture Vertex Span Lifetime Role Tradeoffs

## Scope And Steps

Continue the SAME func_1510BF60 from consumer bf652c1e/tools a01819f and
[Note 1382](1382-texture-vertex-span-optimizer-allocation-and-controlflow-traces-20261015.md).
The previous turn made progress by locating the wrong roles in UOPT output;
this turn tests the resulting source-lifetime hypothesis. No C installation,
new match credit, archive import or reduction of the full source/Game objective.

1. [x] Compile27 complete lifetime, endpoint, induction and copy controls with existing locals/ABI/profile only.
2. [x] Capture two fresh compiler pipelines and one mode5 allocation trace; distinguish a partial register recovery from an overall byte match.
3. [x] Qualify two selected public candidates, an effective clobbered-count control, private prefixes and previous compiler/image gates.
4. [x] Preserve production/archive inputs and unrelated mirror work; bank tools first.
5. [ ] Resolve independent count/opcode allocation, retained end-tag and retail control flow before installation or credit.

## Bounded Source Controls

New tools/experiments/game_texture_vertex_span_lifetimes.py reuses HOMES,
complete-owner compilation, linking and immutable captures. Four groups contain
8 live-role controls,6 shift endpoint controls,10 induction/count-placement
controls and3 copy-propagation controls:27 completed compilations, zero IDO
diagnostics, none improves the HOMES339-word/frame0xA8/258-difference seed.
All fourteen original local declarations and the resolver/public ABI remain.

Reusing the stage1 flag with count/minimum/index worsens matching. Merging the
triangle count into opcode is more informative: it recovers maximumT0/countA3,
but also moves the scanner opcode from retailV0 toA3. The complete target is
still339 words/frame0xA8 and worsens to274 differences. It is NOT a better seed.
Moving the reduction index initialization before decode emits310 words/frame
0xA0 with288 differences and extentSP+98 instead of retailSP+A0. Direct raw
disassembly confirms a single-element maximum loop, not the original peeled/
four-way reduction; the minimum reduction remains unrolled. Do not install it.

All three split opcode-to-count copy forms emit byte-identical target code and
relative relocations to HOMES: copy propagation removes the attempted lifetime
distinction. Five endpoint forms retain339 words/258 differences; one count-
derived cursor form grows343 words/265 differences. Equal difference counts
do NOT establish byte identity. Exactly6 of27 targets/relative relocations
are identical to HOMES:1/8 role,2/6 endpoint,0/10 induction and3/3 copy forms.
Three endpoint forms exchange these four address-setup words only:

| Target Offset | HOMES | End-First / End-Before-Loop / Cursor-From-End |
| --- | --- | --- |
| 0x1CC | 27A20058 | 27A30064 |
| 0x1E0 | 27A30064 | 27A20058 |
| 0x22C | 27A20058 | 27A30070 |
| 0x240 | 27A30070 | 27A20058 |

Every other target byte and relative relocation stays fixed for those three.
The first informal suggestion that all endpoint forms normalize identically
was overbroad; the test checks actual parsed object words, not just counts.

## Fresh Compiler Evidence

Extend the existing phase adapter with optional explicit source-role markers.
Defaults remain unchanged and are freshly regression-tested. Distinct semantic
roles may share one frontend local/register; missing, duplicate or absent count
roles fail closed. Do not alter compiler binaries, default profiles, headers,
production source or the existing owned-child/fingerprint/capture validators.

| Body | CFE Records | UOPT Records | Fired UGEN Events | Word Differences |
| --- | ---: | ---: | ---: | ---: |
| count-as-opcode | 1,212 | 1,299 | 194 | 274 |
| index-init-before-decode | 1,213 | 1,217 | 167 | 288 |

Both normal/traced objects remain identical, and each standalone target exactly
reproduces its complete-owner target including relative relocations. In the
first source, count and opcode share CFE M-16 and UOPT R7/A3; maximum stays
M-28 but changes to R8/T0. The second source assigns maximumR10/T2, countR7/A3
and nestedR9/T1. Both still contain two unallocated -33 ldc records, with no
retained end-tag register. The physical homes of the310-word source also move.

Fresh mode5 evidence for count-as-opcode reports31 variables/50 constraints,
versus the preceding seed's32/51. Shared opcode/count is expression17, color6,
forbidden1..5; maximum is expression8, color7, forbidden1..6. They interfere
with each other. This proves the source-role/allocation tradeoff, not a measured
numeric weighting formula or generic color-to-GPR mapping. Optimized STR R
records and observed UGEN operands supply the physical-register evidence.
Numeric timing/cost values remain unsupported because debug real printing is
suppressed. No additional advisory, provider setup or debugger attach.

## Qualification And Preservation

Each of the two selected candidates passes3,872 guest cases at both SP phases
and1,936 native32 cases per O2/O0 profile. A compiled control clobbers the shared
opcode/count before maximum reduction; guest execution returns a mismatch and
native statuses2/2 prove a returned failure, not a crash. Do not extend this
semantic qualification to all27 source controls. Full private state remains
wrong; count-as-opcode differs at55 of63 paired fired prefixes, first at cut8.
Retain the defined-vertex-base domain and all existing native opcode bridges.

The first14-check run fails48.117s because GCC correctly rejects the now-unused
count declaration kept for IDO's original debug-local layout. Annotate only
that declaration with GCC's unused attribute in the native test adaptation;
assert every executable statement after the resolver is unchanged. No global
warning suppression, synthetic initialization or alteration of the IDO body.
The known maybe-uninitialized vertexBase warning remains. This native-only
annotation is not evidence of private-frame or target-hardware equivalence.

All14 final selected checks pass56.686s: six new consumer tests, two pure tests,
two preceding pure checks, one preceding fresh phase-capture regression and
three preceding matrix installed-image/corruption/inverse gates. Tests freshly
capture both selected pipelines/mode5, not only saved summaries. Shared tools
checks, standalone four-file compile and two namespace-bound pure tests pass.

All18 production hashes and all801 archive fingerprints are freshly unchanged.
ELF2131709f/progress3ad7466c, source owners, original assembly, guards, profiles,
headers and layouts remain fixed. Root README and metrics stay unchanged:
Game2,884/4,829 (59.72%), total3,557/5,502 (64.65%), different1,945, zero drift.
The current scanner remains a production stub and the archive has no C donor
for it. The broader additional-source/Game and separate rectangle queues remain.

Gate all577 initial mirror fingerprints and independent ddbdd16 HEAD. Update
only the previously owned phase adapter and three new absent owned paths.
All576 other initial fingerprints/HEAD stay fixed, leaving580 expected dirty
paths. Hash-check exact owned copies; no reset, mirror commit or history
duplication. Tools518e1ab banks these four research paths before consumer pin/
docs. Keep the independently dirty mirror intact.

The full graph update fails closed at19,211 versus40,993 nodes and retains
19,398 nodes from2,972 excluded-but-present files. Do not force the smaller
scan; await the consumer's incremental commit worker. No push or host source,
build, launch or frozen Release operation. This is further matching evidence,
not completion of the full requested source audit/Game work.

## Next Action

Keep HOMES as the best seed; do not replace it with the274-difference partial
register recovery or310-word induction form. Avoid repeating these27 controls.
Inspect the actual UOPT priority/lifetime decision for independent count and
maximum values; plain copies are propagated away, and a full opcode/count
merge binds too much scanner state toA3. Keep end-tag allocation, stage1 branch-
likely shape and early vertexBase/max+1 return preparation unresolved. Require
complete private/prefix, actual connections, rebases and closed image evidence
before any production change or C-match credit. The full goal stays active.
