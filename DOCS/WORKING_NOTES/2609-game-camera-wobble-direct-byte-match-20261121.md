# Note 2609: Camera wobble direct byte match

Date: 2026-11-21. Consumer baseline `0e32bcce7db4c876186a06859832498744688f00`; tools baseline
`7708beb847e33d9461a8786ae1dad95eb2ef8996`. Qualified tools commit: `f4040a55c5389f3c615c56349c0d5dd6f6d0dc01`.

`func_151256BC` replaces its zero-return placeholder with the complete camera
wobble update. All **154 words / 616 bytes** emit directly from semantic C,
including the **56-byte frame**, saved S0/S1/S2/RA, original float spill homes
and **23 relocation sites**. There are **zero guards, insertions or omissions**.
All **44 owner neighbors**, pools and five existing warnings remain unchanged.

Production recount: **4,593 / 5,528 (83.09%)** total, **3,920 / 4,855 (80.74%)**
Game, zero address drift and **935** still different. Init 492/492 and Debugger
181/181 remain exact. **106 more** matches reach 85% at this denominator.
Conversion rows remain unchanged; the old placeholder was already counted as C.
The root README receives only its two aggregate matching rows.

## Recovered behavior and layout

Owner `game_14FF90`; VA `0x151256BC..0x15125924`, ROM
`0x152B6C..0x152DD4`. The active gate is flag 0x80000, or secondary flag 8
without primary flag 0x40000. An unsigned PRNG result modulo 3 advances the
phase at +0x29C by twice that remainder, the degree-to-radian factor and
`D_800BE9A4`. A strict greater-than loop wraps by the full-turn constant.
The sine value times four is smoothed into amplitude +0x5EC. Rotations use
amplitude times 0.05; flag 0x80000 selects scale pair 4/4, otherwise 1/20.
The +0x2F8 position rotates about +0x2BC first; the second rotation uses the
updated position as its pivot. Both preserve Y through the actual helper.

Inactive zero phase returns without provider calls. Other phases subtract
8 percent of their value, update the same smoothed amplitude and rotate with
scale pair 1/20. There is no additional epsilon threshold in the retail body.

The local `CameraWobble14FF90` view gives meaningful float fields to shared
SDK padding and declares both real vectors as three-element arrays. SDK32
offset/extent assertions verify +0x2C/+0x29C/+0x2BC/+0x2F8/+0x5EC/+0x5F0.
The GCC may-alias annotation supports the local padding view; IDO receives
the same layout. Shared headers and compiler profiles remain unchanged.
The local caller declaration is `void(CameraWobble14FF90 *)`; its explicit
cast preserves the byte-exact transition caller among the 44 neighbors.

The initial source had 156 words/frame 56 and 124 positional differences.
Caching the phase limit recovered 154 words but frame 64. The selected form
casts the unsigned remainder directly and reuses the phase-limit local for
the first rotation scale. This recovers the natural 56-byte frame and all
154 words without adjustment. Raw payload SHA256:
`4d90dceaf9168d6e4b83d05d075265dca119604fe595ab397d74b9e5378a1bd6`.

## Execution, caller and relocation checks

Independent ordered binary32 equations pass **1,952 cases per stream** for
retail, raw and padded code. Full public RAM, private bytes, preserved ABI
state, calls and ordered accesses agree. Cases cover both gates, signed/high
PRNG bit patterns, modulo values, exact wrap boundaries, repeated wraps,
negative phase, signed zero, both scale pairs and modeled provider mutations.
All **149 normal-entry reachable words** are covered. Words 29/30/31 form
the unsigned-conversion correction path made impossible by remainder 0..2;
words 78/103 are skipped duplicate loads. Every emitted word remains literal.
**78 access-fault prefixes** agree in full state, and five instruction controls
are effective. The initially ineffective wrap control required an exact-limit
case; that case now distinguishes `>` from `>=`.

Connecting the original/current **55-word X/Z rotation helper** passes
**96 cases per stream** and covers all 55 helper words. The test oracle gained
the missing bitwise `neg.s` model for this connection. Trig uses pure finite
deterministic float providers; polynomial accuracy, FCSR exception flags and
hardware acceptance are outside this gate. The PRNG uses an explicit bounded
full-width return/side-effect contract, not execution of its handwritten body.

Native SDK32 passes **992 cases each at O0/O2/O3**, with strict aliasing,
UBSan, the recovered rotation C body and seven effective source controls.
The typed camera view/SDK union and complete storage comparison preserve
neighbor bytes. Native private stack layout is not claimed.

A fresh original-ROM census finds two direct calls and no aligned loaded
pointer literals; computed references remain possible. Original caller windows
at **0x15122FC4 (4 words)** and **0x15128598 (10 words)** pass **96 cases each
per stream**. They preserve the camera argument, unused return, next call and
the transition caller's delayed third raw-coordinate copy. Three caller
controls fail. `func_15122C5C` remains a placeholder; its original window is
ROM/ASM evidence, not a current gameplay claim. The restored transition caller
is independently preserved by the owner/image gates.

**Six GNU links** cover retail/raw/padded payloads at original and independently
shifted code/data bases, including HI16/LO16 carry. The isolated raw target
retains its exact payload and relocation bindings. Constant bits are checked
against the sealed ELF, including the distinct equal-valued smoothing and
rotation factors.

## Whole image and adoption

The natural mixed GLOBAL_ASM recipe runs five commands under existing O2/g3.
The production build and independent predictor cover **6,051 slots** and
**572 changed bytes**, with **zero exclusions**. Declared changes are the
target body, symbol extent **16 to 616 bytes**, and three closed symbol/name
swaps involving **six records / 69 string bytes**. All other definitions and
section geometry remain unchanged. All **189,088 protected Game-data bytes /
720 owners** remain exact. ELF SHA256: `7db6dfbd90abbf36e79d0432283b4ad31cee22c4488dd1d44a5f21bf2770b348`.

The complete existing guard CSV remains byte-for-byte unchanged. Five focused
checks pass in both configurations before and after adoption; shared
`make tools-check` passes. Seven tools files are committed first. The private
hybrid has 1190 files, preserving the real dirty sibling HEAD/status
and 352 dependency hashes. Production audits
2330 frozen inputs plus the additional snapshots. Earlier
unchanged broad receipts are reused by fingerprint, not called fresh tests.

Graph refresh retains old IDs and qualification metadata, using scoped serial
extraction when the native refresh refuses a smaller corpus. This is not a
full-corpus extraction. Available host scene configuration/input is audited
read-only; this decomp C restoration supplies no direct import to its binary
input contract. No host/Release/ROM/save changes, push or Claude calls.
The wider **85% goal remains active**.

```sh
python3 -m unittest tools.tests.test_game_camera_wobble_151256bc_match -v
make -C conker -j4 build/conker.us.elf progress.csv
make tools-check
```
