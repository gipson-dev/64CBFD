# 1843: Owner record admission match

Date: 2026-10-29. Target `func_151ACA60`, owner `generated_1D92F0`.
VA `0x151ACA60..0x151ACB38`, ROM `0x1D9F10..0x1D9FE8`: 216 bytes / 54 words.

The zero-return placeholder becomes a complete three-argument semantic routine
matching its existing s32 address-handle caller interface. It returns zero for
a null owner or failed allocation. Otherwise it allocates class0x30, mode0,
payloadSize+0x30 with 32-bit wrapping, flag1, priority255 and final argument1.
It calls func_151ACB38(owner, record+0x18), frees the allocation on rejection,
and returns zero. Success stores owner at+0x1C, its current unsigned identity
byte at+0x20, the signed index relative to D_800CC2D0/0x32C at+0x24, the scale
float at+0x28, then initializes +0x10/+0x14 to1/0. It returns the record address
as a 32-bit handle. The caller already casts this handle to u8* and forwards it.

Unsigned addition/subtraction followed by explicit signed conversion preserves
retail wrapping without introducing C signed-overflow or pointer-subtraction
undefined behavior. Signed division truncates toward zero. The owner identity
is read after helper mutations and after the owner pointer store, as in retail.
The second argument's float bits arrive in A1 because A0 is the owner pointer;
the third argument is A2. The captured scale is copied without arithmetic.

All 54 words and five relocations emit directly from C under the existing
O2/g3 profile. The original 48-byte frame retains S0+32, RA+36, incoming homes
+52/+56 and the record spill at+44 across admission. No guards, insertions,
omissions, shared-header edits, frame adjustments or compiler-profile changes.
Guard and conversion inventory CSV bytes are unchanged.

Eight fresh canonical methods pass independently in each tools copy, plus
shared tools checks. Installed checks rerun two methods per copy; six semantic
methods reuse only complete input/module/artifact identity.

- Guest: 4,080 cases / 12,240 original/raw/padded executions agree in literal
  full state and cover all 54 words. Cases include null owners, allocation
  failure, admission rejection/cleanup, aliased owner/output storage, helper
  identity changes, signed index differences including 32-bit wrap, payload
  size wrap, signed zeros, infinities, quiet NaNs and both stack phases.
- Native32 O0/O2/O3 each pass 1,320 cases with UBSan and reject eight controls:
  class, size, omitted cleanup, inverted admission, freed result, stride,
  identity source and scale offset. Native NaN payload equality is not claimed.
- 64 access prefixes, three layouts / 108 rebase cases and three sparse null
  executions pass. The original ten-word func_151ACB38 executes in 36 connected
  cases: identity1 writes admission1 and succeeds; other identities reject.
  This adds no helper C credit. Allocator and cleanup remain bounded providers.
- The original eight-word caller window in func_1514D9F4, VA1514DA08 /
  ROM17AEB8, passes 24 cases. It supplies scale20.0/payloadSize0 and forwards
  the returned address, owner and selector20 to func_1514EC1C. Earlier parent
  gates and the final receiver are bounded; full parent execution is not claimed.
- Complete owner compilation/padding preserves 32 neighbors and pools. Five
  actual Make commands reproduce the object with zero C diagnostics. The
  inherited duplicate-recipe Make warning remains. All 221 raw-byte/binding
  controls and 236 whole-image corruption controls reject.
- Strict independent full-image prediction equals production: 159 changed
  bytes = 158 target code + one extent, zero metadata changes or exclusions.
  All 6,055 other linked bodies and all function addresses remain fixed.
  Protected Game data stays exact across 189,088 bytes / 720 owners.

The semantic tests do not execute a complete real allocator, release system,
downstream receiver, entire parent, gameplay or hardware session.

Fresh actual adopted-ELF count: **3,920/5,506 (71.20%)**, Game **3,247/4,833
(67.18%)**, Init492/492 and Debugger181/181, zero drift. **210** more to4,130.
Tools commit first: `6260cb4cdff212caf6b53fe8670f47c2c7772b8e`. No push. Root README contains aggregate rows only.

Scoped AST refresh retains or uniquely relocates all 49,747 prior nodes and
retains all 103,154 prior directed relationships. The target keeps its s32
interface, so no return relationship retires. Helper calls and original caller
metadata are source/binding checked. Outside manifest rows and analytics remain
historical; no full-corpus extraction. The 75% goal remains active.

Artifacts: `conker/build/game-owner-record-admission-match/`. Next screened
target `func_150A278C` still needs complete qualification. Parked candidates uncredited.
Older tools mirror preserves 1,967 inherited dirty paths plus three new modules.
No host-port, frozen Release, save/editor, private-input or memory changes.
Zero Claude calls.
