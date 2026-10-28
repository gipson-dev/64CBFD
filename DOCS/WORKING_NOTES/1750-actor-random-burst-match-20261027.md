# 1750 - Attached actor random burst direct C match

Verified: 2026-10-27. Target `func_15147040`, owner `generated_173D40`.
VA `15147040..151470FC`; retail ROM `1744F0..1745AC`.

## Result and source shape

Replace the zero-return placeholder with the complete 47-word /188-byte callback.
All words emit directly under normal O2/g3: frame 0x50, four R_MIPS_26 call
bindings, zero new guards. All 12 owner neighbors and pools remain fixed;
all 13 compact functions agree with the actual three-command Make recipe.
The slice comment now describes partial recovery.

The recovered API is `void(u8 *actor, u8 context, s32 unused)`. Preserve three
incoming word homes even though the third value is not used. The second input
is consumed as its unsigned low byte at incoming SP+7. The callback returns
early when the pointer at actor+0x1D4 is null. Otherwise ask `func_15146890`
for a three-float position, passing the actor, zero and the byte context.
Its return value is ignored. Then draw an integer random word, calculate
`(u32)word % 11U + 5`, save it as s16, draw the float random value, multiply
it by 11.0f and submit the twelve-argument `func_1514C678` packet:
XYZ, scale, 0, 255, count, kind22, flags0, float0, null payload, alpha255.

Keep position at frame+0x44 and count at frame+0x42. Point coordinates and the
signed short count are loaded after the float RNG call. The ordinary enclosing
if source already fits 47 words/frame 0x50 but differs at two opening words.
An explicit early return recovers the retail incoming actor reload and A2
initialization schedule directly. Eight bounded source forms were screened;
a volatile actor parameter and typed indirect helper call did not match.
The selected source uses no volatile qualifier or indirect-call cast.

The existing point helper remains an unrecovered C neighbor. Its old-style
s32 declaration preserves the existing definition; this call passes a float
output pointer, actor pointer, integer zero and the default-promoted byte
context in the measured four-word ABI. Do not change the neighboring stub or
invent a shared prototype as part of this match. Other helper declarations
use the already-qualified RNG and twelve-argument emitter interfaces.

## Callback table and actual dispatcher

An aligned whole-ROM census finds one pointer at ROM22EB9C /VA8008A0DC and
no direct JAL or tail J. This is slot5 of the 21-entry `D_8008A0B4` effect
registry, paired with count -1. The existing `func_15141A7C` dispatcher calls
this callback directly for a selected nonpositive-count effect and through
linked effect records. Its physical arguments are actor, full context word,
and either zero or the sign-extended record halfword. This target narrows
context to a byte and ignores the third word. Native tests call the precise
callback type; they do not invoke an incompatible C function pointer type.

The original and retained 100-word dispatcher bodies are identical. Ninety-six
cases run the actual registry through both routes with context/attachment,
record-halfword and stack-phase boundaries. They visit 93/100 words; unrelated
positive-count branches are outside this target route. Classification and list
search remain explicit bounded contracts, not complete parent/helper claims.

## Qualification and its limits

Both tools copies pass eight fresh canonical methods and their shared tools
checks. Each installed copy runs owner/image checks fresh and reuses six
semantic receipts only after strict source/module/input/artifact identity.

- 4,512 guest cases cover every context byte and high-word noise, unsigned
  RNG boundaries, both attachment states, incoming homes, two stack phases,
  four alias layouts, late point loads and the signed count home. All 47
  target words are visited; compare complete private machine state and memory.
- Native32 O0/O2/O3 with trapping UBSan pass 18,432 positives per profile and
  eight effective C controls: RNG sign/modulus/base, scale, kind, alpha, gate
  and an early position capture. Providers initialize the point before use.
  A retained point pointer is used only during the callback lifetime and is
  cleared by submit. Explicit noinline provider boundaries avoid a conservative
  O3 escaping-local warning; no warning or sanitizer check is disabled.
- 140 fired guest fault-prefix pairs check matching dispatch state, PC and
  branch-delay ownership. A compiled wide-count mutant fails the signed short
  home test. These observations do not claim portable C fault semantics.
- 192 integrations run original 56-word point lookup, the floating path of
  original 49-word matrix extraction, and both retained handwritten RNG bodies
  (18 and 25 words). Visited words are 34/56, 14/49, 18/18 and 25/25 respectively.
  Both RNG seed updates and resulting packets agree with an independent seed
  formula. The fixed matrix path and unrelated point-helper mode are not covered.
- The actual point helper writes only for context 1/2, selecting matrix joints
  19/23. For unsupported selectors the original target submits prior stack
  contents; guest tests preserve those seeded bytes. No native uninitialized
  float execution or portable C guarantee is claimed. The point helper stub
  stays uncredited, and submit remains a bounded provider contract.
- Six GNU links over three layouts, including a different JAL region, preserve
  all four call bindings and pass 18 guest cases. Three raw/binding controls,
  seven image corruptions and three wrong-input controls fail closed.

The initial native O3 harness warning and failed compiler-screen JSON transport
receipt are retained. They did not change the production C/artifacts. Routine
Claude calls: zero. No full helper, hardware, gameplay or host acceptance.

## Production image and measured progress

Normal production Make passes with the inherited duplicate 12D630 recipe warning.
An independent complete-ELF prediction allows exactly 140 changed code bytes and
one symbol-size byte, 141 total, zero exclusions. All 6,056 function addresses and
6,055 other bodies remain fixed. Protected Game data is exact: 720 owners /
189,088 bytes. Inventory and the complete guard CSV remain unchanged.

Native guard CSV SHA-256:
`bc18bdc4633b2387568bc04ee6f816ede14290f391446f745a97b44027eecc59`.
ELF SHA-256:
`b0183c080c3556af45e9eefe8f349268ee71682729805d7370af6d72ee47a78f`.
Full Native/cache audit: 16,177 sealed inputs and 143 focused inputs, with only
qualified source/object/ELF/map overrides. Recount the captured adopted Native
ELF rather than an isolated candidate:

| Section | Exact C functions | Different | Drift |
| --- | ---: | ---: | ---: |
| Total | 3,828 /5,506 (69.52%) | 1,678 | 0 |
| Init | 492 /492 (100.00%) | 0 | 0 |
| Game | 3,155 /4,833 (65.28%) | 1,678 | 0 |
| Debugger | 181 /181 (100.00%) | 0 | 0 |

Only `func_15147040` becomes exact. Conversion totals stay fixed. The 75%
threshold is 4,130, requiring 302 more matches. Remaining source screens are
1,549 placeholders, 120 semantic/other definitions and nine unlocated entries;
source shape is not qualification.

## Banking, graph and next target

Predecessor consumer `87f236f2d1a44879eeb72e459cfbd9ecc9818449` and tools
`5a5f2e5dccbd48131f5b06a8a5866e55d6621b99`. Bank tools first at
`995b06ec87046aeb17f571d3f0cf622288348f8e`, then source, consumer pin and
measured docs. Preserve 1,710 inherited dirty paths plus two new files in the
older tools mirror; do not commit its independent history. No push.
README changes only its two aggregate matching rows.

Refresh ten changed graph sources with node/relationship retention. Resolve
qualified calls using actual source and relocations; the preserved 120-word
submit assembly supplies its definition when no function node is indexed.
Outside manifest rows and historical communities remain historical. No
full-corpus extraction, global clustering or centrality claim.

Evidence: `conker/build/game-actor-random-burst-match/`: immutable raw/Make
fingerprints, preparation, canonical/installed receipts, production/live audit,
actual 75-percent queue and final graph/`FINAL_AUDIT.json` receipts.
Next inspect `func_1516C878` in `generated_197C20` (47 words), beginning with
graph/source/retail/caller review and a fresh frozen predecessor. Keep
`func_1514E920` parked and uncredited. The 75% goal remains active.
