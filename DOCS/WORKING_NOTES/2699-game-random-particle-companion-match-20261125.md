# Random particle companion match - 2026-11-25

`func_150B5E34` replaces its zero-return placeholder with a semantic typed
particle descriptor builder in `conker/src/game/generated_E2DA0.c`.
VA150B5E34..150B6000 / ROME32E4..E34B0: **115 body/slot words,460 bytes,
frame152**, no alignment tail. **94 word values/bindings emit directly;
21 checked guards normalize GPR allocation, an unpassed four-byte flag
spill SP24->20, and independent argument scheduling. Raw C is not byte-exact.**
The frame size, saved RA and incoming/outgoing homes stay unchanged. No
insertions, omissions, dummy storage, shortened descriptor or profile change.
All11 raw/padded neighbors and owner pools remain fixed.

Actual production is **4,678 / 5,528 (84.62%)** total, **4,005 / 4,855
(82.49%)** Game, Init492/492 and Debugger181/181; zero drift and850different.
**21 more verified matches reach85%.** One new match, zero helper/caller
credit; conversion rows and denominators unchanged.

The complete aligned pristine-ROM census finds only two literal direct JALs,
ROME30C0/E32BC (VA150B5C10/150B5E0C), in `func_150B5A3C` and
`func_150B5C38`; no literal entry pointers. Both discard the result. Retail
leaves the last factory's allocation pointer/null in V0, so recovered C
explicitly forwards that pointer as `void *`. This preserves observed behavior;
ignored call results alone do not establish original source-language intent.
Arguments are the existing valid12-byte position union, unsigned8 mode and
signed32 context. The first parent's prototype/call now use the union pointer,
with unchanged emitted bytes. The other parent remains an unmatched C stub;
its original ROM execution below earns no source-matching credit.

The complete established particle layout is112bytes. **98 initialized bytes,
14 unspecified bytes** at5C..5F and66..6F. The original61-word factory
`func_15130280` copies all112bytes, so the untouched tail is retained.
Field04 is20000 despite an older related declaration's zero04 name. Local
signed tag62 joins63/64 at-1; this retains layout and encodes FF. Naming and
signedness follow this routine's stores without claiming unavailable source.

Descriptor fields: flags00=200005,field04=20000,code08=4403,
lifetime4+(unsignedRNG%7),fields0C/10=0. All nine color bytes14..1C areFF;
palette1D=43,halfwords1E/20/22=3/85/1. Scale24=1.0. Extents28/2C share
the separately rounded multiply-then-add `sample*500.0f+500.0f`. Position30
copies all three input words **after** float RNG and **before** the next
integer RNG. Velocity3C,acceleration48 and parameter54 are seven zero floats.
Flags58=C201 plus independent integer-RNG low-bit choices40/80;
bytes60/61=6,62/63/64=FF,65=4. Factory args are(&packet,1,0,0,mode,context),
with mode/context reloaded after the draws. Its allocation kind is82,size168.

Initial complete union-pointer and void spellings both emit115/frame152/
21differences and identical raw bytes/bindings. Explicit pointer forwarding
is selected. Scalar position copies emit114words and were rejected. Real
flag/argument-local and lifetime spellings were bounded: argument locals and
named extent produce frame160; changed declaration order gives52differences;
conditional and nested-block versions change bindings/length. Two flag locals
or a register hint leave21differences. No dummy/size/profile workaround.

The four-byte unpassed flag spill is the only private layout difference.
The scoped symbolic proof checks a bijection swapping raw SP20..23 and24..27
against retail identity; neither span is passed. Complete mapped152-byte
frames agree at every provider and return, as do the full112-byte packet,
all return registers and FCSR. Five provider boundaries, two ordered FP
operations, four low-bit classes covering all115 words, arbitrary lifetime
RNG bits/public epochs, four rebases and10 supported complete controls pass.
The raw physical private bytes/store order/fault order are not claimed equal.
This is a bounded structural proof, not general SMT or all-machine-context proof.

Both full owner padders agree. Actual three-command Make replays the fixed
retail profile. Independent frozen-old-C/original460-byte-ASM reconstruction
through next function150B6000 equals production across the complete ELF:
**348 changed bytes, zero exclusions**. All189,088 protected
Game data bytes across720 owners, existing guards and unrelated inputs stay
fixed.21 guard rows append. All42 guarded corruptions reject;188 unguarded
corruptions remain visible,5 binding pins reject, both oversized probes reject,
and20 GNU links/40 rebased guest executions pass. No owner data/literal pools.

Guest qualification: **632cases/five streams**,
four retail-equivalent plus raw; **216fault quads**
for the retail-equivalent streams. Every mode byte, unsigned modulus boundaries,
all parity pairs, four rounding modes, finite ordinary/inexact FP samples,
position bit-copy extremes including nonfinite values, pointer/null outcomes,
public/packet mutations and guest-only incoming-home redirects are covered.
Raw fixtures explicitly rename only the four-byte spill's unused private
partner bytes. Full mapped frames at calls/return agree; only the normalized
streams claim exact access-fault prefixes. Native providers do not inspect
unpassed private storage or redirect incoming homes.

Native SDK32 uses the complete union and112-byte descriptor, strict aliasing,
SSE explicit rounding/status controls and UBSan traps. **1024
legal calls each at O0/O2/O3**, all256 mode bytes, four rounding modes/sticky
flags, finite/subnormal/max samples, provider position mutation, full112-byte
copy and allocation/null returns pass. It observes98 initialized bytes and
excludes14 unspecified bytes.11 wrong-source controls complete the target then
return comparison42; signals/traps never count as rejection evidence.

Both complete127-word original parents execute the child in
**392cases/stream**, across all five child streams.
Each parent visits all127words; one child per case, both direct call sites,
post-child parent-home reloads, ignored child returns, all112 child bytes and
mapped frames, and retained116-byte parent packets are checked. The first
parent is byte-pinned to the frozen ELF. The second is explicitly ROM-only:
its frozen slot is still the12-byte placeholder plus zeros. Two wrong-child
controls complete the parent then fail comparison. Parent provider internals
are contracted; caller credit remains zero.

Original factory/copy qualification uses actual captured target packets in
**128cases**, including64 successful full112-byte copies.
Both original windows are pinned to pristine ROM and frozen ELF. The factory
visits all41 words reachable for actual kind1/null-extra inputs; six alternative
kind-dispatch and14 optional-extra words are unreachable for this caller.
All11 byte-copy words execute. All14 seeded unspecified source bytes are
copied, input stays fixed, allocation canaries and byte9C zero are checked,
and size108/wrong-destination controls complete then fail. Allocator internals
are bounded; no helper FCSR or new matching credit is claimed.

| Tools execution | Seconds | Qualification |
| --- | --- | --- |
| preinstall-primary | 148.457s | 5 fresh / 0 reused |
| preinstall-sibling | 114.045s | 5 fresh / 0 reused |
| installed-primary | 110.869s | 5 fresh / 0 reused |
| installed-sibling | 122.502s | 5 fresh / 0 reused |

Both tool copies pin task/import/data/profile/artifact bytes. The second copy
links2092 immutable verified dependency files and owns11 new task copies;
existing frozen input hashes are unchanged. One old dependency receives an
additional snapshot copy; shared `make tools-check` passes. Independently dirty
`64CBFD Tools` remains preserved. Freeze:3722inputs/
2638copies.

To relieve the observed C: space failures,156 closed derived ELF copies were
verified byte-for-byte against their own sealed baseline images, then atomically
replaced with hardlinks to those images. All original paths/hashes and baseline
contents remain intact;249,667,584 duplicate allocated bytes are reclaimed.
Shared files are read-only to make accidental old-writer truncation fail closed.
No source, live build image, active task output or host Release was linked.

One packet-only ClaudePro advisory,119.687s, zero tools/MCP/tool uses; all six
findings independently reconciled. Its SP45 palette wording is corrected to
descriptor1D. Original intent remains inferred. Fixture-only errors corrected
before successful gates: relocatable versus linked JAL SHA comparison, missing
libc32 headers (reused existing freestanding SDK32 route), one generated ASM
string escape, and an attempted ELF-equality assertion for the known unmatched
second parent. These are not source failures or negative controls.

Baseline consumer47ccf114b6efb26757040a4a1754e4af4b2d50e3.
Tools commit`a1941007fa593b82250a5fc8795266c6ad4161b5`.
Production ELF SHA256`8216fda1fc97bfcbd0b9e16dd59920e1224758e2e8299a1aa5f23aafeef184ec`.
Padded owner SHA256`496b8a7740af6f7e0697b06b3f5d56a42b9df4b011135ae80edd03e455051fde`.
Receipts:`conker/build/game-random-particle-150b5e34-private`.

Root README receives aggregate rows/date only. Native Graphify update, actual
hook termination and scoped old-ID/proof retention follow before banking.
No full-corpus extraction, host/runtime acceptance, host build/launch, Release
change or push. Keep85% goal active. Inspect the companion parent150B5C38
after this checkpoint is sealed; older private/rejected candidates stay uncredited.
