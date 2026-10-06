# Game Position Projection Investigation

Date: 2026-10-06
Baseline: `e1298167` ([Note 1057](1057-game-actor-event-dispatch-match-20261006.md)).
Continue the Game matching goal; this is an investigation, not an installation.

## Retail Contract And ABI

`func_1514182C`: **63 words /252 bytes**, frame **0x80**, VA
**0x1514182C..0x15141928**, ROM **0x16ECDC..0x16EDD8**. Actor and origin
pointers survive both helper calls in S0/S1. The local4x4 matrix begins at
SP+0x34. Rotation helper `func_150A8050` receives angleX, zero, angleZ.
Origin coordinates then populate matrix row3 at SP+0x64/0x68/0x6C. These are
translation fields, not three unused locals next to a shorter matrix.

`func_150A7960` transforms (zero,height,zero), writing actor+0x34/0x38/0x3C.
The third argument forwards **float bits**, not a numerically converted integer.
Review the current false integer-height prototype in
[`game_16DC80.c`](../../conker/src/game_16DC80.c) and its `func_15141928`
caller together. The latter's source load at actor+0x170 should preserve float
bits when adapting the prototype; do not introduce an integer-to-float conversion.

After the coordinate helper, retail reads the three transformed positions and
all three live origin values **before the first output store**. For each axis:
`position + ((position - liveOrigin) * scale) * 500.0f`, in that multiplication
order. Results go to actor+0x40/0x44/0x48. F0 remains transformed X in the
retail instructions. That observable guest-register result does not by itself
prove that the original C return type was float rather than void; the one known
caller ignores it. Return ABI still needs an explicit decision and qualification.

The common SDK `struct210` is not a suitable float-output view: its0x40/0x44
fields are signed16-bit and it has no named0x48 field. Do not extend or rewrite
that shared type merely for this routine. Owner-local or byte-based views are
the appropriate current investigation boundary.

## Compiler Controls

Ignored files under `conker/build/game-actor-event-dispatch-test/`:

- `next-position.py`:16 matrix-representation/height/profile controls. Corrected
  O2/g3 float-height baseline: **63 words/frame0x80/31 differences**; integer
  height: **66/frame0x80/54**. Array/flat variants have the same outcome.
- `next-position-layouts.py`:16 matrix-layout/parallel-product/return-field
  controls. Best fitting form remains63/frame0x80/31. Explicit parallel
  products emit64/frame0x88/29; fewer differences do not mean a fitting body.
- `next-position-types.py`:12 actor/origin/matrix-type controls, all63/0x80/31.
  Initial SDK-field experiment fails on absent `unk48`;0x40/0x44 are also wrong
  scalar types. Correct only the ignored experiment with float byte casts for
  outputs, retaining existing shared types. All12 corrected controls compile.
- `next-position-cache.py`:eight origin-cache/order/const controls. Caching
  all origin values before outputs gives **67 words/frame0x88/47 differences**.
- `next-position-return.py`:eight float/void-return controls. Void parallel
  products give **63 words/frame0x88/16 differences**, but the frame is wrong
  and the original return type is not established. Not a qualified replacement.

**60 completed control compilations**, empty diagnostics after the explicit
scratch corrections. Families contain overlapping forms, not60 unique sources.
The earlier incorrect-frame-mask receipt remains preserved as documented in
Note1057; no measurement or acceptance relies on that mask. Sources, objects,
ELFs and five family measurement JSON files remain in `next-position/`.
No production source, prototype, compiler profile, shared header or guard edit.

## Bounded Guest Probe

`next-position-probe.py` compares actual compiled candidates with retail.
Rotation is a **bounded identity provider**, not the real angle/rotation routine.
The coordinate helper executes connected retail instructions:58 words mapped,
**40 reached** per body. Compare full external storage, normalized helper calls/
matrix contents, F0, saved GPR/FPR/SP/RA and two SP phases.

**126 cases** per candidate:18 disjoint-origin cases and108 live-origin alias
cases, three heights, three scales and two phases. The fitting63-word baseline
agrees in all18 disjoint cases, but **24/108 alias cases disagree**. Example:
origin=actor+0x38, height=-1, scale=0.25, SP phase0:

```text
baseline output: (3.0, -247.0, 255.0)
retail output:   (3.0, -247.0,   5.0)
```

The baseline reads an origin component after an earlier output overwrites it.
This is a semantic difference, not merely register allocation or stack placement.
Do not normalize the31 words wholesale or install this source as a recovery.

The cached-origin `cache-100` candidate agrees in **all126 cases**, including
every tested alias. **67/67 candidate and63/63 retail owner words reached**;
the baseline also reaches63/63. Its67-word body and0x88 frame still do not fit
retail. Receipts: `probe-position-00-o2g3.json`, `probe-cache-100.json`, plus the
retained initial `probe.json`. No independent arithmetic oracle, actual native-C
fixture, real rotation-helper, special-float/FCSR or gameplay qualification yet.

## Next Steps

1. Recover an alias-preserving source shape that reads origin components before
   output stores, without the four-word/eight-frame-byte growth. Preserve the
   retail two-stage multiplication; factoring scale*500 changes rounding.
2. Resolve the private matrix base0x34 versus candidate0x40, saved-register
   lifetimes, and float/void return evidence. Only derive closed compiler-layout
   normalization after semantic and complete-slot/frame gates hold.
3. Promote the selected screen and probe to maintained tools/tests. Add actual
   32-bit native C, independent expectations, live helper mutations, more alias/
   arithmetic boundaries, negatives, and the connected retail caller.
4. Adapt the local prototype and caller together, rebuild, audit all6059 slots/
   protected sections/720 data owners, update aggregate status, then commit.

## Banked State

`e1298167` remains the code baseline: dispatch55 words directly exact/no guards,
28 focused tests green,6059-slot audit changing only that function, owner
warnings0->0. This investigation changes **no compiled slot or matching count**.
Exact total3334/5464 (61.02%), Game2661/4791 (55.54%),2130 different, zero drift;
converted counts/bytes and10760 guards unchanged. All experiment/probe sessions
terminated; no game runtime, sibling source/build/save/frozen Release or push
change. Continue from the cached-origin versus footprint boundary above.

Checkpoint audit: all6059 slot fingerprints and10760 guard records unchanged
from the dispatch receipt; owner source, shared headers and Makefile match
`e1298167`. **40 documents /3440 relative links /zero broken**; diff checks pass.
