# Game Actor Burst Consumer Guarded Match

Verified locally: 2026-10-14. This installs the complete consumer from
[Note 1354](1354-game-actor-burst-consumer-float-lifetimes-and-angle-conversions-20261014.md).
Retail matching is not host gameplay or complete hardware acceptance. Keep the
wider Game goal active and preserve frozen host Release and unrelated work.

## Target And Baseline

- `func_151A6F00`, owner `conker/src/game/generated_1D43B0.c`.
- VA `0x151A6F00..0x151A73EC`, ROM `0x1D43B0..0x1D489C`.
- Complete315-word /1,260-byte slot, frame `0x168`, existing O2/g3/MIPS2 profile.
- Starting consumer `a441a0ee`, tools `0e244d6`; both active trees initially clean.
- New tools `eb93e2eff87ddbe25d1a7365af63b37887d5f628`, committed first.
- Before ELF `50b064c6d7af59a7a78eeece1a2b3c8e32b2886b1695097fd6b43044f2b092ee`.
- Installed ELF `b2c092d4e31f04377ebc5c05314803c8aed6e75233b93b58e30447187139c499`.

Retain validated before snapshots in
`conker/build/game-actor-burst-consumer-match-test/`. The original assembly,
caller, layout, Makefile and complete conversion CSV remain unchanged.

## Installed Body

Replace only the consumer's zero-return placeholder, adding its local packet
and private aggregate types and narrow helper declarations. The public0x5C
packet matches the existing producer's member names, widths, order and byte
arguments. The caller source stays byte-identical and retains its67-word direct
match. Do not refactor unrelated structures or broaden the header dependency.

Keep the signed old-value count loop, all four kind branches plus default,
unsigned remainder-based angles, spherical position, scale and coefficient
samples, both allocation failure paths, real payload copy and animation rate
reload. Keep all four private homes: descriptor E8, payload D4, scale D0 and
animation8C. Preserve unwritten bytes, especially default-path velocity and
private aggregate holes. Native checks inspect initialized fields only.

The semantic C emits313 words. The existing guard machinery, without a new
core normalizer, restores the two independent scheduling sites identified in
Note1354. The actual linked result matches every315 retail word.

## Ten Guarded Rows

| Compact Offset | Purpose |
| --- | --- |
| 144 | Empty-count branch distance |
| 25C/264/26C/274 | Kind dispatch/default branch distances |
| 2C0/2C4 | Move kind0 Z store before branch and insert its idle delay word |
| 304/308 | Move kind1 Z store before branch and insert its idle delay word |
| 494 | Loop-back branch distance |

All ten rows declare exact expected opcodes and empty relocation ownership.
Two rows insert a NOP through the existing `insert_after` field. The other six
rows rebase affected internal branch distances. There is no broad instruction
transplant, inline assembly, invented volatile field, dummy local or profile
change. Every helper/data relocation retains its symbol/type and is emitted at
the correct moved offset by both existing padders.

The guard file keeps every previous byte, including its mixed historical line
endings, and appends exactly1,462 bytes for these ten rows. Source/ELF/guard
corruption controls require raw bytes as well as parsed/text identity.

## Qualified Gates

The pre-install recovery/first eight match/protected run passes **23 checks in
68.000s**. After installation and audit repairs, the complete recovery, match,
producer and protected-text run passes **40 checks in124.436s**.

- **960 raw-C guest domains** and **288 saved-float call domains** retain the
  prior complete modeled return states and F20..F31 lifetime proof.
- **288 actual guarded guest domains** reach all315 words, including both
  restored NOPs and the real division BREAK paths. Independent initialized-field
  reference and complete modeled return states agree.
- **168 fired alias prefixes** cover public input, created-object storage,
  a global coefficient and four private input homes. Stop at the actual first
  factory boundary; private aliases are guest-only, not portable-C claims.
- **4,080 fired root-access pairs across36 domains** preserve every modeled
  prefix state, actual instruction PC and modeled branch-delay state. Connected
  memcpy accesses are excluded. Raw313-word controls have wrong PC/BD at both
  moved Z-store sites, demonstrating why return-state agreement was insufficient.
- **Three independent carry links** compare independently assembled retail
  with both real padded objects. Rebase both data symbols independently across
  HI/LO carries and preserve all external JALs and internal branch distances.
- **Six neighbors**, their complete words, relative relocations and normalized
  pools remain fixed. Both complete owner padders and both isolated padders
  preserve the same315-word target with exact1,260-byte symbol extent.
- **40 stale-guard rejections** cover each expected word and relocation field
  through both padders. Whole-image, source, guard and metadata controls remain
  effective; eight current symbol/string mutations and one bad baseline fail.
- **24 connected producer/dispatcher/table0 cases** execute the actual guarded
  provider and original11-word memcpy. All14 producer holes can be unmapped in
  mode1; retain three allocations, six integer RNG calls and18 float samples.
- The full14-check producer regression remains green, including its10,800 raw
  guest cases,108 aliases,1,404 root cuts and20,736 native32 cases per profile.
  The consumer's108 native32 O2/O0 cases,18 signed prefixes, four guest BREAK
  prefixes and32 raw direction cases also remain green.

RNG, trig, random-float and allocation systems remain bounded hooks. Complete
all-input/native alias behavior, hardware FCSR/rounding and hardware EPC/BD are
not claimed. Mode2 raw NaNs are copied, not arithmetically qualified.

## Closed Linked Image

The complete3,261,160-byte ELF accounts for exactly **1,048 changed bytes**:

| Region | Changed Bytes |
| --- | --- |
| Target instructions | 988 |
| Target size,12 ->1,260 | 2 |
| Two adjacent symbol record swaps | 27 |
| Their exact string serialization | 31 |

The two asserted groups are `D_80090CD4,D_800A5F3C` and
`D_800A8DC0,func_10019CFC`, each reversed. Before definitions, record adjacency,
string adjacency and original spelling are checked before applying these exact
permutations to the expected image. Every other definition/address/extent and
ELF byte stays fixed; there is no broad metadata exclusion.

Protected data remains exact:189,088 bytes across720 owners, zero differing
bytes/owners. The complete conversion CSV retains SHA-256
`14d100143c0654609b3cd7d97798dbeccd52551a77ad6b4ff1f826acde91482b`.

The initial whole-image gate correctly reports the58 serialization bytes not
yet declared. The first expanded installed run then fails a stale protected
guard pin and a producer byte-corruption control delegated through a text-only
guard check. Add explicit raw-byte identity, keep the old guard prefix intact,
and update both verified fixture pins. Repaired controls pass3 checks6.077s;
the final40-check run is the acceptance receipt, not either failed attempt.

Archive protected text baseline/ELF/guard snapshots before advancing only the
verified ELF and guard pins. All semantic/corruption checks stay enabled. The
build succeeds; touching the shared guard manifest rebuilds other objects, but
the closed image proves their final bytes/data remain unchanged.

## Banking And Next Work

Fresh matching progress: Game2,833/4,823 (58.74%), total3,506/5,496 (63.79%),
different1,990, drift0. Init492/492 and Debugger181/181 remain exact. The root
README changes only its two aggregate matching rows.

The older standalone mirror remains at ddbdd16. Verify its461 starting paths
and the four affected modules against the prior active commit before copying.
Four owned modules are updated and one new match test is added; preserve all457
other fingerprints and its independent history. Both copies pass project smoke
checks and Windows byte-compilation. No push, dependency install or host Release
build/launch is performed.

Next recover `func_151A743C` in this same owner: VA0x151A743C..0x151A7610,
ROM0x1D48EC..0x1D4AC0,117 words/frame0x48. Its production body still returns
zero. Preserve the now-qualified consumer and all six owner neighbors while
recovering that routine; keep the wider Game goal active.

```sh
python3 -m unittest tools.tests.test_game_actor_burst_consumer_match -v
python3 -m unittest tools.tests.test_game_actor_burst_consumer_recovery -v
python3 -m unittest tools.tests.test_game_actor_burst_packet_match -v
```

## Post-Bank Verification

Consumer `e4b8e39a` banks the installation. Seven fresh post-bank checks pass
in28.068s: actual padders, carry links, complete image/serialization, prior
producer audit and both protected-text gates. All installed source/ELF/guard/
conversion hashes remain fixed, including the unchanged67-word caller.

The commit's incremental graph hook finishes40,669 nodes/81,150 edges with no
worker remaining. The full update safely refuses an18,891-node replacement;
preserve the existing corpus and its19,398 nodes from2,972 excluded but present
files. All462 post-copy older-mirror fingerprints and its ddbdd16 HEAD remain
unchanged. No push or frozen host Release work occurs.
