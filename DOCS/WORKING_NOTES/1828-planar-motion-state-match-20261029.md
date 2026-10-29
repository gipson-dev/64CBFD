# Planar motion state callback C match

Verified 2026-10-29. `func_150C308C` replaces the zero-return placeholder and
obsolete commented decompiler output in `conker/src/game_EF410.c`.
VA150C308C..150C3160, ROMF053C..F0610: 53 words/212 bytes, 32-byte frame,
nine external bindings, no alignment words or compiler-profile changes.

## Recovered contract and naming

`s32 func_150C308C(u8 *actor)` reads the signed halfword at actor+0x1C.
States below six skip the motion providers and return one. Otherwise it
gets the current player's motion vector from `func_15144B34(D_80082FA4)`.
The provider has one integer argument; the old decompiler's apparent extra
argument was a live flag register. Its local declaration now matches the
existing `f32 *func_15144B34(s32)` definition in `game_16EE20.c`.

The callback computes motion[0]^2+motion[2]^2. A value below D_800A0310
(retail 2,500,000f) requests state five. Otherwise `func_150484A0` computes
the planar angle, and `func_15144C8C` compares it with actor+0x160.
A result above D_800A0314 (retail approximately 0.4f) also requests state
five. Every route returns one, preserving the callback dispatch contract.
The original symbol name is retained; actor, motion, stop, x and z describe
the recovered roles without assigning an unproved gameplay name.

Separate statements preserve the heading load after the angle helper and
the angular-threshold load after the difference helper. Provider mutations
of these values and the state halfword are covered explicitly. Equality
uses the original strict comparisons; quiet NaN and infinity cases retain
the emitted MIPS behavior. No hardware FCSR or gameplay acceptance is claimed.

## Two checked register substitutions

The semantic C emits all 53 words at the original extent. Two words differ
only in the closed squared-length floating temporary: offset0x54 changes
ADD.S destination F0 to F12, and offset0x58 changes C.LT.S input F0 to F12.
The guard CSV checks both original compiler words before replacement:

| Offset | Expected compiler word | Retail word |
| --- | --- | --- |
| 0x54 | 0x46062000 | 0x46062300 |
| 0x58 | 0x4608003C | 0x4608603C |

No arithmetic opcode, memory operation, branch, binding or call is changed.
The original inherited CSV prefix is byte-for-byte preserved, followed by
these two rows. Raw C agrees on public memory, calls and integer return;
normalized code agrees on complete guest registers, memory and event trace.
Raw F0 is volatile and may differ on the short return path.

Raw C SHA256: `3be6459c58f8bfbd767abf2ea7d6743476db85392fba865573b117498ab0a73a`.
Retail slot SHA256: `677d80795d7ccb46e08e313e46cda1f88abae35a81b20c40f33e59674850a3fb`.

## Caller and validation evidence

An aligned ROM scan finds no direct JAL and one full-address registration
at ROM22E7C8 / VA80089D08, entry60 of D_80089C18. This does not exclude
encoded or computed calls. The original `func_1513B798` dispatcher runs its
complete41-word window through the active callback route in18 cases, with
actor[0x10]=0 and actor[0x11]=60. The callback's one integer argument and
constant-one result preserve that route. Other removal/lifetime routes
and complete provider semantics receive no new matching credit.

Eight fresh methods pass independently in both canonical tools copies,
along with each copy's project tools checks:

- 960 guest cases /2,880 executions compare original, normalized and raw C;
  signed-state boundaries, magnitude/angle equality, quiet NaN, infinity,
  provider side effects and two stack phases are covered.
- Native32 O0/O2/O3 with UBSan:600 cases per profile and six rejected
  controls for signed-state interpretation, state-six boundary, magnitude
  equality, angular equality, early heading and early angular-threshold load.
- 36 access-fault prefix pairs and two sparse-memory skip cases pass.
- Three independent GNU layouts /24 guest cases preserve all nine bindings,
  including signed-low-half relocation boundaries.
- 221 raw-byte/binding controls, four guard controls and216 image mutation
  controls reject corrupted candidates or prove effective behavior changes.
- Full primary-owner compilation preserves17 compact neighbors and pools;
  actual Make's five commands reproduce the padded object without warnings.

52 of53 original words are visited. The duplicate load at150C30FC is
unreachable after an unconditional branch; its original word remains exact.
Sparse skips and fault-prefix checks describe emitted MIPS behavior, rather
than portable C fault guarantees. Provider hooks are bounded contracts.

## Production and progress

Tools were committed first at `1d8b2c70b27e27b8f6a44dababc782da7adf4ad6`. Production reproduces
the independently predicted image:151 code bytes and one target symbol-size
byte change, with zero other metadata changes or exclusions. All6,056
disassembled function addresses and6,055 other bodies remain fixed.
All189,088 protected Game bytes across720 owners stay exact. Linker map
and C inventory CSV are unchanged; only the two reviewed guard rows append.
Each tools copy then passes two fresh installed checks, with six semantic
checks reused only through complete input/module/artifact fingerprints.

ELF SHA256: `b78eb6e337b9812eafa3e14a4ec40998c965ae6270022da158df5c20d34ed69f`.
Object SHA256: `071cff0676051f9db395d46ca11858c75f32f720768404daf2c2c4cf1fd604cf`.
Source SHA256: `3da98ac07f593b9bb1719a49538eaa31659280db3a6f8d17de6fddf67f15b761`.

Actual ELF recount: **3,905/5,506 (70.92%)**, Game3,232/4,833 (66.87%),
Init492/492 and Debugger181/181, zero drift. **225 more** are needed for
the4,130-function75% threshold. The older tools mirror preserves1,922
inherited dirty paths and adds only three new qualification modules;
it is not committed. The root README changes only two aggregate rows.

Graphify receives a scoped structural refresh with historical nodes,
relationships and out-of-scope manifest rows retained. Its graph is a
navigation aid, not the source of byte-match credit or runtime evidence.
Historical clustering and centrality are not recomputed.

Local ignored evidence: `conker/build/game-planar-motion-state-match/`.
Next screen: `func_15163FEC`. The private allocator `func_15187EC0` and
parked `func_1514E920` / `func_151D7000` remain uncredited. Keep the wider
75% goal active. This commit is local; no push is performed.
