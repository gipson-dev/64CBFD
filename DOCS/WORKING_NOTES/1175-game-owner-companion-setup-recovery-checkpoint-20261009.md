# Game Owner Companion Setup Recovery Checkpoint

Continue from [Note 1174](1174-game-owner-link-setup-guarded-c-match-20261009.md).
Start clean at parent09ea9e85/toolsf3bb1e7. One Codex writer, zero Claude
calls; follow the scoped [agent workflow](../AGENT_WORKFLOW.md) and use complete
semantic candidates, existing compiler/oracle/padder helpers and bounded
independent qualification. Keep tools committed before the consumer pin.
No push; preserve the independent older tools checkout and all host state.

## Result And Acceptance Boundary

Recover complete **func_151B2690**, VA151B2690..151B2950,
ROM1DFB40..1DFE00,176 words/704 bytes, original frame0xD8.
It builds two48-byte link packets followed by one40-byte kind-0x13 effect packet.
The [complete C driver](../../tools/experiments/game_owner_companion_setup_candidates.py)
and [nine-test suite](../../tools/tests/test_game_owner_companion_setup_recovery.py)
are committed, but this is a **recovery checkpoint, not a new C match**.

The selected C body has176 words/frame216, correct private stack locations and
122 real instruction differences. Every persisted candidate is explicitly
rejected for byte-exact installation. Keep its genuine
[GLOBAL_ASM](../../conker/src/game/generated_1DF510.c),
[scoped fragment](../../conker/asm/nonmatchings/generated_1DF510/func_151B2690.s)
and [full owner assembly](../../conker/asm/1DF510.s) installed/intact.
No source, guards, profile, protected data or conversion-row changes.
The root README is deliberately unchanged: its aggregate numbers remain correct.

## Recovered Packet And Lifetime Contract

Offsets in this contract are hexadecimal; lengths, durations and argument
values are decimal unless explicitly prefixed with0x.

Capture one endpoint pointer from actor+28 before any helper. Reuse that identity
even when allocation hooks clear actor+28. The48-byte link packet uses the
existing20-byte endpoint layouts, actor at28 and route at2C.
Both endpoint owner fields use the captured endpoint. Read both code bytes at
endpoint+3B before the first allocation; first kind5/second kind2.

First link: route1, vectorsD_800AA320/368. Request flags0/duration100,
start and end from endpoint coordinates14/18/1C, active1/enabled1/extra1,
width5/kind3/distance180, limitsD_800AA388/38C and tail0.
Call the real mixed ABI:
func_151B30B0(&request,0.0015f,48,255,0).
After this call, read the original incoming actor home and derive pair=actor+28.
Unconditionally store its result, including NULL, at pair+14 (actor3C).
On success, copy48 bytes to result+150.

Second link: route0, vectorsD_800AA32C/374 and repeated extra1 store.
**Do not reread the endpoint codes, coordinates or limits.**
Reuse the first packet's code/kind/owner fields and the first request's fields,
even when helpers mutate endpoint bytes/coordinates, actor pointers or globals.
Call the same wrapper; store unconditionally at pair+10 (actor38), then
conditionally copy48 bytes to result+150.

Finally build the distinct40-byte effect packet: endpoint pointer0/code4/kind5,
two untouched holes6/7, vectorD_800AA368 at8, vectorD_800AA374 at14,
width5 at20 and original actor pointer at24.
**Read endpoint+3B again here**, after both link operations and their stores.
This matters when the endpoint aliases actor: actor38's pointer store can itself
change the byte at actor3B before the effect captures it.

Call the existing nine-argument factory:
func_15149130(300,-1,-1,0,0,19,40,255,1).
O32 outgoing stack words10/14/18/1C/20 carry0/19/40/255/1.
Store its result unconditionally at pair+1C (actor44).
On success, copy40 bytes to result+28. Helper/SDK results must not replace the
retained pair/endpoint identities. The allocation/factory hooks may change
scratch GPRs, FP registers, outgoing homes and public memory.

## Shape Evidence

Persist53 complete candidate forms/56 profile rows: selected in four profiles,
48 real declaration-order/workspace-position/copy-source forms, plain and
volatile actor forms, separate locals and request-first locals.
Selected profiles (words/frame/differences):
O2/g3 176/216/122, O2 175/216/150, O1/g3 204/208/202, O1 204/208/202.
All isolated compilations have zero diagnostics and no literal pools.
No production profile or shared-header change.

Selected grouped workspace uses effectSP40/link packetSP68/requestSP98;
savedS0/S1/RA are2C/30/34 and the incoming actor home isD8.
The raw C prologue stores/loads the incoming home early. Retail initially keeps
actor inS1 and stores that incoming home immediately before the first call.
The raw prefix has one extra instruction, closed by its absent late home store.
Register allocation then rotates many scratch operands. Its relocation offsets
shift+4 only before118; all22 relocation type/symbol uses remain correct.
This is not grounds to normalize122 unexplained words.

Ignored additional fitting families keep14 initial self/home forms,10 lifetime/
parameter/size forms,12 initial-pair/capture forms,20 home-cast/placement forms
and six parameter-type forms. These exploratory rows are not additional persisted
catalog coverage or qualified alternatives.

The ignored fitting/third-5.c probe uses a volatile actor and initially captured
pair. It is176/frame216/**69 differences**, with all105 words from11C to2C0
already byte-exact. Its early store/load and opening scheduling still differ.
The69 changed prefix words are not a certified closed GPR permutation.
Do not install this probe or replace its prefix with literal retail words.

## Qualification

Final **nine-test suite passes61.269s, zero skips**:

- All56 persisted complete profile rows compile; none matches retail.
  Selected length/frame/differences and original assembly status are asserted.
- 384 guest cases/768 executions: three memory seeds, endpoint distinct/actor
  aliases, eight success masks, mutations, two stack phases, and distinct or
  actor/endpoint-aliased result pointers. All176 retail words reached.
  Original and selected C have identical complete guest memory and logical calls,
  including seven copied link-packet holes and two copied effect-packet holes.
  **Access traces are not identical or claimed.**
- 16,384 native32 executions of the actual selected body: all256 code bytes,
  endpoint aliases, mutations, eight masks and result aliases. Independently
  check retained coordinates/codes/limits, refreshed vectors, final late code,
  typed wrapper/factory calls, conditional copies and canaries.
  Compile-time endpoint20/link48/request56/effect40 layouts and actor offset36
  are checked. Native32 qualifies defined fields, not native padding parity.
- Six compiled effective negatives: wrong duration, second-link code recapture,
  second-link coordinate recapture, wrong factory mode, omitted failed store and
  short effect copy. Each completes and fails independent public memory/call
  expectations, not an arbitrary oracle assertion.
- Four original/candidate symbol sets/eight independent links,64 cases/
  128 executions, segment and low-half carry boundaries. Complete memory agrees.
  Preserve all22 relocation uses while accounting for the measured prefix shift;
  this is semantic rebase proof, not byte-matching proof.
- Copied actual owner with real asmprocessor/padder preserves all17 neighbors,
  pools and relative relocations. Four old Warning712 messages are unchanged;
  zero new target diagnostics. Scratch padder acceptance does not authorize an
  incorrect byte-match installation.
- 64 connected cases/128 executions with actual original53-word151B30B0 code.
  Both links reach the common allocator with(0x33,0,0x180,1,255,1).
  Independently check complete request/derived/public fields and raw copied holes.
  The installed wrapper is separately verified equal to those53 original words.
  Common allocator, kind-0x13 factory and SDK calls remain bounded.
- 12 missing-byte cases/24 executions: identical public-memory/logical-call
  prefixes. No private-stack/access-trace or hardware-fault equivalence claim.
- Original fragment/installed176-word slot match retail; production source,
  complete ELF, guard manifest and conversion CSV hashes remain unchanged.
  Protected Game data189,088 bytes/720 owners remains exact.

The initial47.988s run catches two local fixture mistakes: absent native runner
temporary directory and an exact-relative-offset relocation assertion despite
the known nonmatching prefix. Add the directory and check the actual measured
prefix relocation shift; do not weaken matching rejection or change shared helpers.

## Checkpoint And Next Step

Toolsfc54d7f98fcc293af26ae73718f8b6829c4769ce commits exactly the new driver and
suite first; parent docs pin it next. Mounted make tools-check and older standalone
check_project_tools.py pass. Preserve all102 initial older status entries,
HEADddbdd16 and both tracked dirty hashes; mirror only the two absent authored
files there, yielding104 entries. No older checkout commit/reset/push.

Fresh make build/conker.us.elf progress.csv reports both targets up to date.
Fresh match-progress NON_MATCHING=1 confirms unchanged:
Game2,739/4,815 exact,total3,412/5,488,zero drift/2,076 differences.
Converted5,488/6,042 (90.83%),85.95% bytes; Game4,815/5,321 (90.49%),85.30%.
No new matching or conversion credit. Older matching receipts are not presented
as freshly rerun tests; the immutable production hashes establish that boundary.

Validation passes69 AST/exact-mirror pairs and161 documents/4,431 relative
links, zero broken links. A scoped graph query finds no function node for
this GLOBAL_ASM target. Manual Graphify update exits1, refusing17,180 nodes over
retained38,965 and preserving19,398 excluded-but-existing nodes from2,972 files.
Existing version/devcontainer warnings persist; no force/reinstall/purge.
Wait for the separate parent post-commit hook before close-out; graph receipts
are operational, not semantic or matching proof.

Ignored conker/build/game-owner-companion-setup-test holds shape/guest/native/
negative/rebase/owner/connected/fault/unchanged and installed-wrapper receipts.
Driver56 rows are in conker/build/game-owner-companion-setup/measurements.json;
ignored fitting/measurements families retain complete exploratory sources/objects.

Source SHA256: 59723ec2982df10861f966a65c4ab016fd7eb04d2d039215f9522a55423c0044.
ELF SHA256: 873bf0f5b6f335c423f8d577cf0e330bf522bfaf04017bffd57ec5d2b6388dde.
Guards SHA256: 8bb14ba149088e62c3b53db93c55030fb36b42b5cfca854e4e600ea0ac2c25d1.
Progress SHA256: 527e0b54688fcf73187476ace7a8d3566de5ebc0329c11b41a36b5343708594c.

Resume **the same func_151B2690 fitting**, not another easier function.
Resolve actor's initialS1 retention versus delayed incoming-home store while
preserving all private packet addresses, endpoint capture/reuse and pair lifetime.
Use the qualified selected body as the semantic reference and the unqualified
69-difference probe only as a narrow scheduling clue. Qualify any new matching
form before installation, then rebuild/audit the linked ELF and fresh totals.
Full caller/factory/resource/SDK/hardware/gameplay and renderer remain open.
The Game goal stays active. No OGL/Release/save/editor changes.
