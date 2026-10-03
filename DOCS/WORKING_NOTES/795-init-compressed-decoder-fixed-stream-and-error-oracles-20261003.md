# Init Compressed Decoder Fixed-Stream And Error Oracles

Date: 2026-10-03.

Follow-up: [Note 796](796-init-dynamic-multiblock-and-core-entry-oracles-20261003.md)
adds connected dynamic, mixed-block, and outer-entry fixtures. Isolated
semantic C and exceptional-context qualification remain pending.

## Result

Ten new tests execute the retained compressed-decoder words and its fixed
wrapper against generated table fixtures. Valid fixed streams agree with
zlib; synthetic malformed streams pin retail-model behavior rather than
assuming zlib's errors describe this implementation. Production Init remains
assembly, with no conversion, compiler/profile/guard change, or aggregate
increase. This follows
[Note 794](794-init-decompressor-table-builder-interface-and-canonical-oracles-20261003.md).

## Fixture And Scope

`tools/tests/test_init_decompressor_decoder.py` builds literal/distance tables
through the original table-builder instruction model. It shares the bounded
low-word runner with the builder, adding only the decoder's LUI/ORI and nested
JAL/JR operations, plus read tracing. Builder regression tests remain active.

The decoder begins at `func_10006E00` with fixed tables supplied through
a0/a1, root widths seven/five in a2/a3, workspace in s6, cursor/reservoir in
s7/gp/fp, and output base/count/limit in f16/f17/f18. The fixture supplies
the five reservoir bits left after a final fixed-block header. It does not
execute the block-header dispatcher or the core's header/overlap setup.

The same stream also runs through `func_1000692C`. Fixture tables are mirrored
at the wrapper's actual `0x8003BE90` workspace so its absolute pointers
`0x8003BE94` / `0x8003C858` execute without patching instruction words.
The wrapper restores its original s6 and RA. Its stack-save writes are kept
distinct from decoder output writes.

Masks and base/extra data are parsed from retained data assembly. Input is
padded with sixteen zero bytes for the decoder's root-table lookahead;
these tests do not establish a compressed-input bounds contract. Sparse
memory still rejects unprovided reads. FPU/64-bit/privileged context execution
is outside this model; zero doubleword scratch stores are its only modeled
doubleword operation.

## Independent Valid-Stream Evidence

An independent canonical encoder produces fixed-Huffman streams. Python zlib
decodes each valid stream as an independent output oracle. Tests also execute
three streams emitted by zlib's fixed-Huffman compressor, rather than relying
only on the fixture encoder.

- Empty output and every literal byte, including zero and 0xFF.
- Distance-one and distance-three forward overlapping copies, including
  a 258-byte match producing 259 repeated bytes from one initial literal.
- All thirty distance classes through distance 32,768, including maximal
  extra-bit values; all length classes, also with maximal extra values.
- Exact output writes and unchanged sentinels on bounded whole-block fixtures.
- Both direct decoder and fixed-wrapper paths.

For the large-distance matrix, the instruction model starts with explicit
preexisting output history and decodes the following match block. The zlib
oracle independently decodes a stream containing both literal history and
the match. This validates history/match mechanics, not multi-block control
flow or a single modeled run through all 32,768 prefix literals. An initial
whole-prefix trial exceeded the model's instruction budget; no production
code was changed in response.

## Behavior A Connected C Recovery Must Preserve

1. Literals are written without the match path's limit check. A four-byte
   literal-only fixture succeeds and publishes count four with limit one.
   This is synthetic model behavior, not a valid caller-capacity guarantee.
2. Length copies require signed `newCount < limit`; equality fails. With one
   preceding literal and a three-byte match, limits three/four fail, while
   limit five succeeds. Failed matches do not write match bytes.
3. The produced count in f17 is published at end-of-block, not after every
   literal/match. A failure after one literal leaves that literal written
   but the prior published count unchanged. Rewrites must not infer no
   output side effects from an unchanged return/count value.
4. Reserved literal/length symbols 286/287 and distance symbols 30/31 return
   decoder status one. The fixed wrapper discards decoder status, returns
   zero, and retains the previous f17 count. Wrapper success status alone
   therefore does not qualify a malformed stream.
5. A synthetic match at distance two after only one literal reads the byte
   before output in this model. With that byte explicitly initialized to
   0xA5, output becomes `41 A5 41 A5` and decoder status is zero; zlib rejects
   the same stream. The assembly subtracts distance and copies without an
   explicit nonnegative history-index check. This is a pinned model/caller
   boundary, not a confirmed gameplay bug or real out-of-bounds observation.

The tests intentionally keep those differences from zlib instead of imposing
a defensive error policy while claiming semantic recovery.

## Reference And Linked Verification

The complete decoder body is 167 words / 668 bytes at
`0x10006E00..0x1000709C`. Its reference words compare to retail when the ROM
is available, with SHA-256:

`9991b45e6425503146d321b1a31b8a114c5932e8c029101ea0942c42c06d4895`.

All ten new decoder tests, all 47 focused Init tests, and all 502 tool tests
pass (full suite: 70.491 seconds). A final focused decoder rerun also passes
after explicitly exercising both 258-byte length encodings. Project tool
checks and `git diff --check` pass. Independent extraction of the current linked ELF again matches
both entire retail sections:

| Section | Bytes | SHA-256 |
| --- | ---: | --- |
| `.init` | 164,048 | `34372ebc8b2e56b5b6c02c8b88ce33a1558d5d329397fdc6e9e984333df6d4bf` |
| `.init_data` | 17,376 | `a3d3d56157fd9f9feb00a48a526c50ec51227b5a5afc277aa9a4b765c8fc6239` |

These are existing linked-artifact checks, not a new build or guest execution.
Init remains 492 C / 47 assembly rows. README aggregates and pending Game
edits are unchanged by this decoder work. No host-port or Release artifact
is touched.

## Next

1. Connect the dynamic code-length parser and builder calls to these decoder
   fixtures. Cover literal code lengths and repetition symbols 16/17/18,
   extra bits, invalid counts, and builder status handling.
2. Exercise stored/fixed/dynamic multi-block sequencing, BFINAL, cursor rewind,
   both enclosing header skips, and core output/error return publication.
3. Then implement isolated connected semantic C with explicit state and test
   it against the instruction-word oracles before choosing production ownership
   and matching strategy. Retain exceptional caller/FPR context separately.
