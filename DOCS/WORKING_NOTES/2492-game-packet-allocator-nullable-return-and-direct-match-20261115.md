# Packet allocator nullable return and direct match - 2026-11-15

`func_15167D84` now returns its nullable allocated packet pointer in C and
emits all **34 retail words directly**, with its original **0x28-byte frame**.
Thirteen old normalization guards, including two inserted instructions, are
retired. This is an interface repair for an already matching function and
earns **zero new matching credit**.

The fresh linked count remains **4,515 / 5,514 (81.88%)**, Game
**3,842 / 4,841 (79.36%)**, Init **492 / 492**, Debugger **181 / 181**,
zero address drift, 999 different. The active 85% goal still needs **172**
additional exact C functions at this denominator. Source conversion remains
5,514 / 6,048 (91.17%), covering 86.19% of function bytes.

## Why this interface repair is necessary

The next emitter, `func_151A11E4`, calls this helper at `0x151A16CC`, tests
the returned pointer and, on success, copies 34 curve bytes to `result+0x50`.
The provider definition and the declarations in `generated_17CAF0.c` and
`generated_1CC440.c` incorrectly said `void`. The installed guarded MIPS
already retained the pointer, masking the incomplete C interface.

The recovered signature is:

```c
u8 *func_15167D84(void *packet, s32 alternate, s32 extraBytes,
                 s8 marker, u8 mode, s32 owner);
```

The helper selects allocation kind 5 for zero `alternate`, 0x42 otherwise,
requests `extraBytes+0x50` with the original owner and byte mode, and returns
the allocator's pointer on both paths. On success, it uses overlap-safe
`bcopy` for the 56-byte header at `result+0x10`, then writes the marker byte
at `result+0x48`. An explicit early null-pointer return recovers the retail
control flow naturally. Argument names and the short source comment describe
that behavior without renaming the retail symbol.

This supersedes [Note 139](139-game-record-copy-builder-match-20260926.md)'s
claim that the old C behavior was complete and its 13-guard normalization.
Existing callers that discard the result remain valid and compile identically.

## Qualification

The retained 895-input baseline is from consumer
`c41ecf0c979010d717250a5ed1b9631797f28941` and tools
`c66c9a5fbc208580838ac1af723862be228b45b7`. It remains immutable. Only six
frozen production inputs change: three C files, the guard table, the provider
object and the ELF. Both caller objects reproduce their predecessor bytes.

Maintained qualification is in
`tools/experiments/game_packet_return_15167d84.py` and
`tools/tests/test_game_packet_return_15167d84.py`. Run from the prepared
consumer root under WSL:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest tools.tests.test_game_packet_return_15167d84 -v
```

Four tests pass freshly before installation, through the isolated sibling
tools overlay, and after installation. Each tools configuration covers:

- All 34 helper instruction addresses across allocation failure and success;
  3,072 guest executions compare recovered and retail helper code and execute
  the original ten-word emitter return/copy window.
- Overlapping header sources on both sides of the destination and exact
  self-copy; allocator mutations before the copy; an opaque copy provider
  that clobbers caller-saved registers and returns an arbitrary value;
  marker ordering; stack phases; full-width selectors and owners; byte modes
  and signed markers. Guest arithmetic includes size wraparound.
- Another 96 guest cases under three independent allocator/copy rebases.
- Native32 C at O0 and O2, 8,192 defined cases per optimization with undefined
  behavior traps. The native domain avoids signed size overflow. It covers
  all 256 byte modes/markers, both allocation outcomes, four alias placements
  and four mutation combinations. Wrong return, marker offset and copy length
  controls fail effectively.
- Fail-closed raw-word and relocation fingerprints, plus a guest result
  corruption that the public return expectation rejects.

All three complete raw owners preserve their other **121 functions** and
constant pools. The provider's five pre-existing warnings are unchanged after
mapping only equal source lines and disposable filenames; no new diagnostic
is accepted. All three whole-owner layout padders preserve their neighbors.
The independent strict padder covers the helper's target-only 34-word span,
reconstructed explicitly from immutable retail annotations because its old
assembly source is absent. This is not a whole-owner strict-assembly claim.

The allocator, `bcopy` and `memcpy` are bounded opaque services in these
tests. The ten-word emitter window establishes this return/copy contract;
it does not qualify the complete 350-word emitter, its dispatcher lifecycle
or gameplay. No host runtime acceptance is inferred.

## Production audit

An independent shadow executes 13 actual Make recipe commands across all
three owners and predicts the complete linked image. Production Make then
rebuilds the installed source, objects, ELF and progress CSV without copying
prebuilt objects. The shared guard file is treated as old for dependency
scheduling only; the affected owner recipes read the new table, whose sole
change deletes this function's 13 guards. All other table bytes stay fixed.

The production ELF equals the independent prediction. Its sole difference
from the predecessor is **one byte of symbol-size metadata**, changing this
helper's extent from 132 to 136 bytes. All **6,051 loaded function bodies**
and addresses are identical, all **698 objects** are audited, and only the
provider object changes. The 189,088 protected bytes remain exact, SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.
There are zero image exclusions and no progress-classification changes.

Production ELF SHA-256:
`cf64bd4fe6af66a1d950c1b4b8f54be54a0420a584f82cc8f5bd7113d6e675fc`.

The retired rows and their original header are retained privately at
`conker/build/game-next-151a11e4-private/return-abi-qualified/retired-guards.csv`
and permanently recoverable from the recorded predecessor commit. Other
receipts, the literal image prediction, native fixtures and the immutable
baseline are in the same target stage. `make tools-check` and diff checks
pass. Unchanged historical neighbor semantic receipts are reused only for
unchanged bodies; this note records fresh owner and full-image checks.

## Sibling, graph and next boundary

The sibling `64CBFD Tools` checkout remains at
`ddbdd16b53ce60b054fb6e11bf0649a41f48375a`, with its 2,434 dirty paths
untouched; its Windows status digest remains
`a3712de44f2fc37079df4a789a5015f134f6ab977a2c2da90a3fde1851606cd9`.
The two task tools are tested in a private overlay over that configuration.
The current `64CBFDOGL` path contains retained capture folders, with no
maintained source checkout to update. No host build, Release or save is touched.

Graph maintenance uses the existing native-update attempt followed by scoped
AST extraction/merge and old-ID retention, including any heading relocation
aliases required after the commit hook. This is not full-corpus re-extraction.
Tools-first local commits are authorized; nothing is pushed.

Continue `func_151A11E4` at VA `0x151A11E4..0x151A175C`, ROM
`0x1CE694..0x1CEC0C`: **350 words / frame 0x110**. Its actual callback is
`D_8008A4E8[2]` under `func_15149264`. Recover the complete typed phase-driven
emitter, preserve persistent packet flags, RNG/provider reload order, five
signed divisions, all floating operations and the 34-byte curve copy. The
return-interface prerequisite is complete; the emitter remains unconverted
and uncredited until its own full qualification and production gates pass.
