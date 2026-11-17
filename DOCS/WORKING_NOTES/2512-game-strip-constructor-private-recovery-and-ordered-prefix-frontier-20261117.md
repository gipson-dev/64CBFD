# Strip constructor private recovery and ordered prefix frontier - 2026-11-17

`func_151ACBD4` has a complete private C recovery for the twenty motion samples
and two banks of twenty four-vertex strips. The useful v2/v7 drafts emit **386 words with
retail's frame 0x40**, preserving all **32 owner neighbors and normalized pools**.
Retail is **360 words / 1,440 bytes**, VA 151ACBD4..151AD174,
ROM 1DA084..1DA624. The opening and complete output behavior are qualified;
the v2/v7 ordered FP relation and byte fit remain open. The v35 follow-up below
closes the complete provider/return relation after four private scheduling words.
**No source installation,
new guard, build-profile change or matching credit.**

Accepted progress stays **4,531 / 5,514 (82.17%)**, Game **3,858 / 4,841
(79.69%)**, Init 492/492, Debugger 181/181, zero address drift, 983 different.
**156 further matches** are needed for the active 85% goal. Root README is
unchanged; this candidate is explicitly uncredited.

## Recovered interfaces and behavior

The constructor accepts a 36-byte descriptor and a 32-bit extra-byte count,
returning a 32-bit record handle. The complete original routine and six call
sites were inspected: two C scene callers and four calls in asm/3CE80.s.
Complete connected-caller execution remains an adoption gate. The legacy
struct179/struct180 declarations mix integer and float members; their physical
layout agrees, while retail reads several copied fields as binary32. Shared
headers are preserved. The recovered private record is 88 bytes, each motion
sample 24 bytes, each texture-table entry 12 bytes, and each SDK vertex 16 bytes.

The constructor selects class 0x4E for category 0x2C, otherwise 0x2F, and allocates
the wrapped extraBytes+0x58 size. A null first result returns zero. It copies
36 descriptor bytes to record+0x10, calculates reciprocal scale, clears state
and status, then allocates 480 bytes for 20 samples. It truncates start XYZ and
endY, interpolates Y through wrapped low-word multiplication and signed /19,
and initializes three zero velocities. Spacing is the signed wrapped height
difference divided by 19. It then allocates 2,560 bytes for two banks of 80
vertices. Category 0xB selects texture 55/shift 4, otherwise 54/shift 5; category 0x39
selects RGB 88/75/44, otherwise 255/255/255. Width/height come from halfwords
at 6/8 in D_80090B60. Only flags, texture coordinates and color are initialized;
the vertex position bytes stay untouched. It clears time and returns the record.
The two buffer allocations have no retail null-result checks; none are added.

The selected C explicitly wraps subtraction, multiplication and addition before
signed division. A simpler signed expression triggers an effective native UB
trap at extreme valid coordinates. Random draws and loop caps are not introduced.
Allocator services may mutate descriptor bytes before the copy, coordinates
after reciprocal calculation, and category/table data before vertex setup.
Fresh reads and the preserved fields are covered by the independent reference.

## Measured fitting and instruction-order frontier

Forty complete source forms v0..v39 and three isolated compiler-option probes
are retained. The first generic corner loop/u[4] draft used frame 0x98. Explicit
four-vertex stores removed that array and recovered frame 0x40. Default v7 uses
a four-sample motion unroll; retail's live loop processes pairs. Counter widths,
trip-count captures, paired source, scopes, named fields, expression forms and
local loop-unroll options produced measured alternatives, without installing
any profile. No body/profile is selected by instruction count alone.

The guest execution reaches 319/360 retail words. The 33-word scalar block
at +0x110..+0x194 exclusive is skipped by an unconditional setup branch; eight
other unreachable words are normal-domain division guards. Its likely compiler
unroll origin is an inference, separate from the observed control flow.

The instruction-driven model proves **four opening paths** through the record
allocation, descriptor copy and reciprocal/state/status setup, stopping before
the point-buffer allocation. It compares every initialized public object byte,
all 80 private/incoming-home bytes at providers, ordered FP/FCSR, actual typed
arguments and null-return saved-register custody. Four deliberately corrupted
size/copy/division/field words reject.

After the point allocator, v7's full prefix has **two passing null routes and
two failing success routes**. Retail orders its TRUNC operations X,Y,endY,Z;
v7 orders X,Y,Z,endY. A strictly private four-word schedule diagnostic exchanges
the two conversions and their corresponding MFC1 transfers. It advances the
comparison through all twenty sample values, then finds the next difference:
retail executes CVT.S.W on integer 19 before the spacing numerator conversion;
the draft materializes float 19 directly. That operation is retained as an
ordered FP/FCSR boundary, not silently discarded because 19 is exact.
These diagnostic words are **not installed guards**. Whole-function proof is
explicitly false, and full private/return equivalence beyond the opening is
not claimed. The symbolic model assumes fresh, mutually disjoint allocator
objects, mapped/aligned private storage and ordinary execution. It does not
prove overlapping allocations, fault-register identity, arbitrary aliasing,
interrupt/hardware behavior or gameplay acceptance.

## Fresh reproducible qualification

All **four maintained private checks** pass in primary tools and the isolated
sibling overlay with identical seven-file fingerprints. The check names and
receipts explicitly retain the open FP frontier rather than calling it a match.

- **1,016 guest cases per retail/v2/v7 stream** compare all initialized public
  bytes, all four helper calls and return values. Coverage includes allocation
  failure, all descriptor byte tags, two stack phases, category branches,
  mutable providers, boundary integer wrapping, texture dimensions 0/65535,
  scale zero/signed zero/NaN/infinities and untouched vertex-position bytes.
  Coordinate truncations stay in the finite signed 32 domain.
- **1,016 SDK32 C cases at O0/O2/O3** pass with strict aliasing and UB traps.
  The signed-interpolation control exits by SIGILL as intended; four wrong
  class/texture/UV/position variants exit 3. All eight executions have the
  expected result. Native tests do not compare FCSR.
- Complete-owner compilation preserves 32 neighbors and pools. The exact
  four-path opening and its effective rejection controls are fresh in both
  tools configurations. Complete caller, both-padder/rebase, full-image and
  production-adoption gates remain open for this candidate.

The **1,482-input** qualification snapshot uses 1,475 immutable-snapshot links
and seven copied task files, with zero live-worktree hardlinks. Every input
remains unchanged. Production ELF remains byte-for-byte
`d54f29167c029522c57b33b4a5678ab2e3866b37820686566daeb73b35fea992`.
No production rebuild is performed for an uninstalled candidate. Shared tool
checks and a fresh real-ELF recount pass. Sibling 2,434 dirty paths and 339 scoped
dependencies stay untouched; the overlay resolves 7 task modules, 301 sibling
modules and 27 unchanged primary fallbacks. No host, Release or save changes.

Use a fresh owned path in `CBFD_STRIP_PRIVATE_WORK`, then run
`python3 -m unittest tools.tests.test_game_strip_constructor_151acbd4_private -v`.
Receipts, exact imported origins, frozen inputs, probes and compiler products
are retained in `conker/build/game-next-151acbd4-private/qualification/` and
the adjacent private study directory. No push.

## Complete ordered relation follow-up

The retained **v35** source captures `count = record->count = 20` and uses
`(f32)(count - 1)` for spacing. It emits the retail conversion of integer 19
before converting the height difference. This preserves the ordered FP/FCSR
operation that the earlier literal `19.0f` draft omitted. Its complete body is
**388 words / frame 0x40**, with all 32 owner neighbors and pools unchanged.

With exactly the same four private TRUNC/MFC1 scheduling words, the complete
instruction-driven provider/return comparison now passes **all ten paths**:
two null-result paths and eight successful category/texture/color paths.
It compares all public object bytes, all 80 private/incoming-home bytes,
typed provider arguments, ordered FP/FCSR operations, preserved registers and
the final return handle. Undoing the schedule rejects all eight success paths
at FP trace event 12. Independent wrong-return and wrong-time-field controls
also reject. These are private diagnostics; zero production guards are added.

All four new maintained checks pass freshly in primary tools and the isolated
sibling overlay. Guest checks compare retail, raw v35 and the scheduled v35
diagnostic over **1,016 cases each**. Native v35 passes the same 1,016 fixtures
at O0/O2/O3 with strict aliasing and UB traps; its five negative variants have
their expected failing exits. Native checks do not assert FP-status parity.
The symbolic result retains the fresh, disjoint, mapped-object assumptions
above. It does not establish fault-register identity, arbitrary allocation
overlap, complete connected callers, portable C evaluation order or hardware.

Five additional source forms v40..v44 test a count shared by both loop groups,
spacing and bank dimensions. They emit 285 or 454 words with unchanged owner
neighbors. The 285-word form changes the opening saved-register/private-frame
relation and is rejected there despite its equal frame size. Four more forms
v45..v48 test inline wrapped height differences and a count-based inequality;
they emit 391, 278, 445 and 389 words, with all 32 neighbors and pools unchanged.
These results leave 49 measured source forms and three profile probes; no new
profile is installed. Continue fitting the paired loop and 360-word slot.

The new immutable snapshot contains **1,486 inputs**: 1,482 links to the prior
sealed snapshot and four copied tools, with zero live-worktree hardlinks.
All input bytes and the production ELF remain unchanged. Shared tools checks
and the fresh actual-ELF recount pass. The dirty sibling and host surface stay
untouched. Receipts are in `conker/build/game-next-151acbd4-private/ordered-qualification/`.
Use a fresh `CBFD_STRIP_ORDERED_WORK` path and run
`python3 -m unittest tools.tests.test_game_strip_constructor_151acbd4_ordered -v`.

This stage adds no source or matching credit. Total remains **4,531 / 5,514
(82.17%)**, with **156** more needed for 85%. Finish the source/slot fit, all
six connected caller checks, both padders and rebases, strict whole-image
prediction, actual production Make and final recount before adoption.
No additional Claude call was used for this follow-up. Graphify retains old
nodes and the explicit ordered-tools reference; it is a scoped refresh.

## Bounded review and next work

One packet-only Claude analysis completed through the existing claude.ai /
firstParty / Pro route. Init advertised tools=[], mcp_servers=[] and there was
no structured tool use. Packet SHA256:
`243e8512abc3d8c5b952e003cd56987373f7fc42abf38f170238b936e524224d`.
Its suggested early delta dependency compiles byte-identically to v7 as v38,
so it does not fix scheduling. Its second test repeats measured evidence;
the dynamic spacing form is retained as v39, 388 words, with no accepted fix.
The response's textual Write/plan-file claim was checked: no actual tool event
or claimed file exists. No review patch or conclusion is adopted by agreement.
The packet's 34-word dead-block count is corrected to the measured 33 words.
No second review is requested.

Resume this function from the complete v35 relation above. Keep the four private
conversion/MFC1 diagnostic words and explicit CVT19 qualified while fitting the
original paired loop and full slot. Continue the pair-loop source fit
from measured control flow, and qualify all six callers before attempting
guards, independent links and whole-image adoption. Keep this private recovery
uncredited until every production gate passes. Graphify refresh retains old
IDs and records the private tools-to-function reference; no full-corpus claim.
