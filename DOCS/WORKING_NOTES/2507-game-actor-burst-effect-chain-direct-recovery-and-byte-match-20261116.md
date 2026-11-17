# Actor burst effect chain direct recovery and byte match - 2026-11-16

`void func_151A6C90(u8 *actor,u8 slot,s32 context)` replaces the zero-return
placeholder with the complete actor burst and effect sequence. All **154
instruction words / 616 bytes emit directly from C**, preserving frame **0xA8**.
The complete **156-word / 624-byte slot** includes its two unchanged alignment
NOPs. **No guards, insertions, omissions, dummy locals or register bindings**
are introduced. VA151A6C90..151A6F00, ROM1D4140..1D43B0; actual code ends151A6EF8.

Accepted production total **4,528 / 5,514 (82.12%)**, Game **3,855 / 4,841
(79.63%)**, Init492/492, Debugger181/181; zero drift, **986** still different,
**159 further matches** to the active 85% goal. Conversion remains
5,514/6,048 (91.17%), 86.19% of bytes. Root README changes only aggregate rows.

## Source, interface and fitting

The original snapshots actor floats at +0x14/+0x18/+0x1C before its later null
branch. The recovered C retains that order and snapshots the point separately
from the burst packet. A mapped non-null actor is the normal input domain;
the later branch is not a promise of portable null safety.

The 92-byte packet follows the already recovered `func_151A6F00` interface,
using a typed three-float position view at the identical offsets. It defines
**86 bytes**; six padding bytes at02/03,12/13,5A/5B stay indeterminate. Count is
`((u32)func_150ADA20() & 3)+6`, duration80, radius60, signed angles0/-63,
ranges255/80, speed0, speedRange35, alternate values10/40, zero direction,
mutable D_800A8DB0 scale, scaleRange0.5, -1/-1/-2/4 values and footer0/0/50/25.
The first submission is `func_151A6F00(&packet,0,slot,context)`.

The remaining original calls are `func_151D5334`, `func_151D3FF4`,
`func_151D5514`, `func_151541B8` and `func_151D5404`, with the saved point and
exact mixed integer/float o32 arguments. The float RNG precedes the second
integer RNG; the fourth effect receives `sample*4+12`, scalar bits3FD20C49,
unsigned remainder `%56+200`, zero, slot and context. Returned values are ignored.
Provider mutations of the separately exposed point and retained packet remain
visible to later calls; the initial actor position is never silently reread.

The first complete candidate emits153 words. The existing actor-burst packet
note1352 explains the separate integer-literal floating-zero source form.
Changing only `packet.speed=0.0f` to ordinary integer `0` recovers154 words and
leaves two stack-home differences. Declaring the real random word before the
real float sample recovers the original sample home and every instruction.
Three candidates were compiled; no ABI/volatile/profile workaround was needed.
Selected raw SHA256:
`5806ac3e53fbdd1ebcaaaa5e59fc868b849324284899480d70355ffc40dc8c17`.
Complete retail slot SHA256:
`52432b3ee110341b2b45c2c12a8911f78d8ae8f2e6b42693a3399dd8597db6a7`.

## Fresh qualification and scope

All four maintained tests pass in primary tools, the isolated sibling-tools
overlay and installed production at the same six task-file fingerprints.

- Independently assembled original154 words and all **11 original bindings**
  agree literally with compiler output. Both real complete-owner padders keep
  every code word, two alignment NOPs, 616-byte symbol extent, all14 neighbors
  and pools. All165 raw-word/binding corruption controls reject. A first pool
  check compared absent compact `.data` with GNU's empty `.data`; the section
  audit established zero bytes/no relocations. Compact-to-compact and padded
  production-to-padded production comparisons now retain the proper boundaries.
- Guest reference: **560 cases per retail/raw/strict/layout stream**, all256
  slot bytes, wide incoming slot words, two stack phases, unsigned RNG boundaries,
  contexts and16 provider mutation modes. Public actor/global state, every call
  argument and all86 defined packet bytes agree. Five semantic defects reject.
  **150 of154 instruction words** execute; the four-word unsigned-conversion
  fallback is unreachable for the proven `%56+200` range. Alignment is not
  claimed as executable code.
- Native32: **560 cases each at O0/O2/O3**, SDK types, strict aliasing and UB
  traps. All64 actor bytes, coefficient/marker, defined packet bytes and nine
  calls agree. Six broken semantic bodies compile and exit3; all nine runs have
  their expected outcome. Incoming wide slot values are narrowed at the C call
  boundary; native tests do not claim raw o32 incoming-home identity.
- **Twelve independent GNU links** compare both whole-owner padders and the
  independently assembled reference over four code/data layouts, including
  HI16 carry. Raw bytes and binding ownership match before relocation.
- The complete **252-word** original `func_1507D754` is verified literal in
  production. Its authentic four-word call window at1507DADC executes the
  complete constructor in **128 cases per stream**, forwarding actor fromS0,
  slot255 and context1. Both wrong-slot/context controls reject. Execution stops
  on return at1507DAEC before the caller's next instruction; complete parent
  execution is not claimed. The exit marker raises before any marker execution.

The actual315-word burst consumer and complete integer/float RNG helpers are
literal retail in production; this suite bounds their effects rather than
requalifying those systems. Normal mapped/disjoint-stack inputs, modeled helper
mutations and defined packet fields are the semantic scope. General alias/fault,
hardware FCSR, padding initialization and gameplay acceptance are not claimed.
Literal direct instruction identity is a separate complete-code check.

## Production and retained evidence

Predecessor consumer5f924d0b / tools7ca1844. The1,420-input initial snapshot
reuses only verified immutable snapshot files, never live worktree hardlinks.
The1,426-input maintained freeze includes six tools files. A caller-wrapper
local name shadowed the imported module on its first maintained run; the failed
snapshot/results are retained. Two corrected wrapper files were copied into
an explicit second snapshot with1,424 immutable links; source semantics,
private passing fixtures and acceptance gates were unchanged.

The shadow runner initially required its private guard-file path even for zero
new guards; that file now contains the unchanged frozen CSV bytes. Its completed
five-command actual-Make receipt is retained. The strict predictor then correctly
rejected a624-byte payload where a616-byte symbol body was required. The final
prediction declares only the616-byte code payload and retains the two alignment
words under the complete-image comparison, with no exclusions. The completed
shadow build is reused only after frozen-input and complete compact/padded-owner
checks; the production Make below is a fresh source build. The exact qualified
source retains one terminal blank line, the sole explicitly reviewed whitespace
diagnostic at commit time.

Actual Make shadow and production build compile the C; no prebuilt object is
installed. Exactly source, owner object and ELF change; **1,423 frozen inputs
remain unchanged**. All other6,050 bodies and all6,051 addresses remain fixed;
only one of698 objects changes. Every14 owner neighbor, normalized pool, guard
CSV byte, Makefile, profile and conversion row remains unchanged. Complete
production ELF equals the independent prediction: **502
changed bytes / zero exclusions**. All **20,289 named definitions**
agree except target extent616, with explicit metadata accounting and effective
symbol/name, protected-data and target-word corruption controls.
All **189,088 protected bytes /720 owners** remain exact.
Production ELF SHA256: `f3fc43e22cd382ce4a1749b95ea990ab289340c9c27c5e1591c49a67ea6a89ba`.

Prepared qualification needs the retained immutable snapshot and a fresh owned
output folder supplied by `CBFD_EFFECT_CHAIN_WORK`. Run
`python3 -m unittest tools.tests.test_game_effect_chain_151a6c90_recovery -v`.
Receipts: `conker/build/game-next-151a6c90-private/adoption/`.
The sibling's2,434 changed paths and339 checked dependency files remain
unchanged; actual overlay/sibling/primary imports are sealed separately.
At `64CBFDOGL` only `.codex` and `recomp_scene` remain, with no source checkout
to synchronize. No host, Release or save changes; zero Claude calls, no push or
dependency upgrade. The native Graphify update refused a smaller replacement
and preserved all63,925 prior IDs. A scoped six-file AST merge retains every
prior ID and adds the verified tools-to-function reference; no full-corpus
re-extraction is claimed. Tools are committed before the consumer pin.

Next inspect `func_151AABC4` from the actual unmatched list. The total85% goal
remains active.
