# Game reverse-slot update match - 2026-09-26

## Result

`func_1515D030` is byte-exact across all 22 words and 88 bytes at
`0x1515D030..0x1515D088`. Fresh totals are 2,719 / 5,469 exact C functions
overall and 2,148 / 4,791 in Game.

## Recovery

The routine decrements an active count and moves a signed slot cursor backward
when at least three entries remain. A negative cursor wraps to the final slot.
The existing behavior was correct, but early returns made IDO generate two
independent return blocks, and the post-decrement spelling loaded the cursor
as unsigned.

Initializing one `result` local to true, assigning false in the short path,
and returning it once reproduces retail's branch-likely false assignment and
shared return path. Assigning `(s8)arg0[0x2E] - 1` reproduces the signed `lb`
before the decrement. No retail-word patch is used.

## Evidence

Linked ELF offset `0x19D030` and decompressed retail offset `0x18A4E0` compare
equal for 88 bytes, both with SHA-256
`52ace76263f53fd9e73fcad2e3e753d4bdd6d1060db7b2381385b6662dce7021`.

| Section | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: |
| Total | 2,719 / 5,469 (49.72%) | 1 | 2,749 |
| Init | 390 / 497 (78.47%) | 1 | 106 |
| Game | 2,148 / 4,791 (44.83%) | 0 | 2,643 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

## Parked measurements

- `guMtxIdentF`: canonical SDK nested-loop source is confirmed, but tested
  current IDO `-O`, `-O2`, and `-O3` profiles do not emit retail's unrolled
  20-word store body. Hand-unrolled C changes FP-zero allocation or ordering.
- `func_1506EF5C`: removing the cached object pointer reproduces retail's four
  object reloads and exact 22-word instruction skeleton, but all live registers
  differ. Typed-array and lifetime-order experiments do not correct allocation.
- `func_1507A4D4`: one packed-mask local restores the late object access, but
  the first two byte loads and the final OR tree remain independently
  scheduled. Split, incremental, explicit-byte, and complement forms regress
  allocation, scheduling, or span size.

All unsuccessful probes were removed and the three functions were rebuilt
from their pre-investigation source before this checkpoint.

## Validation

The focused object and full link, fresh progress and matcher, independent
88-byte span comparison, replacement build, project tool checks, all six
padding-tool unit tests, outer build, and `git diff --check` pass.

## Next boundary

Continue with 23-word `func_15178750`. Keep the three measured compiler
boundaries above parked unless new compiler or provenance evidence appears.
