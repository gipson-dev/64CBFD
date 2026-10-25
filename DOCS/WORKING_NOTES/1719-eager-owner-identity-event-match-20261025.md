# Eager Owner Identity Event Match - 2026-10-25

## Result

Recover `func_151B19A4` in `conker/src/game/generated_1DD500.c` from its
zero-return placeholder. Complete semantic C plus four checked register-role
guards matches all 45 retail words. This is guarded C, not a compiler-only
match. Keep the existing release declaration and canonical callback ABI;
no shared-header or caller-source change is needed.

The production object and ELF are adopted in the Windows checkout, and the
fresh recount uses that actual Native ELF, streamed to the verified cache:

| Section | Exact C functions | Matching |
| --- | --- | --- |
| Total | 3,795 / 5,505 | 68.94% |
| Init | 492 / 492 | 100.00% |
| Game | 3,122 / 4,832 | 64.61% |
| Debugger | 181 / 181 | 100.00% |

Address drift is zero; 1,710 C functions still differ. Only `func_151B19A4`
receives new credit. The unchanged denominator's 75% threshold is 4,129,
requiring 334 more matches. The wider goal remains active.

## Original And Interface

- Original: `conker/asm/1DD500.s`, VA `151B19A4..151B1A58`,
  VROM `1DEE54..1DEF08`.
- Body and slot: 45 words / 180 bytes, frame `0x18`, no alignment tail.
- One binding: `+0x4C R_MIPS_26` to `func_1516972C`.
- Canonical callback: `void(struct260 *, s32, u8)`. Preserve the existing
  `void func_1516972C(void *arg0)` declaration and existing `structs.h` include.
- Private `OwnerIdentity1DD500` and `OwnerIdentityEvent1DD500` expose only
  the saved owner-identity word/key and event pair. Do not infer a complete
  actor schema or move unrelated existing payload declarations.

Read the saved owner word at record `+0x28` before every command gate.
Commands zero and `0x13` release this record if that saved word equals the
first event word OR the saved key at `+0x2C` equals event byte 4. A word match
skips the key reads. There is no added global clear. Do not substitute event
byte 8 for the original comparison against byte 4.

Command `0x2D` reloads the owner word, then exchanges it against the event's
two words. The first match wins. Store the replacement word before reading
late key byte 9 or 8, since overlap can change that read. Other modes still
read the owner word, but need no packet or key mapping in emitted guest code.
Preserve all unrelated bytes and the full incoming A2 word home before masking.

## Caller And Registry

The actual `D_8008A8D8` table has 74 entries, VROM `22F398..22F4C0`, in
`conker/asm/data/22EF80.rodata.s`. This target is index 15, with its one
literal at VROM `22F3D4` / VA `8008A914`. The aligned prepared-image scan
finds no encoded direct JAL. That is not proof against arbitrary computed calls.

The full original and retained `func_15149434` are 23 words / 92 bytes,
VROM `1768E4..176940`, in `conker/src/game/done/game_1765E0.c`. The source,
complete caller object and registry are unchanged. Preserve its selector
range/NULL gates and byte argument masking. Other providers remain bounded
argument/mutation/clobber contracts, not recovered full executions.

Execute the actual original/retained 28-word release helper as well. Its deeper
bookkeeping, callback and fallback providers remain explicitly bounded. Neither
the already-exact caller nor helper receives new credit.

## Compiler Boundary

Twelve additional complete-source probes test formal-argument reuse and
register hints. Reusing the argument produces 46 words, a shifted call and
40 paired differences; register hints retain the original four differences.
None is accepted as a direct compiler-only match.

The selected 45-word C already has the original frame, sole call binding,
branch displacements and memory schedule. Close only the retarget path's
V1/A0 allocation cycle: swap register roles at words 26, 27, 28, 36 and 38,
and commute equality operands at 28 and 36. Word 28 stays byte-identical.
Append exactly four expected-word rows at indices `26,27,36,38`, preserving
the entire old CSV prefix. Check the full raw hash and complete binding map
before derivation; no instruction insertion, omission or profile change.

There are two unreachable original words: the constant load at 23 and duplicate
packet load at 35. Both remain literal. Qualified cases visit all other 43 words.
Do not reuse a one-dead-word assumption from a neighboring event callback.

Normal owner Make uses five commands, including the real GLOBAL_ASM processing,
IDO `-O2 -g3`, padder and assembler. Its shadow reproduces all 16 compact
functions and the complete padded object. Preserve all 15 neighbors, the one
handwritten routine, pools and diagnostics. Inherited duplicate-recipe warnings
for another owner are unchanged; the Makefile is not edited.

## Qualification

Both actual tools copies pass eight genuinely fresh pre-install checks, with
zero errors, failures, skips or reused checks: active copy 261.860 seconds,
older mirror 404.649 seconds. Both shared tools checks pass, in 5.309 and
1.975 seconds. A separate three-check native/fault/image smoke passes in
49.434 seconds before the complete fresh suites.

- 9,728 partitioned guest cases cover all command/key bytes, both release
  modes, full incoming homes, first-match priority and late keys. Nine alias
  layouts include packet/state and nested stack-home overlaps. Check raw C
  public behavior and identical fitted/original complete private state.
- 12,288 connected original/retained dispatcher cases cover all 23 caller
  words, the actual 74-entry registry, selector bounds/NULL slot, every
  selector and command byte, masking and other-provider contracts.
- 64 connected release cases cover both commands, every original/retained
  helper word and the late kind reload after bookkeeping.
- Native32 `-O0`, `-O2` and `-O3`, each with trapping UBSan, pass 786,432 target
  cases and 131,072 dispatcher cases. Use canonical callback types, actual
  retained release C, pointer-member lvalue initialization, character writes
  and declared scalar word reads. Bind the fixture to little-endian native32;
  the wrong-width control also uses character reads. Runtime counters verify
  all 32 pattern/match pairs per command, and all 14 controls are effective.
- 86 paired fault prefixes and 3,036 sparse emitted executions require the
  eager owner-word read while allowing ignored modes to omit packet/key data.
  An actually compiled lazy-owner negative succeeds where original/fitted
  instructions fault, proving the check discriminates that wrong schedule.
  Compiled caller-bound and NULL-call negatives are effective too. These are
  emitted guest access checks, not portable-C fault semantics or hardware proof.
- Reject all 45 raw-word corruptions, the binding, extent/history and real
  padder corruptions. Six independent GNU links cover three layouts and
  rebase the helper call. Reject seven strict-image corruptions.
- Accept the complete 74-input installed map, then reject six independent
  mutations: source, guard CSV, target object, ELF, caller object and shared
  structs header. The installed object must equal the qualified padded object.

After production, each copy passes two fresh checks, in 2.885 / 2.915 seconds:
literal owner/Make/registry identity and strict image/frozen inputs. Six semantic
checks are explicitly reused only under identical sealed inputs, module hashes,
qualified artifacts and actual installed source/object/ELF bytes. These are
not eight fresh installed checks. No test is skipped.

## Production And Preservation

The actual production command is:

```sh
make -C conker -j4 -o retail_word_patches.us.csv build/conker.us.elf progress.csv
```

The established guarded-conversion route pins unchanged guard consumers while
freshly compiling this owner through its normal five-command path. It is not
an unmodified whole-tree rebuild. Audit the sealed old guard prefix and every
non-target object/input. Make exits zero in 26.113 seconds.

The complete ELF exactly reproduces the independent prediction: 126 changed
bytes, comprising 125 target-code bytes and one symbol-size byte (12 to 180).
There are zero exclusions or metadata permutations. All 6,054 other linked
bodies and all addresses are fixed. All 720 protected Game data owners,
totaling 189,088 bytes, remain exact.

The 16,042-file Native/cache seal covers all 1,454 linker input objects.
Native adoption verifies the full closure before and after promotion with
only four overrides: source, guards, target object and ELF. Stream the actual
adopted Native ELF through the verified stdin/tar cache, with explicit WSL
`--cd` and no project-data reads through DrvFS or IDO paths containing spaces.
The actual-ELF CLI recount exits zero in 12.231 seconds. Full reclassification
removes only this function from the queue; no manual counter increment.

Tools are committed first as `d1965a7e4dc40d23b9e18f91998c723238c2ccbf`.
Preserve the older mirror's HEAD and 1,648 pre-existing changed paths; its only
additions are the two owned modules. No mirror commit, push, Claude calls,
package/global/provider configuration changes, or host/Release changes.

| Artifact | SHA-256 |
| --- | --- |
| Snapshot | `5ba53019e482a0ad5ab209e63c8ec44cc3f96c51a8b94bbb5451872dbf8187f7` |
| Raw 45-word body | `f977fb6446a9ff27214ba602ad40f0c3ea52a4897ed059c37a5c148925f647c6` |
| Retail 45-word slot | `7777ae8710799fb5da0b9fa7fac64b022baf412b978936ae94f8dde243b56028` |
| Qualified source | `d540fb4eebd5fc2da474bfa6871f4a4827c9d5c12f3dcd267fa814dc3812dfab` |
| Qualified guard CSV | `876afb871a1a6c41916b69b192d8b9fc786b688ad91a2381bfdcd9a698814d3b` |
| Qualified target object | `969a41aa861c5b73ad23a07b8fd170da5b39ec0dbe569106a40d73f4ded144a0` |
| Adopted ELF | `d44b751638695c2eefa8ed8db23ea9fa15d201907c3bb6bb4fdba7fc05e1ed35` |

## Next Work

The actual ELF-pinned queue has 1,581 placeholder-shaped definitions,
120 semantic/other definitions and nine parser-unlocated entries. Keep the
existing-C `func_15014094` and parser-missed `Gfx *func_1510D8C0` separate.
The root README gets aggregate rows only; this note owns the detailed narrative.

The next ordinary placeholder is `func_151B8CFC` in `generated_1E5FF0`.
A private typed-view source directly matches all 43 body words/frame 32/six
bindings, with two separate alignment words. It advances the compact embedded
oscillation, phase and planar coordinates using existing math helpers and live
global time-step reads. Three alternative forms are rejected. Caller/ABI,
guest/native/float/helper, aliases/faults, owner/padder/Make/image and production
adoption gates remain open. It is uninstalled and uncredited.

Graphify navigation used actual vocabulary and scoped output; its truncated
97-node query is not complete relationship evidence. Verify source/ROM facts
independently. Refresh after the consumer commit and audit retention of all
44,170 baseline nodes and changed-file hashes/mtimes/membership. Extract the
two tools modules separately because the parent ignores `tools/`. Retain the
filtered-corpus warning; do not claim full-corpus re-extraction, old-edge
preservation, or stamp missing producer provenance into graph artifacts.
