# Local vector transform match - 2026-11-25

`func_15117DA4` replaces its zero-return placeholder with a typed two-angle
vector transform in `conker/src/game/generated_142560.c`.
VA `0x15117DA4..0x15117F3C`, ROM `0x145254..0x1453EC`: **102 words /
408 bytes, 48-byte frame, no alignment tail**. **87 words and their bindings
emit directly; 15 expected-word guards normalize tail FPR allocation and
independent output-access scheduling. Raw C is not byte-exact.** Ordered FP
operations and operands remain intact. There is no floating commutation,
private-frame map, insertion, omission or compiler-profile change.

Production recount: **4,682 / 5,528 (84.70%)** total; **4,009 / 4,855
(82.57%)** Game; Init492/492, Debugger181/181; zero address drift,
846 still different. **17 more verified matches reach85%.** One new match;
zero parent or provider credit. Conversion rows and denominators are fixed.

The current C interface takes a record pointer, three `f32` values carried
in A1/A2/A3, and an output pointer at incoming SP+16. The inferred return type
is void: all three observed callers discard the return. This is not proof
of original source intent. Guest checks separately retain the actual machine
V0 output pointer and F0 final cosine result.

The 88-byte typed record view pins angle fields at0/4, signed16 position
components at0x10/0x12/0x14, type at0x54, and all retained ranges. It is a
prefix view, not a claim that the parent uses an88-byte complete object or
that its unknown original C effective type was recovered. Native tests use
legal typed records and a separate12-byte output array. Assembly caller
tests provide the larger backing record needed by the parent. Arbitrary
guest byte aliases are not claimed as portable C aliases.

If type0x8006 and categoryD800BE9F0==0x35 both hold, the target looks up
selector0xFD, invokes the existing attachment updater, and substitutes local
X/Z=0 and Y=D800A2FF4. The lookup must provide a valid record on this path;
no new null-result contract is invented. The first angle is record0 times
D800A2FF8. With its sine/cosine, the target writes X, Y*cos-Z*sin, and
Y*sin+Z*cos. It then uses record4 timesD800A2FFC, reloads output X/Z after
the second trig pair, and writes Z*sin+X*cos and Z*cos+(-X)*sin. Finally it
adds the three signed-halfword positions in retail's operation/access order.
Provider mutations of records, outputs, constants and FP state are retained.

An ordinary source initially emitted100words and omitted two retail output
loads. Explicit observed X/Z reloads recovered102words but exposed reordered
FP operands. A strict ordered-operator model rejected those forms. Capturing
the computed X and old Z before publication, reversing the source expression
needed for the first translation, and naming the final `translationZ`
conversion recover the retail operand order. No dummy work, barriers or size
tricks were added. The scoped volatile loads preserve observed rereads;
original source volatile intent is unknown. All83 other raw/padded functions,
all literal/data pools and the normalO2/g3 profile are unchanged.

The complete target and652-word original parent `func_15117F3C` match ROM.
The aligned JAL-pattern census finds exactly three assembly calls at
151181FC /1511869C /151187B0 (ROM1456AC /145B4C /145C60); no aligned literal
target pointer was found. This is not a universal indirect-call census.

Fresh connected caller qualification is explicitly bounded: **768 cases per
stream,448 child invocations per stream**, all three actual call windows,
their genuine four-word parent prologue, and a separately exercised five-word
epilogue. **127 distinct parent instructions actually execute.** The output
is the12-byte array at parentSP+0x54 in a168-byte parent frame. All five child
arguments, the first window's scale/branch producers, null actor and missing
payload gates, and the latter two windows' original truncation/SH coordinate
consumers are checked. The second window requires the nonnull payload
established by preceding parent code; the third window tests its own payload
gate. Full bounded parent memory, provider frames, saved/return registers and
child outputs agree. Two wrong caller variants complete their bounded window
and separate epilogue, then fail comparison. Dispatch and intervening parent
cases are preconditions, not652-word runtime coverage; the parent C stays an
unmatched placeholder with zero credit.

The scalar guest reference passes **372 cases per stream**, covering gate
outcomes, ten alias locations, provider record/output/constant/FP mutations,
guest-only incoming-home mutations, signed16 boundaries and four rounding
modes in the bounded finite FP model. All102 target words execute. Four
retail-identical versions plus raw compare public/private memory, all GPRs,
machine returns, ordered FP operands and full physical provider snapshots.
**160 access-fault quads** compare exact registers,
memory, PC/delay, trace and modeled FP state across the four literal retail
versions. Raw scratch FPR and fault-prefix equality are not claimed. This is
not a hardware IEEE-FPU or trig-implementation proof.

The structural proof covers **147 cases /49 alias locations**, with the three
gate outcomes and arbitrary angle/translation/retained bits and provider
public-byte epochs. The common first74 words/bindings are literal matches.
FP operators, operand order and FCSR transitions are uninterpreted ordered
operations; no arithmetic identity or NaN commutation is assumed. Complete
provider GPR/FPR state and48-byte frame, ordered public writes, all public
bytes, private frame, all return GPRs, saved FPRs and F0 agree. Four supported
complete controls reject, including a swapped-operand add. It is not an IEEE
emulator, SMT solver or general binary proof. Trig, lookup and updater
internals remain contracted and unchanged; no extra provider credit is taken.

Native32 compiles the actual selected C and independent scalar/provider
harness in two translation units atO0/O2/O3: **372 target calls per profile**,
all seven record-field offset/width pins,88-byte records,12-byte output and
252-byte arena/canaries. Full provider arguments, arena/global snapshots and
MXCSR agree. Four rounding modes, provider sticky flags, record/output/global
mutations, and quietNaN/infinity angle arguments are checked. Trig results
are controlled provider returns; real trig internals and MIPS hardware are
outside this native gate. Strict aliasing, UBSan traps, LTO/type errors,
rounding/trapping/signaling-NaN flags and disabled contraction are enabled.
Seven wrong C variants finish and return comparison42; all normal profiles
return0. No signal or trap counts as an effective control.

Both full-owner padders preserve all42 exported retail jump labels. The
generic path reuses the qualified metadata-only label restoration wrapper;
before-object identity and complete after-object identity close its scope.
The actual five-command Make route includes GLOBAL_ASM pre/postprocessing,
IDO, padding and assembly with zero diagnostics. The independent reference
uses frozen old C and original408-byte targetASM, without new C or guards.
Reference, Make link, literal prediction and production ELF are identical:
**366 changed bytes, zero exclusions**. All189,088
protected Game data bytes across720owners, all unrelated code/addresses,
old guard prefix and conversion rows are fixed. Named symbol/string ordering
uses closed byte accounting; no blanket metadata exclusion is permitted.

Boundary checks reject30 guarded corruptions, expose174 unguarded
corruptions, pin14 relocation sites, and reject both oversized probes.
20GNU links and60 rebased guest runs cover four entry/address/carry patterns.

| Tools execution | Seconds | Qualification |
| --- | --- | --- |
| preinstall-primary | 84.627 s | 5 fresh / 0 reused |
| preinstall-sibling | 84.027 s | 5 fresh / 0 reused |
| installed-primary | 80.774 s | 5 fresh / 0 reused |
| installed-sibling | 89.789 s | 5 fresh / 0 reused |

All task/import/data/profile/artifact fingerprints agree across primary and
an isolated second tools copy: 2135 immutable
dependency links and10 new task copies. Freeze: 3772 inputs
/2690 copies. The second Make route invokes its own tools.
Shared tools-check passes; the independently dirty real tools sibling remains
preserved. This routine used zero Claude calls and no subagents.

Fixture corrections before acceptance: the sign-control needed a nonzero Z
path; provider mutations needed the actual caller output buffer; the second
window needed its valid nonnull payload precondition; C corpus initializers
needed explicit array braces. The old visit set counted stop boundaries, so
final receipts instead count successfully fetched/executed instructions and
include the separately run epilogue. Old receipts are retained before resealing
and the final fresh twin runs. None of these is a production-source defect or
an effective negative-control result by itself.

Baseline consumer `8e6d394908ef2ad50656e1d1f66971191cb7f5b5`.
Tools commit `bc6fe1b82cb3974b0a23b806682bbbbe2374a868`.
Production ELF SHA256 `36a841964477b4d35bcf443f9bc95c83d471c3fe8eaa2e6aeb04353172321393`.
Padded owner SHA256 `03a9b721584c8aa412e678f91c7eb10ee6796cc744a4f8c95e362af2480b827d`.
Receipts: `conker/build/game-local-vector-transform-15117da4-private`.

Root README gets aggregate/date rows only. Scoped graph work retains all old
IDs/qualification metadata after actual hook writers finish; it is not full
corpus reextraction. No host transfer, build, launch, Release change, gameplay
acceptance or push is claimed. Continue the active85% goal after banking.
