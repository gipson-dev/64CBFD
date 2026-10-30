# Note 1872: save checksum submission match

2026-10-30. `func_15007360`, owner `game_33990`, replaces its zero-return
placeholder with `void func_15007360(void)`. VA `0x15007360..0x15007440`,
ROM `0x34810..0x348F0`: all 56 words reachable, 224 bytes, frame 32,
RA at SP+20 and the writer's otherwise unused result at SP+24. Existing
O2/g3 profile is unchanged. Tools commit: `6bd651c26537fe69204cfd7ca9167fc77da66dd0`.

## Recovered source and bounds

`SaveBlock33990` describes the 112-byte save block rooted at `D_800BE2F0`.
Its first halfword is the checksum. The union's byte view keeps the complete
block in bounds while its halfword view gives the checksum its proper width.
The seed symbols `D_800BE2F2` and `D_800BE2F3` alias bytes 2 and 3; the
retail data symbol `D_800BE2F4` aliases byte 4. No shared header or data owner
is changed. The complete C owner retains all 17 other functions and pools.

The checksum starts at `0xCC + 4*seed2 + 8*seed3`. Bytes 4 through 103
contribute `byte << (index & 3)`, with a 16-bit result. IDO unrolls the
100-byte loop four at a time. Truncating after each byte or four-byte group
has the same modulo-65536 result; even the largest untruncated total is
98,889, so signed 32-bit intermediate overflow is impossible. The scalar
C loop and retail's four-byte loop consume exactly the same bytes and weights.

The checksum is stored before reading the disable flag `D_8002AC5C`.
When that byte is zero, the routine calls `func_151DCEF0` with the
`D_800BE900` queue, command `0x44`, the block pointer and length `0x70`.
The result is deliberately retained through a volatile local. Placing that
local between the checksum and index recovers its original SP+24 lifetime
and frame32; no guard changes the frame or result home.

## Nine closed guards

Raw compiler words SHA-256:
`b4633c45e22edea4384385bff9d378190669c77fa8086914cc5a1602c84cb4b8`.
Original normalized words SHA-256:
`dbed982f5e39ef09cf4a39bf885eace6bdaf257debc57284e8a6e99f40af41ea`.
There are 13 bindings. The only new guard offsets are
44, 48, 52, 72, 76, 100, 104, 108 and 112. No insertion or omission.
This is normalized byte-exact C, not a direct raw compiler byte match.

The changed windows `[44,56)`, `[72,80)` and `[100,116)` contain pure integer
operations only. Each linked raw/retail window has the same operation
multiset, and an independent expression-DAG interpreter proves all 32
registers equal at its exit for arbitrary incoming register expressions.
There are no memory or control operations inside those windows. The first
window changes the equivalent relocation spelling `block+4` to the retail
data alias; GNU linking validates the alias relation across four layouts,
including signed-low and high-half carry boundaries. Full-body fingerprints
and explicit expected/replacement bindings make all nine guards fail closed.
All inherited CSV bytes remain an unchanged prefix in the qualified inputs.

## Behavior, ABI and independent controls

Coherent ignored evidence: `conker/build/game-save-checksum-submit-15007360-match/`.
`semantic_v15.py` and all eight private/canonical checks complete with exit 0.

- Main guest: 1,686 cases / 5,058 executions. Original, normalized and raw C
  agree in complete modeled state and memory-access trace. All 56 words are
  exercised, including the exact frame, saved RA, enabled result store and
  disabled untouched home. The provider observes all 112 bytes before it
  can mutate checksum/data/flag fields, preventing a callback from hiding a
  wrong checksum. Both supported stack phases and all flag-byte values pass.
- Fault prefixes: 213 access cuts across enabled/disabled routes. All three
  bodies agree in complete modeled cut state and trace. This routine has
  no memory access in a branch delay slot, so the delay-slot cut count is
  zero. These are guest instruction-model results, not portable C faults.
- GNU rebases: 51 additional cases over three independently linked layouts,
  preserving the block/seed/data aliases. All three bodies remain identical
  in complete state, access order and callback observations.
- Caller: one aligned retail JAL, ROM `0x49B74`; no aligned literal function
  pointers. The four-word original window at `0x1501C6C4` calls the no-argument
  routine and branches to `0x1501C6EC`. Thirty-six connected cases per body
  pass. Current parent `func_1501C57C` remains a stub; no full-parent claim.
- Original callee: all 58 words of `func_151DCEF0` are connected and covered
  in 48 cases per body. Request queue/command/source/length fields and the
  original timer ABI are checked independently. Poll scripts 0/3, 64-bit
  clock boundaries, wrapped `12000*ticks/1000000`, return values and stack
  phases pass. The bounded providers are `func_151DCFD8`, `__ll_mul`,
  `__ull_div` and `osSetTimer`. Its current C body is still a stub and gets
  no credit. No EEPROM device or hardware acceptance is claimed.
- Native: 524,288 cases per O0/O2/O3 profile with trapping UBSan. All 65,536
  seed pairs, eight gate/provider modes, checked 112-byte block/24-byte queue
  ABI, complete canaries, pre-provider observations and ten effective defect
  controls pass. Ten separately IDO-compiled controls also fail the independent
  public-memory/call/observation reference. The native harness alone disables
  GCC's unused-but-set-variable warning for the intentional volatile result;
  the tested source and IDO production flags are unchanged.
- Padder: nine bad word preimages, three bad relocations and a foreign-function
  row reject through the actual legacy padder. The full raw normalization gate
  also rejects 224 byte corruptions plus size, binding and scope negatives.
- Owner/Make: all 17 neighbors and pools remain fixed; all three actual legacy
  Make commands reproduce the complete padded object. Compiler/owner/executed
  command diagnostics are empty. The existing duplicate recipe notice remains
  in the Make plan and does not change this profile.

Both tools copies pass eight freshly executed canonical checks and shared
tool checks. Production repeats two installed checks per copy, reusing six
semantic checks only under exact module/input/artifact fingerprints. Fresh
execution and fingerprinted reuse are distinguished in the receipts.

## Whole image and banking

An independent pre-production prediction reproduces the final ELF literally:
273 changed bytes = 188 target-code bytes + one target-size byte + 84 metadata
bytes. The metadata changes are exactly three declared symbol/string pair
permutations: `D_800BE2F3`/`func_151BD750`, `func_151E5034`/`D_8009EDC4`, and
`D_800BE2F0`/`D_800BE6E0`. All named definitions remain equal except the
target's intended 12-to-224-byte extent. No section or byte exclusions.
Metadata slots and their string bytes have effective corruption controls.
Every other 6,055 function body, all 6,056 function addresses, and all
189,088 protected Game-data bytes / 720 owners remain fixed.

Adopted ELF SHA-256:
`1952d0caf95c252112f271bbd523a87d345ba216c81ef9a1dcd5849bb7c236b1`.
The actual Native ELF recount is **3,949/5,506 (71.72%)**, Game
**3,276/4,833 (67.78%)**, Init 492/492, Debugger 181/181; zero drift.
The conversion inventory CSV stays byte-identical. The 75% target remains
4,130/5,506, requiring **181** additional exact C functions.

The initial full-image probe stopped at symbol/string reorderings; the three
closed named pairs were inspected and added to the predictor before installation.
A private rebase fixture initially left its JAL provider in a different address
region; moving that provider with the entrypoint fixes the fixture. A native
fixture first treated the intentional unused result as an error; the narrow
harness warning exception described above fixes that diagnostic without adding
a volatile read or changing production C. Failed receipts remain archived.

Tools are committed before the scoped consumer source/CSV/docs/pin commit.
The older tools mirror retains all 2,054 inherited dirty paths; only three
new qualification modules are added without a mirror commit. No push.
The root README changes only two aggregate matching rows. Graphify structurally
refreshes the eleven changed supported files and separately binds the guard
CSV by exact rows/hash. Old nodes/valid relationships remain; only the false
s32 placeholder return edge is retired. Original caller/callee annotations
keep the current stub limitations explicit. No full-corpus or new clustering
claim is made.

Next private screen: `func_15063404`. All parked candidates remain uncredited. The 75%
matching goal stays active. Codex owns implementation/validation; zero Claude
calls, no REA, dependencies, account, browser, or sibling host-port changes.
