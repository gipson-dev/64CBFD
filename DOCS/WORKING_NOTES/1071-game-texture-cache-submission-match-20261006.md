# Game Texture Cache Submission Match

Date:2026-10-06. Baseline:`40d4f8ec`
([Note1070](1070-game-oriented-matrix-original-frame-recovery-20261006.md)).
Only `func_15142E24` is installed. No guards, compiler/profile changes,
frame rewriting, caller edits or resolver restoration.

## Direct Match

Retail:102 words/408 bytes, frame0x40, VA15142E24..15142FBC,
ROM1702D4..17046C. Complete semantic C emits every word directly under existing
O2/g3, including return/delay. Linked SHA256:
`ea35a13398e09c276736658a9e7205577c4b8ea7b29aaa7ed297242691ef634d`.

[Driver](https://github.com/gipson-dev/64CBFD-Tools/blob/master/experiments/game_texture_cache_candidates.py):eight
early-return/captured-world/volatile-world shapes across four SDK profiles,
32 final controls without diagnostics. Only default O2/g3 matches102/frame40.
Default O2 without g3:101/96 differences; O1/g3:104/90; O1:104/101.
Captured-world O2/g3:102/52; early-return:102/82; volatile-world:112/68.
No alternate profile is installed.

## Recovered Contract

Eleven inputs: Gfx output pointer,12-byte texture-source record pointer, signed
packed/width/height/value/index words, unsigned kind byte, attachment and sync
pointers, and signed flags. Existing `func_15094FE8` in `generated_C1D70.c`
confirms source/attachment pointer inputs and a32-bit display-list address
argument/return. Explicit casts retain that guest boundary, not a64-bit host ABI.

- Resolve using source, index, arithmetic packed>>16 and low kind byte.
- Compare image/width/height/value/attachment with five live caches. On a hit,
  return output without reading sync or submitting commands.
- On a miss, clear sync only if its byte equals1; no pipe-sync command here.
- Worlds18/13/06/3B/02 or nonzero override byte force flags3 after resolution.
- Submit eleven arguments, including arithmetic packed>>8 and three zeros.
- After submit, cache image and live width/height/value argument homes.
  Preserve the retail attachment **reload-and-same-value-store**, not incoming
  attachment. The volatile accesses retain this observable callback-live store.

Resolver `func_1514306C` stays an unprototyped zero-return placeholder.
Adding a typed four-input definition would change another raw slot. Existing
declaration/definition remain; all forwarded arguments are word-valued,
without a float/default-promotion correction at this boundary.

## Qualification

[Maintained tests](https://github.com/gipson-dev/64CBFD-Tools/blob/master/tests/test_game_texture_cache_match.py):
all ten pre-install tests pass in39.947s, zero skips/errors/failures.

- 2304 paired guest cases:hit/each miss, eight worlds, two override bytes,
  four sync bytes, signed packed fields, three sync aliases, two stack phases,
  callback mutations. All102 instructions in both bodies; full external
  storage/ordered traces and saved GPR/FPR/SP/RA state checked.
- 88 guest-only live argument-home mutations at both helpers/all eleven homes.
- 486 connected cases execute all102 main and50 original resolver words using
  its actual six-entry jump table from exact Game data. Kind truncation, signed
  indices/subindices and unsigned10000000 source threshold checked.
- 6912 actual freestanding32-bit native cases:typed source/attachment helpers,
  signed shifts, globals, sync aliases, full output bytes/fences and mutations;
  pointer/source/Gfx sizes4/12/8. Both native helpers are bounded models.
- Nine actual original call/delay pairs around both complete bodies. Independent
  decode checks argument/private stores and all eleven resulting arguments.
  Return sentinel is synthetic; no whole-caller qualification.
- Ten compiled semantic negatives, eight mapped cases each:wrong gates/shifts/
  flags/sync/cache values and deleting/replacing the same-value store change
  known behavior. Missing mapped storage fails closed.
- Actual padder preserves408 symbol bytes, excludes eight alignment bytes,
  retains all relocations and retargets both calls at offsets2C and138.
- Copied93-function owner retains all92 neighbors/relative relocations/private
  pools and two warnings. Target matches standalone raw object. Resolver and
  oriented placeholders unchanged. Production gate binds source/prototype,
  exact102 words, nine exact neighbors and unchanged10809-row guard digest.

Initial harness failures were not acceptance:IDO rejected a captured-world
declaration after statements (now declared then assigned); unconditional helper
mutation masked one negative (now includes mutated/unmutated cases); native
unsigned-size comparison failed Werror; the initial caller-pair test wrongly
assumed its delay could not change arguments. Corrected tests pass pre-install.

Original submit helper remains a bounded command-write/return model. No full
submit-helper/caller execution, native private-home, hardware/RDP/gameplay
acceptance or host adoption is claimed.

## Production And Progress

US ELF build passes. Audit against Note1069 manifest (unchanged by Note1070):
only this target changes across6059 slots; every address/extent and protected
init/init_data/debugger/game_data byte is unchanged. All720 Game-data owners/
189088 bytes exact; original608-byte private pool preserved. Owner warnings
2->2, zero new warnings. All10809 guards unchanged, canonical SHA256:
`e021c108eef6c84112743955be809d3bdf4ce4e1de0cba474897ed3b0bcabb8a`.

Exact3344/5464 (61.20%), Game2671/4791 (55.75%),2120 different, zero drift.
Conversion unchanged:total5464/6042 (90.43%),85.57% bytes; Game4791/5321
(90.04%),84.89% bytes; Init492/539 (91.28%),92.53% bytes; Debugger181/182
(99.45%),99.19% bytes. All converted Init492/Debugger181 remain exact.
Root README updates only Total/Game aggregate matching rows.

All52 post-link focused tests pass in215.511s, zero skips/errors/failures:
11 texture cache,11 row matrix,13 oriented matrix,12 scaled matrix and5 padder.
Project tools, scoped Python compilation and git whitespace checks pass.
Documentation verification:53 documents/3596 relative links/zero broken links.

## Remaining Work

Ten ignored matrix-storage controls (union-u64/Mtx/f64/flat matrix) do not
improve oriented recovery:142/frameB8/27 private differences or private-exact
142/frameC0/17 wrong-frame differences. Neither is installed. Legitimate
direction68/6C/70 and matrix78..B4 placement remains open.

Next straightforward target:50-word `func_1514306C`, qualified as original
instructions here but still a production placeholder. Recover original switch/
jump-table ordering and pointer/index contract; qualify native/guest/owner/
padder, then install only after full matching gates. Do not infer full rendering
or gameplay acceptance from this cache match.

Ignored receipts:`conker/build/game-texture-cache-test/`,
`conker/build/game-texture-cache/`, matrix scratch:`game-oriented-matrix/`.
No sibling source/build/save/runtime, frozen Release, host adoption or push.
