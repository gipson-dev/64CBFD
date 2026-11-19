# Note 2570: Tank camera callback direct byte match

Date: 2026-11-19. Consumer baseline `4c6f84ec96d8247c29605cdc9092ee52d5cf0354`;
tools baseline `fde315b984e538d2cceb8f9a8b051c7b9b6deda5`.

`func_15104520` replaces GLOBAL_ASM with complete semantic C and emits
**all 45 body words directly**, using the original **24-byte frame**.
Three retail alignment NOPs complete its **48-word slot**. Zero guards,
insertions, omissions, profile changes or shared-header changes.

Fresh production recount: **4,564 / 5,516 (82.74%)** total and
**3,891 / 4,843 (80.34%)** Game, zero address drift, 952 different functions.
Init 492/492 and Debugger 181/181 remain complete. **125 further matches**
are needed for 85% at this new denominator. Converted totals are
5,516/6,048 (91.20%), 86.24% of bytes;
Game 4,843/5,327 (90.91%), 85.62% of bytes.
Exactly one ASM-to-C conversion row changes. The rounded matching percentages
stay the same while both the exact count and conversion denominator increase.

## Recovered source and interface

Owner `conker/src/game/generated_1319D0.c`, body VA
`0x15104520..0x151045D4`, slot through `0x151045E0`; ROM
`0x1319D0..0x131A90`. Original assembly is retained in the full
`conker/asm/1319D0.s` slice and its nonmatching function file.

The callback takes one camera pointer and returns void. A local typed camera
view names the fields used here without changing the shared structure, whose
offset 0x370 remains opaque. Its size is 0x700; field offsets are independently
asserted by native SDK32 compilation. The canonical `struct127` supplies the
subject actor: offset 0x3C is **horizontal speed**, not height or vertical speed.
Names describe observed use, not recovered original debug identifiers.

An override at camera+0x6FC, or zero mode at +0x6C8, sets distance fields
+0x348/+0x34C to 117, desired distance +0x374 to 370 and vertical offset
+0x190 to 77. After those writes the subject at +0x3D0 is loaded. If its
horizontal speed is strictly below 50 and camera transition byte +0x3E8 is
zero, the callback compares half the desired distance with current-minus-desired
distance. A strictly larger gap submits the camera and cached subject to
`func_15128774`, which refreshes its follow origin. NaNs make the ordered tests
false. The helper is called only after all default stores.

The first source already had 45 words/frame24, but its multiply swapped the
F0/F16 input fields. Reversing expression text, a named half alone and a register
hint did not fix it. Naming both `half` and `desired` locally emits the literal
retail MUL.S, preserving all other words and the helper relocation. No guard or
compiler trace is needed for this complete direct match. The source contains
no artificial frame padding or volatility.

## Original indirect dispatch and child

Whole-ROM census finds no direct JALs and exactly one literal function pointer:
ROM `0x22E15C`, table `D_80089670` address `0x80089670`, index **11**.
The original 17-word `func_15130230` loads a byte at selected state+0xF,
skips index zero and calls that table entry with the original camera in A0.
It preserves its unused second argument home and ignores callback results.
The index-11 target and zero gate are exercised through the actual instructions
and original table bytes. Other callback indices and arbitrary computed calls
are not excluded or claimed qualified by this target suite.

The original 27-word `func_15128774` slot is also connected. The independent
reference checks its real ordered reads/stores: actor origin and orientation,
camera position pairs, subject-field+0x40 subtraction, secondary actor value and
camera state byte. Both this actual child mode and an opaque provider with
controlled mutations run through the original dispatcher. Caller assembly,
source, rodata table and child owner are hash-pinned. The callback/table data
stay unchanged in production.

## Qualification

Primary tools and isolated sibling overlay each pass the same five-test suite
before and after installation:

- 588 independent cases per original/raw-C stream, including both default gates,
  exact speed/gap thresholds, signed zero, subnormals, large values, infinities,
  quiet NaNs, transitions and helper effects. All 45 body words are visited.
  Guest-only camera/subject aliases check that defaults precede speed reads;
  these cross-type overlaps are excluded from portable native C fixtures.
- 66 access-fault prefix pairs, six effective instruction negatives and exact
  alignment checking. Predicate inversions are used for branch negatives;
  merely redirecting to a duplicate restore or MTC1 was correctly rejected as
  an ineffective control. Fault prefixes describe guest access order, not
  portable C faults. The numerical model covers IEEE-single values and ordered
  comparisons without FCSR, interrupt or hardware emulation.
- 524 actual SDK32 cases each at O0/O2/O3 with strict aliasing, UBSan and
  float-cast-overflow checks, plus eight executed source negatives per profile.
  Independent Python snapshots serialize initial/final fields, provider
  arguments and state before the call. Native objects use the actual local
  camera type and SDK actor type; byte accessors avoid float/integer aliasing.
  The freestanding Linux entrypoint explicitly aligns its stack.
- Six independent GNU relocation rebases /12 links compare all 180 body bytes.
  Every raw byte and the call binding has an effective corruption check.
  Strict-image negatives include a NOP outside the C symbol body.
- 124 scenarios per stream through the complete original dispatcher, using
  both the real original child and an opaque provider. Original callback entry,
  camera/subject arguments, defaults, helper effects, saved registers and return
  stack are checked. This is bounded connection evidence, not gameplay acceptance.

Both independent padders preserve the full 192-byte slot. The actual pure-C
three-command Make recipe equals the independently padded object. Production
Make finishes in 20.749 seconds. All 6,051 instruction vectors
and addresses remain unchanged; all 189,088 protected bytes in 720 owners stay
exact. The old assembly symbol included its alignment and had size192, while
the C symbol has body size180. The strict complete-image prediction permits
only that size-field change: **one byte**, no exclusions or symbol permutations.
Guard CSV, Makefile and every other frozen input remain unchanged.
`make tools-check` passes.

Production ELF SHA256:
`ea46d16aedc5ea821dac701baf175d0a376a44f97e49196a40ad109e5f8be8d1`.

The real dirty `64CBFD Tools` sibling retains its HEAD, raw status and all343
dependency hashes. The 925-file overlay uses 339 matching sibling files,
580 primary fallbacks, five task files and one empty bootstrap. Installed
imports agree byte-for-byte apart from that bootstrap. The checked sibling
`64CBFDOGL/recomp_scene/out_af4/func_15104520.c` reference is an empty generated
stub; it is not used as a donor. No host files or frozen Release artifacts are
changed or built. This decomp conversion does not establish host-port parity.

Root README receives only four aggregate rows. Five concise indexes link here.
Graphify's native update refuses shrink; scoped five-file AST refresh retains
all existing IDs. Historical aliases and the literal manifest edge are sealed
after the observed commit-hook producers exit. This is not full-corpus extraction.
Ignored evidence and handoff: `conker/build/game-tank-camera-15104520-private/`.
Routine work used zero Claude calls.

## Next

Inspect the converted but unmatched **275-word `func_15104634`** in
`conker/src/game/generated_131A90.c`, VA `0x15104634..0x15104A80`.
Its four small converted neighbors already match; preserve them. Independently
inspect graph, complete original body, callers and profile before editing.
The older private 591-word `func_150BBB5C` candidate remains uncredited and
untouched. The complete 85% matching goal remains active.
