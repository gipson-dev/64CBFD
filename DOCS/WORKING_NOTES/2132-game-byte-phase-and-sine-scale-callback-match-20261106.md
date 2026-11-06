# Byte-phase coordinates and sine-scale callback match

Date: 2026-11-06. Continue the active 80% goal from consumer
`5409015a38957c83d7663cdc0a5f5ec1ddb25ec4` and mounted tools
`4a0589f9e20beb56ef8ca3ff308b25905a2ab896`, following
[Note 2131](2131-game-white-text-crossfade-match-20261106.md).

## Recovered behavior and interface

`func_1515A11C` in `conker/src/game/generated_185560.c` replaces its zero
stub with a complete **71-word / 284-byte callback**, VA
`0x1515A11C..0x1515A238`, ROM `0x1875CC..0x1876E8`. There is no alignment
tail in this slot. Frame `0x28` retains S0, S1 and RA; the unused workspace
argument has its original SP+0x2C home and the first float result uses SP+0x20.

Owner bytes AC/AD advance modulo 256 using signed velocity bytes AE/AF and
full 32-bit D_800BE9E4. Unsigned word arithmetic preserves retail wrapping
without signed C overflow. The clock is read again after the first byte store.
The updated phases, each biased by -64 and narrowed to u8, call the original
quarter-wave lookup func_151423D8. The second phase remains live across the
first call. The first float result remains captured across the second call.

The typed MotionPayload1515A11C starts at owner+A8: shared center float,
two phase bytes, two signed velocity bytes, two radii, three scale floats,
floating phase and rate. Two center-plus-radius products update owner38/3C.
The phase advances by rate*D_800BE9A4, passes through func_15144B68, and is
stored before sinf. All three output scales at owner4C/50/54 use that sine
result and live post-call scale fields. The callback always returns one.

The proper ABI is `s32(u8 *owner, u8 *workspace)`. Helpers use
`f32 func_151423D8(u8)`, `f32 func_15144B68(f32)` and `f32 sinf(f32)`.
Existing shared declarations agree. Only this owner gains the local payload
view and necessary declarations; no shared header or helper definition changes.

The first source shape let IDO sink the payload address until after both
lookups, producing 72 words/frame0x38 with a spilled V1 payload pointer.
A register keyword made no difference. Capturing the payload before the first
lookup and reading that first phase through it recovers the retail S0/S1
lifetime, all 71 words and frame0x28. It is the installed source shape.

## Two relocated scheduling words and complete owner

The unchanged O2/g3/MIPS2/O32 profile leaves only these independent loads:

| Offset | Compiler | Retail |
| --- | --- | --- |
| B4 | LWC1 F16, global scale LO16 | LWC1 F8, payload rate+0x20 |
| B8 | LWC1 F8, payload rate+0x20 | LWC1 F16, global scale LO16 |

Two expected-word guards close this swap. The D_800BE9A4 LO16 relocation
moves from B4 to B8 with its load; the HI at 90 is fixed. Every instruction
has a compiler origin, with no omission, insertion, branch retarget, call
substitution or frame change. Both global HI/LO pairs and four calls retain
all eight bindings. Original guard CSV bytes remain an exact prefix.

The complete owner has 37 functions. All **36 raw and padded neighbors**
retain every body word and binding. The only raw allocatable metadata change
is .reginfo+8, FPR mask **000F5777 to 000F7FF7**. Its explicit XOR 2880 delta
is audited; every other raw pool byte, section field and relocation stays
fixed. All padded allocatable pools and register metadata remain identical.
The padded predecessor equals the original production object, and the actual
replacement equals the predicted object. All **179 frozen inputs** are checked.

Both predecessor and candidate emit the same four preexisting Warning712
messages in other functions: two func_100043B4 pointer/integer arguments and
two func_15158A20 calls. Only copied path/line positions differ. Actual Make
emits that identical four-message set with no new C diagnostics. These
neighbors are preserved; this is not a warning-free-owner claim.

## Qualification and explicit boundaries

Eight focused tests pass before and after installation in both actual tools
configurations. The sibling uses an ignored overlay for the five new modules
while importing and fingerprinting its real shared helpers. Its six tracked
edits and 2,428 untracked files remain unchanged. Both tools smokes are fresh;
three shared suites per copy are exact-fingerprint reuses from Note 2124,
recorded separately from fresh execution. Routine work uses zero Claude calls.

- **2,168 guest cases per body** compare original, raw C and normalized C
  against an independent state/call/snapshot contract. All 256 byte values
  occur in each phase and velocity field; extreme tick words and four
  helper-mutation modes are exercised. All 71 root words are visited.
  Normalized C matches complete RAM, registers, events and access order;
  raw C additionally passes the external state and helper snapshot contract.
- **60 guest aliases per body** cover clock/scale overlap with owner fields
  and private stack locations in both stack phases. Provider mutations are
  enabled for public aliases; stack aliases disable owner/global provider mutations to
  preserve saved-register preconditions. **108 fired access-cut prefixes**
  compare full literal original/normalized state. No raw fault-order,
  portable-C stack-alias, arbitrary FCSR or hardware NaN-payload claim is made.
- **80 caller-window cases per normalized body** execute the original
  17-word window at 15130A0C..15130A50, including skip gates and the callback's
  return boundary. The callback table is **D_80089760[12]**, ROM 22E250,
  VA 80089790. It passes owner A0 and caller workspace SP+0x48 in A1. The
  zero stub fires the expiry path, completing all 17 window words; return 1
  leaves expiry clear. The current 428-word parent func_151303EC remains a
  zero-return C stub. It is explicitly checked and gets no matching credit;
  full-parent or end-to-end runtime integration is not claimed.
- **524 connected cases per normalized body** execute the literal original
  lookup, wrap and sine helpers. Their current linked slots equal retail.
  All **27 lookup words and 24 wrap words**, and **86/104 sine words**, are
  covered. The 65-entry quarter-wave table, wrap period 40C90FDB and complete
  sine constant set are pinned. Explicit +/-100 phase cases exercise both
  repeated-wrap loops. This is a finite wrap-domain check, not all-input
  termination or full sine/gameplay/hardware acceptance.
- **Nine independent GNU links**, three entry/global layouts and **54 cases
  per normalized body** verify all eight bindings, the moved LO16, both
  address-carry boundaries, raw binding and standalone zero alignment bytes.
- **3,072 SDK native32 positive executions** pass O0/O2/O3 with UBSan, the
  correct two-pointer callback and all four 16-word helper snapshots. Complete
  owner bytes, outside canaries, workspace bytes and global words are checked.
  Including eight wrong variants, **27,648 calls** execute. Every negative
  control fails by checked state/result comparison; a sanitizer trap cannot
  satisfy the required killed-mask 255. Controls cover narrowed velocity,
  wrong ticks, wrong phase bias, prematurely cached second phase, wrong time
  scale, ignored wrapped result, wrong final scale and false return.
- All **284 raw-byte corruptions**, eight binding corruptions, two stale
  guard expectations and five whole-image corruptions are rejected.

Fixture corrections added the native clock declaration and the original
helpers' NEG.S instruction to the local oracle. The first private alias set
let a provider overwrite a saved-register slot through a deliberately aliased
global; stack-alias cases now retain their saved-register precondition rather
than disabling the oracle's ABI check. Two initially uncovered wrap words
prompted the explicit multi-period cases. The unsigned-velocity control was
replaced: signed and unsigned products have identical low bytes modulo256,
so it could not distinguish public behavior. Signed LB instructions remain
proved by complete word identity. None of these corrections changes the
recovered C, the two guards or the predicted production image.

## Actual production

```sh
make -C conker -o retail_word_patches.us.csv -o Makefile -j4 build/conker.us.elf progress.csv
make -C conker -o retail_word_patches.us.csv -o Makefile all
make -C conker -o retail_word_patches.us.csv -o Makefile match-progress NON_MATCHING=1
```

Only generated_185560 compiles, once, using the original profile. Keep both
old-dependency flags until a deliberate broader rebuild; unrelated object
timestamps are untouched. The actual ELF equals the independent **227-byte
prediction**, with **zero exclusions or metadata permutations**. Only this
body and its symbol size (12 to 284 bytes) change. All **6,052 addresses**,
conversion rows, progress.csv, Make rules and **189,088 protected data bytes
in 720 owners** are fixed. The unfinished whole image retains its expected
checksum failure and existing duplicate generated_12D630 recipe warning.

| Section | Byte-exact | Drift | Still different |
| --- | ---: | ---: | ---: |
| Total | 4,201 / 5,512 (76.22%) | 0 | 1,311 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 3,528 / 4,839 (72.91%) | 0 | 1,311 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

**209 more** matches reach the current 4,410 threshold for 80%.

- ELF: `8804d7955b17011daf0710dfef42c9270d60845540ffac14d8db3012753fb018`.
- Owner: `a8ed8a9e1ceb2f50d32b1d092977758ad5c8a823752b8f9ec40ed22c7248b6bb`.
- Code binary: `8d5d91891dc09c5825e1252b900d85f6fed619f232dde1419466df98109c5e97`.
- Guard CSV: `ad8c4e24d535e3ccc7aa3d4c3ae7db4972c569bbf690238f68c65757438993c6`.
- Unchanged Makefile: `509371c33a6266fa242b20212c16cf42d4b61575a8773b053bfad43d0778ae1b`.

Evidence is retained in `conker/build/game-phase-motion-callback-1515A11C-match/`.
Graphify receives a scoped AST refresh with old-node retention evidence;
no full-corpus extraction is claimed. Tools are committed before consumer
source, guards, documents and pin. Root README changes aggregate rows only.

Next static target: **func_15160A58**, game_18D770, VA
`0x15160A58..0x15160B74`, ROM `0x18DF08..0x18E024`: 71 words/frame0x68.
Inspect its full 16-argument ABI, owner null gate, descriptor/header layouts,
forwarded factory arguments, payload padding and conditional 24-byte copy.
The current integer placeholder and nearby commented draft are hypotheses
until callers and exact emitted words establish proper types. It remains
uninstalled and uncredited. Preserve private inputs/saves, unrelated work,
handwritten func_150A76F0 and frozen host Release. The full 80% goal stays active.
