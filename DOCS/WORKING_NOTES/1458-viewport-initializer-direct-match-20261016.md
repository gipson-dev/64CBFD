# Viewport Initializer Direct Match

Date: 2026-10-16. Consumer predecessor **3f6b2735**, tools predecessor
**54aff68**. Complete the recovery banked in
[Note 1457](1457-viewport-initializer-recovery-and-matching-boundary-20261016.md).

## Installed Recovery

func_1501A8C0 in conker/src/game_476D0.c now emits all **373 words / 1,492
bytes directly from C**, VA **0x1501A8C0..0x1501AE94**, ROM
**0x47D70..0x48344**. Preserve the original **0x48 frame**, argument homes,
saved-register lifetimes and sine home **SP+0x34**. No new guards, padding,
private pools or compiler profile. Retain the existing target-only no-unroll
selection for func_1501A39C and all ten other normal-profile neighbors.

```c
void func_1501A8C0(s32 index, s32 layout, s32 depth, s16 transferFov);
```

Replace the typed zero-return stub with real dimension/FOV/aspect setup,
signed origin pairs, clip bounds, temporary SDK Vp construction, ordered page
copies, bounds/clamp calls, projection update and final byte publication.
Name only proven fields in the existing **0x180** record. The flag uses its
signed low halfword; depth shifts as a full signed word before narrowing.
Keep live base/page reads and **!page**, including arbitrary nonzero pages.

All **eleven functions / 1,088 retail words** in this owner now compare exact
against the normal linked ELF. This includes previously exact 19-word
func_1501A680 and 38-word func_1501A6CC; neither was changed for this match.

## Source Lifetimes And Sequencing

The prior candidate remains a historical **49-difference** recovery, not a
retroactively exact result. Naming three real values, **referenceWidth,
referenceAspect and selectedAspect**, while preserving the original grouped
divisions/products recovers the FP value coloring. Declare sine before the
reused trigValue and finish each cosine call in its own statement before
reloading the extent. This leaves one commutative address word; index-first
unsigned address addition in the final clamp arguments recovers that word.

The final raw object SHA-256 is
**a1348f447d175e2d072219ef8cecaad9ae4728f797816ecb5e5d7d09268732d4**,
with all **34 relocation bindings** pinned. The three-value unsequenced form
has seven differences, or three with sine declared first; sequencing reduces
that to one, and the index-first address expression reaches zero. Renaming
the reused angle/cosine carrier to trigValue retains the same exact object.

Native qualification found a real C evaluation-order gap in the old draft:
`sine / (extent * cosf(angle))` permits GCC to load extent before the callback.
Case **385**, public word **4383**, produced **BAE07038** instead of
**BAE6C2B4**. Explicit cosine statements fix the source contract as well as the
IDO fit. Keep the old unsequenced source as an effective exit-21 negative;
do not weaken the live-base callback test to accept it.

## Fresh Qualification

All **nine pre-installation tests pass in 94.216s**. After the normal build,
all **12 final tests pass in 159.799s**:

```sh
python3 -m tools.experiments.game_viewport_initialize_lifetimes --prelink
python3 -m unittest tools.tests.test_game_viewport_initialize_match \
  tools.tests.test_game_viewport_initialize_connected \
  tools.tests.test_game_viewport_initialize_native \
  tools.tests.test_game_viewport_initialize_installed -v
make -C conker -j4 build/conker.us.elf progress.csv
make -C conker match-progress NON_MATCHING=1
make tools-check
```

- **1,144 three-way guest cases**, including two invalid-conversion prefixes,
  compare retail, direct raw C and normally padded C against the independent
  grouped float32 reference. All **373 root words** execute. Compare complete
  literal private RAM, GPR/FPR banks, ordered access/events, call packets,
  current instruction and delay state, not a register-permuted result.
- **216 three-way callback cases** assert positive fired gates for live
  base/page/FOV mutations and cached pending angles at two stack phases.
- **475 native32 cases each at O2 and O0**, UBSan and no fwrapv: separate
  typed caller/body/provider units, actual bounds/clamp C, SDK Vp offsets and
  all **6,936 public words plus canaries**. Normalize endian lanes by known
  numeric types and only the declared pointer fields. Seven controls produce
  actual exit-21 output or exit-22 protocol mismatches, never signals,
  compiler failures, missing memory or sanitizer failures.
- **108 three-way connected-chain cases** execute actual ELF/retail-exact
  FOV transfer **99**, sine **104**, cosine **88**, bounds **44**, clamp **87**,
  wrapper **33**, projection parent **129** and child **38** words, **622
  static helper words** total. Check nested ABI packets and independent
  public reference output, plus literal private state. Angle and two SDK
  leaves remain bounded providers; SDK callback modes 0/1/2 are synthetic
  contracts, not natural runtime observations. Not every helper branch is
  claimed executed.
- GNU-assemble the complete original **95-word func_1501A220** against ROM.
  **12 actual caller cuts** preserve the real A3 delay-slot zero, two layout
  routes, live count reload and post-call index increment. This is not full
  startup or caller-loop execution.
- **1,962 fired three-way memory-fault prefixes** cover every executed root
  and connected bounds/clamp access in six fixtures at two stack phases.
  Preserve literal memory/register/event/PC/delay state before each access;
  this is not hardware exception or portable C fault emulation.
- Reject every **373** raw-word corruption, **34** binding corruptions plus
  an extra, private pools and a stale source anchor. Three independent
  original GNU links and three C rebase links compare all words with HI/LO
  carry and call relocation. Preserve both owner-selection paths.

Test-fixture fixes were explicit: include the caller's join address before
raising its boundary, reuse NEG.S semantics for real trig, and map the SDK
provider's explicit alternate bank. The historical recovery oracle remains
unchanged. None of those failures required a production fix or a weaker gate.

## Whole Image And Progress

Independently reproduce the predecessor before installation, then predict all
**3,257,636 ELF bytes**. Exactly **1,181 bytes** change: **1,157 code bytes**,
**two symbol-size bytes** for extent **28 -> 1,492**, and **22 metadata bytes**.
The latter are two closed adjacent symbol/string swaps:
D_8008630C/D_800894F0 and D_8003CA48/D_800C3D48. Pin each original record,
name/order and definition; no definition changes or metadata exclusions.

The normal build exits zero and equals the first complete prediction:
**1e37e75c0cd1215a3e8a2fc9ae4c0b9ed38a56d59a6b5e2d1c5ef03334632096**.
Installed owner SHA-256:
**67b0a4150c68cdea5ffb076231703f799925d0955a7e5fc6f2eabfefc852fff3**.
All **130** live inputs are checked, **128 unchanged**. Makefile and guard
bytes remain identical; protected data remains **189,088 bytes / 720 owners /
zero differences**. Source/image/helper/caller/metadata corruption and both
fixture-stage controls reject unknown successors. The existing
generated_12D630 duplicate-recipe warning remains unchanged.

Fresh official matching: Game **2,935/4,828 (60.79%)**, total **3,608/5,501
(65.59%)**, different **1,893**, zero drift. Init stays **492/492**, Debugger
**181/181**. Conversion remains **5,501/6,044**, **86.04% bytes** because the
old stub already counted as C. Root README changes only the two matching rows.

## Advisory Disposition

One justified, packet-only advisory addressed the unresolved F16/F14 lifetime;
one attempt, one completed turn, no retry or second call. Fresh Claude 2.1.218
auth was claude.ai/firstParty/Pro with no provider overrides. Safe mode,
disabled tools, strict MCP and no persistence initialized tools=[] and
mcp_servers=[]; output records no tool use. Default Opus 4.8 was retained;
result metadata also includes internal Haiku usage, not a client model switch.
This is a tool-free receipt, not a filesystem sandbox or proof of correctness.

Ignored packet/answer/receipt live under
conker/build/game-viewport-initialize-lifetimes/. Packet **1,905 words**,
SHA-256 **229e6a88da9e96d8a2fe9fe389c290af81ea53a60e5120f48cd211437b60f5ee**.
Reject suggested reassociation `a*(b/c)` to `(a*b)/c`: it changes float32
rounding and retail's operation order. A measured a=b=c=**3DCCCCCD** witness
returns **3DCCCCCD** versus **3DCCCCCE**. Half-constant/inline-cast suggestions
repeat prior controls and are not adopted. The impossibility caveat is not
proof; the independently compiled three-value/sequenced fit is directly exact.
No advisory suggestion is accepted by agreement.

## Bank And Next Target

Tools **34c77aeb383e45817247220df04865b4af4690bf** banks all seven new files
before the consumer pin. Both copies pass seven Windows AST checks and eleven
shared padder tests: active **0.032s + 0.022s**, older mirror **0.031s + 0.021s**.
Consumer tools-check passes. All seven task-file pairs match. Preserve older
mirror HEAD **ddbdd16b53ce60b054fb6e11bf0649a41f48375a**, all **914** initial
dirty-file hashes and **921** final dirty paths; do not commit/reset it.

Next: **func_1501C880**, still a zero-return stub in
conker/src/game/generated_49D30.c: **239 words / 956 bytes / frame 0x28**,
VA **0x1501C880..0x1501CC3C**, ROM **0x49D30..0x4A0EC**. Recover display-list
capacity fallback, graphics-task construction, blocking message submission,
optional page flip and frame-counter update, including its actual
func_1501A39C call. Recover the interface from callers before naming arguments.
Preserve that owner's existing no-unroll
profile and unrelated restored functions. Timing's **141 differences**,
wider Game/additional-source queue and gameplay acceptance remain open.
No push, host-port change or frozen Release action.
