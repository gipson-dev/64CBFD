# Actor Animation Request Direct Conversion

Date: 2026-10-10

Continue [Note 1235](1235-game-actor-definition-count-direct-conversion-20261010.md).
Convert complete func_1507EA44 from GLOBAL_ASM to directly byte-exact C and
qualify the actual record caller, definition lookup, list and classifier.
The wider Game matching goal stays active. This is not host/full-game acceptance.

## Scope And Baseline

- Consumer starts clean at 41c57f78, mounted tools clean at 2c8eae2. Single
  Codex writer, zero Claude calls. Keep-committed authorization: tools first,
  consumer source/docs/tools pin second; no push.
- Owner conker/src/game/generated_AB760.c; VA 0x1507EA44..0x1507EABC,
  ROM 0xABEF4..0xABF6C, 30 words / 120 bytes, original 0x18 frame.
  Keep original assembly and nonmatchings copy. Local graph has no target
  node; inspect complete retail routine and actual caller/helper interfaces.
- Seven immutable before-* snapshots cover owner, ELF, guards, conversion
  CSV, protected rodata, tracked symbols and ignored undefined assignments.
  Before-source SHA-256
  bb5309d25735e87d63fc76c7bd7be33d2a51e9eb1584bd3892591640f61fd180;
  ELF bf999834941dc6804caa011978298b58687ee6e9512c4649a766a49d2c57ec91.
  Retain and recheck every hash; never rewrite the baseline after installation.
- Older tools remains ddbdd16, independently dirty: 235 native Windows Git
  entries before, 237 after two absent-path authored mirrors. Exact mirrored
  bytes and both Python parses pass. Preserve dirty fingerprints
  game_owner_pool.py
  159B8C009AF7B2D26BA5DCE29F0C46CA0805CF14DBB27E5C682D107E551CA50E and
  test_game_node_effect_registration_match.py
  C9195B44C4276E410CD6ABAB7F926E4C920363BF84505F5596681937397FBC71.
  No older-tools commit/reset, OGL/Release, editor, save or private-input edits.

## Recovered Behavior And Match

Zero index returns without calling or dereferencing an actor; a null actor is
therefore valid on that skipped path. Otherwise call func_1507E9F8(actor, NULL).
Its nullable list determines whether the constructor is called. Select the
unsigned byte at list + index - 1 without inventing an index clamp. Convert
the full signed third word to single, multiply by live D_8009B8A0 and call
func_15083568(actor, animation, scale, 0). Return contract is void; V0 is not
a result. The mixed O32 third argument carries single-float bits in A2.

The simple nested-if body emits all 30 retail words directly under normal
O2/g3, original 0x18 frame, zero diagnostics, guards, insertions, omissions
or pools. Selected unsigned index subtraction avoids signed index-1 overflow.
Signed subtraction and early-return variants also match; a separately stored
scale emits 30 words with seven scheduling differences and is not selected.
Keep original JAL relocations at +0x24/+0x60 and factor HI16/LO16 at +0x38/+0x3C.

Retail stores all three incoming arguments in their home slots. Reload the
amount after the list callback even when the list is null; actor and index
are reread on the nonnull path. Read live factor before the list byte. The
factor word is 0x3A83126F (single 0.0010000000474974513), not an invented
double constant. Integer-to-single rounding happens before the multiply.
Compare every private read/write/call and exact A2 bits, not only final state.

Authored tools: [complete candidates](../../tools/experiments/game_actor_animation_request_candidates.py),
[qualification and linked audit](../../tools/tests/test_game_actor_animation_request_match.py).

## Fresh Qualification

- 19,201 cases / 38,402 original/C guest executions pass an independent full
  private-order reference. Cover zero/full-word indices, signed amount and
  single-rounding boundaries, nullable list, five finite/zero factors and two
  stack phases. Mutate actor/index/amount homes, list byte and factor during
  callbacks; clobber caller GP/FPR. All 30 retail words execute across cases.
  Extreme wrapping indices are synthetic guest-instruction probes, not
  portable native C or real resource-domain acceptance. No FCSR emulation.
- 264 actual-list/alias cases / 528 runs pass. Execute actual byte-exact
  19-word func_1507E9F8 and 11-word func_150849A0 with original default bytes
  05 06 07 0A 0B. Caller passes NULL output-count pointer; nonnull output
  paths remain a separate gate. Include private amount/factor and saved-RA
  byte aliases; fire 248 strict fault pairs / 496 failed runs and compare
  memory/events/calls/FPR prefix state. Both nonzero-index null-actor runs
  fail at the real classifier read +0x1C9, with identical prefixes.
- Eight independently linked original/C binaries at four entry/list/
  constructor/factor rebases pass 192 cases / 384 runs. Preserve both JALs,
  mixed argument carriers and signed HI16/LO16 carry; no replacement guards.
- Complete copied-owner production compile/post-process/actual padder has
  zero diagnostics. Entire padded objects, all 14 neighbors, extents,
  relocations and pools remain equal under the unchanged manifest.
- Seven freshly compiled IDO negative controls are effective: byte-narrowed
  index, wrong one-based offset, unsigned amount, float input contract,
  wrong mode, truncated scale and cached instead of live factor. The cached
  negative legitimately emits a literal pool; map that ELF's structured
  .rodata/.data into its fixture before execution. The initial unmapped-pool
  failure was a fixture defect, not a production failure or an accepted
  negative result. Rerun the complete nine-test suite after fixing the fixture.
- Native32 complete C at O2/O0 passes 819,328 cases per profile / 1,638,656
  runs. Exercise synthetic valid one-based indices, all low signed amounts,
  full-word conversion/rounding boundaries, nullable lists and live typed
  callbacks. Compare actor/lists/factor and exact float packet bits. Two
  native unsigned-amount/offset controls fail. RNE finite input evidence does
  not establish hardware FCSR, traps, nonfinite behavior or gameplay parity.
- Execute actual 60-word func_1507E5C8, both 30-word request forms, 24-word
  definition lookup, 19-word list and 11-word classifier in 3,456 cases /
  6,912 runs. Independent nested-frame reference preserves descriptor-byte/
  unsigned-halfword inputs, live record rereads, parent full-word amount
  overrides, state byte updates and archive fallback bytes. All 58 reachable
  caller words execute; redundant dead words 37/49 are excluded. Fire 474
  connected strict fault pairs / 948 failed runs, including FPR prefix state.
  Constructor is a bounded typed callback, not its actual 89-word body.

## Linked Audit And Progress

All nine final post-install tests pass in 27.111 seconds. Root tools-check,
older standalone tools check and both mirrored Python parses pass. Source-only
rebuild has no changed-owner compiler diagnostics; retain the existing
duplicate generated_12D630 Makefile recipe warning.

Whole linked ELF is byte-identical: 3,261,160 bytes, SHA-256
bf999834941dc6804caa011978298b58687ee6e9512c4649a766a49d2c57ec91.
All addresses, extents, symbols, headers, sections and instruction/data bytes
remain exact. Guards, protected rodata, tracked symbols and ignored assignments
are byte-identical. Protected data: 189,088 bytes / 720 owners / zero differences,
SHA-256 0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670.
Only the 120-byte target CSV row changes asm -> c; all other rows and both
repeated headers remain exact. Installed source SHA-256
64a4ce9d3ba2640951a234774c59122eec6bd02b4a1468824a07afcabb1df99a;
CSV 738f9596296f185524c6ee24932520ef68be00ed2c653eac6b3c5a4cc6ff102c.

Fresh conversion: total 5,494/6,043 (90.92%), 1,941,060/2,256,728 bytes (86.01%);
Game 4,821/5,322 (90.59%), 1,769,624/2,072,880 bytes (85.37%). Init/debugger
and all denominators unchanged. Delta +1 converted function / +120 C bytes.
Fresh matching: Game 2,771/4,821 (57.48%), total 3,444/5,494 (62.69%), zero
drift / 2,050 different. Delta +1 matching credit; different count unchanged.

```sh
python3 -m unittest tools.tests.test_game_actor_animation_request_match -v
make -C conker -j4 build/conker.us.elf progress.csv
make -C conker match-progress NON_MATCHING=1
make tools-check
```

Bank mounted tools da7086a before consumer source/docs/tools pin, no push.
Root README receives aggregate rows only. Earlier broad neighbor receipts
remain historical, not fresh tests; their linked bodies/guards/data remain
unchanged under this full audit. Eight added relative links pass, zero broken.
Native Graphify update after final code edits refuses unsafe shrink
39,534 -> 17,761 nodes, retaining 19,398 nodes from 2,972 excluded-but-existing
files. Preserve exit 1, skill 0.9.20/package 0.9.26 and devcontainer.json
zero-node warnings; no force, purge or install. The separate consumer hook
requires fresh log growth/completion and zero workers before reporting clean.

## Next And Boundaries

Next: recover complete func_15083568 in conker/src/game/generated_AEB40.c.
The current C is a false zero-return placeholder, not semantic restoration.
Retail VA 0x15083568..0x150836CC, ROM 0xB0A18..0xB0B7C, 89 words / 356 bytes,
original 0x68 frame. Recover descriptor lookup through D_80086CC4, its
eight-byte entries, record iteration and full actor/animation/float/mode ABI.
Existing typed call sites establish u8 * return, even though this request
ignores it. Do not broadly rewrite unrelated historical declarations.
Actual constructor, nonnull list-output paths, other complete callers, real
assets, hardware/FCSR and live gameplay stay open. Wider goal remains active;
zero Claude calls and no billing or goal-completion claim.
