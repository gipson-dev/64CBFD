# Game Record Ring Renderer Recovery

Date: 2026-10-08

## Result

Continue the complete next target from [Note 1138](1138-game-record-ring-shaping-conversion-20261008.md)
using the [focused workflow](../AGENT_WORKFLOW.md). Recover retained
`func_151D80C4`, VA 0x151D80C4..0x151D8718, ROM 0x205574..0x205BC8:
**405 words / 1,620 bytes / retail frame 0xD0**. Preserve the
[original function](../../conker/asm/nonmatchings/generated_204660/func_151D80C4.s)
and [full slice](../../conker/asm/204660.s).

The complete semantic candidate remains **uninstalled**. Natural O2/g3 C
emits 405 words but frame 0xE0 and 319 raw differences. This is recovery and
qualification progress, not a conversion or byte match. No production
source, compiler profile, layout, word guard, progress row or root README
change. Nine focused tests pass in **63.057s**, with no skips.

The unchanged installed ELF's complete SHA-256 is
`f240ca73721dfd7a24c0a85fd5697d45ea1ebc724a11ebd76d965e6b3cd86e99`.
Fresh verification preserves all **6,058 linked bodies, addresses, extents**
and every protected section/data byte. Source, assembly, Makefile, progress
and all **11,275 guards** retain their recorded entry fingerprints.
The installed target still uses its original assembly and is byte-exact.

Totals remain converted **5,481 / Game 4,808**, exact **3,392 / Game 2,719**,
zero drift, 2,089 different. Root README already has those aggregate rows;
do not add a function narrative or grant conversion credit.

## Recovered Contract

The routine emits a textured backward-ring ribbon, with four-vertex loads
and two triangles per segment:

- Signed state byte +0x2C below two returns the input Gfx cursor without
  reading either payload pointer or allocating. Active code captures +0x94
  ring storage and +0x98 payload before the allocator and setup callbacks.
- `func_151D5D60(owner+0x84, (s16)view, count*32+160, &cursor, NULL)`
  supplies an escaped vertex cursor. Count is unsigned +0x25. Null output
  returns without graphics setup, record/global-width reads or vertices.
- Setup uses the recovered eleven-argument texture interface, geometry masks
  0x200005/0x1F0600, combiner kind 0x4C and blend/other-mode globals.
  One private sync byte begins at one; returned Gfx cursors chain through all
  four calls. The target candidate uses the existing SDK graphics macros.
- Flag two seeds the first pair from owner XYZ, zero alpha and captured
  payload phase. Otherwise seed from the previous ring record. Signed
  current +0x2E decrements with unsigned-count wrapping. Records are 28 bytes:
  raw XYZ words, alpha byte +0x14, phase float +0x18.
- Widths are `D_800DD1E8[(s16)view]*5.5f` and
  `D_800DD1D8[(s16)view]*5.5f`. Vertex pairs use X +/- width and Z -/+ width,
  signed truncation followed by low-half stores, phase S, T 0x800/zero,
  RGB 255 and flag zero. Alpha is `(recordAlpha*factor)>>8`; factor is 255
  or `(signed owner halfword +0x1C * 12)&255` under flag eight. Preserve
  retail's 255*255 -> 254 alpha result.
- Each segment emits words 0x01004008, 0x05000204 and 0x05020604. A phase
  decrease makes a real 32-byte memcpy of the last pair, then subtracts
  0x8000 from the **old pair's** S coordinates while advancing through the
  two new copied vertices. The copied pair seeds the next segment unchanged.
- After every segment, even the final one, decrement/wrap the record cursor
  and load the next XYZ, alpha and phase plus the previous phase. Only then
  exit against the live signed goal +0x2D. Captured storage, captured width
  and captured opacity survive memcpy; goal and wrap count remain live.

Do not introduce null/bounds/cycle policy or repair nonterminating retail
domains. Negative-view/count-zero guest fixtures are deliberately mapped;
they are not proof that an arbitrary caller has valid negative-index storage.

## Measurements

The [candidate driver](https://github.com/gipson-dev/64CBFD-Tools/blob/master/experiments/game_record_ring_renderer_candidates.py)
retains **14 complete source forms**: typed/byte/float storage, reused alpha
and phase lifetimes, factored 28-byte stride and a success-branch form.
Four normal profiles are screened for the natural body. No new pools or
isolated compiler diagnostics.

| Full Source / Profile | Words | Frame | Raw Differences |
| --- | ---: | ---: | ---: |
| Natural O2/g3 | 405 | 0xE0 | 319 |
| Natural O2 | 405 | 0xE0 | 336 |
| Natural O1/g3 or O1 | 491 | 0xA0 | 484 |
| Byte stride, reused alpha/phase | 405 | 0xD8 | 316 |
| Byte stride, reversed factor branch | 405 | 0xD8 | 305 |
| Factored stride | 403 | 0xD8 | 322 |
| Factored stride, byte alpha locals | 403 | 0xD0 | 319 |
| Float stride | 410 | 0xD8 | 348 |

No form simultaneously closes the retail extent, frame and register/stack
schedule. The natural candidate spills factor around memcpy; retail keeps
it in GP FP. Its struct indexing also retains a stride constant in S5,
shifting the long-lived graphics command allocation. Those are measured
shape differences; the original declaration/lifetime solution remains open.
Do not replace these with a broad 319-word normalization batch.

## Fresh Qualification

The [focused suite](https://github.com/gipson-dev/64CBFD-Tools/blob/master/tests/test_game_record_ring_renderer_recovery.py)
reuses the existing IDO, copied-owner, MIPS GP/FP and native32 helpers:

- **988 guest cases** compare raw candidate and complete retail code with
  an independent pair/command reference, full public memory, ordered output
  stores, callback arguments/results and saved GP/FP lifetimes. Cover both
  seed modes, opacity modes/boundaries, three phase patterns, six view bit
  patterns, two SP phases, all state bytes and eleven mutations plus baseline.
  The ordinary sweep reaches 393 candidate / 392 retail words; this is not
  complete instruction or hardware coverage.
- **512 cursor/count cases plus three lazy layouts** cover all 256 current
  and count bytes, mapped count-zero record -1, inactive-pointer laziness
  and null-allocation record-read laziness.
- **1,086 native32 cases** run the full C through a volatile typed call.
  An independent offset/vertex/command reference checks callback arguments,
  return cursor and every byte of a 65,536-byte arena. Cover all state,
  current and count bytes, 256 flag patterns, opacity boundaries, four views,
  eleven mutations plus baseline and signed-view allocation-failure bounds.
  Exclude invalid float-to-integer casts.
- **22 missing-byte gates / 44 executions** fail closed at required reads
  or vertex stores, including five lookahead reads after the final segment.
  Do not claim equal raw/retail fault prefixes or portable C fault semantics.
- **14 complete source forms, four profiles and eight effective compiled
  negatives** pass. Negatives independently expose signed-state/current,
  alpha scaling, width, join direction, old-pair selection, captured storage
  and request-size defects. No timeout or unsupported-opcode substitute.
  Other profiles qualify complete ordinary memory/results/calls, not retail
  command-store order; only the selected O2/g3 form claims that order.
- **256 connected cases / 512 executions** run the complete 52-word
  original `func_15147C4C` and actual 52-word `func_151D5D60` against both
  bodies. Verify render-table `D_8008A2A4` entry **16**, ROM 0x22EDA4;
  signed-view forwarding, all nine transform arguments, flag-0x20 context,
  null/existing/new allocations and both framebuffer halves. All backend
  words and 47/52 caller words execute; alternate dispatch/release branches
  remain unqualified. Deep allocation, transform, graphics setup and memcpy
  are bounded hooks, not complete-chain or hardware acceptance.
- Copied owners preserve **22 neighbors**, relative relocations, normalized
  pools and all four existing diagnostics. Postprocess retained assembly
  before comparison. Isolated/copied target bytes agree. The actual padder
  accepts its 1,620-byte extent with no slot padding and no new guards;
  acceptance of size does not qualify its frame or remaining differences.
  Sixteen relocation type/symbol uses are preserved; positions/order differ
  and require fitting plus independent rebases before installation.

Correct only fixture issues encountered: the first vertex address overlapped
the oracle stack; separate those regions. Use the existing copied-owner
signature and assembly postprocessing. Match memcpy mutation timing to its
completed copy. Compare relocation multisets rather than parser insertion
order. Fix native fixture declarations/braces without relaxing compiler
warnings. A mistyped shared-test module is corrected before the passing run.
None of these is a production-code repair or negative-control witness.

Both the original render dispatcher and `func_1513F4E4` combiner remain
linked zero-return placeholders. Executing original dispatcher words with
bounded setup hooks does not restore those bodies or qualify a real complete
render chain. No emulator, gameplay, hardware FCSR/traps or host integration.

Fresh shared checks: **14 matcher/padder/repository-setup tests**, project
checks in both tools checkouts and CLI help. No shared production tool was
changed; earlier complete neighbor suites remain historical, not fresh runs.
Syntax/mirror checks pass for both new files. Scoped documentation checks
pass **125 documents / 4,070 relative links / zero broken links**; remote
publication is not verified or authorized by these local checks.

## Baseline And Banking

Entry parent `86f2fb05b8a88dc269e8569d74b98e1782558bab`, mounted tools
`5c9e50bfb3d84c9a2ac9c9435be2944b2134049e`: both clean. Preserve older
standalone HEAD `ddbdd16b53ce60b054fb6e11bf0649a41f48375a` and its exact
pre-existing dirty status. Mirror only the two new reviewed files after
proving neither target exists; no overwrite/reset/stash or duplicate commit.

Per **"Keep commited"**, bank mounted tools first:
`a22175b6c672a0275fa1a6ac6f77b2df3ba4a17a`.
The parent documentation commit records that exact gitlink. No push.
Receipts remain ignored under `conker/build/game-record-ring-renderer-test/`
and `conker/build/game-record-ring-renderer/`; no ROM or local artifact added.

Graph query preceded investigation. Fresh `graphify update .` exits one:
16,820 nodes versus retained 38,609, refusing reduced-corpus overwrite;
preserve 19,398 nodes from 2,972 still-existing excluded files. No force,
upgrade, installation, changed ignore policy or full graph-repair claim.
One Codex writer, zero Claude calls; OGL/Release and real saves untouched.

## Resume This Target

1. Fit **this same complete function's** frame 0xD0 and 405-word extent,
   escaped cursor SP+0x8C, sync SP+0xA7, captured buffer SP+0xA8, XYZ blocks
   SP+0xB4/+0xC0, S0..S7/FP and F20/F22 lifetimes. Start with meaningful
   stride/factor/alpha lifetimes, not dead locals or inserted instructions.
2. Expand qualification for the fitted body: independent symbol rebases,
   missing-word fault prefixes, relevant input/output aliases and any proposed
   closed schedule. Keep bounded helper evidence distinct from actual callee
   restoration and the still-placeholder linked dispatcher/combiner.
3. Only then install, rebuild, audit every body/data/guard/progress row,
   refresh aggregate README values, and bank tools before source/exact pin.
   The wider Game goal stays active; graph repair and hardware/gameplay open.

```sh
python3 -m tools.experiments.game_record_ring_renderer_candidates
python3 -m tools.experiments.game_record_ring_renderer_candidates --profiles
python3 -m unittest tools.tests.test_game_record_ring_renderer_recovery -v
```
