# Working Note 2082: Game effect descriptor preset direct match

Date: 2026-11-04

## Result

`func_150D64E8` at `0x150D64E8`, ROM `0x103998`, replaces its zero-return
placeholder in `generated_1028F0.c` with a semantic two-pointer initializer.
Natural IDO `-O2 -g3` emits all **66 retail words / 264 bytes directly**, with
no frame and **zero guards**. The recovered interface is:

```c
void func_150D64E8(EffectPreset150D64E8 *preset, f32 *auxiliary);
```

The typed descriptor records its known widths and offsets. Unestablished
field meanings retain offset-based names rather than speculative labels.
The function sets kind/variant `6/3`, writes five live float globals into the
auxiliary output and descriptor, installs the original fixed float, word and
halfword values, then sets byte `+0x50` to `-1` when signed `D_80082FA0 >= 2`
or signed `D_8008FD8C >= 8`, and to zero otherwise. Bytes `+0x08..+0x13` and
trailing structure padding `+0x51..+0x53` remain untouched.

The first source shape already matched the opening 55 words. Expressing the
last predicate as the rejection disjunction restores retail's branch layout;
the acceptance conjunction remains a six-difference source-shape control.
No instruction or guard normalizer is involved.

## Reference and reachability boundary

The complete decompressed retail image has no direct `jal` or aligned-pointer
literal referencing `0x150D64E8`; source/assembly searches agree. Graphify's
predecessor node contains only its file-containment and placeholder type
edges. Its argument contract is therefore inferred from the complete retail
routine, with no caller execution claim. Computed or external reachability
remains unknown. This static limitation does not alter the measured match.

Public execution reaches 65 words. The store at `0x150D65E4` (`+0xFC`) is a
structurally unreachable duplicate after a return and its delay slot. It is
retained byte-exact and is not counted as dynamically covered.

## Qualification

The candidate and installed source pass the same focused suite. The installed
run passes **4 tests in 33.986 seconds**:

- complete owner compilation, exact target words and all 14 original HI/LO
  bindings, 16 unchanged neighboring functions, unchanged pools, production
  owner identity and independent whole-ELF prediction;
- **8,960 guest cases** across seven signed counters, every one of the 256
  state bytes, and five auxiliary aliases: separate storage, two descriptor
  float fields, a later float global, and the counter global;
- all defined descriptor bytes, reserved-byte preservation, raw float bit
  patterns, signed thresholds and short-circuit routes checked against an
  independent memory reference;
- **24,576 native32 executions**: 8,192 each under O0/O2/O3, with the signed
  thresholds, raw float values, defined native aliases and structure extent;
- **28 effective semantic controls** for fixed values, global sources, signed
  comparisons, thresholds, predicate selection, mode and reserved writes;
- **140 fault observations / 29 unique active boundaries** and the bounded
  reference census;
- an out-of-target ELF corruption control rejected by the literal predictor.

The reused guest core lacks `lb`; a local signed-byte implementation supplies
that exact opcode without changing the shared model or production source.
All guest checks pass after this model addition. Fault probes qualify emitted
guest access order, not portable C fault behavior or runtime reachability.

The standard shared match-progress, PC16, guarded-object and protected-data
suite passes **19 tests in 8.175 seconds**. `make tools-check` passes. The
sibling `64CBFD Tools` checkout at `ddbdd16b` contains extensive prior dirty
work and was preserved; this target's new tools are qualified and banked in
the consumer's tools submodule only. Routine work used zero Claude calls.

## Strict image and production proof

All **6,052** linked function addresses remain fixed; the only changed body
is `func_150D64E8`. The full ELF is independently predicted without exclusions:

- **211 instruction bytes** change inside the declared 264-byte target span;
- the named target symbol extent changes from 12 to 264 bytes;
- three closed adjacent GNU symbol/string order swaps account for the other
  metadata differences: `D_800A0AC8` / `D_8009EC34`, `func_15192308` /
  `D_8009E5D4`, and `D_8008B374` / `D_8009E5D0`;
- **79 metadata bytes**, including the target extent, change; **290 total**
  ELF bytes change. Exact reconstruction proves all other bytes identical.

The fresh production owner and ELF equal the independently qualified
artifacts. All **189,088 protected Game-data bytes / 720 owners** remain exact,
SHA-256 `0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.
The guard registry, progress CSV and Makefile remain byte-identical to their
frozen predecessors. Production Make compiles the owner, postprocesses its
existing assembly, pads and links it, then `make all` produces the image and
stops only at the expected retail SHA-1 mismatch. The inherited duplicate
`generated_12D630` recipe warning remains.

| Artifact | SHA-256 |
| --- | --- |
| Natural compact target | `34338181599fa21ee599fb9d25b68ee51208b437819d83fe6f983b9a82addd9d` |
| Linked target / retail span | `1f121928a2a24315de766cdea26184984c3fe753588d4297dcc12187cbd9312e` |
| Qualified / production owner | `3ec751a6888d9410baf9d88078174904ecdf720a473c8abd8e9cd2f93459e906` |
| Predecessor ELF | `a2d33316086de8de82d5ff347c247042f2a22513323ab052c828a9e711faae37` |
| Qualified / production ELF | `1bf15eaf5cd81203aac76f30c50e7bd0819b1c99c1e279807502036e280ca388` |
| Production code image | `7024534063f4e9f1fe92e3cd5841f0716a2365183f13f17375a1f067f86c6385` |
| Production map | `2ab021cc02cab424a5dae0e96a4ed5df1fe5f65ea58964f8e4e04b689771fbeb` |

Reproduce with `python3 -m tools.experiments.game_effect_descriptor_preset_match`
and `python3 -m unittest tools.tests.test_game_effect_descriptor_preset_match -v`
from the consumer root under the prepared WSL toolchain.

## Production recount and continuation

| Section | Exact C functions | Address drift | Different |
| --- | ---: | ---: | ---: |
| Total | **4,153 / 5,512 (75.34%)** | 0 | 1,359 |
| Init | **492 / 492 (100.00%)** | 0 | 0 |
| Game | **3,480 / 4,839 (71.92%)** | 0 | 1,359 |
| Debugger | **181 / 181 (100.00%)** | 0 | 0 |

Converted inventory remains 5,512 / 6,046. The active 80% target is 4,410
exact functions: **257 more** are required. Continue at ordinary candidate
`func_15107E48`, then rerank from the production ELF. Keep the seven documented
custom-ABI/compiler cases (`func_150A76F0`, `func_151F8870`, `func_150A613C`,
`func_150AE280`, `func_15115F68`, `func_151AE2BC`, `func_150A6760`) separate.

## Graph retention

Baseline: **58,571 nodes / 112,343 links / 5,093 communities**, graph SHA-256
`2cd2ab45fc652706bf61c403a3a5e7e3d91ae0aef39066bb1b9728b5cc3a27b3`.
The standard reduced update extracted eight uncached paths but proposed only
24,778 nodes, so it correctly refused to overwrite the retained graph. Its
corpus warning accounts for 31,816 retained nodes from 3,754 still-present
files outside the reduced scan.

The explicit seven-path rebuild with `force=False` produces **58,580 nodes /
112,350 links / 5,118 communities**. It retains **58,568 / 58,571** prior IDs,
with **zero removals outside changed paths**. The three replaced IDs are
line-derived Update Log nodes; twelve new IDs comprise their relocated forms,
the eight Note 2082 nodes and the descriptor type. This is an incremental AST
refresh with no semantic LLM calls, not a new full-corpus extraction.

Qualified graph SHA-256:
`6f178743025e435310352bfda4366c8783239beacf3531afcba5e5ddab90d6cf`.
The final note's one-path stabilization detects no topology changes and
leaves every qualified node and link untouched.
