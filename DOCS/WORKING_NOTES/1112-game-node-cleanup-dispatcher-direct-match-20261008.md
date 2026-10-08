# Game Node Cleanup Dispatcher Direct Match

Date: 2026-10-08

## Result

`func_15031C14` replaces its padded zero-return placeholder with complete
semantic void C. All **134 words / 536 bytes** match retail directly under the
existing IDO 5.3 `-O2 -g3`, MIPS2/o32 profile. Frame **0x38**; **129 previous
word differences become zero**. No word guards, instruction insertion, missing
body words, slot padding, profile, Makefile or shared-header edits.

Production: [generated_5D2C0.c](../../conker/src/game/generated_5D2C0.c).
Retail: [5D2C0.s](../../conker/asm/5D2C0.s), VA `0x15031C14..0x15031E2C`,
ROM `0x5F0C4..0x5F2DC`.
Continues [Note 1111](1111-game-node-action-dispatcher-direct-match-20261008.md).

## Recovered Contract

Resolve actor with `func_15083E90(node[0])`; a null result returns without
reading the action selector or final cleanup key. Otherwise switch on node[1].

| Selector | Action |
| --- | --- |
| `0x5A` | If actor+0x31C is nonnull, subtract 0xAA from state+0x1A6 as a wrapping unsigned halfword. |
| `0x90`, `0x8F` | Clear respectively masks 0x70 and 0xE00 in actor+0x9C. |
| `0x85`, `0x5E` | Clear mask 0x6000 in actor+0x9C. |
| `0x37`, `0x4B`, `0x4C` | Register `func_15033BDC`, node and actor through `func_1000FD38`; reread node[1] after callback, call `func_15100180(actor)` if now 0x37. |
| `0x49` | Submit command 0x10/event 0x29 through `func_151616D0` with the first private actor/group packet. |
| `0x5D` | Submit the second packet through `func_15147D64(packet,0x2E)`, then `func_151494E0(packet,0x2F)` with its saved pointer and potentially mutated contents. |
| `0x3D` | `func_151BD7F4(actor)`. |
| `0x1A`, `0x1B`, `0x5F`, `0x65`, `0x66` | `func_151D4668(actor)`. |
| `0x1D`, `0x82` | `func_151D747C(actor)`. |
| Other values | No action; continue to final cleanup. |

Read node[6] after action callbacks. Keys **0x16 / 0x63 / 0x89** invoke
`func_151027E8(actor)` then `func_151D4668(actor)`. Incoming node and private
cached actor are reloaded at their retail points, not frozen in saved registers.
No extra pointer/bounds/null policy is added.

The only observed direct caller, `func_15030158`, ignores V0 and immediately
loads node fields after the call. Recover a void API; selected guest V0 remains
retail-exact, including null resolution and incidental callback results. Native
qualification does not invent a defined C return for this void function.

## Private Frame And Annotation

Relative to allocated SP: saved RA+0x14; saved paired-packet pointer+0x1C;
second packet+0x24, first packet+0x2C; cached actor+0x34; incoming node+0x38.
The local packet layout is a 32-bit pointer followed by a group byte, padded
to eight bytes; native32 tests assert size and group offset.

An ordinary pointer expression makes IDO recompute the second packet address,
yielding **133 words / 55 positional differences**. An explicit volatile pointer
home, declared after the state local, retains the retail store/reload at+0x1C
and yields all 134 words directly. The first callback receives `&second`; the
second receives the saved pointer. This is a documented **matching annotation**,
not evidence that Rare's source used that exact volatile declaration.
Both packet contents and the pointer-home lifetime are tested independently.

No callback is permitted to use uninitialized packet tail bytes in these
fixtures. Arbitrary private stack aliasing, stack discovery from native C,
complete callback implementations and hardware execution are not claimed.

## Table Ownership

All **48 generated targets** equal the original table at **0x8009701C**, owned
by `asm/data/23B8A0.rodata.s`. The already-installed action dispatcher owns
55 earlier targets beginning at the fixed **0x80096F40** anchor.

The complete copied owner emits 412 useful pool bytes plus four final
alignment bytes, **416 total**. Cleanup starts at **offset 220**, replacing the
previous end alignment at that position. The existing Makefile anchor mapping
is reused; no Makefile or original Game-data edits. Padder keeps symbolic
HI/LO relocation addends and does not link the compact generated pool.
All 55 previous targets and all 39 neighboring functions/relocations remain
qualified. The action-dispatcher baseline-removal test now explicitly accounts
for the later cleanup pool's expected 220-byte packed addend shift while
preserving actual owner/offset identities.

## Qualification

[Driver](https://github.com/gipson-dev/64CBFD-Tools/blob/master/experiments/game_node_cleanup_candidates.py) and
[seven tests](https://github.com/gipson-dev/64CBFD-Tools/blob/master/tests/test_game_node_cleanup_match.py):

- Six pre-install tests: **110.238 seconds**, zero skips/errors/failures.
- Native32 test separately: **0.917 seconds**, zero skips/errors/failures.
- **51,200** selected guest cases: all 256 selectors, four cleanup keys, five
  counter states including null/wrap boundaries, five callback modes, two SP phases.
- **1,024** null-actor cases; selector/key reads remain lazy.
- Selected C and retail match raw V0, GP/FP registers, complete event traces,
  callback arguments/packet contents and external memory; saved registers,
  SP/RA are checked by the bounded ISA oracle.
- Callback modes cover in-place node mutation, incoming-node-home redirection,
  resolver-induced redirection, cached actor-home redirection and paired packet
  pointer-home redirection/content reads. Guest private-home mutation is an
  ABI-model check, not a native C aliasing claim.
- **133 of 134 words** execute. Index55 (`0x15031CF0`) is the unreachable
  duplicate actor-flag load preceding the branch-likely target, not an omitted
  body word. All 134 words match, including that duplicate.
- Nine required-storage faults preserve ordered public prefixes and partial effects.
- **30,720 native32** executions of the complete actual C body, all public
  object bytes and callback ABI, including callback-mutated packet reuse.
- **13 source/profile controls / 3,328 ordinary executions**, two raw exact
  forms. Other controls qualify ordinary public effects only, not all raw V0,
  private homes or ordered reads.
- Four compiled semantic negatives catch counter direction, flag direction,
  missing final cleanup key and incorrect paired event identifier.
- Strict copied-owner compilation has zero diagnostics; 39 neighbors, 55
  existing and 48 new table identities qualify. Actual padder yields 536 bytes,
  no padding, no generated data; 12 symbols rebase independently, plus entry
  rebase and HI/LO carry boundary. The callback-address HI/LO pair stays symbolic.

All **66 installed cleanup/action/attachment/lookup/key-fit/resolver regression
tests pass in 439.488 seconds**, zero skips/errors/failures. Both original
matrix-wrapper connections and prior alias/home/native/owner/padder gates
remain green. `make tools-check`, Python syntax, driver CLI and whitespace
checks pass. Documentation validation checks **94 documents / 4,076 relative
links / zero broken links**. No complete-callee/hardware/PC-port claim.

```sh
python3 -m unittest tools.tests.test_game_node_cleanup_match tools.tests.test_game_node_action_match tools.tests.test_game_attachment_copy_match tools.tests.test_game_attachment_progress_match tools.tests.test_game_matrix_parent_lookup_match tools.tests.test_game_matrix_pair_resolver_key_fit tools.tests.test_game_matrix_pair_resolver_recovery -v
make -C conker -j4 build/conker.us.elf progress.csv
```

## Linked Audit

Compare against `conker/build/game-node-action-test/after.json`:

- **6,058 linked symbols / 6,042 retail slots / 16 overflow symbols**.
- Only `func_15031C14` changes; **6,057 other symbol bodies / 6,041 other
  retail slots** unchanged, all addresses and extents unchanged.
- `.init`, `.init_data`, `.debugger`, `.game_data` unchanged.
- All **720 Game-data owners / 189,088 bytes** exact. SHA256:
  `0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.
- All **11,063 guards** and conversion CSV hash unchanged; target has none.
- Exact total **3,369/5,467 (61.62%)**; Game **2,696/4,794 (56.24%)**;
  **2,098 different / zero address drift**.
- This was an already-counted C placeholder, so converted counts/bytes do not change.
- Root README changes only aggregate matching rows, preserving its thumbnails.

The build succeeds; the pre-existing duplicate `generated_12D630` Makefile
recipe warning remains. Target isolated/copied-owner compilation is clean;
this is not a claim that the whole repository build is warning-free.

Ignored receipts: `conker/build/game-node-cleanup-test/{slot,guest,gates,controls,native,owner,padder,installed,audit}.json`.
Authoritative next baseline: **`conker/build/game-node-cleanup-test/after.json`**.

## Resume

Next local placeholder: **`func_15031E7C`**, retail 83 words, frame-free,
VA `0x15031E7C..0x15031FC8`, ROM `0x5F32C..0x5F478`. Begin with its null
actor-source/node-table gates, actor type 0x55/0x56, inclusive float progress
range, four signed-byte sentinel scans and truncating writes. The intervening
`func_15031E2C` already matches all 20 words with twelve existing guards; it
is not a new direct match and needs no placeholder recovery. Do not introduce
a scan bound or new null/bounds policy without retail evidence.

The broader Game matching goal remains active. Resolver `func_15031070`
stays C84/frame0x20/40 differences with the missing V0-to-A1 key move; matrix
wrapper/basis/translator/sampler, complete cleanup callees, hardware and
PC-port runtime acceptance remain open. No sibling Release/save/runtime work.
