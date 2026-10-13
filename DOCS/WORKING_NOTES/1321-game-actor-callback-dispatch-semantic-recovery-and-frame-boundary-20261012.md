# Game Actor Callback Dispatch Recovery And Frame Boundary - 2026-10-12

## Scope And Current Result

Resume the full Game matching goal from consumer `7dbe2083` / tools `9691502`
and [Note 1320](1320-game-actor-matrix-clear-byte-match-20261012.md).
Both active checkouts were clean. Inspect the focused graph, complete81-word
original, actual caller, helper interfaces and unchanged O2/g3/MIPS2/o32 profile.
Preserve the independent older tools checkout, private inputs and frozen host Release.

Target [func_150345E4](../../conker/src/game/generated_61490.c):
VA0x150345E4..0x15034728, ROM0x61A94..0x61BD8,81 words/324 bytes.
Replace the three-word zero-return placeholder with the complete semantic void
dispatcher. Its real differences fall78->8; all73 non-frame words now match.
**It is still non-matching:** source frame0x28 versus original0x20.
Do not add frame guards, count this as matching, or move past its remaining task.

Add only local helper/global declarations and correct the direct caller's
old `s32 func_150345E4();` to `void func_150345E4(s32 slot);` in
[generated_58F80.c](../../conker/src/game/generated_58F80.c).
Keep s32 returns for the two still-unconverted helper definitions; their scalar
results are ignored. No shared header, compiler/profile, layout, guard or data edit.

## Semantic Contract

- Compute the0x32C-byte actor address with low32 index arithmetic. A null buffer
  at+0x1D4 returns before reading active word0, state byte5, type byte4 or disable.
- If full word0 equals1 or byte5 equals7, call func_1503453C(index). Re-read word0
  after that call; if it now equals0x22, call again. These are independent tests,
  not an else-if chain. Buffer eligibility is not checked again after a helper.
- Only then capture the unsigned type byte into a signed32 local. Types4,0x70,
 0x7B,0x60 select their original callbacks. Other type bytes have no final call.
- Type4 checks D_800BE616 once. If zero, submit `(0,index,9,0)` then
  `(0,index,4,0)`, even if the first command changes the disable byte.
- Type0x70 passes the actor and10/11 to func_15034EB4. Type0x7B calls
  func_150F1A00(actor); type0x60 calls func_150DFDA4(actor).
- Keep the full incoming index home, repeated argument reloads and actor pointer
  saved/reloaded at frame+0x18 around dispatch. Guest-only home overwrites qualify
  those emitted reloads; they are not portable C permission to overwrite a frame.

## Exact Open Boundary

| Offset | Source Word | Original Word |
| --- | --- | --- |
| 0x000 | 27BDFFD8 | 27BDFFE0 |
| 0x008 | AFA40028 | AFA40020 |
| 0x00C | 8FAE0028 | 8FAE0020 |
| 0x054 | 8FA40028 | 8FA40020 |
| 0x088 | 8FA40028 | 8FA40020 |
| 0x0D8 | 8FA50028 | 8FA50020 |
| 0x0F0 | 8FA50028 | 8FA50020 |
| 0x138 | 27BD0028 | 27BD0020 |

RA stays at frame+0x14 and actor at+0x18. Incoming index home is incoming SP+0
in both bodies: frame+0x28 source and+0x20 original. All other opcodes, registers,
immediates, branches, labels, helper relocations and delay slots match. No emitted
target access uses the extra reserved upper8 private bytes.

Measured controls: ordinary switch81/frame0x28/23; original case order reduces
that to12. Explicit s32/u32 type makes81/0x28/8; u8 type gives13. Address forms,
signed/unsigned/old-style index, separate assignment, declaration order, register
and const controls do not recover the frame. Unsupported restrict syntax is
rejected, not fitting evidence. Volatile/eager index variants82/frame0x20 change
the read schedule; no acceptance. If-chain81/0x20/33 and label dispatch81/0x20/25
have the right frame but wrong comparison/scheduling shape. Profile changes,
narrow/word-wide access substitutions and frame-word normalization are excluded.

## One Focused Advisory

Decision: source-level cause/resolution of the otherwise exact function's extra
eight frame bytes. Budget1, attempted1, completed1, no retry. Existing Claude
Code2.1.218 auth confirms claude.ai/firstParty/Pro and no API/provider overrides.
Safe mode, tools disabled, strict MCP selection, plan permissions, no Chrome/
skills/persistence: effective init tools=[]/mcp_servers=[], no tool/server use.
Keep the existing default model, emitted claude-opus-4-8; no billing/model switch.

Ignored packet/answer/receipt:
`conker/build/game-actor-callback-dispatch-review-20261012/`.
Packet SHA2566dec3269f188c39eb1594690e75f155c4f97ddb487ed34fd5d9fb9abdc132b8e.
One result turn reports input2/cache-created4898/output9450 tokens and
total_cost_usd0.288523; that CLI field is not a verified billed API charge.
No repository access or edits occurred. Prose mentions a plan file, but the
effective tool-free receipt records no such operation; do not treat it as evidence.

Reconcile hypotheses independently: explicit default break/return remains
81/frame0x28/8; shared callback pointer worsens to81/frame0x30/12. No accepted
fix. The reviewer's switch-lowering explanation remains an inference, not a
confirmed compiler defect or proof no semantic source can match. Retain the
eight-word boundary and investigate actual frame allocation next.

## Qualification

```sh
python3 -m tools.experiments.game_actor_callback_dispatch_candidates
python3 -m unittest tools.tests.test_game_actor_callback_dispatch_recovery -v
```

Seven pre-install tests pass in82.777 seconds and seven final installed tests
in83.940 seconds, no skips.

- 65,536 isolated guest cases cover all256 types, full-word index extremes,
  ordered gates, provider mutations, disable changes and two stack phases.
  Add24 incoming-index/actor-home overwrites and36 non-seven flag cases.
  Public storage/calls agree with an independent reference; all81 words execute.
- Logical access events rebase source private-frame addresses by8 below the
  incoming SP; incoming parameter home remains absolute and unchanged. Terminal
  GPR/FPR/call state agrees. **This is not physical stack-layout or hardware parity.**
- All65 own-access fault pairs fire, with completed controls and provider accesses
  excluded. Compare public prefixes and logically rebased private accesses/SP,
  not literal private RAM/physical fault state. Null-buffer minimal storage passes.
- Native32 O2/O0 runs the unchanged source for32,768 cases each, complete26-actor
  backing and ordered argument traces. Include byte flags1/0x87/255, not only0/7.
  Four fresh cached-type, else-if state, nonzero-flag and disable-recheck controls
  fail by observed results. Opaque callbacks qualify the target contract, not the
  complete unconverted provider bodies or complete gameplay.
- Two copied owners retain all nine target-owner neighbors and all38 caller-owner
  functions/relative relocations, normalized pools and unchanged diagnostics.
  Complete GLOBAL_ASM postprocessing and both full-owner padders agree. Three
  independent code/data rebases retain exactly the same eight frame differences.

Test-only fixes remove an assertion that included a known frame word, add the
missing CSV import, correct GCC misleading indentation, and make the nonzero-
flag negative effective with non-seven flags. Bound provider observation to its
actual changed byte set rather than scanning the entire fixture on every call.
No shared oracle semantics, profile or production fix is inferred from a fixture error.

## Linked Audit And Banking

`make -C conker -j4 build/conker.us.elf progress.csv` succeeds. The known
duplicate generated_12D630 recipe warning remains; these two owner rebuilds
introduce no diagnostic. No ROM build/replacement.
The literal whole-image gate permits only the raw324-byte target slot and
symbol size12->324:242 target bytes across78 words and two size bytes,244 total.
Every other ELF byte remains fixed, including the caller after its prototype edit.
All189,088 Game-data bytes /720 owners stay exact, SHA0bbc00e1.
Guards/progress.csv/layout/Makefile are byte-identical; no new guard rows.

Source SHA256: 6d101837256f5d766c2a272e762767b0ca4d1834e956cd3ac79da87c3f0e1f41.
Caller SHA256: d15e8947326b0be2765599152782bb2227102c640630a034774d76bf543c9699.
ELF SHA256: 338313b381f06045a8d8c1c9a9a48455940c080b3723a0019e62618874fa38c7.
Guard SHA256 remains8bd422a0acd766c6dbd4e3cbaedf01c22e43cee418079facdf566eca08151cc4.

Fresh matching stays Game2,820/4,823 (58.47%), total3,493/5,496 (63.56%),
drift0/different2,003; converted totals unchanged. **New matching credit0.**
Root README aggregate rows remain unchanged because the fresh figures agree;
do not insert a function narrative there.
After literal image proof, archive the previous text manifest/ELF and advance
only its ELF fingerprint. All eight other inputs remain fixed; fresh text
integrity/corruption tests05/06 pass in1.990 seconds. Explicitly reuse unchanged
broader receipts from Note1320, not fresh-test claims or historical image rewrites.

Tools `e5c386806d3a188dda703a5465f0ae45bce83a22` is committed first, then consumer
source/prototype/docs/gitlink. Consumer/mounted/older tools checks, both Windows
syntax checks and whitespace checks pass. Older HEADddbdd16b and all114 unrelated
saved fingerprints remain fixed; only two absent new files and the verified text
pin synchronize. Dirty392->394, fingerprints115->117, no older commit.
Banking includes relative-link validation, clean active checkouts, post-bank
integrity and fresh terminal Graphify Rebuilt/zero workers. Preserve existing
graph/version/scan warnings; no push, install, host Release/save/config/editor edits.

## Next

Stay on func_150345E4: resolve source frame0x28 to original0x20 and exactly the
eight listed words without frame guards, artificial padding/state or profile
changes. Inspect actual compiler temporary/frame allocation before repeating
unchanged source controls; the unused switch-reservation cause is not proven.
Preserve all73 already-exact words and ordered helper/home behavior, then repeat
the complete qualification/image/progress gates. Same function and full Game
goal remain active. Keep text218/114/cut27 and translator49/34 open.
