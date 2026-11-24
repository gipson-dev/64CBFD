# Menu transition initializer byte match - 2026-11-24

`func_151E53E8` now emits all **101 original words / frame 24 directly from C**,
including all **37 relocation binding sites**, without guards, insertions or
omissions. Its complete semantic body replaces the zero-return placeholder.
Production rises from **4,648 to 4,649 / 5,528 (84.10%)**; Game is **3,976 /
4,855 (81.89%)**. Init remains 492/492 and Debugger 181/181. Address drift is
zero; 879 functions differ and **50 more matches are needed for 85%**.

## Interface and behavior

Original `conker/asm/20AE20.s:8688`, VA `151E53E8..151E557C`, ROM
`212898..212A2C`, 404 bytes. Recovered interface:
`void func_151E53E8(s32 defer)`. Direct callers ignore the return. The full
32-bit argument must survive until the final condition: `256` stores a zero
low byte but still follows the nonzero branch. The source comment explains
that distinction. No caller/helper implementation gains matching credit.

1. Clear word D_800E0A90 and bytes D_8008FE2C / D_80087270[0], preserving the
   emitted ordering around the D_800BE616 gate read. If zero, set D_800E0B94=4
   and finish. Otherwise set D_800E0B94=7 and D_8008FD74=8.
2. Read the live menu pointer D_8008FDD4 and signed selector byte +0x42. Its
   ten-byte row in D_800AB68C has a signed byte at +7. A value other than -1
   sets menu state +0x3F=4 and handler word D_800E0A88=func_151E4BD8; -1
   instead sets state 3 and handler func_151DDBA0.
3. For each index below the live signed byte D_8008FD90, follow the actor's
   struct126 pointer at +0x31C in the 0x32C-byte struct127 record and write
   its signed halfword +0x1AA to live menu +0x6C + index*12. The real shared
   struct types provide both offsets; no unrelated shared ABI is retyped.
   The original reloads both menu pointer and count after each store.
4. Mask halfword D_8008FDC0 with 0xE35F; store the argument's low byte in
   D_800E0A86. Reload menu/selector/row. If the signed row byte is -2,
   full-word defer==0 calls func_151E4BD8 immediately. Nonzero defer sets
   handler func_151DDBA0 and state 3. Other row values return.

D_800E0A88 remains the owner's existing 32-bit code-address word. Native checks
compare actual function addresses through an explicit codec and verify the
immediate call. func_151DDBA0 already has void(void); func_151E4BD8 retains its
existing compatible untyped s32() placeholder, whose result is ignored.
Neither its real implementation nor the complete handler dispatcher is claimed.
The overlapping existing AB690 row declaration is preserved.

## Direct source fit and complete owner

The first semantic draft emitted the correct 101 words/frame 24 but differed
in five scheduling/branch words. Bounded assignment-order/loop experiments
found the natural indexed actor loop, which produces all original instructions
and bindings directly. No volatile, register hints or new compiler profile.
The source uses the real actor types, a signed loop index and explicit byte/
halfword accesses. Existing SDK/compiler flags are O2/g3/MIPS2/o32.

Makefile's owner-specific `RETAIL_RODATA_SYMBOL=jtbl_800AB994` is required and
was passed to both complete padders. The frozen before-source regenerates the
entire before-owner literally. All **59 other raw and padded definitions**,
their bindings, pools and diagnostics are unchanged; this does not assert
that all 59 are matched functions. Both padders' complete parsed objects agree.
Their object metadata bytes differ, which is retained in the report rather
than represented as whole-object identity between implementations. Actual
Make's three-command owner recipe equals the generated-padder object literally.

## Fresh focused qualification

- **246 guest cases per stream**, raw/generic/generated/original, compare all
  public/private memory, registers, access traces and calls. All 101 original
  words execute. Independent public semantics cover signed counts -128/-1/0/
  1/4/127, row values -128/-2/-1/0/127, signed selector extremes, gate 0/1/255,
  and full-word arguments 0/1/256/-1/INT_MIN/INT_MAX.
- Six guest cases alias the first output store with the live count or the
  menu-pointer word, verifying termination and redirected later stores. These
  are guest memory evidence, not a claim of portable cross-object C aliasing.
- **159 access cut points** compare complete state across all four instruction
  streams. This qualifies emitted fault-prefix order, not portable C faults.
- Three original bounded caller windows run four cases per stream: four words
  at 150261AC, four at 1509FB28, seven at 1509FBA0. They verify zero arguments
  supplied from nonzero incoming A0, the full script argument from S0+8,
  the third caller's halfword flag store, and the first two callers' original
  continuations and return values. The third window stops at 150AE280's entry
  after its JAL/delay slot; that helper restores SP and branches into another
  routine. Its first six instructions are frozen and checked against retail.
  No ordinary return from that stack-switch helper is assumed. The enclosing
  2032-/367-word dispatchers are not claimed as fully executed.
- **240 SDK32 native cases each at O0/O2/O3**, strict aliasing and UBSan traps,
  use the actual struct127/struct126 layouts and check menu writes, sentinels,
  all globals, handler addresses and immediate-call state. Native selectors
  are restricted to 0..127; negative selectors and cross-global aliases remain
  guest-only. The fixtures allocate extra backing for safe corruption tests.
- **11 effective source controls** fail known comparisons, with no crash or
  UBSan trap counted: gate, clear, signed count, bound, output stride, actor
  value, mask, argument truncation, row test, handler and state.
- All 101 words and 37 binding sites are covered by **276 corruption visibility
  controls** across both padders. Direct matches have no repairing guards:
  changed words/bindings remain visible and unmatched. The identity pin rejects
  each change. Generated overflow rejects; generic overflow remains unmatched.
- Four independent code/callee/global arrangements produce **12 GNU links and
  96 guest rebase runs**, including HI16 carry boundaries and another J region.

The first native fixture had an unused memcpy and incorrectly mapped selector
-128 to +128, outside its stated typed domain. Those fixture defects were fixed
before the final gates. An early sibling import was attempted while its overlay
was still copying; it ran no tests. Only the subsequent fresh successful suite
is credited. A later audit identified the third caller's stack-switch helper;
its initial simulated return was removed, and the corrected seven-word window
stops before the helper body. The pre-install receipts retain the earlier test
version. Both final installed suites are fresh against the corrected tests;
their previous installed receipts are archived and uncredited. The decomp C,
raw target, guards and linked ELF did not change during this test correction.
Real dirty sibling files and status are preserved. Complete frozen
inputs are verified once per fresh suite process; mutable outputs are checked
again at phase gates, with native full-bank audits around adoption/production.

## Full image, production and records

The independent reference uses frozen-before C plus original target assembly,
not the selected C as truth. It reconstructs every named definition and the
complete string/symbol metadata from the baseline. Selected C and production
Make equal that prediction literally: **328 changed bytes, zero exclusions**.
All 189,088 protected Game data bytes across 720 owners, all other frozen
definitions/addresses/extents, conversion CSV bytes and the **entire guard CSV**
remain unchanged.

ELF SHA256: `4ae07341fd0289db40087e50c6fb7c464774f43f88ce9ef03bcb7e5f6ae68bd6`.
Raw target SHA256: `67f6a610147c0874b411280770f5c340029509d643067d47a022f2ca64b76e07`.
Padded owner SHA256: `11c0e165facf77010b8a3dc60af812db38455c2e40d0d341aa426c2a61b2ee68`.

| Phase | Time | Gates |
| --- | --- | --- |
| preinstall-primary | 74.117s | 5 fresh / 0 reused |
| preinstall-sibling | 83.233s | 5 fresh / 0 reused |
| installed-primary | 62.458s | 5 fresh / 0 reused |
| installed-sibling | 71.094s | 5 fresh / 0 reused |

Shared tools-check passes separately. Initial tools commit
`10ab515f24e60b541ce93d6c1e37d9bd913b4606` preceded source adoption.
A focused tools follow-up, `88df181bed573f8e6342e2ccd8ec474023502615`, records
the corrected caller boundary before the source/pin/docs consumer commit.
No push. Codex used zero Claude calls. Graph receipts separate
normal update, actual observed commit-hook completion and scoped AST merge
with old-ID/qualification retention; this is not full-corpus re-extraction.
Host configuration inputs are reverified without a direct C consumer at the
inspected path. The selected scene configuration still lists this routine as
a stub and consumes a binary input, so this C recovery does not automatically
reach that host scene. No host/Release build or edit. Root README gets two aggregate
rows only. Five DOCS indexes get a concise entry preserving all previous bytes.
Keep the 85% goal active; renderer 15197148 remains private on its older baseline.
