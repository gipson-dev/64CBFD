# Interpolated callback return normalization: private screen

Date: 2026-11-12. Follow-up to [Note 2310](2310-game-interpolated-callback-dispatch-and-return-20261112.md). The three candidates are uninstalled and uncredited.

Two explicit-return C shapes were screened in the real owner. Both preserve the
79 non-target functions in the normal-profile primary object. The target-only
O2/g0 object cannot replace that primary owner wholesale.

* Returning the updated cursor parameter generates 114 words per function. A
  private 50-row expected-word map per function produces the complete retail
  113-word body. Each map omits the compiler-generated `lw v0, 0x60(sp)` at
  source offset `0x198` and moves four relocation positions. Other changes
  cover prologue/epilogue ordering, temporary register allocation, and loop
  scheduling. Omitting the reload changes the count-zero return: the source C
  returns the cursor, while the resulting retail instructions preserve incoming
  `v0`. This is a behavior correction, not merely a scheduling change, and the
  unnormalized C cannot be claimed to reproduce retail for that case.
* Keeping a separate `current = cursor` local and returning it generates 113
  words, with 58 directly matching positions and 55 word/relocation mapping
  rows per function. This C also differs from retail for count zero. It passes
  the bounded positive-count caller and finite native return screens, but has
  not been adopted or normalized for production.

The source arrangements were screened with all six pointer-declaration orders
and with/without the separate cursor local. For the 113-word local variant, the
private guest screens pass 256 finite cases, 576 additional overlap layouts,
408 external access-cut prefixes, and 96 three-call negative-count prefixes
per function. The 80-case original dispatcher-window screen and 96 finite
native cases per function at O0/O2/O3 also pass, including the returned cursor.
Wrong-weight and wrong-mode native controls fail. These are bounded screens,
not proofs of full caller execution, arbitrary aliasing, hardware faults,
floating-point exceptions, or defined C behavior for negative counts.

For the 114-word parameter variant, both padder implementations produced the
same object and all 82 owner functions agreed; the generated-padder test used
a synthetic slice derived from the retail layout, with no jump labels. The
three emitted function bodies compare byte-for-byte to independently assembled
retail. Expected-word and relocation corruption controls were rejected, and a
wrong replacement was detected for each function. In 64 finite guest cases per
function, the normalized byte-identical code matches the retail return,
including preservation of incoming `v0` for zero count. That comparison follows
from the complete byte match and does not establish that the source C itself
has that behavior.

The private Make recipe executed eight commands and reproduced the same
independently predicted ELF as the earlier shadow: 1,081 changed bytes, zero
exclusions or address drift, and 189,088 protected data bytes unchanged. The
padded object SHA-256 is
`aacf10b2c2b855a08461abc5d52c7a97e536f2beba3debeb356827152e06fd55`;
the private ELF SHA-256 is
`14b2668dddcb106aa8f2dd7a4abb19fafb9848ea95d6ac7d23476356be4578fe`.
This is a shadow build, not an installed production result. The guards and
their complete register, relocation, alias, and fault behavior remain
unqualified; the padder controls do not prove dataflow correctness.

Ignored scratch receipts are under
`conker/build/game-three-interpolated-callbacks-screen/`, including
`return-permutations.json`, `return-experimental-map.json`,
`return-experimental-padded.json`, `return-experimental-make.json`,
`return_generated_pad.py`, `return_guard_controls.py`,
`normalized_return_state.py`, and the `*_return_local.py` screens. Scratch may
be cleaned; the summary above retains the outcome. The existing real helper
`func_1500AF08` remains a C stub.

## Connected retail-helper follow-up

Both raw explicit-return shapes were run against the actual retail machine
instructions of `func_1500AF08` in the bounded guest interpreter, rather than
the earlier modeled helper. For each shape and callback, 432 cases varied
positive counts 1..3, capacities 1/2/4/8, initial cursor 0/1/3, slots 0/1/3,
mode bytes 0/2, and mask values 0/15. The original and candidate callback
agree on return values, helper-call arguments, external memory, and external
access traces; an independently calculated cursor bound also agrees. The
helper is 187 words; 101 distinct helper instruction positions were visited.
The callback always passes zero as the helper's seventh argument, so the
randomized helper branch was not entered. A deliberately changed helper cursor
increment caused the first eligible candidate comparison to fail.

An additional 80 cases execute the original indirect-dispatch instruction
window with the 113-word local candidate and the connected retail helper:
28 cases for each of the first two callbacks and 24 for the third. The screen
covers the 20 selecting pairs from the five known table rows with four seeds
and compares the consumed cursor, slot counter, helper calls, and bounded
external state. This is still a modeled instruction window, not complete
parent or hardware execution, and does not exercise zero counts, hardware
faults, FPU exceptions, or the helper's randomized path. The real helper's C
implementation in the production checkout remains a stub.

The ignored reproducibility scripts are `connected_helper_local.py`,
`connected_helper_return10.py`, `connected_helper_bad_return.py`, and
`dispatch_connected_helper.py` in the scratch directory named above. No
source or match count changed as a result of these checks.

Next, establish a legitimate source-level contract for the zero-count path and
fully audit the proposed changes, including saved-register and stack aliases,
branch delay slots, floating-point exceptions, and the reachable caller domain.
Then build durable independent tests, qualify the tools copies and production
Make/full-image result, and recount only after adoption. The last verified Game
checkpoint remains **3,704 / 4,840 (76.53%)**, 168 matches short of 80%.
