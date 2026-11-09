# Camera Transition Dispatch Direct Match - 2026-11-09

`func_15128540` replaces its false zero-return placeholder with the original
camera transition dispatcher. All **80 words /320 bytes** emit directly from
C under existing **O2/g3**, retaining the **0x20 frame**, S0+0x18 and RA+0x1C.
There are **no guards, padding words, profile changes or shared header changes**.

Production: Total **4,286 /5,513 (77.74%)**, Game **3,613 /4,840 (74.65%)**,
Init **492/492**, Debugger **181/181**, zero drift; **1,227** still different.
**125** more exact functions reach4,411/5,513 and80%. Conversion rows stay fixed.

## Recovered body and interface

Owner conker/src/game_14FF90.c; original
conker/asm/nonmatchings/game_14FF90/func_15128540.s.
VA15128540..15128680 /ROM1559F0..155B30. Existing s32(s32 address)
interface stays intact: the entire camera address survives in S0 and the
function returns exactly0 or1. The supplied address is not range-checked.

- Predicate151253CC nonzero returns1 immediately; otherwise predicate15128030
  nonzero returns0. Both tests accept any nonzero signed32-bit result.
- Read live flags+0x2C only after those calls. Bits19,20,21,22, in that priority,
  select1512A360,1512E4B0,151219D0,1512D380. Multiple bits select the first.
- The first branch calls1512A360, copies the three raw words at+0x2A4/+0x2A8/
  +0x2AC to+0x2BC/+0x2C0/+0x2C4, then calls151256BC. Source reads occur
  after the provider, preserving its possible mutations.
- Each selected branch calls151236D0 then151284C4 and returns1. With no
  selected bit,15126378 nonzero calls151284C4 and returns1; otherwise return0.
  Ignored helper returns do not gate these effects.
- The previously implicit1512A360 call now has its existing void(u8*)
  declaration and matching argument cast. Its source/object stay unchanged.
  Other unfinished helper interfaces and bodies are not converted or credited.

## Raw copy and alias contract

The shared camera declaration has two f32 source fields and an unresolved
s32 third source field, while its destinations are f32. Numeric conversion
would change retail's copied bits. The first private draft's struct17 float
view also hid its cross-type alias requirement.

The adopted local CameraPositionBits14FF90 contains three u32 words. Its
aggregate assignment emits the same retail loads/stores without interpreting
NaNs, signed zero or the third word numerically. For GNU compilers the type
has __may_alias__; IDO sees the ordinary aligned word structure. GCC documents
that dereferences through this alias type can access other object types:
[GCC may_alias](https://gcc.gnu.org/onlinedocs/gcc/Common-Attributes.html#index-may_005falias-type-attribute).
This explicitly supports the tested GNU contract, not universal ISO C portability.
No shared struct108 layout/type repair is inferred from the copied representation.

An actual struct108 native fixture checks all0x9A0 bytes with strict aliasing
enabled at O0/O2/O3. An independent two-pointer alias probe sets a typed float,
writes its bits through the alias view, and reloads the float. Removing the
annotation makes that probe fail at O2/O3; O0 still passes. This native-only
control is separately compiled to the same IDO80-word body and bindings.
It is not counted among the12 semantic controls that fail in every native profile.

Alternatives: a plain three-u32 aggregate also matches IDO but lacks the GNU
alias contract. A byte aggregate emits86 words, a byte loop88, an unrolled
byte copy98; memcpy, builtin spelling, intrinsic pragma and bcopy each emit78
words with55 differences. None replaces the selected matching word copy.

## Original caller and scope

Aligned retail census has one direct call, ROM150368/VA15122EB8 in
func_15122C5C, with no aligned pointer/interior entries. Its delay slot passes
the original saved S0 camera address. Nonzero V0 skips the remaining camera
update. The production caller remains its existing zero-return C stub.

Tests execute the complete261-word ORIGINAL caller from entry through return
with the original target, compiled target or independent modeled target.
All512 cases agree on public memory, target calls/snapshots and result:
432 skip the tail and80 continue. They visit250 caller words and all78
reachable target words, including live pre-target flag changes. Other parent
providers stay opaque; their full argument protocols and gameplay are not claimed.
No caller conversion or matching credit follows merely from this connection.

The target has two unreachable duplicate words: flags load at15128580
(index16) and return-zero at15128668(index74). All80 words match literally;
coverage correctly requires the78 reachable words rather than claiming80 execute.

## Qualification and production audit

- **188 frozen inputs** cover owner/other helper sources and objects, original
  assembly, all production headers, compiler, retail image, layouts/guards,
  linker bindings and shared tool modules. All raw320 bytes and bindings are
  pinned; every single-byte mutation and binding-name mutation rejects.
- All **44 raw and padded neighbors**, normalized pools and the register-mask
  union stay unchanged. The actual **five-command Make recipe** reproduces all
  45 owner functions and the exact padded object. Five inherited compiler
  diagnostics remain(four Warning712, one Warning709); the target adds none.
  Its isolated compile has zero diagnostics. Unrelated declarations are retained.
- The generated-slice padder is inapplicable to this C owner: its existing
  func_15125490 has0x68 compiled bytes for a0x64 retail slot. The actual C-object
  padder preserves that inherited overflow. Raw/padded neighbor checks, actual
  Make and independent whole-image prediction cover the entire owner; no new
  padder exception, exclusion or overflow change is introduced.
- Private link objects must retain basename game_14FF90.c.o. Renaming that
  input causes GNU ld to introduce a different STT_FILE name/string geometry.
  With the canonical basename, the predecessor ELF reproduces production
  literally. The qualified ELF differs only in the target body and its extent
  **16->320**: **248 changed bytes, zero exclusions and zero metadata cycles**.
- All **6,052 function addresses** and every other body remain fixed, as do
  **189,088 protected bytes across720 owners**, Makefile, guards, headers and
  progress CSV. Corruptions of the body, unrelated image bytes and retail
  input reject the strict-image guard.
- **2,456 guest cases per body** cover predicate signs, all16 flag combinations,
  ignored bits, priority, post-call loads, raw float representations, provider
  effects and incoming-home mutations. Full literal machine state and access
  order agree; **34 fault-prefix pairs**, including five delay-slot cuts, agree.
  Wrapped addresses and a stack alias are guest-only, not native C claims.
- Six GNU links rebase the target and helpers independently and pass48 cases.
  All **12 compiled semantic controls** have public counterexamples and fail
  in native O0/O2/O3. The separate native alias control keeps identical IDO
  words and is effective only at optimized native profiles, as intended.
- Native32 **O0/O2/O3 each pass896 cases** through a typed s32(s32) callback,
  actual struct108 backing, all camera bytes, helper snapshots and strict
  aliasing, with trap UBSan. The three-u32 view is exactly12 bytes/aligned4;
  all relevant shared field offsets are asserted. No global alias option is disabled.

Five fresh focused checks pass in both tools environments before and after
installation. Shared smoke checks are fresh; three unchanged shared regressions
per copy are reused only by exact helper/test fingerprints. The isolated sibling
overlay binds the consumer root explicitly and records all read-only fallbacks;
it does not modify sibling's2434 inherited dirty paths.

Production compiles only this owner and matches the independent forecast.
The inherited whole-ROM checksum mismatch still makes make all exit2; existing
duplicate Make recipe warnings and the five inherited compiler warnings remain.
Post-review cleanup removes only two unused EOF blank lines from the oracle.
The original test receipts stay intact; strict old/new source hashes and
identical compiled Python code objects under Windows and WSL prove that the
executed program is unchanged. No semantic/test input change is exempted.
Tools commit before consumer. Routine review uses zero Claude calls; frozen
host Release remains untouched. Graphify uses a scoped AST refresh and explicit
retained-node evidence, not a full-corpus semantic extraction.

Fresh focused entrypoint under WSL:
python3 -m unittest tools.tests.test_game_camera_transition_dispatch_15128540_match -v
Receipts: conker/build/game-camera-transition-dispatch-15128540-match/.
Next queue: func_1512E4B0, the selected secondary camera positioning helper,
subject to a fresh audit and no early credit. The80% goal remains active.

Production ELF SHA-256: 4d8e5032726f5931843b6a7b31a6395c44e5eedb782c946e308650ef7c2e2592.
Guard SHA-256: 6a6094f04735cb3127833e50b21f98c3374916605acd7aa79ccdebd80d22dfe7(unchanged).
