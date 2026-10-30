# Note 1873: actor state-9 start direct match

2026-10-30. `func_15063404`, owner `generated_90840`, replaces its zero-return
placeholder with `void func_15063404(struct127 *actor)`. VA
`0x15063404..0x150634E4`, ROM `0x908B4..0x90994`: all 56 words / 224 bytes
match directly from C. No alignment tail or new word guards. Existing
O2/g3 profile, headers and layout remain unchanged. Tools commit: `09811a104f5ac6750239f1144ec7c70b7c104512`.

## Source and ABI

The signed actor-pool byte displacement is divided by `sizeof(struct127)`
and used to capture an entry from `D_800CC2D0`. Its nested state becomes 9.
Requests `0x1D` and `0x1E` use scale 1.0 and mode zero. After both callbacks,
the routine sets the incoming actor's jump-disable field to 20, clears the
run-disable field and byte `0x83`, writes nested halfword `+0x24` to 60,
reloads the nested pointer, sets byte `+0x11A` to 2, and requests animation
`0x7F` with scale 1.0, three zero floats and a zero trailing argument.

The entry is captured before callbacks while its nested pointer must be
reloaded after callback mutations and the halfword store. Existing helper
declarations describe these calls correctly; no shared header is changed.
`struct126` names `+0x24` as padding, so the recovered halfword store uses
a scoped byte-offset cast rather than changing the shared structure.

The first two-local index/entry candidate had 56 words, frame56 and seven
word differences. Combining the index into the entry initializer restores
frame48, RA at SP+36, captured entry at SP+40 and the incoming actor at
SP+48. No saved S registers. Five relocations bind the pool address, two
calls to `func_15083568` and the final call to `func_1505E650`. Volatile
and C pointer-subtraction experiments regressed and remain private.

Raw and retail word SHA-256 are both
`ff370fa8491731248a834409305133d40b5e8db49e1aa7b5970577dd5adfb28b`.
The padded object SHA-256 is
`f770105c3d85fc5bf08b668f99c3bcd739b31f4e0873da1c7c8ce964b0458cba`.
The guard manifest remains byte-identical, SHA-256
`0d1b6200117db2da46587d9776ac0a8e1c7701849dd2020c6b21a92ffae6637b`.

## Qualification and boundaries

Ignored evidence: `conker/build/game-actor-state9-start-15063404-match/`.
`semantic_v11.py` and all eight private/canonical checks complete with exit0.

- Guest: 3,396 cases / 10,188 executions, all 56 words. Original, raw C and
  padded C agree in complete modeled state and access trace. Seven alias
  layouts, signed division truncation, misalignment/negative guest inputs,
  callback pointer mutations, pre-provider state observations and ignored
  return values pass. The fixture maps aliases without overwriting earlier
  regions. Native validity is restricted to the tested allocated domain.
- Access prefixes: 95 cuts, including five branch-delay cuts. Two extra
  actor/stack-alias witnesses are guest-only. These qualify instruction
  order, not portable C fault or invalid-pointer behavior.
- Relocation: 324 cases across three independently GNU-linked layouts.
  Complete original/raw/padded state and access order remain equal.
- Callers: two aligned JALs, ROM `0x93EBC` and `0xC6888`; no aligned literal
  function pointers. The 19-word actor-update window at `0x150669E0`
  passes 96 cases across the global enable gate, states 1/2, target/sibling
  route and post-call state reload. The original 2,146-word dispatcher
  `func_15097A8C` and its actual 142-entry jump table pass 288 cases,
  including event108/state9, found/null lookups, sibling59 and unrelated
  commands0/143. Lookup and sibling handlers remain bounded. Current C
  parents are not equivalent; no complete-parent acceptance is claimed.
- Providers: 192 cases connect original and retained 95-word
  `func_1505E650`. Only 23 words on busy/invalid-actor early-exit routes
  execute; this is not full-provider coverage. Spawn's typed ABI is
  `u8 *(u8 *, s32, f32, s32)`. Animation uses a 16-bit second argument,
  four float arguments in total and a final integer. Larger provider
  semantics remain bounded and receive no new matching credit.
- Native32: 212,992 cases per O0/O2/O3 profile with trapping UBSan, SDK
  layout and typed-provider assertions, 26 actor slots, 256 patterns,
  16 mutation modes and two initial nested banks. All pre-provider/final
  observations and canaries pass. Nineteen native defect controls and
  21 separately IDO-compiled controls fail the independent reference;
  two signed-index/timer-pointer-alias controls are guest-only.
- Fingerprints reject 224 single-byte corruptions plus size/binding/scope
  negatives, 229 in total. A separate two-local C body rejects the wrong
  frame and saved lifetime. No word normalizations are performed.
- Complete owner: all 18 neighboring functions and pools remain fixed;
  five actual Make commands reproduce the complete padded object and
  19 compact functions. Compiler, owner and executed-command diagnostics
  are empty. No compiler flags or function-specific profile is added.

Both tools copies pass eight fresh canonical checks and shared tool checks.
Production runs two fresh installed checks per copy and reuses six semantic
checks only under exact module/input/artifact fingerprints. The initial
native fixture used the defect-control name `run`, colliding with its
harness entrypoint. Renaming that control `run_flag` fixed the fixture;
production source and flags were unchanged. Failed receipts are retained.

## Image, progress and banking

An independent literal ELF prediction reproduces production: 179 changed
bytes = 178 target-code bytes + one target-extent byte, metadata0,
exclusions0. All 6,055 other function bodies, all 6,056 function addresses,
and all 189,088 protected Game-data bytes / 720 owners remain unchanged.
The conversion inventory CSV and map stay byte-identical.

Adopted ELF SHA-256:
`2faf8cd54e3986dd74bd4b83000e2b7c6dba397e1fb65da3b28404de003651c4`.
The actual Native ELF recount is **3,950/5,506 (71.74%)**, Game
**3,277/4,833 (67.80%)**, Init492/492 and Debugger181/181, zero drift.
The 75% threshold is 4,130/5,506, requiring **180** further exact functions.

Tools are committed before the scoped consumer source/docs/pin commit.
The older tools mirror retains all 2,057 inherited dirty paths and adds
only the three qualification modules, with no mirror commit or push.
The root README changes only two aggregate rows. Graphify structurally
refreshes the eleven supported changed files, preserves all old nodes
and still-valid relationships, and retires the two false global/scoped
s32 return-type edges using the actual before/after declarations. The
unchanged guard manifest is bound by its exact hash. No full-corpus
re-extraction, new clustering, full-provider or gameplay claim is made.

Next private screen: `func_1508EF80`. Parked candidates remain uncredited. The wider
matching goal remains active. Zero Claude/REA calls, dependency installs,
account/browser or sibling host-port changes.
