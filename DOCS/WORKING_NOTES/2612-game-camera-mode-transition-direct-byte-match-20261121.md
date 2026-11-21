# Note 2612: Camera mode-transition direct byte match

Date: 2026-11-21. Consumer baseline `973588462e77db54644dedec2fc248209fc349d1`; tools baseline
`acc3dda6113738eaf82dccb3fb552e456188f477`. Qualified tools commit: `8c4c1d088f021beffa40c0d7ef4915370c2fb7f1`.

`func_1512317C` replaces its zero-return placeholder with the complete camera
mode-0x100 gate, actor transition-state maintenance and two scalar springs.
All **227 words / 908 bytes** emit directly from semantic C, including the
**40-byte frame**, S0/RA saves and six R_MIPS_26 relocations. There are **zero
guards, insertions or omissions**. All **44 owner neighbors**, pools and four
existing diagnostics remain unchanged. Shared headers and compiler profiles
are unchanged.

Production recount: **4,596 / 5,528 (83.14%)** total, **3,923 / 4,855 (80.80%)**
Game, zero address drift and **932** still different. Init 492/492 and Debugger
181/181 remain exact. **103 more** matches reach 85% at this denominator.
Conversion rows are unchanged; the placeholder already counted as C. The root
README receives only its two aggregate matching rows.

## Recovered behavior and source shape

Owner `game_14FF90`; VA `0x1512317C..0x15123508`, ROM
`0x15062C..0x1509B8`. The routine snapshots camera flag bits 0x100/0x200 and
builds the stunned-state gate, with exclusions 9/0x38/0x39/0x3B/0x37/0x15/0x26/
0x3A. Ordered short-circuit checks combine mode/flag gates, actor float +0x28,
water byte, secondary flags, state 3, actor byte +0x65 and the query helper.
After that query, the primary actor is reloaded before health and speed tests.
The secondary type low nibble and byte +0x1AC complete the predicate.

Held and edge bit 0x10 control the indexed mode-save helper. A successful save
dispatches `func_1511FC60`. Otherwise mode 0x100/substate zero invokes the
restore helper, clears secondary bytes +0x198/+0x197, writes camera halfwords
+0x5F8=1/+0x5FC=2 and clears input flags. The routine publishes the low byte
of signed substate +0x73C to the secondary actor. A nonzero substate runs two
six-argument springs with target 0, strength 4, damping 9 and fresh delta-time
loads, then clears substate when the current mode is not exactly 0x100.

The original redundant `substate != 0 || substate == 3` expression is retained;
its comparison and branch words remain literal. The SDK exposes the relevant
actor and camera fields; a local existing may-alias short type covers +0x5F8,
and native SDK/view storage asserts the four float spring offsets. No shared
layout is changed.

The first source had 226 words/frame 48 because it kept the initial actor
across the query. Fresh pointer expressions recovered 227/frame 40 but seven
register differences remained. Assigning the reloaded pointer to the existing
actor local recovered the original A1/V0 allocation. Naming the secondary
local also matches, but the smaller source is selected. Raw payload SHA256:
`0591d92a435eff1b30b2070fc64e7a766119b7520ae98caad1d137748dd74556`.

## Execution, caller and relocation evidence

Guest qualification passes **3,293 cases per stream** for retail/raw/padded
code, comparing all public RAM, private bytes, GPR/FPR/HI/LO state, calls and
ordered accesses. Cases cover all byte values for six selectors, stunned
exceptions, old flag combinations, ordered/NaN/infinite predicate values,
zero, positive and negative signed substates, valid actor/input aliases, guest-only camera/actor
storage overlap and provider changes to primary/secondary/input pointers and
delta time. All **226 normal-entry reachable words** are covered. Word 147
is a statically skipped duplicate load; all 227 emitted words are literal.
**110 interrupted-access prefixes** agree in full modeled state. Three guest
instruction controls reject changed old-flag, stunned-exclusion and input
gates. Missing exception/fallback examples found by the first coverage check
were added before acceptance.

The actual original/current **38-word save**, **34-word restore** and
**54-word spring** helpers are connected in **192 cases per stream**, covering
all **124 reachable words** in their combined 126-word bodies. Query,
activation and downstream reset/index behavior use explicit ABI/effect
contracts. The 318-word activation routine remains unfinished and nonmatching;
this recovery does not qualify its complete behavior. FCSR exception flags,
complete providers, hardware and natural gameplay acceptance are outside the
test scope.

Native SDK32 passes **3,254 cases each at O0/O2/O3**, with strict aliasing,
UBSan, SDK/view offset/extent assertions, recovered save/restore/spring C and
**nine effective source controls**. The independent model compares the full
camera, actor and input storage plus calls. Native floating cases are finite;
overlapping camera/actor storage remains guest-only. Private native frame
layout is not claimed.

A fresh ROM census finds **one direct call** and no aligned loaded-pointer
literals; computed references remain possible. The **four-word original
caller window at 0x15122F10** passes **256 cases per stream**, including the
S0 camera delay-slot argument and the following index-helper delay. Two
controls skip the target or pass a valid alternate pointer to the next call.
The current parent `func_15122C5C` remains a placeholder: this is original-ROM
window evidence, not a claim that its current full body matches.

Six GNU links check retail/raw/padded targets at two code bases, retaining
the padded owner base 0x15122AE0 and internal helper definitions. Target
relocations are **R_MIPS_26 only**; no target data relocation or HI16/LO16
carry is claimed.

## Whole image and bank

The natural mixed GLOBAL_ASM Make recipe runs five commands under existing
O2/g3. Production equals the independent full-image prediction across **6,051
slots**, with **727 changed bytes / zero exclusions**. Only the target body
and its symbol extent **16 to 908 bytes** change. There is no symbol/name-order
permutation. All other definitions and section geometry are unchanged. All
**189,088 protected Game-data bytes / 720 owners** remain exact. ELF SHA256:
`b3c4fd50148341e677b3eb9de6a87af1ef2c97bad8f6e788c9ec876a38c684e3`.

The complete guard CSV remains byte-for-byte unchanged. Five focused checks
pass in both tools configurations before and after installation; shared
`make tools-check` passes. Seven tools files are committed first. The private
hybrid has 1211 files, preserving the real dirty sibling HEAD/status
and 352 dependency hashes. Production audits
2361 sealed inputs. Earlier unchanged broad receipts are
reused by fingerprint and are not described as fresh tests.

Scoped Graphify refresh retains prior node IDs and qualification metadata
after the native smaller-corpus refusal; this is not a full-corpus extraction.
Available host scene configuration/input is inspected read-only without an
import or runtime-parity inference. No host/Release/ROM/save changes, push or
Claude calls. Next: inspect `func_15128030` from this committed baseline.
The **85% goal stays active**.

```sh
python3 -m unittest tools.tests.test_game_camera_mode_gates_1512317c_match -v
make -C conker -j4 build/conker.us.elf progress.csv
make tools-check
```
