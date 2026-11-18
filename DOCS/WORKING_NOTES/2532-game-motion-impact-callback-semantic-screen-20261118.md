# Motion and impact callback semantic screen - 2026-11-18

## Status: recovered behavior, original frame, matching unfinished

`func_151B118C` now has two complete, tested C drafts in the tools repository.
Neither is installed in the production source. Both retain the original
**0x98-byte frame** and preserve all **15 owner neighbors** and normalized
pools under the existing O2/g3/MIPS2/o32 compiler profile.

| Stream | Words | Frame | Positional differences including length |
| --- | ---: | ---: | ---: |
| Retail | 187 | 0x98 | 0 |
| `phase-s8` shape draft | 187 | 0x98 | 126 |
| `blend-oldX-ordered` captured-coefficient draft | 184 | 0x98 | 169 |

The three-word length gap in the second draft is not three independent words
to replace. Register allocation, local spills and instruction order remain
different. No guards, added retail instruction ranges, synthetic padding,
profile changes or production modifications are included. **New matching
credit is zero.** Fresh production recount remains **4,542 / 5,514 (82.37%)**,
Game **3,869 / 4,841 (79.92%)**, zero drift and 972 different. **145 additional
matches** are needed for the active 85% goal. Root README remains unchanged.

Source owner `conker/src/game/generated_1DD500.c:178`; original assembly
`conker/asm/1DD500.s:1186`; VA `0x151B118C..0x151B1478`, ROM
`0x1DE63C..0x1DE928`. Frozen baseline consumer
`f98b55974fce955665f29be4ea5af4d1039e71d7`, tools
`b2973805995119659d0dc066ff3ec617db6e1570`.

## Recovered callback and motion fields

The draft interface is `s8 func_151B118C(u8 *effect)`, returning one while the
effect continues and zero after an accepted contact emits its impact. The
actual caller consumes the promoted value as a zero/nonzero removal result.

| Effect offset | Recovered content |
| --- | --- |
| 0x30 | Vertical probe offset |
| 0x34 / 0x38 / 0x3C | Current X / Y / Z |
| 0x40 / 0x44 / 0x48 | Previous/trailing X / Y / Z |
| 0x78 | Complete 36-byte height-query result |
| 0x7C | Nine signed-halfword surface vertices within that result |
| 0x110 / 0x114 / 0x118 | X / Y / Z velocity |
| 0x11C | Vertical acceleration |
| 0x124 / 0x128 / 0x12C / 0x130 | Two extent base/range pairs |
| 0x134 / 0x135 | Probe enable byte / impact selector byte |

Initial Y and both planar velocities are retained before stores. Planar
velocity is damped by `0.25f * D_800BE9A4`; the global is reloaded after the
first velocity store, as in retail. Horizontal displacement uses the mean
of old/new velocity times the timestep. Vertical displacement uses the old
vertical velocity and half the acceleration term; current and trailing
positions advance by those same displacements before trailing interpolation.

The `stage` union shares storage only between consumed initial snapshots,
vertical-integration values and final current-position snapshots. The second
draft also reuses a consumed X capture to retain the interpolation coefficient.
No dummy fields are added to fill the frame.

## Important coefficient and provider boundaries

Retail loads `D_800AA2F0` once and retains it for all three interpolation
components. The 187-word draft reloads it three times; the 184-word draft
captures it once. Both agree in the tested disjoint heap/global fixtures.
The 184-word source is the stronger starting point for recovering retail
access order. Equal word count in the first source is not a reason to prefer
its different load behavior or to install it.

An enabled probe builds `(newX, oldY - offset, newZ)` at its real exposed
SP+0x6C vector. The third helper argument is `newY - offset`. The query is
`func_15046C80(f32 *, u16, f32, HeightResult71820 *)`, with its full result at
effect+0x78. Its current C implementation and matching call declarations are
inspected and frozen; treating this output as just a float is rejected.

On a hit, a second vector at SP+0x60 captures the possibly mutated probe X/Z
and returned height plus 5. The mean extent captures both base/range pairs
before RNG. RNG may mutate the retained probe, extent fields, surface
vertices, selector/header bytes and amplitude coefficients; the already
captured vector/extent stay fixed while the later header/coefficient reads
observe mutations.

The RNG low bit selects one of two calls:

1. `func_151D9B8C(selector, extent * D_800AA2F4, effect[0x5C],
   (s16 *)(effect+0x7C), impact, 100, 0, 1, 0, effect[0xC], effect[1])`.
2. `func_151DAB58(selector, extent * D_800AA2F8, effect[0x5C],
   impact, 1, effect[0xC], effect[1])`.

The first helper's final context is a word; the second's is a byte. Their
return values are unused. Either accepted-hit path returns zero; disabled
and rejected probes return one.

## Fresh reusable evidence

Seven maintained files use the `game_motion_impact_151b118c` stem under
`tools/experiments/` and `tools/tests/`. The manifest pins both complete
bodies, declarations, raw hashes and relocation identities. The focused
four-test suite passes independently in the primary checkout and a private
sibling overlay: **98.642s / 83.254s**,
with **314 / 314**
observed imported tool files fingerprinted against frozen or task inputs.

- All three streams pass **360 guest cases each**. Coverage is **187/187**
  retail words, **187/187** shape-draft words and **184/184** captured-draft
  words. Checks compare all public bytes, ordered calls/all arguments,
  exposed vectors and surface vertices, returned value, saved GPRs/FPRs,
  restored SP and RA. Calls poison volatile registers and outgoing homes.
- Native32 runs each draft at **O0/O2/O3**, **360 cases per run**, with strict
  aliasing, SSE single precision, no fast math and UBSan traps. All six pass.
  Eight effective negative variants reject changed damping, inverted enable,
  shifted height result, wrong impact height, wrong RNG bit, swapped context,
  recaptured probe after RNG and wrong return. Every negative exits through
  the controlled failure path; an arbitrary crash is not a passing control.
- The actual table word at **ROM0x22E7B8 / VA0x80089CF8**, index **16** of
  `D_80089CB8`, equals this callback. The complete 42-word table and original
  **15-word caller window**, VA `0x1513D038..0x1513D074`, are verified in ROM
  and frozen ELF. **720 connected cases per stream** test both incoming
  removal states. They exercise 14 caller words; the zero-selector branch's
  alternate delay instruction is not exercised by nonzero index16. The
  callback receives the real effect pointer, and its zero result sets removal.
- The source screen compiles the complete owner for both drafts, checking
  raw bytes/relocations, original frame and all 15 unchanged compact neighbors
  and pools. `make tools-check` and production match-progress both pass.

One private native fixture initially formed negative floating zero where the
Python provider formed positive zero after integer negation. Correcting that
fixture operation made its byte pattern agree; the candidate source did not
change to bypass the failure.

## Limits and remaining adoption gates

These are bounded finite-value, nonfaulting fixtures with effect/private
stack/global regions disjoint. They do not prove arbitrary aliases, all IEEE
NaN payloads, FP trap/FCSR ordering, instruction-fault prefixes or equality of
every unexposed private stack byte. Query/RNG/emission remain modeled
providers. Only the selected caller window is connected, not every mode of
the full 195-word parent or a hardware/gameplay run. No full-function
symbolic relation or normalization is claimed.

The freeze holds **1,652 inputs**, 1,643 links to immutable snapshots and nine
copies, with zero links to live inputs. Every frozen live input is unchanged.
The production ELF remains
`d3caaa0bd472f25769a9ea5f9de1fcd23cdd35cf5c25aa1ae78344fc0159fe4b`.
The private overlay uses 339 exact sibling files, 358 fingerprinted primary
fallbacks and seven task files. The actual sibling's 2,434 dirty paths and
343 previously scoped dependency hashes are preserved. No host Release,
saves, runtime source or build is changed.

Native Graphify refresh and scoped AST merging are recorded separately;
the AST merge retains all prior IDs and explicitly links the screen to its
production placeholder. This is not a full-corpus extraction. Bank tools
first, then this note/indexes and the consumer pin. No push is requested.
No Claude call is needed for this callback's routine qualification.

## Next work toward 85 percent

1. Resume from `blend-oldX-ordered`, keeping the 187-word shape draft as a
   comparison. Recover the original 187 words and same frame with the single
   coefficient load, old-velocity/acceleration spill lifetimes and extent
   evaluation order. Forty retained-scalar/lifetime controls in the current
   packet did not recover the full stream; volatile fields change the frame
   to 0x90 and are rejected.
2. Prove the complete FP/access/control-flow/private-byte relation before
   deriving any narrowly justified guard transform. No count-only patching.
3. Qualify both object padders/rebases and callers, independently predict the
   complete image, run actual Make and a strict production/protected-data
   audit, installed tests and actual-ELF recount before adoption or credit.
4. The separate `func_151B0B88` draft remains 389/385 and uninstalled. Further
   countdown/continuation/profile probes did not establish an exact body.
   One 385-word control had the wrong frame/control flow and was rejected.
   Preserve its earlier four-test semantic screen and Note2531 handoff.

The 85% goal remains active; this commit preserves measured recovery and
reusable checks without changing accepted matching totals.
