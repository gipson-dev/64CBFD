# Natural direction vector effect byte match - 2026-11-24

`func_150BD954` replaces its zero-return placeholder with semantic C in
`conker/src/game/generated_E8C10.c`. All **122 instruction words emit directly
from C, with zero guards**. Frame176 and every register, operation, binding and
call schedule agree. Body and retail slot are the same488 bytes: VA150BD954..
150BDB3C / ROMEAE04..EAFEC. There is no extra owner padding word. No instruction
insertion, omission, profile/Makefile/guard change, replacement body, dummy
local, enlarged record or alignment override is used.

Actual production is **4,672 / 5,528 (84.52%)** total, Game **3,999 / 4,855
(82.37%)**, Init **492 / 492**, Debugger **181 / 181**, zero drift and856 different.
**27 more matches are required for85%**. Only this callback gains one match.

The first complete semantic screen already had122 words and identical
bindings, but frame168 and26 stack-layout differences. Capture the first float
RNG return in a real `sample` variable, compute the used `speed` from it, and
declare the locals in order sample/request/payload/speed/render. That produces
the original176-byte frame and all122 words naturally. Both float temporaries
participate in the actual arithmetic. The records retain their real bounded
sizes28/32/32; no unused object is added to manipulate the frame.

The callback carries15 o32 words. Active inputs are x/y/z, the direction-vector
pointer in word13 and the final slot byte. X/y are captured from the incoming
GPRs into FPRs; z reloads before the first helper. Only the first two incoming
register homes are stored by this routine. Guest fixtures deliberately poison
the x/y homes, proving they are not the source of the captured coordinates.
The direction pointer and coefficient load occur after the first float RNG
call; the final slot byte reloads after the third. Original registry parents
forward an aligned direction object. This qualifies the actual o32 interface,
without claiming every generic C callback typedef is portable-compatible.

The initial velocity is the supplied three-component direction multiplied by
`(sample*127+85)*D_8009FFD0`. Each direction component is read immediately before
its output store. Three unsigned integer draws set payload byte1B to
`draw%86+180` narrowed to u8, request count to `(draw&3)+3`, and lifetime to
`draw%31+39`. The first result deliberately wraps through byte255 to0..9.
Two later float draws build payload fields00/10 from the remaining globals and
the356 factor. Coefficient bits at D_8009FFD0..D_8009FFE4 are 3A83126F/44168000/43CB8000/3C23D70A/447E4000/3A83126F.
The payload retains the captured y, flags8, kind9 and alpha255. Request mode
and active are one. Render words are0/1/0x160600/3/16/128/32, then bytes0/9.
The single15-word factory call is
`func_15147DA0(request,payload,0,1,11,0,0,0,0,0,0,render,0,slot,1)`;
its result is ignored and the callback returns one.

All eight owner neighbors retain raw/padded instructions and bindings. Both
complete owner padders agree. Raw .rodata/.data stay absent; padded .rodata
stays absent and .data empty. The actual Make route has three commands. The
independent reference uses frozen old C plus original target ASM, with the
following `func_150BDB3C` preserved in the middle-owner splice. Production
equals the full predicted ELF: **484 changed bytes, zero exclusions**.
All189,088 protected Game data bytes /720 owners, conversion rows, guard CSV
and other inputs stay fixed. Make emits the existing duplicate-recipe warnings
for generated_12D630, generated_F44D0 and generated_F5800; its hash is unchanged.
Broad unchanged neighbor suites are not repeated or claimed fresh.

Four retail-equivalent guest streams pass 485 cases each, plus an identical
raw-C stream. All122 words execute and 212 access-fault quads agree. Cases
cover all256 slot bytes, all86 first-draw remainders, all31 lifetime remainders,
count-mask and unsigned-word boundaries, four rounding modes, both factory
outcomes, global/vector mutations, late incoming-home mutations and overlapping
guest vector sources. All92 private-record bytes, including seeded holes,
agree at every call boundary. Guest aliases and home mutations qualify emitted
ABI behavior and are excluded from legal native cases.

SDK32 O0/O2/O3 each pass 453 legal bounded cases with strict aliasing,
controlled rounding and UBSan. Dual32 digests compare ordered calls, globals,
direction vectors and public canaries. The pointer-bearing factory observes
exactly79 initialized record bytes, excluding13 unspecified bytes across the
three records. Native RNG helpers have no record pointer and do not inspect
private records before the factory. All19 source mutations compile and fail
comparison with exit42; no compile failure, signal or UBSan trap counts as an
effective control. No source hole is initialized for the test.

The aligned pristine-ROM census finds zero direct J/JAL encodings and one
literal entry pointer at ROM22F4F4 / VA8008AA34, D_8008AA00[13]. All four complete
original registry parents pass 384 cases per stream plus identical raw C,
forwarding all15 words and 352 child calls per stream. Eight return-zero
controls stop a second child. Coverage remains95/96,113/130,112/120,128/138; two
parents remain unmatched live. Angle and RNG providers are contracted outside
the child body. Finite executions give no parent credit or all-path claim.

The original70-word `func_15147DA0` and11-word `memcpy` are independently bound
to pristine ROM and agree with the frozen live ELF. All81 original words execute
across 16 success/failure, phase, slot and request-mutation cases. The
constructor sets request.active before calling the11-argument allocator, copies
all32 descriptor bytes, writes six control bytes and copies all32 render bytes.
The six unspecified descriptor/render bytes are copied in these seeded guest
executions; native tests exclude them. Destination holes and surrounding bytes
retain their seeded values. Only allocator internals are contracted. The24
coefficient bytes agree with frozen ELF and pristine ROM. Helper credit is zero.

Boundary controls expose 244 unguarded corruptions and pin all
19 bindings. Sixteen GNU links /32 guest rebases cover HI/LO carries and
sign/address regions. Oversized generic output is visibly labeled overflow;
the generated padder rejects it. Shared `make tools-check` passes.

| Qualification | Elapsed | Coverage |
| --- | ---: | --- |
| preinstall-primary | 121.379s | 5 fresh / 0 reused |
| preinstall-sibling | 120.496s | 5 fresh / 0 reused |
| installed-primary | 106.745s | 5 fresh / 0 reused |
| installed-sibling | 110.579s | 5 fresh / 0 reused |

The second tools overlay verifies code/data fingerprints and leaves the
separately dirty sibling unchanged. Tools commit before consumer. Claude calls:
zero; local compiler and execution evidence settle this routine. Root README
changes only two aggregate rows; this note and five concise indexes hold detail.

Consumer baseline: `52505867758858e5c90ee977e09b35804b04aadb`.
Tools commit: `c1828777229d1c0df19fd884c4a5c0ffeb13697e`.
ELF SHA256: `26fdf56506c88cb9f82b0d248fd93abe117ce07f781e368a27c91dc86c7f8979`.
Padded owner SHA256: `b908e169e1b8d8e246a80cbed4e0c7c6c60c4af97d5e79f371719f55126a738e`.
Freeze: 3651 inputs / 2254 copies. Receipts:
`conker/build/game-radial-fragment-150bd954-private`.

Graphify query preceded work. Native update and scoped AST merge retain old
IDs and proof metadata after the actual hook producers terminate. Graph staging
and validation/publication use separate processes to limit memory and temporary
disk demand. Completed private outputs may be NTFS-compressed with every SHA
verified unchanged; frozen baselines and active test files are excluded. No
deletions, full-corpus extraction, host/Release action, push, gameplay acceptance
or all-input equivalence is claimed. Next inspect `func_150C16C0` against its
fresh retail window. The85% goal remains active.
