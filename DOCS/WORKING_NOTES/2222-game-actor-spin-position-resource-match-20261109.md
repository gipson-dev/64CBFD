# Game actor spin, position and resource update match - 2026-11-09

func_150DE458 now integrates actor spin, position and lifetime, then queues
its selected resource pair, replacing a zero-return placeholder. The complete
160-word / 640-byte slot is exact after seven strict temporary-register
normalizations. The semantic C emits the original frame 0x68 naturally;
there are no frame guards, insertions, omissions or compiler-profile changes.
Source: conker/src/game/generated_10B7D0.c; original: conker/asm/10B7D0.s.

Production total **4,291 / 5,513 (77.83%)**, Game **3,618 / 4,840 (74.75%)**,
Init 492/492 and Debugger 181/181. Zero address drift; 1,222 still different.
**120** further accepted matches are needed for 80%; the wider goal stays active.

## Semantic body and field evidence

VA 150DE458..150DE6D8, ROM 10B908..10BB88. The API is void(void *object).
ActorAngleState10B7D0 is a local 0xA0-byte view with a GNU alias attribute
for native builds. Shared actor headers and actual helper definitions stay fixed.

When the low two bits of byte 0x73 equal three, a signed global timestep is
converted once to float32. Angles at 0/4/8 integrate the three angular rates
at 0x60/64/68. Each result wraps once by 360 when negative or at least 360;
this is not a general modulo operation. Named zero/360 float bounds recover
the original frame naturally and preserve the complete floating instruction run.

Positions are the signed halfwords at 0x10/12/14. This is independently
visible in generated_13D350.c:198-200: those fields feed the matrix translation
row, including the existing vertical offset at 0x18. The final source names
position, integer velocity and float angular velocity separately. An earlier
private screen called the positions rotations; the naming review corrected
that interpretation and proved all nine raw functions/bindings unchanged.
Local field names describe measured use and do not assert original retail names.

The Y velocity at 0x5C first subtracts verticalAcceleration * timestep.
The three positions then integrate the signed halfword velocities at 0x5A/5C/5E.
Unsigned intermediate arithmetic preserves the retail low-word/halfword wrap
without signed multiplication overflow. The lifetime byte at 0x8A is captured
before these updates. Its 32-bit wrapped subtraction is interpreted as signed:
a positive remainder updates the byte; otherwise byte 0x6E becomes one.

Independently, type halfword 0x54 with bit 0x8000 ignored selects value 12.
The initial variant at 0x7C selects two entries of D_80090204, whose retail
words are 0x692,0x693,0x694,0x695. The pointer is captured once, but each ID
is loaded when visited. func_1510D0EC(id,&extent,3,0) returns a u32 address
and writes a signed-word output cell at SP+0x54. func_1510D874 receives actor,
address, wrapped address+extent-0x200, and segment pair 4/5 then 6/7.
Its real five-s32 interface is preserved, including the actor-address cast.

## Callback and helper qualification

The full aligned-word retail census finds no direct J/JAL entry and one
literal address at ROM 22D870 / VA 80088DB0. It is row 24 of D_80088C90,
with 12-byte rows. The original 22-word installer at 1509EBBC copies the
callback into actor+0x38, the second pointer into actor+0x78, and the third
word's low byte into actor+0x92. All installer words are executed in the test.

Both original indirect callers at 15113EE8 and 15113FC0 are qualified in
their surrounding 13-word and 30-word windows. The 48 case combinations
cover the removal gate, first/second iteration behavior and saved motion fields.
Four post-return V0 poisons demonstrate that the callback result is ignored.
All three root bodies run through these windows; complete original/normalized
states agree. This is a bounded caller-window proof, not the whole large parent.

The loader is an unchanged non-matching baseline function: original 162 words,
current production body 155 words. Its declaration and complete semantic source
were reviewed; neither version is silently credited as exact. The 19-word queue
helper already is byte-exact. Ninety-six connected cases execute the original
and production loader/queue implementations on resident-resource paths, including
signed priority-byte boundaries, both variants and queue capacities 0/7/8.
Allocation, decompression and hardware acceptance are outside this connection.

The native provider always writes the extent cell. Four guest-only cases also
compare original/normalized literal behavior when a bounded failure provider
leaves it unwritten. They do not claim portable-C uninitialized-read semantics.

## Matching, behavior and image gates

- Full 160-word length, frame 0x68, saved-register lifetime, output-cell offset,
  all branches/calls and loop delay slots agree. Only seven closed temporary
  register roles differ around resource-table setup and the returned extent.
  Exact expected words and relocation annotations guard each normalization.
  Both padders reject stale words/bindings; the inherited CSV is an identical
  byte prefix with exactly seven appended rows for this function.
- Eight owner neighbors remain fixed in raw and padded text/bindings, including
  the prior func_150DE32C match. Pools are fixed and there are no diagnostics.
  The compact object's GPR mask changes E3FFFFF6->E3FFFFFE and FP mask
  F0FF1->F7FF5 for the recovered routine; other register metadata is fixed.
  These are audited section changes, not exclusions. Both padders agree.
- Actual Make in an owned mirror uses the byte-identical Makefile and normal
  source/manifest names. Its object matches independent qualification. Production
  repeats one O2/g3 owner compile and yields the predicted object and ELF.
- Guest: 976 cases per body / 2,928 executions, all 156 reachable words visited.
  Four unreachable duplicate words at indices 36,57,76,118 remain literal.
  There are 131 access-cut pairs, including nine delay-slot faults, six rebased
  layouts / 18 cases, the connected helpers and the callback-window checks.
  Raw C public memory/calls agree; original/normalized complete literal states
  and fault prefixes agree. Float arithmetic uses a bounded nontrapping model;
  no N64 FCSR or gameplay claim is made.
- Native32 O0/O2/O3 each pass 976 cases with strict aliasing and UBSan.
  Expected complete actor/queue images come from the independent guest model.
  Fourteen compiled semantic controls are effective in both native and IDO
  guest runs. They cover gates, signed timestep, wrap boundary, acceleration
  order, lifetime, resource cursor, segment pair and address/priority arguments.
- Strict ELF prediction changes only the 640-byte target body and its symbol
  extent 12->640: **469 changed bytes, zero exclusions, no metadata permutation**.
  All 6,052 function addresses and every other function body remain fixed;
  all 189,088 protected data bytes match. Six image corruptions are rejected.
  Progress CSV bytes, Makefile and compiler profiles stay fixed. Recount adds
  exactly one total/Game exact function. The inherited whole-ROM checksum
  mismatch remains: make all exits 2; whole-ROM equality is not claimed.

Six focused checks pass before and after installation in both tools environments.
The sibling uses an isolated six-module overlay with explicit consumer roots and
dependency fingerprints. Its 2,434 inherited dirty paths are preserved. Fresh
shared smoke runs accompany three unchanged, exactly fingerprinted regression
reuses per copy; reuses are not fresh tests. The package freezes 599 inputs.

Tools commit before consumer; no push. Root README changes only aggregate rows.
Graphify receives a scoped AST refresh with old-node retention, not a full-corpus
semantic extraction. Host-port Release stays frozen. Routine work uses zero
Claude calls. Next audit: the unchanged non-matching func_1510D0EC loader.

Focused WSL check:
python3 -m unittest tools.tests.test_game_actor_angle_resource_150de458_match -v
Receipts: conker/build/game-actor-angle-resource-150DE458-match/.

Production ELF SHA-256: 1501e859635c9c4de35614de5bb60117e486bc0b965c7f18d7fa8e73cd903012.
Guard SHA-256: 8adae535ceeddc5e27cf0989e5eaad0de914ccb2ab8dce879f10a98639b7e173.
