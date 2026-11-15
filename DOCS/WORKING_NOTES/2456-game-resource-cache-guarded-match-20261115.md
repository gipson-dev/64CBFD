# Game record resource-cache guarded match

Date: 2026-11-15. `void func_15016850(void)` replaces its zero-return
placeholder with the recovered record resource-cache builder. All **84 words**
match retail with **27 checked guard rows**, including **three derived
instructions**. Its original **0x60 frame**, seven saved registers and exact
private homes now emit from C. Owner `generated_43D00` advances to
**1 / 3 exact**, superseding the private checkpoint in
[Note 2455](2455-game-resource-cache-private-recovery-20261114.md).

The actual production ELF recount is **4,496 / 5,515 (81.52%)** total,
**3,823 / 4,842 (78.95%)** Game, zero drift and **1,019** different. Init
remains **492 / 492**, Debugger **181 / 181**. **192 more matches** reach
the active 85% total goal. Converted counts/bytes stay **5,515 / 6,048
(91.19%) / 86.17%**. The root README changes aggregate figures and snapshot
date only.

Source: `conker/src/game/generated_43D00.c`; original assembly remains
`conker/asm/43D00.s`. VA **0x15016850..0x150169A0**, ROM
**0x43D00..0x43E50**, **336 bytes**. The 812-input production freeze records
consumer `d2ce800b` / tools `ad71ba4`; intervening private bank
`b6b09232` / `3c8921b` changed only tools/pin/documentation. Production inputs
remain at that freeze until this adoption. Artifacts are retained under
`conker/build/game-resource-cache-15016850-match/`, including `qualified-84/`
for the earlier uninstalled draft.

## Source, ABI and original save recovery

The builder clears the byte cache count, scans the resource at +4 in each
0x30-byte record, and deduplicates against unsigned halfword cache IDs. IDs
below 0xBB call `func_1502B7F0(&handle, 2, 18, resource)`. The loader output
is initialized only once, at **SP+0x50**; a skipped or non-writing loader can
reuse its previous handle. Non-null handles append pointer, ID and byte count
in the original order. Live table/count changes and the captured resource
value are retained across opaque loader effects.

Explicit shift/subtract statements compute the scaled loop extent without
keeping literal 48 in S7. This removes the private draft's extra saved
register and restores every original save home: **S0..S6 at SP+0x18..0x30**,
**RA at SP+0x34**, handle at **SP+0x50**. No frame guards, dummy locals,
volatile qualifiers or compiler-profile changes are introduced. The existing
profile is **O2/g3/mips2/o32**.

The input global now uses the existing **`struct258 *`** declaration from
`structs.h`, with explicit byte access for the full 0x30-byte record stride.
It does not index an array using the shorter prefix's sizeof. This aligns
the pointer declaration with `variables.h` without editing a shared header.
It also recovers retail's commutative address-add operand order directly.
The loader's `void **, u32, ...` prototype matches the existing declaration.

Raw C emits **81 words / 15 binding sites**, SHA-256
`d3f5abc8fb11e70af7d7c262f461082ef89a68b723d542eb746eab77262b2c8c`.
Its 42 reported differences include the three-word length deficit. Both
neighboring raw functions and owner pools remain unchanged.

The original caller at **0x1501706C**, ROM **0x4451C**, supplies no arguments
and ignores the result. A checked traversal of its **16-instruction
continuation graph** finds no incoming V0 read before either `func_15083DA0`
or `func_1508295C` overwrites it. Their original four-/nine-word prefixes
define V0 before reading it; the latter definition is in an ordinary branch
delay slot and executes for both outcomes. Two controls reject a forwarded
old V0 and a removed dominating overwrite. This supports the recovered void
interface; full parent reconstruction and its own return contract remain
outside this child qualification.

## Derived normalization and proof

The normalizer consumes each of the 81 source words once. It restores the
retail split bound calculation using two derived arithmetic copies and one
explicit join branch, inserted at normalized **+0xB8 / +0xE8 / +0xF0**.
They are not alignment NOPs. The existing count arithmetic moves to the
appropriate paths; the temporary bound uses retail's V1 role. The found
conditional is inverted with its corresponding edge mapping, and the null
handle's likely branch becomes the original ordinary branch. All branch
targets, delay slots and named bindings are updated through the closed map.

An independent relational proof checks **five transfer paths** from the
found test through the loop join. Ordered reads/writes, loader packets and
calls, saved registers, SP, the live count snapshot and loop-bound expressions
agree. The surrounding prefix/dedup loop and complete epilogue are checked
word-for-word apart from declared branch targets. Equal offset/bound state
closes the loop induction; its original likely backedge reload is retained.
The read-value model overapproximates memory responses, so identical ordered
access/call traces also retain arbitrary alias effects within that ABI model.

Three valid-instruction proof controls alter a subtraction operand, bound
shift and ID-address shift and are rejected. **96 corruption controls** reject
all 81 changed source words and all fifteen changed bindings. Normalization
reads no retail ROM bytes. Full raw fault-register state and opaque helper
internals are not claimed. The final normalized instructions themselves are
literal retail matches.

## Qualification

- [x] **1,440 guest cases / three streams**, all **84 retail words visited**,
  compare complete public memory, loader packets and complete helper-entry
  snapshots. These include all **256 record-count byte values**, duplicates,
  empty lists, threshold IDs, null/non-writing outputs and all sixteen live
  provider mutation combinations.
- [x] The **1,280-byte cache** preserves actual ID/pointer table overlap;
  **32 guest record/cache alias cases** and two stack phases pass. Guest
  larger byte-index behavior is separate from the native capacity contract.
  Three emitted controls reject initial-handle, saved-register and resource
  argument changes. No full raw memory-fault state equivalence is inferred.
- [x] **576 native32 cases per O0/O2/O3**, with asserted undefined-behavior
  trap flags, compare all **1,280 cache bytes / 768 record bytes**, live count
  and table selection, loader packets and full entry observations. Native
  storage is bounded to eight entries/records; record buffers are explicitly
  aligned for the shared pointer view. Six effective C controls retain handle
  lifetime, threshold, halfword comparison, count increment and live globals.
- [x] The authentic **JAL/NOP caller window** passes **64 cases per stream**,
  with memory, packets, observations, saved GPRs/FPRs and SP checked. An aligned
  input census finds exactly this one direct call and no literal pointer.
  The separate result-use proof above closes the child return interface.
- [x] Both complete-owner padders, all three owner functions, four independent
  code/data layouts and **12 GNU links** pass, including low-half carry cases.
- [x] Mounted pre-install suite passes in **62.249 s**, followed by the fresh
  caller-result proof. The final nine-file sibling-overlay suite passes in
  **44.210 s**. The installed matching suite passes in **44.502 s**. Fresh
  `make tools-check` passes; unchanged unrelated neighbor suites are not
  presented as freshly executed.

Reproduce on the prepared consumer with the adopted matching fixture:

```sh
PYTHONPATH=. CBFD_CONSUMER_ROOT=. python3 -m unittest tools.tests.test_game_resource_cache_15016850_match -v
make tools-check
```

The older private recovery fixture remains tied to its pre-install baseline;
use the matching fixture for the installed source. The qualified 84-word
private draft and its old tools revision remain archived, not credited as a
separate recovery.

## Production audit and resume point

All **812 frozen production inputs** pass before installation. The actual
Make owner's three commands agree with the independent compiler/padder check.
The production ELF is byte-for-byte the independently predicted image:
**288 changed bytes**, target body/size plus three closed named-metadata swaps,
with **zero exclusions**. The swaps are `D_800BE5A8`/`D_800A8B54`,
`D_800BE9F8`/`D_800BEAD8`, and `D_800BE9F0`/`D_800BEAD0`; all named values and
extents remain fixed apart from the declared target function size.

All **6,051 function addresses**, two neighboring bodies, conversion rows,
**82 headers** and **808 immutable inputs** remain fixed. Only the intended
object changes among **698 objects**; its changed sections are `.text`,
`.rel.text`, `.shstrtab`, `.strtab`, `.symtab`. The CSV retains its complete
prior byte prefix and appends exactly 27 target rows, three insertions and no
omissions. The known duplicate `generated_12D630` recipe warning remains.

Protected data is exact across **189,088 bytes / 720 owners**, SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.
Production ELF SHA-256:
`668933c3c17e33b1f6d52729397cdfaf7a88690fac78d81bae9cde41c9b80d9c`.
Sibling HEAD stays `ddbdd16b53ce60b054fb6e11bf0649a41f48375a`, with all
**2,439 dirty paths** and status SHA-256
`a3b1d31058efd5c8483ee15ece0d00b39f54bdfce5b08a8c64838636db14e0fb`
preserved. All nine overlaid task files are byte-identical to the mounted
files; no sibling file is overwritten.

Scoped Graphify AST merge covers ten files, retaining all **61,134 old IDs**,
zero loss: **61,154 nodes / 114,887 links**, zero LLM tokens. This is not a
full-corpus re-extraction. Routine Claude calls: zero. Tools commit
`1e3b5cc8e67476ccff4b8f6f20f7d86a9e79c1c6` precedes the consumer source/pin/documentation commit.
No push; the host Release checkpoint remains frozen.

Next: the owner's **477-word parent `func_150169A0`**. Its recovered child,
input record stride, loader protocol and result-use continuation are now
available as exact components. Preserve the separate common particle updater
as private at [Note 2452](2452-game-common-particle-frame-native-and-callers-20261114.md).
The broader 85% goal remains open.
