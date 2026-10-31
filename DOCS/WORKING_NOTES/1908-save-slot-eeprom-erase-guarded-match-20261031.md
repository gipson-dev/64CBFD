# Working Note 1908: Save-slot EEPROM erase recovery

Date: 2026-10-31. Function `func_1500707C`, ordinary owner `conker/src/game_33990.c`.
ROM `0x3452C..0x34618`, VA `0x1500707C..0x15007168`. Tools checkpoint: `f2669f61c99fdaef1b9a85edbd2d969f21201972`.

## Recovered behavior and interface

The former zero-return placeholder is now `void func_1500707C(s32 slot)`.
It fills all eight bytes of `D_800BE358` with 0xFF, flushes cache, then reads
`D_8002AC5C`. If storage is enabled, it scans four signed slot-ID bytes at
`D_800BE3D8`. Every match writes EEPROM blocks `i*16+4` and `i*16+5` through
`func_151DD4E0(&D_800BE900, block, D_800BE358)`. Both statuses are ignored;
all matching slots are processed. Character-pointer arithmetic views the
complete four-byte sentinel object. Names and comments describe this behavior.

The secondary source calls these reads, but the original helper constructs
`CONT_CMD_WRITE_EEPROM` packets. The original caller at ROM 0x49B54 loads
signed `D_800BE3EC` into A0 in the JAL delay slot and ignores V0. No shared
header or public symbol-name change was needed.

## C generation and normalization

Retail has 59 words and a 56-byte frame. Complete semantic C emits 57 words
with existing O2/g3. Nine declaration/block-lifetime forms and ten discarded-
status forms did not produce an unguarded match; rejected receipts remain.

Twenty-nine explicit expected-word/relocation rows normalize closed saved-
register packing and spill slots, independent argument scheduling, and
the first discarded status assignment. Three insertions and one omission
produce all 59 retail words and eleven named bindings. This is guarded C,
not an unguarded compiler match. All 58 stale-word/binding controls reject.

The complete owner has zero diagnostics; all 17 neighbors and pools agree.
The actual three-command Make plan (IDO, ordinary padder, assembly) produces
the independently qualified padded object. This owner has no GLOBAL_ASM
preprocessor commands.

## Behavioral qualification

Guest: 9,216 cases; 36,864 normalized and 9,216 raw executions; three
independent code/symbol rebases; all 59 words reached; 24 public alias
cases; 120 fault-prefix cuts, including 32 branch-delay cuts. Callbacks
change the post-flush gate, later slot IDs and write-buffer bytes, overwrite
argument homes, and clobber caller-saved registers. Signed/full-word selector
bits and ignored errors are checked.

Normalized images agree in complete architectural and stack state. Raw C
uses different private spill slots: its checks compare public memory/access
order, ordered helper arguments, buffer observations and preserved registers.
Globals aliasing compiler-private spills are outside the portable raw-C claim.

Native32 O0/O2/O3 each pass 594,432 cases with trapping UBSan, covering all
256 signed/unsigned selector forms, all 16 match masks, gate values,
callback mutations and status patterns. Seven wrong semantic controls exit
1; compiler failures and signals do not count. The original five-word caller
window passes 192 cases, 3,072 normalized plus 192 raw executions, and four
V0 poisons. The aligned ROM census finds one JAL and no literal pointer.
No full large-parent, SI protocol, EEPROM hardware or gameplay claim is made.

## Linked image, production and count

Independent whole-image prediction accounts for exactly 187 changed bytes:
186 target code bytes and one symbol-extent byte; zero metadata changes or
exclusions. All 6,055 other bodies and every function address are preserved.
Protected Game data remains exact: 189,088 bytes across 720 owners.
Production ELF SHA-256:
`d4a370151ebe4e7d4b1037e84479848fd95b4398ab7018c29ec07dfb462720ac`.

Both tools copies pass eight fresh canonical methods and shared checks.
Postinstall, each passes two fresh checks; six unchanged semantic checks
are explicitly reused under identical module/input/artifact fingerprints.
The inventory CSV, inherited guard prefix, headers and other objects agree.

Actual adopted ELF: **3,985 / 5,506 (72.38%)** exact C; Game
**3,312 / 4,833 (68.53%)**; Init **492 / 492**; Debugger **181 / 181**.
There are 1,521 differing C functions and zero drift. Threshold 4,130
requires **145** more installed recoveries. Private work is uncredited.

## Evidence and continuation

Ignored stage: `conker/build/game-save-slot-erase-1500707C-match/`.
It retains frozen inputs, rejected probes, Make records, linked prediction,
behavior receipts, canonical tests and production/adoption audits.
The first transport and an inherited neighbor-count expectation failed;
corrected transport and fresh canonical checks supersede them. Signed LB
reads are explicitly tracked; older guest trace receipts are superseded.

Tools are committed before consumer source/guards/pin/docs. Root README
changes are two aggregate rows only. Graphify uses an explicit eleven-file
structural refresh; historical nodes and valid directed links are retained,
and the obsolete placeholder s32 return edge is retired. No full-corpus
extraction, clustering or centrality refresh is claimed.

Next screen: `func_15007558`. The 75% goal remains active. Preserve private stages,
the older tools mirror, build archives and sibling host/Release work.
