# Game Actor Classifier Match

Date: 2026-10-06
Baseline: `0720ffb3` ([Note 1061](1061-game-effect-dispatch-match-20261006.md)).
Continue the full Game matching goal with the actor classifier called by the
banked live effect dispatcher. This is original N64 C recovery, not host-port
source adoption or complete gameplay acceptance.

## Retail Contract

`func_15141C0C`: **45 words /180 bytes**, no frame, VA
**0x15141C0C..0x15141CC0**, ROM **0x16F0BC..0x16F170**, owner
[`game_16EE20.c`](../../conker/src/game_16EE20.c). Load only unsigned actor
byte+4; return a category, with no calls or writes. Typed ABI:
`s32 func_15141C0C(u8 *actor)`.

| Category | Actor IDs |
| --- | --- |
| 10 | 0x79 |
| 9 | 0x21 |
| 8 | 0x7B |
| 0 | 0x00..0x04, 0x96 |
| 1 | 0x10, 0x91 |
| 2 | 0x2B |
| 5 | 0x54 |
| 6 | 0x36, 0x53, 0xA5 |
| 7 | 0x58 |
| 3 | 0x45 |
| 4 | 0x4B |
| 11 | All other unsigned byte values |

Retail branches through a45-entry table for IDs121..165 at800A5218 and an
89-entry table for IDs0..88 at800A52CC. IDs89..120 and166..255 return11
without a table access. All134 targets are original function-interior addresses,
not category integers. Both pools belong to the existing
`build/assets/249CC0.bin.o(.data)` owner; their concatenated span is536 bytes.
The separate context-classifier table starts immediately afterward at800A5430.

## Direct Source And Table Ownership

[Compiler driver](https://github.com/gipson-dev/64CBFD-Tools/blob/master/experiments/game_actor_classifier_candidates.py)
screens inline/s32/u32/u8 identity expressions, inside/outside defaults and
four actual-SDK profiles: **32 controls**, empty standalone diagnostics.
Inline and s32 forms with either default placement are direct under O2/g3
and O2: eight exact controls. u32 emits45 words with one signed/unsigned range
test difference; it is not a semantic failure for unsigned byte input. u8
emits46 words/43 differences; O1 variants emit49 or51 words. Select the
signed32-bit local and outside return11, under the owner's existing O2/g3.

The complete **45 words emit directly from C**, with **no instruction guards,
insertions or omissions**. Preserve the retail return-block order10/9/8/0/1/
2/5/6/7/3/4/11. The compiler emits the same134 table targets followed by eight
bytes of section padding,544 bytes total. Those padding bytes must not replace
the following context table or add a new Game-data owner.

The existing padder's owner-specific `RETAIL_RODATA_SYMBOL` mechanism maps
four code relocations to `jtbl_800A5218_game`. First-table addend0 and
second-table addend180 retain the two original addresses. The compiler's
private `.rodata` contents are discarded; original Game data remains authoritative.
No shared padding-tool changes or replacement table source/data are needed.
Make the owner object depend on Makefile so anchor edits cause a rebuild.

The full-owner screen proves no preexisting `.rodata` section and exactly
four new `.rodata` references, all inside this function. Its unlinked words
and relocation addends match the standalone object. Existing warnings remain
3->3. Recover both local prototypes and update the dispatcher experiment's
actor-classifier prototype; its pending context-classifier declaration and
shared headers remain untouched.

## Bounded Qualification

[Eight maintained tests](https://github.com/gipson-dev/64CBFD-Tools/blob/master/tests/test_game_actor_classifier_match.py):

- All45 compiled words and all134 compiler table targets equal their pristine
  references; the two original table spans are also compared against pristine
  ROM bytes using the structured Game-data owner layout.
- Actual padding emits exactly180 code bytes with the four mapped HI16/LO16
  relocations, no `.rodata` pool. Alternate anchor90007FFC exercises the signed
  low-half carry difference between first and second tables; both addends remain.
- **8192 two-body guest cases** cover every byte, four actor alignments, four
  surrounding poison values and two SP phases. All45 words reached on each
  body; return categories, full storage, saved registers and ordered reads
  agree. The first read is exactly one byte at actor+4; no calls or writes.
- **16384 actual32-bit native cases** use every identity,16 record alignments
  and four poison values, comparing all48 fixture bytes before and after. The
  expected categories derive independently from the original table targets.
- Minimal mapped actor storage contains only its identity byte; every byte
  still classifies. Missing identity and corrupted guest table target fail
  strict mapped-read/owned-jump gates. No invalid native pointer calls or
  hardware-exception claims.
- Six compiled negatives: zero placeholder, signed-byte read, wrong field,
  missing high-range category0 ID, wrong default and wrong category6. Each
  checks all256 inputs and must differ in return or exact read contract;
  unsupported ISA/faults do not count as negative acceptance.
- **4608 connected dispatcher cases** execute the compiled classifier with
  the original100-word dispatcher, mask/context/search instructions, all256
  identities, selections -1/0/20, two lists and three mutation modes. Calls
  and complete external storage match the independent effect reference.

The first ignored table decoder mistakenly interpreted the zero-return OR
instruction as an immediate and failed with KeyError4133. It now decodes that
instruction as category0 and separately asserts each return shape. The first
native fixture failed `-Werror=misleading-indentation`; split the fixture's
poison loop from its identity assignment, without changing recovered source.
The corrected native and compiled-negative rerun passes both tests in5.139
seconds. Positive test cases still require exact returns, reads and full storage.

## Production Verification

Explicit ELF rebuild passes. Relative to `0720ffb3`, all6059 slot addresses/
extents remain fixed, and **only func_15141C0C changes**. All45 linked words
equal retail; the banked100-word dispatcher is unchanged. Target SHA-256:
`94e412a0d3fc5d286a38dfc6d4cab08ce7bfa4dd0c1a82fa8d912dab0c0c0c8d`.
All10785 guard rows are unchanged, with no row for this function. Protected
`.init`, `.init_data`, `.debugger` and `.game_data` addresses/hashes remain
unchanged. All720 Game-data owners /189088 bytes are exact, zero differing
owners/bytes. Owner warnings remain the same3->3, zero new warnings.

Refreshed converted counts and byte coverage are unchanged:5464/6042 total,
4791/5321 Game;85.57% total bytes /84.89% Game bytes. Exact total is
**3337/5464 (61.07%)**, Game **2664/4791 (55.60%)**, **2127 different**,
zero drift. Init492/492 and Debugger181/181 remain exact. This is linked-function
qualification, not an overall retail-ROM checksum claim.

All **24 focused post-link tests pass in257.759 seconds**, no skips/errors/
failures: eight classifier tests,11 retained dispatcher tests and five actual
padding-tool tests. After adding the explicit original640-byte owner assertion
and measuring compiler frames from actual opcodes, the final eight classifier
tests separately pass in **36.264 seconds**. All134 table targets and the
original owner span800A5200..800A5480 remain strict gates.

**44 documents /3485 relative links /zero broken**; `make tools-check`, syntax
and diff checks pass. Required build/audit/regression/context-screen/document
sessions are terminal before checkpointing. Ignored full audit, compiler,
native/guest and test receipts remain under `conker/build/game-actor-classifier-test/`.

## Next Function

Continue **`func_15141CC0`**,57 words /228 bytes, no frame, VA15141CC0,
ROM16F170. Load the live world word once. Worlds47/66/39/25 override to
6/7/8/5; otherwise classify the masked context through the original16-entry
table at800A5430. Two categories also distinguish world2 and world20; default9.
Recover its source/case layout and preserve the already anchored classifier
pool and the next table's offset. Existing connected retail proof does not
restore the context helper's placeholder C. No broad batch before qualification.

Ignored `next-context.py` and `next-context/measurements.json` screen16 actual
SDK controls: global/local world reads, inside/outside defaults and four
profiles. All eight O2/g3 and O2 controls emit57 direct words, no frame; O1
global variants emit68/59 differences, local variants64/64. Select the explicit
s32 world local and outside default for the next qualification. The source
recovers context10->0,7->2,11->1,15->3,2/8/12->world2?7:4,5->world20?5:9,
0->9 and other contexts->9, after the four world overrides. This is not
maintained native/negative/owner-pool-offset/production acceptance yet.

Root README remains aggregate-only. No sibling source/build/save, frozen
Release, runtime launch, host adoption, hardware/gameplay acceptance or push.
