# 1844: Live record dispatch match

Date: 2026-10-29. Target `func_150A278C`, owner `generated_CDE80`.
VA `0x150A278C..0x150A2864`, ROM `0xCFC3C..0xCFD14`: 216 bytes / 54 words.

The zero-return placeholder becomes a complete void actor routine. It tests
actor byte+0x65 once, exiting if nonzero. Otherwise it scans the live count
`D_800D3094` as unsigned, indexing the existing 52-byte `GeneratedCDE80Record`
table at `D_800D3098`. Records qualify exactly when flags+0x15 shifted right2
equals8, accepting bytes0x20..0x23. It queries `func_150A1DA0(actor, record, 0)`.
For a zero query result, it reloads the table pointer and dispatches actor,
unsigned selector+0x17 and payload word+0x18 to `func_15172E7C`.

The table and count remain live across helpers. The query may replace the
table, and dispatch must read from that replacement without repeating the
flag test. Both helpers may change the count, table, record fields or actor
gate. The gate is not rechecked. These reloads are measured retail behavior.
The original caller supplies the actor in A0 and ignores the result, supporting
the recovered void interface. Existing owner record definitions are reused;
only the dispatcher declaration and complete target body are added.

All 54 words and six relocations emit directly from C under the existing
O2/g3 profile. The original 48-byte frame saves S0..S5 at+20..+40 and RA at+44,
with 16 outgoing argument bytes and no incoming-home use. No guards, inserted
words, omissions, frame adjustments, shared-header or compiler-profile changes.
The guard manifest and conversion inventory CSV bytes remain unchanged.

- Eight fresh canonical methods pass independently in each tools copy, plus
  shared tools checks. After installation, two methods rerun per copy; six
  semantic methods reuse only complete input/module/artifact identity.
- Guest: 3,880 cases / 11,640 original/raw/padded executions agree in literal
  full state and cover all54 words. Coverage includes all256 flag bytes,
  disabled actors, zero and high unsigned counts, nonzero/high-bit query
  results, two stack phases and helper mutations of count/base/fields/gate.
  High-count cases terminate by the first query reducing the live count.
- Native32 O0/O2/O3 each pass1,940 cases with UBSan and reject eight controls:
  inverted actor gate, broad flag mask, inverted query result, cached count,
  cached table base, repeated actor gate, wrong record and wrong payload.
  Controls use finite-count fixtures. The native fixture normalizes payload
  words for comparison across host little-endian and guest big-endian layout.
- 137 access prefixes, six sparse executions, three layouts /216 rebase cases
  and72 original caller-window cases pass. The three-word caller window is
  func_1504A730 at VA1504AA14 / ROM77EC4: JAL, actor delay-slot argument and
  the next actor load. No complete caller/query/dispatch execution is claimed;
  helper providers are bounded, including their permitted memory mutations.
- Complete owner compilation/padding preserves27 neighbors and pools. Five
  actual Make commands reproduce the object with zero C diagnostics. The
  inherited duplicate-recipe Make warning remains. All222 raw-byte/binding
  controls and236 whole-image corruption controls reject.
- Strict independent prediction equals the production ELF:166 changed bytes
  =165 target code +one symbol extent; zero metadata changes or exclusions.
  All6,055 other linked bodies and all function addresses remain fixed.
  Protected Game data stays exact across189,088 bytes /720 owners.

Fresh actual adopted-ELF count: **3,921/5,506 (71.21%)**, Game **3,248/4,833
(67.20%)**, Init492/492 and Debugger181/181, zero drift. **209** more to4,130.
Tools committed first: `a683266f164de5f115475e34691516e5f39bb8a2`. No push. Root README gets aggregate rows only.

The scoped AST refresh retains or uniquely relocates all49,800 prior nodes.
It preserves103,261 valid old directed relationships; the recovered void
interface retires exactly one obsolete s32 return relationship. Source/binding
checks qualify both helper-call edges and the original caller window.
Outside manifest rows and analytics remain historical; no full-corpus scan
or hardware/gameplay acceptance is claimed. The75% goal remains active.

Artifacts: `conker/build/game-live-record-dispatch-match/`. Next screened
target `func_150DFBD0` still needs complete qualification. Parked candidates uncredited.
The older tools mirror retains1,970 inherited dirty paths plus three new modules.
No host-port, frozen Release, save/editor, private-input or memory changes.
Zero Claude calls.
