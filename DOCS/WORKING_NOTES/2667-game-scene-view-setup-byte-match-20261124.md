# Scene-view setup direct byte match - 2026-11-24

`func_150FCA30` replaces its zero-return placeholder with semantic C that emits
all **100 original words and 12 relocation sites directly**, using the exact
**80-byte frame**. There are **zero new guards, insertions or omissions**; the
guard CSV is byte-for-byte unchanged.

Production rises from **4,646 to 4,647 / 5,528 (84.06%)**, Game **3,974 / 4,855
(81.85%)**. Init stays 492/492 and Debugger 181/181. Address drift remains zero;
881 functions differ, with **52 more matches needed for 85%**.

## Routine and interface

Original `conker/asm/129EE0.s:11..114`, VA `150FCA30..150FCBC0`, ROM
`129EE0..12A070`. The recovered interface is `void(void)`. The old untyped s32
zero-return placeholder occupied 12 bytes; the new function extent is 400.
The original caller ignores the target's result.

1. Call `func_150FCBC0(0)`, `(1)`, `(2)` in order. The same-owner helper remains
   its original untyped placeholder. A compatible old-style forward declaration
   avoids retyping or crediting it; the actual retail helper narrows to u8.
2. Submit three fixed sound records through the actual twelve-argument
   `func_1000FA64` ABI: u16(u16,s16,s16,s16,s32,u16,s16,s32,void*,s32,s32,s32).
   Kind/coordinates/opaque-angle are `(2B8,-2038,1560,-2631,45)`,
   `(2B7,-319,-273,-3419,0)`, `(2B6,1519,947,-2633,90)`. Common words are
   28000,9000,7000, callback address `func_1000EC24`, then three zeros. The
   callback is an SDK32 code-address word, never directly called here. The
   45/0/90 pointer-sized values are opaque stored words, not dereferenced data.
   Actual declarations/body are in functions.h:986 and init_EB00.c:57/496.
3. Read the live signed count `D_80082FA0` after those submissions. The opening
   gate is signed((u32)count+1)>0: INT_MAX wraps to INT_MIN and skips. The C
   expression uses defined unsigned addition. Index increments as u32; only its
   low byte is passed to `func_15164F0C(4,index.low8,0,255,1)`. Reload count after
   every call and continue while signed(index)<=signed(count). Do not cache the
   count or narrow the full loop index. The provider's actual byte-width ABI is
   established by retained ASM191C30.s and generated_113D60.c:282.
4. Submit an eight-byte `TimedViewRequest150FCA30` to
   `func_151D8868(request,0,255,0)`: byte0=1, signed half2=100, byte4=8, byte5=15,
   signed byte6=-1. **Bytes1/7 remain unwritten**. The request lives at SP+0x44
   within the exact retail frame. Actual generated_205C90.c:50 validates the
   mask/players, allocates, then copies **all eight bytes** into record+0xE.
   Subsequent record code consumes the named initialized fields.

The selected source preserves exact names and uses a local eight-byte type;
there are no shared-header, provider-body, compiler-profile or volatile edits.
No additional helper or caller implementation receives credit.

## Source fit and owner isolation

The initial draft emitted 100 words/frame88 with eight stack-offset differences.
Inlining the callback address expression recovered frame80 and left six request
home offsets. Declaring u32 index before the request produced the literal retail
words/bindings. Only those two fit forms were screened, with ordinary
O2/g3/MIPS2/o32 and the existing GLOBAL_ASM processor; this owner has no special
no-unroll override. The frozen-before compile reproduces the complete production
object literally. All **ten other raw/padded definitions**, bindings, pools and
diagnostic rows remain fixed. Both complete owner padders emit identical object
metadata and instructions.

## Fresh semantic and instruction evidence

- **182 cases per stream**, raw/generic/generated/original, reach all 100 original
  words. Compare complete public/private bytes, registers, dispatched accesses,
  calls and live-count observations. Cases include signed extremes, -2/-1,0..3,
  254..257, independent count mutations during fixed and loop providers, and
  distinct seeded stacks/phases. Return V0 is not compared as a semantic result.
- **164 dispatched-access cut points** compare all four complete states. This
  qualifies emitted instruction prefixes, not portable C fault/EPC semantics.
- Execute the actual **four-word bounded caller window** at 1509D44C, with target
  connected, across four cases. Its branch reaches 1509D76C and loads V0 from
  caller SP+0xC4. Verify saved roles, SP, the target call and that continuation
  value. The complete large switch dispatcher is not claimed.
- **40 connected cases per stream** execute original 151D8868 (111 words), the
  original mask validator151D87E0 (34), and original SDK memcpy (11). Four seeds
  exercise success, and nine bypass/failure gates exercise disable bytes,
  inactive mask, player validation and allocation failure. On success all eight
  copied bytes, including untouched bytes1/7, retain seeded retail values;
  per-player level calls and final record level also match. Allocation, player
  state checks and level providers remain bounded/opaque.
- **182 SDK32 native cases each at O0/O2/O3**, freestanding/static, strict aliasing
  and UBSan traps, compare every call word, live final count, initialized request
  fields, callback-address codec and output guards. Native performs the actual
  eight-byte memcpy; the two unwritten bytes are deliberately not compared with
  guest seed values. No portable C padding determinism is claimed.
- **13 effective native source controls** fail known result comparisons, with
  no signal or UBSan trap counted: reset sequence, sound kind/coordinate/angle/
  callback, INT_MAX gate, stale count, byte-sized index, loop boundary, view
  context, request lifetime/mask/callback.
- Identity pins check all 100 words/12 binding sites and return them unchanged.
  **224 padder corruption observations** keep changed words/bindings visible.
  These are literal mismatch detections, not fail-closed guard rejections.
  The generic oversized body remains explicitly unmatched; the generated
  padder rejects overflow. **12 independent GNU target links / 96 guest runs**
  cover four separate code/callee/global arrangements, including HI16 carry
  and another J-format region.

The first native attempt used system32 headers unavailable in this WSL image;
the project SDK32 freestanding harness avoids that dependency. The O2 startup
fixture required its established force-aligned _start entry. Both fixture
issues were corrected before qualification; neither is a target-code failure.

## Full image and production

Private actual Make replays **five commands**, including the existing ASM
processor; the whole padded owner equals the qualified object. A separate link
uses only frozen-before C plus the original target ASM to construct the expected
image. It reconstructs the complete named-symbol/string metadata without using
the selected target C as truth. The selected C link and later production Make
equal that image **literally: 328 changed bytes, zero exclusions**. All other
frozen inputs/definitions/extents/addresses and all 189,088 protected Game data
bytes across 720 owners remain unchanged; conversion CSV bytes are unchanged.

ELF SHA256: `431d3681c6d0de583458b1e84740a8b13ab40e473cd4f25c4557563aa40908cb`.
Raw target SHA256: `85c49918aded033be87f792d6948db29d26b8aaff7eb726486bdd9133177950f`.
Complete padded owner SHA256: `b8e331cd027b0ec2a23094e573d7b1ce23f8b5bb75a8ccd53737f17204e4a98b`.

| Phase | Time | Gates |
| --- | --- | --- |
| preinstall-primary | 122.974s | 5 fresh / 0 reused |
| preinstall-sibling | 121.326s | 5 fresh / 0 reused |
| installed-primary | 108.938s | 5 fresh / 0 reused |
| installed-sibling | 111.204s | 5 fresh / 0 reused |

Shared tools-check passes separately. No unchanged broad neighbor suite is
called fresh. The isolated sibling overlay records actual imports, data files,
bindings and artifacts while preserving the real dirty tools sibling.
Tools commit `7f9df5c25d44594c296ed82a17b8c82748598332` precedes the consumer
source/pin/docs commit. Codex resolved this routine locally with zero Claude calls.

Graph receipts distinguish normal update, observed commit-hook completion and
the scoped AST merge retaining every prior node ID. This is not full-corpus
re-extraction. Host configuration inputs are reverified; this C owner has no
direct host consumer at the inspected path. No host or Release change/build.
README updates two aggregate rows and their verification date; five DOCS indexes receive one concise
entry with all previous bytes retained. Keep the 85% goal active; renderer 15197148
remains private on its older baseline.
