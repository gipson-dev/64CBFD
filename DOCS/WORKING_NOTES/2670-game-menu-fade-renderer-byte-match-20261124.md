# Menu fade renderer byte match - 2026-11-24

`void func_151E09DC(void)` replaces its zero-return placeholder with the full
menu fade renderer. C directly emits all **101 original words / frame 40** and
**33 relocation binding sites**, without guards, insertions or omissions.
Production rises from **4,649 to 4,650 / 5,528 (84.12%)**, Game **3,977 / 4,855
(81.92%)**. Init remains 492/492 and Debugger 181/181; zero address drift,
878 functions still different, **49 more matches needed for 85%**.

Original `conker/asm/20AE20.s:3428`, VA `151E09DC..151E0B70`, ROM
`20DE8C..20E020`, 404 bytes. Only this function receives matching credit.

## Complete semantic recovery

1. Set RGBA to 255, submit the text command `(148,126,1,"#",26)`, then set
   font/mode byte 0x81. Prototypes follow the actual definitions in
   `game_70200.c`: four u8 color parameters; two s32 coordinates, u8 style,
   s32 format-address word and variadic payload; one u8 font parameter.
2. After those providers, read the live menu pointer and its signed byte +0x42.
   Select the signed byte in the ten-byte row at D_800AB690, then capture its
   D_800AB754 word. These are **flag words**, not pointers: the real renderer
   counts the low 23 set bits. Preserve the existing overlapping AB690 s8 view.
3. For direction byte D_800E0A96==0, clear bit 0x20 in menu halfword +0x20.
   Compute full signed opacity from unsigned 32-bit subtraction of ticks*32.
   If <=0, reload menu and clear state byte +0x3F; optionally submit settings
   through func_151E2404; then clear D_8008FDE0 and set direction -1. This path
   returns without storing the computed opacity or drawing.
4. For nonzero direction, compute unsigned 32-bit addition of ticks*32 and
   interpret the wrapped result as signed. Clamp signed values >=256 to 255.
   The source uses u32 shift/add/sub, avoiding signed overflow or shift UB.
5. Store the low opacity byte, retaining the full signed value for comparison
   with 255. If the full value differs, reload menu and clear the entire flag
   halfword. Submit `(capturedMask,1,0,lowOpacityByte,0)` to func_151E3344.
6. Reload menu after drawing. If flag bit 0x20 is set, clear direction and
   reread the flag halfword before clearing that bit. The reread matters when
   the direction byte aliases the flag word in guest memory.

The indexed body initially differed in two private stack offsets. Declaring
the captured mask before the opacity value recovers its original SP+0x24 home;
all 101 words then emit directly. No new compiler profile, volatile, register
hint or projection is used. Ordinary O2/g3/MIPS2/o32 is retained.

## ABI-only helper change, explicitly uncredited

The new caller needs the actual five-word rendering interface. Its existing
same-owner helper placeholder is now declared/defined as
`s32 func_151E3344(u32 mask,s32 mode,s32 alternate,u32 opacity,s32 flags)`.
The caller explicitly narrows opacity to u8; the formal remains a full o32
word, consistent with retail's argument-word save and later low-byte access.
The placeholder still returns zero and remains **unrecovered and unmatched**.

IDO emits four argument-home stores before that return: raw size changes from
3 to 7 words, frame 0, no bindings. These stores write only SP+0/+4/+8/+12,
preserving SP, RA, saved registers, the fifth argument at SP+16 and zero result.
Four old/new guest stub cases verify every other byte and public state. Both
original direct helper call sites use normal o32 frames: the current 40-byte
target and func_151DF1BC's 48-byte frame. Actual retail helper code is 968 words /
frame 328 and is not represented as restored. Its matching credit is zero.

All **58 other raw and padded definitions**, pools, bindings and diagnostics
remain fixed. The changed helper is separately audited, never excluded from
the image. Both complete padders use the mandatory jtbl_800AB994 mapping. The
reference builder retains every internal helper jump-table anchor while
reducing only the first padding gap by 16 bytes. An initial reference draft
omitted those anchors and failed linking; it was corrected before qualification.
Both parsed padded objects agree; their object metadata bytes differ, which
is recorded rather than described as whole-object identity across padders.

## Focused fresh qualification

- **303 guest cases per stream**, raw/generic/generated/original, compare full
  private/public memory, registers, accesses and calls. All 101 original words
  execute. Cases cover opacity 0/1/31/32/33/254/255, signed directions, zero/
  negative/extreme ticks, shifted sign-bit and wrap boundaries, signed selectors
  and six provider mutation modes. Three cases alias direction with the
  post-draw flag halfword. A removed-reread instruction control fails the
  expected public result while retaining the same calls and saved registers.
- **97 dispatched-access cut points** compare all four full instruction states;
  this is emitted fault-prefix evidence, not portable C fault semantics.
- Four cases per stream execute the original **four-word caller window at
  151DF0C4** in func_151DE8F0. It branches to 151DF1B0 while reloading the
  enclosing RA fromSP+0x1C. The target result is ignored. The complete
  dispatcher is not claimed as executed.
- **300 SDK32 native cases each at O0/O2/O3**, strict aliasing and UBSan traps,
  compare every mapped menu/guard byte, globals, captured flag word, calls and
  provider changes. Native uses typed nonnegative table backing; signed
  negative indices and cross-global aliases remain guest-only. The text
  provider verifies the actual format address and reads the single intentional
  variadic `int`. It does not claim execution of the real text helper's
  unconditional sixteen-word o32 payload copy.
- **16 effective source controls** fail known result/call comparisons, with no
  signal or UBSan trap counted: tick scale, zero bound, clamp, full-value test,
  completed direction, menu close, save gate, stored alpha, captured flags,
  draw opacity, flag gate/mask, stale menu, text payload, font and color.
- All 101 words and 33 binding sites have **268 corruption visibility controls**
  through both padders. Direct code has no repairing guards: corruptions stay
  visible and unmatched, while the identity pin rejects each. Generated
  overflow rejects; generic overflow remains unmatched. Four independent code/
  callee/global arrangements produce **12 GNU links /96 guest rebase runs**.

## Independent whole image and production

Final review removed a duplicated source comment and excess blank lines.
The pre-install receipts identify the earlier comment layout; both final
installed suites are fresh against the cleaned, newly pinned source. The
earlier installed receipts are archived in before-comment-cleanup. Rebuilding
the cleaned C reproduces the same complete object and ELF; no semantic test
receipt is relabeled as fresh through a comment-equivalence exception.

Private actual Make replays three real commands and equals the complete
generated-padder owner. The independent reference uses frozen-before C,
original target ASM and an explicit seven-word ABI placeholder derived from
the argument-home contract. It reconstructs every named-symbol/string record
from the baseline, changing only the two expected function sizes. Selected C
and production Make equal that prediction literally: **486 changed bytes,
zero exclusions**. All 189,088 protected Game data bytes across 720 owners,
other definitions/addresses/extents, conversion CSV and the entire guard CSV
remain unchanged. The helper stays different; the recount adds exactly one match.

ELF SHA256: `f3ae74a868235d2645f7aa42c301b7892e94a78f45da4cfe2367f360355a64d9`.
Raw target SHA256: `80a09cdad1e1a2aca93255faec3098abe9832b1b7b59ff19e0630f0677c60384`.
Padded owner SHA256: `c514829df6f7d229a2a2eef70d5b6c9381c27ff5d9bcb70ad4d01ffcb1b2d61f`.

| Phase | Time | Gates |
| --- | --- | --- |
| preinstall-primary | 80.002s | 5 fresh / 0 reused |
| preinstall-sibling | 84.390s | 5 fresh / 0 reused |
| installed-primary | 74.631s | 5 fresh / 0 reused |
| installed-sibling | 67.464s | 5 fresh / 0 reused |

The shared tools check passes. Tools commit
`252a216ac03e750e98ba813c3d2815c78167996b` precedes the consumer C/pin/docs
commit. Both tracked trees are clean at the bank and the real dirty sibling
tools checkout is preserved. No push. Codex used zero Claude calls. Complete
immutable inputs are checked once per fresh suite process, mutable phase
outputs at later gates, and native full-bank audits bracket adoption/production.
Graph receipts separate normal update, observed hook completion, scoped AST
merge, old-ID retention, current-definition migration and zero helper credit.
This is not full-corpus re-extraction. Host inputs are separately reverified;
the selected scene configuration still stubs this routine and consumes a binary,
so this C change does not automatically propagate there. No host/Release build
or edit. Root README gets aggregate rows only. Five
DOCS indexes receive concise entries preserving all earlier bytes.
Keep the 85% goal active; renderer 15197148 remains private on its older baseline.
