# Working Note 2080: Game effect-band packet callback guarded match

Date: 2026-11-04

## Result

`func_150C2700` at `0x150C2700` now replaces its zero-return placeholder
with typed semantic C in owner `game_EF410`. The recovered callback builds a
fixed eight-byte effect descriptor and a 0x40-byte position/effect payload,
submits the packet once through `func_15150178`, and returns one.

Retail contains 65 words and uses a 104-byte frame. Natural IDO `-O2 -g3` C
uses the same frame but emits 66 words. Twenty-four fail-closed expected-word
rows normalize this compiler-only difference: 23 checked replacements and
one checked omission of a duplicated constant load. The semantic descriptor,
payload construction, helper call, and return remain in C.

The function is not reached by a direct `jal`. Its sole aligned retail
pointer is at ROM `0x22F4CC`, callback slot `D_8008AA00[3]`. The recovered
interface is:

```c
s32 func_150C2700(
        void *unusedOwner, s32 unusedEvent, f32 x, f32 y, f32 z,
        s32 unused5, s32 unused6, s32 unused7, s32 unused8, s32 unused9,
        s32 unused10, s32 unused11, s32 unused12, s32 unused13, u8 channel);
```

Arguments two, three, and four are the binary32 X, Y, and Z values. Argument
14 is an unsigned-byte channel passed in the O32 stack arguments. The other
arguments are unused by this callback but remain explicit so the registry ABI
and incoming argument locations are documented accurately.

## Recovered packet

The typed locals preserve the retail stack layout exactly:

- `EffectBandDescriptor150C2700` is eight bytes with signed-halfword fields
  `0x6B`, `0x46`, `-0x1F`, and `0x2E`.
- `EffectBandPayload150C2700` is 0x40 bytes. It receives the caller's XYZ
  binary32 values; signed-halfword type/variant `6/5`; width/height
  `30.0f/35.0f`; lifetime/zero `100/0`; live globals `D_800A0274`,
  `D_800A0278`, and `D_800A027C`; opacity/scale `0x9B/100`; active/class
  bytes `1/6`; loop byte one; and positive-zero velocity, acceleration, and
  phase fields.
- Payload bytes `0x26..0x27`, `0x32..0x33`, and `0x39..0x3B` are reserved.
  C does not write them, matching retail's preservation of the pre-existing
  stack bytes.
- The helper receives `(&descriptor, &payload, 0, channel, 1)` exactly once,
  after which the callback returns one.

## Byte and relocation proof

The natural compiler body is 66 words and initially has 50 naive positional
differences because one extra word shifts the tail. Applying the checked
normalization produces the complete 65-word retail body:

- 24 guard rows, including exactly one omission at natural offset `+0x07C`;
- four relocation-aware rows move the `D_800A027C` HI/LO pair with its
  scheduled loads;
- seven natural and seven retail relocations;
- all 17 neighboring owner functions unchanged;
- no unguarded replacement, exclusion, address shift, or protected-data
  change.

The compact natural body SHA-256 is
`b115a366a626904c2fa1722f2162ec22c78cb7cc89750f4a47f3c645f0ad12c8`.
The linked qualified target and retail span SHA-256 is
`f37e65e340eb33515ecba468408eb38f24eb250fa7407e22042fe7ae9e5105a4`.

## Behavioral qualification

The big-endian guest model executes 64 cases per body: eight binary32 bit
patterns, four channel inputs (including high-bit and truncation cases), and
both tested stack phases. Retail visits all 65 words and natural C visits all
66 words. Every case submits exactly one byte-identical descriptor/payload,
returns one, preserves non-stack memory, and leaves all three reserved payload
ranges untouched.

Native 32-bit C passes 4,096 cases under each of `-O0`, `-O2`, and `-O3`, for
12,288 positive executions. Eighteen controls are rejected, covering every
descriptor constant, XYZ routing, type/variant, dimensions, lifetime, live
parameter source, opacity, class, positive-zero requirement, channel, and
return value. Injected memory failures produce 68 observations across 63
unique active boundaries. Callback slot `D_8008AA00[3]` remains the sole
retail reference.

The focused installed suite passes all four tests in 40.365 seconds. The
shared match-progress, generated-PC16, guarded-object, and protected-data
suite passes all 19 tests in 5.980 seconds.

## Image and production closure

The strict whole-image comparison covers all 6,052 linked functions, changes
only `func_150C2700`, keeps every function address fixed, and uses zero
exclusions. All 189,088 protected Game-data bytes across 720 owners remain
exact, with SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

The independently predicted qualified owner and ELF equal the fresh
production artifacts. A full `make all` path produces the binary and stops
only at the expected final retail SHA-1 check. The inherited duplicate
`generated_12D630` recipe warning is unchanged.

| Artifact | SHA-256 |
| --- | --- |
| Qualified / production owner object | `d2b39e2d24925aa10d41fdb4b55f4515c71979c194a17cf00cdc613b43740547` |
| Predecessor linked ELF | `fd81b5d15136d9e5062165e7e957bd7a8f651b08c43abd578977ef2e48fe7ff9` |
| Qualified / production linked ELF | `f47123d56f10403eb92105e7ba6107ba81bb24dab4ce2e323d84cecd8185df92` |
| Production rebuilt ROM image | `af74010913225d86f6dcdf7c1f68fc5718de540415062e9f26c31a35f20ae734` |
| Production map | `2ab021cc02cab424a5dae0e96a4ed5df1fe5f65ea58964f8e4e04b689771fbeb` |

## Recount and continuation

The fresh production ELF reports:

- Total: **4,151 / 5,512 (75.31%)**, zero address drift, 1,361 different.
- Init: **492 / 492 (100.00%)**, zero drift.
- Game: **3,478 / 4,839 (71.87%)**, zero drift, 1,361 different.
- Debugger: **181 / 181 (100.00%)**, zero drift.

The converted inventory remains 5,512 / 6,046 functions. The active 80%
target is 4,410 exact functions, so **259 more** are required. Rerank the
ordinary Game queue from this production ELF. Keep the seven documented
custom-ABI/compiler-boundary cases (`func_150A76F0`, `func_151F8870`,
`func_150A613C`, `func_150AE280`, `func_15115F68`, `func_151AE2BC`, and
`func_150A6760`) separate until their specific boundaries are addressed.

## Graph retention

The retained graph baseline is 58,552 nodes / 112,399 links / 5,098
communities with SHA-256
`bfe80b395ab84d2843ef215ed3bee163646cb17282f8aee715297125c801141f`.

The standard reduced `graphify update .` extracted eight uncached inputs but
proposed only 24,759 nodes, so Graphify correctly refused to overwrite the
retained corpus. Its fail-closed report retained 31,816 nodes from 3,754
still-present files outside the reduced scan.

An explicit eight-path incremental rebuild with `force=False` then produced
58,561 nodes, 112,408 links, and 5,117 communities. It retained 58,549 /
58,552 prior node IDs and removed no ID outside the changed-path set. The
three replaced IDs are line-derived `DOCS/UPDATE_LOG.md` nodes; twelve IDs
were added for their relocated forms and the nine new Note 2080 nodes. The
qualified graph SHA-256 is
`a29b3143d78eb37c2318c18ca17e3cf06f6f018ec648e3dc750a5afd47575b2e`.

After adding this receipt, a one-path stabilization detected no topology
change and left every qualified node and link untouched. The final graph is
58,561 nodes, 112,408 links, and 5,117 communities with SHA-256
`a29b3143d78eb37c2318c18ca17e3cf06f6f018ec648e3dc750a5afd47575b2e`.
