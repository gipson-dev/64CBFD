# Linked Shape-Measure Node Direct C Match

Date: 2026-10-22

## Result

Recover `func_1515F1B0` in `conker/src/game/generated_18A8F0.c` from its
twelve-byte zero-return placeholder. Complete semantic C emits all
**43 words / 172 bytes, frame 48 and three call bindings** directly under
normal O2/g3. No guards, inserted words or compiler-profile changes.

VA 1515F1B0..1515F25C / ROM 18C660..18C70C, ends exclusive.
Keep the address-based function name, add a purpose comment and define a
private `ShapeMeasureNode`: descriptor pointer, volume float, area float and
next pointer at offsets 0/4/8/C, total sixteen bytes in the guest ABI.
Retain the original `conker/asm/18A8F0.s` and all 34 owner neighbors.

## Recovered Contract

1. Call func_10003C6C with the exact five-word packet `(0x10, 1, 2, 0, 1)`.
2. On allocation failure return NULL without calling either measurement
   helper or writing a record. Allocator-side effects still occur.
3. Store the captured incoming descriptor in the allocated record.
4. With a nonnull descriptor, call func_1514462C and store its returned
   float at +4. Otherwise store positive float zero at +4.
5. Independently test the captured descriptor again, call func_15144598 and
   store its float at +8, or store positive zero for a null descriptor.
6. Clear the next pointer at +C only after both measurement stages and
   return the captured allocation, not a possibly mutated record field.

The existing helpers compute descriptor volume and area measures. Preserve
their order, side effects and the captured descriptor even if the first
helper rewrites the record's descriptor field. Do not cache helper results,
clear the link early, combine the two calls into an unspecified operand
order, reread the descriptor from the result, or discard a successful result.

## Caller Interface

The sole direct caller, func_150150A4 in `conker/src/game_40490.c`, declared
the result as struct17, a twelve-byte three-float vertex type. That is not
the sixteen-byte linked record constructed here.

Use an opaque byte-pointer return in both translation units. Correct the
caller's local prototype and result variable, and express its existing
area access as a float load from +8. Keep shared struct17 and unrelated
global/header types untouched. No broad vertex or linked-list refactor.

All 32 raw caller functions, pools and relocations remain identical. Its
entire ordinary-Make padded object is also byte-identical:
`f7791694bf224220587ba1c26dbfb1ccf76ea4c14b69726c1fc74cadf543b626`.

## Exact Emission

Raw unlinked SHA-256:
`0e0495852884c13d95f48c200720c2c554cb0b773ca63335bae93b4ed9de00d7`.
Independent original GNU assembly, isolated C and complete raw owner agree
on all words and the three R_MIPS_26 bindings: func_10003C6C at +0x24,
func_1514462C at +0x48 and func_15144598 at +0x70.

Both owners retain assembly-backed neighbors. Their actual Make recipes
each contain five productive commands: asm preprocessing, IDO compilation,
asm postprocessing, padding and GNU assembly. Execute all ten commands,
preserving normal O2/g3 and the unchanged retained assembly bodies.

The strict independent complete-ELF prediction permits exactly
**116 changed bytes = 115 code bytes + one target-size metadata byte**.
Zero exclusions or symbol/string-order allowances. ELF SHA-256:
`daabcd1260cc66c048f76a5c8e57128602a21199c144be7a129e9b57ea0d6291`.
Padded owner SHA-256:
`c4495b20af10b6149b7b794b84b8e215785d31a46ac1a36106aa262e4dcf4cf7`.

## Qualification

Identical task tools in both local copies:
`experiments/game_shape_measure_node.py` and
`tests/test_game_shape_measure_node.py`.
Reuse existing dual-owner, asm-processor/padder, native32, float32, MIPS
access-prefix and independent GNU relocation helpers. Zero Claude calls.

- 5,136 guest phases cover successful/failed allocation, null/non-null
  descriptors, all modeled effect combinations, saved pointer lifetime,
  descriptor/record overlap, high-bit pointers, raw helper float words and
  both stack phases. Every one of the 43 constructor words executes.
- Native32 O0/O2/O3 each exercise 16,384 selected-body cases with trap
  UBSan, sixteen-byte node/field assertions, typed descriptors and fences.
  Twelve defined wrong-C controls detect incorrect size/pool, descriptor,
  helper selection/omission, link, return, late pointer recapture, early
  clear and suppressed descriptor handling. Native tests omit signaling
  NaNs and descriptor/node overlap; do not infer portable native alias or
  signaling-NaN behavior from guest byte/float-word agreement.
- Nine independent GNU links cover 24 rebase phases. Compare 80 fired
  root-access fault prefixes and seven strict-image corruptions. Guest
  instruction fault-prefix agreement is not portable C/MMU fault semantics.
- An aligned retail scan finds one direct JAL at ROM 4255C and no literal
  target pointers. Original/current func_150150A4 agree on all 24 words.
  Execute that complete caller, the new constructor and the actual five-word
  func_1515F25C list insertion across 32 phases. Verify failure returns one
  without insertion; success links the record and adds its +8 area to the
  accumulator. Legacy global declarations are unchanged; this is not a
  native-C qualification of every caller/global type.
- Original/current measurement helpers agree on all 93 words, 56 volume
  plus 37 area. Connect them across 384 signed-dimension, flag, overlap and
  stack phases. Execute 92 words; preserve the original unreachable volume
  load at 1514468C. Read all three coefficient words from the retail data.
  Apply explicit float32 rounding before the area's coefficient multiply.
- Four additional guest phases mutate the incoming argument home while
  allocation runs. The emitted saved input survives; portable access to
  another C function's private argument home is not claimed.

The allocator is a bounded provider with a checked packet, return, mutations
and ABI clobbers. These tests do not execute or re-qualify the complete heap
implementation. No hardware/FCSR, emulator, host-port or gameplay claim.

Initial fixture runs rejected the old three-command Make assumption, then
the same assumption in the caller's assembly-backed recipe. Add strict
shadow-contained preprocessing redirects and require five commands per
owner. A guest fixture field also collided with the base oracle's internal
symbol map; use a dedicated node_symbols field. Failed runs are retained
privately and do not count as passing evidence.

After the first passing pair, make the independent area reference's
float32 conversion explicit and rerun both complete suites. Keep the prior
implicit-rounding receipts separately; the table below reports the final
test-file revision.

| Actual Run | Active Tools | Older Mirror | Errors / Failures / Skips |
| --- | --- | --- | --- |
| Full pre-install suite | 8 tests, 42.718s | 8 tests, 41.348s | 0 / 0 / 0 |
| Fresh installed checks | 2 tests, 13.204s | 2 tests, 10.686s | 0 / 0 / 0 |

Shared project-tool checks pass in 0.259s / 0.304s. Explicitly reuse six
unchanged pre-install behavioral checks per copy under strict source,
raw/padded owner, complete caller object, helpers/inputs, guards and whole
ELF identity. Do not call those six fresh installed runs.

## Production

Commit tools first: `a83687eac3d2616ec4bdbb6c7f3bf5e0334e95d3`. No push.
Preserve all 1,564 prior older-mirror dirty paths, statuses, hashes and HEAD;
add only the two task files, leaving 1,566 dirty paths. Do not reset or
commit that independently dirty mirror.

Seal 15,874 files and all 1,454 linker objects, advancing only the
predecessor's already-committed source, owner object and ELF fingerprints
before adding the four new task-copy rows. Verify all current bytes.

Normal Make completes in 5.039s in the verified Linux copy. Mark only the
verified unchanged guard manifest old to avoid unrelated historical-object
rebuilds. Preserve inherited generated_12D630 duplicate-recipe warnings;
owner/caller diagnostics remain unchanged and isolated diagnostics are empty.

Preserve all other 6,054 linked bodies, all 6,055 addresses and all 720
protected Game-data owners / 189,088 bytes. Protected-data SHA-256:
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

Live adoption audit passes in 35.266s. Verify every static input and
non-target object before and after promoting only the target owner object,
ELF, linker script and progress CSV. Both edited C files already equal
their qualified proposals. The complete caller object needs no promotion;
linker-script and conversion-CSV bytes remain identical. Reproduce the
complete independent 116-byte prediction with zero exclusions.

## Handoff

The standard matcher against the actual live ELF completes in 7.904s:
total **3,745/5,505 (68.03%)**, Game **3,072/4,832 (63.58%)**,
Init 492/492 and Debugger 181/181 exact. Zero address drift; 1,760 different.
The 75% threshold remains 4,129 exact, requiring **384 more matches**.
Queue shapes: 1,629 placeholders, 122 semantic/other and nine unlocated.
Next func_150A3398 is screened only, unmodified and uncredited.
Keep func_1508CAD8's 862-word stub queued.

Root README changes only its two aggregate rows. Detailed updates belong here
and in concise indexes. Post-commit graph-worker and every-old-node audits
remain private receipts. Keep excluded-corpus/large-HTML caveats explicit;
do not claim a full re-extraction or fresh corpus-membership recount.
Host Release, saves and configuration remain untouched.
