# Type-0x5B point effect — direct C match

Verified 2026-10-28. Restore `func_151DC8BC` in
`conker/src/game/generated_209B50.c`: VA 0x151DC8BC..0x151DC97C,
ROM 0x209D6C..0x209E2C, 48 words / 192 bytes and frame 72.
All words emit directly under the normal O2/g3 profile, with no guards.

## Recovered interface and behavior

`void func_151DC8BC(vertex *position, s16 lifetime, u8 companions, u8 flag, u8 group, s32 context)`

If companions is nonzero, invoke `func_151DC6A0(position, group, context)`.
Capture the three position words after that call, initialize the accumulator
to +0.0f and store the flag byte. Create an effect through
`func_15149130(lifetime, -1, 0x5B, -1, 1, 0, 20, group, context)`.
If allocation succeeds, copy all 20 payload bytes to the result at +0x28.
The three trailing payload bytes remain unwritten, as in retail. The guest
checks their literal copied values; native tests make no value claim for
those uninitialized bytes. No dummy local storage or word patches are used.

Declaring the real payload before the result pointer gives the original
stack layout. The earlier reversed declaration order had four SP offsets
four bytes low; the private initial artifacts retain that rejected screen.
The three J26 bindings stay at +44 (companion), +148 (factory) and +168
(memcpy). Raw compiler/original object SHA-256:
`948b4f456f7fca0195f7cbdfd6488af64b4e9be2e1fb7d2b336e01f22a4065f0`.

The local factory prototype correctly represents the extra-size argument
as an O32 integer word. The legacy shared pointer-shaped prototype and
retained factory source remain unchanged; original helper execution proves
that word 20 produces a 60-byte allocation. The companion remains an
old-style s32 C placeholder whose result is ignored. It receives no credit.
The retained callback table at 0x8008A654 points to `func_151DC97C`, whose
original reads support the neutral name `accumulator` for payload +0xC.

## Original caller and retained helpers

The full ROM census finds sites VA 0x15027254 / ROM 0x54704 and
VA 0x1502727C / ROM 0x5472C, both in `func_150265CC`; no pointer literals
reference this target. Execute the original dispatcher from its real entry
0x150265CC through command 0x1B and entries 3/4 of `jtbl_80096BE4`, then
through the saved-register/frame restoration and return. The first route
supplies companions/flag 1, the second 0. Both use a signed halfword lifetime,
the incoming point and group, context 0, and return their own value 1.
The packet skip route also returns 1 without invoking this target.

Across 144 dispatcher cases, 90 of its 3,451 words execute. This is coverage
of the selected routes, not the whole dispatcher. Its C placeholder remains
unchanged. The parser is a bounded 11-argument provider; companion effects
and the heap are also bounded providers in the connected guest runs.

Five retained helpers are checked against ROM and execute together:
factory (49 words), allocator (28), list initializer (20), bzero (40 including
alignment), and memcpy (11). The exercised routes visit 128/148 words;
48 separate helper cases cover success/failure, existing/empty lists,
context bytes 0/1/255, and both companion branches. Unvisited alignment,
other-size, and other factory paths remain retained without a coverage claim.

## Qualification and complete-image evidence

Both tools copies pass eight fresh canonical methods and shared tool checks.
Production runs two fresh installed methods per copy and reuses six unchanged
semantic methods only after exact module, input and artifact fingerprints.

- 1,405 guest cases cover every companion/flag/group byte, signed lifetime,
  late home reads, provider changes before/after capture, and 29 overlaps.
  All 48 target words execute; complete original/C states and traces agree.
- 1,040 fired access-prefix pairs preserve registers, memory, calls, PC and
  delay-slot context. Allocation failure skips the destination copy.
- Native32 O0/O2/O3 each pass 24,576 cases and six effective controls, with
  trapping UBSan, the actual six-argument void function pointer, and whole
  point/record fences. Tail bytes are excluded from native value claims.
- Three independent GNU layouts pass 60 guest cases using original,
  compiler and actual Make objects, preserving all three J26 bindings.
- Four actually compiled IDO semantic mutations fail expectations. Three
  raw body/binding controls and six whole-image corruptions are rejected.

The three-function owner preserves both neighbors and all pools. The real
padder and three-command Make recipe reproduce the qualified object exactly,
with zero diagnostics. The sealed production audit verifies 16,336 paths
and 333 focused frozen inputs. Independent whole-image prediction accounts
for every byte: 145 code bytes plus one symbol-size byte (12 -> 192), with
zero exclusions. All 6,056 addresses, the other 6,055 bodies, and all 720
protected Game data owners / 189,088 bytes remain fixed. Shared headers,
inventory CSV and the complete guard manifest are unchanged.

The first private helper run exposed a missing signed-byte-load operation in
the guest interpreter. Adding that literal LB operation made the retained
factory route executable; no production C change was needed. Guest overlaps
and fault prefixes qualify emitted instruction order, not portable C alias,
hardware exception, FCSR or gameplay behavior.

## Bank and measured progress

Predecessor consumer: `afd0ab04903b0b30425c26d4cf3477e47ba31f24`.
Tools committed first: `1c2d8ca70dae96012a6e8656ef8e202b2bcb2817`.
The older standalone tools mirror retains all 1,772 inherited dirty paths,
with only the three new qualification modules added. No push is performed.

Adopted ELF SHA-256:
`5ebcc1d909d33b946b7b6218c2852941b1c9ba6dafdd1306b97d914c007f9e31`.
Raw receipts: `conker/build/game-type91-point-effect-match/`.

| Section | Byte-exact C | Different | Address drift |
| --- | ---: | ---: | ---: |
| Total | 3,855 / 5,506 (70.01%) | 1,651 | 0 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 3,182 / 4,833 (65.84%) | 1,651 | 0 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

These totals come from the adopted native ELF, not the isolated candidate.
The 75% threshold is 4,130 exact C functions: 275 more are required.
Next inspect `func_15131828` in `generated_15D730`; its queue position is
only a screen. `func_1514E920` stays parked and uncredited.
