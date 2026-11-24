# Actor state-motion callback byte match - 2026-11-23

`func_150B12FC` replaces its zero-return placeholder with the complete actor
movement-state callback. All **98 words / frame 56** and **11 relocation sites**
are byte-exact after a pinned, independently proved normalization of the
98-word semantic C body. It uses **98 expected-word guards, zero insertions and
zero omissions**; this is a guarded match rather than direct raw C identity.

Total rises from **4,641 to 4,642 / 5,528 (83.97%)**; Game becomes
**3,969 / 4,855 (81.75%)**, Init stays 492/492 and Debugger 181/181. There is
**zero address drift**, 886 different functions and **57 more matches to 85%**.

## Actual routine, data and caller interface

The complete original is `conker/asm/DE5A0.s:149..252`, VA
`150B12FC..150B1484`, ROM `DE7AC..DE934`. The callback is slot 7 of
`D_80086014`, original word `80086030` in `conker/asm/data/22AAC0.rodata.s:29`.
The actual active caller is original `func_1504A730` in
`conker/asm/nonmatchings/game_77AD0/func_1504A730.s:264`.

Its complete 14-word dispatch window, VA 1504AB00..1504AB38, checks actor+0x25C
bit 0x200, indexes the table with the actor's first word, skips null entries,
and passes the captured actor pointer in the JALR delay slot. After the callback,
it reloads the actor's first word. The callback result is unused, agreeing with
the recovered `void(struct127 *)` interface. The existing table declaration
uses a scalar word for this pointer; no unrelated table-wide type repair or
extra caller matching credit is claimed.

1. Capture the old signed 16-bit moving angle at actor+0x76 and write counter byte
   +0x80 to 10. Read the unsigned byte selector at+0x13F, fetch its pointer word
   from `D_800D2104`, and read signed 16-bit row+2 as a float.
2. Call `func_15058EA4(actor,height,1,height,D_8009F8BC,12,-16)` using its actual
   pointer-plus-six-floats ABI, then call `func_15056B08` with the actor word.
   The latter's existing C is still a stub and supplies no semantic provider
   proof. Retain its existing `s32(s32)` declaration and SDK32 pointer conversion.
3. Wrap `(oldSignedAngle-currentUnsignedAngle)*6` to signed 16-bit, convert to float,
   scale by exact 0x3B800000 (1/256), and subtract the live actor+0xC4 value.
   Clamp through the original ordered greater-than6 / less-than-6 comparisons.
4. Smooth actor+0x148 as `old+(clamped-old)*D_8009F8C0`, store and reload it,
   then accumulate it into actor+0xC4. Read facing angle+0x7A, add 0x4000 with
   signed 16-bit wrapping, multiply by exact 0x3BB40000, and store float+0x40.
5. Call `func_15059140` and `func_150535F4` with the same captured actor. If
   the predicate returns 0, call `func_1502178C(actor,0,-1)`. Preserve its existing
   unspecified-argument declaration while the actual three-word call is qualified;
   its stub is not substituted as semantic evidence.

Original global words are BF333333 (-0.7) and 3D4CCCCD (0.05), in
`conker/asm/data/244360.rodata.s:35..41`. The second coefficient is read live
after the providers, not cached before their arbitrary public effects. Existing
`struct127` fields and their actual offsets are retained in production C.

## Source recovery and closed role normalization

Existing O2/g3/MIPS2 remains unchanged. The first semantic draft emitted
99 words / frame 56, with 69 differences over the common extent. Expressing
the final speed accumulation as `actor->unkC4 += actor->unk148` recovered
98 words / frame 56, with 62 raw word differences and different binding positions.
Additional signed-field, declaration-width, clamp and expression-lifetime fits
were measured and retained privately; none justified an ISA/profile change or
a volatile declaration. The complete four neighboring routines, pools and
diagnostics remain fixed throughout the selected full-owner compilation.

The normalizer derives its output from fingerprinted instructions and bindings,
without copying the retail body. It closes the GPR and volatile-FPR allocation
cycles, renames the private old-angle short home from SP+0x36 to SP+0x34, and
reorders ordinary RAM work across statically disjoint fields/stores. The
initial LHU becomes LH: its extra extension bits die in the following SH and
the post-provider signed reload remains unchanged. Coalescing correction and
clamped roles into F0 removes an internal MOV.S copy, represented by the retail
NOP in the same slot. No instruction count or frame-size adjustment is needed.

A separate finite-path interpreter imports neither this projection nor its
instruction map. Functional public-memory store/select terms preserve arbitrary
table/row aliases with the actor. It checks both final-predicate choices for
all three clamp paths, ordered FP operands/conditions, full public memory at
each call, arbitrary compatible provider effects, and all o32 saved registers.
Nine semantic mutations must fail by public/call/FP observation difference;
changing the first unsigned short load to signed and renaming FP12/FP14 must
both pass. Unsupported instructions are not counted as negative-control success.

This proof covers normal nontrapping ordinary RAM and compatible returning o32
providers without private-address/return-address reflection. The owner and named
global storage objects are distinct; table and row data may alias public actor
storage. Reads commute only across statically disjoint stores. Raw private/fault
identity, FCSR/hardware exception behavior and full transitive helper semantics
are not claimed. Padded/retail complete state and fault prefixes are separately
compared literally by the bounded guest model.

## Fresh validation and linked audit

| Run | Elapsed | Gates |
| --- | ---: | --- |
| preinstall-primary | 150.501s | 5 fresh / 0 reused |
| preinstall-sibling | 139.679s | 5 fresh / 0 reused |
| installed-primary | 138.028s | 5 fresh / 0 reused |
| installed-sibling | 144.147s | 5 fresh / 0 reused |

- **1,056 guest cases per stream**, covering signed 16-bit boundaries/wrapping,
  upper/lower/NaN clamp behavior, provider changes to angles, fields, globals
  and table state, and separate, angle-row, counter-row, table-owner and
  global-row aliases. All reachable retail words execute; word 57 is an original
  unreachable duplicate constant load, protected by literal identity and guards.
- **125 complete dispatched-word/access fault prefixes** across both padded
  streams and retail; no raw/private or portable-C fault claim.
- **45 actual 14-word dispatch-window cases per stream**: 15 calls, 15 disabled
  paths, 15 null-entry paths. Check A0's delay-slot pointer, saved roles, exact
  boundary and post-callback actor-kind reload. This is not execution of the
  entire `func_1504A730` routine or its surrounding gameplay.
- **256 SDK32 native cases at O0/O2/O3**, strict aliasing and UBSan, typed
  actor/table/row/global backing, exact offset assertions, endian/pointer
  normalization and all public/guard bytes compared. The 768 public-alias and
  32 nonfinite cases stay guest-only; native NaN payload identity is not claimed.
  Ten source controls all reach known comparison exits, including late old-angle
  capture, wrong wrapping/height/clamp/facing and a stale smoothing coefficient.
  Signals and sanitizer traps are not counted as successful controls.
- Both padders reject **218** changed-word/binding controls, covering all 98
  source words and all 11 sites. **12 independent GNU links / 96 guest runs**
  qualify four code/callee/global arrangements, including split HI16/LO16 carry.
- Actual Make owner replay and both complete padded objects agree. The independent
  reference uses frozen old C plus original target ASM; complete ELF prediction,
  actual C linking and production Make agree byte-for-byte: **318 changed bytes,
  zero exclusions**. All 189,088 protected Game data bytes / 720 owners remain exact.
  Named definitions and string values are reconstructed exactly, including the
  predicted target extent change and a two-record symbol-order swap; four owner
  neighbors, other addresses/extents, data and guards stay fixed.

```text
before ELF: 59ab46e1e44ec85c881dd0129386500be582a270c8fcdcb417593c7f75d2e540
after ELF:  15111e092d033e4adc11be4b503a4939feefad2e7a837a4bfd03952523fe86f1
owner:      f6a0914b7b1968fd0b0cc49c12471fec1c7658914342301800274627b2bdbfaf
```

The initial primary run passed four gates and failed an inherited empty-symbol-
permutation expectation in gate1. The independent reference had already predicted
exactly two reordered records (D_8009F8C0 and D_800964C0 at indexes5459/5460),
with their named addresses/values unchanged. The test now pins that exact pair;
the failed receipt is retained and all final paired runs are repeated fresh.
No source, normalizer, predicted image or named-definition check was relaxed.

The prior guard history is retained byte-for-byte with only 98 target rows
appended. Production Make holds the inherited guard dependency timestamp old
with `-o retail_word_patches.us.csv`; the changed owner still rebuilds and reads
the new guards. Every unrelated frozen input is audited unchanged, including
conversion rows, layouts, headers and Debugger. Prior unchanged neighbor-suite
receipts are reused by fingerprint, not described as fresh tests. Shared
`make tools-check` passes; the existing duplicate-recipe warning is retained.

Tools commit `a6812341209fcaee668f0a6dbafa5d440dadfdb7` precedes the consumer
source/guards/pin/docs commit. The real dirty tools sibling is preserved through
an isolated pinned overlay. Both inspected host scene configurations consume
binary artifacts; the selected scene lists this target as a stub. No direct
host C consumer or complete host build root was found at that path, and no host
build, Release change or new gameplay acceptance is claimed.

Codex resolved the routine locally with zero Claude model calls and no account,
provider or model changes. Graphify receipts distinguish normal fail-closed
refresh, observed hook completion and scoped AST refresh with old-ID retention;
this is not full-corpus extraction. README changes only its two aggregate rows;
the five DOCS indexes gain a short entry with every prior byte preserved.

The 85% goal remains active. Continue the next ordinary unmatched Game function
from this committed checkpoint. Renderer `func_15197148` remains private and
uncredited on its separate older baseline.
