# 1870: Group actor channel normalization

Verified 2026-10-30. `func_1501E73C` replaces its zero-return placeholder in
[`generated_49D30.c`](../../conker/src/game/generated_49D30.c) with the recovered
`void(s32 group)` interface. It scans eight-byte records, resolves actors for
type-2 records and clears each channel/value pair when its unsigned value is
at least 10, before refreshing the resolved actor.

Actual linked recount: **3,947/5,506 (71.69%)** total, Game **3,274/4,833
(67.74%)**, Init 492/492, Debugger 181/181, zero drift. The active 75% goal
needs **183** more exact functions to 4,130/5,506. The C inventory is unchanged.

## Behavior, source and compiler layout

The count byte is `D_800C363A[group]`; the record-base pointer is
`D_800C35F0[group]`. Only a record with unsigned halfword type 2 passes its
unsigned byte at offset 2 to `func_15083E90`. Missing actors advance to the
next record. For a found actor, byte 0x6C >=10 clears 0x6C then 0x6A; byte
0x6D >=10 clears 0x6D then 0x6B. It then calls `func_1507EABC(actor)`.

Count and table-pointer reads remain live across callbacks. The loop preserves
count contraction/expansion, moved record tables and aliases. The explicit
`goto advance` recovers the retail null-lookup route and duplicated count/shift;
a nested-if form emitted 53 words, while a separate record index added a saved
register and a 48-byte frame. Neither rejected shape is installed.

The selected C emits all56 words with the original 40-byte frame, S0 at SP20,
S1 at24, S2 at28, S3 at32 and RA at36. It uses the owner's existing O2/g3
no-unroll profile. A scoped helper declaration and concrete behavior comment
are included; shared headers and Makefile remain unchanged. All56 raw/padded
neighbor functions and pools are preserved; target/owner diagnostics are empty.

Five expected-word/relocation guards at offsets0x28,0x2C,0x34,0x38,0x3C reorder
the opening address construction and counter initialization. The six-operation
multiset, including the unchanged branch, is identical. Table HI/LO bindings
move from0x34/0x38 to0x28/0x2C. There are no inserted/omitted words, frame
adjustments or alignment words. All56 normalized words and six bindings match
retail. The inherited guard CSV is retained as an exact byte prefix.

Raw C can leave a different caller-saved T8 value on an empty group. Full guest
state claims therefore compare original with normalized code. Raw C is checked
against the independent public behavior and memory-trace reference. This
distinction is tested explicitly rather than hidden by the harness.

## Qualification and limits

Artifacts: `conker/build/game-group-actor-channel-normalize-1501E73C-match/`.

- Guest: 2,692 cases /8,076 executions cover all56 words, all count, selector
  and channel bytes, null results, live bounds/table mutations and four actor
  alias layouts. There are112 fired access prefixes (9 delay-slot cuts), two
  lazy unmapped paths and144 cases across three independently GNU-linked
  layouts with HI/LO carries. The original and normalized programs agree on
  complete state and trace; raw C agrees on public effects and memory trace.
- Original helpers: 1,152 cases per program connect the72-word lookup and
  28-word refresh, with only `func_1507E7E4` bounded. Lookup covers68/72 words;
  offsets120/156/192/228 are unreachable duplicate loads retained exactly.
  Refresh covers28/28. First-live matches, inactive entries, all unrolled
  return lanes, null IDs and missing results are checked. Fields are observed
  before refresh; the inner provider then mutates channels across0/9/10/255,
  preventing the helper from concealing missing target clears. Both existing
  helpers are already exact and receive no additional credit.
- Caller: 384 cases per program execute the original six-word window at
  VA0x1501E8C0..0x1501E8D8, including group-from-S0, pointed gate clear and
  branch-delay `D_800C3638` clear. The current parent `func_1501E81C` remains
  a placeholder; complete-parent or current-caller equivalence is not claimed.
- Native32: 328,192 cases per O0/O2/O3 profile pass trapping UBSan, SDK ABI
  checks and13 effective controls. Exact call/pre-refresh logs, live count/table
  changes and record aliases are checked. All13 IDO-compiled controls also
  fail the independent reference. The stride control has an explicit type-2
  pattern in unused record bytes, so extra visits cannot remain invisible.
- Guards:235 normalization rejection controls cover every raw byte, bindings,
  lengths and scope. Nine actual padder rejection tests cover word preimages,
  relocations and foreign functions. Foreign owners do not receive these
  guards. Isolated guard tests use the exact target-row subset; full-owner and
  Make checks consume every inherited owner row and fail on unapplied guards.
- Three actual Make commands reproduce the qualified padded object. Production
  equals the independent complete-image prediction, ELF SHA-256
  `1c987848c0ca140b5cb53c73495df96c74011d8e17df783e296b94c6ff164c1e`.
  Exactly166 bytes change:165 target-code bytes and one target-size byte;
  metadata0 and exclusions0. All6,055 other bodies, all function addresses and
  189,088 protected Game bytes across720 owners remain unchanged.
- Both tools copies pass eight fresh canonical checks plus project-tools checks.
  Production runs two fresh installed checks per copy, explicitly reusing six
  unchanged checks only through identical input/module/artifact fingerprints.
  The16,982-file seal validates all other inputs. Existing guard consumers are
  pinned during the scoped production build; their objects and linked bodies
  are audited rather than excluded from comparison.

These are finite native and bounded helper tests. They do not establish
portable fault/private-home/FCSR behavior or hardware/gameplay acceptance.
Guest-only count and stack aliases are separate from valid native record aliases.

## Banking and continuation

Tools commit **ef1cee73e3d58b0979b2ad25b64c3a2cd8d7d2e3** precedes the consumer pin. No push occurs. Root README
changes only its two aggregate exactness rows. The independently dirty older
tools mirror is preserved. The scoped AST graph retains prior nodes and valid
relationships, retiring the false s32 return relationship with before/after
source evidence. Guard data is bound by its CSV hash and exact rows; this is
not a full-corpus extraction or fresh global clustering claim.

Next private screen: **func_151193F4**. Other private candidates remain uncredited until
their complete source, ABI, semantic, owner, production and documentation gates.
