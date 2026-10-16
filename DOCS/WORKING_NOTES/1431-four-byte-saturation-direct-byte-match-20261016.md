# Four-Byte Saturation Direct Byte Match

Date: 2026-10-16. Resume from consumer **308485bf**, tools **166a8a1**,
both initially clean. Bank tools **eee5a08** before consumer source/pin/docs.
Continue [Note 1430](1430-actor-effect-dispatch-and-owner-completion-20261016.md):
restore **func_1516D400**, all **58 words / 232 bytes**, with no stack frame,
separate padding, instruction guards or compiler-profile changes.

## Steps

1. [x] Freeze source/ELF/reference inputs; audit the full original leaf, byte-counter consumers and callback registrations rather than searching only direct JAL callers.
2. [x] Recover the no-input void ABI, unsigned widths, four-counter array and conditional live increment; distinguish source semantics from compiler register allocation.
3. [x] Qualify all 58 direct words, 29 unchanged neighbors, native32, effective negatives, conditional byte-access traces, fault prefixes, independent rebases and the actual current callback dispatcher.
4. [x] Predict the complete ELF before installation, reproduce the predecessor link exactly, rebuild production and reproduce every predicted byte without exclusions.
5. [x] Pass all 12 final tests, refresh aggregate README/status/roadmap rows, preserve the older tools mirror and commit tools before consumer C/pin/docs. No push.
6. [ ] Recover func_1516D738, VA 0x1516D738 / ROM 0x19ABE8, 153 words / 612 bytes, frame 0x98, ending at 0x1516D99C. Audit its display-list/record ABI, helper outputs, cached render state and SP+0x5C read before choosing C locals.
7. [ ] Keep func_1516DB90, inherited-stack func_1516FE1C, the three external effect helpers and earlier callers, and all broader Game/additional-source/raw-matching queues active.

## Recovered Contract

```c
void func_1516D400(void);
```

Owner: [generated_19A8B0.c](../../conker/src/game/generated_19A8B0.c).
Executable span: VA **0x1516D400..0x1516D4E8**, ROM **0x19A8B0..0x19A998**.
The complete 58-word slot is executable code, including the return delay
slot; there is no additional padding word. The ELF symbol grows **12 -> 232**.

For the four unsigned bytes **D_800DD2A0..D_800DD2A3**, read the current
counter. If it is below 255, conditionally read unsigned byte **D_800BE9A0**,
add in a signed word, clamp sums at least 256 to 255 and store one byte.
An already-255 counter causes no increment read or store. An unsaturated
counter with increment zero still performs its byte store. No input
argument is consumed, and the callback driver ignores V0; do not preserve
the false zero-return placeholder prototype.

The donor's four explicit scalar-global blocks recover the arithmetic
but not the raw instructions. Replace them with readable `index`/`value`
locals and an owner-local four-byte array declaration. Keep the original
address-based symbol name and a short semantic comment. This is a measured
compiler match, not proof that the original source used this exact syntax.

The sole same-owner counter consumer, **func_1516EED4**, already indexes the
four bytes through a scalar address. A plain array subscript changes its
temporary allocation and fails an existing word guard. A valid byte view
`((u8 *)&D_800DD2A0)[arg0]` preserves all its raw words, size and bindings
while giving this owner a real four-byte array declaration. Its existing
index domain and instruction guards are not broadened or reclassified.
No global-header/data-layout migration is attempted.

## Matching Evidence

The complete explicit-global baseline has the correct 58-word size but
**56 differing words**. Natural scalar storage forms and completed valid
optimizer screens do not resolve its address commoning and likely-store
branches. O1 emits 67 words; rejected asm-processor flag combinations are
not counted as completed compiler evidence. No experimental profile is installed.

An indexed array loop with one shared value emits **58 words / 12 register
differences**. Separating a current temporary changes the shape to 57 words
and is rejected. The repeated array-read expression in the accepted loop
recovers all 58 words directly under ordinary **O2/g3**, with no warning,
pool, guard or body substitution. The compiler unrolls the loop, retaining
the four conditional increment reads and original ordinary branches.

Raw target SHA-256:
`cb81a04908e36763bd2765801292a0a1052cdac6d76d81c008ad47b70b082af7`.
All **20 relative HI16/LO16 bindings**, including array-index addends, are
checked. All **29 other owner functions** retain their compact words,
lengths and relative relocations. The entire existing guard manifest,
Makefile, layout, conversion CSV and all other frozen inputs remain fixed.

## Fresh Qualification

All **nine final pre-install tests pass in 57.587s**. After installation,
the final **12 tests pass in 80.304s**, exit zero:

```sh
python3 -m unittest tools.tests.test_game_four_byte_saturation tools.tests.test_game_four_byte_saturation_installed -v
```

- **7,170 paired guest cases** cover boundary counter values, all 256 increment bytes, both stack phases and guest-only read-triggered increment mutations. Every one of the 58 instructions executes; complete registers/FP state, access traces, stack and surrounding bytes agree. All-saturated counters have exactly four byte reads and no increment read/store.
- **Native32 O2/O0**, separate translation units and selected-C UBSan, each exhaust all **65,536 start/increment pairs**, with permutations exercising every counter. Both selected binaries exit zero; six arithmetic/index/width negatives exit 20. The intentionally signed-byte negative needs only its expected type-range warning disabled; selected C keeps warnings as errors.
- All **nine compiled guest negatives** reject through observable results/access traces: signed counter, signed increment, wrap-before-clamp, wrong ceiling, missing fourth update, crossed store, updating saturated counters, skipping zero-step stores and caching the increment. Unsupported instructions/compiler failures do not count as effective controls.
- **56 fired fault-prefix pairs** compare literal guest state. These qualify emitted instruction order, not portable C fault behavior. Four independently assembled original rebase sets / **48 paired cases** change both symbol addresses, cross low-half carries and qualify guest-only increment/counter overlap and mutation. No native alias/concurrency claim is made.
- All **58 raw-word / 20 binding corruptions**, unexpected object data and all **92 frozen input** corruptions reject. Installed gates check all 92 live inputs, physical code/callback/accessor/data/symbol/string corruptions and both strict successor-fixture stages. No metadata ranges are excluded.

Both tools copies pass Windows syntax and all **eleven** shared WSL padder
tests. The older mirror uses unittest discovery because standalone `tests`
is not an importable package. Consumer `make tools-check` passes. No shared
helper is edited; unchanged neighbor-suite receipts remain prior evidence,
not fresh reruns. Routine Claude calls: zero.

## Actual Callback Boundary

The aligned ROM scan finds no direct JAL and two absolute registrations:

| Record | Pointer VA | Pointer ROM | Reached By Current Driver |
| --- | --- | --- | --- |
| 17, field +0x18 | 0x8008B834 | 0x2302F4 | Yes |
| 102, field +0x18 | 0x8008C978 | 0x231438 | No |

The real table base is **D_8008B4A8**, not the later data-owner label
D_8008B4D4. Current **func_15167010** is exact across all **23 words / 92
bytes**, ROM **0x1944C0**. It iterates **101 records / 0x1484 bytes**, stride
0x34, calls non-null field +0x18 without argument setup and ignores returns.
The frozen current table equals the retail bytes at ROM **0x22FF68**.

Eight connected cases execute this actual driver/table and restored leaf;
other registered callbacks are explicitly opaque and clobber caller-saved
registers. Record 17 invokes the target once. Registration 102 is preserved
but outside this loop. This does not prove its invocation, complete callback
effects, graphics or gameplay acceptance. Search ignored assembly with
`rg --no-ignore`; default directory searches omit original caller evidence.

## Image And Progress

Before production edits, capture the old link script and padded owner
object. The baseline full link reproduces the predecessor ELF byte for byte.
The qualified full link equals the declared slot-plus-symbol-extent image.
Production reproduces **all 164 changed bytes**, with no extra metadata
changes, exclusions or changes to any other ELF byte / **90 input keys**.
Protected data stays exact across **189,088 bytes / 720 owners**.

```text
before ELF acbf49495584a4d1f9b4917596f9cbea3e5a16535ea09d183e480223c8629c44
after ELF  1186370e78964af1417bcdf165ab7d24a41f9d8e02fd3fffcbda1e1c63c412de
after C    eaae6546b8b83a9791e64029926f2d54dbc386fce1f1cc5d2fa39bbe55229358
```

Fresh official totals: **Game 2,918/4,828 (60.44%)**, **total 3,591/5,501
(65.28%)**, different **1,910**, drift **0**. Init 492/492 and Debugger
181/181 remain exact. Conversions stay 5,501/6,044 (91.02%), converted
bytes 86.04%. Root README changes only its two aggregate matching rows.
The prior duplicate generated_12D630 recipe warning recurs; the build exits zero.

Tools **eee5a08** banks four experiment/checkpoint/test files first.
The older mirror retains HEAD **ddbdd16** and every one of its **787**
initial dirty-file hashes; copy only four newly owned absent files, ending
at **791** dirty paths. Do not commit/reset that mirror. Bank consumer C,
tools pin and docs separately, with no push. Allow the normal incremental
Graphify hook to finish, preserving retained excluded nodes; do not force
a broad scan. No host-port build/launch or frozen Release action occurs.

## Next Audit

The next same-owner placeholder **func_1516D738** spans ROM
**0x19ABE8..0x19AE4C**, VA **0x1516D738..0x1516D99C**, 153 words,
frame **0x98**. Its original uses record bytes, helper-produced display-list
state, cached halfwords and local packed output. On a cache-equal branch,
the load at **0x1516D874** reads **SP+0x5C** without the preceding branch's
stores executing. This is an observed instruction path, not yet proof of
an inherited-stack ABI or permission to invent zero initialization.
Audit helper writes and caller contracts before selecting its C model.
The wider matching goal remains open.

Follow-up [Note 1432](1432-projected-packet-draw-and-projection-byte-match-20261016.md)
locates [Note 1395](1395-packed-fade-scale-callback-and-renderer-deferral-20261015.md)'s
already-qualified positive inherited-stack evidence. Keep func_1516D738
C-deferred rather than repeating this as an ordinary local-initialization
problem; restore its projection/draw providers and continue at func_150958B0.
