# 1756 - Animated quad setup wrapper direct C match

Verified: 2026-10-27. Target func_15171F04, owner generated_19F150.
VA 15171F04..15171FC0; retail ROM 19F3B4..19F470.

## Recovered wrapper

Replace the zero-return placeholder with the complete semantic wrapper.
All 47 words /188 bytes emit directly under normal O2/g3, frame 48,
five bindings (three calls and one table HI16/LO16 pair), zero guards.
No source-order search or compiler-profile override is needed.
The interface is:

~~~c
void func_15171F04(f32 x, f32 y, f32 z, void *indirectVertices,
                   s16 lifetime, u16 color, u8 imageIndex, s32 scale,
                   s32 flags, s32 frameStep, s32 alternate, u8 slot, s32 context);
~~~

Use the existing SDK-vertex QuadEffect19F150 layout and byte-exact constructor
func_15171CA0. Forward lifetime/color/image, flags, frameStep, alternate,
slot and context to its eight-argument interface. Allocation failure exits
without reading any returned record, image table or descriptor.

On success pass record->vertices (+0x10), the indirect vertex-source pointer,
x/y/z, positive zero rotation, scale and image metadata to func_151725FC.
Read the returned record's byte +0x58 after construction, then index the
existing u8-pointer table D_8008CA4C and load its descriptor halfword +6.
The original physical call packet carries that full unsigned halfword; the
provider's original byte load at frame+0xC7 consumes the low byte. The typed
provider argument is u8; native tests check its semantic low byte separately
from literal guest call-word parity.

Release the original record through func_1516972C only when geometry setup
returns zero. Every nonzero result, including 0xFFFFFFFF, keeps the record.
The source uses the canonical struct102 release argument with an explicit
cast and includes structs.h. Shared headers themselves are unchanged.
Incoming floating homes and other late reloads retain their original order;
constructor side effects and returned-record/home aliases must remain visible.

## Explicit dependent placeholder change

The geometry provider is in this same owner and was an empty-parameter
zero-return C placeholder. An eight-parameter prototype conflicts with that
old definition. Give the placeholder the measured pointer/float/word/byte
interface while retaining its zero-return behavior. IDO now emits four incoming
argument-home stores before the same zero return: 28 bytes rather than 12.
This routine remains unfinished and receives no byte-matching credit.

The first private screen found the prototype/old-definition mismatch.
A typed-definition screen then exposed these home stores; register hints did
not remove them and were discarded. The final source contains no such hints.
The final strict prediction explicitly includes this dependent code and size
change; it does not exclude the provider or claim all six neighbors unchanged.
Five other neighbors, including the 43-word constructor, and all owner pools
remain identical. All seven compact functions are audited.

## Qualification and original-code boundaries

Both tools copies pass eight fresh canonical methods and shared project-tool
checks. The first runner attempt stopped on a newly written audit syntax
error before tests; its receipt is retained. Corrected canonical_v2 passes
all eight in 59.818s /60.043s. Production then runs two fresh installed
owner/image checks per copy and reuses six semantic methods only after exact
module/input/artifact fingerprints.

- 24,684 guest cases cover every image/slot byte, signed lifetime, unsigned
  color and byte loads, full-width words, raw floating patterns, allocation
  failure, zero and two nonzero geometry results, four returned-record
  destinations, two stack phases, incoming-home mutations and an actual
  GNU-linked table/home alias. All47 wrapper words are dynamically exercised.
  Complete private RAM/GPR/FPR/events/visits and ordered access traces agree.
- Native32 O0/O2/O3 with trapping UBSan each pass 24,576 positive cases.
  Valid disjoint SDK records, image descriptors and typed providers check
  all thirteen semantic arguments, returned-record image selection, table
  retargeting, geometry writes, release decisions, whole-record bytes and
  surrounding fences. Eleven deliberate C variants fail effectively.
  Guest-private home aliases and FCSR/hardware behavior are not portable-C
  claims.
- 205 fired access-prefix pairs preserve private state, trace, PC and branch
  delay ownership. A null-allocation sparse mapping needs no record, table
  or descriptor. Three independent GNU layouts pass 18 guest cases, including
  signed-low table carries and independently rebased helper symbols; the
  table/home alias links are additional. Three raw/binding and seven complete
  image corruptions fail closed.
- An actually compiled cached-image-argument mutant is rejected by its call
  packet: the returned record's image byte must be read after construction.
  It fails by result, not an unmapped access. Production C is unchanged by
  these negative controls.

The aligned whole-ROM census finds one JAL at ROM111B94 /VA150E46E4 in
func_150E4550, with no pointer literal or tail J. Twelve cases execute the
actual 19-word setup/call/branch window plus the real subsequent byte load.
They confirm thirteen physical slots and that the parent overwrites the
wrapper's return register. The complete 984-byte parent is not restored or
credited.

112 connected cases execute every word of the complete original 43-word
constructor, which is identical to the retained ELF body. The lower allocator
is bounded; verify all six allocator arguments, null/success paths, real
metadata fields and all four SDK vertex flag clears. The retained release
body also equals all 28 original words, but release effects in this suite are
a bounded provider contract. Two further cases map all 329 original geometry
words and exercise its authentic early query-failure path and cleanup, with
a bounded plane-query provider. The complete successful geometry/trigonometry
pipeline, allocator/release machinery and live gameplay remain unverified.

Routine Claude calls: zero.

## Production, image and measured status

The actual three-command IDO/padder/GNU assembler Make route reproduces the
qualified object byte-for-byte. Target and owner IDO diagnostics are empty;
the inherited duplicate generated_12D630 recipe warning remains. Production
Make exits zero in 0.534s.

The entire production ELF equals an independent prediction with 165 changed
bytes, zero exclusions: 145 wrapper-code bytes, 18 typed-provider-stub code
bytes and two function-size bytes. Only these extents advance 12->188 and
12->28; no metadata cycle is introduced. All 6,056 function addresses and
6,054 other bodies are fixed. All named ELF definitions are accounted for.
Protected Game data remains exact across 720 owners /189,088 bytes. Inventory,
guard manifest and shared headers remain byte-identical. The map is unchanged.

ELF SHA-256:
~~~text
bd9f7b5c27bdd3cff531753735c1640eb04e2b27b94afe265b17519bc3eb4842
~~~
Native CRLF guard SHA-256 (Git-normalized LF content is unchanged):
~~~text
f867c3817abab6b6ef822343afa48a4b188e7067ce1d4c69a078b54a6f4b4c40
~~~

Seal 16,207 Native/cache inputs and 194 focused inputs. Recount the captured
adopted Native ELF with the unchanged C inventory:

| Section | Exact C functions | Different | Drift |
| --- | ---: | ---: | ---: |
| Total | 3,834 /5,506 (69.63%) | 1,672 | 0 |
| Init | 492 /492 (100.00%) | 0 | 0 |
| Game | 3,161 /4,833 (65.40%) | 1,672 | 0 |
| Debugger | 181 /181 (100.00%) | 0 | 0 |

Only func_15171F04 becomes exact. Converted totals remain fixed. Threshold
4,130 leaves 296 more matches to 75%. The remaining source screen contains
1,543 placeholders, 120 semantic/other definitions and nine unlocated entries.
The newly typed func_151725FC and the unresolved func_1518F5D0 NULL factory
both remain placeholders and uncredited.

Predecessor consumer f4c4a60d667d2bf255733353c9079461302c9085 and tools
5f661001c850cfffa0351221addb73f3b20c4128. Bank tools first at
44b34edbf6e12ebce84d452b14f5787944d64440, then source, consumer pin and measured
documentation. Preserve the independent older mirror's 1,722 inherited dirty
paths plus two new tools files. No push. The root README changes only its
two aggregate matching rows.

Refresh ten changed C/Markdown/tool sources structurally. Preserve prior nodes
and still-valid relationships/contexts; retire only the target's obsolete
placeholder s32-return relationship against the recovered void declaration.
The provider retains s32 return and gains its measured parameter interface.
Validate the wrapper's three actual helper calls against source and R_MIPS_26
bindings. Outside freshness and communities remain historical, with no full
corpus extraction or global clustering/centrality claim. Receipts and the
independent final audit remain in conker/build/game-record-setup-wrapper-match/.

Next inspect func_151A18DC in generated_1CC440 using a fresh frozen predecessor
and caller/ABI audit. Keep func_1514E920 private and uncredited. The 75% goal
remains active.
