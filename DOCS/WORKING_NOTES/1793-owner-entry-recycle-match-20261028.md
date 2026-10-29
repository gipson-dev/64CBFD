# Owner entry recycler - guarded C match

Verified 2026-10-28. Restore `void func_150C1198(u8 *actor)` in
`conker/src/game/generated_EDE60.c`: VA 0x150C1198..0x150C1254,
ROM 0xEE648..0xEE704, 47 instructions / 188 bytes. The full retail slot is
200 bytes, including three zero alignment words. The routine has no stack
frame or external relocations. Retain the retail name and add comments for
the recovered chain behavior and live pointer reload.

## Recovered behavior and interface

The actor's pointer at 0xA8 selects its owner. The owner stores an entry-array
pointer at 0x40, a signed active-chain head at 0x44, and a signed free-chain
head at 0x46. Each eight-byte entry contains an actor pointer and a signed
next index at offset4; the last two bytes remain untouched.

1. Traverse the active chain until the first matching actor or the -1 sentinel.
2. If found at the head, replace the active head with the matched entry's next
   index. Otherwise update the predecessor's next index.
3. After a predecessor update, reload the entry-table pointer. A guest-memory
   overlap can change this pointer through the preceding halfword store.
4. Set the released entry's next index to the current free head, then replace
   the free head with the released index. Preserve the entry's actor pointer.

Empty chains and absent actors produce no writes. Duplicate actors remove
only the first match. Signed indices are preserved, including sparse guest
probes outside normal native arrays. A no-match cycle remains nonterminating;
only bounded prefixes are qualified for those inputs.

The complete ROM census finds no direct J/JAL. Its sole aligned function
pointer is ROM0x22E2C0 / VA0x80089800, the first entry of `D_80089800`.
The original `func_151303EC` uses the signed actor byte at0x73 to select this
table: -1 skips the callback, zero selects this routine. The JALR is
ROM0x15DF28 / VA0x15130A78. The callback takes the actor in a0, and its result
is ignored. The caller reloads the actor before `func_1516972C`.

The 19-word original caller window and all28 original instructions of the
existing release helper are exercised. The helper first calls `func_151696DC`,
then reloads the unsigned actor type. Types below2 return; other types select
a callback from the 52-byte `D_8008B4D0` table or fall back to `func_15169804`.
The parent C remains a placeholder, so this recovery does not add a fabricated
current C caller edge or credit the parent. Downstream callbacks remain bounded;
these checks do not establish complete teardown, heap behavior or gameplay.

## Closed instruction normalization

The normal O2/g3 compiler profile emits 48 instructions. Eleven expected-word
guards produce the 47-word retail body: ten replace words and one omits a
redundant private pointer copy. Of the final47 words, 37 are unchanged compiler
words. No instructions are inserted and no compiler profile changes are needed.

- Five words change which equal signed head/current register receives the
  initial load and copy. Both values still hold the same signed16 head.
- Keep the released-entry pointer in t1 after the actor argument in a0 becomes
  dead. Move an independent pointer addition into the head-test delay slot,
  omit the redundant t1-to-a0 copy, and retarget the two remaining pointer uses.
- Recompute every branch displacement from the explicit old/new instruction
  index map. Only the found-exit displacement changes after the omission.

The normalizer first verifies the entire raw body and empty binding set. It
derives the guard rows from these field and instruction-order changes. An
independent assembly of the retained original then matches all47 words.
The original word at offset0x4C is unreachable but remains byte-exact; all46
reachable instructions are visited. The three alignment words also match.

## Qualification and installed evidence

Both tools copies pass eight fresh canonical checks and the shared tools check.
After production installation, each copy passes two fresh installed checks;
six semantic checks are reused only with identical input, module and artifact
fingerprints.

- 2,756 guest cases cover empty/missing/head/middle/tail/duplicate chains,
  signed links, sparse indices, two overlapping guest layouts and both stack
  phases. Normalized C agrees with retail in complete state and access trace;
  raw C agrees in public memory. The actor pointer and entry padding survive.
- 864 original-caller cases visit all19 window words and all28 release-helper
  words. Cover disabled dispatch, selector-1, target and other callback routes,
  post-unlink actor-type changes, fallback and dynamic destructor paths.
- Native32 O0/O2/O3 each pass10,920 defined-object cases with real SDK types,
  pointer/offset assertions and trapping UBSan. Nine deliberately wrong C
  variants fail observably. Sparse and overlapping guest headers are excluded
  from native portability claims.
- 61 direct and56 connected access-fault prefixes agree in complete state and
  trace; direct cuts also compare PC/delay state. Two direct delay-slot cuts
  and three nonterminating-cycle prefixes are included. These checks concern
  the emitted guest instructions, not portable C fault behavior.
- Three independent GNU-linked layouts pass216 cases for original, guarded
  actual-Make and normalized selected objects, plus the raw compiler body.
  Thirteen raw-body/binding corruptions and all11 changed expected-word guards
  reject. No external relocation or carry assumptions are needed.
- Ten IDO-compiled semantic negatives terminate with actual wrong-output
  witnesses, including a stale table-pointer reload under the guest overlap.
  Incidental faults and unsupported instructions are not accepted as witnesses.
- Twelve whole-image corruptions reject. Production reproduces the complete
  independently predicted ELF exactly, with zero excluded bytes.

The actual three-command Make recipe reproduces the qualified padded object.
All six neighboring functions, pools and bindings remain fixed. The owner
retains two existing Warning712 diagnostics in its earlier wrappers; the
selected function has no diagnostics. The full build retains the unrelated
duplicate `generated_12D630` Make warning.

The literal image delta is134 bytes:133 target instruction bytes and one
target symbol-size byte (12 to188). There are no symbol-order permutations
or other metadata changes. All6,056 function addresses and6,055 other bodies
remain fixed, as do189,088 protected Game bytes across720 owners. The C
inventory CSV and complete inherited guard prefix remain unchanged; exactly
eleven guard rows are appended. The production seal covers16,449 files and
402 focused inputs; the new working note joins the closing seal.

| Artifact | SHA-256 |
| --- | --- |
| Raw compiler body | dead4e217db1b30585c2456dcefc0b257064798a9f6c75df6fe8963f8e088fd5 |
| Normalized body | 95de15db035c99796749593aec8e86e7fddb5019b4f1f0411651d1c8323259c3 |
| Adopted object | 84e77b04ba7ce18b113a88b9d66f8b6ee2f313b88a5b203620ed45da40facd81 |
| Adopted ELF | 8d8dbb6c26161c75fa60e44f36576aaae96e55644f836b81fb5e41bd8feecb22 |
| Guard manifest | efd6bd3f1e7efba51b4b566abfd447477133a8a52daa3804bc7550b32d273293 |

## Bank, graph and progress

Predecessor consumer: `b383987b49fdd5102e312ea8ab67261aba8867c2`.
Tools committed first: `01a45c2d556802bd845c38b067ca18dfbfaadcdb`.
Bank the owner C, guards, tools pin and measured documentation together.
Preserve1,820 inherited dirty paths plus three new qualification files in the
older tools mirror. No push or mirror commit. Claude calls:zero.

Refresh the eleven changed C/Markdown/tool sources in Graphify, retain all
previous nodes and every still-valid relationship, and retire the placeholder
return-type context with source evidence. Record the original indirect caller
as bounded ROM evidence. Preserve outside-scope manifest rows and historical
communities; this is a scoped AST refresh, not a full-corpus extraction.

The recount uses the adopted native ELF, not an older summary:

| Section | Exact C functions | Address drift | Still different |
| --- | ---: | ---: | ---: |
| Total | 3,871 / 5,506 (70.31%) | 0 | 1,635 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 3,198 / 4,833 (66.17%) | 0 | 1,635 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

The active75% goal needs259 more exact functions to reach4,130/5,506.
Remaining source shapes:1,506 placeholders,120 semantic/other and9 unlocated.
Init and Debugger figures describe the existing C inventory; they do not
claim that retained handwritten assembly is C.

Next inspect `func_150E3514` in `generated_1104D0` (50 retail words).
The queue is only a size/difference screen; caller, semantics and image gates
remain pending. `func_1514E920` stays parked and uncredited.
Private evidence: `conker/build/game-owner-entry-recycle-match/`.
