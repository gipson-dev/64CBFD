# First marked record bit - direct C match

Verified 2026-10-28. Restore func_151140C4 in generated_13D350:
VA 0x151140C4..0x15114188, ROM 0x141574..0x141638, 49 words / 196 bytes.
The existing normal O2/g3 profile emits the entire routine directly with no
frame, four global relocations and no word guards. Automatic loop unrolling
reproduces the original four-bit scan. The retail symbol name is retained.

## Recovered behavior and interface

The recovered interface is s32 func_151140C4(u8 *record).

1. Test bit 0x80 of record[0x4F]. If clear, return zero without reading either
   global pointer or the mask table.
2. Calculate the record index from the signed byte-pointer difference against
   D_800DBEF4, divided by the 0xA0-byte record stride with truncation toward zero.
3. Load that record's signed 32-bit mask through D_800DBF94.
4. Scan bits from zero through 31 and return the first set bit's index.
   An empty mask returns zero, as does a set bit zero.

Keep the unsigned 1U shift so bit 31 is defined in C. A signed local mask
recovers the original commutative AND operand order; the first unsigned-mask
shape differed in four words. The selected body adds no unsafe signed shift,
new shared declaration, compiler-profile change or helper call. Native tests
use pointers within one backing array. Sparse extreme-address guest fixtures
qualify the original 32-bit arithmetic, not arbitrary portable C pointers.
All 33 other owner functions, their bindings and constant pools are unchanged.
The two existing GLOBAL_ASM routines remain in place.

## Original dispatcher and retained lookup

The aligned ROM census finds one direct JAL at ROM 0xCC340 / VA 0x1509EE90
inside func_1509ED74, a 159-word dispatcher with a 56-byte frame. No target
pointer literals occur. Its 17-entry table jtbl_8009F43C selects commands
0x13..0x23; command 0x17 reaches this function. The parent masks the selector
to eight bits, resolves it through the existing 28-word func_151149AC, and
passes the resulting record pointer in A0. A successful result is ORed with
0x2000; null lookup and out-of-range commands return zero.

435 connected cases execute every reachable word of the command-0x17 route,
covering 35 parent words, every lookup word and all target words. They cover
first/last/missing records, selector narrowing, zero/negative record counts,
flag and mask combinations, and two stack phases. Two separate negative-result
controls exercise the parent's rejection branch; the actual target returns
only 0..31. The current lookup and literal switch table match retail.
The parent's other command routes are not qualified here. Its C placeholder
remains uncredited; these tests execute the original parent instructions.

## Qualification and production

Both tools copies pass eight fresh canonical methods and shared tools checks.
After installation, each passes two fresh checks of the installed owner and
entire image. Six unchanged semantic methods per copy are reused only with
identical frozen inputs, module hashes and qualified artifacts.

- 17,521 guest cases visit all 49 words and compare complete machine state,
  return values, memory and access traces across retail, raw C and padded C.
  They cover every flag byte and single bit, signed quotient boundaries,
  extreme 32-bit differences, and pointer/flag/table aliases.
- 37 access-fault prefix triples preserve state, trace, PC and delay slot.
  Disabled records read only the flag; global pointer cells remain unmapped.
- Native32 O0/O2/O3 each pass 139,776 cases with trapping UBSan, complete arena
  and table preservation, and nine effective semantic negative controls.
  A separate signed bit-31 shift control traps. Nine IDO-compiled semantic
  negatives also fail the guest checks as expected.
- Three independent GNU layouts pass 108 guest cases and exercise HI16/LO16
  carries. Three raw/binding corruptions and six entire-image corruptions
  are rejected. The actual generated padder reproduces the qualified object.
- The actual five-command Make recipe includes GLOBAL_ASM processing and the
  generated padder. It reproduces compact and padded owner output with no
  selected, owner or recipe compiler diagnostics. The full build retains
  the known unrelated duplicate generated_12D630 recipe warning.

The qualification seal covers 16,400 paths and 379 focused inputs. Production
reproduces the independent entire-image prediction: exactly 149 changed bytes,
comprising 148 code bytes and one symbol-size byte (12 -> 196), zero exclusions.
All 6,056 function addresses, 6,055 other linked bodies and 720 protected Game
owners / 189,088 bytes remain unchanged. The complete guard manifest, shared
headers, Makefile, retail layout, conversion inventory and other objects are
preserved. No guard is added or removed.

Private fixture corrections were made before canonical qualification: wrap
reference subtraction to 32 bits, exclude the first command-0x13 instruction
from command-0x17 coverage, and supply the object to the rebase linker. A later
inventory driver retained the previous target name; the corrected fresh run
verified all canonical function views. Neither correction changed production C.

| Artifact | SHA-256 |
| --- | --- |
| Raw C and original relocatable body | 590c2f8d2309a42e9b98853caa34b675ddf534e35f8857003e1aeb67b9b50fa9 |
| Linked retail slot | 33416e303519bb77f9a002bddd301cdc118eb0f1ff34f157b0a3d2027cba9549 |
| Adopted owner object | c3c5d589c0ebee18778b6ba482d8b5f02345fde7031b45712bc6ef25c4f55cbe |
| Adopted ELF | 40040146d7a6d2ee87ade76ba8bd2351f8c53f595c6884adaf554802091794d9 |
| Unchanged guard manifest | 91cfc61697b2f874f74475c5dadac1faec1f2e3c4f2a515d593b62d15b71ba03 |

## Bank and measured progress

Predecessor consumer: 72956d690e347c4ae29cf29120c23d4e58382242.
Tools committed first: 5b1c4638e37e9027563ba6df41a967c767ecc16c.
The consumer commit records this source, tools pin and measured documentation.
No push is performed. Preserve all 1,799 inherited older-mirror dirty paths
and the three new qualification modules; do not reset or commit that mirror.
Routine Claude budget/calls: zero. No emulator or gameplay claim is made.

| Section | Byte-exact C | Address drift | Different |
| --- | --- | --- | --- |
| Total | 3,864 / 5,506 (70.18%) | 0 | 1,642 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 3,191 / 4,833 (66.03%) | 0 | 1,642 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

266 more exact functions are needed to reach 4,130 / 75%. Remaining source
shapes: 1,513 placeholders, 120 semantic/other and nine unlocated. Only this
function receives new credit. Keep func_1514E920 parked and uncredited.
Next inspect func_1514F308; screening alone earns no credit.

Retained evidence: conker/build/game-record-first-marked-bit-match/ contains
preparation.json, canonical/installed receipts, sealed-production-proof.json,
sealed-live-adoption-audit.json, canonical-function-views.json and
75-percent-queue.json. The final handoff records the consumer commit, scoped
AST graph refresh and independent closing audit. Root README changes only totals.
