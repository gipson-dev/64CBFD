# Note 2582: Trail emitter recovery and remaining layout boundaries

Date: 2026-11-19. Consumer baseline `a9a705eb8776b7fe30233145a984403cf153c5fe`;
tools baseline `b4f291eb83f21e81ccf3133eb448b88430d66669`.

`func_151058B4` has a tested **private semantic C recovery: 197 words, frame
248, 24 aligned word differences**. Retail has **197 words, frame 240**.
The live function remains GLOBAL_ASM. **Uninstalled, zero matching credit**:
no source, guard CSV, conversion row, production object or ELF change occurs.
No frame guard or patch is installed. This banks the recovery before more
compiler/frame work; the 85% goal remains active and unfinished.

Fresh actual-image recount remains **4,570 / 5,521 (82.77%)** total,
**3,897 / 4,848 (80.38%)** Game, zero address drift and 951 different.
Init 492/492 and Debugger 181/181 remain exact. At the current denominator,
123 further matches reach 85%; additional ASM conversions can increase it.
Root README is unchanged because all aggregate measurements agree.

## Whole body and observed interfaces

The routine spans VA 0x151058B4..0x15105BC8, ROM 0x132D64..0x133078.
It checks the gate pointer at object +0x30, draws a float RNG result, and computes
`(sample * D_800A23EC + D_800A23F0) * scale`. If this local floating count is
strictly greater than one, it prepares persistent metadata and emits particles
in a do/while loop, subtracting one after each submission. Integral and
fractional counts have the original strict-threshold behavior. The count is
local and is not stored back to the object's scale.

The local record models a 56-byte prefix: opaque header +0x00..0x27 and inline
emitter at +0x28, containing source pointer, f32 scale, gate pointer and flags.
The source models the three signed coordinate shorts and the remaining observed
22-byte sampler prefix. Pointer arithmetic stays within these observed objects;
the SDK's misleading `struct207`/`struct206` payload declaration is not used to
interpret the new body's inline fields.

The sampler supplies header X/Z plus top/bottom outputs. Header Y is initialized
once from the source's **signed** Y coordinate; it stays cached when a helper
changes the source pointer. The two packet-range globals are cached once before
the loop. The later parameter globals remain live per iteration. Helper mutation
cases distinguish those lifetimes, channels and persistent private fields.

Each iteration generates its color byte with unsigned modulo 101 plus 155,
its header count with `(random & 3) + 3`, and duration with unsigned modulo 31
plus 30. It then requests a direction using a byte heading, signed pitch
`(s16)(random % 22U - 54)` and float radius `random * 20 + 30`. The complete
six-argument `func_1515C2F0` submission carries the header, 60-byte packet,
zero parameters and the current two header bytes.

The original 38-word consumer is pinned at its header constant-10 store and
60-byte memcpy contract. Its whole allocator behavior and the sampler/trigonometry
providers are outside this target's qualification. In particular, the existing
production sampler placeholder is not restored by this private recovery.

## Actual caller and owner typing

The original 27-word `func_15105848` is the known direct caller. Command 0x38
calls the emitter then sets its flag bit; 0x39 clears that bit; other commands
do not emit. Raw upper command bits are narrowed to the original byte ABI.
Forty cases per stream execute the actual original wrapper and recovered body.

The proposed wrapper retains its shared-header `struct207 *` interface and
uses a complete typed prefix internally. Its local forward declaration for the
emitter becomes void/pointer typed. This removes three existing pointer/type
warnings in the candidate while preserving the wrapper's compiled instructions.
All ten copied-owner neighbors and all constant pools remain unchanged. Two
pre-existing warnings in another function remain. These typing corrections are
part of the **private proposal**, not changes to the live source.

## Fresh recovery evidence and explicit non-matching witnesses

- **140 cases per original/raw guest stream** compare all public memory,
  ordered helper calls, the 22 defined header bytes and 55 defined packet bytes.
  Gate states, strict/fractional count boundaries, signed source extremes,
  full-word RNG values, cached/live globals, source replacement and private
  descriptor mutations are covered. Saved ABI registers and stack restoration
  agree. Two NaN-selection models are separate from hardware FP acceptance.
- Both streams visit **196 / 197 words**. The retained `break 7` at offset
  **0x1C4** is unreachable because the saved modulo divisor is the constant 101.
  Its literal word is pinned; it is not deleted or counted as dynamically visited.
- **40 cases per stream** execute the original wrapper, including commands
  0x38, 0x39, 0x37 and raw 0x138. The proposed C wrapper is also compiled and
  exercised in **54 native cases per positive profile**.
- Actual SDK32 C at **O0/O2/O3 each passes 68 finite cases**, strict aliasing
  and UBSan. Eight compiled source mutations fail at runtime: gate, strict
  count, color/duration moduli, signed Y, loop decrement, channel order and
  cached-range reload. Native checks exclude uninitialized padding and do not
  claim arbitrary FP control/status or full provider behavior.
- The frame is **eight bytes too large**. Private helper arguments are therefore
  at entry-relative addresses **eight bytes below retail**, despite having the
  same SP-relative offsets. The guest observes differences at header padding
  0x16/0x17 and packet padding 0x22/0x23/0x33/0x3A/0x3B. These seven differences
  are deliberately retained as failing exact-layout witnesses, not normalized
  away or excluded from a claimed complete-packet match.
- **68 cases expose a public-read-order difference**. At public access 5 in the
  retained witness, retail reads the source's signed short at 0x50002; raw C
  instead reads the range-base float at 0x800A23F4. Reordering the C statements
  alone did not stop the optimizer's scheduling choice. No raw public-fault-
  prefix or all-input CFG/FCSR equivalence is claimed at this stage.
- Recovery qualification checks all **2,034 frozen predecessor input hashes**
  before this documentation refresh. Subsequent audits allow only the declared
  documentation updates and new tools. The complete live ELF, guard CSV,
  progress CSV, source and production owner object retain the previous baseline
  bytes. The fresh linked recount is unchanged.

Primary tools and an isolated **985-file overlay** each pass six recovery tests.
The real dirty sibling's HEAD, raw status and 343 dependency hashes are preserved.
The overlay contains 341 equal sibling files, 637 explicit primary fallbacks,
six task files and one bootstrap. `make tools-check` passes. Tools commit precedes
consumer documentation/gitlink; no push or Claude call occurs. Host files,
saves and the frozen Release remain untouched.

## Resume the same function

Use `conker/build/game-map-trail-emitter-151058b4-private/` and the committed
manifest's complete selected C. `canonical.c` is the tested proposal; earlier
screen/layout/read-order variants remain diagnostic artifacts. The unsigned
metadata bytes recover the 197-word extent; the grouped scratch gives the
original relative data offsets: bottom 0x88, top 0x8C, packet 0x90 and header
0xCC. The source retains the 24-word difference and 248-byte frame.

Next inspect the actual compiler frame/local-reservation records for this
canonical source. Recover the original **240-byte frame** before installing
any normalizer; then close the source-height/range load schedule and cached-FP
roles. Repeat complete copied-byte, prefix and CFG/FP/ABI checks, both padders,
actual Make, GNU rebases, strict full-image and production/recount gates before
awarding credit. Do not switch to another broad conversion batch or patch the
two frame words merely to make the byte counter green.

Graphify links this manifest to active original ASM and an explicitly private,
uninstalled C reference. Its scoped four-file AST refresh retains old IDs and
is not full-corpus semantic extraction. Reproduce under prepared WSL with
`python3 -m unittest tools.tests.test_game_map_trail_emitter_151058b4_recovery -v`.
