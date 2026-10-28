# Record initializer - direct C match

Verified 2026-10-28. Restore func_15183ACC in generated_1B0740:
VA 0x15183ACC..0x15183BA4, ROM 0x1B0F7C..0x1B1054, 54 words / 216 bytes.
The first complete candidate emits all original words directly under the normal
O2/g3 profile, with a 40-byte frame, eight relocations and no word guards.
Keep the retail function name and a concise behavioral source comment.

## Recovered behavior and interfaces

The interface is void func_15183ACC(s32 index). The existing table D_800DDE80
contains eleven Record15183974 entries, each holding five signed words.
An occupied record returns immediately. Otherwise load the two-component
asset path (9, index+0xAD), with NULL size and relocation outputs and count zero.
On a non-null result, store its address and copy returned words zero, two and
six into record words one, two and three. Publish returned word four through
D_800DDF78[index], then call the graphics-resource helper with arguments
(data, 0, 1, 0x3E, &record.words[4]). Finally set D_800DDF68[index] to one.

Allocation failure retains any loader side effects and skips the field copies,
graphics helper and ready flag. The graphics helper's return value is ignored:
even a zero result is followed by the ready-flag store. Its mutations to record
fields and the published resource survive; only the flag is overwritten afterward.
Publishing the resource before the helper and preserving overlapping copy order
are observable requirements, rather than interchangeable source rearrangements.

Use the established provider declarations:

- game_57FA0.c: void *func_1502B6BC(s32 *size, s32 count,
  s32 *relocated, s32 depth, ...). The two path components are real varargs.
- generated_139FC0.c: s32 func_1510CE60(void *data, s32 unresolvedOnly,
  s32 retain, s32 priority, s32 *output).

Correct the local forward declaration from s32 func_15183ACC() to
void func_15183ACC(s32 index). Both already recovered callers compile unchanged
at the instruction and relocation level. No shared header or compiler profile
changes. Direct table indexing lets IDO compute and spill the row pointer;
RA is at SP+0x1C, row spill at +0x20 and argument home at +0x28.

## Callers and provider scope

The aligned retail ROM census finds fifteen direct JAL sites and no target
pointer literals. Ten sites belong to func_15183290, one to func_151838B0,
two to func_15183974, one to func_151839F0 and one to func_1519897C.
The original call and delay-slot pairs pass 360 cases, covering all thirty
selected words. These bounded call windows do not claim complete dispatcher
or gameplay coverage. Existing C call sites ignore the result.

A further 288 cases execute both complete original neighboring wrappers,
func_151838B0 (49 words) and func_15183974 (31 words), with retail, selected
raw C and padded C initializer bodies. All eighty wrapper words are visited.
The wrappers' own implementations remain unchanged and get no duplicate credit.

192 connected cases execute the original 77-word func_1502B6BC. All 73 words
reachable through the depth-two, NULL-output interface execute, including
missing path components, null allocation and zero post-allocation size.
Unvisited addresses are 0x1502B6F0, 0x1502B7BC, 0x1502B7C0 and 0x1502B7C4:
optional output branches and an unreachable instruction. This is not full
loader-interface coverage. Its already exact source, object and linked body
are preserved. Deeper boundaries remain explicit: func_1502AC88, func_1502B350,
func_1502B4A8 and func_1510CE60. The graphics helper is a bounded service here;
its complete original instruction stream is not claimed as exercised.

## Qualification and production

Each tools copy passes eight fresh canonical methods and shared tools checks.
After production, each passes two fresh installed checks. Six unchanged semantic
checks are reused only with exact module, input and artifact fingerprints.

- 5,664 guest cases visit every initializer word and compare complete state,
  memory, calls, provider-entry observations and access traces across retail,
  raw C and padded C. Cover all eleven normal rows, six returned-record
  overlaps, both stack phases, helper mutations and sparse extreme indices.
- Native32 O0/O2/O3 each pass 8,192 cases with trapping UBSan, all eleven
  defined indices, real variadic arguments, graphics-helper arguments and
  nineteen effective controls. Native returned data is a separate valid
  array. Cross-record pointer arithmetic and extreme indices are guest-only;
  no portable native alias guarantee is claimed for those cases.
- Twenty IDO-compiled wrong-C controls are rejected, including wrong provider
  arguments, premature flag stores, honoring the graphics-helper failure,
  incorrect fields and an early-copy mutation exposed by overlapping data.
- 58 fault-prefix triples and 207 connected-loader prefix pairs preserve
  machine state, memory, PC, delay-slot state and access order. This is guest
  fault behavior, not a portable-C fault claim.
- Three GNU layouts pass 72 cases across HI16/LO16 carry boundaries.
  Three raw/binding corruptions and eight entire-image corruptions fail closed.

The actual three-command Make recipe and generated padder reproduce the exact
qualified object. All selected, owner and recipe compiler diagnostics are empty;
the full build retains the unrelated duplicate generated_12D630 recipe warning.
The first private guest fixture mistakenly extracted 49 words inherited from
the preceding target. Correcting it to the complete 54-word image fixed the
fixture errors without changing the candidate C; the failed receipt is retained.
A predecessor receipt path typo was corrected after the sealed native adoption;
all 16,421 inputs and four permitted live overrides were reverified before recount.

Production reproduces the independent entire-image prediction: exactly 164
changed bytes, 163 code bytes and one target symbol-size byte (12 -> 216),
with zero exclusions. All 6,056 function addresses and 6,055 other bodies stay
fixed. The eight other owner functions, their relocations and constant pools,
all 720 protected Game owners / 189,088 bytes, ELF geometry, named definitions,
guard manifest, Makefile, shared headers and C inventory remain preserved.
The qualification seal covers 16,421 paths and 390 focused inputs.

| Artifact | SHA-256 |
| --- | --- |
| Raw C and original relocatable body | a6f62de46073312759970f68fa2893c72ebb5b7a5ea86d1f52f11a9b14fa05cb |
| Linked retail slot | 030e27791e4ea9996960b35551649a686c21ae91694a965b3f49f562a27c379b |
| Adopted owner object | dc7076e39b946a849a331ba6b53e175849e22005378f6e9e6fea8392475a8f27 |
| Adopted ELF | 36c7270576043a5ffee067c028d12be0aaab7380aa381e59d5bd69c02ae6954f |
| Unchanged guard manifest | 91cfc61697b2f874f74475c5dadac1faec1f2e3c4f2a515d593b62d15b71ba03 |

## Bank and measured progress

Predecessor consumer: 646f2286a8f8d657f757f3407a8a39c373d73479.
Tools committed first: 6b3823566689e7d05f54a92ce5533c1d9ce9b98b.
The consumer commit records the source, tools pin and measured documentation.
Preserve 1,808 inherited dirty paths in the older tools mirror plus three new
qualification files. No push or mirror commit. Routine Claude calls: zero.

| Section | Byte-exact C | Address drift | Different |
| --- | --- | --- | --- |
| Total | 3,867 / 5,506 (70.23%) | 0 | 1,639 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 3,194 / 4,833 (66.09%) | 0 | 1,639 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

263 more exact functions are needed to reach 4,130 / 75%. Remaining shapes:
1,510 placeholders, 120 semantic/other and nine unlocated. Only func_15183ACC
receives new credit. Next inspect the 55-word func_151839F0 in the same owner.
Keep func_1514E920 parked and uncredited.

Evidence lives in conker/build/game-record-initializer-match/: complete-owner
preparation, fresh canonical and installed receipts, sealed production/adoption,
actual ELF recount and canonical function views. The final handoff records the
consumer commit, scoped AST refresh and closing preservation audit. Root README
receives aggregate rows only; detailed recovery history remains in this note.
