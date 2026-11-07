# Resource view creator restored with qualified lifetime and schedule guards

Date: 2026-11-07. Continues [Note 2156](2156-game-fixed-descriptor-factory-match-20261107.md)
from consumer `99e6a02550731cc6264882e50702b90ba6ed3985` and tools
`71829fcb2939715ca39e0a4fae01869ee78d83f4`. This adds one qualified Game
function toward the active 80% total goal.

## Resource descriptor, allocation and live view initialization

`func_1513B5E0` in `conker/src/game_168A90.c` replaces its zero-return
placeholder with the complete **110-word / 440-byte** resource creator,
VA 0x1513B5E0..0x1513B798, ROM 0x168A90..0x168C48. Its recovered interface is
`s32 func_1513B5E0(EffectDescriptor1513BAE8 *descriptor, u8 mode,
s32 extraSize, u8 priority, s32 context)`. Retain address names for unproven
resource fields; semantic local names describe only the measured operations.

The resolver receives two 32-bit output pointers and resource identifiers
at descriptor+0x30/+0x34. Its actual definition is variadic; the allocator
takes four full-word arguments followed by two byte arguments. The tail
service's final argument is a nullable `s32 *`. These declarations were
checked against their current definitions, rather than guessed from calls.
The asset pointer is immediately dereferenced, as in retail.

Derive the buffer extent from asset[0]-asset-40. Capture the allocation's
total buffer size as twice that extent times the initial view count plus one.
Allocate with mode-dependent kind0x38/0x54, context, extraSize+total+248,
group2, priority and1. A null allocation returns zero. Copy all60 descriptor
bytes to created+0x10, including the incoming descriptor's seeded padding;
publish the asset pointer at created+0x4C. Resource data starts at asset+40.

Initialize two buffers per live view starting at created+248, publishing
their pointers through the +0x58/+0x68 arrays. The second copy reloads its
destination from the stored +0x68 slot after the first copy. Reload the
view count after descriptor copying and each pair of resource copies;
callbacks may change it. Keep the initial allocation total unchanged.
After all copies, read the live asset end, publish it at created+0x54,
publish the captured total at+0x50, submit the tail service and return the
created handle. The final end read precedes the total-size store.

Use explicit unsigned arithmetic for modulo32 products/count increments.
The initial count+1 guard is signed after the wrapped addition, preserving
the retail INT_MAX boundary. The source does not manufacture a volatile
access or extra helper to force compiler scheduling.

## Raw source and the closed normalization

The semantic O2/g3 source emits **105 words**, with the correct120-byte
frame and real resolver output homes SP+0x60/+0x5C. Asset and allocation
total remain at SP+0x70/+0x6C. All12 raw and padded neighboring functions,
including the previously banked69-word fixed factory, remain literal.
The four inherited pointer diagnostics remain; there are no new warnings.
The descriptor/payload typedefs move above the new typed declaration without
altering any neighboring instructions. No compiler profile changes occur.

Raw target SHA-256:
`d4ea35b6be8c0053516ecb9efaa5a5a235c65a9292d37dffab195a7df259a985`.
**42 expected-word/relocation guards** derive retail from this exact raw
body and eight exact bindings. The derivation does not read retail words.
It retains every one of the105 original instruction identities exactly once,
preserving the order of existing memory operations and service calls.

Two bounded live ranges use closed GPR cycles: the early stride/product
temporaries and the later row/cursor/loop temporaries. Independent address
and constant setup moves to retail's schedule. Six branches are rebased
by instruction identity, including the loop operation originally in the
initial guard's delay slot. No service, arithmetic operation or branch is
copied from an unrelated function.

The five additional words are real lifetime operations: save/reload the
doubled stride through SP+0x50 across allocation, save/reload it across the
descriptor copy, then assign it to S5 at loop entry. They are four stack
transfers and one late saved-register handoff, not alignment padding.
The emitted normalized body matches all110 retail words and all eight
relocations. Raw C is independently qualified for public behavior; raw
private-register, PC and fault identity is explicitly **not** claimed.

The actual plain-owner `pad_c_object` path accepts the derived42 rows,
including the five insertions and relocated bindings. Raw `.reginfo` and
`.options` changes are constrained to the decoded target GPR union; this
target adds no FPR usage. Both padded owners retain literal zero masks,
unchanged ABI flags and all other allocatable pools. Final linked metadata
needs no exclusion or symbol/string permutation.

## Focused qualification and its limits

Seven checks pass before and after installation in both tools configurations:

* **637 guest cases per body**, retail/normalized/raw, compare an independent
  byte model, public memory, ordered calls, source packets and returned handle.
  Every retail110 and raw105 word executes. Cover all256 mode and priority
  low-byte values with nonzero upper words, allocation failure, zero and
  negative counts, signed count boundaries, modulo32 size/context arguments,
  live descriptor/count/second-slot/asset-header mutations, two descriptor
  aliases and sparse wrapped handles/resources. Three further cases execute
  all11 original SDK-copy words. Aliases and wrapped addresses are guest-only.
* Four deliberate private-stride-home interventions compare the normalized
  guest with retail and the corresponding model. Helpers may overwrite the
  exact SP+0x50 home before its live reload. These private-frame probes are
  separate from ordinary C/native behavior and are not imposed on raw C.
* The aligned retained-input census finds exactly five direct JALs at ROM
  0x3E328,0x135DDC,0x135F28,0x169048,0x1E74F0, with no entry/interior
  pointers. All five preparation windows were inspected for descriptor,
  mode, extraSize, priority and stack context. **10 cases per body** connect
  the complete original69-word `func_1513BAE8`, this creator and11-word SDK
  copy. All69 caller words execute. The other four complete parents are
  not claimed as restored or fully validated by these bounded windows.
* **428 fired access cuts**, including 98 delay-slot cuts, compare retail
  and normalized code with complete private memory, GPR/FPR/HI/LO, PC,
  call and access prefixes. This qualifies emitted guest instruction order,
  not portable C fault semantics, hardware behavior or gameplay acceptance.
* Native32 SDK O0/O2/O3 each pass **75 independent little-endian fixtures**,
  with pointer/descriptor size and field-offset assertions, four fixed
  disjoint arenas, all60 seeded descriptor bytes and UBSan traps. Seven
  compiled negatives fail with exit1: old stub, wrong kind, wrong allocation
  total, short descriptor copy, cached second destination, wrong loop gate,
  and lost handle. The freestanding entry requires `-mstackrealign`; its
  initial missing startup alignment caused a fixture crash and was corrected.
* Two independent GNU links exercise all eight bindings, JAL rebases and
  signed HI16/LO16 carry. Ten altered raw words, a changed binding, two
  object register-metadata corruptions and four full-ELF corruptions reject.

The141 frozen inputs include complete owner/caller assembly, actual service
definitions, compiler/SDK inputs, predecessor source/object/ELF/ROM, layout,
registries, guards, conversion CSV and graph. Imported modules and new tools
are separately fingerprinted. The sibling configuration uses a disposable
new-module overlay; its missing `alloc_pools` remains an explicitly hashed,
read-only mounted fallback. All2,434 inherited dirty sibling paths are
fingerprinted and unchanged. Shared smoke checks pass freshly in both copies;
three unchanged shared regression receipts per copy are reused only after
exact helper/test fingerprints. Claude calls for this function: zero.

## Actual production and progress

Actual Make recompiles only this owner and equals the independent complete
ELF prediction: **338 changed bytes, zero exclusions**, solely the target
slot and symbol extent12->440. All6,052 function addresses remain fixed.
All189,088 protected Game bytes across720 owners stay exact. The conversion
CSV and Makefile remain unchanged. Compile/link succeed; `make all` reaches
the expected nonmatching full-ROM checksum, exit2. The inherited duplicate
generated_12D630 recipe warning remains.

| Section | Exact / converted | Percent | Drift | Still different |
| --- | --- | --- | --- | --- |
| Total | 4,227 / 5,512 | 76.69% | 0 | 1285 |
| Game | 3,554 / 4,839 | 73.44% | 0 | 1285 |
| Init | 492 / 492 | 100.00% | 0 | 0 |
| Debugger | 181 / 181 | 100.00% | 0 | 0 |

**183 additional exact functions** remain to4,410/80%. Root README receives
aggregate rows only; the four status indexes get one concise lead while
retaining their historical bodies. Graphify refresh preserves old nodes
outside changed paths and excluded-but-existing legacy files fail-closed;
this is scoped refresh, not fresh full-corpus extraction. Commit tools first,
then consumer source/guards/docs and exact tools pin, followed by a fresh
hook-terminal and preservation audit.

| Artifact | SHA-256 |
| --- | --- |
| Production ELF | `f21949d45ef5dc42d9182acf70a8180cfdc6cea0804c9bdee063673de56df39a` |
| Production binary | `bfe69e2e440e4df557d3f2bd78b33afc02de5eab5d299cdf15c00382411b400d` |
| Padded owner | `5d6f12996cfa1d038511fe855edace1095059cc7f728c225f422472d4eadf282` |
| Guard manifest | `5f6f9d9b935ceac0f3819711842f4d278bbaa5911c32214771aade923d984f87` |

Receipts and private screens remain ignored under
`conker/build/game-resource-view-creator-1513B5E0-match/` and
`conker/build/game-resource-view-creator-1513B5E0-private/`.

Next: **func_1513B83C**, the75-word adjacent routine in the same owner,
VA0x1513B83C..0x1513B968, ROM0x168CEC..0x168E18. Inspect its complete
assembly/callers and recover semantic C before qualification. Keep the wider
80% goal active. The separate108/110-word `func_150A25D4` stays private and
uncredited; preserve frozen handwritten/hidden-ABI boundaries, unrelated
work, private inputs/saves and the frozen host Release checkpoint.
