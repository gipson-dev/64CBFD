# Init Decompressor Shared Contract And Stored-Block Oracle

Date: 2026-10-03.

## Result

The ten retained decompressor rows are now mapped to a connected entry,
block dispatcher, stored/fixed/dynamic decoding, table builder, and fixed-table
initializer. Eight new tests pin concrete interface words and exercise the
original stored-block words using a bounded instruction model. This is
contract recovery and a test oracle, not a production C conversion or full
decompressor qualification.

The block header, stored LEN/NLEN pair, and fixed code-length ranges correspond
to [RFC 1951 sections 3.2.3, 3.2.4, and 3.2.6](https://www.rfc-editor.org/rfc/rfc1951.html).
That correspondence supports a DEFLATE-family interpretation; it does not
prove that this implementation handles every valid or invalid DEFLATE stream
like zlib. Its enclosing 0x1172/non-0x1172 header behavior is a separate retail
contract, not specified by RFC 1951.

## Connected Entry Map

| Entry | Body bytes | Recovered role |
| --- | ---: | --- |
| `func_10006240` | 28 | Ordinary three-argument wrapper; saves RA in a 0x10-byte frame |
| `func_1000625C` | 208 | Allocates shared 0xA88 frame; selects header skip and overlap limit; returns count or zero |
| `func_1000632C` | 84 | Resets reservoir/count, iterates blocks to BFINAL, backs input cursor over whole buffered bytes |
| `func_10006380` | 164 | Reads three header bits; routes stored/fixed/dynamic; reserved type returns status two |
| `func_10006424` | 1,028 | Dynamic code lengths/table construction followed by compressed decoding |
| `func_10006828` | 260 | Byte-aligns reservoir; stored LEN/NLEN validation and output copy |
| `func_1000692C` | 64 | Fixed-table decoder wrapper; restores workspace and unconditionally returns zero |
| `func_1000696C` | 1,172 | Table builder with extra register arguments and integer FPR save area |
| `func_10006E00` | 668 | Table-driven literals/lengths/distances and forward overlapping back-reference copy |
| `func_1000709C` | 300 | Startup fixed-table initialization, including builder calls |

These bodies total 3,976 bytes. The inventory includes eight trailing alignment
bytes after the initializer, yielding ten rows / 3,984 bytes. All ten body
word sequences independently compare equal to their retail ROM intervals.

Direct JAL scan of Init code finds the outer wrapper at ROM 0x1308 and the
core at 0x6248 and 0x5F2C. The latter is in the TLB/exception path and supplies
workspace `D_800340E8`; startup calls the wrapper with allocation/input,
output at `D_80082B20`, and workspace `D_8003809C`. Startup initializes fixed
tables through a call at ROM 0x1234. This scan covers direct Init JALs, not
indirect calls or a proof of all caller reachability.

## Shared State

| Location | Contract |
| --- | --- |
| `s7` | Next compressed input byte |
| `gp` | Low-bit-first 32-bit reservoir |
| `fp` | Available bit count |
| `s6` | Table workspace base |
| `f16` | Integer output base, moved with mtc1/mfc1 |
| `f17` | Integer produced-byte count |
| `f18` | Integer signed overlap-derived limit |
| `f19` | Builder allocation state; reset per block and at fixed-table initialization |
| `f0/f1` | Dynamic length/distance counts saved across builder calls |
| `f2..f11` | Builder saves s0..s7, fp, gp without an ordinary callee stack frame |

The core sets `s7=input+2` if the first big-endian header halfword is 0x1172,
otherwise `input+4`. It starts the limit at 0x70000000, replaces it with the
signed positive input-minus-output displacement when applicable, then with
a smaller signed nonnegative workspace-minus-output displacement. This is
overlap avoidance, not an explicit caller-supplied output capacity.
Successful core completion returns f17; nonzero block status returns zero.

The 0xA88 core frame saves s0..s7 at 0xA48..0xA64, fp at 0xA78, gp at
0xA7C, and entry RA at 0xA80. Helpers use distinct RA cells at 0xA6C
(block loop), 0xA68 (dispatcher), and 0xA44 (dynamic/fixed wrapper).
The block-final output cell is 0xA70, and the fixed wrapper saves workspace
at 0xA74. Dynamic table outputs occupy 0xA38..0xA40. The initializer builds
length arrays from 0x548 and uses output cells at 0x9C8..0x9D4.
These interfaces must become explicit state/arguments together; adding
independent ordinary prototypes to the internal entries is not sufficient.

## Stored-Block Behavior Proven By Tests

`test_init_decompressor_contract.py` extracts all 65 stored-leaf words from
the retained assembly. Its small model supports only the instructions this
leaf uses, including ordinary and likely branch delay semantics and integer
FPR transfers. It has a fixed step budget and sparse big-endian byte memory;
it is not a hardware emulator or a candidate production decompressor.

- Discard `availableBits & 7` bits before reading LEN and NLEN.
- Compare LEN with the low-sixteen-bit complement of NLEN.
- Reject `produced + LEN >= limit` using signed comparison, before output
  writes or count publication. Equality fails even for a zero-length block.
- Copy one byte at a time and publish the new produced count only on success.
- A malformed complement shifts the reservoir in its branch delay slot but
  skips the subsequent bit-count decrement. Do not assume failure state is
  identical to an untouched stream.
- All eight alignment values and zero through three preloaded bytes pass;
  exact reads/writes and final reservoir state are checked.
- Payloads of lengths 0, 1, 255, 256, 4,096, and 65,535 match Python zlib's
  independent raw stored-block decoding. Input/output fixture regions are
  separated; an initial fixture overlap at the maximum length was corrected
  before acceptance. No retail source change was made in response.

Other tests pin frame/header/FPR instructions and the fixed wrapper's final
`v0=0` return-delay instruction. The fixed wrapper discards the compressed
decoder's status; a clean rewrite must not silently propagate it instead.
The compressed decoder's literal path also lacks the per-literal limit check
seen in its length-copy path; its exceptional behavior needs separate tests.

## Verification And Limits

All eight new tests, all 28 focused Init tests, and all 483 tool tests pass
(full suite: 89.108 seconds). Project tool checks and `git diff --check` pass.
Note 792's same-checkout independent full Init section comparisons and
up-to-date build/matcher remain applicable: production source, profiles,
guards, and assembly ownership are unchanged here.

No fixed/dynamic stream has yet been run through this instruction model.
No actual MIPS execution, FPU context qualification, malformed back-reference
test, production C body, compiler trial, or host-port build is claimed.
README aggregate numbers stay unchanged; pending Game edits are preserved.

## Next Implementation Gates

1. Recover the builder's a0..a3 plus t7/t8/t9 arguments and four-byte table
   entry format from its complete body; characterize allocation/count errors.
2. Add fixed/dynamic literal, end-of-block, extra-bit, and overlapping-distance
   oracle fixtures. Cover ignored fixed-wrapper errors and count publication
   on decoder failure, not just valid-stream zlib equivalence.
3. Exercise multi-block reservoir/cursor rewind and the two header skips.
   Include the exception caller's saved FPR/context boundary.
4. Only then design the connected semantic C state/interface and choose an
   explicit matching strategy. Keep retail assembly as production owner until
   the actual replacement and full-section acceptance gates are proven.
