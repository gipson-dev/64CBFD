# Game particle display callback guarded match

Date: 2026-11-14. `func_151770C8` is recovered in
`conker/src/game/generated_1A20A0.c`. All **101 words / 404 bytes** match
retail after **four independent cursor-scheduling guards**. The semantic
source already emits the original **0x90-byte frame**, saved registers,
private matrix/view homes and all 97 other words directly. Owner now
**4 / 9 C-exact**. No neighboring function or prototype is changed.

VA **0x151770C8..0x1517725C**, ROM **0x1A4578..0x1A470C**.
Source and guard derivation are in
`tools/experiments/game_particle_display_151770c8_match.py`.
Raw SHA-256: `27857f7102944da3d881f3fb8b9c4a27ff9ef7dbf200ede920e4a902c5d54882`.

## Callback contract and source shape

The recovered signature returns `Gfx *` and takes commands, a private
248-byte particle record view and a signed-halfword view. The third O32
transport word is homed at incoming SP+8; both actual uses read its signed
low halfword. The later delegated call rereads that home after culling.
There are no direct JAL callers. Registry slot **0x8008B88C**, ROM
**0x23034C**, names this callback. The original generic dispatcher invokes
it through its eight-word window at **0x15167898..0x151678B8**.

The ten-word culling packet supplies the selected 64-byte view matrix,
three particle position words, `D_800D9B20`, **4000.0f**, the two projection
scales and two null output pointers. Rejection returns the input cursor.
The state byte is read after the culling provider, not captured before it.

State zero calls `func_150A8050` for the rotation matrix, overwrites only
matrix row 3's three position components, and converts all sixteen words
with `guMtxF2L`. The provider's remaining matrix word is preserved. The
matrix destination uses the live page byte, and the emitted matrix command
rereads that page after conversion. Three SDK graphics commands load the
matrix, set segment 1 from `D_800DDE80[51]`, then call the display list from
`D_800DDE80[53]`. States 1, 2, 3 and every other nonzero byte delegate to
`func_15176DF0`, transporting commands/record/signed view and preserving its
returned O32 cursor word.

The delegated renderer remains an unrecovered placeholder. Its body and
old-style declaration are unchanged; the caller explicitly converts the
32-bit cursor result to `Gfx *`. Giving that placeholder named parameters
made IDO add unused-argument home stores, so those draft prototype edits
were rejected. The real three-word call is independently qualified here;
recovery of the delegated body is the next target.

A simple state-zero if/else loses the original switch shape. The explicit
zero/1/2/3/default switch and outer non-rejected block retain all 101 words.
A real `Gfx *packet`, used for the final display-list macro, recovers the
original frame and matrix at **SP+0x50**. No padding local or frame guard
is introduced. Direct macros alone produced frame 0x88; moving increments
after the macro reduced the body to 99 words. Those alternatives stay
private under the ignored target build directory.

## Four-word derivation

The raw body and all **18 named bindings** are pinned. All **119 altered
word/binding controls** are rejected. The normalizer reads no retail body
and rotates only this sequence at **0x14C..0x158**:

```text
source: S1 += 8; LUI T8,DE00; store T8 at A0; load T9 from model table
retail: LUI T8,DE00; store T8 at A0; load T9 from model table; S1 += 8
```

A0 already holds the final packet at 0x144. The three intervening words
neither use nor define S1. The final payload store remains at 0x15C, so
all memory accesses retain their order, including aliases of the command
buffer and the model table. No call, branch, opcode, register assignment,
constant, named binding or stack home changes. Exactly four expected-word
rows are appended; the previous guard history stays byte-identical.
Raw instruction-fault register order is not claimed; the actual guarded
stream is compared with retail at every qualified prefix.

## Completed qualification

- [x] **1,219 independent guest cases** across retail, raw C and the actual
  guarded object compare complete public bytes, helper packets, return
  cursors and sixteen-word matrix snapshots. They include all 256 state
  bytes, signed/packed views, page extremes, provider mutations and two
  stack phases. Providers clobber caller GPR/FPRs and outgoing homes.
- [x] Command buffers alias particle positions and the model table in guest
  probes. The segment/list payloads observe the preceding opcode stores
  when those addresses coincide; no read/write order is waived.
- [x] **80 executions through the original registry dispatcher window**
  verify all three arguments, bookkeeping and saved registers. This is the
  actual callback boundary, not a fabricated direct caller.
- [x] **122 target-memory prefixes** compare full guest memory, GPRs,
  FPRs, HI/LO, calls, matrix observations, traces and delay-slot state for
  retail versus guarded code.
- [x] **376 native32 cases per optimization profile**, O0/O2/O3 with
  undefined-behavior traps, compare all 248 record bytes, 128 command bytes,
  shared fields/model-table words, helper packets and the complete matrix
  snapshot. Five effective controls reject the far plane, page stride,
  state gate, segment field and final display-list field.
- [x] Both complete-owner padders pass **four independent GNU layouts**
  and twelve links, including function/data rebases and low-half carry/sign
  boundaries. The named SDK helper is rebased as code. All nine owner
  functions/pools agree between the padded/guarded objects.
- [x] Actual Make's three recipe commands reproduce the independent owner.
  Full-image prediction, installation, production rebuild/audit and fresh
  actual-ELF recount pass. Post-install suites pass in mounted tools and
  the isolated sibling overlay; shared `make tools-check` passes.

The corpus visits **100 / 101 retail words**. Offset **0xB4** is the
unreachable duplicate angle load; all 101 words are still compared
literally and covered by corruption controls. Native checks use views 0..3,
pages 0..1, distinct command storage and ordinary provider mutations.
Packed/negative views, sparse pages, command aliases and incoming-home
writes are guest-only probes. Providers remain bounded models; no full
trigonometric/conversion implementation, emulator, hardware or host-gameplay
acceptance is claimed.

Reproduce at the prepared consumer checkpoint:

```sh
PYTHONPATH=. CBFD_CONSUMER_ROOT=. python3 -m unittest tools.tests.test_game_particle_display_151770c8_match -v
make tools-check
```

Preserve the ignored target `production-baseline` fixture for replay.
The isolated overlay copies **five byte-identical task files**, uses sibling
dependencies with mounted fallback, and changes no sibling files. Its HEAD
remains `ddbdd16b53ce60b054fb6e11bf0649a41f48375a`; all **2,439** dirty paths and before/after
status SHA-256 `a3b1d31058efd5c8483ee15ece0d00b39f54bdfce5b08a8c64838636db14e0fb` are preserved. Routine Claude calls: zero.

## Linked image and measured progress

The production ELF exactly equals the independent prediction. All
**6,051 function addresses** remain fixed; only this body's slot and its
12-to-404-byte symbol extent change. Exactly **334 bytes** differ, with
**zero exclusions** and **no metadata permutation**.

All **189,088 protected bytes** across 720 owners remain exact. Only
`generated_1A20A0.c.o` changes among **698 objects**, in `.text`, `.rel.text`,
`.symtab` and `.strtab`. Its other eight functions/bindings and pools stay
fixed. All **82 headers**, conversion rows and **802 other frozen inputs**
are unchanged; source/object/ELF/guard changes are explicitly verified.
The registry data is an additional frozen input in this 806-input baseline.

Production ELF SHA-256:
`2a3b004fed599daef31da3fa185bc62cd70b88a2730b1decea2b1676bb044b12`.
Fresh actual-ELF count:

| Section | Byte-exact C functions | Address drift | Still different |
| --- | ---: | ---: | ---: |
| Total | **4,489 / 5,515 (81.40%)** | 0 | 1,026 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | **3,816 / 4,842 (78.81%)** | 0 | 1,026 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

One new C match is credited. Converted functions remain 5,515 / 6,048;
the converted-byte percentage remains 86.17%. **199 more matches** reach
85% at this denominator; keep the wider goal active.

Scoped Graphify AST refresh covers five tools files and the owner. All
**60,762** old IDs are retained: **60,797 nodes /
114,365 links**, zero lost nodes. This is not full-corpus extraction.
Tools commit `dec37389312e2b7b38aa7854efa678a532779837` precedes the consumer commit. Root README changes
are aggregate rows only; no push. `64CBFDOGL` has no source checkout here;
no host build/adoption is performed, and Release remains frozen.

Next focused target: **182-word `func_15176DF0`**, the renderer delegated
to by this callback, at VA **0x15176DF0..0x151770C8**, ROM
**0x1A42A0..0x1A4578**, frame **0xD8**. Recover its model/variant gates and
matrix/material paths, then qualify the real connection from this callback.
Use the production SHA above as the next baseline.
