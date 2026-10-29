# Height-effect probe C match

Verified 2026-10-29. `func_151A99D0` replaces the zero-return placeholder
in `conker/src/game/generated_1D6E80.c`. VA151A99D0..151A9AA4,
ROM1D6E80..1D6F54:53 words/212bytes,64-byte frame,four external bindings.
Normal O2/g3 profile and original assembly are retained.

## Recovered contract

`void func_151A99D0(u8 *input)` captures its owner, reads the attached actor
at owner+0x18, and prepares a three-float position. X/Z come from actor+0x14
and+0x1C. When actor+0x118 exceeds D_800A8F74 (retail -9500f), Y is that
value+100f; otherwise Y is actor+0x18 plus150f. Equality follows the latter
route. Quiet NaN and infinity behavior is checked against emitted MIPS.

`func_15045800(position,0,Y-300f,owner+0x34)` queries a height descriptor.
A nonzero result replaces position.Y with the descriptor's first float and
calls `func_151ABE40(position,descriptor,3,owner[0xC],owner[1])`. The two
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

RawSHA256 `75087c54184f587b84c8de9364b80efd9a941ac77b58815dbe0937d99b638683`.
Retail-slotSHA256 `99742da01b260cb8de9f1f54a5e71356354d41f162bae5af4b462b836d8dad56`.

## Caller and qualification

The aligned ROM scan finds no direct JAL and one full-address registration:
ROM22FA90 /VA8008AFD0 =D_8008AFD0[0], also present in the retained data ASM.
This does not rule out computed/encoded calls. Original parent
func_15158D2C remains a C placeholder. Its10-word window at15158F40,
ROM1863F0, is connected in32cases with S1=owner,S2=required mask,S6=table,
V1=index0 and the earlier first-mask pass as explicit preconditions.
The second-mask pass/skip and its loop-index delay update are exercised.
Complete parent, first gate and full loop behavior are not claimed.

Eight fresh canonical methods and project tools checks pass independently
in both tools copies:

- 864 guest cases/2,592 executions compare original, normalized and raw C:
  threshold boundaries, quiet NaN/infinities, sourceY variants, returns0/1/-1,
  provider changes to descriptor/position/owner metadata and stack phases0/8.
- Native32 O0/O2/O3 with UBSan:432 cases per profile; six rejected mutants
  cover equality, high/low offsets, probe depth, omitted result height and
  stale metadata cached before the query. The first private v21 receipt
  overstated the loop product; corrected fresh v22 and canonical runs use432.
- 56 access-fault prefix pairs,two sparse-memory skips,three rebased GNU
  layouts/24 guest cases,216 raw-byte/binding controls and10 guard controls.
- Fresh full owner preserves40 compact neighbors and pools. Actual Make's
  five commands reproduce the qualified object without diagnostics.
- Literal image controls corrupt all212 target bytes, the closed metadata
  records/name block and selected header/outside bytes; no metadata is exempt.

52 of53 original words are visited; the duplicate load at151A9A24 is
unreachable after an unconditional branch. It remains byte-exact. Fault
prefixes describe emitted MIPS access order, not portable C fault guarantees.
Provider hooks are bounded; hardware FCSR and gameplay are not claimed.

## Image, adoption and progress

The initial link revealed a closed six-name ELF symbol/string permutation.
The predictor was then specified from predecessor names/values and validated
by a fresh full compile/Make/link. Group0x2CBEA4 rotates
D_800A8F74,D_800A8B24,D_800A4124,D_800A0074,D_8009F784,D_8009BB24 into
order1,2,3,4,5,0. Exact names, contiguous string bytes and lengths are checked;
all named values/types/sections remain fixed. This measured hypothesis is
not presented as having preceded the initial diagnostic failure.

Tools were committed first at `3871bb54c958642e63889f443a6a89537af0f181`. Production reproduces the
independent191-byte prediction:155code,one target-size byte,35 closed metadata
bytes,zero exclusions. All6,056 disassembled addresses and6,055 other bodies
remain fixed. All189,088 protected Game bytes/720owners stay exact. Map and
C inventory CSV remain unchanged. Each tools copy then passes two fresh
installed checks, with six semantic checks reused only by complete fingerprints.

ELFSHA256 `2806a69249698e1c1f31967a5686f22e956b45dbef90a88461dc410a36cff590`.
ObjectSHA256 `5b1242910e7542a8828fa8e5537674a5630df98fbabc488ad820f93f56880c62`.
SourceSHA256 `27d1ba01062a3a1a810adaefc09a8d1ae089ad17255328df91f9fd3d48c357f5`.

Actual recount: **3,906/5,506 (70.94%)**, Game3,233/4,833 (66.89%), Init492/492,
Debugger181/181,zero drift. **224 more** to the4,130-function75% threshold.
The older tools mirror preserves1,925 inherited dirty paths and adds only
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

Current local evidence: `conker/build/game-height-effect-probe-match/`.
Next screen `func_151A9FC8`. Other parked1514E920,151D7000 and15187EC0
remain uncredited. Keep the75% goal active. No push is performed.
