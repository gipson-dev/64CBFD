# 2647 - Actor emission preset guarded match

Date: 2026-11-23. The total 85% matching goal remains active.

`func_150BFFE0` in `conker/src/game/generated_EC420.c` replaces its false
zero-return placeholder with the complete actor emission preset. The C body
emits **127 words in the original 160-byte frame**. It has **42 linked word
differences before normalization**; it is not a direct C match. **45 strict,
relocation-aware expected-word guards** restore the original allocation and
schedule, including four offsets whose unbound word is unchanged but whose
relocation differs. The final padded function is byte-exact across all 127
words, with **zero insertions and omissions**. Shared padders are unchanged.

Production: **4,628 / 5,528 (83.72%) total**, **3,955 / 4,855 (81.46%) Game**,
zero address drift, **900 different**, **71 more matches to 85%**. Init remains
492/492 and Debugger 181/181. Converted-function and byte rows are unchanged.

Original: `conker/asm/EC420.s`, line 1147; VA `150BFFE0..150C01DC`,
ROM `ED490..ED68C`, 508 bytes. External bindings are two calls and six data
symbols. Both complete-owner padders and the actual Make recipe keep the
other nine functions, pools and changed-owner diagnostic set fixed.

## Source, interfaces and lifetimes

The interface is `void func_150BFFE0(u8 *actor)`. It snapshots actor X at
+0x14, actor Y at +0x180 plus 70, and Z at +0x1C before calling the effect
helper. The helper can have side effects; the later descriptor must use the
captured position. Its Y then adds 35 with a second single-precision rounding.
Combining the offsets into one addition is observably wrong for the retained
large finite witness. X and Z preserve their original floating payload bits.

The local 108-byte descriptor is a base-count-17/range-7 preset, kind 108,
halfword field 0x5103, header 0x200005, fixed color/parameter bytes and
halfwords, the snapshotted position, six global floats, flags 0x40040E07 and
the final floating payload at +0x68. Bytes +5 and +0x65..+0x67 stay untouched.
The existing descriptor view in `generated_1D0840.c` provided the initial
layout; the complete original consumer confirms widths and the final field.
Opaque fields retain offset-based names instead of invented engine meanings.

The complete 197-word original `func_15136C3C` establishes its local interface:
pointer, six unsigned byte flags, word context, with no consumed result.
The request is `(actor, 0, 0, 1, 0, 0, 255, 1)`. Its source declaration and
the SDK32 provider use those measured widths. Correcting the initial all-word
declaration changes no target instructions or padded owner bytes. The full
224-word original `func_15153634` establishes its pointer/byte/byte/word
interface. It reads +0x68 as a float and copies those four payload bytes into
successful records. This caller passes `(&packet, 255, 255, 1)`.

The literal direct-edge census finds one call, `1507D810`, in
`func_1507D754` (`game_A9D90`): JAL, delay-slot move from saved S0 to A0,
branch and delay-slot V0=0. The wrapper result is discarded. No aligned exact
word pointer appears in the pinned binary; computed/materialized pointers
are not excluded. No existing source caller declaration needs changing.

## Normalization boundary

The first source screen already recovered 127 words/frame 160, with 58 linked
differences. A source-order change reduces that to 42. Additional bounded
storage/order/interface screens did not produce a direct match; a separate
floating temporary grows the frame, and IDO rejects nonconstant aggregate
initializers. These controls remain private, not installed alternatives.

The chosen body supplies every operation, constant, store and binding. Its
register-erased instruction/binding multiset equals the original exactly.
This is structural closure only: it does not prove operand value flow.
Independent raw MIPS and native C gates below provide that separate evidence.
The 45 guard rows contain 41 changed unbound words and four binding-only
offsets; binding the original symbols makes 42 raw word differences. They
normalize floating/general register allocation and instruction ordering,
including the final call-delay store. They do not insert code or supply a
missing operation, body, field value or call. All old guard bytes remain an
identical prefix, and every added row is restricted to this one function.

Raw C has a different access schedule. Its private fault prefixes are not
called retail-exact. The normalized output restores the original instruction
stream and ordered accesses. Both expected instruction words and relocation
bindings must agree before a row can apply; drift is a hard error.

## Focused qualification

Five gates pass freshly in each tools setup before adoption. Installed runs
freshly repeat the complete-owner, actual Make and independent image gate;
four semantic gates are reused only under exact source, object, guard, binding,
original-target, native-artifact, manifest and import fingerprints. They are
not reported as fresh installed semantic executions.

- **128 cases per raw/padded/original stream** check every initialized
  descriptor field, preserved padding, both call boundaries, provider effects
  and final private memory/GPR/FPR/HI/LO state. They cover finite height
  boundaries, signed zero/subnormals, payload copies, two stack phases,
  ordinary and caller-stack actor buffers, and a helper that mutates the
  actor and globals. Every original target word executes. Raw C agrees on
  packet/effects/final state; its trace differs in all 128 cases. Normalized
  and original streams agree on the complete retained state and trace.
- **32 cases per stream** execute the actual four-word caller window,
  checking its saved actor pointer and outgoing V0=0. The large dispatcher
  itself is not fully executed.
- **195 fired own-access fault-prefix pairs** compare normalized/original
  memory, GPR/FPR, HI/LO, ordered accesses, calls and packet observations.
  The raw stream differs in **156** of those private prefixes. Provider
  internals, asynchronous exceptions and hardware remain outside this model.
- Raw source compiled against actual SDK32 at **O0/O2/O3 each passes 8,192
  cases** with strict aliasing, UBSan and explicit IEEE single-precision
  arithmetic. The typed providers check both interfaces, pre-call snapshots,
  separate rounding, all named fields and actor canaries. Seven source
  controls fail comparison: late snapshot, combined-height rounding, wrong
  kind, wrong color, wrong first boundary, wrong payload and wrong flags.
  Native code does not read uninitialized padding or execute the guard rows.
- Both full-owner and isolated-target padders produce the exact function.
  **12 GNU links / 96 guest rebase runs** cover four independent code,
  two-callee and HI16/LO16 data arrangements, including signed-low-half carry
  and another J26 region. Four wrong-word/binding outputs fail comparison;
  four changed expected-word/binding inputs fail closed. Oversized input is
  rejected by the generated padder's extent check and by the generic
  padder's stale-overflow-guard check. There is no accepted overflow body.
- `make tools-check` passes. A disposable sibling overlay uses explicit
  required primary fallbacks; the actual sibling tools HEAD, dirty state
  and 353 retained dependency hashes stay fixed. Existing duplicate Make
  recipe and legacy compiler warnings remain. Routine Claude calls: 0.

Initial fixture failures were corrected before fresh five-gate reruns: the
isolated target initially received unrelated owner guard rows, correctly
rejected by the shared padder; the oversized control assumed only the
generated padder would reject; and the native standalone entry needed SSE
stack realignment. A bounded GDB run identified the latter at `movaps` on a
misaligned `_start` stack. The harness now aligns its entry. None of these
fixes changes shared padders, the compiler, target code or production options.

## Independent whole-image and production audit

The actual full ELF equals an independent prediction across **all bytes**:
**481 changed bytes, zero exclusions**. The target's 508-byte slot and symbol
size 12->508 change. Twelve symbol records reorder in exact closed groups,
with the full list pinned in the manifest. No symbol/string section is
excluded and no other definition, function address or extent is allowed.

The independent reference recompiles the frozen OLD owner with OLD guards,
requires its entire padded object to equal the frozen production object,
then replaces only this target using independently assembled original ASM.
Recovered C and the new guard rows do not construct that reference. The
predictor requires identical ELF geometry, the complete named-definition
multiset after the one declared size update, and full nonconflicting string
pool reconstruction before comparing the literal complete image.

All **189,088 protected Game data bytes across 720 owners**, other loaded
bytes, private inputs, headers, profiles and conversion rows remain fixed.
The only guard-file change is the verified 45-row target suffix. Fresh
production Make and live recount establish the totals above. Documentation
and the graph cache are accounted for separately in the final input bank.
No sibling host import/build, Release change or gameplay acceptance is claimed.

Raw target SHA256: `96ec198fe149b3bb2095b69ca07a71449e81772a7a649f2507c59a1d4d39f97b`.
Normalized full-owner SHA256: `dc156bb4de49d8ddddc88cff096d99faf1263679277d9c05505b32f9276d2858`.
Production ELF SHA256: `104d7c8da69b3f95a8d2eca97b3fcbfdc00fe5d3511fa79bfb485c9116f03352`.

```sh
python3 -m unittest tools.tests.test_game_actor_emission_preset_150bffe0_match -v
```

Artifacts: `conker/build/game-actor-emission-preset-150bffe0-private/`.
The fixture fails closed on phase-input drift. Codex owns implementation and
validation. Tools are committed before the consumer pin; no push.

## Next work

The earlier direct matches stay banked in
[Note 2645](2645-game-paired-preset-factory-requests-direct-match-20261122.md)
and [Note 2646](2646-game-effect-preset-packet-direct-match-20261123.md).
The separate `func_150A6760` decoder forms remain private and uncredited;
see [Note 2644](2644-game-visibility-bitplane-decoder-private-recovery-20261122.md).
The next same-owner stub is `func_150C01DC`, 185 words, ROM `ED68C..ED970`.
Inspect its complete original body and consumer interface before source
fitting. Continue the full 85% goal with 71 further matches required.
