# Game Matrix Creation And Transform Setup Direct Matches

Date: 2026-10-08

## Result

Continue `func_150335C8` from
[Note 1118](1118-game-fourth-tile-scroll-direct-match-20261008.md).
Install complete semantic C for it and its previously empty final helper,
`func_15030D54`, in
[generated_5D2C0.c](../../conker/src/game/generated_5D2C0.c).
Both emit every retail word **directly** under existing IDO5.3 O2/g3:

| Function | Words /Bytes | Frame | Raw And Linked Differences | Previous Placeholder Differences |
| --- | ---: | ---: | ---: | ---: |
| `func_150335C8` | 113 /452 | 0x168 | 0 | 111 |
| `func_15030D54` | 45 /180 | 0x20 | 0 | 44 |

No guards, filler, generated data, compiler-profile, Makefile or shared-header
change. The seven caller calls and two helper allocator calls remain symbolic
R_MIPS_26 relocations. Actual copied-owner/padder/link qualification is separate
from the standalone compiler match.

Caller VA `0x150335C8..0x1503378C`, ROM `0x60A78..0x60C3C`.
Helper VA `0x15030D54..0x15030E08`, ROM `0x5E204..0x5E2B8`.
Retail: [5D2C0.s](../../conker/asm/5D2C0.s).

## Caller Contract

1. Preserve the node in S0 and the actor/kind/index in their incoming homes.
   Read the actor's matrix pointer at+0x1D4. A zero bank returns0 without
   accessing node fields or creating an object; the actor itself is required.
2. Call `func_15083568(actor, kind, 1.0f, 0)`. Read the full index from its
   home **after the callback**, even on a null result. Null creation returns0.
3. Write index's low byte to created+2, and copy node+0x14C to created+0x40.
   Incoming argument5 controls clearing or setting bit4 of created+0x16.
4. Reload the actor from its home and its matrix bank after creation/flag
   updates. Convert bank plus the **full signed word index times64**, not the
   byte stored in the created object. Retain the cached post-create index.
5. Convert/invert the selected matrix with `guMtxL2F` / `func_15048B10`.
   Build a node transform through `func_150A9B0C`, passing fields+0xB8,+0x40,
   +0xC4 and scales+0x14C,+0x150,+0x14C. Only the repeated horizontal scale is
   cached within this call; node fields are read again after earlier callbacks.
6. After the builder callback, copy node position+0x14,+0x18,+0x1C to row3.
   Set column3's first three entries to0 and the final entry to1. Multiply
   transform then inverse into the combined matrix, preserving operand order.
7. Decompose through `func_1503E5F8` into three position, three angle and
   three scale outputs. The scale outputs remain required private destinations
   although this caller does not consume them.
8. Read argument6's home **after decomposition**. When nonzero, clear all
   three position outputs to positive zero. Submit position/angles to the
   typed final helper and return the created pointer, including when that
   helper's internal allocation fails.

Private layout: created pointerSP+0x164; matricesSP+0x124,+0xE4,+0xA4,+0x64;
positionSP+0x60,+0x5C,+0x58; scaleSP+0x54,+0x50,+0x4C; angleSP+0x48,+0x44,+0x40.
This is measured compiler/retail layout, not original declaration-name proof.

## Helper Contract

The final helper's zero-argument s32 placeholder could not support a faithful
typed float call in the same owner. A block prototype conflicts with its
existing definition; a pointer cast compiles but emits an indirect call and
changes the retail shape. Recover the real helper rather than retain that bridge.
Its caller ignores the return, so the semantic C interface is void.

Always request `allocate_memory(24, 1, 0, 2)` and store the returned pointer at
node+0x44, even when null or replacing an existing value. Failure skips every
float store and the matrix-bank gate. On success, store the six incoming floats
at record offsets0,4,8,12,16,20. The compiler retains the first allocation result
for the first store, then reloads node+0x44 for every later store. An alias can
redirect later destinations; do not cache the record across all six stores.
Read float homes after the first allocator callback.

Only after those stores, read node+0x34. Preserve an existing bank; otherwise
request `allocate_memory(128, 1, 2, 2)` and store its result, including null.
No extra initialization, free, fallback or allocation-success return is added.

## Source Fit

[Caller driver](https://github.com/gipson-dev/64CBFD-Tools/blob/master/experiments/game_node_matrix_creation_candidates.py)
uses typed matrix/callback declarations, a positive creation guard/common zero
return, and the created-pointer declaration before four matrix arrays. These
recover all113 words/frame0x168 without instruction normalization. The retained
early-return control is C113/88 differences; ordinary-node is also direct.
Volatile-result is C119/101. O2 without g3 is C111/110; O1 with or without g3
is C134/frame0x158/133.

[Helper driver](https://github.com/gipson-dev/64CBFD-Tools/blob/master/experiments/game_node_transform_setup_candidates.py)
recovers all45 words/frame0x20. Expressing the first float destination through
the node's record field resolves12 temporary-register allocation differences;
the optimizer still eliminates that redundant first read. Ordinary-node and
early-return forms are also exact. O2 without g3 is C45/4; O1/g3 is C57/54 and
O1 is C57/53. Pointer/int allocator-result casts did not resolve allocation.

Together **24 measured forms**, **14 ordinary executions** and **ten effective
compiled negatives** cover cached banks/records, byte-truncated matrix indices,
flag direction, skipped position zeroing, reversed matrix operands, wrong
allocation class/size, swapped final floats and unconditional bank allocation.
No warning suppression or production-profile change was added.

## Qualification

[Eight tests](https://github.com/gipson-dev/64CBFD-Tools/blob/master/tests/test_game_node_matrix_creation_match.py):

- **10,058 caller guest cases**, all256 flag bytes, seven index patterns,
  fifteen binary32 patterns, four modeled callback mutation modes and two SP
  phases. Required live actor/index/position homes and post-builder position
  reads qualify. **112/113 words execute**; word31 is the unreachable duplicated
  flag-byte load bypassed by both retail routes.
- **961 helper guest cases**, including both allocator failures, existing-bank
  gates, mutable float homes/bank state and a valid record alias that overwrites
  node+0x44 during Y's store. All **45/45 words execute**.
- **480 connected guest cases** execute both actual C bodies and both retail
  bodies together; caller returns its created pointer even when helper allocation
  fails. Three lazy cases and **twenty fault prefixes** cover thirteen caller
  and seven helper required-storage failures, preserving prior writes/calls.
- **65,536 actual native32 executions** connect both complete semantic C
  bodies, all flag bytes, four valid matrix slots, optional position reset,
  null creation, both allocation failures and existing banks. Verify every
  input/object/record byte, bank word and callback/allocation argument.
- Actual full owner: **38 neighbors** and their relative relocations/useful
  pool identities unchanged; target bodies equal standalone output. The real
  padder emits both complete slots without padding/data. **Six independent
  links** qualify entry relocation and every symbolic call target rebase.

Matrix/creation callbacks and the allocator are bounded controlled test hooks,
not substitutes for fully qualified original callee bodies. Defined returns,
call ABI, ordered public accesses and memory qualify against an independent
reference; full GP/FP state and complete traces/memory agree C-versus-retail for
the selected bodies. Arbitrary private-frame aliases, complete matrix-library/
creation/allocator behavior, hardware, gameplay and PC-port acceptance stay open.

The first seven-test run takes31.589s: three passes/four fixture failures.
Correct the coverage expectation to word31 only, remove an invented first
record-pointer read from the reference, and seed the byte-index negative's
alternate matrix storage. The next eight-test run takes59.329s: seven pass,
native compilation rejects two unused fixture locals. Removing those locals
lets the standalone native test pass in1.954s. Production candidates are unchanged
by these fixture corrections; no diagnostics are disabled.

Post-install **28 focused tests pass in176.922s**, zero skips/errors/failures:
eight new, seven tile-scroll, three earlier owner/padder, four selection-binding
and six selection-scheduling checks. This run predates the extra seven helper
fault probes; the strengthened new suite is rerun separately. Ten shared padder/
word-patch tests pass in0.045s. ELF/progress rebuild, tools, Python syntax,
driver/owner/profiles and whitespace checks pass. Existing duplicate
generated_12D630 recipe warnings remain; no warning-free repository claim.
The final strengthened **eight-test run passes in48.566s**, zero skips/errors/
failures, including all twenty required fault prefixes and the native fixture.
Documentation validation: **101 documents /4,169 relative links /zero broken**.

```sh
python3 -m tools.experiments.game_node_matrix_creation_candidates --profiles
python3 -m tools.experiments.game_node_matrix_creation_candidates --owner
python3 -m tools.experiments.game_node_transform_setup_candidates --profiles
python3 -m unittest tools.tests.test_game_node_matrix_creation_match -v
make -C conker -j4 build/conker.us.elf progress.csv
make tools-check
```

## Linked Audit

Against `conker/build/game-node-tile-scroll-test/after.json`, retain all6,058
symbols /6,042 retail slots /sixteen overflow symbols. Only these **two targets**
change; **6,056 other bodies** and every address/extent remain unchanged.
The prior placeholder hashes and155 combined differences are explicitly checked.
`.init`, `.init_data`, `.debugger` and `.game_data` are unchanged. All720
Game-data owners /189,088 bytes remain exact, SHA256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.
All **11,144 guards** and the conversion CSV hash are unchanged.

Exact total **3,374/5,467 (61.72%)**, Game **2,701/4,794 (56.34%)**,
**2,093 different /zero drift**. Init492/492 and Debugger181/181 remain exact.
Both placeholders already counted as C; converted function/byte counts do not
increase. Root README changes only aggregate matching rows; detailed recovery
stays here and in the documentation indexes.

Next authoritative checkpoint:
**`conker/build/game-node-matrix-creation-test/after.json`**.
Ignored auditor/receipts live beside it; additional candidate/fit evidence is
under `game-node-matrix-creation/`, `game-node-transform-setup/` and
`game-node-transform-setup-{fit,source}/` in `conker/build/`.

## Next Work

Next local placeholder **`func_15033838`**, **100 words /400 bytes**,
**frame0x20**, VA `0x15033838..0x150339C8`, ROM `0x60CE8..0x60E78`.
Static inventory: node action+6, actor type+0x84 and attached state+0x31C
select modes4/6/5. A node+0x38 latch responds to attachment bytes/flags/counter
and calls `func_151026BC` or `func_151027E8`. This is **inventory only**, not
a qualified C or matching claim. Preserve its required reads and callback ABI.

Wider Game, resolver `func_15031070` and full callee/runtime qualification
remain open. No sibling source transplant, Release, save, runtime, hardware
or push action was required for this retail decomp checkpoint.
