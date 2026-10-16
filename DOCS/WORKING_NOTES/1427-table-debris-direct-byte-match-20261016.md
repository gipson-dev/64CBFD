# Table Debris Direct Byte Match

Date: 2026-10-16. Resume from consumer **83f57f64**, tools **57f58b3**,
both initially clean. Bank tools **a9f3606** first. Finish
[Note 1426](1426-table-debris-semantic-recovery-20261016.md): replace
**func_15170F4C**'s placeholder with complete semantic C, matching all
**158 retail words / 632 bytes**, original frame **0xE8**, packet
**SP+0x84**. **No target instruction guards, insertions or omissions.**
Use the existing literal-pool alias mechanism, not a compiler-profile change.

## Steps

1. [x] Resume the banked contract and audit the remaining frame, origin homes, saved FP roles and exact literal-pool provenance.
2. [x] Observe three actual owned compiler runs with fingerprint-locked read-only frame watches, fired capture gates and successful driver/child exits; require normal/traced functional output equality.
3. [x] Recover the original frame and all homes with genuine locals and the original float literals. Recover the last two scheduling words by moving the real loop-bound initialization before table-pointer initialization.
4. [x] Pass 15 final target/install checks, including native32, all packet bytes, fault prefixes, effective negatives, rebases, original caller limits and connected current consumers.
5. [x] Predict the complete linked ELF before installation, account for all six symbol/string cycles, install only the body/declarations and pool alias, rebuild and match every predicted byte with no exclusions.
6. [x] Refresh official numbers and aggregate README rows, preserve the older tools mirror and bank tools before consumer source/build/pin/docs. No push.
7. [x] Recover func_15171200, all 256 words / 1,024 bytes, frame 0xE0, in [Note 1428](1428-random-packet-burst-direct-byte-match-20261016.md), with its full float/word/byte ABI, escaped packet and RNG qualified. No target instruction guards.
8. [ ] Restore the wider caller func_1511C638 and retain func_1516D400, inherited-stack func_1516FE1C and all broader Game/additional-source/raw-matching queues.

## Source And Contract

Retain the address-based name and effect-only prototype:

```c
void func_15170F4C(u8 *actor, u8 flags, s32 context);
```

The complete body spans VA **0x15170F4C..0x151711C4**, ROM **0x19E3FC**,
with no separate padding word. Its owner is
[generated_19E040.c](../../conker/src/game/generated_19E040.c).
Preserve the six 28-byte records, unsigned-halfword lookup followed by a
live kind reread, signed coordinate snapshots, six full packet submissions,
two zero-argument float draws per piece and final single-byte actor update
from Note 1426. There is no ring call in this routine.

Rename only the shared packet's misleading `zero5C/zero5D` members to
`control5C/control5D`: the installed earlier producer still writes zero,
whereas this producer writes 2/1. Its earlier compiled body remains fixed.
Add the typed table and exact helper declarations. Do not import the
reference's incorrect widths, pointer layout or wide actor store.

## Frame Provenance

Run **64 named source/layout screens** in the successor directory:
18 loop, eight object, nine table/local-order, six literal, twelve slot
and eleven initialization/count screens. Some bodies are identical;
do not count them as independent implementations. Loop spelling, narrow
counter, const and aggregate controls alone do not recover all retail roles.

The existing observer follows only newly owned compiler processes and their
children. Pin all four compiler hashes; capture actual CFE/UOPT inputs,
decode descriptor-defined records and require fired UGEN frame watches.
All three driver and producer/consumer runs exit zero. The traced target
equals its complete owner, and text/functions/relocations/pools equal a
normal compile. `.mdebug` differs, so literal object-file equality is not
claimed. No compiler change, install or simulated-memory write is used.

| Measurement | Previous Scalar | Origin Array | Accepted C |
| --- | ---: | ---: | ---: |
| CFE/UOPT M reservation | 140 | 140 | 124 |
| UGEN local reservation | 144 | 144 | 128 |
| Observed saved reservation | 88 | 88 | 88 |
| Outgoing reservation | 16 | 16 | 16 |
| Temporary increment | 0 | 0 | 0 |
| Final frame | 248 | 248 | 232 |

This is declared local storage, not a UGEN spill problem. Re-express the
three motion coefficients as their genuine **0.09f, 0.23f and 0.1f literals**
instead of explicit snapshot locals. The compiler recovers all six saved
FP roles and the original separate 2.0 reload. Its pool is exactly:

```text
3DCCCCCD 3E6B851F 3DB851EC 00000000
   0.1f     0.23f     0.09f    alignment
```

The first twelve bytes equal retail ROM **0x24BA64..0x24BA70**, VA
**0x800A6FA4..0x800A6FB0**. The final four alignment bytes are not emitted
over the next retail constant. Use the existing target-specific
`RETAIL_RODATA_SYMBOL := D_800A6FA4` in the Makefile; six relocations retain
their numeric words/addends 0, 4 and 8 while binding to the original pool.
No additional data is linked. Native literal tests assume the initial
readonly pool values; guest emitted code still reads the actual retail
addresses, preserving the observed pre-loop snapshot lifetimes.

Use the real index before the packet and real count after it. The packet
is M-100, with origins M-108/-112/-116, recovering **SP+0x84** and
**SP+0x7C/+0x78/+0x74**. There are no artificial padding variables, volatile
workarounds, fixed-register bindings or invented arguments. Finally move
`count = 6` before the table-pointer initialization: the last independent
S4/S0 schedule then emits directly, without two-word normalization.

Raw target SHA-256:
`b819068d7c34b241235c8488ac0da42757752cdd0aa0d9eb058683e76a61e309`.
The unaliased compact-owner link differs only at six literal addresses;
the actual production pool alias yields **zero linked-word differences**.
All **eight neighbors**, their raw bytes/sizes/relative relocations and
prior empty pools remain fixed apart from this new 16-byte compiler pool.
The existing guard CSV is byte-identical, with no row for this target.

## Fresh Qualification

All **15 final tests pass in 102.084 seconds**, exit zero:

```sh
python3 -m unittest tools.tests.test_game_table_debris_match tools.tests.test_game_table_debris_match_installed -v
```

- **648 whole paired sequences** cover high-bit unsigned kinds, signed coordinate extremes, flags/context widths, live tables, post-lookup rereads, six provider modes and both stack phases. All **158 original instructions** execute, and all **96 packet bytes** are checked. Six extra raw-stream cases execute the compiler's own immutable pool and compare retained packet observations with retail.
- **Native32 O2/O0, 1,024 cases each**, separate translation units and selected-C UBSan, check all 90 initialized bytes and provider-seeded holes. Eleven effective guest/native negatives cover kind width/sign, cached kind, integer positions, absolute value, motion/rotation/range errors, repeated fixed-field reset, reserved-byte reset and wide actor store. Native first indeterminate bytes and arbitrary FP environment are not acceptance claims.
- **474 fired fault-prefix pairs** compare complete literal guest state. The direct instruction stream is retail-identical; this is not portable native fault-order proof.
- All **158 raw-word flips, 18 relocation-binding flips, 16 pool-byte flips and a wrong production pool alias** reject effectively. Three independently assembled original rebase sets / **72 paired cases** change every table/constant/call binding, including signed-low carries and literal addends.
- **Four original caller captures** preserve actor from SP+0x48, flags 255 and context zero. The current caller **func_1511C638 remains a placeholder**, and its 44-byte call-site window remains zero-filled. Do not convert original ABI evidence into current caller/gameplay acceptance.
- **48 current consumer/allocator runs** execute 54 actual words and check every copied packet byte, zero assets and every-third allocation failure. RNG, lookup, heap, registration and bcopy remain bounded or opaque.
- All **78 frozen/live input keys**, capture/initial-manifest/successor controls and physical code/data/callee/metadata corruptions are checked. Preserve all **75 unaffected inputs**, including guards and conversion CSV. Both tools copies pass Windows syntax and all eleven shared WSL padder checks; consumer `make tools-check` passes. Routine Claude calls: zero.

Qualification corrections are confined to tests/artifacts: compare the actual
empty-pool schema (`.rodata/.data: None`), apply the explicit pool alias to
the rebase helper, and give the neighbor compile a distinct filename. The
initial neighbor compile overwrote an owned frozen-object artifact; recover
it byte-for-byte from the unchanged live baseline object at its original
recorded SHA, without changing the manifest. The final suite reproduces
the baseline link from that recovered capture and passes all gates.

## Complete Image Prediction

Before production edits, snapshot the baseline linker script and padded
owner object with hashes. A full GNU-ld link using the captured old object
reproduces the frozen predecessor ELF exactly. Substitute only the qualified
new owner selector to predict the new ELF. The first complete prediction
is captured in `initial-prediction.json` before installation.

The target-slot/extent component changes **507 bytes**, size **12 -> 632**.
The pre-install full link also predicts exactly **121 metadata bytes** in
six contiguous record/name cycles, with every named definition unchanged
apart from the target size:

1. `(D_800A6FA0, D_80090B50)` swaps.
2. `(D_800A6FA4, D_800A1304, D_80090B54, D_800AAC14, D_800AA3E4)` rotates left once.
3. `(D_800A6ED8, D_80090A88, D_80090928)` rotates left once.
4. `(D_80099F3C, D_800A3E0C)` swaps.
5. `(D_8009952C, D_80095B2C, D_800A3D9C)` rotates right once.
6. `(D_800A6F98, D_80090298)` swaps.

The serializer SHA-gates the structural prediction, checks all original
record fields and contiguous name spans, preserves canonical definitions,
and requires exactly 121 byte changes. **51 record/name corruption controls**
reject. Full baseline/prediction relinks pass before and after installation.
There is no section, symbol or metadata exclusion, and no post-install
amendment to the first complete prediction.

The guest build exits zero, including the broader incremental rebuild
triggered by the Makefile timestamp. Inherited duplicate-recipe and legacy
compiler warnings remain. The final **3,257,636-byte ELF** equals its
complete pre-install prediction byte-for-byte: **628 changes = 507 + 121**,
every other byte fixed. Protected layout is **189,088 bytes / 720 owners /
zero differences**.

| Input | SHA-256 |
| --- | --- |
| ELF | 13196f6d2e9516c7bab5b9b4ad21f68812e40da2ae48b9b8b6a8d75fe1484141 |
| Owner | 9b6b76a4eb7e8c9a1751a83e7357ee0c33d7bd8d0e3a8c54dd43ed9080931e5f |
| Makefile | bba39f33c36fa73065ede3642013a0349d0f482fe80b6b156da172d4168c817e |
| Unchanged guards | a5f47cb991e377c7f9e80faa896b4db392a7999273a958520dcc61d9d1b22b62 |

## Banking And Resume

Fresh official measurement: **Game 2,914/4,828 (60.36%)**, **total
3,587/5,501 (65.21%)**, different **1,914**, drift **0**. Init 492/492 and
Debugger 181/181 remain exact. Conversion data stays 5,501/6,044 (91.02%),
byte coverage 86.04%. Root README changes only the two matching rows.

Tools **a9f3606** contains four new experiment/checkpoint/test files. Keep
the older mirror at HEAD **ddbdd16**, preserving all **767 initial dirty
file hashes**. Copy only the four absent additions hash-equal, yielding
**771 paths**; do not reset or commit that checkout. Bank tools first,
then consumer source/build/pin/docs. No push.

Next is **func_15171200**, 256 words / frame 0xE0. Use a new successor
directory and the strict table-debris checkpoint; keep these captures and
older fixed-live suites as historical receipts. The wider caller and all
other Game queues remain active. No host build/launch, gameplay acceptance
or frozen Release operation.
