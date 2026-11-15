# Motion effect literal recovery and guarded match

Date: 2026-11-15. This closes the private recovery and frame boundary in
[Note 2468](2468-game-motion-effect-private-recovery-and-frame-provenance-20261115.md).
`func_150C2C00` is installed as semantic C in `conker/src/game_EF410.c` and
matches all **243 words / 972 bytes**, VA **0x150C2C00..0x150C2FCC**, ROM
**0xF00B0..0xF047C**, with no alignment tail. Its original **0xE8 frame**,
saved-register set, packet at **SP+0x94**, heading at **SP+0x8C** and RA save
at **SP+0x6C** are restored. Twenty-two checked word normalizations complete
the match. No word is inserted or omitted.

The fresh actual production recount is **4,503 / 5,514 (81.66%) total**, Game
**3,830 / 4,841 (79.12%)**, Init **492 / 492**, Debugger **181 / 181**, zero
address drift and **1,011** still different. **184** further matches are
required for at least 85%; the goal remains active. Conversion counts and
converted-byte percentages are unchanged.

## Recovered source and compiler cause

The routine accumulates emission attempts in owner float **0x28**, checks the
motion X/Z squared magnitude, and consumes a unit after each accepted or
rejected heading attempt. Successful construction copies the four-byte heading
to result **0x160**; failure skips the copy. The late owner bytes, exact random
call sequence, unsigned duration/color remainders and live accumulator reloads
remain semantic C. The 72-byte constructor packet has **69 defined bytes**;
bytes **0x35..0x37** remain uninitialized. Existing neutral field names are
retained, with a local comment explaining this variant's mode-four word.

The key fit was recovering the twenty numeric float literals, instead of
representing the coefficient block as twenty unrelated mutable externs.
IDO emits an **80-byte `.rodata` pool** identical to retail ROM
**0x244D80..0x244DD0**, original labels **D_800A02C0..D_800A030C**. Every float
is checked bit for bit, pool SHA-256
`e4b3618e3af815343708f5f38ed632631a9b4a5b54ecedebdefdd52e14b63f12`.
This removes the saved coefficient-address roles, including S8, and recovers
the retail duration/color range registers and heading-pointer lifetime.

Reusing the existing draw scalars for the initial motion gate removes three
unneeded locals. Separating float-returning calls from their following
arithmetic eliminates an anonymous reservation. Real declaration order and
the accumulator pointer's lifetime recover the original homes and extent;
there is no arbitrary padding object, assembly body or physical-register
binding in the C. The compiler profile remains the existing **O2/g3/mips2/o32**.

A fresh fingerprint-locked owned CFE/UOPT/UGEN trace records reservations
**0 -> 88 saved -> 112 after 24 outgoing -> 232 after 120 locals**. CFE's
M reservation is **112 bytes**, UOPT's **120**, versus **128 / 136** in the
prior private source. All producer/driver exits pass, and both deliberately
broken observer logs are rejected. Normal and observed code, relocations and pools agree;
complete debug-metadata object identity is not claimed.

## Literal ownership and production guard

The original coefficient owner is `conker/asm/data/244D60.rodata.s`, an
allocated `.rodata` block. The valid C domain keeps implementation literal
storage fixed. The old private mutable-extern fixture remains available with
its original behavior; its deliberate coefficient writes are not credited as
valid native executions of the new literal source. Owner, motion, selector,
allocation and helper-side-effect mutations remain qualified.

The compact owner's only pool is the target's exact 80-byte literal block;
all 17 non-target function bodies and bindings are unchanged. The existing
padder maps compact pool offset zero to retained **D_800A02C0**, preserving
all twenty offsets. No new constant data is emitted into the production ELF.

`tools/check_motion_effect_150c2c00_pool.py` now runs in production after the
assembly postprocessor and before padding. It checks the ELF type, pool size,
values/order and non-writable section flag, complete target body hash and all
58 relocation bindings. It also rejects pool references from another function.
The Makefile adds one conditional check line and enables the checker and pool
base only for `game_EF410.c.o`; other compiler profiles are unchanged. Every
old Makefile byte is retained outside that conditional insertion and appended
owner configuration. Future changes to this owner's pool require explicit
requalification rather than silently discarding changed C literal values.

Twenty-four corrupted-object controls reject changes to each coefficient word,
the function body, pool writability, an unrelated function's pool reference and
a target relocation. The actual production build executes the checker and
prints `verified: true` before padding.

## Twenty-two checked words

Raw body SHA-256:
`fea76614f958e051351b365170fabaa1bf6651de21e4e6e14738686ab5bb7111`.
The full raw body and relocation set are pinned before normalization.

| Group | Words | Qualification |
| --- | ---: | --- |
| Owner/motion roles | 9 | Closed S2/S3 role permutation and independent original-register save ordering; all save homes and restores retained |
| Motion FP scratch | 4 | Initial Z scratch F20 to F2 and norm-result F0 to F12, with dead-use/next-definition and no-argument-call boundaries checked |
| Setup schedule | 3 | Distinct constant destinations with identical symbolic block effects |
| Packet FP scratch | 6 | One closed F10/F16/F18 cycle, complete stores and no subsequent use before the no-argument float-returning call |

There are no frame, save-set, loop-count or operand-order substitutions.
Eighty corrupted-word/relocation controls reject, as do twenty direct pool-word
controls. The two guarded pool loads retain their exact relocation addends;
the declared retail pool base supplies the final addresses.

## Semantic, native and caller checks

- **864 finite cases / three streams** compare original, raw C and normalized
  MIPS. They cover accumulator and motion boundaries, heading acceptance and
  rejection, live helper mutations, two stack phases and fixed/null/mixed
  allocation outcomes. There are **155 emissions / 87 successful copies**,
  including partial-success patterns. All **241 reachable target words** and
  the complete original **22-word polar helper / 11-word memcpy** execute.
  Two fixed-nonzero divisor `break 7` words remain in the matched extent.
- **Eight guest alias cases** cover heading copies overlapping owner mode/
  timer bytes, the accumulator and motion components. These are separated
  from native object-layout acceptance. Read-only coefficient and callee-private
  frame aliases are outside the valid C domain.
- **146 exceptional cases / two streams** compare original and normalized
  modeled state. Distinct quiet-NaN motion operands retain original F12
  payload **7FC00001** under an explicit left-selection rule and **7FC30002**
  under an explicit right-selection rule. Physical FCSR/traps and full 64-bit
  floating-register semantics are not claimed.
- **481 fired access prefixes** compare registers, HI/LO, memory, traces,
  calls, packet/copy observations, PC and delay-slot state. Every injected
  boundary must actually fire. This is instruction-state evidence, not a
  portable-C fault guarantee or a hardware EPC claim.
- SDK32 native **O0/O2/O3** each execute the actual C across **864 cases** with
  UB traps and **eight effective source controls**. Checks include the 160-byte
  owner, 64-byte motion and 448-byte result backings, all defined packet bytes,
  call script, copy counts and live selector/marker state. Native exceptional
  payloads and guest aliases are not credited.
- The original **45-word `func_15149264`** parent passes **576 cases / three
  streams** through **D_8008A4E8[18]**, JALR **0x151492B0**. Its update route
  visits 30 words, covers timer-decrement choices and post-callback owner/timer
  reloads. Wrong table-slot and argument controls reject. Expiry/free routes
  remain outside this caller qualification.

Random generation, motion/angle helpers, trigonometric providers and the effect
constructor remain bounded models. Only the specifically identified original
polar, copy and caller instructions are connected; gameplay acceptance is not
claimed by these tests.

The native helper's optional API preserves default behavior: its original
576-case mutable-extern harness was freshly rerun, retaining the identical
generated-source and all three executable hashes. Reused helper stdout retains
historical private/two-stream labels; the enclosing stored reports correct the
installed state and three-stream caller count. These labels do not determine
match credit. Routine Claude calls: zero.

## Padders, actual Make and strict production image

Both padders process the complete **18-function owner**, preserve its **17
neighbors** and emit no additional pools. **Twelve GNU links** compare both
padders with independently assembled original code across four code/data
layouts, including HI16/LO16 carries. Init `memcpy` moves with the Game code
in these rebases so each JAL remains in its 256 MB region. All **44** corrupt
CSV expected-word controls reject. The manifest preserves every old CSV byte
and appends exactly 22 target rows.

The independent **six-command owner Make replay**, production build and
production audit pass. Actual production ELF equals the independent prediction
byte for byte. Its **754 changed bytes** are completely accounted for with
**zero exclusions**, including one closed metadata ordering swap between
**D_800A02C0 / D_8009FEC0**. Every named definition remains fixed except the
target extent, which grows from the 12-byte placeholder to 972 bytes.

All **6,051 function addresses** remain fixed. Of **698 production objects**,
only `game_EF410.c.o` changes; its section differences are exactly `.text`,
`.rel.text`, `.symtab` and `.strtab`. Its three added names are the intended
pool base, `func_1514373C` and `memcpy`. All **80 headers / 82 include inputs**
and the conversion CSV remain fixed. Of **844 frozen inputs**, only source,
Makefile, guard CSV, owner object and final ELF change; **839** remain identical.

All **189,088 protected data bytes / 720 owners** remain unchanged, SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.
Production ELF SHA-256:
`98936610b7d62b2ec3378dc8da56ac61f14e426bf0c76c9ef2154539a0afd573`.
The fresh recount uses this actual production ELF.

Final complete suites pass before installation in **53.797 seconds**, through
the sibling overlay in **51.895 seconds**, and installed in **49.213 seconds**.
`make tools-check` passes. Earlier screening runs remain diagnostics; these
receipts include the production checker. The existing duplicate
`generated_12D630` recipe and line-ending notices remain; no broad warning or
line-ending cleanup is included.

## Commit, graph and next target

Tools commit **`801108f29d429523171a8e8d7a215695e5e43df5`** precedes the
consumer source/configuration/docs/pin commit. The eight-file ignored overlay
preserves sibling HEAD **`ddbdd16b53ce60b054fb6e11bf0649a41f48375a`**, all
**2,434 Windows-Git dirty paths**, status SHA-256
`a3712de44f2fc37079df4a789a5015f134f6ab977a2c2da90a3fde1851606cd9`.
Scoped Graphify AST refresh covers eight files, retains all **61,656 old IDs**
and records **61,690 nodes / 115,676 links**, zero lost IDs. It is not a
full-corpus extraction. Evidence and the immutable pre-install receipts remain
under `conker/build/game-motion-effect-150c2c00-match/`.

Root README receives only its two aggregate matching rows. The host path still
contains only scratch `.codex` / `recomp_scene` directories; no host import or
build is made, and frozen Release is untouched. No push.

Next target: **`func_150C3574`**, **264 words / frame 0x38**, in the same owner.
Recover its complete behavior and caller ABI, then qualify the owner/pool
interaction, guest/native state, actual padding, Make and strict image gates
before counting another match. The 85% goal stays active.
