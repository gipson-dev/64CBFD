# 1737 - Packed Object Command Direct C Match - 2026-10-26

The adopted Native ELF measures **3,814/5,506 exact C functions (69.27%)**,
Game **3,141/4,833 (64.99%)**, zero address drift and 1,692 different.
Only `func_1509F284` gains credit. Inventory and converted-byte totals stay
fixed; 316 more matches reach the 4,130-function 75% threshold.

## Complete source and packed interface

`func_1509F284`, owner `generated_CBDB0`, occupies VA `0x1509F284`..`0x1509F33C` and
ROM `0xCC734`..`0xCC7EC`. The complete routine has **46 body words, no alignment word,
and a 40-byte frame**. It saves S0/RA and homes its unused first argument.
Retain that argument and the retail symbol. The other arguments are a full
32-bit command and a pointer to six packed words.

Command 1 sends `record[2] & 0xFFF` to `func_1509F660` with mode 0; command 0 uses
mode 1. Command 2 sends the unsigned upper 16 bits of `record[0]`, the low 12 bits of record[2],
and `record[3..5]` to `func_1509F77C`. Each recognized command returns 1 regardless
of the provider result. Unknown full-word commands return 0 without reading
record, so NULL remains valid on that path. Preserve the case 1 before case 0 source order
and the explicit unsigned high-half mask before the logical shift.

The callback is D_800884D4 slot 6, at address `0x800884EC` / ROM `0x22CFAC`. A full aligned
reference-image search finds that sole literal registration and no direct JAL.
Graphify first locates the old stub at `generated_CBDB0`.c:L25; its return-type
edge describes the stub, not independent ABI evidence.

## Provider ABI and direct compiler output

`func_1509F660` is `void(s32, s32)`. `func_1509F77C` receives full incoming words,
then narrows its first and third values inside the provider before its final
call. Its previous u16/s16 C formal types caused a fully prototyped caller to
insert extra narrowing and emit 47 words. An unprototyped declaration conflicts
with the promoted-width definition; implicit declarations also fail CFE.

The accepted source declares F77C's first slot u32 and third slot s32, and
makes its existing downstream u16/s16 conversions explicit. Concise comments
explain where narrowing belongs. No shared header or calling object changes.
The provider's entire emitted body stays byte-identical, as do the other 15
neighbors. The wrapper and all 16 neighbors retain their existing addresses.

The complete semantic wrapper emits all 46 original words directly at normal
O2/g3, with three R_MIPS_26 bindings at relative offsets `0x40`, `0x5C`, and `0x94`.
Raw SHA-256: `60ae6ecf1656a8383435c541960b00e313c872d4457ce81c8b6635f5b243a5ac`.
No guards, instruction insertion/omission, profile override or assembly body
is added. The whole existing guard manifest remains byte-identical.

## Focused qualification

Both canonical tools copies pass six fresh methods and their shared tools
checks. After installation, each copy runs two fresh input/image checks and
reuses four unchanged semantic checks only under exact module, frozen-input
and qualified-artifact fingerprints.

- 2,688 guest cases cover full-word commands, packed identifier/payload classes,
  two stack phases and bounded provider clobbers/effects. Compare with an
  independent public-memory/call reference and complete original/C states.
  All 46 body words execute. Four lazy-read cases remove unused record backing.
- Native32 O0/O2/O3 each execute 896 wrapper cases and 64 direct-provider cases.
  The complete wrapper and both actual C providers are compiled together;
  bounded lookup/sink stubs check full incoming slots, signed16/unsigned16
  narrowing, finite coordinate conversion, ignored provider returns and full
  State canaries. Trap UBSan stays enabled. Ten compiled semantic negatives
  fail with the intended status 23. Align the freestanding native entry before
  calling compiled code. Native tests use valid objects and arrays.
- Execute the complete 92-word variadic caller `func_1509BFB0` in 252 cases,
  including negative/zero/unrolled counts and both stack phases. Verify slot 6
  callback selection, packet construction, provider arguments and return values 1/0.
  Execute the real 26-word script window `0x150AE12C`..`0x150AE194` in 56 cases, covering
  selector-zero bypass, preserved high index bits and S7 link scratch. This
  is a bounded script window, not qualification of its full parent.
- 56 fired guest access prefixes compare complete original/C states. Provider
  behavior remains a bounded contract; these checks do not emulate the large
  providers, gameplay or hardware fault semantics.
- Six independent GNU links compare original assembly with fresh C across
  three code/provider layouts, including a first-JAL PC+4 region carry at
  entry `0x1FFFFFBC`. All three bindings and all 46 words agree. Seven full-image
  corruptions, including file extent and a neighbor boundary, are rejected.

The fresh complete-owner compile preserves all 17 raw functions except the
intended wrapper replacement. The ordinary Make compiler/padder/assembler
reproduces all 17 compact functions and the entire independently padded object.
Owner compiler diagnostics are empty. The inherited `generated_12D630` duplicate
recipe warning remains; no unrelated build rule is changed.

## Production and committed continuation

Production Make exits zero in 11.469s and reproduces independent
ELF cddeb3c277626c6b4865dc20eb66c36b5eb6bbd2ad52293fbc93710743754b56. The complete delta is **136 bytes: 135 target-code bytes and one
symbol-size byte, zero exclusions**. Target extent changes 12 -> 184. Preserve
all 6,056 addresses, 6,055 other bodies and exact Game data: 720 owners / 189,088 bytes,
SHA-256: `0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.
No symbol/string serialization allowance is used.

Source SHA-256: `a4a708884443484fd7724f1fd9b6076343c5a86c3533f65b4ece0e28db9899ba`.
Padded object SHA-256: `aa971c155f574b11724feccabe6182cff57e9ff6cb7516b41f3af4a22c2c8cca`.
Baseline consumer e880311f, tools efb8378f, ELF `121a867b`.
Tools 3626acace3ba7bdb0c4bf7d0175774da71a09175 are committed first, then pinned by the consumer.
The seal covers 16,115 Native inputs and exactly four qualified adoption outputs.
Preserve all 1,684 pre-existing dirty paths and the older tools mirror's history;
only the new pair is added there. No push or host-port work is performed.

The scoped native no-cluster graph refresh updates eight changed C/Markdown
sources and must retain or uniquely relocate all 44,318 previous nodes. Preserve
historical manifest freshness outside that scope and prior community labels.
No global clustering/centrality recomputation or full-corpus extraction is
claimed. Tools AST extraction remains separate from the parent graph.

The actual adopted ELF queue contains 1,563 placeholders, 120 semantic/other
entries and nine unlocated screens. Next screened placeholder is `func_1512B100`
(`generated_157840`), uncredited until source/ABI, guest/native, owner/Make and
production qualification closes. The unresolved pointer/NULL factory remains
a placeholder. Keep the 75% goal active. Routine Claude calls: zero.

Prepared-checkout focused command:

~~~sh
python3 -m unittest tools.tests.test_game_packed_object_command_match -v
~~~
