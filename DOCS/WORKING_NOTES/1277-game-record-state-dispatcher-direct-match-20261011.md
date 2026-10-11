# Game Record State Dispatcher Direct Match

Date: 2026-10-11. Recover complete func_1503DF48 in
conker/src/game/generated_6B320.c, replacing its zero-return placeholder.
VA 0x1503DF48..0x1503E1F4, ROM 0x6B3F8..0x6B6A4: 171 words / 684 bytes.
All 171 retail words emit directly from semantic C with the existing O2/g3
profile. No word guards, instruction drops, handwritten assembly or recipe
changes. Matching +1; conversion counts/bytes unchanged. Full Game goal active.

## Baseline And Contract

Consumer c4c3235618030fb012b5e6c1178907285efa4580 and mounted tools
3b4d8ecc89567eddf33a5edf3141dedbf055c553 were committed at entry.
[Note 1276](1276-game-actor-group-mask-command-direct-match-20261011.md)
left this genuine unmatched body as the next target, not its already-exact
27-word predicate. Query Graphify and inspect the complete retail routine,
owner types, direct caller and actual data tables. Reuse IDO 5.3, MIPS and
native32 fixtures, ELF/CSV/pool parsers, assembly processor and both padders.
Zero Claude calls: direct source/profile measurements resolve the scheduling.

Recover void func_1503DF48(s32 slot). Retail does not establish a return status;
the sole current caller func_1502BD84 ignores it. Correct only that caller's
declaration to void func_1503DF48(s32); its complete 88-word body remains exact.
Existing struct106 is 16 bytes, struct04 is 0x68, struct127 is 0x32C.
The guest buffer address remains the existing s32 record field, not a new
pointer/header type. Incoming slot stays full width, without new bounds gates.

- Read record state +0xF once. State two ORs actor +0x74 with 0x80, locally
  advances to three, and returns if actor +0x1D4 is NULL. Do not publish state
  three; the actor flag store still occurs on the early NULL exit.
- State three reads the unsigned group-count byte even with an existing
  buffer. Cache count across all callbacks. Missing buffer requests
  allocate_memory(count * 0x68, 1, 0, 0); NULL returns without publication.
  A successful zero-size request still publishes its returned address.
- Initialize +0x64 of each element using the cached returned buffer. Retail
  emits the ordinary loop as remainder-first / four-element unrolled writes,
  in order i+1, i+2, i+3, i for each four-element group.
- After allocation/clearing, reread group and cache its signed type-array
  base. Only signed -2 skips. Read bytes live; -1 and other negative types
  proceed. Compute the current element before calling func_1503E1F4(index,
  slot), then read its flag after the predicate. Predicate zero skips setup.
- Setup uses all five O32 arguments: func_1503E3C4(slot, index, 0, element, 0).
  Reread group after setup to select its element callback. Keep the already
  selected element across pointer mutations and write flag one after callback.
- Finish uses the live group callback, then publishes record state one even
  if that callback cleared it. Active callback selection rereads group;
  reread record state after active callback. A nonzero state gates both tail
  calls once: clearing it in func_1503EA54 must not suppress func_1503E82C.

Real tables have three groups with counts 27/31/45, signed type arrays and
separate element/finish/active callbacks. Their actual addresses/data are
qualified as inputs; callback implementations remain separate open bodies.

## Direct Source Shape

The initial flat conditional/cursor source gives 177 words / 177 differences,
frame 0x48 under the owner profile. Its compact diagnostic is 152/170; O1 is
194/189. An indexed signed-byte switch restores frame 0x38, all saved-register
lifetimes, the native unrolled loop and 171-word length, leaving two tail
scheduling differences. Writing local state one before the record-byte store
recovers both remaining words directly. The selected compact diagnostic is
153 words / 168 differences, frame 0x48; it is not installed. These are scoped
completed measurements, not an exhaustive profile sweep.

Original RA +0x34, S0..S5 +0x1C..+0x30, cached record/count/type base, element
call-delay update, fifth stack argument +0x10 and all branch-delay exits now
emit directly. Preserve the owner GLOBAL_ASM body and all retail assembly,
guards, layouts, symbols, conversion rows, recipes and shared headers.

## Fresh Qualification

New tools: experiments/game_record_state_dispatch_candidates.py and
tests/test_game_record_state_dispatch_match.py. Private immutable before-inputs
and receipts live under conker/build/game-record-state-dispatch-match-test/.
Update only the affected older dispatcher compiler/test fixtures for the void
contract. Its source-identity assertion now recognizes two previously restored
u8 argument casts; no new caller-body cast or behavioral edit is made here.

- Thirteen pre-install tests pass in 18.388 seconds. All thirteen installed
  tests plus nine affected caller tests pass in 26.656 seconds, 22 total.
- The 612-case state/allocation matrix exercises all state bytes and reaches
  all 171 target words. Run the complete actual 27-word predicate with its
  hook removed: 26 words reached, one unreachable duplicate zero remains.
- The 162-case count/type/mask/slot matrix compares retail/raw/padded forms,
  including 0/1/3/4/5/27/31/45/127/128/255 counts, signed -2/-1/-128 types,
  mask branches and unrolled write order. Invalid slots are mapped guest
  fixtures, not portable C bounds evidence.
- Thirty-two callback mutation cases preserve cached count/type-base/element
  and live group/pointer/flag/state reads. External hooks clobber all caller-
  saved GPR/FPRs. Include allocation mutation, pointer replacement in the
  predicate, setup/group changes, type-array changes and the one-time tail gate.
- Two independently linked placements remap twelve symbols, with HI16/LO16
  carries; 36 cases compare all three forms. The predicate is a boundary hook
  only for rebases; actual predicate execution is separately tested at retail.
- All 144 fired fault-prefix comparison pairs agree, including private and
  public accesses, events/registers/memory. This qualifies emitted guest
  instruction order, not portable C fault semantics.
- Six freshly compiled semantic controls fail effectively: wrong sentinel,
  lost actor flag bits, premature failure publication, late element selection,
  early element flag and repeated tail gate. Literal-audit controls reject
  source, target, neighbor, extent, symbol-value/string and guard corruption;
  stale/duplicate installers are rejected without mutating production inputs.
- Both complete copied owners pass production GLOBAL_ASM post-processing and
  both real padders: all 21 target-owner neighbors and 38 caller-owner functions,
  normalized pools, other slots/relocations and caller code remain exact.
- The actual complete 88-word caller executes the retail/raw/padded dispatcher
  and actual predicate, both hooks removed, in 24 cases. Allocation failure
  and active callback mutation preserve the caller's later live active gate.
  Other caller helpers, allocator, setup, callbacks and tails are bounded models.
- Native32 O2/O0 each pass 1,106 valid-fixture state/count/mutation cases;
  a sentinel mutation fails. Use a defined unsigned masked-shift predicate
  hook, not the existing helper C's shifts beyond its portable domain. Actual
  predicate evidence is MIPS-only; do not claim native helper portability.
- Forty-four guest alias/actual-table cases include element flags overlapping
  actor flag, record state/group and type byte, plus all three real count/type/
  callback tables. Mapped aliases are not portable C aliasing evidence.

Initial harness failures are corrected explicitly: a tail-index assertion,
missing coverage fixtures, a rebased hook address accidentally inside the
owned code, native logging bounds, and stale caller-source assertions. No
production workaround or refreshed baseline is used to make them pass.

```sh
python3 -m tools.experiments.game_record_state_dispatch_candidates --profiles
python3 -m unittest tools.tests.test_game_record_state_dispatch_match tools.tests.test_game_actor_update_dispatch_match -v
make -C conker -j4 build/conker.us.elf progress.csv
make -C conker match-progress NON_MATCHING=1
make tools-check
```

## Linked Audit And Checkpoint

Full rebuild exits zero. Exactly 562 ELF bytes change: 554 in this function's
684-byte slot, two function-size bytes (12 -> 684), and six bytes in the
explicitly verified adjacent absolute-symbol permutation D_80088730 /
D_80084430. Parse both records and strings, require their exact names/values/
attributes, and reconstruct only that fixed permutation. Every other ELF
byte, body/address/extent, symbol meaning and metadata entry remains literal
exact; no blanket metadata ignore or source/binary projection. Corrupting
either the permitted symbol value or string is effectively rejected.

All seven other assignment inputs remain exact: guards, progress CSV, rodata
assembly, symbol addresses, undefined functions, layout and Makefile.
Protected data: 189,088 bytes / 720 owners, zero differences, SHA-256
0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670.

| Input | SHA-256 |
| --- | --- |
| Target source before | b8430ca27296d5711b518bc5610a56e48618d16cd4285c2bf15418b16ebd67dc |
| Target source after | 2dec3adb58a154d8be55eade61a66857a381e1b45886d8c9d5cc75535b487d4b |
| Caller source before | c773916b3cd9e131e58429fa772fe687ef04ac2469a34bb7b706a1611207654b |
| Caller source after | e197450c5028644167943b0e0878ab200b463db3d6ce4fea466bda32f4b20162 |
| ELF before | 43c9d060b98cb1f8662d6d8e34f84eb9497cf0dfc4be19843595a03a422fac2f |
| ELF after | f529e1b3dbe2f252a309438b8a3e84bfb587d7f39db0199e48c8627569db62c1 |
| Guards unchanged | 2c86d53acedfcb94ac1e3fcd03bab86a3b0854c6813f07dfb080f415b26255a7 |

Fresh match-progress: Game 2,798/4,822 (58.03%), total 3,471/5,495 (63.17%),
Init 492/492 and Debugger 181/181. Zero drift / 2,024 still different.
Matching +1 only; root README updates aggregate rows, not function narrative.
Prior Note 1276 broad neighbor receipts are not rerun or represented as fresh;
the strict new literal audit proves those linked bodies remain unchanged.

Consumer/mounted/older tools shared checks and native py_compile pass. Bank
mounted tools 72fe85784a2d61bf53e174f110af7b6055f05485 first, then the two source
paths, this note, five current indexes, aggregate README and tools gitlink.
Older sibling HEAD ddbdd16b53ce60b054fb6e11bf0649a41f48375a and all 45 recorded
fingerprints remain unchanged. Copy only two absent new paths, identical
hashes: dirty count 322 -> 324. Do not overwrite its older dispatcher fixtures
or commit/reset/push that independent history. Function tests ran in the
mounted consumer, not standalone. Both active checkouts are to stay committed;
no push requested/performed.

Native graphify update . exits one on protective shrink refusal: 18,133
candidate nodes versus 39,913 saved; preserves 19,398 nodes from 2,972 existing
excluded files. No force/purge/install. Version/empty-source warnings are
separate from compiler diagnostics. Preserve the existing duplicate
generated_12D630 Makefile recipe warning. After consumer commit require a
fresh terminal Rebuilt, advanced log bytes/UTC and zero workers, not just
the hook-launch message; the precommit log is 533,788 bytes.

## Next Game Body

Live linked recheck: dispatcher 171 / zero differences and predicate 27 / zero.
Skip that already-exact predicate. Next func_1503E260 remains a placeholder:
89 words / 89 differences, VA 0x1503E260..0x1503E3C4,
ROM 0x6B710..0x6B874, same generated_6B320 owner. Recover its complete body
and callee contract before installation. The following setup func_1503E3C4
is also open at 141 words / 136 differences; this dispatcher's bounded setup
hook does not qualify that routine or prove gameplay behavior.

Third-loader's two final scheduling guards, parent/pair guard removal and
deeper SDK/allocator/heap/hardware/renderer/gameplay remain separate work.
No OGL Release build/change, private-input/save mutation or active editor/
debugger changes. Keep the full Game goal active; no completion claim.
