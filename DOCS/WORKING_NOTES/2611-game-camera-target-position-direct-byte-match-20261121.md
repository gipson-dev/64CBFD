# Note 2611: Camera target-position direct byte match

Date: 2026-11-21. Consumer baseline `5805d036399704a2eb84d0aac5077e8a1066ccb4`; tools baseline
`7a19dc306f9777ac76bde669daf6692dee6a2e0d`. Qualified tools commit: `acc3dda6113738eaf82dccb3fb552e456188f477`.

`func_151247C0` replaces its zero-return placeholder with the complete actor
target-position update, scalar springs and heading offset. All **189 words /
756 bytes** emit directly from semantic C, including the **56-byte frame**,
S0/RA saves and nine relocation sites. There are **zero guards, insertions
or omissions**. All **44 owner neighbors** and pools remain unchanged.

Production recount: **4,595 / 5,528 (83.12%)** total, **3,922 / 4,855 (80.78%)**
Game, zero address drift and **933** still different. Init 492/492 and Debugger
181/181 remain exact. **104 more** matches reach 85% at this denominator.
Conversion rows are unchanged; the old placeholder was already counted as C.
The root README receives only its two aggregate matching rows.

## Recovered behavior and compiler shape

Owner `game_14FF90`; VA `0x151247C0..0x15124AB4`, ROM
`0x151C70..0x151F64`. A nonzero unsigned halfword +0x7F4 returns immediately.
Otherwise the low byte of secondary actor word +0x9C OR byte +0x95 selects
target factor 0.25 or 1.0. This is an explicit byte truncation, not a Boolean
test of the whole word. Counter +0x23C forces the factor and clears velocity;
otherwise `func_150495B0` smooths factor/velocity with six typed arguments.

The routine selects the primary actor or the midpoint with its partner at
+0x248. Counter mode copies X/Z directly; normal mode interpolates X/Z using
the current factor. Y follows the selected target without that interpolation.
A second scalar spring controls the heading offset. Sine/cosine use the two
distinct constants `D_800A34FC` and `D_800A3500`, both original bits 0x3FC90FDB.
The resulting X/Z are copied to +0x2BC/+0x2C4 before `func_15125594` runs.

`CameraPosition14FF90` recovers the exact 0x9A0 camera view, its partner
pointer, float padding fields and spring records. The activity view places
its byte and word at +0x95/+0x9C. GCC may-alias annotations support the local
view; shared SDK headers remain unchanged. Native SDK32 offset, extent and
scalar assertions pass. The existing caller receives an explicit pointer cast.
The corrected void/pointer interface removes exactly its prior warning 712;
diagnostics move from five to four with no new warnings. A prior comment is
clarified to name `func_1515BA48`; its emitted instructions remain unchanged.

The initial SDK-cast source had 188 words/frame 56. A conditional activity
expression restored 189 words. Typed fields, inline interpolation reads and
integer-zero late comparisons recover the float allocation; flags-first OR
recovers the final opening read order. No scheduling normalization is needed.
Raw payload SHA256:
`7526b9483c51e326a2e0902c4e697e9ff6d2846bb6999d48d386625ca957ca2c`.

## Execution, caller and relocation gates

Independent guest checks pass **2,870 cases per stream** for retail/raw/padded
code, comparing public RAM, private bytes, preserved ABI state, calls and
ordered accesses. They cover forced/normal modes, both actor selections,
low-byte truncation, signed zero, finite interpolation and spring boundaries,
legal and guest-only overlap aliases, provider mutations and disabled paths
with absent actor pointers. All **184 normal-entry reachable words** are
covered. Words 24/36/74/103/112 are statically skipped duplicate instructions;
all 189 emitted words remain literal. **131 access-fault prefixes** agree in
full modeled state. FCSR exception flags and hardware behavior are not modeled.

Connecting the actual original/current scalar spring passes **864 cases per
stream**, covering all **52 reachable words** of its 54-word slot. Words 15/49
are skipped copies. Both overshoot directions are included after the first
connected corpus exposed missing coverage. Pure finite deterministic trig
and an explicit finalization contract bound the remaining providers. The
54-word spring and 29-word final helper are literal in the sealed ELF; full
finalization and natural gameplay acceptance remain separate.

Native SDK32 passes **2,833 cases each at O0/O2/O3**, with strict aliasing,
UBSan, the recovered spring C and eight effective source controls. Valid
primary==partner aliases are included. Camera/actor storage overlaps remain
guest-only; native private-frame layout is not claimed.

A fresh census finds **one direct call** and no aligned loaded pointer literals;
computed references remain possible. The original/current **six-word caller
window at 0x15126138** passes **128 cases per stream**. It covers the caller's
24-byte frame, delayed camera save to its incoming home, post-call camera
reload and primary pointer load. Two effective controls use a valid alternate
pointer so rejection does not depend on an oracle error. Whole-caller
acceptance is outside this window's scope; its complete body is separately
preserved among the 44 neighbors.

Six GNU links cover retail/raw/padded targets at two code/data bases, with
HI16/LO16 carry. The padded owner retains base 0x15122AE0 and its internal
final helper definition. The target has five R_MIPS_26 and two HI16/LO16 pairs.

## Whole image and adoption

The natural mixed GLOBAL_ASM recipe runs five commands under existing O2/g3.
Production and the independent predictor cover **6,051 slots** and **683
changed bytes**, with **zero exclusions**. Declared changes are the target,
symbol size **16 to 756 bytes**, and one closed symbol/name swap involving
`D_800A34FC`/`func_1504095C` (**two records / 25 string bytes**). All other
definitions and section geometry remain unchanged. All **189,088 protected
Game-data bytes / 720 owners** remain exact. ELF SHA256:
`3199afbb21ea723e99999885a6be2207ecee1e121cfee8b70b97e780afd90623`.

The complete existing guard CSV remains byte-for-byte unchanged. Five focused
checks pass in both tools configurations before and after adoption; shared
`make tools-check` passes. Seven tools files are committed first. The private
hybrid has 1204 files, preserving the real dirty sibling HEAD/status
and 352 dependency hashes. Production audits
2352 frozen inputs. Earlier unchanged broad receipts are
reused by fingerprint and are not called fresh tests.

Scoped Graphify refresh retains prior IDs and qualification metadata after
the native smaller-corpus refusal; it is not a full-corpus extraction.
Available host scene configuration/input is inspected read-only without a C
import or runtime-parity inference. No shared-header/profile/Make/guard,
host/Release/ROM/save changes, push or Claude calls. The **85% goal stays active**.

```sh
python3 -m unittest tools.tests.test_game_camera_position_151247c0_match -v
make -C conker -j4 build/conker.us.elf progress.csv
make tools-check
```
