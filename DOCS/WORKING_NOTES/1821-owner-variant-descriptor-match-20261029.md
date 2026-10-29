# Owner variant descriptor direct C match

Verified 2026-10-29. `func_150D10E4` is adopted from its zero-return placeholder
in `conker/src/game/generated_FDD70.c`. VA `0x150D10E4..0x150D11B4`, ROM
`0xFE594..0xFE664`: 52 words / 208 bytes, 88-byte frame. All words emit directly
from semantic C using the normal O2/g3 compiler profile. No guards, alignment,
insertions, omissions, shared header changes or compiler-profile changes.

## Recovered contract

`void *func_150D10E4(u8 *owner, u8 variant)` constructs the established 60-byte
descriptor on its stack and returns the constructor pointer, including null
on allocation failure. The variant's low byte selects -30 for nonzero and +30
for zero. The original caller ignores the pointer. The owner ID is captured
from `owner+0x3B`; the pointer, zero fields, callback selectors 6/7/-1/-1,
mode 2, active frames 50, restart delay 22, lifetime 2000 and raw float rate
`D_800A0890` are supplied to `func_15134DAC(packet,0)`.

The offset field's physical meaning is not established; the source comment
deliberately calls it a signed offset. Padding remains uninitialized as in
retail; native C tests compare only defined fields. The packet begins at
frame+0x1C / incoming SP-60. Bindings are global HI16/LO16 at offsets 92/96
and constructor JAL at 184. Selected and complete-owner raw bytes match the
original assembled object, SHA256
`2384616d6715080829c7f65476e7c5ac276e0ccc311d69ba04b9f99ed1079478`.

## Qualification

- Eight fresh canonical checks in each tools copy, plus both shared tools
  checks; two fresh installed checks per copy and six explicitly reused
  semantic checks under identical module/input/artifact fingerprints.
- 608 guest cases cover all variant bytes, high incoming-home bits, sparse
  addresses, aliases, raw NaN/infinity bits and all 60 packet bytes including
  original padding. All 52 instruction addresses are covered. Complete state,
  call, memory and access traces agree for retail, selected C and padded C.
- 160 connected cases execute all 39 original constructor words and all 11
  original memcpy words. The allocation service is bounded. Both existing
  linked helper bodies are independently confirmed byte-exact; no helper
  source changes or additional matching credit are included.
- The only two aligned JAL references in the full ROM are at `0x1C29B0` and
  `0x1C29BC`; no aligned pointer registrations. The original six-word caller
  window `0x151954FC..0x15195514`, inside `func_151951E0`, passes 48 cases,
  invoking the target with S0/variant0 and S1/variant1. The current parent C
  remains a placeholder. No complete parent execution or gameplay claim.
- Native32 SDK O0/O2/O3 each pass 262,144 defined cases with trapping UBSan
  and canaries. Nine compiled semantic controls reject independently in
  guest and native checks. Three GNU rebases pass 96 cases, preserving all
  four original/Make/padded/selected instruction images and signed-low carries.
- 546 guest fault-prefix pairs include 196 delay-slot cuts. These establish
  emitted guest instruction order, not portable C fault or hardware FCSR behavior.
- 55 raw/binding corruption controls and 233 complete-image corruption
  controls reject. The actual Make compiler/padder/assembler path has three
  commands, no warnings and four unchanged neighboring functions.

## Linked audit and measured progress

The independently predicted full ELF equals the actual production build.
The complete delta is 168 bytes: 157 target instruction bytes, one function
extent byte and ten bytes from one closed GNU symbol bucket swap
(`D_8009943C` / `D_8009EE3C`). Both original definitions and serialized slots
are validated before prediction. Zero exclusions. All 6,056 addresses and
6,055 other function bodies, 189,088 protected Game data bytes / 720 owners,
the guard CSV, conversion inventory and map are preserved.

Fresh recount of captured live ELF: **3,899 / 5,506 (70.81%)**;
Game **3,226 / 4,833 (66.75%)**; Init492/492; Debugger181/181; zero drift.
**231 more** exact C functions reach 4,130 / 5,506 (75%).

ELF SHA256 `b8c35254472ac16519fa663b71c395823c265508a604f2bf5f0fcae50c07d44e`.
Object SHA256 `ce22456e1cc4279095fdd900026b7f605350580d98a1b36ce34ffc705bad76c3`.
Tools are committed first as `7e259bf`; consumer commit follows this note.
The older tools mirror retains all 1,904 inherited dirty paths, plus only
the three new qualification modules. No push, mirror commit or host change.

## Resume

Evidence: `conker/build/game-owner-variant-descriptor-match/` holds the frozen
648 focused inputs, 16,645-file seal, canonical/installed receipts, independent
image prediction, production build, recount and graph/final audits. Graph
refresh is scoped to the changed sources; no full-corpus or global analytics
refresh is claimed. Keep the 75% goal active. Next screen `func_15190770`;
next note1822. `func_1514E920` and `func_151D7000` remain parked and uncredited.
