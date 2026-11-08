# Position/Subtype Query Direct Match - 2026-11-08

`func_150A3058` replaces its zero-return placeholder with the complete
class-3 record/position query. All **79 words emit directly from C**, with
the original **888-byte frame**, seven initialized local actor fields,
five bindings, and saved-register lifetimes. No guards, compiler profile,
shared-header, data or metadata-order changes.

Fresh production count: **4245/5513 = 77.00%**, Game **3572/4840 = 73.80%**,
Init 492/492, Debugger 181/181, zero drift. **166 more** exact functions reach
4411/5513 and 80%. Conversion counts and the progress CSV stay unchanged.

## Source, ABI and ordered behavior

Entry 150A3058..150A3194; ROM D0508..D0644; 316 bytes. Owner
`conker/src/game/generated_CDE80.c`; normal IDO 5.3 O2/g3, MIPS2/O32.
Interface: `s32 func_150A3058(s32 subtype, s16 x, s16 y, s16 z)`.

The signed short coordinates become exact float32 values in a local
812-byte struct127. The routine initializes current x/y/z, old x/y/z, and
secondary Y at offset 180. Original incoming coordinate homes contain the
full supplied words before their low halves are sign-extended. Other local
actor bytes are deliberately left as the original stack contents.

The scan uses unsigned D_800D3094 and 0x34-byte records at the live
D_800D3098 pointer. It requires byte14 zero, flags>>2 equal to 3, and byte17
equal to the complete subtype word. A zero result from func_150A1DA0 with
that local actor, the record address and mode zero returns 1 immediately.
Exhaustion returns zero. Rejected/provider paths reload the count; loop
continuation reloads the record base. The local actor is built once, so
provider changes to it survive subsequent iterations. Input-home rewrites
do not rebuild its coordinates.

The initial candidate already had 79 words/frame888, with one commutative
addu operand-order difference in the descriptor address. Unsigned offset,
reversed addition and comparison-order variants still leave that difference;
a byte-pointer form has 21 differences. Expressing the descriptor base as
u32 recovers retail's offset-first addition without a guard. Raw SHA-256:
`b27e518bfe6748d268e56d6ff60db39fe46b742b712214a246cea693ab7bc330`.

## Complete owner, actual Make and image gates

Predecessor consumer 99fc2d63b7f586156ab09f9b2c317521705a4994; tools
af166b5ef3d54a3566fefb4a443d13d80138503f. Qualification freezes 103
source/header/compiler/input files, including both original caller owners.
All 27 raw/padded neighbors, bindings, allocatable pools and register
metadata stay fixed. Production and strict padders agree on all 28 functions
and pools, with all 31 preserved original case-label definitions accounted for.

The actual copied five-command Make recipe reproduces the complete qualified
object. Production compiles this owner once under O2/g3 and emits no C
warnings. The independent whole-image predictor equals production after
**241 changed bytes, zero exclusions**: 239 target-body bytes and two
symbol-size bytes, from 12 to 316. No metadata permutation is needed.

Every other linked body, all 6053 addresses and all other named definitions
remain fixed. All 189088 protected data bytes across 720 owners remain exact.
Makefile, guard CSV, headers, layout, absolute rules and progress CSV are
unchanged. Existing duplicate generated_12D630 recipe warnings and the normal
development-image checksum rejection are separately recorded. The guard CSV
is checked without rewriting it or changing its modification time.

## Focused qualification

Both mounted and sibling configurations pass six fresh tests before and
after installation. Three new modules use an ignored sibling overlay. Its
missing pool helper uses an explicit mounted fallback; other helper origins
and every task/dependency module fingerprint are recorded. Its 2434 existing
dirty paths remain unchanged. Both shared smoke checks are fresh; three
unchanged shared regressions per copy are explicitly reused by hashes.

| Check | Evidence |
| --- | --- |
| Ordered guest model | 905 cases; complete literal state equality and independent callback/query observations |
| Query payload | All seven initialized float fields; complete 812-byte observations in seeded guest RAM; original uninitialized bytes retained |
| Scan behavior | Disabled/class/subtype gates, full-word subtype, unsigned count, growth/shrink, live table redirects, first accepted record and empty scans |
| Aliases/mutations | Local-query/table/incoming-home/global overlap probes, provider query changes and incoming-coordinate-home rewrites |
| Callers | Three original windows totaling 59 words; 36 connected cases; actual float truncation, signed-halfword narrowing and branch consumers |
| Native32 | 386 cases at each of O0/O2/O3; typed s32/s16/s16/s16 entry; real SDK actor812/descriptor52/pointer32 layout sizes; trapping UBSan |
| Effective negatives | Stub, unsigned X, wrong secondary Y, wrong class, byte subtype, inverted provider truth, cached count and query reinitialization |
| Fault prefixes | 167 executed-access cuts, including local setup/stores and live scan loads; exact literal low-word machine states |
| Relocation/image | Two independent GNU links of all five bindings with signed LO16 carries; four complete-image corruptions rejected |
| Fail-closed inputs | All 79 raw-word corruptions, all five binding corruptions and guard-prefix corruption rejected |

Exactly 78 words are reached from the public entry in this corpus. Word 62,
`lw t7,0(s3)` at 150A3150, is unreachable in the original ordinary control
flow after the unconditional success return. It remains literally matched;
no instruction is dropped or entered artificially to inflate coverage.
The original ROM contains no entry/interior pointers or direct interior jumps.

The three JALs occur at ROM E647C, E7428 and E7474. The first caller uses
subtype 1; the second and third use subtypes 2 and 1. Their original float
coordinate loads/truncations, explicit short sign extension, delay slots,
restored floating arguments and branch-likely return-address load are
connected to the actual query. Ordinary and wrap-to-short finite-coordinate
cases are covered. The complete large physics/script callers are not claimed.

Native providers read only the seven initialized fields. Arbitrary sparse,
wrapped and stack/global alias probes belong to the bounded guest contract,
not portable C array/padding claims. The collision provider remains a separate
production placeholder and bounded test service; its geometry/gameplay is
not qualified here. Full hardware upper-register/FCSR behavior is not modeled.
Routine task: zero Claude calls. The host and frozen Release remain untouched.

## Bank and next action

Production ELF SHA-256: `3be4682d22779bf33a8fe268d5991efc97f06044f7f5fb69a915994ac2237ba2`.
Binary: `5f5c443c597210dc56bcda3338d06fc178b70502922e37740727038247aa5982`.
Owner: `499967fdae0d2c33faa7727153c21bf562d4422da39217a92723d94172427a5c`.
Unchanged guard CSV: `9a0c7123b46c9a22927ff17a9aa46b3eba0f53256d31f0c2a1b461b5dd05d3d0`.

Reproduce in prepared WSL from the consumer root:
`python3 -m unittest tools.tests.test_game_position_subtype_150a3058_match -v`.
Canonical receipts: `conker/build/game-position-subtype-150A3058-match/`.
Tools first, then source/docs/README aggregate rows/pin are committed locally.
No push. Graphify uses a scoped refresh with explicit old-node retention,
not a full-corpus extraction.

Next inspect `func_150A104C`, the 94-word record-list/view-state updater,
including its large local actor, live list reloads, flag bit and height field.
Keep the full 80% goal active; func_1513FAB4 remains private and uncredited.
