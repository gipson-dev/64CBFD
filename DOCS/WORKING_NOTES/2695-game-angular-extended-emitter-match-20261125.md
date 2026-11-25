# Angular extended emitter match - 2026-11-25

`func_150B2EB4` replaces its zero-return placeholder with semantic C in
`conker/src/game/generated_DFBF0.c`. Its complete normalized 181-word body
and slot match retail, frame 192: VA150B2EB4..150B3188 / ROME0364..E0638.
**152 words with bindings emit directly; 29 checked rows normalize GPR
allocation cycles.** Raw C is not byte-exact. The relocations, private offsets,
floating-point operations, helper schedule and saved-register lifetime already
agree. No instruction insertion/omission or private stack map is used.

Actual production is **4,674 / 5,528 (84.55%)** total and **4,001 / 4,855
(82.41%)** Game, Init 492/492, Debugger 181/181, zero drift and 854 different.
**25 more verified matches are needed for 85%**. This function gains one match;
callers/helpers gain none. Conversion rows and denominators remain unchanged.

The routine uses the fifteen-word o32 registry interface. X/y/z are words
2/3/4; heading is word8, start word9, radius word10, extra word12, slot word14.
The first four incoming GPR homes are stored. Retail reads the full heading
before the first angle helper and reloads its byte after that call; coordinates
reload after the second angle helper. Start/radius/extra reload after the
first float RNG and slot after the fifth. Guest mutations exercise these
actual ABI reload points. This does not claim every generic callback typedef
is portable-compatible C.

The first lookups obtain heading cosine/sine from heading-64 and heading,
narrowed to u8. Speed is first float draw*31+18. Yaw is the signed16 result of
start+trunc(((60*headingSine)*radius)*extra)-64; pitch is the signed16 result
of trunc(48*headingCosine)-20. Four additional angle lookups obtain the two
cosine/sine pairs. Horizontal=speed*pitchSine, velocityX=horizontal*yawCosine,
velocityY=-speed*pitchCosine, velocityZ=horizontal*yawSine.

The real 124-byte descriptor contains flags0x9E8, zero rotation, unit scale,
the three coordinates and field04=D_8009FB8C. The next draws build field40/48
as draw*80-40, field44 is zero and duration is100. Field4C uses
draw*D_8009FB90+D_8009FB94. Field00 is one; field08 and field0C share
draw*72.5+D_8009FB98. Resource28, field6A2 and the explicit remaining control
fields precede `func_15132A4C(&descriptor,3,255,0,slot,0)`. The factory result
is ignored and the callback returns one. Four coefficient bits are
3E4CCCCD/BFE0418A/BF5645A2/41EE6667.

The initial semantic screen had the correct 181 words/frame192 and 41 word
differences. Restoring the real rotation/scale assignment order fixes eight
FP register-color differences. A real horizontal temporary alone grows the
frame to200 and was rejected. Reusing the overwritten, otherwise unused
signed16 index parameter for the two angles permits that real temporary
without extra frame space. All eight float locals participate in the actual
calculation. This recovers all private offsets and leaves 29 GPR operand
differences. The descriptor remains 124 bytes; no object is shrunk/enlarged,
no dummy/padding local is introduced, and the existing O2/g3 profile and
Makefile stay fixed. All five raw/padded neighbors and owner pools remain fixed.

The committed symbolic module extends the previously qualified scoped machine
with MFC1, trunc.w.s and the six-argument factory contract. It proves equal
ordered memory, FP-operation and call traces: **111 events /12 calls**, all
181 words reachable, saved registers/SP/RA and return one preserved. Four
address layouts include HI/LO carry and jump-region boundaries. Six supported
negative controls alter resource, slot home, flags, factory resource,
multiply operation or coefficient binding; every variant fails trace comparison.
The proof assumes valid disjoint stack/data regions and o32 helper contracts,
permits arbitrary provider results/public-memory epochs and factory writes to
the entire bounded descriptor. It is a scoped structural proof, not a general
SMT or all-machine-context claim.

Both full owner padders produce the same target and owner object. Raw
.rodata/.data remain absent; padded .rodata remains absent and .data empty.
Actual Make executes three commands. The independent reference splices only
the original target ASM into frozen old C and preserves following B3188.
Production equals the complete independent predicted ELF:
**615 changed bytes, zero exclusions**. All 189,088 protected
Game data bytes across720 owners, unrelated inputs, layout and conversion rows
are unchanged. Only the29 checked guard rows append to the frozen CSV.
The existing duplicate-recipe warnings for generated_12D630/F44D0/F5800 remain;
Makefile hash is unchanged. Broad unchanged neighbor suites are not repeated.

Guest checks pass **656 cases per each of four retail-equivalent
streams plus raw C**, all181 words and **304 access-fault quads**.
They cover all256 heading/slot bytes, signed start/angle boundaries, rounding
modes, fractional truncation, provider/global/home reload mutations and both
factory outcomes. Every seeded descriptor byte, including12 unspecified bytes,
agrees at each helper boundary. Eight cases separately model invalid guest
float-to-s32 conversions. These are excluded from native C; no hardware
execution of those modeled exceptional conversions is claimed. Fault-prefix
checks qualify emitted instruction order, not portable C exception semantics.

SDK32 O0/O2/O3 each pass **640 legal cases** with strict aliasing,
rounding controls and UBSan. Factory observes exactly112 initialized descriptor
bytes, excluding12 unspecified bytes. Earlier helpers have no descriptor pointer
and do not inspect private records. Dual32 digests compare ordered calls and
bounded public effects. All21 wrong-source controls compile and exit42 on
comparison. An initial horizontal control left a local unused and was rejected
by the compiler; it was corrected and rerun. No compile failure, signal or
sanitizer trap counts as an effective control.

The aligned pristine-ROM census finds no direct entry J/JAL and one pointer
at ROM22F4E4 / VA8008AA24, D_8008AA00[9]. All four complete original registry
parents pass384 cases per stream plus raw C, forwarding352 child calls per
stream. Eight return-zero controls stop a second child. Their visited counts
are95/96,113/130,112/120,128/138; two parents remain unmatched live. The larger
upstream effect wrappers are not claimed completely executed.

The original27-word angle helper executes all256 inputs and all27 words.
Its260-byte table and the16 coefficient bytes agree with pristine ROM and
frozen ELF. The original15-word factory wrapper matches live and executes
across16 cases, checking all seven forwarded backend arguments. The original
11-word memcpy also matches live and executes across16 cases, copying all124
seeded descriptor bytes. Backend1513264C remains unmatched and contracted:
full backend/allocator behavior is not qualified here, and helper credit is zero.

Boundary checks reject58 guarded corruptions, expose304 unguarded changes,
pin20 bindings and verify full/scoped guard equality. Twenty GNU links and
40 guest rebase runs include raw and normalized/original bodies. Both padders
reject the oversized probe. Shared `make tools-check` passes.

| Qualification | Elapsed | Coverage |
| --- | ---: | --- |
| preinstall-primary | 122.3s | 5 fresh / 0 reused |
| preinstall-sibling | 120.106s | 5 fresh / 0 reused |
| installed-primary | 116.533s | 5 fresh / 0 reused |
| installed-sibling | 124.35s | 5 fresh / 0 reused |

The second tools overlay is fingerprinted; the separately dirty sibling is
preserved. Tooling commits before consumer. Claude calls for this routine: zero.
One detailed note and five concise indexes carry this narrative; root README
receives aggregate status rows and its verification date as needed.

Baseline consumer: `a2acf3d801b67c8324792f755010f0f4a49a284c`.
Tools commit: `cb0a3cb742fadf63515f8f0f858840905ce6fedf`.
ELF SHA256: `5c4e806a2c35262911459422b2aae372fa86f49f33d1bec2c56dc07b41cf7cd4`.
Padded owner SHA256: `36409dd32a2c2d6d0253bc7675a349feeee7236a0268402acaaa9ecc2be97664`.
Freeze: 3673 inputs / 2278 copies.
Receipts: `conker/build/game-angular-extended-150b2eb4-private`.

Graphify was queried before the screen. Native update and scoped AST refresh
retain old IDs and qualification metadata after actual hook producers terminate.
Staging and low-memory atomic publication run separately. Completed independent
C16C0 artifacts were NTFS-compressed with every SHA retained; baselines, shared
hardlinks and active files were excluded, and nothing was deleted.
No full-corpus extraction, host/Release action, push or gameplay acceptance
is claimed. Next inspect B3188, the remaining unmatched nonnull callback in
this table. C9BDC and the matrix candidate stay private/uncredited.
The85% goal remains active.
