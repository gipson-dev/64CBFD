# Save prefix and live-pointer record defaults recovered

Date: 2026-11-05. Target `func_15007168`, owner `game_33990`.
Source `conker/src/game_33990.c`; original
`conker/asm/nonmatchings/game_33990/func_15007168.s`.

## Result and recovered storage contract

The complete **69-word / 276-byte** leaf matches at VA
`0x15007168..0x1500727C`, ROM `0x34618..0x3472C`, with frame zero,
**eight bindings and two scheduling guards**. All **seventeen compact and
padded neighbors** remain identical. The interface is
`void func_15007168(void)`; the final V0 value is the loop index 10, not a
semantic return value.

The first do/while clears exactly **104 bytes** from `D_800BE2F0` to
`D_800BE358`. The source's existing 112-byte SaveBlock33990 view overlaps
the first eight bytes of the scratch object at this actual layout. Clearing
the nominal union size would overwrite retained bytes. Synthetic zero-length
end rebases still execute one store, preserving the original do/while.

The actual pointer word `D_80082BBC`, ROM `0x22767C`, is **0x800BE2F2**:
save base plus two. A local ten-byte record view names byte offsets without
inventing game-field meanings. For indices 0 through 9, the store protocol is:

1. Reload the global pointer and store +1 = 3, +3 = 2, +4 = 1, +2 = 10,
   with a separate reload before every store.
2. Store +5 = 3 for index 0; 5 for indices 1/2; 20 for index 7;
   20 followed by +2 = 0 for index 5; 3 for indices 8/9. Indices 3/4/6
   perform no +5 store.
3. Reload the pointer again and store +9 = 0. The record stride is ten.

Bytes +0, +6, +7, +8 and the omitted +5 cases retain their existing values
when the pointed-to records lie outside the cleared prefix. Pointer-object
aliases prove that caching the pointer changes observable behavior. The s8
view at +5 recovers the compiler's duplicate constant-three loads and retail
register roles; the byte stores alone do not establish later signed gameplay
interpretation of that field.

## Compiler schedule, pool and build profile

The natural C has the correct 69-word body. Only the first two independent
LUI operations are reversed. The two appended expected-word guards at +0/+4
swap V0/end and V1/start address loads, moving their HI16 relocations with
them. The unchanged LO16 uses at +8/+12 complete the same addresses.
Raw and original private state converge after these first two instructions,
before any memory access; padded and normalized compact words are exact.

The existing `jtbl_80095A00_game` has ten entries / 40 bytes at
VA `0x80095A00`, ROM `0x23A4C0`, targeting offsets
156,172,172,244,244,204,244,188,232,232 within this function.
The one target-specific Makefile rodata rule binds the compiler table to
that existing table. The compact table is exactly 48 bytes: forty relocated
bytes and eight alignment bytes, aligned to sixteen. Its ten R_MIPS_32
relocations and every target offset are pinned. It is not duplicated into
the loaded image. All other compact allocatable sections, including register
information, and every padded pool remain unchanged.

The root-owner padder is `tools.pad_c_object.emit_padded_assembly`.
Existing guards remain an exact prefix of the manifest; only two rows are
appended. No shared headers, compiler options or original assembly change.

## Caller and ABI evidence

An aligned full-ROM census finds exactly two JALs: ROM `0x347F8` /
VA `0x15007348` in `func_1500727C`, and ROM `0x49AF0` /
VA `0x1501C640` in `func_1501C57C`. There is no tail jump or aligned address
literal. The latter's current generated C is still a placeholder and contains
no C call to repair. Its source and complete production object remain
unchanged. The same-owner reader already uses the corrected void declaration.

The complete **57-word original checksum reader** calls the opaque
`func_151DD3A0(queue,0x44,save,112)` provider, computes the original checksum
over bytes 2..103 and calls the initializer only on mismatch. The provider
supplies varied packets and clobbers caller-save GPRs/FPRs, HI/LO and four
outgoing homes. Valid and invalid checksum cases execute both outcomes.

The other original **six-word selection window** compares selector A0 with
four, conditionally calls this leaf, then clears `D_80082BB4` on either path.
The window stops before its enclosing branch/frame teardown. The complete
selection parent and the opaque reader implementation are not qualified.

## Fresh checks

Seven pre-install checks pass in **61.321 seconds**; seven installed checks
pass in **71.724 seconds**. The suite is
`python3 -m unittest tools.tests.test_game_save_defaults_match -v`.

* **208 guest cases per body** compare original, natural compact,
  normalized compact and padded instructions, complete private state and
  every ordered data access against an independent byte-store reference.
  All 69 words execute. Six pointer placements, sixteen initial byte patterns,
  both stack phases and writes aliasing each of the four pointer bytes are
  included.
* **690 fired memory-access prefix cuts** and four sparse clear/pointer/
  table/final-record faults retain registers, RAM, traces and PC/delay state
  across all four bodies. These are guest instruction-model observations,
  not portable invalid-access or hardware-MMU claims.
* **32 cases per body** execute the full original checksum reader; **ten
  cases per body** execute the selection caller window. Original, natural
  compact and padded target bodies agree at both caller boundaries.
* **Nine independent GNU links**, three layouts and **97 cases per body**
  qualify all eight bindings, switch targets, HI/LO carries and clear lengths
  0,1,7,103,104,105,112. The first layout crosses 0x81007FFC.
* Native32 O0/O2/O3 pass **4,608 executions**, 1,536 bounded fixtures per
  profile, with UBSan and a volatile void-function pointer. The native arena
  represents the real 104-byte save/scratch overlap. A reference-derived FNV
  digest checks all 232 save/scratch and 400 separate payload bytes. Pointer
  object aliases remain separate guest evidence.
* **Fourteen separately compiled IDO controls** and **thirteen native
  controls** have fired witnesses: short/long clear, four wrong common fields,
  wrong switch constants, missing index-five reset, wrong final byte, unwanted
  retained-byte write, wrong record index and cached pointer. Cached pointer
  is guest-only. Each IDO control is GNU-linked with its actual relocation
  addends and its own compiled switch targets.
* **276 raw-byte, eight binding, four expected-word/relocation guard and
  five literal-image corruption controls** fail closed. The old zero-return
  placeholder is rejected by its missing writes.

Nineteen shared matcher/padder/relocation/protected-data checks pass in
**20.380 seconds**; `make tools-check` passes. The sibling
tools checkout's twelve supported standalone checks and smoke test pass in
34.799 seconds. The new target suite runs fresh in the mounted consumer
layout. Unchanged neighbor suites are reused through complete body, binding
and pool identity. Routine Claude calls: zero.

## Production image and preserved inputs

The immutable snapshot has **105 files**, including headers, source, owner/
caller objects, original assembly/ROM, manifests, Makefile, linker, ELF,
binary, progress and graph. Artifacts are under
`conker/build/game-save-defaults-15007168-match/`.
Consumer baseline: `37b2385353f77054bdc80b1ba03db13acead280f`.
Mounted tools baseline: `6ea23cff3be96f909de0fc369fd7c27c40840728`.
The sibling tools checkout's existing dirty work, private inputs, saves and
frozen host-port Release remain untouched.

The natural before/after root owners compile without diagnostics. The normal
Make rebuild agrees byte for byte with the independently assembled owner and
**entire ELF**. All **6,052 function addresses** stay fixed; only this target
body/extent changes. All **189,088 protected bytes across 720 data owners**
remain exact. The literal full-file prediction accounts for **206 changed
bytes**, entirely in the target slot and its size update from 12 to 276.
There are zero metadata permutations, zero excluded bytes and no unexplained
image differences.

| Artifact | SHA-256 |
| --- | --- |
| Natural target | `422469e5692b36a2a789d3cdc3755ca9d1b73bfe578ca365185b9bb9bbe36b83` |
| Original target | `78e4ccbc59d52731909318a8fbb8b5c18c592e021910e431d37bdb47eb94f354` |
| Production owner | `879965bd0265a30bc7de46d40937d647d6fe18d37897f8823d1b49cd4fb98fbe` |
| Complete ELF | `dfda98f2d79107f1c65b55b101831d491bf9530fcb15566fd4342b1c144592e6` |
| Code binary | `58f368e177b387f81c746e03e850d198f4c45a14e366d219132e0d2685d503cf` |
| Two-row-extended guard manifest | `015f773de9b6c97c9f3b12ee69cd3d20d758f8f3e9a7319ce93a23f2cfcf5466` |

The production rebuild/recount takes **422.092 seconds**.
`make -C conker all` produces the binary and returns 2 only at the expected
incomplete-project retail checksum mismatch. The inherited duplicate
generated_12D630 recipe warning remains; the broad build is not warning-free.
The entire progress CSV remains byte-identical, preserving conversion rows
and byte percentages. Existing source and Makefile newline styles are retained.

## Progress and continuation

| Section | Byte-exact / converted | Match | Drift | Different |
| --- | --- | --- | --- | --- |
| Total | 4,180 / 5,512 | 75.83% | 0 | 1,332 |
| Init | 492 / 492 | 100.00% | 0 | 0 |
| Game | 3,507 / 4,839 | 72.47% | 0 | 1,332 |
| Debugger | 181 / 181 | 100.00% | 0 | 0 |

Converted inventory remains 5,512/6,046. Root README changes aggregate rows
only. The 80% threshold is 4,410, leaving **230 more** exact functions.
The live nonexact list, Graphify navigation and complete original assembly
identify **func_15007440** next: seventy words, frame 24, owner game_33990,
ROM `0x348F0..0x34A08`. It reads a 32-byte block, validates its checksum,
fills or copies 28 bytes, restores a signed byte snapshot and calls two
post-load helpers. It remains a placeholder and receives no matching credit.

Retain the eight separate boundaries from Note 2103: func_150A76F0,
func_151F8870, func_150A613C, func_150AE280, func_15115F68,
func_151AE2BC, func_150A6760 and func_150A70C0. Keep the wider 80% goal active.

The first disposable `func_15007440` source screen is retained at
`conker/build/game-save-defaults-15007168-match/next-private/`.
It compiles without diagnostics but emits 77 words against retail's 70.
It has no caller, ABI, guest/native, padded-owner or whole-image qualification
and remains uninstalled and uncredited.

Mounted tools are committed first as
`6bed449c25d26ce1ac90577ac99ae7b1d39c64c2`
(`test(game): qualify save record defaults and pointer aliases`).
The consumer records that exact pointer with the C, rodata profile, two guards
and documentation. These are local commits; no push is performed.

The ordinary Graphify update refuses its smaller 25,006-node replacement.
The existing graph remains byte-identical at that boundary. The following
refresh is explicitly scoped to the nine changed consumer paths; the 31,816
nodes from 3,754 files outside the current scan corpus are preserved rather
than described as a fresh full extraction.

The scoped refresh retains 58,799 old IDs, relocates three update-log IDs
through unique same-label/same-source replacements and adds eleven IDs.
Zero nodes outside changed paths are lost. The result is **58,810 nodes /
112,578 links / 5,267 communities**, SHA-256
`e82ae6b207400782d5a6531efd4c290e12b747c18e90009c725881a50ee57ed0`.
The target node is refreshed to L83. A stale s32 return-type edge remains
from the earlier placeholder despite the recovered void definition. This is
a scoped-graph limitation; source, ABI and emitted instructions are the
authoritative evidence. No graph policy/package change or hand-added edge
is made. The final receipt is followed by a no-topology-change refresh and
stable-hash check.

The final production audit rechecks all four production hashes, the exact
two-row guard extension, table profile, unchanged progress CSV, all 105
frozen inputs and the complete external caller object. The tools and consumer
commits preserve the verified checkpoint while the wider goal remains active.
