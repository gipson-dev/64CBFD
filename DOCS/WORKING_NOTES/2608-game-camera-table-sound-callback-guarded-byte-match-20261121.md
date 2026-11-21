# Note 2608: Camera table-sound callback guarded byte match

Date: 2026-11-21. Consumer baseline `64df4fa598754e27bf384d0afe9e81b17a232d34`;
tools baseline `03694d0a53897ad3ab52c6e7cc05fb899ea00a1d`. Qualified tools commit: `7708beb847e33d9461a8786ae1dad95eb2ef8996`.

`func_15127520` replaces its zero-return placeholder with the complete
table-driven camera sound callback. All **164 words / 656 bytes**, the
**72-byte frame**, saved S0/RA, original spill home and nine relocation sites
are recovered. **Four checked scheduling guards** restore two independent
call sequences. There are **zero insertions or omissions**. All **44 owner
neighbors**, pools and five existing warnings remain unchanged.

Production recount: **4,592 / 5,528 (83.07%)** total, **3,919 / 4,855 (80.72%)**
Game, zero address drift and **936** still different. Init 492/492 and Debugger
181/181 remain exact. **107 more** matches reach 85% at this denominator.
Converted rows remain unchanged because the previous placeholder counted as C.
The main README receives only its two aggregate matching rows.

## Recovered behavior

Owner `game_14FF90`; VA `0x15127520..0x151277B0`, ROM
`0x1549D0..0x154C60`. The seven-argument callback receives the shared sound
record, five unused mix-value pointers and a pending sound ID pointer. Bit 31
of the packed history selects one six-byte row of `D_800894E0`; low 24 bits
hold the previous comparison value. The original rows are **0x603/0x604/0x605**
and **0x620/0x621/0x622**. Camera field +0x1A4 is multiplied by `D_800A3580`,
whose original bits **0xC61C4000** represent **-10000.0f**.

The reset ID is cleared, primary-actor coordinates are truncated into the
record, and secondary actor state must equal 2. Other states return 1. Active
state converts the snapshotted product to unsigned 32-bit, compares the full
converted word with the old low 24 bits, and stores `(selector << 31) | value`
when changed. The conversion result is preserved at full width.

A changed value selects the row's first ID after releasing a nonzero handle
when needed. An unchanged first ID transitions to the second ID and emits
`func_10010F30(id, 20000, 64, 0, 0)`. Another unchanged path with flag 0x80
submits the camera event and emits the third ID. Active paths clear flag 0x80
in the original order and return zero. Table/provider mutations and sound-ID,
handle, coordinate and table-halfword aliases remain visible to reloads.

The source reuses `CameraSoundRecord14FF90`, declares the measured two-row
table and float constant, and uses the camera event helper's real `void *`
interface. Shared headers and profiles are unchanged. The first source had
164 words/frame 80 and 117 differences. Removing the redundant packed snapshot
recovered frame 72 and ten differences. Using the cached float directly in
the comparison/store recovered the original spill home and left four words.
The two source casts emit **one unsigned-conversion sequence**, including its
normal IDO fallback path. Union, narrow-selector, padding and comma screens
were rejected. The adopted source retains ordinary scalar expressions.

## Scheduling, guest and native qualification

Raw payload SHA256:
`79226ad5f9b01234ebb9954104070a677c85fbeb8ef67991117b1e91a9057758`.
All **160 non-window words** are literal. At words 128/129, the table load
and outgoing zero store exchange order. At words 147/150, the table load and
zeroing A3 exchange positions around the delayed call. The table address,
outgoing argument and link-register update are independent; delayed callees
observe identical five-argument values. The structural certificate and **64
window cases** check both rows, phases, data bases and unsigned halfword edges.
Four altered-word controls fail. Its explicit domain keeps fixed global table
storage disjoint from automatic outgoing storage.

Independent guest execution passes **1,824 cases per stream** for original,
raw and padded bodies. It covers **all 162 normal-entry reachable words**;
words **80 and 137** are unreachable duplicate loads, established by decoded
control-flow traversal. All 164 guarded words still match literally. Cases
cover all actor-state bytes, both rows, unsigned-conversion boundaries,
negative fractions, invalid/overflow fallback, aliasing and provider mutations.
The explicit FCSR model checks control save/restore across the conversion.
It is a bounded model of those instructions, with arithmetic flag/hardware
acceptance outside its scope.

Raw comparisons canonicalize only the four declared scheduling positions;
public RAM, private bytes, preserved ABI state, calls and canonical accesses
agree. **158 memory-access fault prefixes** compare original and padded code.
Raw C has its own legal access order and has no fault-prefix parity claim.
Four effective guest instruction controls fail.

Native SDK32 passes **1,608 cases each at O0/O2/O3**, with strict aliasing,
UBSan and seven effective source controls. These use actual SDK camera/actor
objects and legal typed record/table aliases. Float-to-unsigned integral parts
are representable; invalid guest conversions and explicit FCSR state remain
separate. The first attempted flag control changed an earlier redundant clear
and was ineffective on the corpus; mutating the common final clear provides
an effective control. SDK/private offset and extent assertions pass.

## Original caller, links and whole image

A fresh census finds two constructed original references at
`0x151268FC/0x15126900` and `0x15126A0C/0x15126A10`. There are no direct JAL/J
sites or aligned loaded-pointer literals; computed references remain possible.
The registration parent `func_15126378` remains a placeholder. Its reference
sites are original-ROM/sealed-ASM evidence. The Init constructor/dispatcher
windows and 11-word camera-event provider are literal in the frozen ELF.

The original **24-word dispatcher window at 0x10011848** passes **640 cases
per stream**, checking all seven argument addresses, both return branches,
pending sound ID, five unused mix locals and FCSR restoration. Three caller
controls fail. Deletion uses a bounded provider contract; the full outer
dispatcher and natural gameplay through the unfinished parent are separate.
Six GNU links cover original and code+0x10010/data+0x18020 bases, including
HI16/LO16 carry. Raw links match independent raw binding; original and padded
links match retail. The isolated raw target preserves its complete payload
and bindings; full-owner coverage comes from Make and image checks.

The natural mixed GLOBAL_ASM recipe runs five commands under existing O2/g3.
The normal production rebuild and strict predictor cover **6,051 slots**,
**533 changed bytes**, **zero exclusions** and no unexplained differences.
Declared changes are the target body, symbol size **12 to 656 bytes**, and two
closed symbol/string permutations involving **seven records / 80 string bytes**.
All named definitions otherwise remain unchanged. All **189,088 protected
Game-data bytes / 720 owners** remain exact. Production ELF SHA256:
`a722ffc7e495439196f51276dc2188a9195863ad1432cb2783dc0a9df3ac4360`.

The guard file preserves every prior byte and appends only four owned rows.
Five focused checks pass in both configurations before and after adoption;
shared `make tools-check` passes. Eight tools files are committed first. The
private hybrid has 1183 files, preserving the real dirty sibling
HEAD/status and 352 dependency hashes. The production
audit checks 2314 frozen inputs. Earlier unchanged broad
suites are reused by fingerprint and are not reported as fresh.

Graph updates retain old IDs and qualification metadata. A native smaller-corpus
refusal plus serial scoped extraction is distinct from a full-corpus refresh.
The available host scene input/configuration is inspected read-only; no host
source import or runtime parity is inferred. No Make/profile/shared-header,
host/Release/ROM/save changes, push or Claude calls. The 85% goal remains active.
Next candidate: `func_151256BC`, a 154-word/frame-56 camera placeholder, requiring
fresh source, ABI, caller and image qualification.

```sh
python3 -m unittest tools.tests.test_game_camera_table_sound_15127520_match -v
make -C conker -j4 build/conker.us.elf progress.csv
make tools-check
```
