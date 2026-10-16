# Table Debris Semantic Recovery

Date: 2026-10-16. Resume from consumer **448de8cc**, tools **c0bbd87**,
both initially clean. Bank tools **57f58b3** first, then the consumer pin
and documentation. **This is a pre-install recovery checkpoint, not a new
byte match.** Production C, guards, ELF, conversions and README remain
unchanged. Continue the same target's frame and saved-lifetime recovery.

## Steps

1. [x] Audit all 158 original words of func_15170F4C, its six 28-byte records, six float constants, packet consumer and sole direct original caller.
2. [x] Recover typed semantic C: unsigned halfword kind, float offsets/rotations, post-lookup kind reread, coefficient/origin snapshots, two float-RNG draws, fixed packet lifetimes and final byte store.
3. [x] Run 40 named O2 source/layout screens, one whole-owner O1 control and three isolated profile controls. Recover the 158-word count, but explicitly reject the remaining frame, packet-home and FP lifetime differences.
4. [x] Pass seven focused checks: 648 paired sequences, all original instructions, full per-stream packet bytes, native32 O2/O0, eleven effective guest/native negatives, original ABI captures, current consumer/allocator connections and 78 frozen/live input keys.
5. [x] Preserve all production artifacts and the additional source, refresh official unchanged numbers, check both tools copies, preserve the independent mirror and bank tools before consumer pin/docs.
6. [ ] Recover retail frame 0xE8, packet SP+0x84, all three origin homes and saved coefficient/constant lifetimes without artificial locals, volatile workarounds, fixed registers or invented calls. The current selected body is 158 words / frame 0xF8, with 121 real differences.
7. [ ] Qualify any proposed normalization with appropriate expression/lifetime, fault-prefix, caller/rebase and connected-consumer gates. Install only after a complete linked-image audit and fresh matching measurement; do not blindly replace the current 121 words.
8. [ ] Recover the sole wider caller func_1511C638 and retain func_1516D400, inherited-stack func_1516FE1C and all broader Game/additional-source/raw-matching queues.

## Recovered Contract

**func_15170F4C**, VA **0x15170F4C**, ROM **0x19E3FC**, is **158 words /
632 bytes**, frame **0xE8**, ending at **0x151711C4** with no separate
padding word. Its owner remains a placeholder in
[generated_19E040.c](../../conker/src/game/generated_19E040.c).

```c
void func_15170F4C(u8 *actor, u8 flags, s32 context);
```

It is another six-piece producer using the existing 96-byte packet, but
it has no final ring call. Copy signed-halfword actor coordinates
+0x10/+0x12/+0x14 into float snapshots. Snapshot three packet coefficients
from D_800A6F98/9C/A0 (0.3, -0.7, -0.2) and the three motion constants
from D_800A6FA4/A8/AC (0.1, 0.23, 0.09). The source uses the actual stored
single-precision values, not decimal recomputation of those constants.

The table **D_800A6ED8**, VA **0x800A6ED8**, ROM **0x24B998**, contains
six **28-byte** records ending at VA 0x800A6F80. Each record is:

```c
typedef struct TableDebris19E040 {
    u16 kind;
    u16 reserved02;
    f32 offset[3];
    f32 rotation[3];
} TableDebris19E040;
```

All six retail kinds are **0x0152**, not an unsigned byte read from the
high address. The two-byte +02 field is not consumed. Table values at
+04/+08/+0C and +10/+14/+18 are floats, not integers or host pointers.

Initialize fixed packet fields once: rotation zero, scale 2, lifetime 60,
mode 2, alpha 255, bytes +56/+57/+58/+59 zero, variant +5B=6 and controls
+5C=2, +5D=1. The four bytes +44..+47 and two bytes +5E..+5F remain
untouched. The experiment renames the existing packet's `zero5C/zero5D`
members to `control5C/control5D`, since this routine uses nonzero values;
that rename is confined to the proposed owner, not production.

For each of six records:

- Call func_1518C900 with the **unsigned halfword** kind. After lookup, reread the live halfword and narrow it to packet byte +5A. Lookup can change the table, so caching the first read is incorrect.
- Add the three live float offsets to the original coordinate snapshots. X/Z velocity uses the saved 0.09 constant; Y velocity is abs(offsetY) times the saved 0.23 constant, with no added 7.
- Copy the three table rotations into packet +0C/+10/+14. Spin X is the stored first rotation times saved 0.1. Call the genuine zero-argument **func_150ADA68** twice for `(draw * 4) - 2` and `(draw * 10) - 5`, preserving separate float multiply/subtract operations.
- Store the lookup asset word late and submit func_15168BE4(packet, byte flags, full-word context). Increment index and advance the table pointer by 28 bytes.

Only after all six submissions, set **one byte** at actor +0x6E to 1.
The additional source's float coordinate reads, byte-only kind lookup,
integer table fields, void-pointer layout and wide final actor store are
not imported. That reference file remains unchanged.

## Compiler Evidence

The first corrected candidate is **156 words / frame 0xF0**, packet
SP+0x90. A genuine named loop bound recovers the retail signed SLT/branch
instead of the compiler's constant-bound BNE. Chained scale initialization
recovers the separate 2.0 reload at the first RNG result. Together they
produce **158 words / frame 0xF8**, packet **SP+0x98**. Eight neighbors,
their raw bytes/sizes/relative relocations and normalized pools are fixed.

Selected raw SHA-256:
`7c11a8d372b5d02912bf3e11053e88e2223aba5746f8f446e0cb33e2788f1436`.
It has **121 real linked-word differences**, no diagnostics and no
data/rodata pool. The actual production padder retains all those
differences; fitting the 632-byte slot is not a match. `qualify()` rejects
this candidate explicitly; no target guard or profile is installed.

The 40 named O2 screens cover scalar/array/struct origins, initializer and
local declaration order, scoped real RNG intermediates, loop-bound spelling
and scale-assignment direction. Some bodies are identical. The `register`
storage-class controls do not change allocation and are not selected;
no fixed-register binding is used. Whole-owner O1 gives 179 words / frame
0xA0; isolated O2/no-unroll controls retain 156 / 0xF0 for the initial body.
Do not change the production profile on that evidence.

The early O1+g3 and whole-owner no-unroll invocations were rejected by
asm-processor's option parser, not by the source/compiler. Use the existing
isolated compiler helper for profile controls; do not count rejected
invocations as emitted candidates.

Retail's remaining allocation boundary is concrete:

| Role | Retail | Selected Candidate |
| --- | --- | --- |
| Frame | 0xE8 | 0xF8 |
| Escaped packet | SP+0x84 | SP+0x98 |
| Origin X/Y/Z | SP+0x7C / +0x78 / +0x74 | saved F28 / F30 / SP+0x8C |
| Rotation / vertical coefficient | saved F24 / F22 | SP+0x7C / +0x80 |
| Horizontal coefficient | saved F20 | saved F20 |
| RNG 4 / 10 / 5 constants | saved F26 / F28 / F30 | saved F22 / F24 / F26 |

Resolve those real lifetimes and homes before considering instruction
normalization. Do not replace a large unqualified allocation difference
with retail words merely because semantic examples pass.

## Fresh Qualification

All **seven tests pass in 42.123 seconds**, exit zero:

```sh
python3 -m unittest tools.tests.test_game_table_debris -v
```

- **648 whole sequences / 1,296 retail-candidate runs** cover signed coordinate extremes, zero/high-byte flags, full-word contexts, high-bit unsigned kinds, six provider modes, RNG tape rotations and two stack phases. All **158 original instructions** execute.
- Compare all **90 initialized packet bytes** across streams. Independently derive all **96 bytes for each stream's actual frame/home**, including first residue. Do not claim equal private frames or first-hole values across the different homes. Provider-seeded holes and retained fixed fields are checked on later iterations.
- **Native32 O2/O0, 1,024 cases each**, separate translation units and selected-C UBSan, check the typed ABI, layout/stride, all initialized fields and provider-seeded holes. First indeterminate bytes, asynchronous/volatile behavior, private guest homes and FP fault environment are outside native acceptance.
- **Eleven effective compiled guest and native negatives** reject narrowed/signed kind lookup, cached post-lookup kind, integer position interpretation, missing absolute value, wrong horizontal coefficient, wrong rotation component, wrong second draw range, fixed-field reset, reserved-byte reset and wide final actor store.
- **Four original caller captures** check actor from caller SP+0x48, flags **255**, context **0**. The current ELF's corresponding **44-byte window is zero-filled**, and [generated_142560.c](../../conker/src/game/generated_142560.c) confirms **func_1511C638 is still a zero-return placeholder**. Do not claim a current caller ABI or whole-game acceptance from the original window.
- **48 connected runs** execute the actual 26-word consumer and 28-word allocator. Check all 96 copied bytes, zero assets and every-third allocation failures. First residue is checked against each stream's own home; RNG, lookup, heap, registration and bcopy remain bounded or opaque.
- All **78 frozen/live input keys** remain fixed. Every frozen-capture corruption and changed baseline manifest rejects. Production source/guards/ELF and the additional-source reference remain unchanged. No linked production rebuild is needed for this tools-only checkpoint.
- Both tools copies pass Windows syntax and all eleven shared WSL padder tests; consumer `make tools-check` passes. Routine Claude calls: zero.

The native fixture's initial `0x5E+i` preprocessing-number typo was fixed
by separating tokens. The caller test's initial expectation of a matching
current window was contradicted by actual ELF bytes; retain that evidence
and explicitly test the missing current window instead. Negative packet
checks derive the actual escaped pointer rather than assuming every
negative retains S3's allocation. The complete final suite reruns all
corrected checks. None is a production edit or matching concession.

## Banking And Resume

Fresh official measurement remains **Game 2,913/4,828 (60.34%)**, **total
3,586/5,501 (65.19%)**, different **1,915**, drift **0**. Init 492/492 and
Debugger 181/181 remain exact. Conversion data stays 5,501/6,044 (91.02%),
byte coverage 86.04%. The root README is unchanged because neither its
aggregate rows nor its 2026-10-16 verification date need changing.

Tools **57f58b3** contains four new experiment/oracle/native/test files.
Preserve the older mirror at HEAD **ddbdd16** and all **763 initial dirty
file hashes**. Copy only four absent additions hash-equal, giving **767
paths**; do not reset or commit that checkout. Bank tools first, then
consumer pin/docs. No push or host/frozen Release action.

Resume **func_15170F4C**, not a different easier function: recover its
retail frame, packet home and saved FP roles from the table above. Preserve
`conker/build/game-table-debris/` captures, the previous debris successor
checkpoint and every wider queue. Caller restoration and independent
rebases/fault-prefix obligations for a future normalization remain open.
