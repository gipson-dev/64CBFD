# 1757 - Record effect packet direct C match

Verified: 2026-10-27. Target func_151A18DC, owner generated_1CC440.
VA 151A18DC..151A1998; retail ROM 1CED8C..1CEE48.

## Complete direct C and packet layout

Replace the zero-return placeholder with the complete void callback:
~~~c
void func_151A18DC(struct260 *record);
~~~
All 47 words /188 bytes emit directly from normal O2/g3. Preserve the 88-byte
frame, S0/RA lifetimes and two R_MIPS_26 bindings at +140/+160 to
func_151491F4 and memcpy. Zero guards, no profile override and no added
padding fields are needed. The new local packet is exactly 32 bytes:

| Packet offset | Captured value |
| --- | --- |
| +0x00/+0x04/+0x08 | three position words from record+0x28/+0x2C/+0x30 |
| +0x0C | float from record+0x34 |
| +0x10 | positive-zero phase |
| +0x14 | float from record+0x38 |
| +0x18/+0x1A/+0x1C/+0x1E | halfwords from record+0x3E/+0x40/+0x42/+0x44 |

Capture all 32 bytes before calling the factory. Its eight arguments are
signed lifetime from record+0x3C, -1,3,1,0,32, unsigned slot byte+0x0C and
unsigned context byte+1 promoted to the final word argument. Reuse the
canonical typed func_151491F4 interface. If it returns nonnull, copy all 32
captured bytes to result+0x28. Allocation failure still reads and captures
the source; it skips only the child/copy operation. The provider can change
the source after capture without changing the packet unless the guest
addresses themselves overlap.

The pointer declaration precedes the packet declaration. The initial
packet-first source already had 47 words/frame 88 and correct bindings, but
nine local addresses were four bytes high. Swapping those two ordinary
local declarations restores the original packet at SP+0x34 (incoming SP-36)
and all 47 words. Preserve initial-fit objects, initial-packet-input.c,
fit-order.json and the selected source; do not credit the first shape alone.
A first private driver had retained a predecessor work-directory namespace
and stopped at the input-seal gate before compiling. The corrected driver
uses this owned output directory. No production code was changed for that
transport failure.

The position uses a real three-float value copy; all packet fields are
explicitly assigned, with no unwritten packet padding. Add local layout
views and the existing structs.h include, without changing shared headers.
The complete owner has 39 compact functions. All 38 other functions, their
bindings, pools and all six GLOBAL_ASM routines remain unchanged.

## Callback registration and complete original dispatcher

The aligned ROM census finds no direct JAL or tail J and one pointer literal
at ROM22EF8C /VA8008A4CC: slot3 of the ten-entry D_8008A4C0 table in
asm/data/22EF80.rodata.s. Its existing declaration is a void(struct260 *)
callback array. The identified expiration dispatcher func_15149264 passes
the record in A0 and observes no callback return value.

2,304 cases execute all45 original dispatcher words at
VA15149264..15149318 /ROM176714..1767C8, which are identical to the retained
ELF body. Cover timer enable/disable, signed-halfword lifetime wrapping,
update sentinel and callback gates, death sentinel/slot3, update-provider
changes, null/successful child allocation and post-callback lifetime changes.
The final lifetime is reread after the callback before optional cleanup.
The updater and cleanup are bounded contracts; the complete dispatcher body
is exercised, without claiming the complete implementations of those providers.
It was already retained C and receives no new matching credit.

## Fresh qualification and connected helpers

Both tools copies pass eight fresh canonical_v2 methods and shared project-tool
checks in 15.307s /15.301s. The first canonical run passed seven methods and
stopped native compilation on an unused fixture helper under -Werror.
Remove that unused helper while retaining the strict flags. Preserve the
failed receipts; the recovered C and prepared objects remain unchanged.
Installed copies later run two fresh owner/image checks and reuse six
semantic methods only after exact input/module/artifact fingerprints.

- 8,848 guest cases cover every slot/context byte, signed-halfword boundaries,
  raw position/float patterns, null and successful allocations, four source
  layouts and four returned-record destinations. Private source aliases and
  forward-overlapping copies are tested as literal guest behavior. Providers
  can change the source, packet bytes and caller lifetime. All47 root words
  are dynamically exercised; compare complete private RAM/GPR/FPR/events/
  visits and ordered access traces, plus all 32 captured and copied bytes.
- Native32 O0/O2/O3 with trapping UBSan each pass 524,288 positive cases.
  Sweep all 65,536 halfword values and all slot/context byte pairs, two
  allocation states, two source-mutation states and two valid destinations.
  Check every defined packet byte, source changes after capture, complete
  input/output storage and surrounding fences. Ten deliberately wrong C
  variants fail effectively. Native buffers are disjoint; guest-private
  stack overlaps and FCSR/hardware behavior are outside this native contract.
- 240 fired access-prefix pairs preserve private state, trace, PC and delay
  ownership. Null allocation needs no child mapping while still capturing
  all source fields. Three independent GNU layouts pass 18 guest cases with
  both J26 bindings. Three raw/binding and six full-image corruptions fail
  closed.
- An actually compiled late-capture variant is rejected by its copied packet
  after the constructor changes the source. The negative fails by result,
  without an unmapped-read shortcut.

80 additional connected cases map the complete original/retained helper chain:
func_151491F4 (28 words), func_15149130 (49), func_15167A68 (28) and
memcpy (11), 116 words total. Every mapped helper body equals retail/current
ELF bytes. The rooted cases visit 28/47/28/11 words respectively; the two
main-constructor words for its alternate kind95 branch are outside this
callback's fixed flags1 path. Do not claim those two words were exercised.

Verify the real eight-to-nine argument expansion, allocation kind35,
72-byte allocation, slot/context stores, signed lifetime and callback header
fields, 16 zeroed state bytes and the complete 32-byte payload copy. Heap,
registration and bzero providers remain bounded. The retained constructor's
legacy pointer spelling for its numeric size slot is unchanged; these
literal guest integrations do not claim portable execution of that entire
old helper C pipeline. No new helper conversion or live gameplay acceptance
is credited. Routine Claude calls: zero.

## Production and complete image preservation

The actual five-command asm-processor/IDO/postprocess/padder/GNU assembler
Make route reproduces the qualified object byte-for-byte, including all
six retained assembly routines. Target and complete-owner IDO diagnostics
are empty. The inherited duplicate generated_12D630 recipe warning remains.
Production Make exits zero in 0.566s.

The entire adopted ELF equals the independent 141-byte prediction:
140 target-code bytes and one target-size byte, zero exclusions. Only the
target extent advances 12->188; no metadata cycle is introduced. All 6,056
function addresses, 6,055 other bodies and all other named ELF definitions
remain fixed. Protected Game data stays exact across 720 owners /189,088
bytes. The map, inventory CSV, guard manifest and shared headers are unchanged.

ELF SHA-256:
~~~text
b160a355f28b36f0a7e432e9f44183b400a5f35735adc98de33a65a232fd3ce6
~~~
Native CRLF guard SHA-256 (Git-normalized LF content is identical):
~~~text
f867c3817abab6b6ef822343afa48a4b188e7067ce1d4c69a078b54a6f4b4c40
~~~

Seal 16,212 Native/cache inputs and 203 focused inputs. Recount the captured
adopted Native ELF with the unchanged C inventory:

| Section | Exact C functions | Different | Drift |
| --- | ---: | ---: | ---: |
| Total | 3,835 /5,506 (69.65%) | 1,671 | 0 |
| Init | 492 /492 (100.00%) | 0 | 0 |
| Game | 3,162 /4,833 (65.43%) | 1,671 | 0 |
| Debugger | 181 /181 (100.00%) | 0 | 0 |

Only func_151A18DC becomes exact. Converted totals stay fixed. Threshold
4,130 leaves 295 more matches to 75%. The remaining source screen contains
1,542 placeholders, 120 semantic/other definitions and nine unlocated entries.
The typed func_151725FC zero-return provider and func_1518F5D0 NULL factory
remain placeholders and uncredited.

Predecessor consumer fe2ba388cb1cac2a7f3c9ccae02985ba93b8a1a3 and tools
44b34edbf6e12ebce84d452b14f5787944d64440. Bank tools first at
270010858c73aebeda411d70c12d69981ce70b5f, then the source, consumer pin and
measured documentation. Preserve the independent older mirror's 1,724
inherited dirty paths plus two new tools files. No push. The root README
changes only its two aggregate matching rows.

Refresh ten changed C/Markdown/tool sources structurally, retaining all prior
nodes and still-valid relationships/contexts. Retire only the target's
obsolete placeholder s32-return relationship against the recovered void
callback declaration. Validate its canonical struct260-pointer parameter
and two actual calls against source and R_MIPS_26 bindings. Outside freshness
and communities remain historical; no full-corpus extraction or global
clustering/centrality claim. Receipts and the independent final audit remain
in conker/build/game-record-effect-packet-match/.

Next inspect func_151ED1E0 in generated_215960 using a fresh frozen predecessor
and caller/ABI audit. Keep func_1514E920 private and uncredited. The 75% goal
remains active.
