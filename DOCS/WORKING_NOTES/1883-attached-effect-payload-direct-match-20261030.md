# 1883 - Attached effect payload constructor direct C match - 2026-10-30

`func_150ECA68` replaces its zero-return placeholder with a semantic attached-effect
constructor in `conker/src/game/generated_1199D0.c`. All **57 words / 228 bytes**
emit directly from C under the existing O2/g3 profile. Both relocation bindings
match; **no guards, insertions, omissions or profile changes** are needed.

Tools commit: `fd96793e3d672d55f82c34e4375eb0960aabc545`. Ignored evidence:
`conker/build/game-attached-effect-payload-150ECA68-match/`.

## Recovered behavior and interface

The nine arguments are an owner byte pointer, five unsigned setting bytes, a
signed 16-bit duration, an unsigned selector byte and a signed 32-bit category.
The routine captures the owner pointer and its identity at offset `0x3B`, followed
by the five setting bytes. A duration of `-1` selects 300 frames and allocation
flag 0; every other signed duration passes through with flag 1.

The allocation request to `func_15149130` uses callbacks `-1, 0x5D, -1`, request
byte `0x45`, a payload size of 12, the selector and category. On success it copies
all 12 payload bytes to the created object at offset `0x28`; on failure it skips
the copy. The function has a void return and its caller ignores the result.

The shared allocator currently declares its seventh argument as `struct37 *`.
This recovery includes the real SDK structure typedefs and uses an explicit
`(struct37 *)sizeof(payload)` cast to preserve that declaration and the retail
argument word 12. The test checks the declaration against the recovered helper
definition. Retail adds `0x28` to that word for the 52-byte allocation request.
The allocator's existing broad type contract remains a separate investigation.

## Payload representation and stack lifetime

The payload is a normal SDK32 structure: pointer at offset 0, identity at offset
4, five setting bytes at offsets 5..9, and two alignment bytes at offsets 10..11.
The frame is **72 bytes**, saved RA is at `SP+44`, and the complete payload starts
at `SP+60`. Retail leaves the final two bytes untouched and copies them too.
The source preserves this object representation rather than initializing them.

Guest tests compare the complete stack/RAM/register state, access trace and
fault context against retail, including poisoned padding, helper mutations of
the two padding bytes, incoming-home aliases and stack alignment phases. Native
tests check all 12 copied representation bytes without assuming a portable fixed
padding value. Guest aliases and emitted fault order do not establish portable
C overlap semantics or hardware behavior.

## Focused qualification

- **488 guest cases / 1,464 executions** compare original, direct C and padded
  code with the original 49-word allocator and 11-word `memcpy` connected. Every
  target word and 47 reachable allocator words execute. The allocator's flag-2
  path is unreachable from this routine's flags 0/1 and is not claimed covered.
- **74 access cuts**, including six delay-slot cuts, compare complete state and
  actual fault context across all three versions. Six independent function and
  callee rebases cross address boundaries with literal instruction equality.
- The sole aligned JAL is at ROM `0x11A108`, VA `0x150ECC58`; no aligned literal
  function pointers occur. The complete original 28-word wrapper `func_150ECC00`
  passes **32 cases** with its initialization call, all nine forwarded arguments,
  both allocation outcomes and the connected allocator/copy routines.
- Native SDK32 O0/O2/O3 each pass **262,144 cases** with trapping UBSan: all 65,536
  duration patterns, both allocation outcomes and identity mutation during
  allocation. Payload layout, all copied bytes and owner/output canaries pass.
- **13 effective controls** run through IDO/guest and native compilation: identity
  offset, first/fifth settings, default lifetime, sentinel, duration, allocation
  flag, callback kind, request byte, copy length/destination, allocation-failure
  handling and an incorrectly conditional copy. Compiler or interpreter failures
  do not count as successful controls. Signed-byte interpreter support has four
  explicit sign-extension checks.
- Both tools copies pass eight fresh canonical checks and shared checks. After
  production, two installed checks per copy run fresh; six semantic checks reuse
  their fresh receipts only under complete input/module/artifact fingerprints.

## Owner, image and progress

All **six owner neighbors** and constant pools remain identical. The actual
three-command generated-owner Make recipe reproduces the padded object.
Selected, owner and executed-command diagnostics are empty. The existing
duplicate `generated_12D630` Make warning remains in the dry-run plan.

The independent whole-image prediction equals the private first link and adopted
ELF: **174 changed bytes = 173 code bytes + 1 symbol-size byte**, metadata 0 and
exclusions 0. All **6,055 other bodies** and all **6,056 function addresses** remain
fixed. Protected Game data is exact across **189,088 bytes / 720 owners**. The C
inventory CSV, shared headers and the entire guard manifest remain unchanged.

Raw C SHA-256: `7f7d6b59ae81ed60418499c70bf4b7daa2a725d502ab59d6c9eac975f59f745f`.
Owner source SHA-256: `accc94e14e211a016d3792f8f00458906de4f0c6ea5647f5f6aaf2a473521c37`.
Padded owner SHA-256: `99835fb3241d40955f59ad65895552409791e5da916d875ecd99868647ee667b`.
Adopted ELF SHA-256: `5a93ed8ae4f16c38b38b2bb63601b70d2b311cb0e63b22a854e612bdd54d70f9`.

Fresh recount: **3,960 / 5,506 (71.92%)** total exact C and **3,287 / 4,833
(68.01%)** Game, zero drift. Init remains 492/492 and Debugger 181/181. The 75%
goal remains active: **170** more matches are needed for 4,130 / 5,506. Next private
screen: `func_15109ED4`. Root README changes only its two aggregate matching rows.

All 2,087 inherited mirror dirty paths and its HEAD are preserved, with three new
qualification files. Tools are committed before the consumer; nothing is pushed.
Graphify refreshes eleven changed sources/documents, retaining old nodes and valid
relationships and retiring the obsolete placeholder return-type edge. This is a
scoped AST refresh with historical communities; no full-corpus extraction, global
clustering, higher-parent execution or hardware acceptance is claimed.

Codex handled implementation, review and qualification. Routine direct matching
used zero Claude calls and no dependency or provider changes.
