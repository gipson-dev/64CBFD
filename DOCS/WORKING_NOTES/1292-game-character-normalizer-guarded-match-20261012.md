# Game Character Normalizer Guarded Match

Date: 2026-10-12. Recover complete func_15042C40 in
conker/src/game/generated_6E770.c. VA 0x15042C40..0x15042D50,
ROM 0x700F0..0x70200: 68 words / 272 bytes. The semantic C body is 65 words,
frame zero; twelve expected-word guards normalize cached-byte reads and
scratch allocation. Preserve three original zero tail words. This is not
direct C. Keep the existing no-unroll profile, pool binding, original ASM,
data, SDK and callers. No insert/omit rows, helper stub, dummy state or broad
conversion batch. Matching +1 only, converted functions/bytes unchanged.

## Baseline And Contract

Consumer 879832f43f79fe9c1b7d7193139863a44b8fbdae and mounted tools
5d3c18bdb8e2fac83bbd8a5b3f7a2a8662edea3e were clean at entry.
[Note 1291](1291-game-extended-character-metrics-direct-match-20261012.md)
left the 68-word / 62-difference placeholder. Read the complete original
routine, both direct callsites and actual data owner/compiler profile; query
Graphify for navigation. Codex sole writer, zero Claude calls. Reuse IDO,
structured ELF/object/pool parsers, MIPS/native32 and both actual padders.

Recover s32 func_15042C40(u8 character). Preserve a copy of the incoming
byte. Search uppercase ASCII for input a..z, but return the original byte
when absent. Space returns 0x60 before any table read. All other bytes scan
exactly 95 entries, return the first matching index, or the original byte.
The final zero alignment byte at index 95 is not a searched entry. The first
three entries are separate original labels D_80085930..32; the remaining
92 entries are accessed through D_80085933 in four-byte scan groups.
Retain the original conker/asm/data/2275E0.data.s, not a copied/rebuilt pool.
Its duplicate EA entries at indices 81/83 and F4 at 89/91 stay first-match.
Do not apply Unicode/locale conversion, add NULL/range gates, return the
uppercase fallback, search the padding byte or reorder table reads.

The original first instruction stores the complete incoming O32 word at
SP+0 before narrowing to its low byte. Guest tests retain noncanonical high
bits and home/table aliases; native tests use the actual typed byte argument.
This does not claim portable private-home or 64-bit-register behavior.
No helpers, allocated frame, saved-register changes or table writes occur.

Twelve guards are exact compiled-word checks without relocations. Three
read A0 versus V1, which hold the same cached byte at these points. The other
nine reassign the closed counter/bound lifetimes: raw A2 counter -> retail
A0, raw A3 bound -> retail A2. The normalized search byte remains A1; the
original byte remains V1. PCs, branch offsets, delay-slot effects and live
reads/stores are unchanged. Include the unreachable duplicate counter word
in the literal guard closure. These are not scheduling swaps or a direct
compiler match. Stale words and a missing counter guard fail effectively.

## Source Screen And Qualification

The first four-entry C form emits 65/frame zero with twenty differences.
An explicit original-byte lifetime and first-three comparison direction
reduce that to thirteen; cursor-before-counter initialization reduces it to
twelve. Integer search, byte return, local order, for/do forms, parameter
reuse and register declarations do not produce a direct owner-profile match.
Sixteen small original-capture variants retain twelve differences. Select
the clear explicit-lifetime body; do not pretend this bounded screen proves
no possible direct form exists.

Selected default O2/g3 gives 110 words/79 differences; O1/g3 and O1 give
87 words/frame 0x10/81 differences. A properly array-declared simple 95-entry
loop gives 33/50 under current no-unroll, but 65/three differences under
default O2/g3. That is a useful future guard-removal route, not permission to
change the whole owner's profile without requalifying its earlier manual
lookup and every neighbor. Bank the qualified current profile first.

Nine pre-install tests pass in 42.739 seconds. Nine installed tests pass in
17.248 seconds; final nine installed tests pass in 18.035 seconds after
correcting a native receipt label (no float-size claim for this byte routine).
The final two literal-integrity/corruption-control gates pass after all indexes
in 4.202 seconds. All 4,437 relative links across seven edited docs resolve;
git diff --check passes, with only the existing CSV line-ending warning.
Receipts: conker/build/game-character-normalizer-match-test/.

- 1,737 original/raw/guarded leaf cases cover every byte, three incoming high-
  word patterns, two phases, all 95 forced first-match indices, duplicates,
  absent lowercase, space and the excluded padding byte. Raw complete memory,
  events and return agree with the reference; guarded complete GPR/FPR state
  agrees with retail. No unsupported raw scratch-register equality claim.
- All 61 reachable body words are exercised. The original 65-word body has
  four unreachable words: duplicate loads at 0x15042CF0, 0x15042D04 and
  0x15042D18, and duplicate increment at 0x15042D2C. Branch-likely paths
  either load in the taken delay or return, never enter those copies. Retain
  all four literally, plus the three zero tails; do not claim execution of
  all 65 body words or delete originals merely because they are unreachable.
- 60 home/rebase cases qualify the full incoming home store before table
  reads and two independent code/four-label table links with HI16/LO16 carries.
  Private-home aliases are byte-addressed guest evidence only.
- 594 fired original/guarded fault pairs compare complete partial memory,
  events and GPR/FPR. Space succeeds with the entire table unmapped and only
  its one argument-home store. No portable C/hardware or raw private-fault
  register claim.
- Six independent compiled semantic controls fail: lowercase bounds, space
  code, normalized fallback, short table and skipped first duplicate. Stale
  expected-word and missing-counter-guard controls reject or produce a real
  wrong public return, not just a differing instruction fingerprint.
- Complete copied owners are diagnostic-free under actual no-unroll;
  all seven neighbors' bodies/extents/relocations and pools are identical.
  GLOBAL_ASM and both actual padders agree, retaining the existing metrics
  pool binding. Compare unlinked target bytes/relocations to independently
  linked isolated guarded retail words; do not compare unresolved relocations
  directly with absolute ROM instructions.
- 1,024 actual call/return-mask window cases execute the original JAL and
  delays at 0x15041BD8..15041BE0 and 0x15042968..15042974. No lookup hook;
  guarded state equals original. Synthetic window exits do not qualify the
  complete formatter or measurer.
- Native32 O2/O0 each pass 2,655 actual semantic-C cases, original table,
  all 95 forced indices and complete table/padding/adjacent canaries. Byte
  arguments, four-byte integers/pointers and six effective negatives pass.
  No native private-home, 64-bit, FCSR/RSP/RDP/hardware/gameplay claim.
- Frozen source/entire-ELF/extent/guard-prefix/ten-input gates reject source,
  instruction, original padding, neighbor, size, table and guard corruption;
  stale/duplicate source and duplicate guard application also fail. No
  production mutation, metadata projection or frozen-baseline refresh.

Fixture corrections before install: isolate leaf guard rows from unrelated
owner guards; distinguish four unreachable words from reachable coverage;
compare unlinked relocations through the actual linked isolated target; and
declare a genuine 95-entry array for the simple-loop experiment instead of
indexing past a scalar declaration. No production workaround or weaker
immutable audit was introduced.

~~~sh
python3 -m tools.experiments.game_character_normalizer_candidates --profiles
python3 -m tools.experiments.game_character_normalizer_candidates --filter=loop95 --profiles
python3 -m unittest tools.tests.test_game_character_normalizer_match -v
make -C conker -j4 -W src/game/generated_6E770.c build/conker.us.elf progress.csv
make -C conker match-progress NON_MATCHING=1
make tools-check
~~~

## Linked Audit And Progress

Promote the independently qualified generated CSV successor only after
checking the old manifest hash. Preserve its exact old byte prefix and mixed
line endings; append precisely twelve rows. The changed guard dependency
triggers a broad rebuild; original session reaches terminal exit zero.
Existing unrelated CFE diagnostics and duplicate generated_12D630 recipe
warning remain separate from the diagnostic-free target owner.

The literal entire-ELF audit changes only 198 bytes: 196 target bytes and two
size bytes (12 -> 260). All other instructions, addresses, extents, headers,
symbols, strings, sections, pools and data are byte-identical. No linker
metadata exception is needed. Ten other inputs remain byte-identical:
progress CSV, Makefile, original ASM, table data, metrics pool, rodata,
symbol definitions, undefined functions/symbols and layout. Old guard history
is an exact byte prefix. Protected data: 189,088 bytes / 720 owners,
zero differences, SHA-256
0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670.

| Input | SHA-256 |
| --- | --- |
| Source before | 8677e241aee0ae98694ab04154d4d1949de586b49d86e64e110edc37cfb33473 |
| Source after | 802b4d27659c80620c2ca509df4c3da84d136c5c92b758d7a6390c4428d2273d |
| ELF before | 1337dd11530d3ef13938f6cf3995e65acee4357cae88832059f50559aa7a7d07 |
| ELF after | 978d39eab009d4134e5c03d4bdd2d433010812544a5be599c823fdff1ce2aa14 |
| Guards before | 9b08dabc9ccc24cfa82b40ec626d3f5f73a7521f89d5a118f8e62773ccfea168 |
| Guards after | 3f12cf872b84100963934734de2e67f5f07073ce3112ccbd2e5c4cb8af84666e |

Fresh matching: Game 2,813/4,823 (58.32%), total 3,486/5,496 (63.43%),
Init 492/492 and Debugger 181/181. Zero drift / 2,010 still different.
Matching +1 only; converted functions/bytes unchanged. Root README gets
aggregate rows only; detailed function narrative stays here.

## Checkpoint And Next Body

Bank mounted tools 05875fe0def7acca6c67977c7ca19d80b620c7c7 first, then
consumer source/guards/docs/exact gitlink; no push. Consumer, mounted and
older WSL shared checks and native Windows py_compile pass. Preserve older
standalone HEAD ddbdd16b53ce60b054fb6e11bf0649a41f48375a and all 75 prior
hashes; add only two absent identical copies, dirty count 352 -> 354,
final 77 hashes. Do not commit/reset independent older history. Prior unchanged
neighbor-suite receipts are reused on exact fingerprints, not claimed fresh.

Graphify query completes; native update exits one on protective shrink
refusal: 18,265 candidate nodes versus 40,043 saved. Preserve 19,398 nodes
from 2,972 excluded but existing files; no force/purge/install. Version and
empty-source warnings are separate from compiler diagnostics. Before final
reporting require a fresh terminal post-consumer-commit Rebuilt receipt,
advanced log bytes/UTC and zero native workers; launching a hook is not proof.

Six of eight owner functions now match; two placeholders remain. Next recover
func_150428D4: 219 words / 876 bytes, 199 differences, frame 0x80,
VA 0x150428D4..0x15042C40, ROM 0x6FD84..0x700F0. Inspect its complete four-
argument text/three-output contract before naming output meanings. NULL leaves
outputs untouched; an empty string is not NULL and follows its height path.
Recover newline accumulation, 0xBC two-byte skip, space/control/ordinary/
extended glyph paths, repeated live D_80085994 pointer loads, final live
D_800380A0/A4 float scales, aliases, truncation and return semantics. Connect
actual normalizer and metrics helpers, not stubs, for full-chain qualification.
Then address the remaining 1,098-word func_150417AC formatter.

Guard removal, hardware/FCSR/RSP/RDP/renderer/gameplay acceptance and the
full Game goal remain open. No OGL build/change, private save/input or active
editor/debugger mutation.
