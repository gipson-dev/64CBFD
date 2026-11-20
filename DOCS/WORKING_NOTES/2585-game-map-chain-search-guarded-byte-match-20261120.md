# Note 2585: Two-column map-chain search guarded byte match

Date: 2026-11-20. Consumer baseline `9ee61facbac011ccca2210e1c4a087399cc6ac8b`;
tools baseline `bd443a14d6d4a2dd7a6a2ac886bf97f384428110`.
Qualified tools commit: `2606e4b690ed52be3c60bf4d5b6716cd235e63f1`.

`func_15105C24` is restored from GLOBAL_ASM to complete semantic C and is
byte-exact across its **46 body words / 184 bytes and 47-word retail slot**,
retaining a **zero-byte frame**. Raw O2/g3 C emits 47 words. **40 checked
word/binding guards** recover register roles, independent opening layout and
loop-counter delay transfers. One address addition is folded into the column
load, omitting that redundant source word; no instruction is inserted.
This removes the last GLOBAL_ASM from `conker/src/game_131F30.c`.

Fresh production recount: **4,572 / 5,523 (82.78%)** total, **3,899 / 4,850
(80.39%)** Game, zero address drift and 951 different. Init 492/492 and
Debugger 181/181 remain exact. Converted functions: **5,523 / 6,048
(91.32%)**, 86.43% of bytes;
Game **4,850 / 5,327 (91.05%)**,
85.83% of bytes. One ASM conversion row becomes C.
The 85% goal remains active: **123 more matches** at this denominator, which
further ASM conversions can increase. Root README changes aggregate rows only.

## Search order, table and pointer interface

VA 0x15105C24..0x15105CDC, padding through 0x15105CE0; ROM
0x1330D4..0x13318C, padding through 0x133190. The leaf accepts one s32 key and
returns the first matching node pointer or NULL. Node-next is +8, unsigned
type byte +0x13 and full 32-bit key +0x28. Local types name observed fields;
unobserved prefix bytes remain opaque. No complete allocator object is claimed.

The outer loop selects columns **35 then 95** from `D_800A5770`; the inner loop
visits row 0 then row 1 at a **0x1A0-byte stride**. Each list is followed through
next pointers until a node has type 0x2E and the requested key. It stops at the
first match. Both loop counters narrow through u8 at their updates; the source
retains the observed shift/add row stride and explicit loop control.

The previous shared declaration described `D_800A5770` as a single s32 despite
two indexed reads. `conker/asm/data/24A230.rodata.s` independently supplies
0x23 and 0x5F, followed by eight unchanged alignment bytes. The real producer
`func_151494E0` passes this address and count 2 to `func_15169260`. Its original
assembly loads table words through the supplied pointer. The header now declares
`s32 D_800A5770[2]`; no scalar out-of-bounds indexing is used. No data bytes move.
The complete dispatcher/producer implementation is not reconstructed here.

A proper `void *func_15105C24(s32 key)` prototype is added inside `functions.h`'s include guard.
The actual `func_1515FBC4` caller now holds its result in `void *node` and uses
an explicit byte-offset read at +0x98. It still submits command 0x6002E with an
attached-object index or -1. Its original complete 28-word body is unchanged.
The ROM has exactly one direct JAL at 0x18D084; this census does not exclude
arbitrary computed calls. The consumer reads all 32 returned pointer bits.

The three affected dependency owners retain **35 + 12 + 15 = 62 functions**,
normalized pools, loaded sections and register info under the proposed headers.
Their complete production-route objects are byte-identical. The target owner's
other ten functions and pools are unchanged. Two unrelated owner warnings remain.
No compiler profile, shared structure layout or original assembly is changed.

## Derived layout and control-flow proof

The normalizer derives output from the actual source, without a retail-word
replacement array. It folds the selector-address ADDIU low relocation into the
load and moves the paired HI relocation with its instruction. Register-field
changes follow the block live intervals. Backedges target their full headers;
duplicated delay-slot shifts become transfers of the narrowed induction values.
Raw hash: `db62de6a30284d461c8a4265f4f0a230d36428302b2143abaf77fb98a1d4c520`.

An independent instruction-driven relation has **37 transfer paths**: five
entry paths and 11/9/7/5 node-iteration paths for the four group/row states.
It compares ordered public reads, exact live roles, return value, SP/return link
and all saved ABI registers. It covers **46/47 raw and 45/46 retail reachable
words**. The dead next-load after the early return is retained and normalized;
the final slot padding is preserved. There are no stores, helpers or FP effects.
The relation supports arbitrary stable public memory and list iterations in
the valid-object domain, including aliases and repeated heads. Acyclic fixtures
exercise termination; no cycle guard is invented for retail's unbounded lists.
Raw instruction PCs, timing and full hardware fault-state identity are separate.

**Nine effective relation mutations** challenge type, key/next offsets, row/group
bounds, address scales and return value. The closed normalizer rejects all
47 changed source words and all four altered bindings. **160 guard checks**
exercise every row's expected word/binding through both real padders. Eight
independent GNU links cover four symbol rebases, including low halves
0/0x7FFC/0x8000/0xFFFC and the signed carry in the folded selector load.

## Qualification, recipe transition and production

- Primary tools and a **1,005-file isolated sibling overlay** first pass seven
  fresh preinstall tests. The unpadded debugger dependency below then requires
  an explicit follow-up audit. Both configurations pass **eight complete fresh
  installed tests**, including the new dependency case and repeated guest,
  native, relation, padder, rebase and corruption checks. The final overlay has
  **1,006 files**: 341 equal sibling, 655 explicit primary fallbacks, nine task
  files and one bootstrap. All imports are hash-paired; preinstall receipts are
  retained against their original Git versions. The real dirty sibling's HEAD,
  raw status and 343 dependency hashes remain unchanged.
- **288 guest cases per stream** compare return values, complete ordered read
  traces, read-only public memory and ABI preservation. Cases include empty lists,
  all four search positions, duplicate/reversed/extreme valid columns, high-bit
  keys, false type 0xAE and keys differing only above bit 15. **37 fired read
  prefixes** agree. **64 cases per stream** execute the original 28-word parent,
  including absent attachments and signed index arithmetic.
- Actual SDK32 C at **O0/O2/O3 each passes 288 cases** with strict aliasing and
  UBSan. Seven compiled semantic controls fail at runtime. The initial key-width
  control was ineffective on low-bit-only key differences; high-word differences
  and matching-key/wrong-type nodes were added before credit. These are bounded
  native vectors, separate from universal hardware or unrelated helper acceptance.
- Both full-owner padders agree on all loaded instructions and pools. Actual Make
  qualifies the old **five-command mixed** route and the new **three-command
  plain C** route under the existing O2/g3 profile. All three header dependencies
  additionally pass their own real Make routes and object comparisons.
- Production Make passes in **335.85 seconds**. The complete ELF equals the
  independent prediction with **one changed byte, zero exclusions**: the target's
  ELF symbol size changes **188 -> 184**, separating its actual body from the
  trailing padding word. Every loaded function slot and address, all other
  symbol fields and all **189,088 protected data bytes / 720 owners** are unchanged.
  All **2,059 frozen inputs** are checked except declared source/header/guard/
  conversion/docs changes. Four full-image corruption controls fail.
  New ELF SHA-256:
  `d428a774da73a7a019242548481f707cc7e7c6d670c233af41189771495dfb04`.

The production input audit also finds a changed **unpadded debugger object**,
`debugger_258ED0.c.o`. An archived copy is retained only after matching its exact
frozen SHA-256. Its sole original assembly function, pools, relocation sections,
register info and every ordinary section remain identical. The only changes are
the undefined `D_800A5770` symbol's recorded size **4 -> 8** and **20 additional
bytes of ECOFF auxiliary type metadata**. A fresh paired CFE/assembler compile
uses the original debugger source and old/new headers at the same private file
path; it reproduces these two metadata sections and the same 20-byte growth.
Both rebuilt bodies/bindings agree with actual production. Closed object hashes
reject three corruption controls, including nonloaded metadata. This dependency
is declared in the production plan rather than excluded. It does not add another
ELF difference: the complete image still equals the independent one-byte size
prediction. The extra audit is a separate tools commit before consumer adoption.
Final review moved the new public declaration inside the header guard. A fresh
35.539-second production Make retained the same complete ELF prediction, and
both final eight-test suites pass again with an explicit guard-placement check.
The final unpadded debugger fingerprint is
`483b5099e8d671e2f9401d453e84a1fd73472237f40d96b79b6ad1b5e0a958c0`.

Tools are committed before consumer code, headers, guards, docs and gitlink.
`make tools-check` passes. No push, Claude call, host edit, save change or frozen
Release operation occurs. Retail slot bytes are unchanged, so no host delta is
needed. Graphify retains old IDs, links the manifest to the installed C and marks
the original ASM historical. Native update, scoped AST and post-commit retention
receipts are kept in the ignored target packet; this is not a full-corpus extraction.

## Continue

Next owner is `generated_133190`, beginning with `func_15105CE0` at
VA 0x15105CE0..0x1510608C / ROM 0x133190. Only its layout span was inspected;
caller, source recovery and qualification remain open. No credit for it.
Reproduce this suite with
`python3 -m unittest tools.tests.test_game_map_chain_search_15105c24_match -v`.
The ignored `conker/build/game-map-chain-search-15105c24-private/` holds immutable
inputs, selected source, both Make routes, dependency audits and the current handoff.
