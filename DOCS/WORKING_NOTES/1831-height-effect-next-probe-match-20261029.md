# Second kind-four height-effect probe C match

Verified 2026-10-29. `func_151AA09C` replaces the zero-return placeholder
in `conker/src/game/generated_1D6E80.c`. VA151AA09C..151AA170,
ROM1D754C..1D7620:53 words/212bytes,64-byte frame,four external bindings.
Normal O2/g3 profile and original assembly are retained.

## Recovered contract

`void func_151AA09C(u8 *input)` captures its owner, reads the attached actor
at owner+0x18, and prepares a three-float position. X/Z come from actor+0x14
and+0x1C. When actor+0x118 exceeds D_800A8F90 (retail -9500f), Y is that
value+100f; otherwise Y is actor+0x18 plus150f. Equality follows the latter
route. Quiet NaN and infinity behavior is checked against emitted MIPS.

`func_15045800(position,0,Y-300f,owner+0x34)` queries a height descriptor.
A nonzero result replaces position.Y with the descriptor's first float and
calls `func_151ABE40(position,descriptor,4,owner[0xC],owner[1])`. The two
metadata bytes reload after the query; query mutations of position.X/Z
are retained, and changing owner+0x18 does not redirect the second call.

The query has signature s32(f32*,u16,f32,HeightResult71820*) in its existing
generated_71820.c definition. The local void* output declaration preserves
the same pointer ABI without adding a shared type. The retained assembly
effect provider uses five arguments; its existing declaration in
generated_1F4650.c agrees with void(f32*,void*,s32,u8,s32). No shared header,
provider implementation or additional caller receives matching credit.
The original symbol is retained; local owner/actor/position names describe
the recovered roles without assigning an unproved gameplay identity.

## Checked normalization

The semantic C emits53 words at the original extent. Eight expected-word
guards normalize six independent setup words at0x14,18,1C,20,24,28, including
the exact moved threshold HI16/LO16 bindings, and one closed private spill
slot in SW0x80/LW0xA4 (SP+0x28 becomes SP+0x2C). No instruction is inserted
or omitted; arithmetic, branches and calls are unchanged. The inherited
guard CSV prefix remains byte-identical and exactly eight rows append.

Raw C agrees on public memory, calls and position payloads. Normalized MIPS
agrees on full registers, FPRs, memory, events and access traces. Raw stack
and fault traces are not claimed identical. Owner/actor objects are outside
the callee's private stack frame. Initial source forms exposed incoming
parameter-home lifetimes and local-array placement; the selected explicit
owner capture/local layout recovers the saved-register lifetime and frame.

RawSHA256 `9be248d879bd7f3634a86a597e4cbd850771fa42aea93bb308f08aa677f664df`.
Retail-slotSHA256 `11f886a1c90bff880bc379d876bd676eeaab96d44e2c35ca4a1e2782690e909b`.

## Caller and qualification

The aligned ROM scan finds no direct JAL and one full-address registration:
ROM22FAAC /VA8008AFEC =D_8008AFD0[7], verified directly in the frozen retail image.
This does not rule out computed/encoded calls. Original parent
func_15158D2C remains a C placeholder. Its10-word window at15158F40,
ROM1863F0, is connected in32cases with S1=owner,S2=required mask,S6=table,
V1=index7 and the earlier first-mask pass as explicit preconditions.
The second-mask pass/skip and its loop-index delay update are exercised.
Complete parent, first gate and full loop behavior are not claimed.

Eight fresh canonical methods and project tools checks pass independently
in both tools copies:

- 864 guest cases/2,592 executions compare original, normalized and raw C:
  threshold boundaries, quiet NaN/infinities, sourceY variants, returns0/1/-1,
  provider changes to descriptor/position/owner metadata and stack phases0/8.
- Native32 O0/O2/O3 with UBSan:432 cases per profile; six rejected mutants
  cover equality, high/low offsets, probe depth, omitted result height and
  stale metadata cached before the query. The independently rerun canonical checks use432 cases per profile.
- 56 access-fault prefix pairs,two sparse-memory skips,three rebased GNU
  layouts/24 guest cases,216 raw-byte/binding controls and10 guard controls.
- Fresh full owner preserves40 compact neighbors and pools. Actual Make's
  five commands reproduce the qualified object without diagnostics.
- Literal image controls corrupt all212 target bytes, the closed metadata
  records and both name blocks and selected header/outside bytes; no metadata is exempt.

52 of53 original words are visited; the duplicate load at151AA0F0 is
unreachable after an unconditional branch. It remains byte-exact. Fault
prefixes describe emitted MIPS access order, not portable C fault guarantees.
Provider hooks are bounded; hardware FCSR and gameplay are not claimed.

## Image, adoption and progress

The initial diagnostic link exposed two closed symbol/string permutations.
The predictor was then specified from predecessor names/values and validated
by a fresh full compile/Make/link. At ELF offset2859620, func_1515AB88 and
D_8009E7AC exchange slots. At2902132, D_800A8F90,D_800A8B40,D_800A4140,
D_800A0090 rotate into order1,2,3,0. All named values, sizes except the
restored target, types and sections are preserved. Exact names, contiguous
string bytes and lengths are checked. All53 changed metadata bytes are
included in the literal209-byte prediction; no metadata is excluded.
The hypothesis was formed after the initial diagnostic prediction mismatch.

Tools were committed first at `0929434721ba38c0eb91e98a9b268b2c4b2755a8`. Production reproduces the
independent209-byte prediction:155code,one target-size byte,53 closed metadata
bytes,zero exclusions. All6,056 disassembled addresses and6,055 other bodies
remain fixed. All189,088 protected Game bytes/720owners stay exact. Map and
C inventory CSV remain unchanged. Each tools copy then passes two fresh
installed checks, with six semantic checks reused only by complete fingerprints.

ELFSHA256 `74ec7deab8de6e07c41a7b8d9ee351a3672e71d26f78486d824e83309c470a07`.
ObjectSHA256 `e743fdc24fc0ffe5b7ca5b75869885c9c4aeb6876fe571d6959e033c871dfd9d`.
SourceSHA256 `b9ae37c668bcd3d8700d76360d2a1932f167188b195a2267fdbf13dd8b0684b3`.

Actual recount: **3,908/5,506 (70.98%)**, Game3,235/4,833 (66.94%), Init492/492,
Debugger181/181,zero drift. **222 more** to the4,130-function75% threshold.
The older tools mirror preserves1,931 inherited dirty paths and adds only
three modules, without a mirror commit. The root README changes only two
aggregate rows. Graphify receives a scoped structural refresh with historical
nodes/valid relationships retained; no full-corpus or new global analytics claim.

The earlier func_15163FEC reference-event investigation remains private and
uncredited. Its1,440 guest cases,77-neighbor owner audit and64 bounded caller
cases support semantics, but its52-word C still misses the53-word exit.
Read-only fingerprint-locked CFE/UOPT/UGEN/AS1 captures reproduce normal
objects and show the shared exit already present before final assembly.
No assembly insertion or artificial matching credit is used; its twin
func_15164134 is also untouched. Private evidence is retained under
conker/build/game-owner-reference-event-match/.

Current local evidence: `conker/build/game-height-effect-next-probe-match/`.
Next screen `func_15030310`. Other parked1514E920,151D7000 and15187EC0
remain uncredited. Keep the75% goal active. No push is performed.
