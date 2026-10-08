# Game Texture Resolver Match And Table Binding

Date:2026-10-06. Baseline:`ff2b59b2`
([Note1071](1071-game-texture-cache-submission-match-20261006.md)).
Restore only `func_1514306C`; caller types now describe its real four-input
contract. No other production routine, profile, header or padder logic changed.

## Recovered Routine

Retail:50 words/200 bytes, no stack frame, VA1514306C..15143134,
ROM17051C..1705E4. Semantic C emits all50 instructions directly under existing
O2/g3. The original first-word load and branch-delay index copy are recovered
by assigning index from source->unk0, then spelling the dereference path with
source->unk0 again. The compiler emits a single actual source-word read.
A separate word local or using only index emits49 words and loses that copy.

[Compiler driver](https://github.com/gipson-dev/64CBFD-Tools/blob/master/experiments/game_texture_resolver_candidates.py):
18 source shapes across four SDK profiles,72 controls without diagnostics.
Exactly two match:plain index/repeated-source and condition-assignment/repeated-
source under O2/g3. Early returns, local/inline words, alternate threshold order,
argument reuse, else-only assignment and pointer-local forms are retained controls.
No alternate compiler profile is installed.

| Kind Low Byte | Result |
| --- | --- |
|1|Zero, without reading source or lookup globals|
|2|D_80091564[index]|
|3|D_80091514|
|4|D_800915B0|
|5|Raw index word|
|6|source first word; if unsigned >=10000000, indexed word through that pointer|
|Other|First word of12-byte D_80090B60[index], then subindex lookup through it|

Signed indices/subindices retain retail word-address arithmetic; no invented
bounds/null/threshold fallback. Four-input prototype uses GameTextureSource*,
s32 index/subindex and u8 kind. Source metadata/attachments are not modified.
Guest high kind bits truncate before switch; its original full argument word
is stored at caller home SP+C. The original102-word cache caller stays exact.

## Jump-Table Ownership

Retail six-entry table at800A562C:
151430B8,151430C0,151430AC,151430A0,151430D4,151430DC.
Standalone compiler table contains exactly these24 bytes plus eight alignment
zeros. Its original asset owner is retained, not replaced with compact data.
Owner:`build/assets/249F40.bin.o(.data)`, ROM249F40, VA800A5480..800A56D0.

Copied owner previously had600 payload bytes plus eight alignment zeros.
New compact table begins at offset258/600, replacing alignment zeros and
extending the pool to624 bytes. All prior600 payload bytes and their table
addends stay unchanged; the new six targets have the exact original relative
function offsets. All92 other raw functions/relative relocations and two
existing warnings are preserved.

Owner's existing pool anchor800A5218 would place the new reference at800A5470,
not retail800A562C. Two existing-schema expected-word/relocation guards bind
only this function's HI16/LO16 pair at offsets20/28 to jtbl_800A562C_game:
HI instruction stays3C010000; compact LO8C2F0258 becomes8C2F0000 with the
explicit original table symbol. No branch, register, stack, return, insert/omit
or scheduling rewrite. Original10809 rows remain unchanged; two rows appended.

## Qualification

[Resolver tests](https://github.com/gipson-dev/64CBFD-Tools/blob/master/tests/test_game_texture_resolver_match.py) and
[pool tests](https://github.com/gipson-dev/64CBFD-Tools/blob/master/tests/test_game_owner_pool.py):all12 pre-install checks
pass in53.365s, zero skips/errors/failures. Ten resolver tests include a further
post-link production gate; three independent pool tests reject incorrect targets.

- 13824 paired guest cases:all256 low kinds with high bits, signed indices/
  subindices -2/0/2, threshold0FFFFFFF/10000000/80050000 and two stack phases.
  All50 words in both bodies, exact whole memory, ordered reads/writes and
  GPR/FPR/SP/RA saved state. Only kind home is written.
- 19200 actual freestanding32-bit native typed-caller cases:all kinds, valid
  index/subindex ranges, low literal words and real high-address stack pointers.
  All source/record/table/global bytes checked unchanged. Negative indices and
  exact threshold addresses are guest-only; no undefined native array indexing.
- 486 connected cases execute all102 original cache-caller and50 resolver
  instructions in both bodies, all cache hit/miss paths, flags/sync and signed
  fields. Full external storage and ordered traces agree. Submit remains a
  bounded command-write/return helper, not original rendering execution.
- Ten compiled semantic negatives,24 valid mapped cases each, change known
  outputs/data reads:placeholder, full-width kind, signed/shifted threshold,
  wrong null/global/table/record/subindex and passthrough results.
- Missing required source/table/global/pointed storage fails closed. Unused
  source is not read on other kinds; no new null validation is claimed.
- Standalone actual padder retains200 symbol bytes, excludes eight text
  alignment bytes and retargets all five relocation pairs under alternate
  addresses, including carry boundaries.
- Copied owner is passed through actual assembly post-processing before full
  padding. Both guards preserve original table ownership; target relinks to
  all50 retail words and alternate carries. Wrong expected word/relocation
  fails with stale-guard error before emission.

[Pool comparator](https://github.com/gipson-dev/64CBFD-Tools/blob/master/tests/game_owner_pool.py) normalizes only actual
R_MIPS_32 text relocations to function name/relative offset. Every other pool
byte remains exact. This qualifies neighboring copied-owner tests when their
earlier C functions change packed addresses of the new switch targets. Three
independent assembler fixtures detect changed relative targets/literal bytes,
missing relocations, unsupported relocation types and unowned targets.
Neighbor guard checks retain the original10809-row digest and permit only the
exact two new table-binding rows, not an arbitrary additional suffix.

Initial pre-install failures were fixture defects, not acceptance:the pool
fixture used an unsupported .rodata shorthand; full padding needs the actual
assembly post-processing step; wrong-subindex negative reused the source-word-
overwritten index and read unmapped storage; connected caller only exercised
image miss/hit, leaving three annulled delay words unseen. Corrected fixtures
use a mapped subindex+1 negative and all five cache-miss gates; all12 pass.

## Production Receipt

US ELF rebuild passes. All6059-slot audit against Note1071:only this resolver
changes; every address/extent and protected init/init_data/debugger/game_data
byte unchanged. All720 Game-data owners/189088 bytes exact. Existing owner
warnings2->2, zero new warnings. Caller102 words remain exact.
Target SHA256:`42e78e136863285d8b9113240dabac8b6a5bce1f773011f1ec7f93d0bac1ebd6`.
Guard10809-row prefix unchanged;10811 total including two table bindings.
Canonical full SHA256:
`9e8f11db1c07370f470888d62e63b3b8ced846afa67a1db81ca94f0c44e601da`.

Fresh progress:3345/5464 exact (61.22%), Game2672/4791 (55.77%),2119
different, zero drift. Converted counts/bytes unchanged:total5464/6042 (90.43%),
85.57% bytes; Game4791/5321 (90.04%),84.89%; Init492/539 (91.28%),92.53%;
Debugger181/182 (99.45%),99.19%. All converted Init492/Debugger181 exact.
Root README changes only Total/Game aggregate matching rows.

All81 focused post-link tests pass in315.971s, zero skips/errors/failures:
10 resolver,3 pool,11 cache,11 row matrix,13 oriented matrix,12 scaled matrix,
8 actor classifier,8 context classifier and5 padder. This also requalifies
both existing original classifier tables after the compact-pool extension.
Project tools, scoped Python compilation and git whitespace checks pass.
Documentation verification:54 documents/3611 relative links/zero broken links.

## Next Work

Next chronological candidate:98-word `func_15143134`, frame78, currently exact
original assembly. Recover its point/output/Mtx input ABI, zero/null gates,
live diagnostic status writes and original guMtxL2F/transform-helper boundaries.
Qualify helpers within their actual contracts before installing C.
The larger `func_151432BC` placeholder follows it and contains FCSR-sensitive
float conversion paths; do not treat its commented approximation as recovered.

Oriented `func_15142600` remains uninstalled with27 private offsets differing;
this resolver match does not resolve its frame/layout work.
Ignored receipts:`conker/build/game-texture-resolver/` and
`conker/build/game-texture-resolver-test/`.
No sibling source/build/save/runtime, frozen Release, host adoption, full
submit/render/gameplay acceptance or push.
