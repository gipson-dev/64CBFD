# Owner Burst Emitter Recovery And Private Layout Gap

Verified 2026-10-17. Consumer predecessor `dfdf4011`; tools predecessor
`e033fe7`. Both active trees began clean. The preceding turn installed the
90-word scale/timer update; this turn recovers its larger neighboring emitter.
This candidate is **not installed and earns no matching credit**.

## Complete Recovery

`func_150F2D14`, owner `generated_11FF10`, original `asm/11FF10.s`:
VA `150F2D14..150F3194`, ROM `1201C4..120644`, 288 words / 1,152 bytes,
retail frame `0x150`.

The complete semantic C candidate is in
`tools/experiments/game_owner_burst_emitter.py`. It reconstructs:

- The global disable byte, linked-owner active word and byte-epoch gate.
  Invalid owners receive the original **halfword** `-1` store at actor `0xE`.
- The owner-state transition, three-record reset, signed byte counter and
  optional seven-argument state notification.
- The float32 timer increment, strict `> 1.0f` gate, and repeated emission
  while both the timer and signed counter permit it.
- Two ordered random samples, duration/base/decay calculations, cached scale
  multiplier, two-point matrix transform, and basis-generation gate.
- An explicit 52-byte emitted payload and 88-byte actor descriptor, including
  padding holes whose live bytes remain nonmatching. Field names describe
  proven roles or byte offsets rather
  than inventing unproven meanings for the descriptor constants.
- The unsigned byte conversion, 12-argument constructor, optional full 52-byte
  payload copy, and counter/timer updates even when allocation fails.

The alternate draft is reference-only. It contains wrong-width accesses and
explicit conversion-error placeholders; none were accepted as matching C.
The symbol and purpose comment are retained in the experimental body. The
isolated linker uses the established `memcpy=0x10022EC0` synthetic Init address,
not the incompatible runtime `0x80022EC0` address.

## Measured Matching Gap

The candidate emits **288 words**, with the same saved GPR/FPR set and 25
relocations, but frame **`0x158`** and **85 unequal words**. Raw SHA-256:
`de1b59b226ecb144ea4a7ff1d460c2f757bb7180907431cbe75357fb2a8b2f18`.
Actual padding preserves the same candidate words: it does not repair them.
All 11 neighboring raw/padded functions and normalized owner pools are exact.
No compiler profile or word guard is changed.

| Local | Retail SP Offset | Candidate SP Offset |
| --- | ---: | ---: |
| Delta vector | `0x9C` | `0xAC` |
| Output-pointer pair | `0xA8` | `0xB8` |
| Input-pointer pair | `0xB0` | `0xC0` |
| Emitted payload | `0xBC` | `0xC8` |
| Actor descriptor | `0xF0` | `0xFC` |
| Saved data pointer | `0x14C` | `0x154` |

The saved data pointer is at the same physical caller-SP-minus-four address,
but the other packet offsets and the live SP do not match. Opening V0/V1
allocation, cached multiplier/constant FPR roles, and transform-setup scheduling
also remain different. Do not describe these as two independent scheduling
words or install broad guards over the frame/packet differences.

Bounded screens reject scoped/register locals, reversed state predicates,
combined-workspace layouts, and an 8-byte-aligned descriptor proposal. The
alignment proposal gives frame `0x160`, not `0x150`; no original double/u64
descriptor field is claimed. The initial unsigned decrement produced 86
differences; the explicit signed byte load restores that instruction and leaves
the measured 85-word gap. Equal word counts are not matching evidence.

## Qualification And Rejection Evidence

Six final research tests pass in **47.767s**. Some deliberately assert the
remaining mismatches; this is not an installation acceptance result.

- 987 uniform-stack cases compare complete public memory and complete call
  packets across retail/raw/padded execution. The core corpus emits 42 records;
  additional cases cover provider mutations, repeated samples, signed counter
  endpoints, allocation failure and two stack phases.
- Seven model-only conversion-edge cases cover negative fractions, high
  unsigned values, overflow, infinity and NaN. Private callback mutations and
  invalid conversions are not claimed as portable native C behavior.
- The corpus reaches all **287 reachable retail words**. The remaining word,
  offset `0x8C` / VA `150F2DA0`, is an unreachable duplicate byte load.
- With nonuniform stack bytes, three records expose **nine actual public
  payload-padding differences**, at payload offsets `5..7`. Constructor
  descriptor bytes also differ at `6, 7, 0x4D, 0x4E, 0x4F`. These bytes are
  observed and asserted, not masked into a claimed complete public match.
- A paired fault at the first modeled memory access already differs in live
  SP by eight bytes. Full private/fault-prefix matching remains open.
- Two independently rebased links pass 24 uniform-stack public-protocol cases,
  varying globals across signed HI16 carry boundaries and rebinding callees.
- Native32 O2/O0 each pass **960 typed-object cases** with UBSan and six
  effective equality/signed-counter/payload-length negative controls. Native
  checks cover defined packet fields, not indeterminate padding or guest faults.
- The existing signed-LB implementation is reused through a local adapter,
  with six independently checked byte endpoints and access accounting. No
  shared interpreter is changed. Native compilation adds an explicit memcpy
  binding; no production workaround was needed for the fixture declaration.

Random, transform, basis and constructor providers have explicit bounded
contracts; their deeper implementations and complete dispatcher behavior are
not qualified here. The conversion/FCSR model is bounded, not hardware trap,
NaN-payload, general FCSR or gameplay acceptance. The callback entry at
`0x8008A658` / ROM `0x22F118` is checked and protected.

## Preserved Baseline And Resume

All **266 protected entries / 244 distinct paths** remain unchanged. The
complete production ELF is still
`5efb8a9f598af0712d97eaf4d0f2ab2df134e349ad16eddfeb0f75e74128b7d4`:
all 6,057 bodies and addresses, all 189,088 Game-data bytes / 720 owners,
guards, profiles, conversion rows and earlier checkpoint fixtures remain exact.
No new production build is claimed or needed for this uninstalled experiment.

Fresh match-progress remains Game **2,964 / 4,828 (61.39%)**, total
**3,637 / 5,501 (66.12%)**, 1,864 different and zero drift. Init and Debugger
remain 100% exact among converted functions. Root README is untouched because
its aggregate rows remain correct.

Tools **44ac35d** banks the candidate and six-test fixture before the consumer
docs/pin. Both tools copies freshly pass 12 shared tests and smoke checks;
four ASCII/AST parses and two identical task pairs pass. Both mirror destinations
were absent before copying. All 1,132 prior mirror hashes and HEAD `ddbdd16b`
remain unchanged; the mirror now has 1,134 dirty paths. No mirror commit/reset,
push, Claude call, host-port change or frozen Release action.

- [x] Recover the full routine and both packet layouts, with no production edit.
- [x] Verify bounded protocol/native behavior and expose private/public padding failures.
- [x] Preserve the complete installed baseline, prior checkpoints and mirror.
- [ ] Continue this **same function**: trace automatic-storage placement for
  the delta, pointer pairs and packet objects; recover frame `0x150` and retail
  offsets before fitting V0/V1, saved FPR roles and setup scheduling.
- [ ] Then qualify nonuniform padding, full private/fault behavior, callers and
  the complete first linked image before installation. Keep the 139-word gate,
  both fade lifetime gaps and broader Game goal open.

```sh
python3 -m tools.experiments.game_owner_burst_emitter
python3 -m unittest tools.tests.test_game_owner_burst_emitter -v
make -C conker match-progress NON_MATCHING=1
make tools-check
```
