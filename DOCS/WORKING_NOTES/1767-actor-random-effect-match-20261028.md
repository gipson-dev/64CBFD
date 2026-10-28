# 1767 - Actor random effect direct C match

Verified: 2026-10-28. Target func_1506FD30, owner game_981E0.
VA0x1506FD30..0x1506FDF0 /ROM0x9D1E0..0x9D2A0: 48 words /192 bytes,
frame80, six external bindings and zero guards. Normal O2/g3 profile.

## Recovered source and callback ABI

Replace the zero-return body and its local placeholder declaration with
void func_1506FD30(s32 arg0). The canonical D_80086150 callback declaration
already uses void (*)(s32), and its existing dispatcher passes the selector.
The argument is unused by the recovered behavior; retain its original incoming
home store at entrySP+0. The function's own frame is80 bytes and saves RA at+76.
No shared header or helper declaration changes are required.

Keep canonical struct127 *D_800D154C and its unsigned unique_id byte at+0x3B.
Add only the private extern f32 D_80099EA0 near the recovered definition,
replacing its obsolete placeholder comment. Keep the address-based symbol;
the short source comment identifies the actor effect and randomized scalar.

Call the retained float provider func_150ADA68 first. Then read the live global
parameter, current actor pointer and unsigned unique ID. The provider may change
any of them. Submit seventeen arguments to func_150E2EA4:

| Positions | Values |
| --- | --- |
| 0..3 | actor, unique_id,1,-1 |
| 4..9 | 0.0f,zero,D_80099EA0,0.0f,zero,414.0f |
| 10..16 | 3,3,5,20.0f,random*10.0f+40.0f,1,50.0f |

Use a normal f32 zero local for the two indicated positions. This preserves the
original separate F12 zero constant lifetime. The literal-zero/all-zero-local
forms emit47 words; the selected form and an equivalent early-initialized local
emit all48 original words directly. Eleven source forms are retained privately.
No volatile qualifier, register binding, synthetic effect or binary patch is used.

The multiply and add round separately to float32. At PRNG low-halfword822,
random bits0x3C4D80CE produce a one-ULP difference between the original expression
and (random+4.0f)*10.0f. The actual compiled negative and native controls reject
the reassociation. Keep unsigned ID promotion, the signed-1 sentinel, all fixed
arguments and both late global reads. Do not cache actor, ID or parameter before
the provider, add a null check, skip the provider or invent a returned value.

## Original registry, dispatcher and helper boundaries

The aligned ROM census finds no direct JAL/tailJ and one target pointer at
ROM0x22AC90 /VA0x800861D0, slot32 of D_80086150. The frozen table contains111
entries. Preserve its complete assembly/data object. func_15071D38 is already
C and byte-exact: its original16 words/frame24 load the selector from
D_800D1580, load the callback, skip a null slot, pass selector32 and ignore the
callback result. This bank preserves that existing dispatcher among327 neighbors.

The actual func_150E2EA4 wrapper is59 words /236 bytes with frame120. Its retained
source is translation_units/10EF60_wrappers.c. It forwards the seventeen inputs
to the28-argument func_150E1AB0 factory with kind0x27 and fixed defaults.
The wrapper's u8/s16/u16 parameters agree with the caller's promoted32-bit views
for the recovered constants and unsigned ID range. Do not change the shared
header to resolve an unrelated prototype style. Connect the original dispatcher,
target and complete wrapper; the deepest combined frame is224 bytes. The final
factory remains a bounded opaque provider in these tests.

The retained handwritten func_150ADA68 is25 words /100 bytes, unchanged in the
current ELF and still GLOBAL_ASM. Its return uses a masked low16-bit value times
D_8009F740, whose retail bits are0x37800080. All65,536 output encodings at that
retail scale are covered natively. The target tests model the float return and
permitted provider mutations; they do not recover its64-bit PRNG implementation
or prove hardware FCSR behavior. D_80099EA0's retail bits are0x43AC8000.

Raw original/selected target SHA256:
~~~text
3ebf61c79d401f6769991bb63497cc2dbff682b24f177e01afa12c61ac99f594
~~~
Original linked192-byte slot SHA256:
~~~text
83493fca2ce6d26cf36f2e09ab8055481d93fc98457dbf8f91773802e749d501
~~~

## Focused qualification

Both canonical tools copies pass eight fresh methods plus their project-tool
checks. Each installed copy then passes two fresh owner/image methods and reuses
six semantic methods only under exact module, frozen snapshot, sealed-input and
qualified-artifact identity. Routine Claude calls:0.

- 3,200 guest cases compare literal retail and direct C private state/access
  traces, plus an independent public-memory/call reference. Reach all48 words.
  Cover all unsigned-ID boundaries, provider redirects and ID/parameter changes,
  post-emitter mutations, signed zero and selected float encodings. Six valid
  mapped layouts include ID aliases with the incoming home, provider outgoing
  home, parameter/global-pointer bytes and an initially null actor redirected
  before its first dereference. Unmapped combinations are not native-C claims.
- 760 fired access-prefix pairs compare complete private/public memory,
  registers, PC, delay ownership and trace. Preserve the initial argument-home
  store, provider-before-actor order and all outgoing argument stores. Opaque
  provider hooks clobber caller-saved GPRs/FPRs, HI/LO and their argument homes.
- 128 connected cases execute all16 original dispatcher words, the target and
  all59 wrapper words. Verify selector32, seventeen outer and28 inner arguments,
  every fixed/default value, stack restoration and ignored return. A separate
  actual null registration skips the callback. Original binary windows are
  checked against both frozen retail and the predecessor ELF before execution.
- Native32 O0/O2/O3 with trapping UBSan each pass270,336 positive cases. Cover
  all65,536 scaled random values over four provider modes and all256 IDs over
  eight float samples/four modes. Use canonical typed actor storage, provider
  mutations, whole-world fences and exact forwarded float bits. Fourteen wrong
  scale, bias, double/reassociated rounding, ID sign, cached actor/ID/parameter,
  missing provider, flag, sentinel, limit, zero and parameter variants fail by
  values or call sequence. Guest pointer/home aliases remain separate.
- Three independent GNU layouts pass108 cases, including signed low-half
  relocation carries and relocated calls. The real regular-object padder is
  byte-identical; three raw/binding corruptions are rejected.
- Three actually IDO-compiled controls cache the actor, cache the parameter or
  reassociate the scalar. All fail by call arguments in mapped memory. Six
  complete-image corruptions, including protected data and metadata records,
  are rejected without section exclusions.

The first native harness lacked the project's freestanding startup routine.
Preserve canonical-attempt1 and its failed result; adding the normal startup
allowed the complete fresh eight-method rerun in both copies to pass. No source
semantics, flags or gates were weakened.

## Actual Make and exact whole-image prediction

Preserve all327 other compact and padded functions, their relative relocations,
constant pools and14 GLOBAL_ASM routines. The actual regular-owner Make path is
five commands: asm preprocessing, IDO, ASM postprocessing, pad_c_object.py and
GNU assembly. It and production reproduce the qualified padded object.
Selected diagnostics are empty. Existing owner pointer/prototype warnings remain
identical after normalizing only diagnostic source filenames/line numbers;
production also retains the existing duplicate generated_12D630 Make warning.
This is not a warning-free full-owner build.

The complete adopted ELF equals a199-byte prediction, with no exclusions:
152 target instruction bytes, one target-size byte12->192,20 symbol-record bytes
and26 string bytes. All named values/types/sizes/sections are unchanged except
the target extent. The metadata recipe rotates only three consecutive records
and their36-byte string window:

~~~text
D_80099EA0,func_150D0E90,D_800AB1B4
 -> func_150D0E90,D_800AB1B4,D_80099EA0
~~~

Derive each record and its new name offset from the frozen predecessor. Require
identical section geometry, exact original names/positions and complete named-
definition equality. The first temporary input basename changed an STT_FILE name;
using link-object/game_981E0.c.o restores the production basename before this
proof. Failed temporary-name artifacts remain archived. A reporting-variable
collision was corrected before evidence fingerprints were sealed; independent
native parsing confirms152 code and47 total size/serialization bytes.

All6,056 function addresses,6,055 other bodies,720 protected Game-data owners
and189,088 protected bytes remain fixed. Shared headers, helper sources/objects,
registry, map, inventory CSV and the entire inherited guard manifest are unchanged.
Seal16,262 files and264 focused inputs. No new guard rows are added.

ELF SHA256:
~~~text
5ccc025d4407926820062c60ccf343e007f84751e22fddfe7a1d2088afdc52e9
~~~

## Measured progress and bank

Recount the actual captured native ELF; preserve the existing C inventory.
Only func_1506FD30 becomes exact:

| Section | Exact C functions | Different | Drift |
| --- | ---: | ---: | ---: |
| Total | 3,845 /5,506 (69.83%) | 1,661 | 0 |
| Init | 492 /492 (100.00%) | 0 | 0 |
| Game | 3,172 /4,833 (65.63%) | 1,661 | 0 |
| Debugger | 181 /181 (100.00%) | 0 | 0 |

The4,130 threshold leaves285 more to75%. Remaining source screens:1,532
placeholders,120 semantic/other and9 unlocated. These screens do not qualify
any other body, the pending NULL factory, the PRNG or complete gameplay.

Predecessor consumerd65ca83de19742c81b6d19760d0687b2878083eb and tools
59b50f29a362d76d1fe606634d8747d42fd487f7. Bank tools first at
15b79b7e00bcf377d80fe8c1c983444619bba255, then source, tools pin and seven
measured documents. Preserve1,744 inherited dirty mirror paths plus only two
new target modules. No push. Root README changes only two aggregate rows.

Refresh ten structural C/Markdown/tools files. Retain old nodes or unique
relocations and all valid confidence/context keys; retire only this target's
false s32 return relation after checking the committed void(s32) signature.
Validate its s32 parameter and both helper-call relationships against actual
source declarations and the J26 bindings. Record the RNG's retained ASM
implementation and the wrapper's real source; add no speculative registry
caller or full-factory edge. Outside freshness, communities/global analytics
remain historical. This is not a full-corpus extraction. Receipts and the
independent audit live under conker/build/game-actor-random-effect-match/.

Next inspect func_150979CC from a fresh predecessor. func_1514E920 remains
parked and uncredited. The75% goal remains active.
