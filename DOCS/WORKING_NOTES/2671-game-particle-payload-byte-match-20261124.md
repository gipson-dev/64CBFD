# Particle payload creation byte match - 2026-11-24

`u8 *func_150B3F5C(f32 *source, ParticlePosition150B3F5C *position, s16 count)`
replaces its zero-return placeholder with the complete particle request,
payload and positional sound routine. The source emits **99 words / frame
184**, with seven relocation binding sites. **97 words match directly**;
two guarded words restore the order of disjoint packet stores. All 99 words
have expected-word and relocation checks, with zero insertions or omissions.

Production rises from **4,650 to 4,651 / 5,528 (84.14%)**, Game **3,978 / 4,855
(81.94%)**. Init remains 492/492 and Debugger 181/181; zero address drift,
877 functions still different, **48 more matches needed for 85%**.
Only this function receives matching credit.

Original `conker/asm/E1280.s:119`, VA `150B3F5C..150B40E8`, ROM
`E140C..E1598`, 396 bytes. Owner `conker/src/game/generated_E1280.c` retains
all nine other raw and padded definitions, bindings, pools and diagnostics;
this does not claim that those nine functions are all matched.

## Recovered behavior and ABI

1. Copy 64 bytes from the source into an 88-byte private payload. Reread the
   live source floats +0x14/+0x18 after the copy provider, add them in retail
   FPU operand order, and store the result at payload +0x40/+0x4C. Clear the
   two float fields and byte flags at +0x44/+0x54 and +0x48/+0x50.
2. Copy the 12-byte position into a 28-byte request, set lifetime 500, flags
   2, kind 9 and the low byte of the signed halfword count at +0x15.
   Unwritten request and payload bytes remain unwritten. Do not add a memset.
3. Call the existing eleven-argument `func_15147A80` factory with payload
   size 88, entry size 36, three 7s, zero optional/resource values, channel
   255 and context 1. Return NULL immediately on failure.
4. On success, call the retained RNG and reread the live position. Truncate
   each float to signed 32 bits and then narrow to signed 16 bits for sound
   0x221, volume 25000, pitch 4000, range 600, callback-address word
   `func_1000EF40`, zero optional arguments, value 8 and random mask 0x40.
5. Reread the created object's payload pointer at +0x98 after audio, copy
   all 88 payload bytes there, and return the created object.

The declarations follow the actual factory, sound, callback and SDK memcpy
interfaces. `memcpy` uses `size_t`. The frame retains RA +0x34, created pointer
+0x40, payload +0x44, request +0x9C, and the incoming argument homes. Twelve
outgoing sound words occupy 48 bytes below the saved RA.

## Store scheduling proof and limits

The raw C instruction pair at words 17/18 stores the count byte at SP+177
and F0 at SP+136. Retail schedules them in the reverse order. An independent
decoder, which does not import the normalizer, proves that the disjoint
valid-frame writes commute for arbitrary register/FP values. The other 97
words and all seven bindings are unchanged. No branch, delay slot or provider
enters the pair. The normalizer pins the entire raw body and binding digest.
It does not change any FPU arithmetic or operand order.

This proof requires both valid stack writes to succeed. Raw intermediate
fault-prefix identity is explicitly excluded; only the normalized outputs
and retail receive that comparison. Complete raw results and traces compare
after exactly one proved adjacent-store commutation. Four structural negative
controls reject store overlap, wrong FP source and other changed words.

## Fresh qualification

- **156 cases per stream** compare raw C, generic/generated padding and
  retail: every public/private byte, seeded unwritten padding, registers,
  calls, copied bytes and normalized traces. All 99 retail words execute.
  Counts cover negative, zero, byte wrap and incoming high bits. Providers
  change source, position, incoming homes and the final payload destination.
- **139 normalized/retail fault-prefix triples** compare full state and
  dispatched accesses. They make no portable C fault-semantics claim.
- Seven cases per stream execute the original **115-word factory** and
  **11-word memcpy**. Allocation and bzero remain bounded providers. The
  retained MIPS3 RNG and actual audio/callback implementations are not claimed
  as executed by this 32-bit oracle.
- Both direct caller windows execute original code: four words at
  150B2DC8 and eleven at 150B669C, four cases each per stream. Arguments,
  delay-slot stores, copied data, target frame and saved registers agree.
  The complete 477/148-word caller functions and epilogues are outside scope.
  Their current C definitions remain placeholders and contain no C call to
  this target; no existing C caller declaration requires a relay repair.
- **144 SDK32 native cases each at -O0/-O2/-O3**, with strict aliasing and
  UBSan, verify typed packet fields, raw source bytes, live provider effects,
  callback address encoding and output guards. Native comparisons exclude
  unspecified padding, cross-object aliases and incoming-home mutations.
  Coordinate conversions cover finite signed-32 representable values; invalid
  conversions and hardware FCSR behavior remain outside this native claim.
- **16 effective source controls** fail known call/result comparisons.
  Signals and sanitizer traps do not count as successful controls.
- Both padders reject all tested word/binding corruptions: **212 controls**,
  covering 99 source words and seven relocation sites. Four independent
  code/callee/callback arrangements pass **12 GNU links / 96 guest runs**.

## Full image, production and bank

Actual Make replays the owner's three real commands and reproduces the
complete generated-padder object. The independent image uses frozen-before C
and original target ASM, reconstructing symbol/string metadata and retaining
all anchors. Production equals that prediction literally: **296 changed
bytes, zero exclusions**. All 189,088 protected Game data bytes across 720
owners, unrelated objects/definitions/addresses/extents and the conversion
CSV remain fixed. The existing guard CSV is retained byte-for-byte as a
prefix; exactly 99 target-only rows are appended. Holding that dependency
old during targeted production Make avoids unrelated rebuilds; the changed
source forces this owner to compile, and full frozen-input/image audits
verify every other output. Live recount adds exactly one match.

ELF SHA256: `ca229614ff7bf5dbf1dcf3b434df2078414b2f08e6f056a1bce9d73eb0193f55`.
Raw body SHA256: `81192ac16816e06e5dffb951c3f54080bd099f234c3e8456c487097adeebb931`.
Padded owner SHA256: `44daac24acde72a4669d4b0ce16e3879f28e828ee3c4f872e4c52dac60155320`.

| Phase | Time | Gates |
| --- | --- | --- |
| preinstall-primary | 149.893s | 5 fresh / 0 reused |
| preinstall-sibling | 163.389s | 5 fresh / 0 reused |
| installed-primary | 164.187s | 5 fresh / 0 reused |
| installed-sibling | 160.452s | 5 fresh / 0 reused |

Shared tools-check passes. Tools commit
`6045e0820d8214fcc96c6cebc696b395deb88f2d` precedes the source/guards/pin/docs
commit. Both tracked trees are clean at the bank, and the real dirty sibling
tools checkout is preserved. No push. Codex used zero Claude calls. Immutable
inputs are verified once per fresh suite process; full native bank audits
bracket adoption and production. Graph receipts distinguish normal update,
observed hook completion, scoped AST merge and old-ID/qualification retention.
This is not full-corpus re-extraction. Host applicability is audited separately;
no host/Release edit or build is included. Root README receives aggregate rows
only; five DOCS indexes receive concise entries preserving all prior bytes.
The 85% goal remains active. Renderer 15197148 remains private on its older
baseline.
