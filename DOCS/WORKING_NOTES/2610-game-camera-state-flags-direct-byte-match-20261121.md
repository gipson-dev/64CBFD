# Note 2610: Camera state-flags direct byte match

Date: 2026-11-21. Consumer baseline `9b75c49f8a11ffbe225ee9d6075431be2a35dd47`; tools baseline
`f4040a55c5389f3c615c56349c0d5dd6f6d0dc01`. Qualified tools commit: `7a19dc306f9777ac76bde669daf6692dee6a2e0d`.

`func_151236D0` replaces its zero-return placeholder with the complete camera
actor/height flag updater and player transition dispatch. All **153 words /
612 bytes** emit directly from semantic C, including the **24-byte frame**,
RA save at SP+0x14, camera's incoming home at SP+0x18 and **nine R_MIPS_26
relocations**. There are **zero guards, insertions or omissions**. All **44
owner neighbors**, pools and five existing warnings remain unchanged.

Production recount: **4,594 / 5,528 (83.10%)** total, **3,921 / 4,855 (80.76%)**
Game, zero address drift and **934** still different. Init 492/492 and Debugger
181/181 remain exact. **105 more** matches reach 85% at this denominator.
Conversion rows are unchanged; the previous placeholder already counted as C.
The root README receives only its two aggregate matching rows.

## Recovered behavior and interface

Owner `game_14FF90`; VA `0x151236D0..0x15123934`, ROM
`0x150B80..0x150DE4`. The routine snapshots old height flag 1 from +0x5F0.
When secondary actor +0x3D4 exists, it updates flag 0x40 from that actor's
+0x9C/+0x95 and the primary actor's +0x137; clears 0x400 when primary float
+0x28 is zero; sets/clears flag 8 from secondary halfword +8 and byte +0x16;
and sets/clears 0x80 when secondary byte +0x4E equals 2. A null secondary
skips these actor dereferences.

Height flag 1 is set when camera Y +0x2FC is at most float +0x360 and mode
word +0x2C is not exactly 0x100. Equality, signed zero and unordered NaN
comparisons follow retail. Old/new height flags, counter byte +0x23C, flag 4
and mode bit 0x40000 select one of six player-index helper routines. Releasing
through `func_1515BA48` clears float +0x7B0 **after** the call. Another route
calls `func_1515BA54` then the camera reset helper `func_15124B18`.

The recovered interface is `void(struct108 *)`; player byte +0x23D is promoted
into A0 for the index helpers. Four explicit pointer casts in the existing
transition caller preserve its exact compiled body. Local GCC may-alias scalar
types make the float padding fields and secondary halfword accesses explicit
without changing shared SDK headers. Native offset/extent assertions pass.

The first full semantic source already emits all 153 original words. Adding
the scoped scalar alias types and comments preserves the same payload. SHA256:
`bf2a5a3eabbdd4cf272f4c3392809961600823f78aeb50d5e5a9f795011dd62a`.

## Execution and caller qualification

Independent guest checks pass **4,064 cases per stream** for retail, raw and
padded code. Full public RAM, private bytes, preserved ABI state, calls and
ordered accesses agree. Cases cover null secondary/primary-safe paths, all
byte values for the relevant selectors, old/new flag combinations, exact mode
equality, ordered/NaN/infinite height values, typed primary-secondary aliases,
guest-only overlapping storage and incoming camera-home redirects.
The floating model checks ordered comparison results; FCSR exception flags
and hardware behavior are not modeled.

All **147 normal-entry reachable words** are covered. Words 22/45/58/75/89/134
are skipped duplicate instructions, established by decoded control flow;
all 153 emitted words remain literal. **480 access-fault prefixes** agree in
full state, and six instruction controls are effective. The initial controls
revealed missing equal-height and state-2 examples; both are now included.

All six small original/current index wrappers are also connected: **432 cases
per stream**, **52 literal words**, all **50 reachable words** covered, with
two trailing alignment words in the final wrapper. Their downstream providers
remain bounded. A fresh audit confirms that those six wrappers and the
72-word reset helper currently match their original ELF slots. Full reset,
downstream provider and natural gameplay behavior are separate from this gate.

Native SDK32 passes **3,179 cases each at O0/O2/O3**, with strict aliasing,
UBSan and seven effective source controls. Its independent transition table
selects routes from old/new flags. Valid SDK objects and primary==secondary
aliases are covered. Cross-object storage aliases and incoming-home redirects
remain guest-only; native stack layout is not claimed.

The original-ROM census finds **eight direct calls** and no aligned loaded
pointer literals; computed references remain possible. **288 cases per call
window per stream** preserve S0/S1 camera arguments, the unused return within
the selected windows and their delayed argument updates. Four current exact
transition-caller windows also execute the next call; four other two-word
windows are original-ROM evidence from unfinished/nonmatching parents.
Eight lost-delay-argument controls are effective. Whole callers are not claimed.

Six GNU links check retail/raw/padded targets at two code bases. The full
padded owner is anchored at **0x15122AE0**, preserving its internal
`func_15124B18` definition during rebasing. The initially reused arbitrary
owner base was rejected and corrected. The target has **only R_MIPS_26
relocations**; there is no target data relocation or HI16/LO16 carry claim.

## Whole image and adoption

The natural mixed GLOBAL_ASM Make recipe runs five commands under existing
O2/g3. The production build and strict predictor cover **6,051 slots** and
**494 changed bytes**, with **zero exclusions**. The only declared changes
are the target body and symbol extent **12 to 612 bytes**. There is **no
symbol/string reordering**. All other definitions and section geometry remain
unchanged. All **189,088 protected Game-data bytes / 720 owners** remain exact.
ELF SHA256: `303bf3db7be33337032e2cf58927c8ff93c59db1954b872d560380b11a302bf1`.

The existing guard CSV remains byte-for-byte unchanged. Five focused checks
pass in both tools configurations before and after adoption; shared
`make tools-check` passes. Seven tools files are committed first. The private
hybrid has 1197 files, preserving the real dirty sibling HEAD/status
and 352 dependency hashes. Production audits
2341 frozen inputs. Earlier unchanged broad receipts are
reused by fingerprint, not reported as fresh checks.

Scoped Graphify refresh retains prior IDs and qualification metadata when the
native refresh refuses a smaller corpus; it is not a full-corpus extraction.
Available host scene configuration/input is audited read-only, with no direct
C import or runtime parity inferred. No shared-header/profile/Make/guard,
host/Release/ROM/save changes, push or Claude calls. The **85% goal stays active**.
Next candidate: `func_151247C0`, a 189-word/frame-56 camera placeholder,
requiring fresh source, ABI, caller and image qualification.

```sh
python3 -m unittest tools.tests.test_game_camera_state_flags_151236d0_match -v
make -C conker -j4 build/conker.us.elf progress.csv
make tools-check
```
