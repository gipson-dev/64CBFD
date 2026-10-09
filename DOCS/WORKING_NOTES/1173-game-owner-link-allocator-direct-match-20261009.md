# Game Owner Link Allocator Direct Match

Continue from [Note 1172](1172-game-owner-link-setup-recovery-checkpoint-20261009.md).
Start clean at parent65425349/toolsb7cdf231. One Codex writer, zero Claude calls;
use the scoped [agent workflow](../AGENT_WORKFLOW.md), local complete bodies and
bounded independent evidence. Keep tools committed before the consumer pin.
No push; preserve the independent older tools checkout and all host state.

## Installed Result

**func_151B30B0 directly matches all53 retail words** under existing O2/g3:
VA151B30B0..151B3184, ROM1E0560..1E0634,212 bytes/frame0x28.
Replace the false12-byte zero-return C placeholder with its complete pointer-
returning body in [generated_1E0560.c](../../conker/src/game/generated_1E0560.c).
No guards, new literal pools, shared headers or compiler-profile edits.
Original [allocator owner assembly](../../conker/asm/1E0560.s) remains intact.

The complete [driver](../../tools/experiments/game_owner_link_allocator_candidates.py)
screens11 forms/four profiles,44 rows. Selected O2/g3 is53/frame40/zero
differences; O2 is52/40/50, O1/g3 is63/48/53, O1 is63/48/57.
Moving the two real float locals before the pointer keeps53 words but frame48
and11 differences. Volatile forms are unnecessary; selected plain C is exact.

## Actual ABI And Body

The mixed five-argument interface is:
u8* (void* request,f32 parameter,s32 extraBytes,u8 slot,s32 context).
A0 carries request, A1 carries parameter bits, A2 size, A3 slot, context is
incoming stack word10. Store the four register arguments in their retail homes;
low-byte slot narrowing is deliberate. Outgoing common allocator call:
func_15167A68(0x33,context,extraBytes+0x150,1,slot,1).

AllocationNULL returnsNULL immediately, without request reads, memcpy or bzero.
For success, copy all56 request bytes to created+10, then read distance from
created+38: **request field28, not width field20**. OR created byte10 with0xE.
Compute scaled=distance*distance/D_800AA390; store scaled+scaled at138.
Store truncated distance*parameter*4096.0f at13C; zero16 bytes at140.
Return the retained original pointer, not memcpy's destination pointer.
Single-precision operation order and the multiply hazard nop are exact.

The common allocator/SDK calls may change memory and scratch registers.
Distance and flags are deliberately read after memcpy; parameter and created
retain their original lifetimes. Wrapper result lives in v1 with private
homeSP24 across memcpy/bzero; incoming f32 remains inSP2C. No new saved S regs.

## Qualification

[Eight-test suite](../../tools/tests/test_game_owner_link_allocator_match.py):

- Direct53-word match, frame/5 relocation uses/zero diagnostics/pools/guards,
  four complete selected profiles.
- 7,168 guest cases/14,336 executions: all256 slot bytes with high-bit words,
  seven signed-size boundaries, failure/success and both stack phases. Vary
  finite distance/parameter/divisor, three seeded memories and memory mutation.
  All53 retail words reached. NULL request is safe on allocation failure.
- Independent expected complete public memory/calls/return and identical
  original/candidate traces. Bounded hooks mutate request before copying and
  created fields after copying, overwrite outgoing argument homes, scratch
  GPRs/FP registers and return unrelated bzero scratch values.
- 774,144 native32 executions of the actual C body with typed allocator/SDK
  fixtures, all slot bytes, seven safe signed sizes,108 independently computed
  float triples, mutation/failure and full result canaries.
  Expected float words are generated independently in Python; SSE32 execution
  is not N64 hardware/FCSR proof.
- Copied production owner preserves all16 neighboring routines, pools and
  relative relocations; actual production padder accepts. Before/after
  diagnostics are both empty. Existing duplicate generated_12D630 Makefile
  recipe warnings remain unrelated.
- Five compiled effective negatives: wrong distance, short copy, reloaded copy
  result, small allocation and wrong multiplier. Each completes in the oracle
  domain and is rejected for public memory/call/return mismatch, not arbitrary
  assertion failure. Seed a finite word for the wrong-return-pointer read.
- Four independent original/candidate symbol sets/eight links/32 cases/
  64 executions, including segment and low-half carry boundaries. All original
  and C relocation uses agree.
- 128 actual setup-chain cases/256 executions: original210-word func_151B2348
  calls actual original53-word wrapper versus exact C53-word wrapper.
  Eight failure masks, four endpoint aliases, mutation on/off, both phases.
  Three real common-allocation calls receive(0x33,0,0x180,1,255,1).
  Check full56-byte requests, independent defined packet/public fields and
  original setup's copied raw stack holes. Common allocator/SDK remain bounded;
  the unmatched setup C candidate is not installed.

Finite float conversions are within s32 range; signed size additions are
within s32 range. NaN/infinity/out-of-range conversion, FCSR exception behavior,
allocator/resource/hardware/gameplay integration remain separate open gates.
Do not generalize these modeled semantics to undefined portable-C domains.

Initial eight-test run20.446s catches local oracle method-reuse error, not
production failure. Use explicit TriangleOracle dispatch in the composed
chain model. Pre-install suite then passes16.300s. Initial installed run
27.131s catches metadata-order assumptions, investigated below. Refined
installed suite passes16.886s; **final eight-test installed suite29.437s,
zero skips**, after strengthening effective-negative discrimination.

## Whole-ELF Audit And Progress

Only this212-byte target slot changes in loadable ELF data. Its symbol size
changes12 to212. GNU ld also reorders three symbol records after the newly used
D_800AA390 reference. All20,318 symbol meanings are unchanged except the
target size; ELF/section headers/table extents/string multiset are unchanged.
Verify complete symbol multisets after the intended size update, then permit
only symbol/string ordering. Compare every other byte of the ELF.
Do not claim raw ELF identity outside a single st_size word.

All11,510 guard rows and the entire progress CSV are byte-identical.
Protected Game data189,088 bytes/720 owners is exact, zero differences.
Fresh build/progress.csv and match-progress NON_MATCHING=1 pass:

| Section | Converted Functions | Converted Bytes | Byte-exact C | Drift | Different |
| --- | ---: | ---: | ---: | ---: | ---: |
| Total | 5,487/6,042 (90.81%) | 85.91% | 3,411/5,487 (62.17%) | 0 | 2,076 |
| Init | 492/539 (91.28%) | 92.53% | 492/492 (100%) | 0 | 0 |
| Game | 4,814/5,321 (90.47%) | 85.26% | 2,738/4,814 (56.88%) | 0 | 2,076 |
| Debugger | 181/182 (99.45%) | 99.19% | 181/181 (100%) | 0 | 0 |

Conversion totals are independently recomputed from fresh us CSV rows,
excluding repeated headers. The placeholder was already C-classified:
one new exact function, **not new conversion credit**.
Root README changes aggregate rows only; detailed updates remain in docs.
Previous whole-ELF recovery/state/constructor receipts are historical and
superseded by this installation; do not recapture their immutable baselines.

## Evidence And Next Work

Tools3b7e4c1690694a0c919f62cf5be00dda6d6d7453 is committed first with exactly
the driver and focused suite. Parent source/docs pin it next. Mounted
make tools-check and older standalone check_project_tools.py pass.
Preserve all98 older initial status entries, both dirty tracked hashes and
HEADddbdd16; only two absent authored files are mirrored, yielding100 entries.
No independent older checkout commit/reset/push.

Validation passes65 AST/exact-mirror pairs and159 documents/4,400 relative
links, zero broken links. Manual Graphify update exits1, refusing17,169 nodes
over retained38,945 while preserving19,398 excluded-but-existing nodes from
2,972 files. Existing version/devcontainer warnings persist; no force/reinstall/
purge. Wait for the separate parent post-commit hook before checkpoint close-out;
these graph operations are not function-matching proof.

Ignored conker/build/game-owner-link-allocator-test keeps immutable
before-source/ELF/guards/progress/baseline and shape/guest/native/owner/negative/
rebase/chain/audit/conversion receipts. Driver44 rows are in
conker/build/game-owner-link-allocator/measurements.json.
A prepared clone lacking immutable pre-install history explicitly skips that
audit rather than claiming installation proof.

Before source SHA256: 02e6c96f6db3261d355b63964da5b7dfe81dc5cf53a0d671743db8777d116b17.
Installed source SHA256: 0cc27c7073d28ef46127064b74ce1591512662f87bde060dd9a60fe37e91fd1f.
Before ELF SHA256: 7a42ef3e037f2d0665e3d35bf62e4be56d6586db75702bf5cef9dd84.
Installed ELF SHA256: 873bf0f5b6f335c423f8d577cf0e330bf522bfaf04017bffd57ec5d2b6388dde.
Protected data SHA256: 0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670.

Resume **func_151B2348**,210 words, now with a real exact allocator dependency.
Four typed actor/pair forms and15 alternate copy-return declarations did not
improve the previous stack/register shape; those ignored exploratory copies
are not added to the17-form persisted setup catalog. Screen real pointer-local
declaration order next while preserving second-before-first capture and
incoming actor-home lifetime. Retail retains pair inS2 and packetSP34/requestSP64.
Qualify complete raw packet provenance/native32/rebases/copied owner before
replacing its genuine assembly. func_151B2690 remains original176-word assembly.
Full renderer remains pending; Game goal stays active.
No OGL/Release/save/editor changes.
