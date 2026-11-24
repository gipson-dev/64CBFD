# Scene-node render pass byte match - 2026-11-23

`func_15030E08` replaces its zero-return placeholder with the complete scene-list
render pass. The semantic C emits **100 words / frame 72**. An independently
proved redundant shift-mask elimination and closed temporary-register rename
produce all **99 retail words**, using **100 expected-word guards, no insertions
and one omission**. This is a guarded C match; the raw C is not byte-identical.

Total rises from **4,642 to 4,643 / 5,528 (83.99%)**; Game becomes
**3,970 / 4,855 (81.77%)**. Init stays 492/492 and Debugger 181/181.
There is **zero address drift**, 885 different functions and **56 more to 85%**.

## Routine and actual interfaces

The complete original is `conker/asm/5D2C0.s:1161..1272`, VA
`15030E08..15030F94`, ROM `5E2B8..5E444`. Its interface is
`Gfx *(Gfx *cursor, s32 view, s32 mode)`.

1. Capture `D_800C3EE0` once; an empty list returns the incoming cursor.
   Capture node+0x54 before any provider, and skip disabled node byte+3.
2. Resolve node byte0 through `func_15083E90`. Skip a null actor, zero actor
   word+0x1D4, or a fully present view bit in actor byte+0x74.
3. Keep `1U << (view & 31)` in semantic C so every 32-bit view word has a
   defined shift. Preserve the original full view word passed to providers.
4. Mode2 bypasses the filter and draws only actor byte5==7. Other modes call
   `func_1506196C(actor,view)` before reading the live node flags and actor state.
   Mode1 draws if flags&2, status!=255 or actor.state==1. Other modes draw if
   flags&2 is clear, signed status>=255 and actor.state!=1. Keep the full signed
   word contract rather than replacing both comparisons with one sampled range.
5. Draw with `func_150311C4(cursor,node,actor,view,0)`, retain the returned cursor,
   and advance through the captured next link even if providers change the head
   or current link. Future nodes and actor fields remain live when visited.

The actual getter in `generated_AEB40.c:442` takes a byte and returns a pointer.
The existing owner's pointer-return/s32-argument declaration is retained: the
actual argument is a zero-extended byte and its word interface is checked.
`func_1506196C` in `game_83300.c:1605` takes `(u8 *,s32)`; its current byte-product
implementation commonly returns 0..255, but the recovered parent preserves its
opaque signed-word contract. `func_150311C4` remains an existing unspecified-
argument s32-return stub. This change retains its legacy SDK32 word-to-pointer
cast and qualifies the actual five-word call without claiming helper semantics.

The actual caller `func_1502BAD0`, `generated_58F80.c:44..114`, routes outer
mode1 -> target0, mode2 ->1 and mode6 ->2. Original JALs at 1502BCE4,
1502BD04 and 1502BD20 pass the retained cursor and full view word. A contiguous
29-word original window, 1502BCD4..1502BD48, exercises all three sites and bypass
paths, then uses the returned cursor for the two following display-list stores.
The complete caller and rendering helper are not executed or credited here.

## Source and independent normalization proof

The first complete semantic draft already preserved the 72-byte frame, all 39
neighbor functions, pools and diagnostics. It emitted 100 words against 99,
with 71 differences over the common extent. Existing O2/g3/MIPS2 stays fixed.
No volatile qualifier, narrower view domain or undefined C shift is introduced.

IDO emits `andi t8,s3,31` before SLLV. SLLV itself masks its shift count to five
bits, so the normalizer omits that ANDI and uses the original view register at
the shift. It closes only the affected temporary-register allocation region,
retargets branches and moves the five binding sites with the surviving words.
The loop's final preload register is a fresh lifetime and stays outside that
rename. Output words are derived from pinned raw words/bindings, not copied
from the retail payload.

A separate interpreter imports neither projection nor instruction mapping.
Its entry relation has two paths; one arbitrary nonzero-node iteration has
28 paths, 14 returns and 14 loop cuts. The entry and arbitrary-iteration relation
establish an inductive/coinductive whole-loop result, including continued
iteration. It compares ordered public reads, branch predicates, formal calls,
arbitrary provider public effects, returned cursor, loop live roles and saved
frame/register state. Dead temporaries and provider register/home clobbers may
differ independently between the two programs.

Fourteen semantic changes must fail by a predicate or public observation
difference, including narrow view masking, incorrect captured-link offset,
mode/state/flag gates, signed status comparison, render arguments and discarded
cursor. A complete T0/T1 alpha rename must pass. Unsupported instructions do
not count as effective negative controls.

The proof covers ordinary mapped nontrapping RAM and compatible returning o32
providers, including public node/actor aliases. It excludes reflection on code
addresses or the private frame. Raw full private/fault identity and transitive
helper implementations are not claimed. Padded and retail private state/fault
prefixes are separately checked literally by the bounded instruction model.

## Fresh validation and full-image audit

| Run | Elapsed | Gates |
| --- | ---: | --- |
| preinstall-primary | 277.049s | 5 fresh / 0 reused |
| preinstall-sibling | 302.348s | 5 fresh / 0 reused |
| installed-primary | 276.060s | 5 fresh / 0 reused |
| installed-sibling | 298.845s | 5 fresh / 0 reused |

- **1,725 guest cases per stream** across raw C, both padded streams and retail:
  empty/short lists, disabled/null/inactive actors, full-word view/mode/status
  boundaries, special modes, list/head/next/provider mutations, shared actors
  and overlapping node/actor backing. Padded/retail complete memory/register/
  instruction state agrees. Original words64/76 are unreachable duplicate
  loads/moves, retained literally and protected by expected-word controls.
- **184 access-fault prefix triples**, with full padded/retail state equality;
  **42 actual caller-window cases per stream**, 21 target calls and 21 bypasses.
  All three call sites and the downstream returned-cursor stores execute.
- **1,501 SDK32 native cases each at O0/O2/O3**, strict aliasing and UBSan,
  typed node/actor/global backing, offset assertions, endian/pointer codecs and
  all public/guard bytes. Shared actor aliases are included; 224 overlapping
  node/actor cases stay guest-only. Ten source controls reach known comparison
  exits; no signal, compile failure or sanitizer trap counts as success.
- Both strict padders reject **210** changed-word/binding controls over every
  raw word and all five binding sites. **12 GNU links /96 execution runs** cover
  four independent code/helper/global arrangements and signed HI16/LO16 carry.
- Both complete padded owners preserve all **39 neighbors, bindings and pools**.
  Their object metadata is not literally identical; parsed text/definitions/
  relocations/pools agree. The generated padder and actual Make owner recipe
  reproduce the same complete object. The existing `jtbl_80096F40_game` setting
  is applied to both padder checks and the independent reference.
- The independent reference uses frozen old C plus only original target ASM.
  Full ELF prediction, actual C linking and production Make agree byte-for-byte:
  **303 changed bytes / zero exclusions**. Every named
  definition and string value is reconstructed, including explicitly predicted
  symbol ordering (0 moved records).
  All 189,088 protected Game data bytes /720 owners remain exact. Every unrelated
  frozen input, address/extent, conversion row, layout and prior guard is fixed.

```text
before ELF: 15111e092d033e4adc11be4b503a4939feefad2e7a837a4bfd03952523fe86f1
after ELF:  8b6184f9c38df6e054d3cf0dc91552c7bc83baabd9dc9f724f679802a6e75cfd
owner:      fdbdeec0c4f05884bd787d4787a084f499c765f1ad46dac5395ac51e2134f817
```

The 100 new guard rows append to the prior CSV bytes. Production Make holds
only the inherited guard dependency timestamp old with `-o retail_word_patches.us.csv`;
the changed source still rebuilds and reads the new guards. Unchanged earlier
receipts are retained by fingerprint and are not described as fresh tests.
Shared `make tools-check` passes.

Tools commit `267566474693b9ec5b5e3846cf5d7c7e8fcdb22f` precedes the consumer
source/guards/pin/docs commit. The real dirty tools sibling is preserved through
an isolated pinned overlay. Inspected host scene configurations consume binary
artifacts and do not directly consume this C owner; no host build, Release
change or new visual/gameplay acceptance is claimed.

Codex resolved the work locally with zero Claude model calls and no account,
provider or model changes. Graph receipts distinguish the normal refresh,
observed hook completion and scoped AST refresh with old-ID retention; this is
not a full-corpus re-extraction. README changes only its aggregate rows. Five
DOCS indexes gain a short entry with every prior byte preserved.

The 85% goal remains active. Continue from this committed checkpoint with the
next ordinary unmatched Game function. Renderer `func_15197148` stays private
and uncredited on its older baseline.
