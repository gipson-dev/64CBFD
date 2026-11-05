# Working Note 2084: Game object-follow update direct match

Date: 2026-11-04

## Recovery and callback contract

`func_1515BFA8` occupies `0x1515BFA8..0x1515C0B8`, ROM
`0x189458..0x189568`, in `generated_188F90.c`: **68 words / 272 bytes**.
Its zero-return placeholder is replaced by a typed, void callback receiving
one writable object-follow record. The record retains its object pointer at
`+0x18`, identity byte at `+0x1C`, flags at `+0x1D`, signed timer at `+0x1E`,
current XYZ at `+0x20`, previous XYZ at `+0x2C`, and velocity at `+0x38`.

Flag bit zero enables the tick subtraction. The subtraction wraps to the
stored signed 16-bit timer; explicit unsigned intermediate arithmetic also
defines the word-overflow cases. A negative result requests retirement. The
callback still reads object liveness and identity after that timer decision.
An inactive object or mismatched identity also requests retirement through
`func_1516972C(record)`.

Otherwise, it copies current XYZ to previous XYZ, reloads the object pointer,
copies the object's XYZ from `+0x14/+0x18/+0x1C`, then writes each velocity
component as **(previous - current) * D_800BE9A8**. The scale is read separately
for all three components; a cached value changes observable alias behavior.
Reserved bytes remain untouched.

The sole aligned retail pointer is ROM `0x230990`, VA `0x8008BED0`, the
callback in **D_8008B4A8[0x32].unk0**, with descriptor stride `0x34`.
No direct JAL references exist. The original `func_151670C0` dispatcher calls
it at JALR `0x15167170`, passing the record in A0 and ignoring the return.
Its delay slot saves the already-loaded next record before the callback.

## Exact compilation and behavioral evidence

The complete body emits all **68 retail words directly** under the existing
`-O2 -g3` owner profile, including the original **24-byte frame**. No guards,
insertions, omissions, profile changes, or shared declarations are needed.
All five natural bindings remain exact: the HI16/LO16 pairs for
`D_800BE9E4` and `D_800BE9A8`, and the call to `func_1516972C`.

The focused suite passes before and after installation:

- **2,016 cases per body**, covering every instruction, flag/timer boundaries,
  signed word tick extremes, inactive/stale records, both stack phases, signed
  zeros, subnormals, finite extrema, infinities, and quiet NaNs.
- **48 alias cases per body** across six layouts, including record/scale and
  record/object overlap. A separately compiled cached-scale control is rejected.
- Native32 O0/O2/O3 pass **12,288 executions** with undefined-behavior traps;
  **15 compiled semantic controls** are rejected.
- **132 fault observations / 43 unique active boundaries** qualify emitted
  access order. **16 connected cases** execute the original four-word
  dispatcher window through the callback and return, checking its next-record
  store, call trace, and saved registers.

The retirement helper is a bounded clobbering provider in these tests; its
full implementation and full-game execution are not qualified by this note.
Guest fault prefixes are instruction evidence, not portable C fault semantics.
The cached-scale control initially placed a declaration after statements,
which IDO rejected. Moving that control's declaration to the local declaration
block corrected the fixture; the selected body was unchanged.

All **five installed tests pass in 41.553 seconds**. Shared match-progress,
PC16, word-guard, and protected-data regressions pass **19 tests in 6.025
seconds**. `make tools-check` passes. Routine work used zero Claude calls.
The standalone tools checkout's pre-existing dirty work is preserved; these
fresh target receipts belong to the mounted tools checkout.

## Whole-image and production audit

The independently compiled/padded owner preserves **ten neighbors** and its
normalized pools. Across **6,052 linked functions**, only this target's body
changes, and every address remains fixed. The entire ELF is reconstructed by
replacing the target instruction span and updating its named symbol extent
from 12 to 272 bytes: exactly **202 changed bytes**, with **zero exclusions**.
Corruption inside and outside the target span is rejected.

All **189,088 protected Game-data bytes / 720 owners** remain exact, SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

| Artifact | SHA-256 |
| --- | --- |
| Natural target before relocation | `1a99704973315185196aac958b0c9161a53539fb9731329773fc41a2521791a1` |
| Linked target / retail | `3d4b93b8301d2b23626a7bc16a33000b90840454052c5b36efd36928998959dc` |
| Qualified / production owner | `9b8a280fecdeea48397376a672d5d6d4483ad7aa68de0abe0b6d57a57118cfde` |
| Frozen predecessor ELF | `92b4ed1166612a791154a72a680449cbeafae6eb8ef320422f338c9e546e57db` |
| Qualified / production ELF | `b775949211d110993c2e819b0c15135c0e21f92b74bd8dac61f5996a4ff3fdbb` |
| Production code image | `bd34425b743c8da3c28a7702bc00c82e8361199028c68c7d521690c0de384093` |
| Production map, unchanged | `2ab021cc02cab424a5dae0e96a4ed5df1fe5f65ea58964f8e4e04b689771fbeb` |

Actual Make recompiles this owner and links successfully. `make all` writes
the binary and stops only at the expected retail SHA-1 mismatch. The inherited
duplicate `generated_12D630` recipe warning remains; this owner adds no new
diagnostics. The guard CSV, conversion CSV, and Makefile remain byte-identical
to the frozen predecessor.

## Authoritative recount and continuation

| Section | Exact C functions | Address drift | Different |
| --- | ---: | ---: | ---: |
| Total | **4,155 / 5,512 (75.38%)** | 0 | 1,357 |
| Init | **492 / 492 (100.00%)** | 0 | 0 |
| Game | **3,482 / 4,839 (71.96%)** | 0 | 1,357 |
| Debugger | **181 / 181 (100.00%)** | 0 | 0 |

Converted inventory remains 5,512 / 6,046. The active 80% target requires
4,410 exact functions, **255 more**. Continue at ordinary candidate
`func_1517A84C`, followed by the tied ordinary candidates in the fresh recount.
Keep the seven previously documented custom-ABI/compiler boundaries separate.

Reproduce under the prepared WSL toolchain from the consumer root:

```sh
python3 -m tools.experiments.game_object_follow_update_match
python3 -m unittest tools.tests.test_game_object_follow_update_match -v
make -C conker -j4 build/conker.us.elf
make -C conker all
```

## Graph retention

The frozen graph has **58,589 nodes / 112,363 links / 5,188 communities**,
SHA-256 `089130a69286337eae36eae43a62fb4f161642926a217c5cbdabe3b1e716b215`.
The standard reduced update extracts eight uncached paths but proposes only
24,795 nodes, so it correctly refuses to overwrite the retained corpus. The
explicit seven-path refresh with `force=False` produces **58,597 nodes /
112,369 links / 5,137 communities**, retaining **58,586 / 58,589** prior IDs.
No prior ID is removed outside changed paths. Three line-derived Update Log
IDs relocate; eleven IDs are added, including seven Note 2084 nodes and one
new inferred type node. The corpus warning retains 31,816 nodes from 3,754
still-present files outside the reduced scan.

Qualified graph SHA-256:
`5af8548a03f68d8c1dfadd75deea6324b067150244cd439c528568a940c5dacf`.
This is a scoped AST refresh with zero semantic LLM calls, not a fresh
full-corpus extraction. A final one-path note refresh checks stabilization.
