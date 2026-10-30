# 1869: Selector record coordinate payload

Verified 2026-10-30. `func_1500A7E8` replaces its zero-return placeholder in
[`game_36680.c`](../../conker/src/game_36680.c) with its recovered void interface.
All 56 words / 224 bytes and five relocation bindings emit directly from C,
with no guards, insertions, omissions, alignment words, frame adjustments,
shared-header changes or compiler-profile changes.

Actual linked recount: **3,946/5,506 (71.67%)** total; Game **3,273/4,833
(67.72%)**, Init 492/492, Debugger 181/181, zero drift. The active 75% goal
needs **184** more functions to 4,130/5,506. The C inventory remains unchanged.

## Behavior and recovered interface

The dispatcher table `D_80082BFC` has six entries for this function, commands
0x50..0x55. There are no direct J/JAL references and no other aligned pointer
literals in the full-ROM census. The routine copies six selector bytes from
`D_80082BF4` (retail IDs 2..7), indexes by `command-0x50`, then resolves that
record through `func_151149AC`. The command domain explains the apparent
negative offset in the original stack-relative byte load.

A missing record returns without accessing coordinates or allocating. A found
record supplies three signed halfword coordinates at offsets 0x10/0x12/0x14.
The 24-byte payload contains -400.0f, 4.0f, the record pointer and the three
coordinates converted to float. The header sets bytes 0/23, duration 300 and
byte zero, retaining its untouched padding byte. `func_1516037C` allocates the
payload with slot 255 and context 1. On success, it copies the payload to
effect+0x18; failed allocation leaves output untouched.

The recovered interface is `void func_1500A7E8(struct226 *actor, s32 command)`.
The local declaration order is header, payload, effect pointer, selector table.
This places the table at SP36 and recovers the last compiler word directly.
The earlier order placed it at SP40 and was rejected. The frame is 80 bytes,
RA is saved at SP28, the actor home is SP80, packet is SP48..72 (record at56),
and header is SP72..78. The source receives a concise behavior comment and its
disabled decompiler draft is removed. All 81 raw/padded neighbors and pools
remain fixed. Six inherited compiler warnings retain their exact source sites;
the target has no diagnostics and introduces no owner warnings.

## Qualification and limits

Artifacts: `conker/build/game-point-selector-payload-1500A7E8-match/`.

- Original/raw/padded execution: 2,688 cases / 8,064 executions, all56 words
  covered, with independent public packet/header/call references and complete
  guest state and trace equality. Cases cover every selector byte, signed
  coordinate extremes, lookup/allocation failures, callback mutations and
  output aliases. There are 78 fired access prefixes (11 delay-slot cuts),
  eight private incoming-home cases, two unmapped failure paths and 144 cases
  in three independently GNU-linked address layouts with HI/LO carries.
- Original dispatcher/helper execution: 434 cases per program exercise all
  six callback slots, invalid commands, null callbacks, null selectors,
  signed empty/negative counts and first/middle/last/missing search results.
  Every word is covered in the 17-word dispatcher, **28-word** original lookup
  and 32-word factory. Allocation and byte copy remain bounded providers.
  A preliminary 32-word lookup slice included four words from the following
  function; the corrected boundary is independently checked and fully rerun.
- The current lookup remains nonmatching. Executing its original words does
  not establish equivalence of its current C implementation and earns it no
  credit. The factory and dispatcher are already exact.
- Native32: 147,456 finite/signed/alias cases per O0/O2/O3 profile pass trapping
  UBSan with SDK size/offset checks and 14 effective semantic negative controls.
  IDO-compiled controls independently fail the guest reference. Native provider
  shims are noinline to retain external call boundaries; this also prevents an
  intentionally invalid null-copy control from being folded into the harness.
  The raw compiler and all binding bytes have 229 effective corruption checks.
- Five actual Make commands reproduce the padded object. Production equals
  the independent complete-image prediction, ELF SHA-256
  `8d40a1b98b135f365c61541faf5cbf914a79e4304873fabd2e3ac4b35a18dae6`.
  Exactly173 bytes change:172 target-code bytes and one target-size byte;
  metadata changes0 and exclusions0. All6,055 other bodies, every function
  address and189,088 protected Game bytes across720 owners remain unchanged.
- Both tools copies pass eight fresh canonical checks and project-tools
  checks. Production runs two fresh installed checks per copy and explicitly
  reuses six unchanged checks only through identical artifact/module/input
  fingerprints. The16,975-file seal preserves all other inputs. The production
  build completed before a driver-only stale path assertion failed; verified
  completion resumes its audit and installed checks without rerunning Make.

These checks do not claim portable C fault/private-home behavior, FCSR or
hardware/gameplay acceptance. Native shims model bounded external services.

## Banking and continuation

Tools commit **479d95e88cd09ff7348e0e4455225af556bfc469** precedes the consumer pin. No push occurs. Root README
changes only its two aggregate exactness rows. The older dirty mirror remains
preserved. The scoped AST graph retains prior nodes and all still-valid
relationships; one obsolete s32 return-type relationship is retired with
before/after source evidence for the recovered void interface. This is not a
full-corpus extraction or a fresh global clustering claim.

Next private screen: **func_1501E73C**. Other private candidates remain uncredited until
their complete source, ABI, semantic, owner, production and documentation gates.
