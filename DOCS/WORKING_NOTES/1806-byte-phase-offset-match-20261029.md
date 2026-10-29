# Byte phase offsets and caller ABI: guarded C match

Verified 2026-10-29. `func_15131C84` replaces its zero-return placeholder in
`conker/src/game/generated_15D730.c`. Semantic C emits all 50 instructions
with the original 24-byte frame and four symbol bindings. Two expected-word
guards exchange only the source operands of independent `mul.s` instructions.
The corrected declaration and call in `generated_1BF090.c` preserve that
entire caller object's bytes.

The adopted live ELF recount is **3,884 / 5,506 (70.54%)** byte-exact C
functions: Game **3,211 / 4,833 (66.44%)**, Init 492/492 and Debugger 181/181.
There is no address drift; 1,622 C functions still differ. The 75% target is
4,130 exact functions, leaving **246**. Conversion inventory is unchanged.

## Recovered behavior and interface

The routine takes two byte phases, two signed byte rates, a floating base,
two floating amplitudes and two output pointers. It advances both phase bytes
by rate times the live tick count, wrapping modulo 256, before calling the
trigonometric helper. Each helper argument is the updated phase minus 64,
also wrapped to a byte. Each output is the corresponding helper sample times
its amplitude, plus the base.

The original preloads the second phase before storing the first, but reloads
the tick count and second rate after that store. Amplitudes, base and output
pointers are loaded after each helper call. The first output store precedes
the second phase/amplitude reads. Qualification preserves these observable
orders, including aliases and guest argument-home mutations.

The recovered signature is:

```c
void func_15131C84(u8 *phases, s8 *rates, f32 base, f32 *amplitudes,
                  f32 *first, f32 *second);
```

Both original callers ignore the result and return one. The existing C caller
`func_15192308` previously declared an integer result and integer third
argument. Its declaration now uses `void`, typed pointers and `f32`; the call
loads its base as a float. The third argument still travels in A2 as the same
32-bit representation. All eight functions, relocations, pools and complete
padded object in that caller owner are unchanged.

| Evidence | Value |
| --- | --- |
| Virtual range | `0x15131C84..0x15131D4C` |
| Retail ROM range | `0x15F134..0x15F1FC` |
| Target owner | `generated_15D730`, 31 compact functions |
| Tick bindings | `D_800BE9E4`, HI16 at byte 8 and LO16 at byte 12 |
| Helper calls | `R_MIPS_26 func_151423D8` at bytes 100 and 152 |
| Guard at byte 128 | `0x46002182` to `0x46040182` |
| Guard at byte 176 | `0x46008482` to `0x46100482` |
| Raw object body SHA-256 | `909d1483c867a7dc9c3f3de5f87bec95709180803439c490a7620c05d3689612` |
| Normalized object body SHA-256 | `35c58ca334568ccb9993ec3ba04305fb7d3568b619fe4881f0464877021b2437` |
| Retail slot SHA-256 | `d1e213d664f794ec9c1be945792375c3b578b5deabac87aba7601fb8c1a9a69f` |
| Adopted ELF SHA-256 | `1ce16ec7808c68d91ffe727a183b4099f94431b85b07209cf6c3e9a614e120b5` |

There are no inserted/deleted instructions or register-allocation cycles.
The guard manifest retains its exact inherited prefix and appends two rows.

## Qualification

The private suite and both independent tools copies pass all eight methods;
shared project-tools checks pass in both copies. Production reruns the two
installed-source/image checks per copy and reuses six semantic checks only
after verifying complete input, module and artifact fingerprints.

- 1,640 direct guest cases cover all 50 instructions, phase/rate byte lanes,
  live tick reloads, 40 alias/rounding vectors and first-output-before-second-read
  ordering. Legal volatile-register and outgoing-home clobbers occur at calls.
- 512 connected cases execute all 27 original words of `func_151423D8`, using
  its unchanged 65-float, 260-byte table. The current helper already has exact
  C; this recovery gives it no additional matching credit.
- Sixteen cases execute both complete 20-word original callers,
  `func_15131D9C` and `func_15192308`. Their only aligned retail JALs are at
  ROM `0x15F27C` and `0x1BF7E8`. The first is retained GLOBAL_ASM; the second
  is qualified from its corrected C and actual Make output as well.
- Native32 SDK builds pass 18,432 vectors and 256 actual-C-caller cases per
  profile at `-O0`, `-O2`, `-O3`, with trapping UBSan, valid backing and
  canaries. Ten compiled incorrect implementations fail observable tests at
  every profile. Guest argument-home mutation is separate from native scalar
  parameter semantics. Floating tests use default rounding; FCSR, hardware
  exceptions and architecture-specific NaN payloads are outside this scope.
- Signed and unsigned rate loads have the same public modulo-256 result.
  The raw instruction gate rejects an unsigned load where retail uses `lb`;
  public-output tests explicitly establish their modulo equivalence instead
  of claiming a false behavioral distinction.
- 294 paired access-fault prefixes include twelve delay-slot cuts, comparing
  RAM, registers, PC, delay state and access trace. These establish emitted
  access order, not portable C fault behavior.
- Three GNU link layouts pass 36 cases. All 50 word and four binding
  corruptions are rejected, as are four actual-padder guard corruptions and
  ten whole-image corruption controls.

Private preparation corrected doubled blank lines introduced by a Windows
text write and an oracle fixture that included one extra word after each
caller. The original artifacts are retained under `superseded-format-v1/`.
The cleaned source produces the same object and image; both callers are
exactly 20 words. All final tests use the corrected fixtures and source.

## Build, preservation and commit boundaries

Before/after target-owner compiles and the actual five-command Make rule
agree with the selected object. All thirty neighboring functions, including
two retained GLOBAL_ASM entries, relocations and normalized pools remain
unchanged. There are no target-owner compiler diagnostics.

The caller's actual three-command Make rule reproduces its entire prior
object. Its one inherited Warning 712 remains at the unchanged
`func_1519257C` call on line 29, passing an integer to a pointer parameter.
Qualification checks that exact diagnostic and source line; it does not claim
the caller owner is warning-free.

Production reproduces the qualified private image. Independent prediction
permits exactly **155 changed bytes**: 154 target-code bytes and one
symbol-size byte. There are no metadata moves or exclusions. All 6,056
disassembled function addresses and 6,055 other bodies are preserved, as are
189,088 protected Game data bytes across 720 owners and conversion inventory.

473 focused inputs and 16,540 sealed current inputs are verified. The older
standalone tools mirror keeps its 1,859 inherited dirty paths plus the three
new qualification modules; it is not committed or reset. Tools are banked
first in `fac4e7f10befb1cca2c0a49c4129bc60dea1a5b7`; the consumer commit
contains both C sources, the appended guards, tools pin and measured docs.
No push or sibling host/Release changes are part of this work.

Ignored receipts live in `conker/build/game-byte-phase-offset-match/`.
After the consumer commit, `FINAL_AUDIT.json`, `BANKED_STATUS.json` and the
banked input seal record the independent final audit. The graph refresh is
limited to twelve changed source/document/tool files, preserving old nodes
and valid directed relationships and retiring only source-proven obsolete
return-type relationships. Historical global analytics are not recomputed
or represented as fresh full-corpus extraction.

## Next work

Inspect `func_150C7670` in `generated_F4B20.c`, the next unparked placeholder
in the measured queue, at 51 words. Recover its ABI, original callers and
owner constraints before giving it credit. `func_1514E920` remains parked and
uncredited. The 75% goal stays active.
