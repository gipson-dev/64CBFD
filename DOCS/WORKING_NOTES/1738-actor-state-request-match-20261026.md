# 1738 - Actor State Request Direct C Match - 2026-10-26

The adopted Native ELF measures **3,815/5,506 exact C functions (69.29%)**,
Game **3,142/4,833 (65.01%)**, zero address drift and 1,691 different.
Only `func_1512B100` gains matching credit. Inventory and converted-byte totals
stay fixed; 315 more matches reach the 4,130-function threshold for 75%.

## Complete source and observed interface

`func_1512B100`, owner `generated_157840`, occupies VA 0x1512B100..0x1512B1B8 and
ROM 0x1585B0..0x158668. The complete routine has 46 body words, no alignment
word, a 24-byte frame and one saved RA. Its single argument is an actor pointer;
its output consists of actor writes or a handler call, not a fabricated return.

Capture the full signed word at actor+0x2C. Require its bits other than 0x100
to be nonzero and both global bytes D_800BEAC0 and D_800C3671 to be zero.
Only then choose between the handler and the state writes. The handler requires
that the original, unmasked type differs from 0x40, actor+0x84 has mask 0x8 set
and mask 0x200 clear, actor+0x23C is zero, and actor+0x5F0 has masks 0x80 and
0x40 clear.
Otherwise write halfwords 1, 2, 60 at 0x5F8, 0x5FC, 0x5FE, preserving 0x5FA and
all other bytes. Ineligible outer gates leave the actor untouched.

Preserve the individual short-circuit tests and the original type comparison:
0x140 must not be treated as 0x40. The u8 actor view keeps the known access
widths without changing the shared header; struct108's pad5F4[6] still spans
the unnamed 0x5F8 field. The existing func_1512AD54 placeholder is unchanged.
Do not infer that provider's implementation from the wrapper qualification.

Two aligned direct calls occur at ROM 0x15048C/0x1504B8, VA
0x15122FDC/0x15123008, in parent func_15122C5C. No aligned literal registration
is found in the complete reference image. That parent remains an unrecovered
16-byte compiled placeholder. Graphify locates the old target at
conker/src/game/generated_157840.c:L18; its stub return-type edge is not ABI evidence.

## Direct compiler and owner proof

The complete semantic C emits all 46 original words at the ordinary O2/g3
profile. Five bindings occur at offsets 0x10/0x20 for D_800BEAC0,
0x24/0x30 for D_800C3671, and 0x84 for func_1512AD54. Raw SHA-256:
9f0769a5dba59ee9f1a8901cb702b5d9bdc2eddecaada042fd06faa26f72fa14.
No guards, assembly body, instruction insertion/omission or compiler override
is added. Every existing guard-manifest byte is preserved.

All 14 neighboring bodies, bindings and pools are unchanged. The normal Make
compiler/padder/assembler reproduces all 15 compact functions and the entire
independent padded object. Owner diagnostics are empty; the inherited
generated_12D630 duplicate-recipe warning remains unchanged.

## Focused qualification

Both canonical tools copies pass six fresh methods and their shared tools
checks. After installation, each copy runs two fresh input/image checks and
reuses four unchanged semantic checks only with exact module, frozen-input
and qualified-artifact fingerprints.

- 8,192 guest cases cover full-word types/flags, both global gates, the status
  byte, state bits, two stack phases and bounded provider clobbers/effects.
  Another 768 cases sweep every value of each global/status byte. Eighteen
  fixed-global/actor aliases compare with an independent byte-addressed
  reference. All 46 body words execute. Nine lazy-read cases remove backing
  that must remain unused, including output backing on the handler-only path.
- Forty-nine fired guest access prefixes compare complete original/C states.
  Native O0/O2/O3 each run 4,096 cases with trap UBSan and full State canaries.
  The native harness declares and asserts the exact word/halfword offsets in
  a local typed actor layout; it does not write halfwords through a word array.
  Thirteen compiled semantic negatives fail with the intended status 23.
- Execute both actual six-word caller windows in 864 cases. Each contains
  the target JAL, A0=S0 delay-slot copy, and the next two calls with the same
  actor forwarding. A declared JR S7/NOP adapter ends the bounded window.
  RA is excluded only at that synthetic boundary; the actual target's saved
  RA and return are still executed. Verify S0/SP and complete original/C
  states. Seven distinct unused V0 values reach the next call, supporting the
  void interface. This is not full-parent or post-provider qualification.
- Six independent GNU links and 972 rebased semantic cases relocate code,
  helper and both byte globals across signed low16 carries. All five bindings
  and all 46 words agree. Seven strict full-image corruptions, including
  file extent and a neighbor boundary, are rejected.

The original private fixture failure is preserved. It reused self.mode,
which inherited MaskOracle initializes to zero, while the independent
reference expected mode 1 effects. A first-failure diagnostic reproduced the
mismatch in both original and C code. The corrected state_effect_mode field
is distinct from the base oracle's field. No production body changed for that
fixture correction. Packaging also exposed a caller-test local-name collision;
that failed execution is preserved and the loop variable is corrected.
Canonical executions run all six packaged methods freshly in both copies.

Provider effects are bounded contracts, not emulation of the large handler,
full parent, gameplay or hardware fault semantics. Native cases use valid
aligned objects; fixed global/actor overlaps belong to the guest checks.

## Production and committed continuation

Production Make exits zero in 5.979s and reproduces independent
ELF 93b75e6065f9e162c33df5549b84b80b4c431f51ada713570d1eec77b2d9cabf. The complete delta is **142 bytes: 141 target-code bytes and one
symbol-size byte, zero exclusions**. Target extent changes from 12 to 184.
Preserve all 6,056 addresses, 6,055 other bodies and exact protected Game data:
720 owners / 189,088 bytes, SHA-256
0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670.
No symbol/string serialization allowance is used.

Source SHA-256: 6a00b7dfc39bac9f549d2d4d801a2fade3ebb0f880b0537590400c7665a29bc2.
Padded object SHA-256: f168653c0941f999d905d5bbe2b96d5cb912547683b6d4e3112039e42e70814c.
Baseline consumer b4bbbddf, tools 3626aca, ELF cddeb3c2.
Tools af1ffab1acd0103e5a1d9351b0b2ea4ef71b99ec are committed first and then pinned by the consumer.
The seal covers 16,119 Native inputs and exactly four qualified adoption outputs.
Preserve all 1,686 pre-existing dirty paths and the older mirror's history;
only the new pair is added there. No push or host/editor/Release work occurs.

The scoped native no-cluster graph update refreshes eight changed C/Markdown
files and must retain or uniquely relocate all 44,325 prior nodes. Preserve
historical manifest freshness outside that scope and prior community labels.
No global clustering, centrality recomputation or full-corpus extraction is
claimed. Tools AST extraction remains separate from the parent graph.

The adopted queue contains 1,562 placeholders, 120 semantic/other entries and
nine unlocated screens. Next screened placeholder is `func_151A8F6C` (`generated_1D4E00`),
uncredited until source/ABI, guest/native, owner/Make and production gates
close. The unresolved pointer/NULL factory stays a placeholder. The 75% goal
remains active. Routine Claude calls: zero.

Prepared-checkout focused command:

~~~sh
python3 -m unittest tools.tests.test_game_actor_state_request_match -v
~~~
