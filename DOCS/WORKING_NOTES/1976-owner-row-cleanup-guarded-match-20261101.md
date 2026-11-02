# 1976 - Owner row cleanup recovered as a guarded byte match

`func_1518BBF4` now matches all **55 retail words**, with its natural **48-byte
frame**. Semantic C emits 54 words; **eight checked guard rows** restore a
closed loop rotation, independent address setup and the retained endpoint alias.
Actual production Make and the independent Native ELF recount confirm
**4,043/5,507 (73.42%)**, Game **3,370/4,834 (69.71%)**, zero drift and
1,464 still different. Exactly one match is added. The threshold is 4,131:
**88 more** are needed for 75%; the wider goal remains active.

## Behavior and interface

Owner `generated_1B8F40`, source `conker/src/game/generated_1B8F40.c`, VA
`0x1518BBF4..0x1518BCD0`, ROM `0x1B90A4..0x1B9180`.
Recover `void func_1518BBF4(u8 *owner)` from the false zero-return placeholder.
Null owner returns before any public access. A nonzero owner is an opaque token
on reachable paths; the original never dereferences it there.

Traverse two 0x1A0-byte rows of `D_800DCE50`, using each head at +0x7C. Increment
the signed global depth byte `D_800DD190` before walking each row, save record
+8 into `D_800DD198[depth]`, store owner at record +0x24, and call
`func_1516972C(record)`. Reload the **live depth and live pending-pointer slot**
after cleanup. The helper can repair pending pointers, mutate depth or change
the later row head; caching the next pointer across it is incorrect. Decrement
the live depth after each row. Target signed-byte wrapping is retained.

The inner owner/record identity condition is unreachable under the outer nonnull
owner gate. Keep its four emitted instructions at offsets +0x74..+0x80; public
coverage excludes them explicitly. No fabricated owner null check or extra
depth-exit condition is added. Declarations are owner-local and compatible with
the existing later cleanup declaration; no shared header or caller source edit.

## Closed layout normalization

Raw isolated C payload SHA-256:
`a1faf50f5736e7ad28255ff837773002798a24f33bc878e9362d1c17b2f2597e`.
Raw shape is 54 words/frame48, with 16 position-aligned differences from the
55-word retail slot. Eight expected-word/relocation guards do only the following:

- +0x20 adjusts the null exit across the inserted word.
- +0x28 rebinds the endpoint high half from table-plus-addend to the retained
  `D_800DD190` endpoint alias. +0x34/+0x38/+0x3C/+0x40 form the independent
  address-completion permutation, with exact HI16/LO16 bindings.
- +0xB0 moves the depth decrement store before the back edge. +0xB4 replaces
  the raw ordinary branch with the original likely branch and copies the depth
  preload into its taken delay slot. The initial preload is already present.

Raw code enters the loop at the depth load; retail's taken back edge executes
that same load in its delay slot and enters at the head load. The copied static
load adds **no dynamic read**. Both versions store the decremented depth on the
final iteration. All 55 normalized words and all nine relocation bindings equal
independently assembled original code. Existing guard bytes are an exact prefix;
only these eight rows are appended. No shared padder, compiler profile, Makefile,
inline assembly or physical-register source binding is introduced.

The retained BSS group is table at `0x800DCE50`, depth at table +0x340 and slots
at table +0x348. Three GNU layouts use table bases `0x800DCE50`, `0x80107FFC`
and `0x8020FF10`, checking HI/LO carry behavior and the group geometry. This
is a grouped relocation proof, not a claim that the endpoint alias can move
independently. Portable native fixtures deliberately separate depth from the
array endpoint while keeping the C endpoint expression based on the array.

## Qualification and limits

- **5,824 guest inputs** produce **17,292 finite cases / 51,876 executions**
  over three layouts and original/raw/normalized roots. All 256 depth bytes on
  empty rows, signed negative slots, physical aliases, helper depth/slot/head
  mutations, modeled nested repair, stack phases and full owner words are
  checked. Complete bounded GPR/FPR/HI/LO, memory, calls and access traces agree
  for raw C too. Original covers 51 words and raw covers 50; four dead words
  remain emitted. Three sparse null-owner executions map no public objects.
- **60 cyclic inputs / 540 bounded prefix executions** stop after 16 modeled
  callbacks. An independently repeated reference state proves the provider
  cycle; these are not counted as terminating cases. **226 access-prefix
  triplets** check the same bounded state and access order. Raw fault PC/BD
  equality, portable C fault semantics and real hardware are not claimed.
- Native32 **O0/O2/O3 each pass 2,892 cases / 26,028 executions** with UBSan and
  complete public World bytes. Signed indices have valid interior-array
  backing. Eight effective controls reject omitted owner stores, freed-next
  reload, ignored live slots, unsigned depth, missing decrement, skipped row,
  an extra nonnegative-depth exit and priming depth only once.
- Original `func_1516972C` (28 words), `func_151696DC` (20) and `func_15169804`
  (8) equal retained production slots. **484 finite cases / 1,452 executions**
  execute every helper word, including pending-pointer repair and default/typed
  callback routes. Four cyclic helper cases have 12 bounded prefix executions.
  Lower `func_15168B10(node, 1)` and typed callback bodies remain stubs; modeled
  callback repair does not establish complete engine behavior.
- A complete aligned ROM census finds one direct JAL at ROM **0xC5A1C**,
  VA **0x1509856C**, within the 2,210-word parent `func_15097A8C`. The original
  four-word window forwards S1 to A0 in the delay slot and forces V0 to one
  after the call, establishing the unused/void result. **157 cases / 471
  executions** cover all four words and full-width owners. The actual branch
  endpoint is `0x15099C00`. No full-parent qualification is claimed; one cyclic
  root sample remains in the separate prefix suite. No direct J/pointer literal.
- Both raw and padded owners retain **eight neighbors**, identical normalized
  pools and **zero diagnostics before/after**. There are no GLOBAL_ASM bodies
  in this owner. Its actual **three-command Make recipe** produces the qualified
  padded object literally. The inherited duplicate generated_12D630 recipe
  warning remains in full production logs; the build is not called warning-free.
- Each tools copy passes **five target tests and shared checks before and after
  installation**. Fresh public tests recompile C and relink three layouts;
  immutable private artifacts are fingerprinted, not silently regenerated.

## Advisory review and disposition

One read-only Claude Pro advisory was attempted and completed for the loop
schedule question, before this continuation. Effective tools and MCP lists were
empty; no additional call or retry was made. Model `claude-sonnet-5`, packet
SHA-256 `649e230d6f3d1a7eabfe845a47c0efea7c915411dc2de33de14cae09ad1fcc17`.
This is the transmitted LF-normalized UTF-8 digest; the retained local packet
file has SHA-256 `17a007d7efe90837cb4590ee5d725e86631bd54bed50d21f26c653c54f235d6e`.
Packet, answer and receipt remain in the ignored stage. A scheduler tie-break
explanation remains unproven. Priming depth only once and an extra depth-exit
condition are independently rejected by guest/native witnesses. Footer swapping
was already ineffective across all twelve source-screen pairs. Zero C changes
were adopted from the advice; normalization and dynamic-read equality were
independently derived and tested.

Preparation failures are retained: full-owner padding on an isolated object was
corrected to its isolated retail layout; an aliasing provider cycle was given an
explicit bounded-prefix classification rather than misreported as termination.
No guard or test gate was weakened to bypass either failure.

## Production preservation and continuation

The independent predictor starts from frozen ELF
`2d4f55fb3eb0eb90fb9d5cf829d92ea1771b03b1d2529a3f22bb8a8ba0c7f3af`.
Only the 220-byte target slot and symbol size **12 to 220** change. Actual Make,
first private link and prediction agree literally, with **zero exclusions**.
All **6,052 addresses**, **6,051 other function bodies**, complete named-definition
multiset except the declared extent, ELF length, map and Makefile remain fixed.
All **189,088 protected Game data bytes across 720 owners** remain exact.
Every one of the **17,714 prior sealed files** is reviewed: before documentation,
only source, guard CSV, owner object and production ELF change.

Production ELF SHA-256:
`83088793cafaec148da7082549742f2dd2c964ba2049ca56acb368fc8e01e6d1`.

Stage `conker/build/game-owner-row-cleanup-1518BBF4-match/` retains frozen inputs,
**39 preparation-artifact pins**, source screens, private/public test receipts,
original assembly, actual Make commands/object, image prediction, production and
Native recounts, full current seal and handoff. Four public tools modules cover
source/image, guest/helpers/caller, native controls and integration. The scoped
13-file AST graph refresh preserves every old node and valid edge occurrence,
archiving the obsolete integer return-type edge. Zero LLM tokens; no global
reclustering or full-corpus extraction. README changes aggregate rows only.
Commit tools before consumer; no push. Private candidates, unrelated mirror
changes, cleanup archives and frozen host Release stay preserved.

Next ordinary unmatched function from the actual linked inventory:
**`func_151618BC`**, 57 words in `game_18D770`. Its seven-argument placeholder and
commented donor suggest an audio-event selector, local ten-word table copy and
unsigned PRNG remainder. Audit the complete original, true narrow arguments,
stack argument homes and callers before proposing C. No match or runtime
qualification is credited to it here. Historical whole-image fixtures and parked
candidates require explicit rebasing before reuse. The 75% goal stays active.
