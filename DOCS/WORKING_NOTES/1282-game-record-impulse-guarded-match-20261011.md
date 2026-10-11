# Game Record Impulse Guarded Match

Date: 2026-10-11. Recover complete func_1503EB78 in
conker/src/game/generated_6B320.c, replacing its zero-return placeholder.
VA 0x1503EB78..0x1503ECA0, ROM 0x6C028..0x6C150: 74 words / 296 bytes.
The semantic C body emits all 74 words with the retail 0x60-byte frame;
69 match directly. Five expected-word guards normalize one closed
coefficient-preparation FPR allocation cycle. All 74 linked words are exact.
This is guarded-exact, not full direct C. No instruction drops/insertions,
new pools, shared headers, compiler profiles or build recipes change.
Matching +1 only; converted counts/bytes unchanged. Full Game goal active.

## Baseline And Contract

Consumer 3bbea21a23390457268a0c977d649a32a36e8786 and mounted tools
6f16f59e2d940f86ff8a3e9c355aed660a2d94bb were clean at entry.
[Note 1281](1281-game-record-motion-guarded-tail-match-20261011.md)
left this genuine 74-word / 72-difference target. Read the complete retail
body, three direct element callbacks and existing callback-table interface
after a scoped Graphify query. Reuse existing IDO, ELF/object/pool/CSV
parsers, MIPS/native32 helpers, 64-bit RNG interpreter, GLOBAL_ASM
post-processing and both real padders. Codex is the single writer;
zero Claude calls, no bridge, installs or account changes.

Recover void func_1503EB78(struct04 *record, f32 horizontal, f32 vertical,
s32 mode). First argument is a record pointer, not a slot. Existing callers
ignore V0; retail happens to leave the sixth RNG result without a separate
status calculation. Use the existing 104-byte struct04 and local float view.

- Full-width nonzero mode selects mask 0x80 and bias 0x7F; zero mode selects
  mask 0xFF and bias zero. Cache these across all six RNG calls.
- Before the first call, scale both input amplitudes by D_80098920
  (retail word 0x3CE0E0E1), caching horizontal/vertical/horizontal at private
  SP+0x50/+0x54/+0x58. Cache the first-phase record pointer.
- First three calls multiply the live velocity fields +0x48/+0x4C/+0x50
  by separately rounded ((random & mask)+bias)*coefficient + 2.0f.
  Read each private coefficient and old velocity after its RNG call.
- Reload the incoming record home after the first three calls. Next three
  calls set +0x54/+0x58/+0x5C to ((random & 255)-128)*0.03125f.
- After the sixth call, read live D_80098924 (retail 0xBE99999A), reload
  the incoming record home again and store acceleration at +0x60.
- Preserve the paired F20/F21 save/restore, S0..S4, RA and frame lifetime.

Align the three callbacks func_1503F078/func_1503F0AC/func_1503F0D8 with
the existing D_80084430 type: void (*)(struct04 *, s32). Their second
argument remains unused. Complete 13/11/12-word bodies, argument literals,
pools, relocations and extents stay unchanged. Their inputs are respectively
(2.0,2.0,0), (1.0,2.0,1) and (2.06,3.0,1).

Retain func_150ADA20's original handwritten 18-word 64-bit RNG assembly.
Tests reuse next_seed and the existing wide-register oracle from
tools/tests/test_game_random_selector_outputs_match.py, not a new RNG engine.
Six actual calls update the full seed, including mapped record/seed aliases.

## Compiler And Guards

The original semantic array shape is 74 words with 22 differences. Parameter
reuse and mask-first local order reduce this to five. Named scalar, cursor,
store-order, width, scoped-local, reused-mode and register-parameter trials
do not remove them while retaining the retail shape. Compact no-unroll is
identical to selected O2/g3; O1 profiles differ.

Raw coefficient preparation uses F0 for the scale and F12 for the horizontal
product; retail uses F2/F0. Vertical product stays in F14. The five replacements
at +0x48/+0x54/+0x60/+0x68/+0x6C cover the load, two multiplies and two
horizontal stores. +0x48 retains its R_MIPS_LO16:D_80098920 relocation;
the other four have none. No order, arithmetic, addresses, calls or saved
registers change. Guard history remains its original byte prefix plus five
rows. Earlier teardown spill and motion dead-tail guards remain intact.

## Fresh Qualification

Twelve pre-install tests pass in 22.662 seconds. The installed suite passes
all twelve in 33.960 seconds after the bounded metadata audit described below.
The final two literal-install/integrity gates pass again in 4.954 seconds;
the later tools whitespace-only amendment does not change test semantics.

- 2,560 retail/raw/guarded cases exercise all 256 low-byte values, arbitrary
  upper RNG bits, mode 0/1/-1/256/0x80000000 and both stack phases. All 74
  words are reached; exactly six calls and saved registers/F20/F21 survive
  deliberate caller-saved clobbers.
- Eighteen callback/home/global/private alias cases distinguish cached
  coefficients, mask/bias and first pointer from live velocity, second/final
  pointer-home reloads and acceleration after the sixth call. A private alias
  overwrites the home and redirects the final store to explicitly mapped
  guest memory. These are emitted-guest lifetime checks, not portable C
  stack-alias behavior.
- Ninety-six actual RNG cases cover twelve 64-bit seeds, both modes/phases
  and effective record/seed aliases. All 18 retained RNG words are reached.
- Two independent links rebase the two globals and RNG with HI/LO carries
  in eight cases. All 72 fired fault triplets preserve memory/events/GPRs;
  guarded/retail FPRs are exact. Raw private scratch allocation differs.
  Faults do not establish portable C faults or hardware FCSR behavior.
- Five freshly compiled controls fail on public effects: wrong mask, bias,
  overwrite instead of multiply, lost acceleration and wrong angular bias.
  A stale expected guard word is rejected.
- Both copied complete owners are diagnostic-free, pass GLOBAL_ASM processing
  and both real padders. All 21 neighboring bodies/extents/relocations and
  normalized pools remain identical, including the three typed callbacks.
- Strict source/ELF/guard successor checks and effective stale/duplicate
  install, source, eight ELF and guard-corruption controls pass. No baseline
  is refreshed to make an audit pass.
- 288 cases execute actual callback13/11/12 -> impulse74 -> RNG18 against
  the independent ordered reference and original callback table. Full unused
  callback words include 0/255/256/0xFFFFFFFF.
- Native32 O2 and O0 each pass 12,544 cases, including all low bytes, modes,
  signed-zero/amplitude inputs, call-time velocity/global mutations and
  correctly typed callback tables. Check all 26 words of all three records
  and exactly six draws. Three controls fail with actual mismatch receipts.
  Native tests exclude private stack/global alias and FCSR claims.
- 197 float-boundary cases cover signed zero, subnormals and finite rounding
  against the reference. Infinity/NaN/overflow compare machine forms only,
  not hardware NaN propagation or FCSR acceptance.

Pre-install fixture corrections recognize the old four-argument stub's
28-byte symbol size and map a deliberately redirected alias store. These
were fixture fixes, not production workarounds.

Fresh validation commands:

```sh
python3 -m unittest tools.tests.test_game_record_impulse_match -v
make -C conker -j4 build/conker.us.elf progress.csv
make -C conker match-progress NON_MATCHING=1
make tools-check
```

Standalone mounted/older checkouts also run python3 check_project_tools.py.
Native Windows py_compile covers both identical new-file copies.

## Linked Audit

The existing wider guard-manifest dependency rebuild exits zero with known
source warnings and the duplicate generated_12D630 recipe warning. The strict
initial whole-ELF audit caught metadata rotation; it was investigated, not
ignored. Only four consecutive symbol/string entries rotate:
D_80098920,D_8009D4C0,D_8009D880,D_8009D0F0 becomes
D_8009D4C0,D_8009D880,D_8009D0F0,D_80098920. All values, types, bindings,
sizes and section identities remain unchanged. The test predicts this exact
rotation from the frozen baseline, never copies arbitrary current metadata.
Corrupt moved values/sections/strings and an adjacent string fail effectively.

Literal full-ELF comparison changes 257 bytes: 233 target bytes, two symbol
size bytes (28 -> 296) and 22 measured rotation bytes. Every other ELF byte,
body, address, extent, section/header and metadata entry stays exact. Six
other inputs are identical: progress CSV, rodata assembly, symbol definitions,
undefined functions, retail layout and Makefile.

Protected data: 189,088 bytes / 720 owners, zero differences, SHA-256
0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670.

| Input | SHA-256 |
| --- | --- |
| Source before | e367e9c05a6fbdd714f4ea53cb88939e32a50361fb08640f67d403d5593f3d41 |
| Source after | 9367a1516def9e328ede83dc1c82584a6c6ae6e485ac32ff45bf57e29a9b0fde |
| ELF before | acd55ef04121c1aad24f275cdb53e7a313d3f8608317ce381b09c200105cd666 |
| ELF after | 9ae3dd99b1c097f66414e7a23f5ad8d847b39e09b7112437687f9f173046f355 |
| Guards before | 50d69274e599b51d2cebee2e9942b09fad6a7c75f7d91a56f2666c6d823a872b |
| Guards after | 2887c379208a8ddadbded3ee593396db2e7c7920261ee9f05443f0af412e7911 |

Fresh progress: Game 2,803/4,822 (58.13%), total 3,476/5,495 (63.26%),
Init 492/492 and Debugger 181/181. Zero drift / 2,019 still different.
Matching +1 only; root README gets aggregate rows, no function narrative.

## Checkpoint And Next Body

Consumer, mounted and older standalone shared tool checks and native
py_compile pass. Bank mounted tools f6b3f22 first, then source/guards, this note,
five current indexes, aggregate README and exact consumer gitlink. No push.
Older sibling HEAD ddbdd16b53ce60b054fb6e11bf0649a41f48375a and all 55
recorded fingerprints remain unchanged. Only two absent paths are copied
with identical hashes; dirty count 332 -> 334. Do not commit/reset that
independent dirty history. Target tests run in the mounted consumer, not
the standalone mirror. Prior unchanged motion/matrix/setup suite receipts
are reused from Notes 1281/1280/1279, not called fresh full-suite runs.

Native graphify update . exits one on protective shrink refusal: 18,178
candidate nodes versus 39,958 saved. Preserve 19,398 nodes from 2,972
excluded but still existing files; no force/purge/install. Version and
empty-source warnings are separate from compiler diagnostics. After consumer
commit require a fresh terminal Rebuilt receipt, advanced log bytes/UTC and
zero workers. Precommit log: 537,061 bytes. Launch alone is not completion.

Fresh recheck: func_1503EB78 74 words / zero linked differences. Next genuine
placeholder is func_1503ECA0, 134 words / 128 differences, VA
0x1503ECA0..0x1503EEB8, ROM 0x6C150..0x6C368, same owner. Inspect the
complete body and direct caller contract before the next recovery.

The five FPR guards, earlier guard removal and deeper hardware/FCSR/
renderer/gameplay acceptance remain separate and open. No OGL Release
build/change, private input/save or active editor/debugger mutation. Keep
the full Game goal active.
