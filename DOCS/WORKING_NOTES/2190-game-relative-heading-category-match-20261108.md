# Relative Heading Category Match - 2026-11-08

`func_1506B3B8` now matches all **77 words / 308 bytes**, with retail's
**32-byte frame** and local choice byte at **SP+0x19**. Its complete semantic
C uses **34 checked normalization rows**, with no inserted or omitted
instructions. The owner retains its O2/g3 MIPS2/O32 profile and existing
shared table declarations. The obsolete commented attempt is removed and
the generated declaration now agrees with `void func_1506B3B8(void)`.

Production recount: Total **4,259 / 5,513 (77.25%)**, Game **3,586 / 4,840
(74.09%)**, Init **492 / 492**, Debugger **181 / 181**, zero address drift.
There are **1,254** different converted functions and **152** additional
exact functions needed to reach 4,411 / 5,513 and the active 80% goal.
Conversion rows and denominators remain unchanged.

## Recovery and preserved behavior

Owner: `conker/src/game_981E0.c`; VA 0x1506B3B8..0x1506B4EC;
ROM 0x98868..0x9899C. Graphify located the retained work from
[Note 1949](1949-relative-direction-private-semantics-and-codegen-boundary-20261101.md)
and [Note 1950](1950-relative-direction-cfe-stack-home-recovery-20261101.md).
A fresh isolated and complete-owner compile reproduces the selected raw
payload `1db2220b4471fe4d980cc6783866d3abda9a2371b1c09123f6f7d270e16acee2`.
Earlier captures and frozen inputs remain intact; all current adoption
evidence is under the separate `resume-2189/` directory.

Initialize the choice byte to zero. Pass pool-slot-zero X minus current
actor X, current actor Z minus pool-slot-zero Z, and integer zero to
`u16 func_1505A630(f32, f32, s32)`. The first two arguments use f12/f14;
the third is in a2. Reload the actor after this helper before reading its
facing halfword +0x7A and shifted offset byte +0x1FD.

Truncate the angular difference to signed 16 bits, arithmetic-shift its
high byte, and fold its unsigned representation to a magnitude in 0..128.
The -128 high byte folds to 128. Preserve the ordered strict comparisons
against bytes at D_80099A3C, D_80099A43 and D_80099A3E. Apply the
sign-dependent category increment with byte wrap. The table accesses are
explicit byte views of existing legacy halfword declarations.

Clear the captured post-helper actor's +0x138 byte before the selected
table read. Reload the live actor global for the +0x244 halfword store,
then reload it again for +0x21C = 20000. Guest aliases make the clear alter
a table entry or make the result store retarget the actor global; the raw
and normalized programs preserve these exact memory operations and order.

## Address and register normalization

The remaining compiler difference was an equivalent table-address
factorization. The raw stream shares a complete HI16+LO16 table base.
Retail keeps an early HI16 for indexed access and applies the signed
LO16 at each byte load, with a separate threshold-address high half.

The qualifier derives the original form from the raw words, moving the
independent high half, splitting the shared complete address into the two
equivalent accesses, and applying the resulting closed temporary-register
mapping. All 77 instructions survive; the branch structure, memory order,
frame and private choice home stay exact. There are **13 raw bindings /
14 normalized bindings**. The normalization does not copy words from ROM.
All 77 altered-word controls, 13 altered-binding controls and 72 register
metadata corruption controls reject unknown inputs.

Three independent GNU links and 18 focused executions cover table labels
whose low halves cross 0x8000 and wrap near 0xFFFF. The larger guest matrix
also runs at three distinct code/global layouts. The unreachable duplicate
instruction at relative +0xFC is preserved; 76 words are reachable.

## Original callers and action callback

The aligned pristine census finds one direct JAL at ROM **0x989A4** /
VA **0x1506B4F4** in the original eight-word `func_1506B4EC` wrapper, and
one pointer at ROM **0x22AE48** / VA **0x80086388**, D_8008630C[31].
No interior direct entry or interior pointer literal was found.

The original ten-word constructor window, VA **0x1505E394..0x1505E3BC**
in `func_1505E0C4`, installs slot 31's function into the animation state
or clears it for a null configuration. The original invocation is in
`func_1507BDB0`: its 15-word window **0x1507BFBC..0x1507BFF8** saves
live homes, loads state+0, executes JALR at **0x1507BFD0** with delay NOP,
and restores its integer/FP homes before reloading state+0x28.

Fresh checks cover **88 wrapper cases**, **32 constructor cases**, and
**16 installed indirect-callback cases**, for original, normalized and raw
target bodies. The recovered production timeline C independently uses
`state->callback()` and sets the current actor earlier in the same parent.
These bounded windows do not claim full constructor/parent reachability,
complete animation behavior, or emulation of the opaque angle provider.

## Fresh qualification and production

Six focused checks pass before and after installation in both tools
checkouts, using four sequential runs with exact source/dependency hashes.
An earlier successful mounted run preceded cosmetic test-name/import
cleanup; the final four recorded runs use the final identical files.

- **6,148 guest cases** at three layouts, plus **12 alias cases** and
  **299 exact memory-fault cuts**. Original and normalized literal states
  agree; raw C also agrees on complete memory, calls and access traces.
- **4,096 native32 cases per profile**, O0/O2/O3 with trapping UBSan,
  SDK offset assertions, post-helper actor retargeting and canaries. All
  seven semantic controls are effective. Native overlapping table labels
  are consistently seeded separate globals; actual address overlap and
  synthetic global/private aliases belong to guest fixtures.
- All **327** raw and padded neighbors, pools and exact register-mask
  union are preserved. The isolated body agrees with the full owner.
  The actual five-command Make recipe produces the same **328-function**
  padded object. **36 inherited warnings, zero added warnings**; isolated
  target diagnostics are empty. No shared header or compiler-profile edit.

The literal full-image predictor changes only this 308-byte body and its
symbol extent from 12 to 308 bytes: **245 changed bytes, zero exclusions**.
All 6,052 disassembled entries keep their addresses and every other body
and extent remains unchanged. Protected data is exact across 720 owners /
189,088 bytes. Five image-corruption controls cover header, body, extent,
protected data and the owner's file-symbol string.

GNU ld synthesizes an STT_FILE name from this input object's basename.
The first scratch link used a different filename, adding six string bytes
and shifting symbol string offsets despite an identical owner object.
The qualifier now stages the unchanged object bytes under Make's actual
`game_981E0.c.o` basename. Predecessor and current ELF then agree literally;
no metadata exclusion or binary-string patch is used.

Production Make compiles only this owner, links the predicted image,
regenerates an identical progress CSV and passes a fresh recount. The
existing whole-ROM checksum failure (make all exit 2) and duplicate
generated_12D630 recipe warning remain. FP edge cases are model evidence,
not hardware/FCSR or gameplay acceptance.

Both shared tools smoke checks are fresh; three prior regression checks
per copy are explicitly reused with matching helper/test hashes. The
sibling's 2,434 existing dirty paths are fingerprinted and preserved via
a private three-file validation overlay.

Baseline consumer: `89c4a04251ff463a98f55c130fa43bdcd0afe27c`;
tools: `4322edcb7bbb5df6ae28fb00041d1392efeb354b`. There are **117** frozen
inputs. Claude calls: **0**; local compiler, instruction, relocation and
image evidence resolved this bounded recovery without an advisory call.

ELF SHA-256: `dd7d8f793c940feb2244725dff2bd75f10971b3f6574b7b1c4f737fb8d25eb62`.
Binary SHA-256: `364d9a50a42aaf9f8e7c9dee8a71c8b7e88d09e7f3aa10e91643c132c0ef032f`.
Owner SHA-256: `8a254e4b0dec363c0ff6abdca3758e82b59d2d5d9347f770af13e30ed100d010`.
Guard CSV SHA-256: `f67f8d18908dc6db9ba58dfa2db4b4204a7202104e67173c35213711333f4dd9`.

## Resume boundary

Next: **`func_1509C7C8`**, the uncredited selector/status query placeholder
in `conker/src/game/generated_C98F0.c`. The complete body is 77 words /
308 bytes, VA 0x1509C7C8..0x1509C8FC, ROM 0xC9C78..0xC9DAC, with no
frame. Preserve the incoming a2 home spill and qualify the actual caller
interface. Recover the six-entry selector switch rooted at jtbl_8009E458,
the unsigned selector-minus-one bounds check, full-word argument versus
unsigned-byte comparisons, ordered global gates and raw byte-return case.
Do not reduce every return to a boolean. Qualify original table ownership,
source/profile/bindings/labels/neighbors, callers and all normal adoption
gates before installing or counting it. Graphify currently exposes only
its placeholder and neighboring-owner relationships.

Current receipts: `conker/build/game-relative-direction-1506B3B8-match/resume-2189/`.
Tools are committed before the consumer pin. The scoped Graphify refresh
includes an old-node retention audit, preserving existing unscanned nodes
without claiming a new full-corpus extraction. Host Release remains frozen.
The 80% goal remains active.
