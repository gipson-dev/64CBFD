# Sibling composite preset and caller storage - 2026-11-25

`func_150B5C38` now has a semantic, typed descriptor builder in
`conker/src/game/generated_E2DA0.c`. VA150B5C38..150B5E34 /
ROME30E8..E32E4: **127 body/slot words,508 bytes,frame 144**, no alignment
tail. **76 instruction words and their bindings emit directly;51 checked guards normalize
GPR allocation and independent initialization scheduling. Raw C is not
byte-exact.** Complete private frame 144, incoming/outgoing homes, saved RA,
and complete116-byte packet agree at all three providers and return.
No private spill map, insertions, omissions, dummy storage, narrowed packet,
or compiler-profile change. All 11 target-owner neighbors/pools stay fixed.

Production recount: **4,679 / 5,528 (84.64%)** total; **4,006 / 4,855
(82.51%)** Game; Init492/492,Debugger181/181; zero drift,849different.
**20 more verified matches reach85%.** One new match; zero additional
caller/helper credit. Existing conversion rows and denominators are fixed.

The aligned pristine-ROM census finds two direct JALs,9EB84/AF628
(VA150716D4/15082178), and no literal entry pointers. The parents are
`func_15071690` (23 words/frame 40,already C) and `func_15081E78`
(466 words/frame 944,GLOBAL_ASM). Both pass(position,255,1) and ignore
the result. ASM-only grep missed the first caller because it has no residual
function ASM file. The recovered preset returns void and calls15152B38,
150B5E34,150B6000 in that order, reloading mode/context/position homes.
The matched particle companion uses its typed union pointer and forwards
its pointer/null result; this preset ignores it. The trailing helper takes
the actual float-array member. No arbitrary unrelated aggregate cast is used.

`func_15071690` previously passed an undersized scalar `s32 sp1C` as a
12-byte transform output, with an unused `pad0`. The repaired function in
`conker/src/game_981E0.c` declares a genuine12-byte position union before
its actor pointer, removes both scalar/pad, and uses typed transform/preset
prototypes. This emits **all 23 original words and bindings directly**, frame 40,
with no guards. Actor-pointer-first and register-hint experiments each leave
two SP-offset differences and were rejected. The full manual owner is audited:
327 other raw functions,normalized pools,and 36 existing diagnostics stay
fixed; its **entire328-function padded object is byte-identical to baseline**.
The producer already had matching credit; the storage repair earns zero more.

The descriptor reuses the established116-byte composite schema.112 bytes are
initialized; four holes59..5B/6B remain unspecified. Base count/range13/8;
position08..13 copies all 12 input bytes. The four float coefficients at
8009FCAC/FCB0/FCB4/FCB8 are pinned across pristine ROM and frozen ELF.
Radii152/100; first0/255; second-20/50; header byte3/2; short20/15;
field40=1; fixed42/43/44=4/2/3. Color bases45/46/48 and 4D/4E/50 are255,
47/4F are180; base55=255; all nine ranges zero. Fixed57/58=3/36;
field5C=200005,60=60600;64/66/68=8/31/1;6A=0,6C=1.0,
70=FF,71=0,72/73=FF. Semantic names follow established field roles without
claiming unavailable original source names.

Both target padders agree. The actual Make routes are replayed for both owners:
three commands for the generated target and five for the manual GLOBAL_ASM
owner, including preprocessing/postprocessing. No new diagnostics. Independent
old-C/original508-byte-ASM reconstruction matches the complete proposed and
production ELF: **483changed bytes,zero exclusions**.
The producer object is explicitly included and verified identical; no dependent
object is silently excluded. All 189,088 protected Game data bytes across 720
owners remain fixed, as do historical guards and unrelated frozen inputs.

All 102 guarded corruption probes reject;152 unguarded probes remain visible;
11 binding pins reject. Both oversized probes reject.20 GNU links and 40 rebased
guest runs cover four addresses/low-half carry patterns. Symbolic structural
proof covers all 127 words,arbitrary public input bits/provider epochs,complete
frame/packet at all three providers and return,all return registers/FCSR,
four rebases,and eight effective supported controls. This is a bounded proof,
not general SMT or every machine context. Raw private store/fault order is
not claimed equal. Native providers never inspect unpassed incoming homes.

Guest qualification: **672 cases/five streams**,
four retail-equivalent plus raw,**225fault quads**
for the four retail streams. Full116-byte seeded packets,112 initialized bytes,
all 256 mode values,32-bit context boundaries,position bit-copy extremes,
public/packet mutation,and guest-only incoming-home redirects are checked.

Native qualification compiles the actual target and repaired producer in
separate translation units plus providers,using compatible shared types and
the complete812-byte SDKactor. Each O0/O2/O3 profile runs **656 direct target
calls and 1,312producer invocations**, with -m32, strict aliasing,UBSan traps,
LTO,and type-mismatch errors. All 256mode/producer-flag bytes,matrix0/1,
rounding/status preservation,and 56 canonical public bytes are checked.
All 53 packet fields have independent offset/width pins; both union members
are pinned at offset 0, and the actual580-byte SDK matrix object has a typed pointer.
The producer's escaped local position is observed only while its lifetime is
active; a final snapshot is taken inside the last provider.13 deliberately
wrong source variants complete and return comparison42; signals/traps do not
count. Four unspecified packet bytes are excluded from native reads.

Both original parent windows and the12-word geometry wrapper are pinned to
ROM and frozen ELF. Per distinct child stream: **512manual-parent cases and
6,144large-parent cases**,1,392connected children. All 23manual and 12wrapper
words execute;173of466large-parent words execute. The large-parent scope is
complete entry-to-return state0/state2 paths,including type gates,health/gate,
attached-counter wrap,events0/5/7/9/10/13,post-child cleanup,signed actor index,
directed subtract/multiply,and unsigned conversion fallback/FCSR restoration.
State1/state3 non-target dispatch remains explicitly outside this caller scope.
All four normalized child programs are proven byte-identical and executed
once per case; raw C is a separate stream. Two wrong-child variants complete
the parent then fail comparison. Original transform internals are contracted.
Assembly record+8 has a complete12-byte storage contract; its unknown original
C effective aggregate type is not asserted.

Original270-word composite and 56-word tail helpers each run 128captured cases.
All 256 nontrap composite words execute;14 divisor traps are unreachable;
1,840nested child submissions are checked,including24-byte headers/60-byte
payloads and the tail's full six-byte header/12coordinates. The original
matched115-word particle child runs 64nested captured cases,all words visited,
with both separately rounded FP operations checked. Its original61-word factory
and 11-word copy run 64 cases/32successful112-byte copies;all 41factory words
reachable for actual kind 1/null-extra inputs and all 11copy words execute.
All 14 seeded particle holes are copied;allocation canaries/9C zero remain
checked. RNG/vector/allocation internals are contracted; no fresh composite,
tail,or factory FCSR/hardware/runtime claim or helper matching credit is made.

| Tools execution | Seconds | Qualification |
| --- | --- | --- |
| preinstall-primary | 166.975 s | 5 fresh / 0 reused |
| preinstall-sibling | 164.779 s | 5 fresh / 0 reused |
| installed-primary | 160.72 s | 5 fresh / 0 reused |
| installed-sibling | 173.117 s | 5 fresh / 0 reused |

Task/import/data/profile/artifact fingerprints agree across both tool copies.
The second copy uses 2103 immutable dependency
links and 11 new task copies. Freeze:
3734 inputs/2650 copies. Shared tools-check
passes. The independently dirty tools sibling is preserved. One packet-only
ClaudePro advisory used zero tools/MCP/tool calls; findings are independently
reconciled in `claude-reconciliation.json`,never treated as matching credit.

Fixture corrections before acceptance: the reused helper Capture class still
inherited its old guest fixture,so it was replaced with the actual N45capture;
nested phases are adapted after the existing oracle's0/8entry constructor,
with real stack/home/register state reset explicitly. These were fixture
failures,not source defects or effective negative controls. The first paired
setup also caught a stale prior-task filename glob and refused the manifest
fingerprint; its incomplete run is uncredited and preserved separately. All
3,734 original input hashes remained fixed; the corrected twin setup passes.

Baseline consumerf464486642d1e27af072b7fd19fc58514af30683.
Tools commit`52a64b57339ce7a477eac9c7130d30756f4b61d0`.
Production ELF SHA256`fcd951b5f84bb6a43e380668123801d103e617a9eda80b8eaa58ef50ce1f3417`.
Padded target owner SHA256`f44497e4531840b09da62c1f76252693f892868b95e062a5b059f6cfd01b58c0`.
Unchanged producer object SHA256`1fe0e79ac5aaf3794c75593ff3af85e5abb24750ee2019db0e42f439ef1ca3e5`.
Receipts:`conker/build/game-sibling-preset-150b5c38-private`.

Root README gets aggregate/date rows only. Graph refresh retains every old ID
and qualification field,then adds current definitions for both changed owners;
actual hook termination and scoped graph publication precede the sealed bank.
No full-corpus reextraction,host build/launch,Release change,or push. Continue
the active85% goal from the next small unmatched Game routine after banking.
