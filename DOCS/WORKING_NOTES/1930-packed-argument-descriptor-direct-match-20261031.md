# Packed argument descriptor restored directly from C

`func_1510A930` now has complete semantic C in
`conker/src/game/generated_137DE0.c`. All **57 body words and five relocation
bindings emit directly**, with zero guards, insertions or omissions. Three
alignment NOPs complete the original 60-word slot. The recovered interface is
`void *func_1510A930(u32 first, u32 second, u32 third)`; it forwards the
descriptor factory's allocated record or NULL. The only retail caller ignores
that pointer and publishes its own success value.

Actual production Make and an independent recount against the Windows
consumer ELF establish **4,005/5,506 (72.74%)** exact C functions, Game
**3,332/4,833 (68.94%)**, zero address drift and 1,501 still different. Init
remains 492/492 and Debugger 181/181. The guard and conversion-inventory CSVs
are unchanged. The active 75% target is 4,130/5,506: **125 more matches** remain.

## Descriptor and arithmetic

The real body is VA 0x1510A930..0x1510AA14, ROM 0x137DE0..0x137EC4. The slot
ends at VA 0x1510AA20 / ROM 0x137ED0. The 96-byte frame places its 60-byte
descriptor at SP+0x24, with saved RA at SP+0x14.

The private `PackedArgumentDescriptor` names the recovered fields without
changing a shared structure. It publishes asset `D_800917EC`; packs
`(first<<16)|second` at descriptor+8 and `(third<<16)|sum` at+12; stores 10000
at+16 and the low half of the wrapping three-word sum at+20; and supplies
228.0f, the bits loaded from `D_800A26A0`, and the original fixed halfword/byte
parameters. These full-word OR operations do not mask their second operands
to 16 bits. Unsigned shifts and additions express the original wrapping
arithmetic without introducing signed-overflow undefined behavior.

The inputs' higher-level component meaning is not yet established, so their
names remain first/second/third. The C source preserves all 51 bytes written
by retail and leaves nine other bytes untouched. Those nine bytes are the
word at+4, two bytes at+0x1A, one at+0x38 and two at+0x3A. They are not
silently zeroed or promised to have portable C values.

The first candidate already had the correct 57-word length and all bindings,
but its frame was 88 bytes. Frame-size-only screens reached 96 bytes while
leaving 25 descriptor-home instruction differences. Declaring the meaningful
sum and packed-word locals after the descriptor recovers its original SP+0x24
home and every instruction directly. No dummy padding declarations, extra
descriptor fields or compiler-profile change are used in the selected source.

## Original caller and providers

The aligned retail census finds one JAL at ROM 0x534F4 / VA 0x15026044 and no
aligned literal function pointers. Its original eight-word bounded window at
0x15026034 loads a word from caller SP+0x164, performs three word subtractions,
supplies A1/A2, and moves S0 to A0 in the JAL delay slot. After the call it
branches to 0x150265B4 and sets V0=1 in that branch's delay slot.

The original window plus complete target and providers pass 144 cases / 288
executions, including high-bit argument values and both allocation outcomes.
The pointer result is therefore correctly forwarded by the target while being
ignored by this caller. The window test does not establish natural entry
through every preceding parent gate or execution of the complete large parent.

The original eight-word `func_15169968` calls the 26-word
`func_15169900(descriptor,255)`. That constructor calls
`func_15167A68(94,0,76,0,255,1)`; on success it copies 60 bytes from the
descriptor to record+16 with `bcopy`, then returns the allocated record.
Allocation and bcopy remain explicitly bounded service models in this target
suite; their entire internal implementations are not claimed as executed here.
The 34 original wrapper/constructor instructions do execute in connected cases.

A fresh compilation and padding check of the unchanged `generated_196DB0`
provider owner reproduces its existing object exactly, preserving all four
functions. Provider source, assembly and object inputs are frozen alongside
the target and caller evidence. No provider repair is needed.

## Guest and native qualification

The guest matrix passes 1,456 cases / 2,912 executions, including 728 cases
with the original connected providers. It covers all 57 target words, both
supported stack phases, varied initial stack contents, complete 32-bit inputs,
wrapping sums, success/NULL allocation, and live descriptor/global mutations
at the allocation boundary. The copied descriptor, returned pointer, public
effects, calls and saved register state agree. Callee-saved GPR/FPR registers,
SP and RA are preserved.

Two independently linked code/global profiles add 32 executions with distinct
global high halves and signed-low16 carry boundaries. Both complete payloads
remain identical. There are 102 fired access-prefix cases and three guest
descriptor/scalar aliases. The alias tests preserve the original fact that
the asset store precedes the scalar load. Guest checks include all copied
bytes relative to the explicit initial stack fixture; they make no portable
C padding, fault or overlap claim.

Native32 asserts the 60-byte descriptor size and important offsets. O0/O2/O3
each pass 728 cases under UBSan, checking both returned pointer outcomes,
defined descriptor fields, scalar bits and record canaries. Native observations
avoid the nine indeterminate bytes. All eight compiled negative controls fire:
masking the second input, truncating the sum, dropping the third term, replacing
packed OR with addition, changing the asset, changing a fixed halfword,
replacing the scalar load, and discarding the returned pointer. Scalar tests
include zero, negative zero, 1.0 and a quiet-NaN bit pattern; no FCSR or hardware
NaN-exception behavior is claimed.

## Make, whole image and commits

The complete one-function owner compiles with no diagnostics or changed pools.
The actual normal three-command generated-owner Make recipe reproduces the
independently padded object. There are no owner neighbors to exclude. All 228
payload-byte corruption controls, five binding controls and two scope controls
fail closed. The protected provider object remains unchanged.

The initial whole-image predictor exposed 14 additional metadata bytes:
`D_800A26A0` and `D_800E0BAC` exchange two adjacent named symbol records and
their equal-length strings. The predictor validates their precise original
names, records and string offsets, then models that closed permutation. It
does not mask or exclude metadata. Private and production ELF files now match
literally across the full image, with **194 changed bytes** including that
14-byte permutation. All 6,055 other linked bodies and every address remain
fixed. Protected Game data is exact across 189,088 bytes and 720 owners.

The full 17,392-file predecessor seal has only the expected target source,
object and ELF changes, with no unplanned dependent-object differences. Eight
fresh target tests pass in both tools copies; both shared checks and the
installed production suite pass. Tools `555d11a` are committed before the
consumer pin. The independently dirty older mirror is preserved and is not
committed. Nothing is pushed.

Production ELF SHA-256:
`2847bf0af139e1e48fe62a34b41f3bb4a03335309e2c19826936e387c4bdbacf`.

With the prepared inputs and retained stage:

```sh
python3 -m unittest tools.tests.test_game_packed_argument_descriptor_match -v
make tools-check
make -C conker -j4 build/conker.us.elf progress.csv
python3 tools/match_progress.py conker/progress.csv conker/build/conker.us.elf conker/conker.us.bin
```

Stage: `conker/build/game-packed-argument-descriptor-1510A930-match`. Receipts
include `preparation.json`, `runtime-qualification-v9.json`,
`production-v17.json`, `production-seal-changes-v17.json`,
`installed-audit.json` and `native-production-recount.txt`. The complete
Native/cache current seals and final banking audit are retained there.
Scoped Graphify refresh preserves prior valid node/edge occurrences and
archives the obsolete placeholder return relationship with provenance; there
is no full-corpus extraction or global reclustering claim.

Next screen: `func_15185B54`, a 60-word interpolation routine in
`generated_1B1600`. Qualify the output vertex layout, returned cursor, float
division/truncation and original caller before installation. Existing private
candidates remain uncredited.
