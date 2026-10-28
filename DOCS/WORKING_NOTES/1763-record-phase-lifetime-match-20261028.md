# 1763 - Record phase and lifetime direct C match

Verified: 2026-10-28. Target func_15169988, owner generated_196DB0.
VA15169988..15169A48 /ROM196E38..196EF8: 48 words, 192 bytes, frame 24.

## Complete source and original ABI

Replace the zero-return placeholder with void func_15169988(u8 *record).
Use the canonical callback table type, void (*)(void *), already declared
for D_8008CA20 in game_1944C0.c. Include structs.h and declare the release
interface with struct102 *, using an explicit cast at the call. Keep the
address-based symbol and descriptive record/selector/value/period/lifetime
names. These type repairs preserve the complete raw words and bindings.

1. Read the signed byte selector at record+0x40. Zero skips the table and call.
   Otherwise call D_8008CA20[selector](record). Retain sign extension, the
   original absence of a null/bounds check, and the live parameter home:
   save A0 at entered SP, then reload it after the optional callback.
2. Read the signed clock D_800BE9E4, signed halfword rate+0x28 and signed
   phase+0x26. Use u32 compound arithmetic to form the wrapped phase update.
   Period is the unsigned byte+0x41 shifted eight bits. If signed phase is
   at least period, subtract period once; otherwise add it once if negative.
   Preserve exactly one adjustment, including zero period and large steps.
3. Capture signed lifetime+0x24 before storing the phase halfword+0x26.
   Zero lifetime skips the second clock read and release. Otherwise reread
   the live clock after that store, subtract with modulo32 arithmetic, and
   release when the signed result is <=0. Only a positive result is stored
   back to the lifetime halfword; do not store a computed expired value.

The second clock read matters when its word aliases the lifetime/phase pair.
Callback mutation and guest argument-home redirection also affect which
record receives the updates. Native C callback tests use valid storage and
mutations; direct guest home writes remain a separate instruction-level test.
All 48 words are retained; 47 are reachable. The redundant lifetime store at
+172 follows an unconditional branch and remains intact.

The first source emits 48 words with eight allocation differences. Splitting
the phase assignment leaves one commutative-add word. An unsigned accumulator
with compound += recovers all words directly under normal O2/g3, while keeping
wrapped arithmetic defined. Six source forms are retained in the private fit
receipt. Canonical pointer declarations preserve the exact result.
No guards, inserted words, profile changes or fake fields are added.

Raw selected/original SHA256:
~~~text
0485506ae976faa1630ca8eb6e7aeaaa657f25a8b405ab88a291f838621f6436
~~~
Five bindings: callback-table HI16/LO16 at+12/+28; clock HI16/LO16 at+48/+52;
release J26 at+156. Preserve all five across independent GNU layouts.

## Retail registration, dispatcher and retained release code

The aligned ROM census finds no direct JAL/tailJ and one pointer at ROM231280,
VA8008C7C0. This is the update callback in descriptor type 0x5E (94):
D_8008B4A8 +94*0x34. The original creator func_15169900 requests type 0x5E.
The descriptor also points to the still-unrecovered func_15169A48 renderer;
its definition remains unchanged and uncredited.

Frozen data owners 22FF40.rodata.s and 22FF90.rodata.s establish the descriptor
and D_8008CA20 extent. The optional table has 11 entries, including its two
opening nulls. Zero selector skips access; other signed selectors retain
retail's unchecked dispatch. All-byte guest/native backing tests do not claim
that every byte is a valid index into this eleven-entry retail table.

The actual 11-word func_151670C0 window at VA15167158 /ROM194608 reads the
registered callback, saves next+8 in the pending-record slot before the call,
and passes the record in A0. Its current C/ELF definition is an unchanged
three-word stub, so original execution is distinguished from production.

Fifty-four connected cases run that window and the selected callback, then
connect the original/current-byte-exact release wrapper func_1516972C
(28 words), queued-record scan func_151696DC (20 words), and adapter
func_15169804 (eight words). The scan updates pending references from the
released record to its next pointer; type 94's null destructor selects the
adapter. Only final func_15168B10 is a bounded unlink provider in this test.
No complete list service, full dispatcher recovery or gameplay claim follows.
No retained original assembly source for these helpers was located; original
instruction provenance is the checksum-frozen retail ROM plus independent GNU
disassembly, checked against current ELF bytes. Do not cite a nonexistent ASM.

## Fresh focused qualification

Both tools copies pass eight fresh canonical methods and shared project-tool
checks. Installed copies each pass two fresh owner/image methods; six semantic
methods are reused only after exact input/module/artifact identity checks.

- 4,740 guest cases cover every selector byte, sign extension, callback field/
  clock/next-pointer mutations, volatile GPR/FPR/HI/LO and outgoing-home clobbers,
  guest live-home redirects, signed halfword boundaries and wrapped tick values.
  Every aligned clock alias across the 80-byte record is checked. Compare an
  independent effects/call reference and literal complete private state/trace.
- Native32 O0/O2/O3 with trapping UBSan each pass 524,296 positive cases.
  Use valid typed record storage, whole-storage fences, a 512-cell offset
  callback backing table, all selector/period bytes and all halfword phase
  encodings. Distinct positive/negative callback tags make an unsigned-index
  variant fail by behavior without out-of-bounds access. Eleven wrong C forms
  fail effectively, including full-modulo, eager-expiry-store and <= boundary
  changes. Native clock storage is disjoint or a valid s32 record cell;
  overlapping-halfword clocks and direct homes are guest-only probes.
- 285 fired root access prefixes preserve complete state, trace, fault PC and
  branch-delay ownership. Zero selector needs no table mapping or home store;
  zero lifetime reads the clock once and never releases.
- Three independent GNU layouts pass 27 cases and preserve all five bindings,
  signed low-half carries and negative selector indexing in bounded memory.
  Three raw/binding and six entire-image corruptions fail closed. The actual
  padder reproduces the object byte-for-byte.
- An actually compiled cached-clock negative fails on the live clock alias
  at record+0x24. Initial lifetime -1/phase0/rate1/period3 causes retail to
  store lifetime 64767 after the phase changes the clock word; the cached
  variant stores 65535. The rejection is by value, not an unmapped-read shortcut.

Preserve the initial route-inspection receipt that used an incorrect inventory
column name; the corrected extractor uses length, completes with exit 0 and
retains raw/disassembly receipts. All final tests pass without weakened flags
or gates. Routine Claude calls: zero.

## Actual Make, exact image and measured progress

The owner has four compact functions and no GLOBAL_ASM routines. Preserve
all three neighbors, bindings and pools. The actual three-command IDO/padder/
GNU Make route and production reproduce the qualified object. Selected,
owner and actual Make diagnostics are empty; the inherited duplicate
generated_12D630 Make recipe warning remains.

The entire adopted ELF equals the independently predicted 136-byte delta:
135 target-code bytes and one target-size byte 12->192, with zero exclusions.
All 6,056 function addresses, 6,055 other bodies, named definitions and 720
protected Game-data owners /189,088 bytes remain fixed. Shared headers,
retained helper/dispatcher source and objects, data owners, map, inventory
CSV and the prior guard manifest remain unchanged.

ELF SHA256:
~~~text
cc2ca2d66d3026bb183b2eb1dc9381d86707bbeff2c972dd5f6ed9099d352a61
~~~
Unchanged Native CRLF guard SHA256:
~~~text
7a8a7a39ff6271b22dfb93589c78def9bf0b04d022adb5795ce3afa044c226a6
~~~
Seal 16,242 Native/cache inputs and 242 focused inputs. The actual captured
Native ELF recount, with unchanged C inventory/classifications, gives:

| Section | Exact C functions | Different | Drift |
| --- | ---: | ---: | ---: |
| Total | 3,841 /5,506 (69.76%) | 1,665 | 0 |
| Init | 492 /492 (100.00%) | 0 | 0 |
| Game | 3,168 /4,833 (65.55%) | 1,665 | 0 |
| Debugger | 181 /181 (100.00%) | 0 | 0 |

Only func_15169988 becomes exact. The 4,130 threshold leaves 289 more to 75%.
Remaining shapes: 1,536 placeholders, 120 semantic/other and nine unlocated.
Keep typed func_151725FC and NULL func_1518F5D0 uncredited.

Predecessor consumer cb3f130477e8498391969cabb169077522e75cf3 and tools
c57fb83690ae63f4645136eb9c5fec5464f3e3ec. Bank tools first at
35c985f745fdc603ba3d123016dbb828b61c6729, then the source, tools pin and
seven measured documents. Preserve the older mirror's 1,736 inherited dirty
paths plus the two new files. No push. Root README changes only its two
aggregate matching rows; detailed function updates remain here.

Refresh ten changed structural C/Markdown/tool sources, retaining old nodes
and every still-valid confidence/context relationship. Retire only the target
stub's false s32 return after validating the final void interface. Validate
its u8 pointer, canonical callback table and release call against committed
source and object bindings, without inventing caller/indirect-callback edges.
Outside freshness and communities remain historical; no full-corpus extraction
or global clustering/centrality claim. Detailed receipts and independent audit
live under conker/build/game-record-phase-lifetime-match/.

Next inspect func_1512B53C using a fresh predecessor and caller/ABI audit.
func_1514E920 remains parked/uncredited. The 75% goal remains active.
