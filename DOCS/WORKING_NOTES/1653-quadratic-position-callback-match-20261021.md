# Quadratic Position Callback Direct C Match

Date: 2026-10-21

## Result And Scope

Restore `func_1517B7F8` in `conker/src/game/generated_1A89B0.c` from its
zero-return placeholder. The complete 41-word/frame0 routine emits directly
from normal O2/g3 C with no relocations, instruction guards, raw emitters,
shared-header changes, profile changes or omitted logic. Preserve the original
reference in `conker/asm/1A89B0.s` and the other 13 owner functions.

VA `1517B7F8..1517B89C`, ROM `1A8CA8..1A8D4C`, ends exclusive.
Raw C/GNU-original/retail body SHA-256:
`4bf70494ba05666dca2ef816374e5fcf6ac8dc30e3992b5cfa370cd172faad52`.
The current source has meaningful argument names and a purpose comment:
`s32 func_1517B7F8(s16 *input, s16 *output, s32 *counter, s32 unused)`.

## Recovered Semantics

Store the full unused incoming word in entry-SP+12. If the signed counter is
at least 0xD00, return one without reading either position. Otherwise:

1. For counter below 0x100, copy input Y directly. For 0x100..0xCFF, store
   input Y plus `(0x190000 - (counter - 0x600)^2) / 0x1E00`, using signed
   integer division that truncates toward zero and a halfword output store.
2. Reload the counter after the Y store. When it is at least 0x200, subtract
   0x800 if it is at least 0xA01; otherwise store 0x200. Retain this fresh
   read rather than carrying the pre-store value across possible guest aliases.
3. Copy X, then Z, with sequential reads/stores, and return zero.

The multiplication is bounded on the executed C path: the operand is
-1280..1791, so the square and numerator fit s32. Extreme negative counters
take the copy path, not a signed-overflowing multiplication. Narrow stores
retain the retail halfword behavior. Guest cross-type/stack aliases qualify
the emitted machine instructions, not portable C aliasing or fault semantics.

An explicit captured-counter local produced 43 words and extra input-home
traffic. Repeated pointer reads restored 41 words but retained 18 allocation
differences. Splitting the quadratic numerator into its own assignment to
`offset` recovered the original allocation and all 41 words directly.
No guard or compiler-profile adjustment was needed. Keep the duplicate
comparison at VA1517B814: it is statically exact but unreachable in normal
control flow, so dynamic coverage is 40 words, not 41.

## Original Caller Boundary

The only aligned retail literal for the function is ROM2319B8 / VA8008CEF8,
in `D_8008CEBC` row five's 12-byte callback entry. No direct JAL to it occurs
in the frozen ROM. The actual table reference is retained in
`conker/asm/data/231970.rodata.s`.

Execute the original 54-word window `1517C658..1517C730` in
`func_1517BBAC`, connected to both the original and newly compiled callback.
Qualify all four argument registers: input record, output record, caller
SP+0xBC counter, and output+0xF unused pointer value. The caller consumes
zero as the keep-output join at1517C730 and nonzero as the skip join at1517C864.
The NULL table slot takes its original XYZ-copy path. Exercise the descriptor
signed byte and both opacity-clamp paths before dispatch. There are 192
caller phases and 53 reachable window words; the duplicate load at1517C708
remains statically present and unreachable.

The larger current `func_1517BBAC` is still a placeholder. This is original
caller-window qualification with the recovered leaf, not a complete current
parent execution, natural registration, rendered output or gameplay proof.
No C-caller declaration needs changing in this checkpoint.

## Focused Tests

Tools files: `experiments/game_parabolic_position.py` and
`tests/test_game_parabolic_position.py`. Both local copies contain exactly
the same final bytes.

| Run | Active tools | Older mirror | Errors / failures / skips |
| --- | --- | --- | --- |
| Final full pre-install suite | 8 tests, 10.510s | 8 tests, 8.950s | 0 / 0 / 0 |
| Fresh installed checks | 2 tests, 3.508s | 2 tests, 3.166s | 0 / 0 / 0 |

Explicitly reuse the other six checks per copy only under complete source,
raw/padded object, helper, input and image identity. They are not fresh
installed test runs. Shared project-tool checks pass in both copies.

- 6,692 guest counter phases cover every value 0..0xD01 plus signed extrema,
  both stack phases, full argument-home values and NULL-position early returns.
- 506 guest alias phases cover shifted position overlap, counter/position
  overlap and argument-home overlap. A compiled cached-counter control is
  distinguished on all 18 selected counter-alias probes.
- 116,656 native32 cases per optimization at O0/O2/O3 use trap UBSan, typed
  same-array s16 overlap, a disjoint s32 counter and complete object/fence
  comparisons. The independent reference squares in s64, then narrows the
  proven-bounded numerator for signed32 division. No cross-type guest alias
  is represented as defined native C.
- Eight compiled wrong-C controls are effective. Six independent original/C
  GNU links cover three bases and 96 rebase phases; no absolute-PC assumption
  or missing relocation is hidden. There are 250 fired root-access fault
  prefixes, including the incoming home store, and six strict-image corruption
  controls. Preserve all 22 historical/current input pins and the old object.

Initial fixture failures are not passing receipts: the freestanding reference
first requested __divdi3, the bounded caller oracle needed signed LB support,
and one caller branch needed opacity-clamp cases. The final reference keeps
independent wide squaring without requiring a runtime wide divider. Increasing
the lower threshold by one and moving 0xA01 to 0xA00 were behaviorally equivalent
at those boundaries; replace those ineffective negative controls with genuinely
different thresholds. Do not count the earlier runs as full passes. The final
whitespace-only cleanup was followed by both full suites again.

## Sealed Production And Preservation

The earlier Linux-local scratch directory no longer exists. Recreate a new
owned cache at `/tmp/cbfd-parabolic-sealed-3ssdob7w/64CBFD`; no dependency
installation, provider reconfiguration or host build is needed. Restore only
cache executable modes lost by the Windows archive; preserve live file bytes.

The inherited static manifest omitted the earlier mutable
`conker/build/src/game/generated_113D60.c.o`. A clean cache link exposed that
missing file. Add its verified live bytes to the inventory and explicitly
enumerate all 1,454 linker-object inputs. Require a full predecessor relink
to reproduce the entire committed ELF, SHA-256
`bba307cc6a04e01abe6d87053b9db3c28a4a76796345608cc9feaeadd24fc02a`,
before relying on cached qualification. Do not silently assume the inherited
file count covers the linker closure. All 15,782 current live/cache inputs are
then fingerprinted; task-fixture revisions are explicitly synchronized before
the final tests. Static and non-target inputs remain immutable through adoption.

The actual Make shadow executes three productive commands. Production Make
exits zero in 1.061s, rebuilds the owner, links the complete ELF and regenerates
progress. The inherited duplicate-recipe warning for generated_12D630 remains;
owner compiler diagnostics are unchanged. The full production image exactly
reproduces the independent prediction: **110 changed bytes =109 instruction
bytes + one symbol-size byte**, with zero metadata exclusions or permutations.

Installed ELF SHA-256:
`05264b64f004e8e7160542e4a63deeb776559ba1554e52b4efe15218ba5fa5c3`.
Installed owner object SHA-256:
`745ecc4f761e08777e33f52f3059acbf8a2bc2983f06e216b650383b5e2f83ef`.

All other 6,055 bodies and all 6,056 function addresses remain fixed.
All 189,088 protected Game-data bytes across 720 owners remain exact
(SHA-256 `0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`).
The complete guard manifest remains unchanged. Native adoption rechecks all
15,782 files before and after promoting only the owner object, ELF, generated
linker script and progress CSV. The private adoption helper's first attempt
stopped before promotion on an undefined local; correct it and rerun the
completed archive, rather than restarting production or assuming adoption.

Tools commit `81b53767a45e7faa8f3ea30124890901a5475d91` precedes the
consumer source/docs/pin checkpoint. Preserve all 1,518 pre-existing dirty
statuses/hashes in the older tools mirror; only the two task files are added,
yielding 1,520 dirty paths. Do not commit/reset/stash/clean that mirror.
Root README changes only its two aggregate rows. No push, host change/build/
launch, dependency upgrade or Claude call. Host Release remains frozen.
Refresh Graphify and verify old-node retention after the consumer commit.

## Measured Progress And Resume

The literal standard matcher exits zero against the adopted live consumer ELF:

| Section | Byte-exact converted C | Address drift | Still different |
| --- | ---: | ---: | ---: |
| Total | 3,721 / 5,505 (67.59%) | 0 | 1,784 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 3,048 / 4,832 (63.08%) | 0 | 1,784 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

The 75% threshold is 4,129; **408 more exact functions** are required. The
broader goal is not complete. The new ELF-pinned screen contains 1,651
placeholders, 124 semantic/other definitions and nine unlocated entries.

Next: `func_151D710C`, 41 slot words: 40 body words/frame24 plus one alignment word,
in `conker/src/game/generated_203E20.c`, reference `conker/asm/203E20.s`.
VA 151D710C..151D71AC, ROM 2045BC..20465C, ends exclusive; slot ends 151D71B0.
Static inspection shows the descriptor byte+0x43 gate, two segment-address
choices, two calls to `func_15133EEC` and a fifth-argument byte flag output.
Determine the real caller/return ABI and ordered graphics/helper effects
before drafting or installing. No new candidate or credit is claimed.
`func_150B3DD0` follows in the screen; keep the larger 862-word
`func_1508CAD8` owner stub queued rather than broad-converting it here.

Private evidence is under `conker/build/game-parabolic-position/qualified/`:
snapshots, source probes, raw/padded objects, original caller/negative/native
fixtures, test logs, actual Make receipts, first link, predecessor-relink and
linker-closure proofs, sealed production/adoption audits, literal matcher,
remaining queue, mirror-preservation proof and checkpoint audits. No ROM,
private generated fixture or build artifact is committed.
