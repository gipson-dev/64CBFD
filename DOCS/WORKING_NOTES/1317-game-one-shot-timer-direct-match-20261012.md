# Game One-Shot Timer Direct Match - 2026-10-12

## Scope And Recovery

Continue the full Game matching goal from consumer `25e20f20` / tools
`0a939ff` and [Note 1316](1316-game-rectangle-bounds-predicate-direct-match-20261012.md).
Both active repositories were clean. Query the existing graph, inspect the
complete retail routine, SDK prototype and actual caller before editing.
Preserve the open text218/114/cut27 and translator49/34 checkpoints.

Target `func_1501BB20` in
[generated_48FD0.c](../../conker/src/game/generated_48FD0.c:11):
VA0x1501BB20..0x1501BBB8, ROM0x48FD0..0x49068, 38 words/152 bytes,
frame0x28. Its three-word zero-return placeholder had37 real differences.
The recovered void body plus four local extern declarations emit all38 words
directly at unchanged O2/g3/MIPS2, no instruction guards, pools, shared-header,
compiler-profile, layout or Makefile change.

Constant-first `(25 * D_8002BD10) / 1000000` is directly exact. A typed ULL
constant and local countdown emit the same words. Clock-first multiplication
is semantically equivalent but has six scheduling/register differences and is
not installed. The SDK fixed-clock OS_USEC_TO_CYCLES macro does not preserve
this mutable global-clock contract.

## Contract And ABI

- Read the complete byte latch D_80084064 once. Zero does not read the clock
  or call any helper. Every nonzero byte takes the same arming path.
- Read D_8002BD10 as unsigned64, multiply by25 modulo2^64, then perform unsigned
  division by1,000,000. Preserve __ll_mul then __ull_div and high/low O32 words.
- Call osSetTimer with OSTimer D_800BE6E0, the computed countdown, interval0,
  OSMesgQueue D_8003B218 and message6. O32 slot1 is an alignment hole, not a
  defined argument; countdown occupies A2/A3 and the remaining words use stack.
- Clear the latch after the SDK call, unconditionally on its return value.
  Do not add a retry/error branch, return a fabricated zero, or clear it early.
- The real main-loop caller func_15007B3C immediately calls func_15008870
  afterward without consuming this result. The source caller func_1501905C
  likewise discards it. These are static void-contract observations, not full
  caller/runtime acceptance. The neighboring controller reader sets the latch
  to1 after osContGetReadData; no controller/queue flow is changed here.

## Qualification

```sh
python3 -m tools.experiments.game_one_shot_timer_candidates --controls
python3 -m unittest tools.tests.test_game_one_shot_timer_match -v
```

Seven pre-install tests pass in46.021 seconds; seven final post-install tests
pass in65.862 seconds, no skips.

- 36,864 guest cases combine all256 latch bytes, twelve clock edge patterns,
  both stack phases, two provider-mutation modes and three SDK status words.
  Complete RAM/events/GPR/FPR/calls agree with retail. Independently check
  the two arithmetic ABI calls, wrapped product/quotient and all defined timer
  argument words without treating the alignment hole as an argument.
- Clocks include quantization edges39999/40000, normal46875000, high32-only
  values, signed-boundary bit patterns, overflow-before/after MASK64/25 and
  MASK64. Provider mutations change clock/latch after multiplication and latch
  during SDK setup; the captured arithmetic and final clear remain correct.
- The arithmetic and SDK hooks are bounded opaque providers. Their access
  counts are excluded from own-instruction cuts and argument observation uses
  non-gated peeks. Actual 64-bit helper instructions, timer-list updates,
  interrupts, queue delivery, FCSR/EPC and hardware behavior are not emulated.
- Inactive latch works with clock/timer/queue memory unmapped. Every reached
  latch/clock byte fails closed when missing. All92 own-access cut pairs fire
  and match, with terminal no-fault controls.
- The actual unchanged linked __ll_mul48, __ull_div60 and osSetTimer224 bytes
  independently equal pristine retail. The complete image gate keeps those
  bodies and all other code fixed.
- Native32 O2/O0 uses the actual SDK header/types and prepared 32-bit shared
  libgcc arithmetic. Each profile passes116,736 cases, 233,472 comparisons,
  against independent Python-generated wide-integer vectors, all latch bytes,
  mutation/status modes and complete OSTimer fields. Fresh scale, narrowing,
  missing-clear and early-clear controls fail on valid inputs.
- The copied production owner is actually preprocessed/postprocessed, retaining
  both GLOBAL_ASM routines. Seven neighbor bodies/relative relocations, all
  normalized pools and zero diagnostics stay fixed. Both full-owner padders
  emit identical objects; target bytes/relocations equal the isolated object.
- Independently assemble/link retail and C at three code/data layouts, retaining
  eight-byte clock alignment and the low-word alias D_8002BD14=CLOCK+4.
  Signed LO16 carry boundaries are included; all38 body words agree. Standalone
  GNU section padding outside the152-byte function is checked zero, not inserted
  into the production slot or counted as new matching instructions.

## Native Runtime And Fixture Corrections

The default GCC lacks a 32-bit static libgcc archive, but a prepared i386 shared
runtime exists at `/lib/i386-linux-gnu/libgcc_s.so.1`. Link that existing runtime
explicitly; do not install packages, rebuild a compiler or hand-roll division.
Readelf verifies ELF32/Intel80386; ldd resolves the existing 32-bit runtime/
loader/libc. Runtime SHAa53ae62e is unchanged before/after qualification.
SDK assertions retain four-byte pointers/messages, eight-byte OSTime and
32-byte OSTimer; native i386 argument layout is not claimed to be O32.

Initial failures were bounded harness issues: assuming an exact section length
instead of the function extent, requesting the unavailable static archive, and
comparing captured byte output with a text empty string. No production workaround
or shared-oracle change follows.

## Literal Image And Symbol Serialization

Build succeeds with only the known duplicate generated_12D630 recipe warning.
The strict full-image gate initially rejects eight extra metadata bytes. A
structured ELF parse identifies two existing absolute symbols, D_800BE6E0 and
D_800BE2F0, whose value/string serialization order changes when the timer is
referenced. Both names, addresses, sizes, types, bindings and section identities
remain identical; the normalized complete symbol multiset agrees after the
single declared function-size update.

Account only for those two adjacent symbol value fields and two adjacent
eleven-byte name strings, verifying their old identities/values/attributes.
Then compare every ELF byte literally. No symbol/string table is skipped,
no linker artifact or source is manipulated to force the previous ordering,
and no unrelated metadata change is accepted.

Final delta:121 changed target bytes across37 words, one size-field byte12->152,
and eight closed serialization bytes,130 total. All other bytes/code/addresses/
sections stay fixed. All189,088 Game-data bytes/720 owners remain exact,
SHA0bbc00e1; guard history, progress.csv, layout and Makefile are byte-identical.

ELF SHA-256: `948ca624f482b318e5257eb5b9f191b87a77bf6f0dbdd0dbc08fcc9009f9627d`.
Source SHA-256: `210f19ef8c744387ba42ddcadb2fc8aea38d14013a9b573b4742df4149e95f7c`.
Fresh matching: Game2,817/4,823 (58.41%), total3,490/5,496 (63.50%),
different2,006/drift0. Converted functions/bytes stay fixed; root README gets
only its two aggregate rows.

## Fixture And Bank

After the independent image gate, archive the previous ED98 text manifest/image
in ignored `game-one-shot-timer-test/text-fixture-before-one-shot-timer/`.
Advance only its expected ELF hash and generated before-image/manifest. All
other eight input/snapshot hashes remain unchanged. Fresh target image and text
immutable/corruption controls pass as three tests in33.273 seconds.
Reuse prior unchanged broader semantic receipts explicitly, not as fresh tests;
historical full-image gates stay frozen to their own banks. No text or translator
matching credit is added.

Mounted tools `6a9eb2d87664c410a303703abeb6d2e396e306bf` is committed first,
then source, this note, indexes/workflow, README aggregates and gitlink.
Preserve older tools HEAD`ddbdd16b` and unrelated dirty work.
Only two absent task files and the verified shared fixture are synchronized.
All106 unrelated saved fingerprints remain unchanged; dirty384 becomes386
and task hashes107 become109. WSL consumer/mounted/older tools checks,
Windows py_compile and whitespace checks pass. All4,585 relative links across
eight checked documents resolve. No older commit or history duplication.
Require syntax/tools/link checks, clean active checkouts, post-bank integrity
and a fresh terminal Graphify Rebuilt receipt with zero workers. Preserve
existing graph/version/scan warnings. Zero Claude calls; no push, dependency
installation, host/OGL Release/ROM/save/config/editor change or full-goal finish.

## Next

Next ordinary queue entry is `func_150226BC` in `game/generated_49D30.c`,
38 words/frame0x20/current37 differences. The full original is in `asm/49D30.s`.
Its two indices select a nonzero halfword through D_800C35C8 and an eight-byte
record through D_800C35F0. Type3 uses record byte2 to obtain an actor from
func_151149AC; nonnull actor byte+0x6E==1 dispatches func_15022640 with actor
byte+0x72 and the preserved group, then clears the original actor flag.
Recover incoming-home and post-callback pointer lifetimes, early returns and
typed accesses before conversion. No source fit is accepted yet; keep the full
Game goal and separate text/translator/handwritten boundaries open.
