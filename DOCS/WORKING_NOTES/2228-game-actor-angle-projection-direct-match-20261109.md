# Game actor angle projection direct match - 2026-11-09

func_1505210C now emits all **85 words / 340 bytes directly from C**, with
the original **0x38-byte frame** and **zero new guards**. The corrected source
fits its original slot and removes the obsolete 356-byte overflow copy. The
guard manifest is byte-identical. No compiler profile or conversion row changes.

Fresh total **4,296 / 5,513 (77.92%)**, Game **3,623 / 4,840 (74.86%)**,
Init 492/492, Debugger 181/181, zero drift and **1,217** different converted
functions. **115** additional accepted matches reach 4,411/5,513 and the active
80% goal. README changes only these aggregate rows.

## Source and lifetime recovery

Owner: conker/src/game_77AD0.c. VA 1505210C..15052260; ROM 7F5BC..7F710.
Preserve the five-argument float-returning interface: actor, X/Z input pair,
secondary output pointer and limit. The actual SDK heading is at actor+0x40.
There is no separate original assembly file for this already-converted routine;
the frozen US ROM slot supplies the reference and derived layout fixture.

The prior ECTS-derived C emitted 89 words. Compute both projected components
before the first func_150484A0 call, retaining original X until the secondary
component is complete. A trial that overwrites X too early also fits 85 words
but is semantically wrong; the overwritten-original-X control catches it.

Reuse the captured scalar parameters for the live result roles. Keep the
second helper result in a separate temporary, copy it to the secondary result,
and test that original temporary for wrapping. This restores all retail words,
saved F20/F22 pairs and exact branch-delay schedule without word normalization.
An otherwise correct source with a single secondary variable fits 85 words but
still has fourteen scheduling/register differences; it is not the chosen form.

Correct the old sine/cosine local names. func_150AD780 adds the verified
0x3FC90FDB quarter-turn constant before falling into the polynomial routine;
func_150AD78C uses the unshifted argument. Preserve both helper bodies and their
call order. Capture heading radians once, negate incoming Z, preserve float32
multiply/add grouping, and submit both projected values with literal 1.0f.

Reload each degree scale after its corresponding angle-helper call. Wrap each
angle by subtracting 360 exactly once when it is at least 180, then apply the
upper and lower clamps in their original order. Negative/zero/NaN limits are
not replaced with a speculative absolute-limit policy. Publish secondary only
after all helpers and return primary in F0. Shared declarations stay fixed.

## Focused qualification and caller limits

Six focused checks pass before and after installation in both tools
environments, using 665 frozen source/header/assembly/tool/build inputs. The
sibling executes the new modules through a read-only overlay; its inherited
dirty state is preserved. Task modules and loaded helpers are fingerprinted.
Routine Claude calls attempted/completed: **0**; local evidence settles it.

- **421 independent guest cases per raw, padded and retail body**, **1,263
  executions**, cover every root instruction, all wraps/clamps, signed zero,
  infinities, NaN classification and ordered comparisons, callback effects,
  fresh scale loads, saved FPR pairs, actor/output aliases and caller-stack
  output. Guest-only incoming-home mutations qualify the emitted ABI.
- **Eight independent symbol/entry/stack rebases**, plus **four actual GNU
  links / eight executions** at low halves 0000/7FFC/8000/FFFC, qualify paired
  high/low carries and float-call bindings independently of the normal link.
- Native32 O0/O2/O3 with trapping UBSan passes **316 cases per profile**, real
  SDK layout, actor canaries, actor/output aliasing and callback scale reloads.
  All **twelve semantic controls** are effective at each profile and also have
  IDO guest witnesses. Compilation/interpreter failures are not witnesses.
- The direct qualifier rejects **85 corrupt words and ten changed bindings**;
  scope checks reject the wrong owner/function. Eight independent whole-image
  corruptions cover target code, the retargeted jump, retained private code,
  symbols, strings, program headers and protected data. No guards are added.

The retail census finds **three JALs**, ROM 78C98 / 7E7B8 / 7F274, with no
aligned entry-pointer literal. Their owners are func_1504B0FC, func_150511E8
and func_15051558. **All three remain pre-existing 12-byte return-zero C
placeholders** in the current project. The linked census contains **zero**
calls to this target and their original call-window ranges remain zero-filled.
They are preserved, not silently restored or credited by this checkpoint.

The three original retail windows nevertheless execute with raw, padded and
retail target code in **939 cases / three bodies**, checking their actual O32
float packets, natural limits 180/50, output/input aliases and primary-result
stores. All **32 static window words** execute across the 9/10/13-word windows,
including two third-caller branch-likely rejections. These are bounded original
window tests, not executions of the current placeholder parents or full callers.

Helper bodies are checked against their retail bytes; their algorithms remain
bounded in semantic tests. NaN payload propagation, FCSR flags, hardware timing
and full gameplay are not claimed. Native aliases use valid SDK float fields
under the existing non-strict-aliasing policy; incoming-home mutations remain
guest-only.

## Complete owner and overflow image closure

All **57 neighboring raw and padded functions** and pools stay unchanged.
The owner has 58 functions and no C diagnostics. The register-usage metadata
changes only its FPR mask from 000FFFFF to 00FFFFFF, exactly the F20..F23 pairs
saved/restored by the recovered target. The other five register-metadata words
remain identical. Ordinary whole-owner and independent complete-target padders
agree; the independent target padder is not described as padding all 58 routines.

The unchanged actual five-command Make recipe reproduces the complete padded
object with ordinary -O2 -g3. The inherited duplicate generated_12D630 Make
recipe warnings remain separate from C diagnostics.

The independent full-ELF predictor accounts for every resulting byte with zero
exclusions. Replace the canonical trampoline with the direct 340-byte body and
remove __retail_overflow_func_1505210C at 15F00000, length 0x164:

| Retained private function | Old address | New address |
| --- | --- | --- |
| func_1506EE60 | 15F00164 | 15F00000 |
| func_150768DC | 15F001B4 | 15F00050 |
| func_150A7B80 | 15F00438 | 15F002D4 |
| func_15125490 | 15F004BC | 15F00358 |

Each retained private body keeps every byte. The sole remaining live canonical
trampoline requiring retargeting is func_150768DC. The loaded-code J/JAL census
and aligned pointer scan prove closure; before/after trampoline windows forward
the complete incoming state unchanged to the derived destinations.

The overflow section shrinks 0x524 -> **0x3C0**. Its program-header sizes shrink
by 356. Aligned __romPos and debugger_overflow_ROM_START move 0x170 bytes,
25AB10 -> **25A9A0**. Remove the obsolete private function and its sole local
game_77AD0.c.o file symbol, compact the shared private/public name suffix and
reinsert the public name at its derived global position. String payload shrinks
33 bytes, local symbol count drops by two, and all symbol references, section
payload/header offsets and ELF header are rebuilt literally. ELF shrinks by
**420 bytes**. No whole metadata section is excluded or copied from the result.

The disassembly inventory falls 6,052 -> **6,051** solely through removal of
the obsolete private function. All **6,047 canonical function addresses** remain
fixed. Only the target and the declared trampoline change canonical bodies.
All **189,088 protected Game-data bytes / 720 owners** remain exact. Whole-image
equality covers Init and Debugger, including their expected ROM-cursor metadata.

Production Make compiles one C owner and matches the predicted object/ELF.
Makefile, conversion CSV and complete guard CSV remain byte-identical. Normal
make all retains the expected unmatched-ROM checksum exit 2. Both shared smoke
checks are fresh; three unchanged shared regression receipts per environment
are reused only after exact helper/test fingerprints, not called fresh tests.

Production fingerprints:

- ELF: `68eda6652d59e449f0980ee0e749a9f1169627d136cd4322616a158938017529`
- Binary: `b284636a34ec83e1100b9218a27059359199b91a9e290693dae63cbcfd98d03c`
- Owner object: `79587358eefc523755fbb4ba0e01a11d67fecf2f1e7f1b22170f3403417fcc60`
- Guards: `32583c070dc35bc872dbf4bccd830a0e404777d38435dba71ac933407196da11`
- Makefile: `8e676e04318f8645e6b277ed60ed9f221d8901a5e6a02efd279d478d46a615f8`

## Continuation

Graphify receives a scoped AST refresh with fail-closed retention of unscanned
nodes. Audit all 54 C function labels and four retained assembly functions;
distinguish the disabled func_1504B0FC draft location from its active placeholder.
The graph's legacy-draft edges are not proof of linked callers. This is not a
full-corpus semantic extraction. Commit tools before the consumer pin.

Next target: **func_1504AF10** in the same owner, an existing semantic 123-word
actor attachment/status updater. Inspect its complete US body, resolver output,
16-bit packed flags, actor/record indexing and caller ABI before fitting. It is
uncredited and needs all normal gates. Empty void routines must be excluded
from the semantic shortlist as well as return-zero placeholders.

The hard func_1510D404 compiler investigation remains private/uncredited. No
sibling tools work, host-port source or frozen Release artifact is changed.
