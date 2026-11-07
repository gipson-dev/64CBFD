# Record lifetime and animation update recovered and byte matched

Date: 2026-11-07. Continues [Note 2160](2160-game-resource-scroll-update-match-20261107.md)
from consumer `6c8513fbcc9e0364582214bc3372f0344a831fdc` and tools
`7c89d0bde2833b3f2bd534cb1247b091e34d7032`. One qualified Game function
advances the active 80% total goal.

## Recovered interface and behavior

`void func_1513C060(u8 *record)` in `conker/src/game_169510.c` replaces its
false s32 zero-return placeholder. The complete **188 words / 752 bytes**
match at VA 0x1513C060..0x1513C350, ROM 0x169510..0x169800. Retain frame32,
RA at SP+0x14, signed byte remove flag at SP+0x1B and the resource home at
SP+0x20. No saved S registers or floating-point operations are introduced.
The ordinary O2/g3 MIPS2/O32 compiler profile is unchanged.

The callback performs these original operations:

1. Skip when word+0x10 bit0 is clear. For flags+0x18 bit0, subtract live
   D_800BE9E4 ticks from signed16+0x1C, narrowing before testing expiration.
2. Nonzero byte+0x80 selects the D_80089C70 update callback. Zero return
   requests removal. Preserve the pointer and byte-flag homes around it.
3. Flags0x8000 and0x10000 gate two timer/threshold fade updates. Signed16+0x1C
   must be below signed16+0x3A. Multiply by signed16+0x3C, compare against
   byte+0x28, then narrow into byte+0x28 or+0x2D. The second comparison still
   reads+0x28, including a possible first update.
4. While active and rate+0x24 is nonzero, advance cursor+0x20 with low32
   rate*ticks. Read the frame count from D_80090B64[byte1E*12]; the inclusive
   fixed-point limit is `(frames << 16) - 1`.
5. Above the limit, flag2 removes, flag0x40 stops/clamps, flag4 reflects by
   `limit - cursor%limit` and reverses rate. Otherwise repeatedly subtract
   the limit. Below zero, flag8 removes, flag0x80 stops/zeros, flag4 reflects
   with signed `(-cursor)%limit` and reverses rate; otherwise repeatedly add
   the limit. Preserve both signed remainder operations and trap guards.
6. On removal, nonzero byte+0x81 selects D_80089CA8. Its zero return retains
   the record; nonzero releases through func_1516972C. No callback releases.

Live callback mutations and the captured/reloaded homes remain significant.
The existing struct210 contains padding/other views over several packed
fields, so the recovery uses local byte-offset views and callback declarations
without broad shared-struct changes. Original assembly remains retained.

## Source shape and explicitly bounded normalization

The selected C itself emits all 188 words and the correct frame/homes.
Raw target SHA-256:
`eaa43dd093d333255d8e5a71786b1524588e38de7cc5977f5aed5b97b5baa1f3`.
All **12 relocation bindings** remain literal. Sixteen exact expected-word
guards normalize two closed differences:

* Eight words move the early flags lifetime from A2 to A1. A2 is overwritten
  by the rate load before reuse; A1 is overwritten by the frame-table address
  before reuse. The complete source/body/binding fingerprints pin this range.
* Eight words forward each cursor loop's own preceding store, and retain the
  retail copied cursor in its branch delay. At every loop edge, V0 equals
  RAM[A0+0x20]. A0/V1 are fixed and the only loop store writes that same word.
  There are no calls or other mutations inside either loop. Induction over
  the original 32-bit add/subtract and signed comparison preserves the cursor,
  trip count and ordinary-RAM result.

There are no inserted/deleted instructions, branch retargets or synthetic
padding. The forwarding contract is ordinary mapped RAM without concurrent,
volatile, atomic or MMIO effects. **Raw C claims public memory/call/termination
agreement within that contract. It does not claim raw private-register,
access-prefix or fault equivalence.** Normalized output matches retail's
complete private state and access order separately.

Six dedicated closed-loop checks validate the invariant, and two effective
counterexamples deliberately break it and produce different results. This
records the required precondition rather than treating the rewrite as a
generic load deletion. All other words stay literal.

Declaration and expression screens recovered the byte home, explicit frame
count and cursor update shape. Signed-shift controls were not selected; the
bit test uses an unsigned shift and the qualified 32-bit interpretation.
The first screens were185/186 words. Whole-owner source screens and raw hashes
remain in the adjacent private directory.

## Original registry caller and independent semantics

The aligned retained-ROM census finds no direct target JAL, exactly two entry
pointers at ROM0x2304E4/0x230E70, VA0x8008BA24/0x8008C3B0, and no interior
pointers. They are slot0 of the52-byte registry records for kinds0x1B/0x4A
at D_8008B4A8. The existing creator func_1513C350 selects those same kinds.

The complete original **74-word func_151670C0** passes one resource pointer
through that slot and does not consume V0. **80 connected cases per body** cover
both kinds, both banks, one/two-record chains, two nesting depths and provider
mutations. All74 dispatcher words execute, including the next-link store
before JALR. **This dispatcher remains unrestored in production C.** Its
original retail execution qualifies the callback interface; this change does
not claim a restoration of the dispatcher or live gameplay acceptance.

Seven focused checks pass before and after installation in both tools copies:

* **963 guest cases per body** compare retail, normalized and raw C against an
  independent integer memory/call/termination model. Cover flag combinations,
  expiration/narrowing, fades, signed cursor limits/remainders, repeated wraps,
  all13 update and3 exit targets, callback outcomes/mutations, pointer/flag
  homes, record/global aliases and the reachable negative-overflow trap.
  A disabled record requires only its active word and actual private frame.
* **185 words execute**; all188 compare. The unexecuted literal trap words
  are114,120,151. For all256 possible frame-count bytes, the derived limit
  is nonzero, so the two zero-divisor traps cannot fire. The positive branch
  also cannot contain INT_MIN/-1, proving its overflow guard unreachable.
  The negative reflection overflow trap does fire in a guest-only fixture.
* **60 fired access cuts**, including 11 delay cuts, compare normalized/retail
  full private memory, GPR/FPR/HI/LO, PC and access-prefix traces. RA, stack and
  signed byte-flag home lifetimes stay exact. Raw redundant reads are outside
  this private/fault identity claim.
* Native32 O0/O2/O3 each pass **942 ordinary-record cases** with actual SDK types,
  pointer32 assertions, typed void updater/s32 callback tables, disjoint
  banks and trapping UBSan. Ten compiled negatives reject with exit1: stub,
  skipped timer, wrong update/exit gates, missing release, wrong second fade,
  wrong period/reflection/reversal and stale flags.
* Two independent GNU links verify all12 bindings and signed LO16 carries.
  Altered raw words/bindings, guard history, register metadata and six strict
  whole-image corruptions reject.

Callbacks and release remain explicit bounded providers. Out-of-table indices,
private-home writes, aliases and exceptional arithmetic remain guest-only.
The modeled DIV overflow register result is a bounded convention followed by
the retained software trap, not a hardware exception claim. Portable C does
not define the exceptional signed division; it is excluded from native cases.

The native fixture caught a second-record/guest-stack overlap in the initial
test map. The second bank moved to0x50000, explicit bank-disjointness checks
were added, and the complete model/caller/native suites were rerun. No record
or stack bytes were removed from observation to make that fixture pass.

One packet-only Claude request was made with tools/customizations disabled.
Its response was lost when the Windows log writer rejected a Unicode character;
the writer was fixed to UTF-8. No review findings are retained or credited and
no second request was made. Qualification rests on the direct proofs and tests.

## Whole owner, actual Make and linked checkpoint

All **181 frozen inputs** remain accounted for, with tools/dependencies hashed
separately. All **58 raw and padded neighboring functions** remain literal.
Raw/padded pools, register masks and options are unchanged. All43 inherited
compiler warnings are identical; none are added. The private padder honors
the existing Makefile's `jtbl_800A5188_game` rodata anchor. The initial manual
rebuild omitted that argument and correctly failed object identity; applying
the existing rule reproduces the full predecessor object, without exclusions.

Actual Make recompiles only game_169510.c and equals the strict independent
image prediction: **533 changed bytes, zero exclusions**. They comprise515
Game body bytes,8 symbol-table bytes and10 string-table bytes. One closed
adjacent metadata pair swap, D_80089C70 / D_800E0D9E at file offset2979468,
accounts for the serialized ordering change. The exact predecessor slots,
complete names and permutation are pinned. Named value/type/section fields
stay fixed; only this target's extent changes12->752.

All **6,052 function addresses** and other bodies remain fixed. All **189,088
protected Game bytes across720 owners** remain exact. Exactly16 guard rows
append. Historical guards, conversion CSV and Makefile are unchanged. Compile/
link succeed; whole-ROM checksum retains expected nonmatching exit2 and the
inherited duplicate generated_12D630 recipe warning.

Both tools copies pass fresh shared smoke checks. Three unchanged shared
regression receipts per copy are reused after exact helper/test hashes. A
disposable overlay and explicitly hashed read-only alloc_pools fallback keep
all2,434 inherited dirty sibling paths unchanged.

| Section | Exact / converted | Percent | Drift | Still different |
| --- | --- | --- | --- | --- |
| Total | 4,231 / 5,512 | 76.76% | 0 | 1281 |
| Game | 3,558 / 4,839 | 73.53% | 0 | 1281 |
| Init | 492 / 492 | 100.00% | 0 | 0 |
| Debugger | 181 / 181 | 100.00% | 0 | 0 |

**179 more exact functions** remain to4,410/80%. Root README receives only
aggregate rows; four concise index leads preserve their historical bodies.
Refresh Graphify on changed paths, retaining excluded legacy nodes fail-closed
without claiming a new full-corpus extraction. Commit tools before consumer
source/docs/pin, then verify fresh hook completion and production stability.

| Artifact | SHA-256 |
| --- | --- |
| Production ELF | `150e1bff286d9d9af64604e00a1707e320b90db014998234db9290241cc4b448` |
| Production binary | `87fc76e9c30b066f6c81ecf6103b1889f0f87546d609310a23c923871d3d8e2a` |
| Padded owner | `aa7108e732bb4edccc6b2b3773f4505f8526a4c841542ec169d75e0e720008a1` |
| Guard manifest | `7ef176125a7b37e6e890ea01d8e76e3becaf14ff54fb3c0d6ff3ea1d12705d76` |

Ignored receipts: `conker/build/game-record-animation-update-1513C060-match/`;
source screens and the review capture failure remain in its private sibling.

Next: **func_1513CFE4**, the related195-word updater at VA0x1513CFE4..
0x1513D2F0, ROM0x16A494..0x16A7A0. Recover its additional callback and shifted
field layout from the full retained window, then qualify it independently.
Keep the80% goal active and other private candidates uncredited. Preserve all
frozen handwritten/hidden-ABI boundaries, unrelated work, private inputs,
saves and the frozen host Release checkpoint.
