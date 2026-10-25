# Compact Embedded Oscillation Direct C Match - 2026-10-25

## Result

Replace `func_151B8CFC`'s zero-return placeholder in
`conker/src/game/generated_1E5FF0.c` with complete semantic C. All 43 body
words, frame 32 and six bindings emit directly from the normal compiler.
The complete 45-word retail slot also preserves its two alignment words.
There are no new guards, compiler-profile changes or shared-header edits.

Production output is adopted in the Windows checkout. The fresh recount
uses that actual Native ELF, not a predicted counter increment:

| Section | Exact C functions | Matching |
| --- | --- | --- |
| Total | 3,796 / 5,505 | 68.96% |
| Init | 492 / 492 | 100.00% |
| Game | 3,123 / 4,832 | 64.63% |
| Debugger | 181 / 181 | 100.00% |

Address drift is zero; 1,709 C functions still differ. Only `func_151B8CFC`
receives new credit. The 75% threshold remains 4,129 exact C functions,
requiring 333 more. The wider goal remains active.

## Original And Interface

- Original: `conker/asm/1E5FF0.s`, VA `151B8CFC..151B8DA8` for the body,
  with two alignment words through `151B8DB0`; full VROM slot `1E61AC..1E6260`.
- Body 172 bytes / 43 words; full slot 180 bytes / 45 words; frame `0x20`.
- Canonical callback: `s32(u8 *)`, returning one to retain the actor.
- Preserve the existing single-precision sine, wrap and time-step declarations.
- Six binding byte offsets: `12 R_MIPS_26 sinf`, `24 HI16 / 52 LO16 D_800BE9A4`,
  `80 R_MIPS_26 func_15144B68`, and `96 HI16 / 100 LO16 D_800BE9A4`.

The private `CompactEmbeddedOscillatingMotion` view exposes only the 0x1C-byte
state at actor `+0x110`: base, amplitude, phase, phase rate, X velocity,
four reserved bytes and Z velocity. The output is actor `+0x38`; planar
coordinates are `+0x40` and `+0x48`. Do not infer an entire actor schema.

Compute sine output with separate float32 multiply/add operations, advance
and wrap phase, then advance both planar coordinates. Keep field reloads
after the helpers and separate live time-step reads. The original loads Z
before storing X, then reloads the time step for Z. The directly emitted
instructions preserve that schedule, the incoming actor home and saved
motion-pointer lifetime without adding volatile declarations or guards.

The actual `D_80089CB8` registry has 42 entries; this target is slot 35,
literal VROM `22E804` / VA `80089D44`. The complete original dispatcher
`func_1513CFE4` is 195 words at VROM `16A494`. It uses the unsigned selector
at actor `+0x70`, skips zero, passes the actor pointer and uses a zero callback
result as a stop request. No aligned encoded direct-JAL sites are found;
this is not proof against arbitrary computed calls.

The retained dispatcher remains a 12-byte zero-return C placeholder, with
18 of its 195 retail-slot words equal. Connected original-dispatcher tests
are not retained-C dispatcher parity, new caller credit or a working
production gameplay path. Caller source/object and all registry data remain
unchanged. Do not import the neighboring routine's signed slot-2 ABI.

## Qualification

Both tools copies pass ten genuinely fresh pre-install checks, with zero
errors, failures, skips or reused checks: active copy 110.421 seconds,
older mirror 40.417 seconds. Both shared tools checks pass, in 0.310 and
2.004 seconds. Four separate discriminating smoke checks pass in 63.225 seconds.

An earlier smoke failure was a test-fixture initialization error: the stale
target's negative case left actor `+0x72` at its patterned value and entered
the original stop callback table. Initialize it to zero, matching the bounded
positive fixture. Preserve the failed log, reseal both copies, then rerun the
smoke and both complete fresh suites. No production C or emitted words changed.

- 443 guest cases across two stack phases give 886 modeled phases, including
  112 clock-alias phases. Execute all 43 target words; compare complete private
  state, helper arguments, public bytes, returns and stack restoration.
- Native32 `-O0`, `-O2` and `-O3` each pass 366 valid, nonaliased typed-object
  cases with trapping UBSan and separate float32 operations. Verify the actual
  compact 0x1C-byte subobject, 0x12C-byte actor, field offsets and fences.
  All 12 compiled semantic negative controls are effective.
- Original sine and wrap chains pass 72 connected phases. Their retained
  baseline slots are independently exact across 104/104 and 24/24 words.
  Visit 124 helper words, including all 24 wrap words; do not claim all sine
  paths, huge/infinite wrap completion, complete FCSR or hardware parity.
- The full original 195-word dispatcher is loaded for 576 connected cases:
  active/selector/timer gates, countdown outcomes, both stack phases and
  helper mutations. Animation and secondary callbacks are deliberately
  disabled; release is a scripted provider. Reject the old target stub's
  wrong stop request and separately observe the retained parent stub's lack
  of effects. Do not claim all 195 caller words were executed.
- Nine independent GNU links across three layouts compare original, raw C
  and padded C, exercising all six bindings and signed-low carries in
  72 rebase phases.
- Compare 200 target-access fault prefixes. These qualify emitted guest
  accesses, not portable-C fault semantics or hardware exceptions.
- An actually compiled post-wrap cached-clock negative diverges when the
  X store aliases the clock before the Z load. This is guest-only alias
  evidence, not a fabricated overlapping native C object.
- Reject 43 raw-word perturbations, all six binding corruptions and seven
  strict-image corruptions. Check both alignment words and the unchanged
  guard CSV. Accept the full 40-input installed map, then reject six live
  and six frozen mutations plus the stale predecessor object. The installed
  object must be the qualified new object, not the old stub object.

After production, both copies pass two fresh installed checks in
14.645 / 12.185 seconds: owner/Make/registry identity and strict image/input
history. Eight semantic checks are explicitly reused only under identical
sealed inputs, module hashes, qualified artifacts and actual installed
source/object/ELF bytes. These are not ten fresh installed checks.

## Production And Preservation

The actual production command is:

```sh
make -C conker -j4 -o retail_word_patches.us.csv build/conker.us.elf progress.csv
```

Pin inherited unchanged guard consumers while freshly compiling this owner
through its normal three-command O2/g3 path. There are no new guard rows.
This is not an unmodified whole-tree rebuild claim. The Make shadow reproduces
all four raw functions, complete padding and metadata; all three neighbors
and owner pools remain fixed. Inherited duplicate-recipe warnings for a
different owner are unchanged. Actual production Make exits zero in 6.008 seconds.

The complete production ELF equals the independent prediction exactly:
142 changed bytes, comprising 141 target-code bytes and one symbol-size
byte (12 to 172). There are zero exclusions or metadata permutations.
All 6,054 other linked bodies and all addresses remain fixed. Protected
Game data is exact across 720 owners / 189,088 bytes, with zero differences.

The 16,046-file Native/cache seal covers all 1,454 linker input objects.
Adoption checks that closure before and after promotion with only three
overrides: source, target object and ELF. The guard CSV stays unchanged.
Use explicit WSL `--cd` and verified stdin/tar transfers; no project-data
reads through DrvFS and no IDO paths containing spaces.

The actual adopted Native ELF is streamed back for the CLI recount, which
exits zero in 6.360 seconds. Reclassify all 5,505 US C rows; remove only this
function from the queue. The remaining source-shape queue has 1,580 placeholder
definitions, 120 semantic/other definitions and nine parser-unlocated entries.

Tools are banked first as `284f8401a0c98394a5d9a66e75e236b8003d36ca`.
Preserve the older mirror's HEAD and all 1,650 pre-existing changed paths;
its only additions are the two owned modules. No mirror commit, push,
Claude calls, package/global/provider configuration changes or host/Release changes.

| Artifact | SHA-256 |
| --- | --- |
| Input snapshot | `b9aaa450990993cac090fdb3ecca406383d0902748f49f6db646ad1d1e3b85bc` |
| Raw 43-word body | `fa2bba2b02a026c254cf9379bd07e03a033ff51b03b68b1155973f79af3fbfd6` |
| Qualified source | `38859b61fd08db476b437333202cde72a34eb5a6c16f98f7175e9b5b0ea79e78` |
| Qualified target object | `96a4332489a2d69590927aa45887d81ee6a34b6463c3518737e7bec706772284` |
| Adopted ELF | `cc82d9781d419bde3fe004381a1c4ee34101f384336cb8e5f50ad8aa386f5388` |

## Next Work

The next ordinary placeholder is `func_15085ABC` in `generated_B21B0`.
Five private source forms isolate the first three forms' sole difference to
integer-AND operand order at word 21. Writing the shifted bit first closes it:
all 44 body words/frame 48/five bindings match directly, with one alignment
word outside the body. The full 32-bit-argument alternative is rejected.
Raw matching-body hash is
`2933bafae376c06d981bf0e15d46afc5af43b2608481dc196819a202f33654ac`.

This screen leaves production source, object, guard and ELF inputs unchanged.
Caller/helper ABI, registration, guest/native, aliases/faults, complete owner,
padding/Make/image and adoption gates remain open. It is uninstalled and
uncredited. Keep existing-C `func_15014094` and parser-missed `Gfx *func_1510D8C0`
separate from ordinary zero-return placeholders.

The root README gets aggregate rows only. Graphify navigation was a bounded,
truncated 101-node query, not complete relationship evidence. After the consumer
commit, verify owned graph workers actually exit zero, all 44,180 baseline
nodes are retained or uniquely one-to-one relocated, and all eight changed
C/Markdown manifest hashes/mtimes/memberships are current. Extract the two
tools modules separately because the parent ignores `tools/`. Retain the
filtered-corpus warning; do not claim full-corpus re-extraction, old-edge
preservation or stamp missing producer provenance into graph artifacts.
