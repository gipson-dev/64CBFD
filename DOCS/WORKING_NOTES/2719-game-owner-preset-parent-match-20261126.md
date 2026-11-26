# Owner preset parent direct match - 2026-11-26

`func_1518F5D0` replaces the zero-return placeholder in
`conker/src/game/generated_1BA1D0.c`. **All 125 words / 500 bytes and all seven
binding positions emit directly from semantic C**, with the original 200-byte
frame and zero guards. VA `0x1518F5D0..0x1518F7C4`, ROM
`0x1BCA80..0x1BCC74`; the function fills its slot. No insertion, omission,
alignment tail, compiler-profile or Makefile change. All 60 raw/padded
neighboring functions, pools and the complete guard CSV stay unchanged.

Production: **4,698 / 5,528 (84.99%) total**, **4,025 / 4,855 (82.90%) Game**,
Init 492/492, Debugger 181/181, zero address drift, 830 still different.
**One more accepted match reaches 85%.** One new matching credit; conversion
rows and denominators stay fixed. No new wrapper, child or helper credit.

The recovered ten-word interface returns a record pointer and receives an
actor, an existing 80-byte `Generated1BA1D0Preset`, signed16 lifetime, three
signed8 selectors, an unsigned8 value, signed32 extra size, unsigned8 channel
and full32 context. The typed local forward declaration now describes this
interface; the already-matched wrapper compiles identically. Local type/field
names describe measured roles and are inferred, not original source names.

The 92-byte packet contains progress0 at offset0, the captured preset at4,
an originally unwritten child-pointer word at0x54, two selector bytes at0x58/
0x59, a value at0x5A and an unwritten byte at0x5B. The 16-byte header contains
actor pointer0, ID byte4, signed16 lifetime6, finite flag8, four zero bytes9..12
and active byte13. Bytes5/14/15 remain unwritten. Lifetime-1 produces300 and
finite0; other signed16 values are retained with finite1. There are no new
padding initializers or invented local fields.

The primary factory receives `(&header, extraBytes+0x60, channel, context)`.
A successful main record receives the original 92-byte packet at0x30. For
selector-1 the attached child field is cleared; otherwise the routine calls
the newly restored `func_1519021C(main, actor, (u8)selector, lifetime, channel,
context)` and stores its result at main+0x84. The resource word at main+0x78
is read after that child call. Actor XYZ are read and truncated after the
resource call. Event0x4D receives signed16 coordinates,15000,2000,800,
the `func_1518E298` address, **main record as argument8, actor as argument9**,
then two zeros. The main record, including NULL, is returned independently of
opaque helper return values. The extra four requested payload bytes remain
outside the 92-byte copy. The event callback is forwarded as a 32-bit address;
its implementation is not invoked or newly qualified here.

The first natural body already had125 words and all bindings, but frame192.
Separating the finite flag into its actual integer value recovered frame200,
the original branch shape and register roles, leaving17 stack-address words.
The selected declarations are `header; s32 finite; packet; attached; created;`.
They naturally reproduce packet SP+0x58..0xB3 and header SP+0xB8..0xC7, with
saved S0/S1/S2/RA at0x38/0x3C/0x40/0x44. No dummy locals, larger objects,
alignment unions, physical register bindings or word guards are used.

Validation:

- Both complete production padders and the actual three-command Make recipe
  agree on the entire owner. Four existing Warning712 diagnostics remain at
  the two `func_1518E4A0(arg0)` and two `func_15190454(arg0)` calls, with exactly
  their old normalized signatures. Zero new compiler diagnostics; no warning
  suppression or unrelated source repair.
- Guest: 1,008 cases per each of five identical streams, all 125 target words
  and781 access-fault quintuples. Full private memory, GPR/FPR, HI/LO, FP/FCSR,
  trace and fault states agree. An independent complete-parent reference
  compares public memory, header16/packet92 observations, call order, copied
  bytes, FP operations and returned pointer. The original109-word child is
  connected and ROM/frozen-ELF pinned. The original11-word memcpy also executes
  on nonmutating paths. Allocation failure, selector-1, invalid child presets,
  child NULL/success, signed widths/high incoming bits, descriptor/output and
  actor/output aliases, caller-stack input, helper mutations and four rounding
  modes are included. All original unwritten guest bytes remain observable.
  Some guest aliases produce invalid FP conversions, handled by the stated
  software truncation/FCSR model; native C uses only finite signed32-range
  inputs. No hardware acceptance or original primary-allocator execution.
- Native: actual selected C in three typed units,4,096 cases at O0/O2/O3,
  strict aliasing/FP, UBSan traps and LTO type checks. The providers observe 13
  initialized header bytes and87 initialized packet bytes. Capture alone
  canonicalizes the three unknown header destination bytes and the one final
  packet padding byte. The child word is fully compared after its mandatory
  overwrite. Source/runtime padding behavior is unchanged. A descriptor
  aliases a real typed member of the output record, testing capture before
  allocator mutation. Child/resource providers mutate reachable state to
  discriminate late resource/actor reloads. Typed arenas, canaries, metadata,
  copy order, returned pointer and MXCSR agree, across four rounding modes
  and existing flags. Ten semantic controls finish with comparison exit42,
  including a late descriptor copy, wrong child store and reversed event
  pointer arguments; no compiler failure, trap or signal counts as rejection.
- The first O3 fixture comparison differed in the precision flag at case520
  with visible provider implementations. Preserving the intended opaque call
  boundaries with provider-only `noipa` attributes makes O0/O2/O3 agree without
  changing the actual recovered C, compiler flags or reference behavior. This
  is a native test-observer boundary, not a claimed retail/compiler defect.
  The rejected pre-boundary binary is retained privately. Native services are
  deliberate opaque replacements, not original backend implementations.
- Complete original wrapper `func_1518F51C`:45 words/frame56, ASM/ROM/frozen
  ELF equal.192 cases per original/raw parent stream,48 connected parents
  each, all 45 wrapper instructions. An independent semantic-parent provider
  counterpart agrees publicly; literal private states agree. The ten-word
  ABI, 80-byte preset stride, NULL actor, failed selector/allocator and returned
  pointer passthrough are qualified. Three poisoned parent returns change the
  wrapper result, and a wrong stride40 is rejected by complete execution.
  Selector/table fixtures remain opaque. The aligned ROM census finds one
  direct JAL at0x1BCA68 and no pointer words. No new wrapper/helper credit.
- Both scoped padders expose250 word and14 binding corruptions. Twenty GNU
  links and100 guest rebases independently move parent/child services,
  callback, child tables and scalar through jump regions and signed-low carry
  seams. Rebased child instructions are derived from the frozen owner ASM,
  not an untracked prior build object. Oversize is visible to the generic
  padder and rejected by the generated padder.
- The existing36-word primary factory,109-word child and11-word copy are
  pinned to ROM/frozen ELF. Static pins remain separate from connected child/
  copy execution and grant no new helper credit.
- Independent frozen old-C plus original-ASM prediction equals the complete
  private and production ELF: **383 changed bytes, zero exclusions**. All
  189,088 protected Game-data bytes across 720 owners stay fixed. ELF SHA256:
  `80a0d1b42529e0c697bc7a0df62c99994806d052b39bf3f95612d275851398f3`. Native indeterminate-byte boundaries are not image
  exclusions.

| Phase | Elapsed | Tests |
| --- | ---: | --- |
| preinstall-primary | 129.793 s | 5 fresh / 0 reused |
| preinstall-sibling | 128.388 s | 5 fresh / 0 reused |
| installed-primary | 112.072 s | 5 fresh / 0 reused |
| installed-sibling | 129.269 s | 5 fresh / 0 reused |

All 20 packaged target tests are fresh with identical primary/isolated-sibling
task, source, import and data fingerprints. Shared tools-check passes; prior
unchanged broad-suite receipts are reused explicitly, not called fresh.
Frozen inputs:3983; snapshot copies:2916.
The separately dirty real tools sibling remains intact. Tools commit:
`f16752b04e974bed859a89bebf6689ce09a6268c`. Baseline consumer:
`ad19626581bc5e6b0a78f3bd76fbe2ed38ad4b0d`. Receipts:
`conker/build/game-owner-preset-parent-1518f5d0-private`.

One tools-disabled Sonnet advisory reviewed the earlier 17-word placement
packet (`83ff5704d76102c4f089c429448613acafc599e26653a3c4acaf787a6a67b054`), using the confirmed logged-in OAuth
profile in an empty cwd with hooks/MCP/session persistence disabled. It
recommended testing aggregate order and the finite local's position. The
parallel local experiment had independently found exact order 14023 before
the advisory returned. The actual compile establishes that result; source
provenance and compiler-internal allocation hypotheses remain unproved.
No second advisory call or subagents, and no matching credit from review.

The historical generated host target remains an empty stub; active host
implementation is unqualified. No host transfer/build/launch, Release change,
push, gameplay or hardware acceptance. Scoped Graphify refresh audits all 61
owner definitions and retains old IDs/qualification metadata after observing
actual hook termination. This is not full-corpus extraction. The root README
receives aggregate/date rows only. The active target is now 90% total, requiring 4,976 matches.
Current status records 278 more accepted matches to that updated target.
