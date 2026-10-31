# 1914 - Owner identity and value payload restored from direct C

Date: 2026-10-31. Function: `func_15109410`, owner
`conker/src/game/generated_1368C0.c`, VA `0x15109410..0x151094FC`,
ROM `0x1368C0..0x1369AC`. Tools checkpoint: `c66c713a7f8bafa0357a793c7525b3b5e1cc2e93`.

The zero-return placeholder is replaced with a semantic owner payload
constructor. All 59 words emit directly from C under the retail O2/g3
profile. No guards, insertions, omissions, compiler exceptions or alignment
words are needed. The 80-byte frame, return pointer, two call relocations,
argument homes and branch delay slots match retail.

## Recovered behavior and ABI

The signature is `void *(u8 *owner, s16 lifetime, s8 first, s8 second,
f32 value, u32 extraBytes, u8 selector, s32 category)`. A null owner returns
null without allocation. Negative signed 16-bit lifetimes request 300 ticks
with flag zero; other lifetimes retain their value and set flag one.

The 20-byte payload contains owner at offset zero, the captured byte
`owner[0x3B]` at offset four, zero at offset eight, the requested float at
offset twelve, and two signed settings at offsets sixteen and seventeen.
The identity is captured before allocation, so a helper that changes the
owner does not change the captured identity. Padding at offsets 5, 6, 7,
18 and 19 is preserved by the retail copy and is not initialized by this
source.

The original `func_15149130` signature is retained. Its kind and operation
are both `0x1A`; the size is the unsigned 32-bit sum of extraBytes and 20.
A successful allocation receives all 20 representation bytes at offset
`0x28`; failure returns null without copying. The returned pointer remains
the allocation base. The nearby `func_15109ED4` and `func_1510A344` bodies
are unchanged.

The alternative source was read as a hypothesis only. Its 32-bit read at
the unaligned byte field `0x3B` and integer return type were corrected using
the actual retail `lbu`, SDK allocator definition and call interfaces.
The matching C was reconstructed and independently compiled locally.

## Qualification evidence

- Eight fresh target checks passed separately in both tools copies, plus
  both shared tool checks. After installation, each copy ran two fresh
  source/image checks; six unchanged checks were reused only after complete
  input, module and qualified artifact fingerprint validation.
- All 59 instructions were exercised across 1,230 guest cases, with 3,690
  original/raw/padded executions. Tests connect the original 49-word
  allocator wrapper and 11-word copy routine, including allocation failure,
  signed settings, lifetime boundaries, raw float representations, seven
  wrapping size patterns, helper side effects, padding and returned pointer.
  Eight additional cases exercise two independent rebases. Guest traces,
  memory/register state and 89 access cuts, including five delay cuts,
  agree. These are emitted-instruction checks, not portable fault semantics.
- The original parent `func_150265CC` contributes two 15-word windows,
  with JAL sites at ROM `0x54A60` and `0x54A9C`. All 192 caller cases pass
  through original argument setup and connected allocator/copy code.
  The parent ignores the constructor result and returns one. The aligned
  retail census finds those two JAL sites and no literal function pointers.
  The complete parent and gameplay are outside this bounded caller claim.
- Native SDK32 checks pass 524,288 cases each at O0/O2/O3 with UBSan
  trapping, covering all 65,536 duration/signed-byte combinations, null
  owners, allocation outcomes, owner/output aliases, canaries and float
  representations. Another 1,024 cases per profile verify the unchanged
  neighboring identity constructor. Native checks copy all 20 representation
  bytes without assuming values for the five padding bytes.
- Fifteen independently compiled IDO and native semantic negative controls
  fail by explicit comparison. The reversed null gate initially trapped in
  its absent-owner case; the final corpus checks the present-owner case
  first and rejects it with a controlled mismatch. Compiler, interpreter and
  sanitizer errors are not accepted as successful negative controls.
- Complete raw/padded owner compilation preserves nine other functions and
  all pools with zero diagnostics. The actual three Make commands produce
  the qualified object exactly. No shared declarations or headers change.
- Independent full-image prediction equals the first link and production
  ELF: 174 changed bytes = 173 target code bytes + one target symbol extent
  byte. There are no metadata permutations or excluded ranges. All 6,055
  other linked function bodies and all 6,056 addresses are preserved.
  Protected Game data is exact across 189,088 bytes and 720 owners.

Production ELF SHA-256:
`4061e827bfdcdeb8fdb088993a5199851e594ec1779b81441c63cef68f90a4fc`.
The map, progress inventory CSV and complete inherited guard manifest are
unchanged. Qualification artifacts and machine receipts reside in
`conker/build/game-owner-state-payload-15109410-match/`.

## Installed recount and continuation

The actual adopted ELF recount is **3,991 / 5,506 (72.48%)** exact C
functions, Game **3,318 / 4,833 (68.65%)**, Init 492/492, Debugger 181/181,
and zero address drift. The 75% threshold is 4,130, requiring **139** more
verified functions. Conversion inventory totals remain unchanged.

Next screen: `func_15133EEC`. Other candidates remain uncredited. Tools are committed
before the consumer source/pin/docs. No push or host-port/Release changes
are part of this recovery. The scoped graph refresh covers eleven changed
files, preserves prior nodes and valid directed relationships, and retires
the two obsolete signed-return relationships for this pointer-returning
function. It makes no full-corpus, global clustering or gameplay claim.
