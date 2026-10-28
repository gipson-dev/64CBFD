# Adjacent record load - direct C match

Verified 2026-10-28. Restore func_151838B0 in generated_1B0740:
VA 0x151838B0..0x15183974, ROM 0x1B0D60..0x1B0E24, 49 words / 196 bytes.
The normal O2/g3 profile emits all original words directly with a 40-byte
frame, six relocations and no word guards. Keep the retail function name.

## Recovered behavior and interface

The interface is void func_151838B0(s32 index). D_800DDE80 is the existing
eleven-entry array of Record15183974, each containing five signed words.
If the current record is empty, call func_15183ACC(index). Reload the next
record afterward; the initializer may have changed it. If it remains empty,
call the asset loader with NULL size output, count zero, NULL relocation
output, depth two and path components 9 and index+0xAE.

On a non-null result, store its address in the next record, copy returned
words zero and two, copy the current record's word three, clear the next
record's last word and set D_800DDF69[index] to one. Allocation failure leaves
the provider's own mutations intact. Copies must preserve access order when
the returned block overlaps either table row.

Use the provider's existing recovered interface from game_57FA0.c:281:
void *func_1502B6BC(s32 *size, s32 count, s32 *relocated, s32 depth, ...).
The two path components are actual variadic arguments. No shared declaration
or compiler profile is changed. The initializer's current placeholder is
preserved and receives no matching credit.

Direct table indexing recovers the original 40-byte frame. The initial
explicit record-pointer local created a 48-byte frame and ten stack-offset
differences. Register hints and block-local placement did not fix it.
The final C keeps one result pointer; IDO computes and spills the row address
itself. RA is at SP+0x1C, the row spill at +0x20 and the index home at +0x28.
All eight other owner functions, relocations and constant pools are preserved.

## Original callers and helper boundaries

The aligned ROM census finds one direct call at ROM 0x1B08AC / VA 0x151833FC
inside the 392-word func_15183290, and no target pointer literal. The delay
slot passes index zero. 96 cases execute all 37 words of the original window
0x151833FC..0x15183490, including the following eighteen-argument consumer
call. The consumer is a bounded service. Other dispatcher routes are not
claimed; its C placeholder remains uncredited.

128 connected cases execute every instruction of the original 54-word
func_15183ACC. It loads the current row if needed, publishes its resource,
calls func_1510CE60 and sets the current-row flag. Returned-block aliases and
mutations are included. The allocator and resource services are bounded.

A further 144 cases connect the original 77-word func_1502B6BC as well.
They execute all 73 instructions reachable through this target's depth-two,
NULL-size-output, NULL-relocation-output interface, including missing path
components, null allocation and post-allocation zero size. Unvisited words
are 0x1502B6F0, 0x1502B7BC, 0x1502B7C0 and 0x1502B7C4: the non-null optional
output branches and an unreachable instruction. This is not full-interface
coverage of the loader. Its already exact source, object and linked body
remain unchanged, with no duplicate credit. Deeper boundaries are explicit:
func_1502AC88, func_1502B350, func_1502B4A8, func_1510CE60 and func_15175390.

## Qualification and production

Both tools copies pass eight fresh canonical methods and shared tools checks.
Each then passes two fresh installed checks; six unchanged semantic methods
are reused only with identical input, module and artifact fingerprints.

- 10,272 guest cases visit every target word and compare full machine state,
  memory, calls and access traces across retail, raw C and padded C. They
  cover valid adjacent rows, six returned-table aliases, both stack phases,
  initialization/loading mutations and sparse extreme guest indices.
- Native32 O0/O2/O3 each pass 16,384 cases with trapping UBSan, real variadic
  arguments, all ten valid adjacent-row indices, six legal table aliases and
  sixteen effective controls. Native tests do not claim out-of-array indices.
- Sixteen IDO-compiled semantic negatives independently fail as expected,
  including stale next-row tests, changed loader arguments, copy order,
  omitted initialization and incorrect field/flag updates.
- 65 fault-prefix triples and 424 connected-provider prefix pairs preserve
  the emitted instruction state and access order. These qualify guest fault
  behavior, not portable C faults.
- Three GNU layouts pass 72 cases, including HI16/LO16 carry boundaries.
  Three raw/binding corruptions and seven full-image corruptions are rejected.

The actual three-command Make recipe and generated padder reproduce the
qualified object. Selected, owner and recipe compiler diagnostics are empty.
The full build retains the unrelated duplicate generated_12D630 recipe warning.
The first private integration fixture lacked backing bytes for the initializer's
larger block reads when a returned pointer aliased the next row. Extending
that guest backing region fixed the fixture; production C was unchanged.

The qualification seal covers 16,414 paths and 387 focused inputs. Production
reproduces an independent entire-image prediction: exactly 149 changed bytes,
148 code bytes and one symbol-size byte (12 -> 196), zero exclusions. All
6,056 function addresses and 6,055 other linked bodies are unchanged. All
720 protected Game owners / 189,088 bytes, ELF geometry, named definitions,
guard manifest, shared headers, Makefile and conversion inventory are preserved.
No guard is added or removed.

| Artifact | SHA-256 |
| --- | --- |
| Raw C and original relocatable body | d08b875c488e42d9a4f3fee075cd8286c63649f530091ca8b1c8b85b18d9cd72 |
| Linked retail slot | eaa8b96397b1df970cbd5dac27abe6d14cf5afc58ba8967ad12105cf51876823 |
| Adopted owner object | 87d668ef426c75c827d6d8b103c285a79adf8caadad15d7e3f98ad0118d527fb |
| Adopted ELF | 16a6cb0868ea9ba387f9039374021609fa5450fdc9cf1470f0b6b6a6a7f8a93c |
| Unchanged guard manifest | 91cfc61697b2f874f74475c5dadac1faec1f2e3c4f2a515d593b62d15b71ba03 |

## Bank and measured progress

Predecessor consumer: 4b7330676ae8e2f9dc74548f70426778ac26ef58.
Tools committed first: 5d587696bf8f707575365ac847e00cbad7d415da.
The consumer commit records the source, tools pin and measured documentation.
Preserve all 1,805 inherited older-mirror dirty paths and the three new modules.
No push, mirror reset or mirror commit is performed. Routine Claude calls: zero.
No gameplay acceptance is claimed.

| Section | Byte-exact C | Address drift | Different |
| --- | --- | --- | --- |
| Total | 3,866 / 5,506 (70.21%) | 0 | 1,640 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 3,193 / 4,833 (66.07%) | 0 | 1,640 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

264 more exact functions are needed to reach 4,130 / 75%. Remaining source
shapes: 1,511 placeholders, 120 semantic/other and nine unlocated. Only
func_151838B0 receives new credit. Next inspect its initializer func_15183ACC,
using the now-qualified calling context. Keep func_1514E920 parked and uncredited.

Evidence lives under conker/build/game-adjacent-record-load-match/: preparation,
canonical and installed receipts, sealed production/adoption proofs, actual
ELF recount and canonical function views. The final handoff records the
consumer commit, scoped AST refresh and closing audit. Root README receives
only aggregate status rows; detailed recovery history remains here.
