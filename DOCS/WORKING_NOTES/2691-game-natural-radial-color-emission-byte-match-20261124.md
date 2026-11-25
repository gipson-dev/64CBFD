# Natural radial color emission byte match - 2026-11-24

`func_150B3C0C` replaces its zero-return placeholder with semantic C in
`conker/src/game/generated_E0F60.c`. All **112 instruction words emit directly
from C, with zero guards**. The retail slot is 113 words / 452 bytes: its last
word is unchanged owner padding. VA 150B3C0C..150B3DCC / ROM E10BC..E127C is
the 448-byte body; slot end is VA 150B3DD0 / ROM E1280. Frame 112, every register,
binding, operation and call order match naturally. No instruction insertion,
omission, profile/Makefile change, private stack map, dummy local or enlarged
descriptor is used. Existing guard CSV bytes remain completely unchanged.

Actual production is **4,670 / 5,528 (84.48%)** total, Game **3,997 / 4,855
(82.33%)**, Init **492 / 492**, Debugger **181 / 181**, zero drift and 858 different.
**29 more matches are required for 85%**. Only this function gains one match.

The real declaration order is four float intermediates followed by a 60-byte
descriptor. Capture the fourth angle result into `speed`, then separately use
`speed = 10.0f * speed;`. This recovers retail's multiply operand order without
a guard. Combining the call and multiply produces one operand-order difference;
an extra angle temporary enlarges the frame. Quarter-angle subtraction casts
to u32 before narrowing to u8, preserving wrap without signed overflow.

The interface carries 15 o32 words. Coordinates, both angle words and the final
slot byte are active; the other parameters remain unused. Subtraction paths use
LW and direct lookup paths use LBU, so angle/start are s32 parameters whose low
bytes select the lookup. All four register homes match; coordinate homes reload
after four lookups and the slot byte reloads before the first factory. Original
registry callers supply byte-range headings. This qualifies the actual o32 ABI,
without claiming all generic C callback pointer types are portable-compatible.

The routine performs four angle lookups, three float RNG calls, two RGB-provider
calls, one direct integer RNG call and two factory submissions. Its velocity is
derived from the two angular inputs and scale ten. Six coefficient globals
D_8009FBCC..D_8009FBE0 produce the two velocity scales and the final float field;
their bits are pinned in address order as 3FF9FBE8/406F1AA0/3F70A3D8/400E45A2/402A3D70/3FECCCCC. RGB command eight is used
twice, both alpha bytes become 255, kind is nine, lifetime is `(draw&15)+15`,
flags are 0x1601, alpha is 255 and the last halfwords are ten and twenty-five.
The shared descriptor is submitted to `func_15156190(packet,1,0,slot,1)`, then
`func_15156388(packet,1,0)`. The second wrapper selects slot 255 / owner zero.
Both results are ignored and the emitter returns one. Provider mutations test
global load timing, late slot reload and reuse of the first factory's packet
changes by the second submission.

Both complete owner padders agree. The single neighbor `func_150B3AB0` retains
its raw/padded instructions and bindings; raw .rodata/.data remain absent,
padded .rodata absent and .data empty. The actual Make route has three commands.
The independent reference uses frozen old C plus original target ASM, without
the recovered C or guards. Production equals its full predicted ELF:
**507 changed bytes, zero exclusions**. The one padding word, all 189,088
protected Game data bytes / 720 owners, conversion rows and other inputs stay
fixed. No broad unchanged neighbor suites are repeated or called fresh.

Four retail-equivalent guest streams each pass 592 cases, plus an identical
raw-C stream without canonical stack adjustment. All 112 words execute;
176 complete access-fault quads agree. Tests cover every angle/start byte,
signed word boundaries, four rounding modes, RNG-mask boundaries, both factory
outcomes and provider effects. All 60 packet bytes, including unspecified holes,
agree at call boundaries. Guest incoming-home mutations qualify emitted ABI
behavior rather than portable C fault semantics.

SDK32 O0/O2/O3 each pass 576 legal bounded cases with strict aliasing,
controlled rounding and UBSan. Canonical dual32 digests compare ordered calls,
globals and canaries. Only 32 initialized packet bytes are observed before the
first RGB call, 35 before the second and 54 at each factory; six unspecified
bytes are excluded. All 17 source controls compile and fail comparison with
exit 42. No compile failure, signal or UBSan trap counts as a successful control.

The aligned pristine-ROM census finds zero direct J/JAL entries and one pointer
at ROM 22F4E0 / VA 8008AA20, D_8008AA00[8]. All four complete original registry
parents run 384 cases per stream plus raw-C cases, forwarding all 15 words
and 352 child calls per stream. Eight return-zero controls stop a second
child. Coverage remains 95/96,113/130,112/120,128/138; two parents remain unmatched
live. Parent lookup interception is restricted outside the child body because
parent and child share the same angle helper. Finite original executions grant
no parent matching credit or all-path claim.

Original factory126/wrapper12/angle27/color31 words are independently assembled
and bound against pristine ROM. The constructor remains unmatched live; the
other three match the frozen ELF. Its descriptor reads cover precisely the 54
initialized bytes and exclude all six holes. Constructor/wrapper internals are
contracted, not freshly executed here. Dedicated original-helper executions
cover all 27 angle words across 256 inputs and all 31 color words across six
draws, including the color helper's internal RNG call. The target itself calls
integer RNG once; the two RGB providers each have their own internal draw.
All 24 coefficient bytes, 260 angle-table bytes and 12 palette bytes agree with
the frozen ELF and pristine ROM. Helper matching credit is zero.

Boundary controls expose 224 unguarded corruptions and pin all
24 bindings. Sixteen GNU links / 32 guest rebases cover HI/LO carries and
sign/address regions. Oversized generic output is explicitly labeled overflow;
the generated padder rejects it. Neither silently accepts a fitted slot.
Shared `make tools-check` passes.

| Qualification | Elapsed | Coverage |
| --- | ---: | --- |
| preinstall-primary | 263.51s | 5 fresh / 0 reused |
| preinstall-sibling | 191.888s | 5 fresh / 0 reused |
| installed-primary | 185.776s | 5 fresh / 0 reused |
| installed-sibling | 146.748s | 5 fresh / 0 reused |

The isolated second tools overlay verifies all code/data dependencies and leaves
the separately dirty sibling unchanged. Tools commit before consumer. Claude
calls: zero; this routine is settled by local evidence. Root README changes
only its two aggregate rows; this note and five concise indexes hold detail.

Consumer baseline: `7b17666b49ed2d359afc1677e0f05f67e8bde261`.
Tools commit: `3d23c69bf2816113a754640a21496c26299bed76`.
ELF SHA256: `4aa2c55750588caa9e6726c273886ccc3a69de89303133d675aaad9e1127bd9e`.
Padded owner SHA256: `d92bddccba49f76a6e23324a5d365f46458961fdaf53c19622ef07a555fa7828`.
Freeze: 3628 inputs / 2226 copies. Receipts:
`conker/build/game-radial-effect-150b3c0c-private`.

Graphify query preceded work; native update and scoped AST merge retain old IDs
and proof metadata after the actual hook producers terminate. No full-corpus
extraction, host build/launch, Release change, push, gameplay acceptance or
all-input equivalence is claimed. Next: inspect the remaining radial registry
callbacks, starting with `func_150B2570`. The 85% goal remains active.

The production Make log retains existing duplicate-recipe warnings for
`generated_12D630`, `generated_F44D0` and `generated_F5800`. The Makefile is
byte-identical to the frozen baseline; this is a successful build with those
pre-existing warnings, not a warning-free full build.
