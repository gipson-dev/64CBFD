# Four direct damping callback matches

Date: 2026-11-12. `func_150BB260`, `func_150CAC28`, `func_150CBCE0`, and
`func_150CC8D4` replace zero-return placeholders in generated owners
`E8090`, `F5800`, `F8590`, and `F9430` respectively. Each 106-word retail
body is identical. Each reads the global tick count once, repeatedly multiplies
record floats at `0x58` and `0x60` by the factor at `0xA8`, and returns one.
A separate pointer to the factor recovers the original compiler shape.

Each IDO body emits all 106 retail words and relocations directly from C,
without word guards or insertions. The original indexed dispatcher
`func_151303EC` selects these bodies using `D_80089760` entries 2, 9, 7, and 8
respectively. Retail and candidate guest runs pass 440 cases per target, with
all 106 retail words visited; the dispatcher window passes the same case count
and two return-branch negative controls per target. Native SDK32 O0/O2/O3
pass 440 cases and six effective negative controls per target under UBSan.
No helpers are modeled or called by the callbacks themselves.

Both padders reproduce separately assembled retail words and relocations for
each target. Per function, twelve GNU rebases and 68 bounded access-cut triples
pass; another 80 bounded prefixes cover a tick value of `0xFFFFFFFF`. That
high-count prefix does not establish completion of the full iteration count,
and the tests do not establish complete dispatcher or gameplay behavior or
native/hardware fault semantics.

The combined actual Make and independent linked-image audit agree: 1,304
changed bytes, no metadata groups or exclusions, all 6,050 function addresses
fixed, and all 189,088 protected Game-data bytes unchanged. Owner compilation
preserves respectively five, eighteen, nine, and five other functions. Actual
ELF SHA-256: `f7c51feadcd208965cbe85b27472cb124ac01208a61ec4b45784d62b3263f890`. The existing whole-ROM checksum mismatch
remains.

Fresh ELF recount: **3,694 / 4,840 (76.32%)** Game and **4,367 / 5,513
(79.21%)** overall, zero drift. The Game 80% target needs 178 more matches.
Tools commit `b34167cdbf6711e56ccbd38d6f7a018ed85e9627` precedes this consumer change.
