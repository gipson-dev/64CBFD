# Note 2593: List-flare renderer recovery and branch-layout boundary

Date: 2026-11-20. Consumer baseline `3177dfd2a8105cd3f2267343b3770bd3f29e1a2f`;
tools baseline `2e0e069aed61fb29c695454ce02c05049bad3c0b`.
Qualified recovery-tools commit: `05ed56bc3c15b99ceb25dd4a375b4ca8131c234d`.

`func_1517E28C` has a complete, tested research C body. It emits **132 words /
frame 120**, while retail has **135 words / frame 120**. It remains **uninstalled
and uncredited**. Production C, original assembly, guards, Makefile and ELF are
unchanged. No normalization or installation route was added for this candidate.

Fresh recount remains **4,578 / 5,527 (82.83%)** total, **3,905 / 4,854 (80.45%)**
Game, zero drift and 949 different. Init 492/492 and Debugger 181/181 remain exact.
The 85% goal remains active, requiring **120 more** at this denominator. Root
README is unchanged because the aggregate figures did not move.

## Recovered interface and state

Owner `conker/src/game/generated_1AB530.c`; VA `0x1517E28C..0x1517E4A8`,
ROM `0x1AB73C..0x1AB958`, a 540-byte slot with no alignment tail. The interface
is `Gfx *(Gfx *commands, s32 unusedCategory)`. Retail stores the unused second
argument into its incoming home. The complete aligned-ROM census finds one
direct JAL at ROM `0x46FD0`, no literal target pointer; computed callers remain
unexcluded. The source call is in `game_45B80.c`. Repairing its pointer-return
prototype and removing integer/pointer casts preserves all **16 raw caller
functions**, their bindings and pools. Three pre-existing Warning 712 messages
remain identical after normalizing only the temporary source filename.

Three two-byte stack copies select flare groups `{0,1}`, element counts `{7,3}`
and falloff factors `{1,30}`. Their four-byte readonly slots are at D_8008D004,
D_8008D008 and D_8008D00C; only two bytes of each are copied. The preceding
selector contains `{NULL,D_8008CFF0}`; D_8008CFF0 is the point `(-73,80,-95)`.
All 32 bytes from that point through the three palettes agree in ROM and the
actual production ELF. The valid native fixture uses selector one and palette
indices zero/one. No speculative NULL/index guard was added to the C body.

The routine captures the list head, clears D_800DDD60, and visits enabled records
at byte +0x30. Flag 0x01 selects the fixed-point projection helper, gated by
D_800DCDD0. A disabled gate skips drawing. Otherwise `func_1517EAAC` projects the
selected point into the record's +0xC/+0x10 floats; sample +0x2A equal to 0xFFFC
selects strength 255, otherwise -1. The other route calls `func_1517EC1C` with
the local sampled-depth word and selects strength 256 when the signed 32-bit
wrapped difference between record depth +0x2C and sampled depth is below 30,
otherwise -1. Both helpers must return exactly one to allow drawing.

Helpers can change flags, sample/depth values, global state and list links.
Flags are refreshed after a helper before mask 0x02 chooses the optional
D_800DD2D0 intensity pointer. A skipped record clears that byte when selected.
An accepted record calls `func_1517E4A8` with the cursor, record, selected group,
count, falloff, strength and optional intensity pointer, and adopts its returned
cursor. The next link is read after helper effects; the captured head is not
reloaded. The large draw helper remains a production stub. Its seven-argument
contract is modeled here, not claimed as restored or gameplay-validated.

## Storage, source experiments and remaining layout

The sampled-depth word at **SP+0x6C** can retain a previous value because the
already-restored helper can return without writing it. The strength carry home
is **SP+0x74**. Neither is initialized speculatively. The strongest candidate
preserves those addresses, the **120-byte frame**, all nine saved-register roles,
the palette bases **SP+0x60/+0x5C/+0x58**, and all seven raw owner neighbors and
their bindings/pools. Source names express recovered roles, not original debug
names. The research owner changes only this body and the adjacent stub's return
type for a consistent pointer-return declaration; neither is installed.

The first source was 126 words with 134 positional differences. Narrowing the
intensity-pointer scope, naming the flag snapshot, inverting the early gate and
recovering the declaration order gives 132 words with **76 positional differences**.
The raw body SHA-256 is
`673fc386318f7a0843b64ca6459e55b846c499258bb536e0c780598798b49af5`.
Counts alone do not describe the remaining work: diagnostic alignment isolates
it to words **45..91**, including early output-address scheduling, strength
constants crossing helper calls, conditional-delay choices, duplicated flag
loads and two branch continuations. Retail word 91 is unreachable in this
corpus. It is not three harmless padding words. No NOP padding, whole-body
replacement or broad guard was used to force a match.

O1 has the wrong 80-byte frame. The existing no-unroll option does not improve
the source; a whole-owner no-constant-register experiment changes neighbors and
is rejected. Literal/const/volatile array forms, explicit switches, loop forms,
alternate predicate forms and measured scope/continuation forms are retained as
private rejected controls. Switch shapes do not recover the retail layout.
The next discriminating work is compiler/source control-flow and scheduling in
that middle region under the fixed frame, homes, ABI and neighbor constraints.

## Fresh qualification and limits

Five tests pass in each tools configuration, with **308 matching imported
Python fingerprints**. The isolated second bundle contains 1,051 files: 347
matching sibling files, 699 primary fallbacks, four task files and one empty
bootstrap. The real dirty sibling preserves its HEAD, full status and **351
dependency hashes**. It was not overwritten or committed.

The bounded big-endian guest screen compares candidate and retail across
**1,024 cases per stream**, including all three helper targets, effectful flag
and link changes, full-byte flags, signed depth arithmetic, both stack phases,
empty/disabled lists, retained depth, helper return values 0/1/2/-1, cursor and
intensity effects. All **132 candidate words / 134 reachable retail words** are
visited. Public memory, helper arguments, results and **all final private and
incoming bytes agree in all 1,024 cases**. Four effective instruction controls
reject an inclusive depth threshold, redirected output home, wrong intensity
mask and missing intensity clear.

Native SDK32 O0/O2/O3 each pass **745 cases** with strict aliasing and UBSan.
Three source controls reject unsigned depth comparison, nonzero-as-success and
stale helper flags. Fixtures normalize pointer identities and serialize the
mixed halfword/byte record fields explicitly. The first depth output is written
before its native C read; later untouched outputs may retain that initialized
value. Guest ambient-stack reads are not claimed as defined portable C. An
initial signed-zero mismatch in the provider fixture and correlated test inputs
were corrected; effective negative controls then pass. These were fixture
issues, not changes to production C.

The complete routines of the downstream helpers and parent are not executed in
this screen. Fault-prefix, arbitrary alias, FP-exception, hardware and gameplay
parity are unproven. This behavioral recovery does not pass the missing raw-word,
padder, actual-Make, independent-image or installation gates and earns no match.

`make tools-check` and the fresh actual-ELF recount pass. All **2,135 frozen input
hashes** were reverified before documentation/pin changes. Production ELF SHA-256
remains `165cbb8165b7a082361604cf437faaad940f0c54221b2bfcdfe0116b07397582`.

Claude auth discovery reports signed out; **zero model requests were attempted**.
No auth/provider/billing configuration was changed. Native Graphify update
refused to shrink the graph and retained all 68,694 prior IDs; scoped research
AST/reference merge is used, with zero API cost and no full-corpus claim.
Local commits only; no push or host/save/Release changes.

Reproduce the five focused tests from the prepared consumer root:

```sh
python3 -m unittest tools.tests.test_game_list_render_1517e28c_recovery -v
```

Retained receipts and rejected screens are under
`conker/build/game-list-render-1517e28c-private/`. Continue this same function's
middle-region recovery, then run every adoption and image gate before credit.
