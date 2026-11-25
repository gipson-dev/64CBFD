# Random pitch radial color emission byte match - 2026-11-24

`func_150B2570` replaces its zero-return placeholder with semantic C in
`conker/src/game/generated_DF930.c`. The complete 115-word body is byte-exact
after 32 expected-word guards normalize a closed private stack map. Its frame
already matches at 120 bytes; 83 words emit directly. The retail slot has 116
words / 464 bytes, including one unchanged owner padding NOP. Body VA
150B2570..150B273C / ROM DFA20..DFBEC is 460 bytes; slot end is VA150B2740 /
ROMDFBF0. No instruction insertion, omission, profile or Makefile change,
replacement body, dummy local, enlarged descriptor or added padding is used.

Actual production is **4,671 / 5,528 (84.50%)** total, Game **3,998 / 4,855
(82.35%)**, Init **492 / 492**, Debugger **181 / 181**, zero drift and 857 different.
**28 more matches are required for 85%**. Only this function gains one match.

The callback carries 15 o32 words and returns one. Coordinates, heading word
eight and the final slot byte are active; the start word and other parameters
remain unused. The two initial angle lookups use heading-minus-64 / heading.
The first direct integer RNG draw chooses signed halfword pitch
`(u32)draw % 21U - 30`, ranging from -30 to -10; two further angle lookups use
pitch-minus-64 / pitch. Unsigned subtraction before narrowing to u8 preserves
wrap at word boundaries. Speed is ten times the fourth lookup. Coordinates
reload after the angle calls and pitch draw, and the slot reloads immediately
before submission. All register homes agree. Original callers supply byte-range
headings. This qualifies the actual o32 interface, without claiming portable C
compatibility of every generic callback typedef. The negative-pitch comment
does not infer a physical direction from the angle convention.

The 60-byte descriptor receives position and velocity, three float RNG based
fields using D_8009F900..D_8009F914, two command-eight RGB colors, both alpha
bytes255, kind9, lifetime `(u32)draw % 7U + 18`, flags0x1601, alpha255 and final
halfwords8/31. Coefficient bits in address order are 3F5BE76D/4066E97A/3E9E3540/4017BE77/3FB1EB85/404D70A4. There are four
angle lookups, two direct integer RNG calls, three float RNG calls, two RGB
providers and **one** `func_15156190(packet,1,0,slot,1)` submission. No second
factory wrapper is called. Its result is ignored; return one keeps the parent
iteration alive. Provider effects test global load timing, late slot reload,
caller-saved clobbers, packet mutation and public-memory effects.

All guards preserve the instruction upper16 bits, SP base, operation, register,
width and relocation bindings, changing only a displacement by minus four:

| Private object | Raw SP range | Retail SP range |
| --- | --- | --- |
| Three float intermediates | 2C..38 | 28..34 |
| Pitch halfword | 3A..3C | 36..38 |
| Descriptor60 | 3C..78 | 38..74 |

Ranges are half-open and disjoint in each layout, fit the unchanged 0x78 frame,
and exclude RA at1C plus incoming/outgoing homes. All 32 accesses and derived
pointers are enumerated, including the pitch LBU. Raw fixtures copy from one
immutable initial snapshot so overlapping physical source/destination ranges do
not cascade. Canonical comparison maps the three RGB pointer arguments and
factory packet pointer, the complete packet, float group and pitch; it preserves
fixed frame prefix, incoming homes, public memory, call observations, FCSR,
return, SP and saved registers. Original normalized streams compare full state.

Both complete owner padders agree. Neighbors `func_150B2480` and `func_150B2494`
retain raw/padded instructions and bindings; raw .rodata/.data remain absent,
padded .rodata absent and .data empty. The actual Make route has three commands.
The independent image reference uses frozen old C plus original target ASM,
without the recovered C or guards. Production equals its full predicted ELF:
**423 changed bytes, zero exclusions**. Padding, all 189,088 protected Game
data bytes / 720 owners, conversion rows and other inputs stay fixed. Make emits
the existing duplicate-recipe warnings for generated_12D630, generated_F44D0 and
generated_F5800; the Makefile hash is unchanged. Broad unchanged suites are not
repeated or claimed fresh.

Four retail-equivalent guest streams each pass 445 cases, plus raw C
under the complete stack map. All115 words execute; 176 access-fault quads
agree. Cases cover all256 heading and unused-start low bytes, every pitch draw,
both unsigned modulo boundaries, signed-word boundaries, all four rounding
modes, both factory outcomes and provider effects. All60 guest packet bytes,
including unspecified holes, agree at call boundaries. Incoming-home mutations
qualify emitted ABI behavior and are excluded from portable native cases.

SDK32 O0/O2/O3 each pass 437 legal bounded cases with strict aliasing,
controlled rounding and UBSan. Canonical dual32 digests compare ordered calls,
globals and canaries. Native observation includes only32 initialized packet
bytes before the first RGB call,35 before the second,54 at the factory; six
unspecified bytes are excluded. All17 source controls compile and fail
comparison with exit42. No compile failure, signal or UBSan trap counts as a
successful control.

The aligned pristine-ROM census finds zero direct J/JAL entries and one pointer
at ROM22F4DC / VA8008AA1C, D_8008AA00[7]. All four complete original registry
parents run 384 cases per stream plus raw-C cases, forwarding all15 words
and 352 child calls per stream. Eight return-zero controls stop the second
child. Parent coverage remains95/96,113/130,112/120,128/138; two parents remain
unmatched live. Parent lookup interception applies only outside the child body
because parent and child share the angle helper. Finite original executions
grant no parent credit or all-path claim.

Original factory126/wrapper12/angle27/color31 words are independently assembled
and bound against pristine ROM. The constructor remains unmatched live; the
other three match the frozen ELF. The wrapper binding is historical evidence
only and is not called by this target. Constructor descriptor reads cover
exactly54 initialized bytes and exclude all six holes; constructor internals
are contracted. Original helper executions cover all27 angle words across256
inputs and all31 color words across six draws, including the color helper's
internal RNG. The target's two direct integer draws are separate from these
RGB-provider draws. All24 coefficient bytes,260 angle-table bytes and12 palette
bytes agree with frozen ELF and pristine ROM. Helper credit is zero.

Boundary controls reject 64 guarded corruptions, expose
166 unguarded corruptions and pin all24 bindings. Sixteen GNU links /
32 guest rebases cover HI/LO carries and sign/address regions. Both padders
reject the oversized standalone body. Shared `make tools-check` passes.

| Qualification | Elapsed | Coverage |
| --- | ---: | --- |
| preinstall-primary | 122.344s | 5 fresh / 0 reused |
| preinstall-sibling | 124.473s | 5 fresh / 0 reused |
| installed-primary | 96.135s | 5 fresh / 0 reused |
| installed-sibling | 109.649s | 5 fresh / 0 reused |

The isolated second tools overlay verifies code/data dependencies and leaves
the separately dirty sibling unchanged. Tools commit before consumer. Claude
calls: zero; local evidence settles this routine. Root README changes only two
aggregate rows; this note and five concise indexes carry the detailed update.

Consumer baseline: `acae77f51922c844713eda1c2475e6fa6e339495`.
Tools commit: `75bea44f375f210fcaa680ee50ee95c19838b84b`.
ELF SHA256: `5c6601c3707236ce75a40873a3902a69683e7611dca129e832bc8428bb414254`.
Padded owner SHA256: `9251d95e292b7fa849b5d8a504856f0ce361fb2620f4dbefb96dd8049f503b95`.
Freeze: 3639 inputs / 2239 copies. Receipts:
`conker/build/game-radial-color-150b2570-private`.

Graphify query preceded work. Native update and scoped AST merge retain old IDs
and proof metadata after the actual hook producers terminate. No full-corpus
extraction, host build/launch, Release change, push, gameplay acceptance or
all-input equivalence is claimed. The host sibling currently has only .codex
and recomp_scene, with no source checkout to receive this change. Next inspect
`func_150BD954` against its current retail window. The 85% goal remains active.
