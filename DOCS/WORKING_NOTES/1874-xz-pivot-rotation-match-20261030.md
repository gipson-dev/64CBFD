# Note 1874: X/Z pivot rotation match

2026-10-30. `func_1508EF80`, legacy owner `game_BC430`, replaces its
zero-return placeholder with `void func_1508EF80(f32 *point, f32 *pivot,
f32 degrees, f32 *output)`. VA `0x1508EF80..0x1508F05C`, ROM
`0xBC430..0xBC50C`: 55 reachable words / 220 bytes, followed by one slot
alignment word through `0xBC510`. Existing O2/g3 profile and shared headers
remain unchanged. Tools commit: `593d879ca1ee11533ab66ae90c830fcd4334b6a0`.

## Recovered behavior and ABI

The routine captures `dx = point.x - pivot.x` and `dz = point.z - pivot.z`,
then rotates that offset around the pivot using `degrees * D_8009DC80`.
The data constant is confirmed as `0x3C8EFA35`, approximately pi/180.
The four original calls are cosine, sine, sine and cosine. Both X/Z results
are computed before either output store, and output Y is untouched.

Pivot X is reloaded after the second call and pivot Z after the fourth.
The source preserves these reloads, the repeated trig calls and delayed
stores when point, pivot and output alias or a bounded provider mutates
their data. Negation applies to the second sine result before multiplying
by dx. Splitting each final pivot addition from its product sum recovers
the original operand order; no floating commutation or reassociation is
used to justify the match.

The 64-byte frame, RA at SP+28, saved f20 pair at SP+16, pivot home at
SP+68 and output home at SP+76 emit directly from C. Captured dx/dz are at
SP+60/+56, computed X at SP+40 and the shared trig spill at SP+36. The
third float argument arrives in A2 under this mixed o32 signature; the
first instruction sequence transfers it to f14. The initial six-local
candidate used frame56. Explicit provider values and the recovered local
lifetimes restore frame64 and all original homes without a frame guard.

## Eight closed opening guards

Raw C word SHA-256:
`20b4d2dfe724eca987d3fd7a14a1543e19335211d4bfda26ee159e1036522053`.
Normalized original object-word SHA-256:
`5926c24d93ff52d68ec35f87f1c9fc90fefe25a3f1ac43500973e27aa3b2e8d7`.
There are six relocations: the constant's HI/LO pair and four trig calls.
The LO relocation moves from offset `0x20` to `0x24` with its instruction.

The only guards are offsets `0x20`, `0x24`, `0x28`, `0x2C`, `0x30`,
`0x34`, `0x3C` and `0x48`. All lie in the opening `[0,76)` through the
first call's delay-slot store. Independent symbolic execution proves the
same ordered memory trace, ordered floating-expression sequence and all
GPR expressions. Only caller-saved f4/f10/f16/f18 differ at the boundary;
each is overwritten before its next caller read at offsets 96/104/116/120
as appropriate. This proof does not assume the helper clobbers them.
Eight supported semantic mutations break that proof. No insertion or
omission, and all inherited guard bytes remain an unchanged prefix.

This is guarded byte-exact C; it is not a direct raw compiler match.

## Qualification and limits

Ignored evidence: `conker/build/game-xz-pivot-rotation-1508EF80-match/`.
`semantic_v26.py` records one coherent oracle revision. All eight private
checks and all eight canonical checks per tools copy pass.

- Guest: 8,192 cases / 24,576 executions, all 55 reachable words. Original,
  raw C and normalized C agree in complete final modeled state and access
  trace. Eight array alias layouts, provider mutation modes, signed zero,
  subnormals, finite limits, infinity and NaN patterns are covered. Two
  additional constant/input/output alias cases are guest-only.
- Access prefixes: 90 cuts, including six delay-slot cuts. Original and
  normalized bodies agree in complete cut state. Raw scheduling agrees in
  memory/call effects; transient raw FP register equality is not claimed.
  These are instruction-model checks, not portable C fault semantics.
- GNU relocation: 108 additional cases across three layouts, including
  signed-low and high-half carry boundaries. State and access order agree.
- Providers: 320 cases connect the actual original cosine (85 words) and
  sine (104 words) bodies, which are also retained in the current ELF. The
  suite visits 175 provider words and checks the actual polynomial results.
  No additional helper credit, full-provider path coverage, IEEE exception
  flag model or hardware acceptance is claimed.
- Callers: the complete aligned-ROM census finds eight JALs and no literal
  function pointers. Four calls live in legacy `func_151256BC`, missed by
  a top-level-assembly-only search. Two paired windows of 19/13 words check
  successive in-place rotations, point/pivot exchange and saved arguments.
  Other windows are 3/25/7/3 words in `func_1512AD54`, `func_1512C20C` and
  `func_1512D390`, including the absolute-angle gate and signed clamp.
  All six windows pass 864 cases per body. Current C parents remain stubs;
  no complete-parent or gameplay acceptance is claimed.
- Native32: 8,192 cases per O0/O2/O3 profile with trapping UBSan, no warning
  suppressions, SDK float/pointer width assertions and typed trig callbacks.
  Pre-provider observations, final data, canaries and all 14 effective
  defect controls pass. Native NaN payloads are canonicalized for portable
  comparison; guest modeled cases preserve the original operation ordering.
  Fourteen separately IDO-compiled controls also fail the independent
  public-memory/call/observation reference.
- Actual padder: eight bad word preimages, two bad relocation preimages and
  a foreign-function row reject. The complete raw body gate rejects220
  byte corruptions plus size/binding/scope negatives, 225 in total.
- Owner/Make: this owner has one function and no neighbors. Pools stay
  fixed; all three actual Make commands reproduce the complete legacy
  padded object. Selected, owner and executed-command diagnostics are empty.

Early fixture corrections are retained in failed receipts: `.size` was
needed for the isolated original assembly; caller boundaries needed an
owned sentinel; `abs.s` needed its exact sign-clear operation; the second
157840 caller belongs to `func_1512C20C`; native reference formatting and
an explicitly initialized result removed warning errors without suppressions.
A receipt comparison needed JSON normalization of integer dictionary keys.
None of these changes modified production behavior to satisfy a fixture.

## Image, progress and banking

The strict independent prediction reproduces the production ELF literally:
194 changed bytes = 175 target-code bytes  + one target-extent byte + 18 metadata
bytes. The metadata delta is one explicitly checked three-symbol/string
permutation, `D_8009DC80` / `D_80098850` / `D_8009D3D0`, order 1/2/0. All
named definitions remain equal except the target's 12-to-220-byte extent.
No byte or section exclusions. All 6,055 other function bodies, all 6,056
function addresses and all 189,088 protected Game-data bytes / 720 owners
remain fixed. The conversion inventory CSV and map remain byte-identical.

Adopted ELF SHA-256:
`72d17139b031fde8cc28703303696819946ee00a09fa0ed38e021ea44e44f0f3`.
The actual Native ELF recount is **3,951/5,506 (71.76%)**, Game
**3,278/4,833 (67.83%)**, Init 492/492 and Debugger 181/181; zero drift.
The 75% threshold remains 4,130/5,506, requiring **179** more exact functions.

Production runs two fresh installed checks per copy and explicitly reuses
six unchanged semantic checks under exact module/input/artifact fingerprints.
Tools are committed before the scoped source/guards/docs/pin consumer commit.
The older tools mirror preserves all 2,060 inherited dirty paths and adds
only three qualification modules, without a mirror commit or push.
The root README changes only its two aggregate matching rows.

Graphify structurally refreshes eleven changed supported files and binds
the guard CSV by exact rows/hash. Every old node and still-valid relationship
is preserved or relocated; one obsolete s32 return relationship is retired
against the actual declarations. Caller/provider annotations retain the
scope limits above. No full-corpus re-extraction or new clustering claim.

Next private screen: `func_150B36AC`. Parked candidates remain uncredited, and the
75% goal remains active. Zero Claude/REA calls, dependency installs,
account/browser, sibling host/editor or frozen Release changes.
