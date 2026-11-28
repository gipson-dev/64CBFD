# Actor matrix extents guarded byte match - 2026-11-28

`func_15184150` in `conker/src/game/generated_1B1600.c` replaces its three-word
zero-return placeholder with the complete **134-word / 536-byte** actor extent
routine. VA `0x15184150..0x15184368`, ROM `0x1B1600..0x1B1818`, frame **64**.
There is no alignment tail, insertion, omission or frame-size adjustment.
**132 words emit directly from C; two expected-word guards preserve one
private model-ID store/reload pair.** All 31 raw/padded neighbors and pools stay fixed.

Actual production: **4,727 / 5,528 (85.51%) total**, **4,054 / 4,855 (83.50%)
Game**, Init 492/492, Debugger 181/181. Zero drift; 801 still different.
Conversion rows and denominators are unchanged. Exactly one new match is
credited; **249 more** reach the active 90% target of 4,976/5,528.
Previous consumer `822b60ca`. The first tools packet `880b55e8` was banked
before a source review identified chained stores with aliased outputs. The
corrected packet `a7fdfc15152c33fa95aa4c0d920be06de678d4b0` was committed
before the consumer; the first packet and its receipts remain intact.

## Recovered source and private slots

The interface is `s32 func_15184150(s32 actorIndex, f32 *x, f32 *y, f32 *z)`.
The routine snapshots the actor's model byte, clears z/y/x in that order, and
returns zero when its matrix pointer is null or the byte gate `D_800C3E90` is
set. Otherwise it obtains the signed record count from `func_1502DB20`.

For each 64-byte position record, it loads x/y/z at +0x30/+0x34/+0x38 and
subtracts the actor coordinates. It conditionally negates negative deltas,
then updates each output maximum in order. The actor matrix pointer is
reloaded per iteration; actor coordinates are not cached across output stores.
The local record view matches these fields without changing SDK `struct255`.

If any output is zero, it falls back to signed model dimensions through
`struct124 *D_800D1C90[187]`: width at +0x1A times `actor->xz_scale`, stored to
z then x from the same product; then (+0x1E + +0x1C) times `actor->y_scale` for
y. Model ID, descriptor pointer and scales retain their original reload points.
The dx temporary is reused for fallback dimensions; dy carries the shared
width product for the explicit z and x stores. There is no FP operand
swap, reassociation, unconditional fabs substitution or artificial local padding.

| Target offset | Raw C | Retail | Preserved local |
| --- | --- | --- | --- |
| 0x44 | sw t8,0x38(sp) | sw t8,0x3C(sp) | Model ID store |
| 0x64 | lw a0,0x38(sp) | lw a0,0x3C(sp) | Model ID reload |

This is one closed four-byte spill pair inside the unchanged 64-byte frame.
Its private slot does not overlap RA or outgoing argument homes. The actor
pointer now emits its retail SP+0x1C store/reload directly. All **44,253
previously committed guard rows** remain an exact byte prefix; only the two
model-ID rows are added. Both padders reject each incorrect expected word,
four effective rejections in total. The discarded actor-pair guards existed
only in the provisional, uncommitted consumer state.

The selected C uses separate full expressions for the opening z/y/x clears
and fallback z/x stores. This preserves retail access order when output
pointers alias and avoids the C99 sequencing problem in the earlier chained
assignments. Reusing dy for the shared product also improves direct matching
from 130 to 132 words. Full native aliases, machine/caller fixtures, padding,
Make, image and rebases were rerun for this exact source; the prior version
is held as superseded and is never the authoritative committed bank.

## Return ABI and one focused review

Retail defines V0=0 on early exits. Normal paths leave an incidental register
value: a descriptor pointer on fallback, or another residual value otherwise.
The sole aligned direct JAL is ROM **0x1B239C** / VA **0x15184EEC**, in the
newly accepted `func_15184DF0`. The prepared-ROM scan finds no aligned literal
function-address references. This is evidence about observed callers, not a
proof excluding every possible computed indirect call.

The C normal path intentionally falls through without a synthesized return.
Its observed caller discards the result. A focused packet-only Claude review
completed once through the existing first-party Pro login, with effective
tools=[] and mcp_servers=[] and zero tool use. Codex independently verified
that every original caller return path replaces child V0 before exposing its
own result, including branch-delay selection of the saved distance. A consumed-
V0 control fails. The exact historical C return type remains unproven.

The exact selected C definition is native-tested with its result discarded on
every path. GCC's `-Wreturn-type` remains a visible diagnostic, demoted from
error **only for the target translation unit**. Provider, harness and link keep
strict `-Werror`; UBSan, aliasing and LTO type checks stay enabled. Each of three
profiles and six controls records its one expected warning. IDO/assembler emit
no warning; six pre-existing duplicate Make-recipe warnings remain. The void
alternative emits 131 words and changes control flow; it is not installed.
Review packet SHA256:
`1722d6e349926773af7753dc8486a95f5315030524bc49ada8c92323f18f057d`.

## Fresh qualification and exact linked acceptance

- Native SDK32: **6,352 cases per O0/O2/O3**, all 187 valid model IDs, twelve
  typed float alias modes, negative/zero/positive counts through eight records,
  signed dimension boundaries, signed zero/subnormals and callback mutations.
  Independent Python binary32 expectations check every byte of **21,112 actor
  bytes, 1,024 position bytes, 132 descriptor bytes**, three output cells, the
  gate and all 187 descriptor-pointer identities. Six semantic controls exit 42.
- Guest: **7,556 cases x four normalized streams / 30,224 executions**, all
  **133 reachable words**, retained unreachable index 30, and **2,136 literal
  fault-prefix quadruples**. The four streams are original GNU-linked retail,
  raw C with the two guards applied, and both complete padded objects.
  Separately, unmodified raw C instructions preserve public state, registers
  and public access order in **6,660 cases**. Raw private stack addresses and
  raw private fault order are not claimed equal. Nineteen alias modes include
  896 guest-only homes/metadata cases, plus guest-only invalid C indices and
  model IDs, three sparse pointer domains and both stack phases. These are
  machine observations, not native C acceptance for invalid typed accesses.
- The complete original **109-word caller** executes all 108 reachable words,
  with its unreachable word 104 retained, and the complete child executes all 133
  reachable words: **4,068 fixtures x four / 16,272 connected executions**, plus
  4,068 raw public checks. All four argument words and all output values are
  checked. Three forced child-return values leave the caller's complete final
  state unchanged. Wrong-z-pointer and lost-saved-distance controls reject.
- The original model-count provider's **25 words and 64-entry dispatch table** are pinned; its LHU and
  optional subtraction establish signed results -4..65535. Its complete
  execution remains opaque. The unchanged 32-word norm provider ABI from
  Note 2747 is reused as an opaque boundary in the connected parent.
- Both complete padders reproduce the frozen before object and the same new
  whole owner. The actual **three-command Make recipe** uses unchanged
  `-O2 -g3 -Wo,-loopunroll,0 -mips2 -o32`. No Makefile, profile, SDK header or
  original assembly change is required. **16 real GNU links** rebase code,
  three globals and the helper, including signed HI16/LO16 seams. All134 words
  and seven binding positions match. Twelve strict-image controls reject.
- Independent frozen-before-C plus original-target-ASM prediction equals
  private and actual production output: the original N93-to-N94 recovery
  changes **380 bytes**, and the corrected store/guard revision changes
  **zero additional image bytes**, with zero exclusions or metadata
  permutation. The first revision's independent original-ASM prediction is
  retained; a fresh correction prediction independently reproduces that ELF.
  Only the original recovery changes the target body/size. All other linked
  bodies, addresses, extents, all **720 protected data owners / 189,088 bytes**,
  guard history and conversion rows stay fixed. ELF SHA256:
  `1225a2a6867e6f14dd36db72788c884129d52dca967947448e6c69fb5ce5e7f4`.
- Five complete packaged tests pass in both closed tools roots before and
  after installation: **20 fresh checks**, equal reports and audited import/
  data closures. Shared `make tools-check` passes. The isolated twin uses
  2,496 frozen dependency hardlinks and eleven independent task-file copies.
  Native Windows Git status and all pinned real sibling files remain intact;
  no Git configuration is changed to reconcile the WSL submodule-status view.

Finite native fixtures do not establish hardware FCSR exception flags,
enabled FP traps, NaN behavior, arbitrary invalid typed accesses or complete
provider/gameplay acceptance. Literal emitted retail words remain exact.

README changes are its two aggregate rows only. Scoped Graphify AST refresh
retains every previous ID and qualification field; this is not full-corpus
extraction. Actual hook-terminal, graph and immutable-bank receipts reside in
`conker/build/game-actor-matrix-extents-15184150-sequenced-private/`.
The earlier `game-actor-matrix-extents-15184150-private/` retains the original
ABI/provider pinning, Claude packet, full-image recovery and rejected-source
receipts. Those unchanged original-code facts are reused explicitly; all
twenty packaged source/guard qualification checks above are fresh for the
corrected source.
A read-only host reference audit finds all 134 original guest instruction
addresses and the original frame/spill slots in `recomp_scene/combined_objpass.c`.
This C/guard restoration needs no behavioral host patch; active host build
selection is not claimed. No host build/edit/launch occurs; Release stays
frozen. No push or subagent is used. N82 `func_1514EECC` remains parked.

Next: qualify **func_151873E4 (127 words)** from the sealed N94 bank. The wider
90% goal remains active.

Fresh packaged-suite durations in seconds: pre-primary 255.563, pre-sibling 264.59, installed-primary 301.455, installed-sibling 294.917.

After the ten pre-install checks, final diff review corrected only the two
CSV description fields, replacing an inherited reference to both spill pairs
with the remaining model-ID pair. Two additional focused tests compare every
CSV field and both complete padded objects; every executable word and the
whole ELF remain identical. The pre-install tools manifest and sealed twin
are retained unchanged. A new isolated twin carries the corrected metadata
for all ten fresh installed checks. The qualification tools commit is
`5992fdb`; its metadata-only successor is `a7fdfc15152c33fa95aa4c0d920be06de678d4b0`.
The twenty package checks all exercise the same corrected C source and exact
two guard rewrites; the description edit earns no additional matching credit.
