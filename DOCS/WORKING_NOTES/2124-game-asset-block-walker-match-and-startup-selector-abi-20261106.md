# Asset-block walker match and startup selector ABI

Date: 2026-11-06. Continue the 80% goal from consumer
`7128bda5f1ef5e4e52dffb733a60faedccba611d` and mounted tools
`3bca5890b029d47c75e9c0da6e1bf9d745c928cc`.
This completes the next target in
[Note 2123](2123-game-double-bank-record-constructor-direct-match-and-sdk-vertices-20261106.md).

## Installed reconstruction

`func_15015920`, owner `generated_42DC0`, now matches its complete **70-word**
slot: VA `0x15015920..0x15015A38`, ROM `0x42DD0..0x42EE8`, 280 bytes,
frame `0x38`, six bindings. Semantic C emits **69 of 70 words directly**;
one expected-word guard preserves retail's commutative unsigned-add operand
order at `0xC0`: `01D07821` to `020E7821`. Both are ADDU with the same
destination and exchanged source registers. Opcode, function, destination,
immediate bits and all bindings remain fixed. This changes no arithmetic
result, saved state or memory-access order. No frame, insertion, omission,
profile or algorithm normalization is used.

The recovered interface is `void(s16 selector)`. S4 captures the signed low
16 bits before allocation, while the original argument word is retained in
its incoming home at SP+`0x38`. S0..S4 and RA use the original SP+`0x20..0x34`
save slots. The startup caller's local declaration in `game/entrypoint.c`
now agrees as `void func_15015920(s16)`. Copied old/new caller compilation
preserves its sole function, allocated pools and register metadata; both
padded objects equal the actual production object byte for byte.

The walker allocates `func_10003C6C(0x2800, 1, 2, 1, 0)`. There is no retail
allocation-failure gate. It selects the eight-byte start/end entry at
`D_80082F80 + signedSelector * 8`, then submits a blocking copy through
`func_10004514(start, base, unsigned(end - start), 1)`. The local range view
uses signed 32-bit address words for the SDK's source-address interface;
transfer lengths and all address-limit arithmetic preserve unsigned wrap.

After the copy it reloads both table endpoints and tests
`unsigned(cursor + 15) < unsigned(base + end - start)`. Each complete header
calls `func_15015A38(cursor, index, signedSelector)`, then reads the live
big-endian length bytes 4..7 and advances the cursor. It reloads the endpoints
after every consumer call and increments the record index in the original
back-branch delay slot, including the last trip. It always frees the original
allocation, including empty ranges. The copy and consumer results are ignored.

The neighboring consumer remains an unconverted zero-return placeholder.
Its existing unspecified-parameter declaration is retained with a comment
recording the retail three-word interface. A typed-placeholder probe added
three incoming-home stores, changing 12 bytes to 24, and was rejected and
archived. The installed change does not refine or credit that placeholder.

## Source fit

The first ordinary pointer/range-local source emitted 73 words/frame `0x58`.
A narrow parameter retained the correct early sign extension but still used
73 words/frame `0x50`. A guarded do/while recovered frame `0x38`; repeated
indexed table expressions removed an extra named-range copy, and the signed
source-address field removed a separate argument move. This recovered all
70 words and saved-register lifetimes. Equivalent unsigned byte-weight
expressions reduced the remaining schedule to the single ADDU operand order.
Other groupings, full-word parameter forms and pointer arithmetic screens
remain rejected. The normal **O2/g3 profile** is retained.

Codex is the single writer. Claude calls attempted/completed: **0/0**.
Local compiler and instruction evidence settled the fit. The private screens
and rejected typed-placeholder object are retained in the ignored target
directory. The standalone tools checkout's existing work is preserved.

## Qualification

```sh
python3 -m unittest tools.tests.test_game_asset_block_walker_match -v
```

All **eight focused checks** pass before installation and again after
installation with both tools configurations. The ignored overlay exercises
the standalone sibling's actual compiler fixture, object parser, timing engine
and native command builder, recording source paths and hashes. Its actual
padder also reproduces the unchanged startup caller object.

- **2,588 cases per original/raw/padded body** execute every root word. They
  cover raw-word selector truncation/sign, all 256 values in each of the four
  size bytes, empty/one/multiple blocks, 15/16-byte boundaries, live table
  changes after allocation/copy, post-consumer length changes, unsigned
  wrap/signed-limit edges and saved GPR/FPR/SP state. Null allocation has no
  invented early exit in the guest model.
- **120 aliases per body** relocate table entries into output buffers and
  incoming homes, and let copied output overwrite the original argument home
  after S4 has captured the selector. **120 own-access fault prefixes** match
  complete literal states across all three bodies. Private/sparse guest
  aliases are not portable C memory-contract claims.
- **288 cases per body** connect the complete original **273-word texture
  consumer** to an independent RLE reference. All descriptor fields and pixel
  backing bytes agree, including eight-byte row stride, odd-row XOR-4 swizzle,
  zero borders, run lengths and padding. They reach **261 words**. The other
  **12 remainder-path words** are proven unreachable: only two instructions
  define T3, setting it to `(byteWidth + 7) & 0xFFF8`; the later T3 modulo 4
  is therefore zero for all 256 widths. Pinned mask/branch words and an exact
  write-register census account for the skipped prologue. All 273 words remain
  literal. The production consumer is still unconverted and gets no credit.
- **128 cases per body** execute the actual **four-word startup window**:
  JAL, zero-selector delay, following JAL and NOP. Two poisoned free-return
  values are ignored and the following call replaces the result. The full
  containing 124-word startup routine is not claimed as emulated. The aligned
  ROM census finds one JAL at `0x34DA0`, no tails or literal pointers.
- **Nine GNU links** and **99 rebased cases per body** qualify the table
  HI16/LO16 carry boundaries and all four R26 sites. The ADDU guard remains a
  non-relocated pure operand exchange at every layout.
- **7,326 native32 positive calls**, 1,221 rows per direct/compatible-callback
  path and O0/O2/O3 profile, use SDK headers and UBSan. They compare the full
  `0x2800` buffer plus 32 sentinel bytes using exact byte deltas from the
  independent reference, live table words and exact provider call traces.
  Twelve effective controls cover selector sign, allocation/copy arguments,
  blocking mode, boundary/signed comparison, index/selector arguments, endian
  decoding, consumer/free omissions and freeing the wrong pointer. Every
  control exits 1 through a checked rejection, without faults or diagnostics.
- Fail-closed gates reject 280 raw-byte corruptions, six altered bindings,
  three changed predecessor-guard prefixes, five full-image corruptions and
  the former zero-return stub.

The reused guest engine initially lacked the consumer's XOR instruction;
this target's oracle now implements it. The coverage checker also needed
SLTI and stack-store classification before its T3-write proof could run.
Both fixture issues were corrected and the complete suite rerun; neither
changes production C or shared helper code. Allocator, ROM I/O and free are
bounded providers; model agreement is not DMA, hardware or gameplay proof.

Both project-tools smoke checks and all three shared suites (progress parser,
word-patch relocation handling and PC16 padding) are **fresh in both copies**.
Their helper and test-source hashes are captured. No previous shared receipts
are substituted for this run. The sibling's six tracked edits and 2,428
untracked files remain preserved.

## Production closure

The guard CSV retains its complete predecessor byte prefix and appends exactly
one filename-scoped row. All **two raw and padded neighbors**, compact allocated
data and padded pools remain unchanged. The compact GPR mask changes from
`80000006` to `A31FFFF6`; the independent complete-body register decode derives
that union. The other 20 register-metadata bytes remain pinned. All **98 frozen
inputs** are protected, including the unchanged production caller object.
Both affected owners emit no compiler diagnostics.

The actual production build is:

```sh
make -C conker -o retail_word_patches.us.csv -j4 build/conker.us.elf progress.csv
make -C conker -o retail_word_patches.us.csv all
make -C conker -o retail_word_patches.us.csv match-progress NON_MATCHING=1
```

The `-o` flag marks the shared guard-file dependency old while Make rebuilds
the two changed C sources. This avoids rebuilding owners whose filtered guard
records are byte-identical: the sole appended row belongs to this walker.
The exact prefix/row audit, copied caller proof and complete linked-image
comparison cover the result without exclusions. The startup caller's padded
object remains `ef22ef9969c5ae5956349f091a8493da97cf014df71c724a22f341824c109dac`.

The full ELF equals the independent **226-byte** prediction, with **zero
exclusions** and **zero named metadata permutations**. Only the target slot
and its symbol size, 12 to 280 bytes, change. All **6,052 function addresses**
remain fixed, and all **189,088 protected data bytes in 720 owners** are exact.
The wider unfinished image retains the expected checksum exit 2. The existing
duplicate `generated_12D630` recipe warning is unchanged. The recount is:

| Section | Byte-exact | Drift | Still different |
| --- | ---: | ---: | ---: |
| Total | 4,193 / 5,512 (76.07%) | 0 | 1,319 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 3,520 / 4,839 (72.74%) | 0 | 1,319 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

Conversion rows and `progress.csv` remain unchanged. **217 more** matches reach
the current 4,410 threshold for 80%. Production fingerprints:

- ELF: `89e741ec7be49a4f13b1cc59e0d4bf204bb3dc74c7c85c27f272cbf3c62a2b2b`.
- Owner: `c57da52e374935462b2309543e4a25dab295cc916de9dc068d517e094a569261`.
- Code binary: `c7e57db9b6f9569392b0c95a822a5d6e366f38a17ab012ffe15584a9d1ac96ff`.
- Guard CSV: `3faf86a68cc26b5a29f6e96d1aaf8aa1c905686fa74a5992b868a70ef3bcdfd6`.

Evidence lives under `conker/build/game-asset-block-walker-15015920-match/`.
Graphify receives a scoped refresh with old-node retention accounting, without
claiming a full-corpus extraction. Tools are committed before the consumer
pin, two C sources, guard row, aggregate README rows and concise indexes.

Next: `func_1503F9F0` in `generated_6CEA0`, a 70-word controller-axis sampler
with a signed-halfword countdown, signed slot, dead zone and output clamps.
Inspect its original caller/result use, unconditional pad-table lookup and
input/output aliases before reconstruction. Keep handwritten `func_150A76F0`
separate, preserve earlier boundaries and keep the full 80% goal active.
