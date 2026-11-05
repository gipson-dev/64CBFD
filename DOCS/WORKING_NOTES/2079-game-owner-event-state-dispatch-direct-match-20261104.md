# Working Note 2079: Game owner event-state dispatch direct match

Date: 2026-11-04

## Result

`func_151C86AC` at `0x151C86AC` now replaces its zero-return placeholder
with semantic C. The owner `generated_1F4650` emits all 64 retail words with
the original 24-byte frame and no expected-word guards.

The routine is not reached by a direct `jal`. Its sole aligned retail pointer
is ROM `0x22EA30`, callback slot `D_80089F64[3]`. The recovered callback ABI
is:

```c
void func_151C86AC(u8 *owner, u8 *event, u8 eventCode);
```

The third parameter is an unsigned byte. This is material: IDO emits the
retail argument home, low-byte narrowing, and `a2` register lifetime from that
type. The callback returns no value.

## Recovered behavior

The low byte of the event code selects two routes:

- Event `0x20` requires owner-state flag `0x10` and equality between owner
  state word `+0x28` and event word `+4`. It validates the event through
  `func_151C87E0(event->word0, owner)` and, on success, forwards the same pair
  to `func_151C899C`.
- Event `0x3A` first requires owner word `+0x138` to equal event word zero.
  Selector byte zero sets state bit two, selector one clears it, and selector
  two calls `func_151C899C(NULL, owner)`.
- Other event codes and failed gates leave the owner unchanged.

The donor's apparent four-argument helper calls were rejected. `a2` and `a3`
merely retain the event code and pointer at those call sites; both helpers are
called with two semantic arguments. Preserving that distinction eliminates a
false local spill and reproduces retail's 24-byte frame.

The exact source also takes the address of the owner parameter. This keeps the
owner in its incoming ABI home across calls without introducing a saved
register. Expressing the identity comparison as state-relative `+0x28`
allows IDO to schedule the equivalent owner `+0x138` load and state-base
advance exactly as retail did. The `0xFFFD` clear mask preserves the original
promoted integer operation.

## Byte and relocation proof

The retail `-O2 -g3` profile produces:

- 64 / 64 linked words equal to retail;
- frame `0x18` in both natural C and retail;
- no guards, inserted words, omitted words, or exclusions;
- `R_MIPS_26` calls to `func_151C87E0` at `+0x068` and
  `func_151C899C` at `+0x07C` and `+0x0E8`.

The compact target body SHA-256 is
`cd22afb41cc9617da662a270199edbab25ea6902758bfdb82da4f15c72d69e61`.
The linked target and retail span SHA-256 is
`aec69e41677220ab8f52285c6c06ed15f3a0d156593353319cd958b65f9cb8c5`.

## Behavioral qualification

The big-endian guest model executes 222 cases per body across both stack
phases. It covers event-code low-byte aliases, gate success and failure,
identity equality and inequality, validation success and failure, all five
sampled selectors, both bit mutations, the null dispatch, and unrelated event
codes. Retail and natural C each visit all 63 reachable words. Word
`0x151C8774` is a statically exact duplicate load stranded between an
unconditional branch and the next target, so it is not executable.

Native 32-bit C passes 4,096 cases under each of `-O0`, `-O2`, and `-O3`, for
12,288 positive executions. Ten controls are rejected: both wrong event
codes, wrong gate bit, wrong state fields, inverted validation, wrong action
arguments, and wrong set/clear masks. Injected memory failures produce 102
observations across 25 unique active boundaries. Callback slot
`D_80089F64[3]` remains the sole reference.

The focused installed suite passes all four tests in 61.668 seconds. The
shared match-progress, generated-PC16, guarded-object, and protected-data
suite passes all 19 tests in 18.930 seconds.

## Image and production closure

The predecessor and qualified owners preserve all 45 neighboring functions.
The strict 6,052-function image changes only `func_151C86AC`, keeps every
function address fixed, and uses zero exclusions. All 189,088 protected Game
data bytes across 720 owners remain exact.

The actual Make owner rule rebuilt `generated_1F4650`, and the production
owner and ELF equal the independently predicted qualified artifacts. The
broad `make all` path rebuilt the binary and stopped only at the expected
final retail SHA check. The inherited duplicate `generated_12D630` recipe
warning is unchanged.

| Artifact | SHA-256 |
| --- | --- |
| Qualified / production owner object | `335da158d1122d7640df8c9917c05ebf28f0179d6b1ed7f391a120737f1a16b8` |
| Qualified / production linked ELF | `fd81b5d15136d9e5062165e7e957bd7a8f651b08c43abd578977ef2e48fe7ff9` |
| Production rebuilt ROM image | `4c993d67de6d01a0e69464ec4fc5a6fc72034b351eb624b0d7e7a384a439a3dc` |
| Production map | `2ab021cc02cab424a5dae0e96a4ed5df1fe5f65ea58964f8e4e04b689771fbeb` |
| Installed owner source | `e4039cf24fa53a7050cb3d70ee8711b6f01243e0f6c6a8fa835b542630df62d9` |
| Guard table, unchanged | `8516b4ea5fc16f8ad49f0108159cb5e4f7e5424d27cc38b758d1d45f76671c89` |
| Retail layout, unchanged | `67a28e9dfe6bd0dc21e3a386966e69f7507a8e1628dc0f67d46425ac297dadcb` |

## Recount and continuation

The fresh production ELF reports:

- Total: **4,150 / 5,512 (75.29%)**, zero address drift, 1,362 different.
- Init: **492 / 492 (100.00%)**, zero drift.
- Game: **3,477 / 4,839 (71.85%)**, zero drift, 1,362 different.
- Debugger: **181 / 181 (100.00%)**, zero drift.

The converted inventory remains 5,512 / 6,046 functions. The active 80%
threshold is 4,410 exact functions, so **260 more** are needed.

The refreshed ordinary queue continues at `func_150C2700` (65 words, 64 real
differences), followed by the tied 64-difference group. Keep the seven
documented handwritten/custom-ABI/boundary rows (`func_150A76F0`,
`func_151F8870`, `func_150A613C`, `func_150AE280`, `func_15115F68`,
`func_151AE2BC`, and `func_150A6760`) separate until their specific
boundaries are addressed.

## Graph retention

The retained graph baseline was 58,543 nodes / 112,390 links with SHA-256
`8e9f65e87fac857b43db4cbffd8af512395786e6212ebf63a75efc19a4a20579`.
The standard reduced `graphify update .` extracted eight uncached inputs but
proposed only 24,749 nodes, so Graphify correctly refused to overwrite the
retained corpus. Its fail-closed report retained 31,816 nodes from 3,754
still-present files outside the reduced scan.

An explicit ten-path incremental rebuild with `force=False` then produced
58,551 nodes, 112,398 links, and 5,073 communities. It retained 58,540 /
58,543 prior node IDs and removed no ID outside the changed-path set. The
three replaced IDs are line-derived `DOCS/UPDATE_LOG.md` headings; eleven IDs
were added for their relocated forms and the new Note 2079 document and
sections. The qualified graph SHA-256 is
`2b64014e728ada63fa591630bff845c778a5241c3a9ffd2097f09d76fbe24ee7`.

After adding this receipt, a one-path stabilization retained all 58,551
existing node IDs and added only the new `Graph retention` heading. The final
graph has 58,552 nodes, 112,399 links, 5,098 communities, and SHA-256
`bfe80b395ab84d2843ef215ed3bee163646cb17282f8aee715297125c801141f`.
