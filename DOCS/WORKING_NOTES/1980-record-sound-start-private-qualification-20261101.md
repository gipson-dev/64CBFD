# 1980 - Record sound-start privately qualified; epilogue still unmatched

`func_150A23E4` has a fully reconstructed and privately qualified semantic C
candidate, **54 words/frame64**, against retail's **55 words/frame64**. Nine
overlapping words differ, plus the missing word; the differences are the first
branch displacement and closing epilogue layout. **No function is installed or
credited.** Production remains **4,046/5,507 (73.47%)**, Game **3,373/4,834
(69.78%)**, zero drift and 1,461 different. **85 more** are needed for 75%.

## Record, call and state contract

The target is in `conker/src/game/generated_CDE80.c`, original
`conker/asm/CDE80.s`, entry `0x150A23E4`, ROM `0xCF894..0xCF970`.
The existing 0x34-byte `GeneratedCDE80Record` covers its fields without a new
shared declaration: signed origins at 0/2/4, flags at 0x15, selector at 0x17,
word flags at 0x18, packed sound/parameter at 0x1C and full-word state at 0x20.

When state is zero, the candidate submits `func_1000FA64` with the packed high
halfword, signed coordinates, `327 * (selector & 127)`, word flags OR 0x8000
when the low two flag bits are zero, the packed low halfword, three zeros,
mode 8 or 0x108 according to selector bit 7, and a final zero. It publishes
state 1 **after** the helper. An initially nonzero state also becomes 1,
without calling the helper. The return value from audio submission is ignored.

The private candidate uses `void (GeneratedCDE80Record *)`. Both identified
original caller windows ignore its result; the production placeholder remains
the old `s32 func_150A23E4()` because this candidate is uninstalled. The
existing typed twelve-argument enqueue declaration is retained, including
callee halfword narrowing. IDO leaves the incoming upper argument bits to the
callee; the source explicitly masks the packed low-halfword argument to
reproduce the retail call preparation. No unprototyped helper, false ABI,
register binding or volatile qualifier is adopted.

## Fresh semantic qualification

The guest corpus has 2,580 cases across selector/flag bytes, full-word state
values, signed coordinate and packed-word boundaries, helper mutations and
two stack phases. Three code/helper layouts give **7,740 cases / 15,480
original-candidate executions**, covering all 54 reachable retail words and
53 reachable candidate words. Each body has one unreachable duplicate store.
GPRs, FPRs, public memory, calls and complete access traces agree. Forty-eight
fired access-prefix pairs also agree; differing PCs and delay-slot identities
are not claimed equal. Helper writes to the record and incoming homes test
captured arguments, preserved record pointers and post-call state publication.

The current retained enqueue helper equals all **109 retail words**. Connecting
it gives **756 cases / 1,512 executions**, covering 88 helper words reachable
under this target's mode and argument restrictions. Tests cover queue counts
0/31/32/33, full-queue returns, sorting-induced count changes and nonzero audio
handles. `alCents2Ratio` and `func_10011624` remain bounded mocks; the target's
mode cannot enter the helper's alternate coordinate-provider branch.

Both original callers are exercised from ROM: a six-word window at
`0x150A0AE4` and a four-word window at `0x150A1A48`, 120 executions each.
They form the record address, call the root, ignore its result, and reach their
real following branch destinations. The first window observes the live
post-call global count reload. These parent functions remain unrecovered
production stubs; whole-parent execution is not claimed. Fresh public fixtures
use a complete 0x34-byte record offset.

Native 32-bit typed calls pass all 2,580 cases at **O0, O2 and O3** with
undefined-behavior traps, record/surrounding fences, all twelve helper arguments,
helper mutation preservation and pre-publication state observations. Seven
effective controls per profile reject a byte-only gate, omitted flag/mode,
wrong scale, lost low halfword, early state publication and wrong final state.
Guest incoming-home mutation does not imply portable C stack-alias semantics.

## Generated owner, Make and complete private image

Both raw and padded objects preserve **27 neighbors** and pools, with zero
owner diagnostics before and after. The real generated-owner recipe consists
of five commands: preprocessing, IDO compilation, assembly postprocessing,
generated-slice padding and GNU assembly. It reproduces the independently
padded object byte-for-byte. The generated padder must retain the original
slice's jump labels; the plain-C padder has equivalent text here but different
symbol/relocation-index serialization and is not the appropriate object proof.

The independent private image prediction derives the 216-byte body from the
qualified padded object, resolves its single `R_MIPS_26` enqueue binding, adds
the existing final alignment word and changes this symbol's extent from
12 to 216 bytes. It predicts the **entire ELF literally**, with zero exclusions
or metadata permutations. All 6,052 function addresses, all 6,051 other
function bodies and every named definition remain fixed. Protected data
matches all 189,088 bytes across 720 owners. The normalized map is unchanged.
Private image SHA-256:
`f88a211d92648be3f637ca1561ff121be38984dc9808f2ad1461d72895227abc`.

Both tools copies pass five focused methods and shared tool checks. The
production ELF, source, objects, guards, profiles, conversion rows and README
aggregates remain unchanged. This is private semantic/build qualification,
**not** an exact match or installation.

## Measured code-generation gap

The best raw payload hash is
`c543a36df03e35fa34f5f8fe30d2cae9649ad718370a723e6b24494cb141801d`.
The complete call preparation from +0x20 through +0xB4 and its binding match
retail. The candidate sinks the state store into an unconditional branch's
delay slot, then shares one return-address restore. Retail stores state first,
fills that branch's delay slot from the return-address restore, jumps over it,
and retains a second restore for the other incoming path. The second static
restore is the extra retail word. Do not insert an instruction or repurpose
alignment padding to manufacture it.

Measured exclusions:

- If/else, explicit returns, goto and switch forms share the same 54-word body.
- Full owner versus isolated and void versus fallthrough-s32 contexts do not
  close the gap. Return type is not changed solely for matching.
- Direct IDO O2/g3 emits 54 words/10 differences including length; O2/default-g
  emits 65/64, O2/g0 emits 54/15 and O1/g3 emits 62/61.
- Assembler O0/O1/O2 controls emit the same 54-word body.
- Volatile store/field diagnostics also emit the same body. An entirely
  volatile pointer emits 55/41 and is unsupported as a recovered qualifier.
- A disposable `cc -S` capture crashes that new ugen child. It is not valid
  stage-output evidence. No compiler is modified or installed; normal
  compilation and actual Make continue to pass.

One packet-only Claude analysis was used for this persistent backend question,
with safe mode, no tools/MCP, one turn and no session persistence. The useful
hypothesis is the choice between filling the branch delay from its predecessor
or its target. Its assertion that tested O1 emitted 54 words is contradicted
by the measured 62-word result; its suggested inverted condition was already
tested. Its absolute claim that no source form can recover retail is not
established. The exact retail backend setting/patch level remains unknown.
No extra analysis call was made. Preserve this distinction in later work.

## Evidence and continuation

Stage: `conker/build/game-record-sound-start-150A23E4-match/`.
Key records: `private-guest-v14.json`, `private-native-v16.json`,
`private-owner-image-v22.json`, `Make-commands.json`, `prepared-artifacts.json`,
the compiler profile screens, `claude-review-v17.json` and final handoff.
The four qualification modules are committed tools first; production code is
unmodified and the candidate remains private/uncredited. The 75% goal stays
active. README status numbers need no change.

Next ordinary target: `func_150C5E0C`, a 60-word/frame40 embedded oscillator in
`generated_F3270.c`, original `asm/F3270.s`. It has the same instruction shape
as `func_151AB090` in `generated_1D6E80.c`: capture/clear a notification byte,
subtract the live tick count from a signed halfword countdown, call integer
and float RNG providers on expiry, then blend a signed output value and return
the captured notification. Qualify wrapping, zero-divisor fault prefixes,
provider mutations and captured/live fields before credit; start with one
owner. The smaller `func_150A613C` fallback is excluded from ordinary C screens:
its original uses T4 and F16..F31 as incoming state and updates S2 in the return
delay slot, an internal register convention requiring separate entry/ownership
analysis. Neither fallback receives new conversion or matching credit here.
