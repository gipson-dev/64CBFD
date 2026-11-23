# 2649 - Owner phase callback direct match

Date: 2026-11-23. The total 85% matching goal remains active.

`func_150BF760` replaces its zero-return placeholder in
`conker/src/game/generated_EC420.c` with the complete owner phase callback.
The C body emits **all 199 original words in the original 64-byte frame**,
including every relocation binding. This is a **direct compiler match**:
**zero new guards, insertions or omissions**. The complete guard CSV, layout,
compiler profile and shared padders remain unchanged.

Production: **4,630 / 5,528 (83.76%) total**, **3,957 / 4,855 (81.50%) Game**,
zero drift, **898 different**, **69 more matches to 85%**. Init stays 492/492
and Debugger 181/181. Conversion rows and converted-byte counts stay fixed.

Original: `conker/asm/EC420.s:561`, VA `150BF760..150BFA7C`, ROM
`ECC10..ECF2C`, 796 bytes. Both complete-owner padders and the real Make recipe
preserve the other nine functions, all pools and the owner diagnostic set.

## Recovered behavior and interfaces

The measured interface is `void func_150BF760(u8 *owner)`. No direct JAL edge
appears in the literal census. Its one aligned pointer is ROM `22D7B0`, VA
`80088CF0`, the first callback in **`D_80088C90[8]`** at a 12-byte entry stride.
The original 22-word setup window `1509EBBC..1509EC14` copies the entry's
callback to owner +0x38, its second callback to +0x78, and its byte flag to
+0x92. Actual JALR windows at `15113EE0` and `15113FB8` pass the saved owner
pointer and discard the result. Complete setup/dispatch parents are not
claimed. Computed/materialized references are not excluded by this census.

The callback returns early when `D_800C35EA == 1 && D_800C35E8 != 1`.
Otherwise it calls the phase updater, reloads the owner handle at +0x124,
requests a missing handle, and looks up object ID 20. The request supplies
`(owner, D_800902B8, 1, -1, 0, 0, -8)`. It then reads the owner's low two
phase bits at +0x73. A present object's animation at +0x2D0 supplies progress
`animation[8] / (animation[0x18] - 2.0f)`, with separate float32 rounding.

The callback clears owner +0xA8 and applies the original phase-dependent
sine motion and threshold tests. Phase 2 can create a missing object,
clearing the selected 48-byte resource record's byte at +0x02 first; it then
sets object +0x232 to 2 and clears +0x218 when needed. Phases 0 and 3 can
release a present object at progress >=1. Phase 1 has its separate curve
and creation route, followed by the original unusual null-object condition.
Opaque fields remain offset names; no unsupported engine meaning is assigned.

The complete 174-word original phase helper, 72-word lookup, 33-word index
lookup, 231-word creator and original object-release routine establish their
local pointer/word/byte interfaces. The original bank-request dispatcher and
its 16-word owner relay establish the full-word request result.

`func_15195FB0` in `generated_1C2C60.c` previously declared `void` and discarded
that result in C. Its definition now explicitly returns the **32-bit opaque
handle** from `func_15195DD4`. All **69 compiled function payloads**, pools and
diagnostics in this owner remain fixed; both full-owner padders and its real
Make recipe produce the exact previous complete object. This corrects the
source interface and gives **no additional matching credit**. The downstream
request dispatcher is still unrecovered and is a bounded provider here.

## Frame recovery and retail null behavior

The first complete semantic body already emitted 199 words; only 16 frame/
home references differed, using frame 48 and the object's spill at +0x28.
Declaring the existing object, animation, phase and index locals before the
initialized progress float recovers frame 64 and the original +0x3C object
home. Every word then matches directly. No extra variable, padding array,
volatile access, register directive or frame guard is introduced.

The final phase-1 condition is preserved literally: a nonnull object skips
the final state update, while a still-null object reads address +0x232.
Phase 2 likewise reads that byte after unsuccessful creation. The recovery
does not silently repair these branches. Ordinary unmapped guest fixtures
retain their null-read faults. Eight explicitly mapped-zero guest controls
exercise the literal remaining stores and complete all target-word coverage.
Those controls are **not portable native C or hardware acceptance**. Native
validation excludes null-fault and mapped-zero cases instead of invoking C
undefined behavior and calling it a successful run.

## Focused qualification

Five gates pass freshly in each tools setup before adoption. The first
installed phase check correctly rejects an expected source hash recorded with
Windows CRLF while the tested source text and installed source both use LF.
Their decoded text, raw instructions, objects and full image agree exactly;
only the manifest expected source hash needs correction. The old paired
receipts and semantic artifacts are archived before that correction. After
fixing the one expected hash, **all five gates run freshly in both installed
tools setups** with the corrected manifest. No installed semantic reuse is
claimed after this fingerprint correction.

- **1,580 cases per raw/padded/original stream** compare full retained memory,
  GPR/FPR/HI/LO state, conditions, call sequence and ordered access traces
  between streams. A separate reference checks public effects and provider
  arguments. They cover all four phases,
  both gate bytes, existing/missing handles, creation outcomes, state bytes,
  helper mutations, threshold-adjacent progress, signed zeros/subnormals,
  infinities/quiet NaNs, stack phases and caller-stack owner buffers. These
  buffers do not overlap the target parameter homes or private frame. The actual
  **16-word relay executes** between parent and request provider. All 199
  target words execute; **144 unmapped null faults** and **8 mapped-zero
  guest-only cases** are retained honestly.
- The **22-word table setup** passes three owner/stack arrangements. Both
  actual **four-word JALR windows** pass **100 cases per stream**, establishing
  the configured callback, owner argument and discarded return convention.
- **159 fired access-cut prefix triples** compare raw/padded/original memory,
  registers, ordered accesses, condition and calls, including the real relay,
  sine call-save, caller-stack owner buffer and the null-read boundary.
- Actual SDK32 parent and corrected relay C pass **1,428 valid native cases
  each at O0/O2/O3**, with UBSan, strict aliasing, SSE float32 arithmetic and
  contraction disabled. Independent vectors check every typed output, all
  other owner/object/resource bytes, canaries and every provider argument.
  Arithmetic NaNs compare by class. **152 guest-fault/mapped-zero cases are
  excluded**; guest stack aliases are not claimed natively. Ten controls fail
  output comparison: cached phase, wrong gate/ratio/curve factor/object ID,
  repaired final null condition, wrong counter reset, discarded/narrowed
  relay result and wrong relay bank. The wrong-bank control reads the valid
  typed handle field, avoiding an aliasing violation in the fixture itself.
- Both padders match the isolated target and complete owners. **12 GNU target
  links, 8 relay links and 96 guest rebase runs** cover four independent code,
  callee and data arrangements, low-half carry and another J26 region. Four
  wrong-word/binding outputs fail comparison. The generated padder rejects
  oversized input; the generic padder retains an explicitly unmatched overflow
  body, which is not counted as a matching result.
- `make tools-check` passes. The disposable sibling overlay uses explicit
  required primary fallbacks. The actual sibling tools HEAD, dirty state and
  353 retained dependency hashes are preserved. Routine Claude calls: 0.

Two fixture issues were corrected before the fresh five-gate runs: the short
caller window needed a retained return-boundary instruction and caller-local
RA expectations; generated native event arrays needed nested braces. The
owned compiler was terminated during the repeated brace diagnostic, its log
was losslessly compressed with a verified hash, and native compiler errors
are now bounded with `-fmax-errors=1` and bounded assertion output. These
changes do not alter the recovered C, IDO profile or shared matching tools.

Sine and resource/phase/object services are bounded providers. FCSR, library
internals and gameplay are not qualified. Read-only sibling checks retain
both scene configuration hashes and binary inputs. Neither imports this C
owner; the inspected host path has artifact directories and no Git/CMake
root. No host source/build, Release or runtime acceptance is claimed.

## Independent image and production audit

The private and production full ELF equal an independent literal prediction:
**626 changed bytes, zero exclusions**. Only this target's 796-byte slot and
symbol size 12->796 change, plus **four closed metadata record permutations**
whose complete list is pinned. The relay owner's whole object stays identical.
ELF geometry, every other definition and the fully reconstructed string pool
are checked without excluding symbol or string sections.

The reference recompiles the frozen OLD owner with unchanged OLD guards,
requires its full padded object to equal the frozen production object, and
replaces only the target slot with independently assembled original ASM.
New C does not construct that reference. All **189,088 protected Game data
bytes across 720 owners**, other loaded bytes, profiles and conversion rows
stay fixed. Fresh source-only production Make and live recount establish the
totals above; unrelated objects are checked against the frozen input bank.

Raw target SHA256: `f44b2b2c65b9330318c28395f6d68fa303abee0f6ce139839265ad42eb435725`.
Complete padded owner SHA256: `8427761e94ceef0d66014207404195f22d5a4e27dcc1103de66e2449cf8322eb`.
Production ELF SHA256: `e7e82a5c34c43e7340e9a7f4ad33da5fde84af6a5fedf29dca254ffb29d8b8d1`.

```sh
python3 -m unittest tools.tests.test_game_owner_phase_update_150bf760_match -v
```

Artifacts: `conker/build/game-owner-phase-update-150bf760-private/`.
Tools are committed before the consumer pin. Scoped graph refresh retains
old IDs and qualification metadata; it is not a full-corpus re-extraction.
No push. Codex owns implementation and validation.

## Next work

[Note 2648](2648-game-dual-impact-preset-guarded-match-20261123.md) preserves
the preceding dual impact callback. The next useful shorter candidate is
`func_15195DD4`, the **119-word bank request dispatcher** behind the corrected
relay, VA `15195DD4..15195FB0`. Its complete original is retained. Audit its
callee returns, repeated-search mode and early missing-entry result lifetime
before source fitting. The separate `func_150A6760` decoder stays private and
uncredited. Continue the full 85% goal with 69 more qualified matches required.
