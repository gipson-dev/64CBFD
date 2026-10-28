# Dependent record load - direct C match

Verified 2026-10-28. Restore func_151839F0 in generated_1B0740:
VA 0x151839F0..0x15183ACC, ROM 0x1B0EA0..0x1B0F7C, 55 words / 220 bytes.
The normal O2/g3 profile emits every original word directly, with frame40,
eight relocations and no guards. Keep the retail name and behavior comment.

## Recovered behavior and interfaces

The interface is void func_151839F0(s32 requiredIndex, s32 index).
Both indices select the existing eleven-entry D_800DDE80 record table.
If the prerequisite record is empty, call func_15183ACC(requiredIndex).
Reload its first word afterward. Only when that record is now available
should the routine inspect the destination and load it if empty.

The destination load calls func_1502B6BC(NULL, 0, NULL, 2, 9, index+0xAD).
Its established interface is void *func_1502B6BC(s32 *size, s32 count,
s32 *relocated, s32 depth, ...); the final two values are real varargs.
On success, store the returned pointer and copy returned words0,2,6 into
record words1,2,3. Clear record word4 and set D_800DDF68[index] to one.
There is no destination graphics-helper call in this routine.

Failed prerequisite initialization skips destination loading. A failed
allocation retains provider mutations while skipping the field/flag stores.
When both indices name the same record, successful initialization makes the
destination occupied, so the second load is skipped. Initialization may also
populate or clear the other record; neither gate may use a stale snapshot.
Preserve access order when returned data overlaps either record.

The existing void initializer declaration and variadic loader declaration are
reused. Move the single existing D_800DDF68 extern before this function so it
is visible to both this routine and the initializer. No shared header changes.
The initial explicit record-pointer local gave55 words but frame48 and nine
stack-offset differences. Direct indexed accesses recover frame40 without
guards. RA is at SP+0x1C, the row spill at +0x20 and destination-index home
at +0x2C. The prerequisite index does not need to remain homed after its call.

## Original caller and helper boundaries

The aligned retail census finds one direct JAL, at ROM0x1B09AC / VA0x151834FC,
in the392-word func_15183290, with no target pointer literals. The preceding
instruction at0x151834F8 passes prerequisite7; the call delay slot passes
destination10. 288 cases execute every word of the24-word original route
0x151834F8..0x15183558, through the following func_15174FA4 call and the
branch to0x15183888. That renderer receives ten observed arguments, including
two floating-point bit patterns in the stack argument area, and is bounded.
The parent and renderer C placeholders remain uncredited. Other parent routes
and complete renderer behavior are not claimed.

1,296 connected cases execute all54 original initializer words. A further
1,152 cases connect the original77-word asset loader as well, including
missing path components, null allocation, zero post-allocation size, equal
indices, overlapping returned data and graphics-helper mutations that leave
the prerequisite unavailable. The already adopted initializer and loader
bodies remain unchanged and receive no duplicate matching credit.

All73 asset-loader instructions reachable through depth-two / NULL-output
calls execute. Unvisited addresses are0x1502B6F0,0x1502B7BC,0x1502B7C0 and
0x1502B7C4: optional output branches and an unreachable word. Full loader
interface coverage is not claimed. Deeper services remain bounded:
func_1502AC88, func_1502B350, func_1502B4A8, func_1510CE60 and func_15174FA4.

## Qualification and production

Each tools copy passes eight fresh canonical methods and shared tools checks.
After installation each passes two fresh checks, with six unchanged semantic
methods reused only under identical module/input/artifact fingerprints.

- 6,418 guest cases visit all55 target words and compare complete machine
  state, memory, calls and access traces across original, raw C and padded C.
  Cover all121 normal index pairs, equal-row behavior, six returned-record
  overlaps, both stack phases, live gate mutations and sparse extreme indices.
- Native32 O0/O2/O3 each pass16,384 cases with trapping UBSan, all121 defined
  index pairs, real variadic arguments and nineteen effective wrong-C controls.
  Equal indices are a defined native alias. Returned data is a separate valid
  array; cross-record data overlaps and extreme indices remain guest-only.
- Twenty IDO-compiled semantic negatives are rejected, covering stale gate
  snapshots, omitted/wrong initialization, incorrect provider arguments,
  wrong copied fields/flag/clear and an early copy exposed by overlapping data.
- 82 fault-prefix triples and344 connected-provider prefix pairs preserve
  complete machine state, PC, delay-slot state and access order. These are
  guest fault checks, not portable-C fault claims.
- Three GNU layouts pass72 cases across HI16/LO16 carry boundaries. Three
  raw/binding corruptions and eight whole-image corruptions fail closed.

The actual three-command Make recipe and generated padder reproduce the
qualified object. Selected, owner and recipe compiler diagnostics are empty.
The full build retains the unrelated duplicate generated_12D630 recipe warning.
All eight other owner functions, relocations and constant pools are preserved.

The16,428-path qualification seal and390 focused inputs remain pinned through
production. The independent entire-image prediction allows exactly165 changed
bytes:164 code bytes and one target extent byte (12 ->220), with zero exclusions.
All6,056 function addresses and6,055 other linked bodies stay fixed, along with
all720 protected Game owners /189,088 bytes, ELF geometry and named definitions,
guard manifest, shared headers, Makefile and conversion inventory. No guard
is added or removed.

| Artifact | SHA-256 |
| --- | --- |
| Raw C and original relocatable body | 996e6292aa8afb1951267d5d50daf7c910096f7cfdd81c83a3606b7b959af3ef |
| Linked retail slot | c4f49ac2322f8e67208690a5a9d438eff3ed6003492c79213f9960d7d444e41c |
| Adopted owner object | 425f206bc7a52ef145ad41cf6d4ce1d12609f797dec8daa0ddf0dbb2e3d70960 |
| Adopted ELF | 701bc876df16234842a1432aa15e06b2d3371a81a444b688863f8bf3b6fbeb14 |
| Unchanged guard manifest | 91cfc61697b2f874f74475c5dadac1faec1f2e3c4f2a515d593b62d15b71ba03 |

## Bank and measured progress

Predecessor consumer: 311939e6d5461797127cc084a5ad0e4f360994bd.
Tools committed first: 79499020fdeacae87a034f372ecfe5e72931b4a8.
The consumer commit banks source, tools pin and measured documentation.
Preserve1,811 inherited dirty paths in the older tools mirror and three new
qualification files. No push or mirror commit; routine Claude calls:zero.

| Section | Byte-exact C | Address drift | Different |
| --- | --- | --- | --- |
| Total | 3,868 / 5,506 (70.25%) | 0 | 1,638 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 3,195 / 4,833 (66.11%) | 0 | 1,638 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

262 more exact functions are needed for4,130 /75%. Remaining shapes are1,509
placeholders,120 semantic/other and nine unlocated. Only func_151839F0 gets
new credit. Next inspect the64-word record cleanup func_15183C28 in this owner.
Keep func_1514E920 parked and uncredited.

Evidence lives under conker/build/game-dependent-record-load-match/: complete
owner preparation, canonical and installed receipts, sealed production/adoption,
actual ELF recount and canonical function views. The final handoff records the
consumer commit, scoped AST refresh and closing audit. Root README receives
only aggregate rows; detailed recovery history stays in this note.
