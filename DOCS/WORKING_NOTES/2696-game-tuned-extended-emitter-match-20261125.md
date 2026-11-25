# Tuned extended emitter match - 2026-11-25

`func_150B3188` replaces its zero-return placeholder with semantic C in
`conker/src/game/generated_DFBF0.c`. VA150B3188..150B36AC / ROME0638..E0B5C:
329 words, 1,316 bytes, frame248. The complete normalized body and slot match
retail. **297 word values and bindings emit directly; 32 expected-word guards
normalize proved GPR allocation cycles. Raw C is not byte-exact.** All FP
operands, private offsets, relocation positions and bindings already agree.
The real descriptor is124 bytes and a separate four-byte float payload is passed
only on successful allocation. No private stack map, inserted/omitted instruction,
dummy local, record-size change, compiler profile or Makefile change is used.

Actual production: **4,675 / 5,528 (84.57%)** total and **4,002 / 4,855
(82.43%)** Game. Init492/492 and Debugger181/181, zero address drift,
853different. **24 more verified matches to85%**. This target gains one match,
helpers and callers gain none. The conversion rows and denominators stay fixed.

The fifteen-word o32 interface uses x/y/z at2/3/4, heading8, start9, radius10,
extra12, slot14. First-four GPR homes are stored. The second heading lookup
reloads the low byte after the first helper. Coordinates reload after the ninth
tweak call. Start/radius/extra reload after the first float RNG; slot reloads
after the fifth. Guest mutation cases cover these actual ABI reads; no claim
is made that every generic callback typedef is portable-compatible C.

The first two angle calls capture heading cosine/sine. Nine seven-argument
`func_151422DC` calls, IDs6..14, retain their two debug-label pointers,
minimum/maximum/default and line values. Their results form signed16 duration,
fieldBias/Range, speedBase/Range, sizeBase/Range, yawScale and pitchScale.
Signed32-to-single conversions and coefficient load/multiply order follow retail.
The six coefficient words at D_8009FB9C..D_8009FBB0 are
3A83126F/3A83126F/3DCCCCCD/3DCCCCCD/3E4CCCCD/3DCCCCCD.
The original seven-word getter is byte-exact and returns its fifth argument;
its real body is separately executed rather than inferred from its name.

Speed=draw*speedRange+speedBase. Yaw is signed16(start+
trunc(((yawScale*headingSine)*radius)*extra)-64); pitch is signed16(
trunc(pitchScale*headingCosine)-20). Four more angle lookups derive velocity:
horizontal=speed*pitchSine, vx=horizontal*yawCosine,
vy=-speed*pitchCosine, vz=horizontal*yawSine. The descriptor has flags29E9,
unit scale, zero rotation, captured coordinates, field04=D_8009FBAC,
field40/48=draw*4-2, field44=0, duration+32,
field4C=draw*fieldRange+fieldBias, shared field08/0C=draw*sizeRange+sizeBase,
field00=sharedSize*D_8009FBB0, resource28, field63=5, field6A=2,
field72=32, field74=7 and the explicit remaining control bytes.

`func_15132A4C(&descriptor,3,255,4,slot,0)` runs once. Only a nonnull
result causes `memcpy(created+0x170,&payload,4)`, where payload is -18.0f.
The callback returns one in either allocation outcome. The original factory
wrapper forwards backend arguments (descriptor,3,255,0,4,slot,0).
Backend1513264C remains unmatched and contracted; no full allocator/backend
or gameplay qualification is claimed.

The initial329-word/frame248 body had34 differences. Moving the real payload
declaration after the used created pointer recovers retail SP+30 instead of34
and leaves32 GPR-only differences. Both void*/u8*created probes emit the same
bytes. The installed body uses u8*created and the existing actual124-byte
descriptor type. All five raw/padded neighbors and owner pools stay fixed.

The scoped structural proof compares ordered memory, FP-operation and call
events under arbitrary provider results and public-memory epochs. Failure:
208events/21calls/326visited words; success:209events/22calls/all329words.
Four rebase layouts times both outcomes give8 proofs, including jump-region
and HI/LO carry cases. Six supported execution controls alter duration default,
resource, slot home, multiply operation, copy count or coefficient binding;
every variant fails comparison. Saved registers/SP/RA and return one agree.
A nonnull factory pointer is symbolic and constrained valid/disjoint. The
factory may overwrite the bounded124-byte descriptor, preserving the unpassed
four-byte payload. This is scoped structural evidence, not general SMT or a
claim about all machine contexts. The first missing LH interpreter operation
was implemented accurately; an interpreter failure is not a negative control.

Both complete owner padders agree. The three-command actual Make route and
independent reference link use frozen old C with only original target ASM
spliced in, preserving following B36AC. Complete production equals the predicted
ELF: **1557 changed bytes, zero exclusions**.
All189,088 protected Game data bytes/720 owners, layout, conversion rows and
unrelated frozen inputs remain fixed. Only32 checked guard rows append.

Guest tests pass **914cases per four retail-equivalent
streams plus raw**, all329 words and **496fault quads**.
They cover all256 heading/slot bytes, both factory paths, four rounding modes,
signed start/angle and CVT boundaries, public/global and actual home reloads.
Eight modeled invalid-trunc cases remain guest-only.
Native SDK32 tests pass **898legal cases at O0/O2/O3**,
strict aliasing, explicit rounding and UBSan. They inspect112 initialized
descriptor bytes at the factory, exclude12 unspecified bytes, and check the
four-byte success payload through its real passed pointer. Earlier providers
have no descriptor/payload pointer and do not inspect private records.
All27 source controls compile and exit42 by comparison, including signed
tweak metadata, payload, copy count and omission. The size control preserves
all initialized fields. No compile error, signal or sanitizer trap counts.
Fixture corrections recovered the actual factory argument order and exact
memcpy contract (the copy has no artificial public marker effect).

The pristine aligned-ROM census finds no direct entry J/JAL and one pointer
atROM22F4E8 / VA8008AA28, D_8008AA00[10]. Four complete original registry
parents pass384cases/352child calls per stream plus raw. All15 callback words
are observed; eight return-zero controls stop a second child. Parent visited
counts95/96,113/130,112/120,128/138; two remain unmatched live. Larger upstream
effect wrappers are not claimed completely executed. The original angle
helper executes256inputs/all27words with its260-byte table pinned.
The original getter executes108cases/all7words including signed32 boundaries.
The original15-word factory wrapper executes16cases, all seven backend
arguments checked. The original11-word memcpy is connected for the real
four-byte success payload and separately copies124seeded descriptor bytes,
including12 guest-unspecified bytes. Helper credit stays zero.

Boundary tests reject64guarded corruptions, expose594unguarded changes and
pin70bindings. Twenty GNU links/40guest rebase runs include raw and normalized
bodies. Both padders reject oversize. Shared `make tools-check` passes.

| Qualification | Elapsed | Coverage |
| --- | ---: | --- |
| preinstall-primary | 179.012s | 5 fresh / 0 reused |
| preinstall-sibling | 182.1s | 5 fresh / 0 reused |
| installed-primary | 174.356s | 5 fresh / 0 reused |
| installed-sibling | 249.247s | 5 fresh / 0 reused |

The second tools overlay is fingerprinted; the separately dirty sibling is
preserved. Tools commit before consumer. Claude calls for this routine: zero.
Baseline consumer `f2be019f68eec3827a6ff2e632a0474b0a7f0cbc`.
Tools commit `b1486a01a0cc85ec88138e70c593170dee30ddf6`.
ELF SHA256 `5d66156c9fb3e971d91e095827ac6799e51e7382d57252d263721a8c639bf075`.
Padded owner SHA256 `1df7a41364ebdc6c5eb181e11a6b30040b0a2d7d58bd9f2a6c2513be0e392a50`.
Freeze 3684inputs/2289copies.
Private receipts `conker/build/game-tuned-extended-150b3188-private`.

Graphify was queried first; native update is followed by a scoped AST refresh
that retains old IDs and proof metadata after actual hook producers terminate.
Staging and low-memory atomic publication run separately. Banking retains
byte hashes and uses compressed graph appends with verified-prefix recovery.
The root README receives aggregate rows/date only. No host/Release build,
push or gameplay acceptance is claimed. C9BDC and matrix candidates remain
private/uncredited. The85% goal stays active; next screen another unmatched
callback/helper after the complete checkpoint is banked.
