# Owner-position effect preset match - 2026-11-25

`func_150F802C` replaces its zero-return placeholder with a typed descriptor
builder in `conker/src/game/generated_124920.c`. VA150F802C..150F81BC,
ROM1254DC..12566C: **100 body/slot words, 400 bytes, frame 200**, no alignment
tail. **51 words/bindings emit directly; 49 expected-word and relocation
guards normalize independent instruction scheduling. Raw C is not byte-exact.**
The bound instruction-word multiset is identical to retail. There is no GPR
coloring,private-frame mapping,insertion,omission,dummy storage,or profile change.
All16 other raw/padded owner functions and the absent literal/data pools stay
fixed. The complete200-byte frame agrees at every provider and return.

Production recount: **4,680 / 5,528 (84.66%)** total; **4,007 / 4,855
(82.53%)** Game; Init492/492,Debugger181/181;zero drift,848different.
**19 more verified matches reach85%.** One new match;zero additional
caller/helper credit. Conversion rows and denominators remain fixed.

The recovered input format is 68 bytes: position[3], direction[3], and 44 retained
bytes. Only the first 24 bytes are read. The 124-byte main descriptor initializes
116 bytes; holes at hex offsets 59..5B, 69, 6B, 71, and 76..77 remain unspecified.
It captures the direction and position, unit scales, zero velocity, reference
vector, flags 0x980, a signed 16-bit parameter, resource ID 47, and the remaining
measured byte/halfword/word fields. Coefficient `D_800A1BDC` is pinned to actual
bits 0x3CA3D70B; the 12-byte vector `D_800A5480` is pinned to three zeros across
ROM and frozen ELF.

The actual factory call is `(descriptor,3,255,NULL,180,slot,context)`.
Before the call, the target captures a 20-byte owner/position/zero tail. On
success it copies that tail to `result + 0x170` with the SDK 20-byte memcpy; null
skips the copy. The factory allocation is 548 bytes. No floating arithmetic
occurs in the target: coordinates and constants are bit copies. Locals use
genuine aggregate extents and compatible prototypes,including the existing
ExtendedState15F680 pointer ABI and SDKlibc/string.h declaration.

The inferred C return type is void: the only literal caller discards the result.
This is an evidence-supported interface,not proof of original source intent.
Emitted MIPSV0 still preserves the factory null or memcpy destination,checked
separately by guest tests. Pointer-forwarding and early-return source forms
produced103/104words;ternary105/frame208. Unnecessary named constants and
register hints were rejected. Coefficient-store ordering recovered100/frame200
and reduced84scheduling differences to49 without changing the normalO2/g3 profile.

The full3,451-word original parent `func_150265CC` matches pristine ROM.
The aligned target-call census and literal26-entry jump table identify one
childJAL150277F4,tableindex9/subcommand10,case150277C4. The table is pinned
to ROM and frozen ELF. The parent frame is750hex/1872bytes. Its production
C placeholder remains unmatched and receives zero credit.

Fresh connected execution is explicitly bounded: **532cases per distinct
child stream,512children,35parent words**,starting15027550 after the decoder
returns and continuing through the shared29BB4return. It executes the decoder
return minus timestamp calculation,wordstore660/signedlowhalf662,actual
table dispatch,independent bank/record indices,68-byte stride,slotLBU773,
context1,and the branch-delay overwrite of childV0 with1. Invalid subcommands
0/27/127/128/255 and savedRA/S0/SP/calleeFP restoration are covered. The
type5/opcode65/state0 prefix,decoder internals,valid backing allocations and
unrelated dispatcher cases remain preconditions,not complete-parent runtime
claims. The assembly record's original C effective aggregate type is unknown.
Four wrong caller variants complete this bounded path then fail comparison.

The original 256-word `func_1513264C` is executed on this captured packet in
**378cases/172successes**. All216words reachable for flags980/kind25/pool1,
resource47/null-state are visited. The40other words belong to duplicate-load,
alternate-kind/pool,retained-resource and nonnull-state paths that this call
cannot select. All11 original memcpy words execute. Count gating,allocation,
node-allocation/resource-load failures,head/nonhead linking,search indices
0/1/98/99/100,reference wraps,view count-1/0/3 and provider mutations are
checked against independent state/list/counter/canary expectations. Default
state coefficient800A3868 is pinned to C61C4000. Allocator,loader,free and
view-provider internals remain contracted;only sqrt of fixedzero is used.
No helperFCSR or arbitrary-helper-path claim is made. Current factory C
remains256words/184differences,unmatched and uncredited. Three wrong helper
variants complete and fail comparison:descriptor-copy width,allocation size,
new-node resourceId offset.

Both target padders agree. The actual five-command Make route includes
GLOBAL_ASM preprocessing/postprocessing,IDO,padding and assembly,with zero
diagnostics. The independent frozen-old-C/original400-byte-ASM reference,
whole-owner Make link,prediction and production ELF are literally identical:
**302 changed bytes,zero exclusions**. All189,088
protected Game data bytes across720owners,old guard prefix,conversion rows,
unrelated objects,addresses and frozen inputs are fixed.

Boundary tests reject98guarded corruptions;102unguarded corruptions remain
visible. Six relocation pins reject;both oversized probes reject.20GNUlinks
and40rebased guest runs cover four address/carry patterns. Bounded symbolic
proof covers100words,complete frame/descriptor/tail at providers and return,
both result paths,arbitrary public bits/provider epochs,all return registers
andFCSR,eight path proofs/four rebases,and five effective complete controls.
It is not a general SMT or hardware proof. Raw private-write/fault order is
not claimed equal.

Fresh guest checks execute **496cases/five streams**:four retail-identical
and raw. They compare full frames,144passed descriptor/tail bytes,public RAM,
all return registers/FCSR,all256slot bytes,signed16/context32 boundaries,
coordinate bit-copy extremes,null/success paths and provider mutations.
**213access-fault quads** compare exact state/PC/delay/trace among four
retail-identical streams. Three complete guest controls are effective.

Native checks compile the actual target and provider/copy harness in separate
translation units under32-bitO0/O2/O3. **2,048calls per profile** cover all
256slot bytes,parameter/context boundaries,both outcomes,eight mutation
classes,68-byte source,548-byte allocation/canaries and active tail lifetime.
All33 descriptor fields have independent size/offset pins;tail/input extents
are pinned. Eight unspecified descriptor bytes are excluded from native
reads. The actual frozen SDKmemcpy C body executes. Four rounding modes
and provider sticky flags survive. Strict aliasing,UBSan traps,LTO and
type-mismatch errors are enabled.12wrong source variants complete and return
comparison42;all normal profiles return0. Signals/traps are not accepted
as effective comparisons;native tests do not claim source-language semantics
for guest-only incoming-home overwrites or unknown original aggregate types.

| Tools execution | Seconds | Qualification |
| --- | --- | --- |
| preinstall-primary | 108.531 s | 5 fresh / 0 reused |
| preinstall-sibling | 108.881 s | 5 fresh / 0 reused |
| installed-primary | 109.552 s | 5 fresh / 0 reused |
| installed-sibling | 109.787 s | 5 fresh / 0 reused |

All task/import/data/profile/artifact fingerprints agree across primary and
the isolated second tools copy. The second copy uses
2114 immutable dependency links and11new
task copies. Freeze:3746inputs/2663copies.
Shared tools-check passes. The independently dirty real tools sibling is
preserved. The second-copy Make route invokes its own tools,not primary.

One packet-only ClaudePro review completed in166.89seconds,
with empty tools/MCP and zero tool uses. All seven findings were reconciled
independently. Two advisory details were corrected:the parent savesS0/RA
atD0/D4 rather than homingA0 at750,and childLH662 reads the signed low half
of decoder-return minus timestamp. Tableindex9 was independently pinned,
not accepted from inference. `claude-reconciliation.json` records each finding.
The review itself earns no matching credit. Fixture corrections before
acceptance included original factory default bits,list consistency,child
return delay-slot tracking,and control opcode selection scoped to the actual
case. Earlier failures are not production defects or negative-control passes.

Baseline consumer`60d19a750a1fb0ef8776a36606fa879a192cb51e`.
Tools commit`c3a59e0d73ab6624763b0b6d77be61ac2e055f7b`.
Production ELF SHA256`fd016712a08e9c8b2638ad8d8fbf2650197cda24d56fc1bdb49756bde5857227`.
Padded owner SHA256`b0a12040e9cc35c4b252393245c4810e6b822b7e70a6c4e28b7d3f1b7b05b87d`.
Receipts:`conker/build/game-owner-position-preset-150f802c-private`.

Root README gets aggregate/date rows only. The graph refresh retains old IDs
and qualification metadata,then refreshes the changed owner and10Python
task files after actual commit-hook writers terminate. Scoped AST extraction
is not a full-corpus reextraction. The host sibling currently has no source
checkout at its expected path;no host transfer,build,launch,Release change,
or gameplay acceptance is claimed. No push. Continue the active85% goal
from a newly frozen small unmatched Game target after banking this result.
