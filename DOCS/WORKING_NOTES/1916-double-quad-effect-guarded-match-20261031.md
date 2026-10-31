# 1916 - Double quad effect restored from guarded C

Date: 2026-10-31. Function `func_15166118`, generated owner `193430`.
VA `0x15166118..0x15166204`, ROM `0x1935C8..0x1936B4`.
Tools checkpoint: `473beb80e6e2099b7bf926e09bdc9f448714b5dd`.

The zero-return placeholder is replaced with the semantic double-quad
effect constructor. The complete 59-word slot is byte-exact after thirty
checked register-allocation/setup guards. The C compiler already emits the
correct 59-word length, 32-byte frame, both call relocations, memory access
sequence and all field/coordinate values. No words are inserted or omitted,
and there is no alignment padding.

## Source and ABI

The function returns void. Its first eight arguments are full signed words:
two byte-valued settings, x/y/z, animation step, lifetime and mode. Only the
ninth argument, the allocation selector, has a byte ABI; category is the
tenth full word. The original caller ignores the result register.

Allocation uses `func_15167A68(4, category, 0xA8, 1, selector, 1)`. Failure
adds no constructor writes or coordinate-origin update. Success sets the
quad count at offset `0x95` to two, then writes two blocks of four UV pairs
at stride `0x40`, preserving the exact `0x2000`/`0x2800` corner pattern.
Only the sixteen UV halfwords change; other vertex fields remain untouched.

Phase at `0x9E` becomes one. Lifetime is truncated into bytes `0x92` and
`0x93`; x/y/z into halfwords `0x98`, `0x9A`, `0x9C`; step into `0x96`;
mode into byte `0x94`; and the first two settings into `0xA0`/`0xA1`.
Finally, `func_1517E05C(x, y, z)` receives the original full coordinate
words. Its complete original seven-word body writes their low halfwords
to `D_800DD470`. The recovered helper definition confirms three arguments.

The alternative source was a hypothesis only. Its incorrect full-word
stores at byte/halfword fields, wide selector and extra helper argument
were corrected from retail instructions and the recovered helper definitions.

## Guard scope and proof

Thirty expected-word guards normalize these closed compiler intervals:

- Allocation result in A3 becomes T0 for the record writes.
- Within the quad loop, low/high UV constants, counter and bound move from
  V0/A0/A1/A2 to A0/A1/A2/A3.
- Post-loop temporary loads move from T0..T3 to T1..T4.
- Five independent setup instructions are permuted into the retail order.

`register_proof` reconstructs the retail words through only those register
substitutions and the explicit setup permutation. It rejects changes to
immediates, control-flow destinations or memory offsets. Complete raw-body
SHA-256 and both relocation bindings are checked before normalization.
The actual padder rejects sixty bad expected-word/binding preimages, and
the entire inherited CSV prefix is preserved. No helper or shared headers
change. The unpassed fourth origin-writer register is not an ABI input.

## Qualification evidence

- Eight fresh target checks pass independently in each tools copy, plus
  both shared tool checks. Each installed copy runs two fresh source/image
  checks and reuses six unchanged checks by complete input, module and
  qualified artifact fingerprints.
- Guest tests pass 1,576 cases, with 3,152 original/normalized executions
  and 1,576 raw C executions. Every target and origin-writer instruction is
  exercised. Raw C agrees in complete RAM, preserved registers, calls and
  memory trace; dead caller-saved registers differ as documented. Normalized
  execution agrees in complete machine state. Another six cases use two
  independent entry/helper/global rebases. All 106 access cuts, including
  nine delay cuts, agree. Incoming-home mutations are guest instruction
  evidence, without a portable C alias or fault claim.
- The aligned retail census finds one JAL at ROM `0xA2280` and no literal
  function pointers. Its original 31-word caller tail passes 128 cases,
  including float truncation, angle-derived settings, all ten arguments,
  allocation success/failure and the connected origin writer. The complete
  `func_15074C80` parent and gameplay remain outside this bounded claim.
- Native SDK32 O0/O2/O3 with UBSan trapping pass 262,144 cases per profile,
  covering all 65,536 low-halfword patterns, all selector/byte patterns,
  both allocation outcomes, external allocation effects, full coordinate
  arguments and all 640 record/canary bytes. The void result is not read.
  Fourteen IDO and native negative controls fail by explicit semantic
  comparison; compiler/interpreter/sanitizer failures are rejected.
- Whole raw/padded owner compilation preserves four neighbors and all
  pools with zero diagnostics. The actual three Make commands produce the
  qualified object exactly.
- Independent full-image prediction equals first link and production ELF:
  184 changed bytes = 183 target code bytes + one target symbol extent
  byte, with no metadata permutations or excluded ranges. All 6,055 other
  bodies and all 6,056 addresses remain fixed. Protected Game data remains
  exact across 189,088 bytes and 720 owners.

Production ELF SHA-256:
`e269ee9d742947ddf7c03f010390773904c4b44628202386fedd6878695b9821`.
The map and C inventory CSV remain unchanged. Receipts and immutable inputs:
`conker/build/game-double-quad-effect-15166118-match/`.

## Progress and continuation

The actual adopted ELF recount is **3,993 / 5,506 (72.52%)** exact C,
Game **3,320 / 4,833 (68.69%)**, Init 492/492, Debugger 181/181, with zero
address drift. The threshold remains 4,130; **137** more verified functions
are needed for 75%. Conversion inventory totals do not change.

Next screen: `func_1501DE18`. Tools are committed before consumer source/guards/pin/
docs. The eleven-file graph update preserves prior nodes and valid directed
relationships, retiring the two obsolete signed placeholder return edges.
No full-corpus extraction, global clustering, push, host-port or Release
work is claimed.
