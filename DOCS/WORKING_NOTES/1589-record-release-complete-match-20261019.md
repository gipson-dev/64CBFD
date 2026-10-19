# Record Query/Release Complete Match

Verified:2026-10-19. **Installed complete C recovery: all78 words /312 bytes
match retail, including frame0, all reloads and float32 conversion order.**

Finish `func_1508DAEC`, generated_B3020, VA `1508DAEC..1508DC24`, ROM
`BAF9C..BB0D4`, after
[Note1588](1588-parallel-array-reset-complete-match-20261019.md).
Consumer predecessor **4f69bcd0**, tools predecessor **958811a**. Bank tools
**f873d04** before the consumer source/guards/docs/pin. No push.

## Complete Source And Interface

Use signed32 slot and mode inputs, not the old unprototyped zero-return stub.
If D_800D23B0 is null or its EB0[slot] record is negative, return0. A negative
mode with a valid record returns1 without clearing anything. Otherwise clear
the initial context's EB0[slot] to -1 **before** rereading context and checking
record flags+11F4 mask0x2. A set flag returns0 but retains that early clear.

Clear current F70[record] and10F0[record] to -1 with global-context reloads
between stores. Capture current EAC unconditionally, including mode1, before
the branch's optional coordinate path. Mode1 stores300 at12F4[record], caches
actor D_800CC2D0+slot*32C, and writes signed truncated coordinates:

```text
1374[record] = trunc(actor.X at14)
13F4[record] = trunc(float32(actor.Y at18 +50.0f))
1474[record] = trunc(actor.Z at1C)
```

Retain fresh global-context reads around every output, including after Z.
Mode1 then writes4 to current1070[record]; other nonnegative modes write the
captured EAC. All release paths return0. Keep confirmed offset-based names
and the concise query/release comment; do not invent original source names
or a speculative enclosing record/actor type.

Six distinct direct JAL sites exist, confirmed by aligned ROM word0D4236BB
scan as well as assembly. Duplicate nonmatching assembly is not a new site:

```text
VA1508AB28 ROMB7FD8  B3020.s   delay AD400FF0: store zero at T2+FF0
VA1508E520 ROMBB9D0  B3020.s   delay 00002825: mode=0
VA1509E11C ROMCB5CC  CB3D0.s   delay 8E05000C: load full-word mode
VA150ED904 ROM11ADB4 11A680.s  delay 93A4016A: load unsigned-byte slot
VA150ED92C ROM11ADDC 11A680.s  delay 00002825: mode=0
VA150EDA58 ROM11AF08 11A680.s  delay 8FA40060: load full-word slot
```

Upstream mode0 in the11A680 cases and explicit frame/register live-ins are
supplied, not silently executed or inferred from test input. These are
two-actual-word caller windows followed by a synthetic stop, not complete
caller/dispatch execution. Add11A680.s to frozen inputs with SHA256
`54a63a8903fd59c8b04b3fcb671926dfac0ba82a81b953280d5311092ee4a94c`.

## Source Shape And Checked Layout

Twenty-one successful structural source forms compare early exits, shared
exits, nested conditions, declarations, formal reuse and register hints.
Initial complete C emits82 words/frame0. Sharing both record-negative and
flag-reject zero exits reduces it to78 words/frame0. The accepted source
uses structured nested C, not gotos, dummy operations or volatile accesses.
Declaration/register-hint changes do not remove the seven allocation words;
formal reuse emits79 words and is rejected. Both owner profiles have empty
diagnostics and preserve all72 neighbors and normalized pools.

`game_record_release_layout.py` specifies one closed V1/A1 GPR cycle from
word33 onward: source state V1 becomes retail A1, source actor A1 becomes
retail V1. Only words33,46,47,53,57,65,74 change. Decode real GP fields; for
LWC1/SWC1, only the base is GP. COP1 arithmetic/transfer operations and all
FP register fields stay identical. No schedule, memory access, branch,
immediate or instruction position changes. All78 origins remain exactly
once; all four bindings remain at byte offsets0,4,164,172.

Seven expected-word/expected-relocation guards encode that recipe. Exact raw
SHA, binding dictionary and normalized SHA gate it. The actual padder and
seven expanded Make commands reproduce it; no shared padder, Makefile,
compiler profile, assembly or retained data is changed. The old CSV prefix
is preserved byte-for-byte.

```text
raw:        fd31bb42488446f081ba82001aa1f0d2ed933fd9567783ee3a5cc6b7b1085a98
normalized: f6d3adaf757e663f6e8e93d6782baed348c072c7a9bbd0755b4523fbc807886c
```

## Fresh Qualification

Eleven pre-install tests pass in24.466 seconds; **eleven installed tests
pass in32.995 seconds**, without skips. Repeated raw/normalized, caller and
mapped fixtures are not additional independent input domains.

- **948 fixtures/two phases:1,896 literal pairs** agree in full modeled
  state, ordered accesses and result. The same corpus independently checks
  raw C public memory/result and ordered stores. All78 words are visited.
  Eight backed guest alias layouts redirect pointer storage or overwrite
  subsequent actor coordinates;288 executions actually redirect context.
- **262 fired access-cut pairs** confirm each requested gate. Three further
  invalid-pointer prefixes stop before the requested invalid/alignment
  access. F70/10F0 aliases request W10EF and REAB respectively; the cuts
  precede access checks and do not demonstrate hardware exceptions.
- **36 invalid-FP-load boundary pairs** stop before loading signaling/quiet
  NaNs, infinities or out-of-range coordinate values. **12 finite out-of-range
  conversion-dispatch pairs** stop before executing TRUNC. All requested
  boundaries fire. FCSR, hardware traps and invalid numerical conversion
  results are explicitly **not modeled or claimed**.
- Native32 **O0, O2 and O2+UBSan** each pass639 fixtures, checking all8,094
  numerical words across two1,408-word contexts and the26-actor buffer.
  Expected patches are endian-neutral. Executed conversions are finite and
  within signed32 range; arbitrary FP bits occur only on unvisited paths.
  Preserve the existing stack-realignment/no-strict-aliasing harness policy.
  Native row/actor backing does not validate arbitrary wide guest indices or
  signed-overflow/pointer arithmetic outside that bounded native domain.
- Five effective native source negatives alter query result, flag mask,
  record clear, double-versus-float Y addition, or truncate-before-add order.
  Each exits21 while positives exit0; no signal/trap is counted as success.
- Two effective completed **guest** C controls cache context or read flags
  too early. Context redirection changes the output bank. For slot209 /
  record0, EB0[209] aliases11F4[0], so the initial -1 clear must precede the
  flag read. That actor index is backed in the guest control, not native C.
- **96 caller-window pairs** cover all six distinct actual sites and their
  delay stores/argument loads. Only the actual JAL and delay word execute
  before synthetic stop; upstream live-ins are explicitly supplied.
- **Three independent GNU maps** agree for all78 words and four bindings,
  including HI/LO carry boundaries. Execute270 mapped cases with code,
  global pointer storage, actor array, both contexts and pointer-carrying
  alias coordinates rebased together.
- Nine raw/binding/recipe corruptions reject; six actual-padder manifest
  corruptions fire stale-word/relocation checks; three image corruptions
  fail the strict whole-image verifier. Actual padding preserves all72
  other owner bodies/addresses and normalized pools in both profiles.

## Production And Commits

The first private link matches its strict complete-image prediction on the
first attempt. Production Make reproduces the same3,257,636-byte ELF:
**240 changed bytes =238 target-code bytes +two target-symbol size bytes**
(12 ->312). No metadata permutation or broad exclusion. Every other6,056
linked body, every function address, all189,088 protected Game-data bytes /
720 owners and all other frozen inputs stay fixed.

The manifest-triggered full rebuild succeeds with the inherited duplicate
generated_12D630 recipe advisory and diagnostics from untouched code. Empty
target-profile diagnostics do not mean a warning-free whole build. Full log:
`conker/build/game-record-release/integration/production-build.log`.

```text
owner:  af0fd776d65e309e9dcc8e4d68bd3e3155dc0eff3c46faf6fa8f28da66ad96b8
guards: 5ddd1615d90ce59ff70ff6e95de91a52151b442b86156c2aea53a738393c34c3
ELF:    14bd44cfcbbb6ea376ada9c64ab529cd029dd38984f35e023ef166a594ccfcfe
```

Fresh matching: **Game3004/4832 (62.17%)**, **total3677/5505 (66.79%)**,
Init492/492, Debugger181/181, **1,828 different / zero drift**. Conversion
counts/bytes remain5505/6044 (91.08%),86.08% overall and4832/5323 (90.78%),
85.44% Game: the previous placeholder was already counted as C. Root README
contains aggregate rows only; this note owns the recovery narrative.

Both tools copies pass three repository setup tests and smoke checks;
consumer `make tools-check` passes. Five new files are identical ASCII/Python
in the standalone mirror. Preserve its ddbdd16 HEAD and all1,343 previous
dirty leaf hashes; add five task files, without mirror commit/reset. Retain
the post-commit graph-preservation audit under ignored `integration/`.
No compiler capture, Claude/REA call, sibling host or frozen Release action.

```sh
python3 -m unittest tools.tests.test_game_record_release_match -v
python3 -m tools.experiments.game_record_release_integration --audit
make -C conker match-progress NON_MATCHING=1
make tools-check
```

## Next Target

Fresh owner audit: **56/73 exact,17 different**, with the complete remaining
list in ignored `integration/owner-completion.json`. Continue the smallest
remaining stub, **func_15085BE8**, VA `15085BE8..15085DA8`, ROM
`B3098..B3258`: **112 words/frame96**,108 real differences, no helper call.
The existing caller at15085BD0 in B3020.s returns its result.

Recover six maximum/minimum scratch entries initialized to -10000/+10000, signed16
count D_80087290, and16-byte rows at D_800D2350. Row+2 is signed16; row+6
is the category byte. Compact categories whose minimum<=maximum into
D_800D237C and count D_800D2358. For each adjacent category, store float32
0.5f*(next minimum+current maximum) at D_800D2360, and set the return flag
when next minimum<current maximum. Append the100000.0f sentinel even for
zero/one active category. Preserve ordering, count/offset widths and signed
comparisons, including nonpositive row counts; native category/index validity
and guest out-of-range stack aliases need separate explicit domains.

Freeze `conker/asm/data/242480.rodata.s` before the next candidate: SHA256
`4add61fb582bd9368ec71f1a974de8545c88624aa7ee27c41d9addd675013618`.
It supplies D_8009D9C0/C4/C8 (-10000,10000,100000). Qualify the retained
returning caller, full frame/scratch lifetime and FP rounding boundaries
before any installation. Owner completion and broader Game matching remain
open; no whole-owner completion is claimed.
