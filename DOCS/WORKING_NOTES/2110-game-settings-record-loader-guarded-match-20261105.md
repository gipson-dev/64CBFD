# Settings read, checksum and retained-byte protocol recovered

Date: 2026-11-05. Target `func_15007440`, owner `game_33990`.
Source `conker/src/game_33990.c`; original
`conker/asm/nonmatchings/game_33990/func_15007440.s`.

## Result and settings protocol

The complete **70 words / 280 bytes**, frame **0x18**, match at
VA `0x15007440..0x15007558`, ROM `0x348F0..0x34A08`.
This is semantic C with **46 expected-word/relocation layout guards** and
a target-only O2/g3/no-unroll profile. Twenty-four words remain unchanged.
There are **21 raw and 25 retail bindings**; all **seventeen normal-compact
and padded neighbors** remain identical.

The recovered interface is `void func_15007440(void)`:

1. Call `func_151DD3A0(&D_800BE900,0,D_800BE358,32)`, ignoring its result.
   The provider can update the live settings as well as delivering its packet.
2. Starting from 0xCC, add each unsigned payload byte 2..29 shifted left by
   `index & 3`, narrowing to sixteen bits after every addition. The payload
   alias `D_800BE35A` is the scratch base plus two. Compare the result with
   the big-endian halfword at the scratch base. Bytes 30/31 are retained.
3. Capture the **live signed byte at settings offset 16**, after the read and
   checksum. On mismatch fill all 28 settings bytes with 255. On a match copy
   the 28 payload bytes. Each copy group reads all four source bytes before
   writing any destination byte, preserving overlap behavior.
4. Restore the captured byte on either outcome, before calling
   `func_151DD9E4()` and then `func_151E7EF8()`.
5. Set byte `D_8008FE30` to one after both helpers. Their effects on other
   fields remain visible; the caller does not restore the snapshot again.

The saved byte has no invented field meaning. Its s8 type recovers the
original LB, while its eventual SB preserves all 256 byte patterns. The
original routine leaves the final helper's V0 lifetime unconstrained; a
zero-return interface is not retained.

The existing `func_151DD9E4` C body remains a separate placeholder. Its
old-style s32 declaration reflects that current boundary without inventing
a new prototype/body. `func_151E7EF8(void)` agrees with its established
void declaration in generated_20AE20. The new completion flag is a byte.

## Compiler layout and isolated profile

The natural initial draft emitted 77 words: IDO unrolled the checksum and
kept the transfer loops scalar. The selected source makes the four-byte
snapshots explicit and uses the no-unroll compiler option to retain the
scalar checksum. Both transfer loops use their original equality end test.

The 46 guarded words account for checksum/index register roles, address
hoisting and rematerialization, the fill-loop cursor/end allocation, the
copy-loop snapshot registers and branch-delay scheduling, and the final
completion register. Every expected opcode and relocation is pinned.
All replacements are fixed in the tool, checked against the full original
body and bindings, and applied as exactly 46 appended rows. There are no
insert/omit rows or placeholder-generated instruction bodies.

The Makefile excludes only this owner from the generic plain-object recipe
and compiles normal and no-unroll objects. The root-owner padder selects
**only func_15007440** from the alternate object. All other functions use
their established normal object. The existing `jtbl_80095A00_game` anchor
continues to serve the earlier save-default initializer.

Normal-owner allocatable pools, including register information, and every
padded pool remain unchanged. The selected alternate function references
no private pool; the alternate object's other functions are not adopted.
No header, original assembly, compiler executable or sibling project changes.

## Original caller and integrity helper

A full aligned ROM census finds one JAL, ROM `0x49B84` /
VA `0x1501C6D4`, and no tail jump or aligned address literal. The original
ten-word dispatch window follows the call and its branch, reloads
`D_800BE3F0`, and clears `D_80082BB4`. It stops before the enclosing BEQL /
frame cleanup at `0x1501C6FC`. Its other case's two words are skipped.
The return is unused. The complete parent is not qualified.

The generated caller's C body is still a placeholder and contains no C call
to repair. Its source and complete production object remain unchanged, as
does the generated_20AE20 helper owner.

The test also executes all **26 original words** of `func_151E7EF8`. After
the opaque `func_151E7E9C` call, it sums the **2,996 original code bytes**
from `0x151DDC20..0x151DE7D4`, compares with `0xBFC924E3`, and either keeps
or clears the mapped `osSpTaskLoad` word at `0x10003330`. Original code and
a deliberately changed input exercise both outcomes.

That span is a separately mapped retail-code fixture. It does not certify
the incomplete project's currently loaded code span or gameplay. EEPROM
reading, `func_151DD9E4`, and the integrity helper's own first callee remain
effectful opaque ABI providers. Their implementations are not adopted here.

## Fresh qualification and native-row reuse

All **seven pre-install checks pass in 257.147 seconds**; all **seven
installed checks pass in 141.702 seconds**.
Rerun with `python3 -m unittest tools.tests.test_game_settings_record_load_match -v`.

* **768 guest cases per body** cover original, natural no-unroll C,
  normalized compact C and padded C. All 70 original and natural-C words
  execute. Ordered public-memory traces, three calls, call-boundary snapshots
  and all final data agree. Corrected bodies have complete private-state
  equality. Raw caller-save allocation differs; its preserved ABI is checked.
* **29 alias cases** include destination/source overlap in both directions
  and the completion flag inside either buffer, including natural C.
  **242 fired access-prefix cuts** and three sparse destination faults preserve
  the corrected complete state. An effective early-store instruction control
  proves the four-read snapshot matters under overlap. Invalid-access
  evidence is limited to the guest model, with no portable-C/MMU claim.
* **32 cases per body** execute the original integrity helper, both checksum
  outcomes and both stack phases. **Eight caller cases per body** execute
  the original dispatch window with a zero/nonzero post-call gate.
* **Twelve independent GNU links** across three layouts check all 21 raw /
  25 retail bindings and the +16 LO16 addend across HI/LO carry boundaries.
  **77 cases per body** also cover positive group lengths 4,8,12,16,28,32,64.
  The physical settings payload remains 28 bytes.
* Native32 O0/O2/O3 pass **12,288 executions per suite**, 4,096 bounded fixtures per
  profile, with UBSan and a volatile void-function pointer. Inputs cover every
  saved byte, checksum match/mismatch, reader changes and helper effects.
  The halfword header is adapted numerically for native byte order; all other
  scratch bytes, settings/canaries, call snapshots, markers and the final
  flag are checked. Overlap remains separate guest evidence.
* **Sixteen native and sixteen separately compiled IDO controls** have
  witnesses: seed/weight/bounds, read channel/length, default-fill and branch
  selection, copy offset/length, wrong or late restoration, missing/reordered
  helpers, and missing/early completion flag. The rebinder preserves actual
  HI/LO addends; independent GNU results verify it.
* **280 raw-byte, 21 binding, eight guard-field and five literal-image
  corruptions** fail closed. The old zero-return stub fails its three-call
  protocol. All inherited guard bytes remain an exact prefix.

Native reference rows are now cached once per immutable fixture tuple.
All **nineteen generated C programs** are byte-identical to the uncached
pre-install versions; their SHA-256 identities are retained in
`native-cache-identity.json`. The audit records 4,096 rows, eighteen cache
hits and 1.666 seconds for generation/comparison. No native execution,
optimization profile or negative control is removed.

Nineteen shared matcher/padder/relocation/data checks pass in
11.350 seconds; `make tools-check` passes. The sibling
tools copy's twelve supported standalone checks and smoke test pass in
16.080 seconds.
The target suite is fresh in the mounted consumer layout. Neighbor suites
are reused through unchanged complete code/binding/pool evidence.
Routine Claude calls: zero.

## Literal production image and inputs

The immutable snapshot contains **108 files**, including all headers,
source/objects, original target/caller/helper assembly and ROM, manifests,
linker, Makefile, ELF, binary, progress and graph. Artifacts remain under
`conker/build/game-settings-record-load-15007440-match/`.
Consumer baseline is `921b46676de23e2156ae902e7c8a6585c25d01f1`;
mounted tools baseline is `6bed449c25d26ce1ac90577ac99ae7b1d39c64c2`.
Existing sibling dirty work, private inputs, saves and frozen host-port
Release remain untouched.

Actual Make equals the independently assembled owner and **entire ELF**
byte for byte. The literal prediction accounts for **240 changed bytes**,
only in the target slot and its size update from 12 to 280. There are no
metadata permutations or excluded bytes. All **6,052 function addresses**
remain fixed; all **189,088 protected data bytes across 720 owners** are exact.
Both complete caller/helper production objects remain byte-identical.

| Artifact | SHA-256 |
| --- | --- |
| Natural target | `a85a19a8cd877a8610630df46f9c96f7b0d3814df993187d7286af399bff430c` |
| Original target | `736e27ae8db3f7f1fa4a7f8bba6c14de36bb5494a50be1973762d9873b621282` |
| Production owner | `62e5950ce8011358e84942df9de14ba4698a6cfb32527eabb2a3324e426c4db5` |
| Complete ELF | `ab6262907a6a478b78e45d878bdb1a9fa32fdb951a7815face207408d7fd0697` |
| Code binary | `aa5f969618442abe5e208148939905483724c3f4c94e100586b23402631bc73e` |
| Extended guard manifest | `27673a32272270e3dc8bf10de90f57e5273beb43ec26516e5d449e7e60de990a` |

The production rebuild/recount takes **500.241 seconds**.
`make -C conker all` produces the binary and returns 2 only at the expected
incomplete-project retail checksum mismatch. The inherited generated_12D630
duplicate recipe warnings remain; the broad build is not warning-free.
The entire progress CSV is byte-identical. Existing source/Makefile newline
styles remain intact. Root README changes aggregate rows only.

## Progress and continuation

| Section | Byte-exact / converted | Match | Drift | Different |
| --- | --- | --- | --- | --- |
| Total | 4,181 / 5,512 | 75.85% | 0 | 1,331 |
| Init | 492 / 492 | 100.00% | 0 | 0 |
| Game | 3,508 / 4,839 | 72.49% | 0 | 1,331 |
| Debugger | 181 / 181 | 100.00% | 0 | 0 |

Converted inventory remains 5,512/6,046. The 80% threshold is 4,410,
leaving **229 more** exact functions. The live nonexact list selects
**func_1503B840** next, 71 words with 67 current differences. Its original
body and caller/interface still need qualification; it receives no credit.

Retain the eight separate boundaries from Note 2103: func_150A76F0,
func_151F8870, func_150A613C, func_150AE280, func_15115F68,
func_151AE2BC, func_150A6760 and func_150A70C0. Keep the wider 80% goal active.

The next owner is `conker/src/game/generated_68C70.c`, with the original
`conker/asm/68C70.s`, ROM `0x68CF0..0x68E0C`, frame zero. The complete
original routine gates on type one, compares ordered halfword IDs and ORs
bits into byte +0x2FB. A disposable first draft under this checkpoint's
`next-private/` compiles without diagnostics but emits 87 words against
retail's 71. Its interface, tables, callers and execution remain unqualified;
it is uninstalled and uncredited.

Mounted tools are committed first as
`f6749eb211c5b2789ab03756c8ee7566d2a194ab`
(`test(game): qualify settings loader and cache native fixtures`).
The consumer records that exact pointer with the semantic C, target-specific
profile, guards and documentation. These are local commits; no push is made.

The ordinary Graphify update refuses its smaller 25,006-node replacement,
leaving the previous graph byte-identical. The following refresh is scoped to
the nine changed consumer paths. The 31,816 nodes from 3,754 files outside
the current scan corpus are retained; this is not a fresh full extraction.

The scoped refresh retains 58,807 old IDs, relocates three update-log IDs
through unique same-label/same-source replacements and adds eleven IDs.
No nodes outside the changed paths are lost. The result is **58,818 nodes /
112,585 links / 5,230 communities**, SHA-256
`30546d0c08899dace51b6d39943fc312a1918b1cd84f80c5d7a7ff62cb3694b5`.
The target node is refreshed to L157. Its old s32 return-type reference
remains, and the cross-file helper-call edges are absent. Those are scoped
graph limitations; source, caller/ABI evidence and emitted code remain
authoritative. No graph package/policy change or hand-added edge is made.
The receipt is followed by a no-topology-change refresh and stable-hash check.

The final production audit verifies all production hashes, the exact guard
extension and target profile, all 108 frozen inputs, unchanged progress,
the complete caller/helper objects and all nineteen native-source hashes.
The source recovery remains separate from host-port gameplay acceptance.
