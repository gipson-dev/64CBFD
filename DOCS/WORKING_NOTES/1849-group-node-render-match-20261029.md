# 1849: Actor group node renderer match

Date: 2026-10-29. Target `func_15030F94`, owner `generated_5D2C0`.
VA `0x15030F94..0x15031070`, ROM `0x5E444..0x5E520`: **220 bytes / 55 words**.
The body fills its complete slot; there are no extra alignment words.

The zero-return placeholder becomes
`Gfx *func_15030F94(Gfx *cursor, u8 *actor, s32 view, s32 mode)`, matching
the existing caller declaration in `generated_58F80.c`. It returns the
incoming cursor when actor is null, actor+0x1D4 is zero, or unsigned group
byte actor+0x3B is zero. Otherwise it walks `D_800C3EE0` through node+0x54.
Each node's next pointer is saved before testing its unsigned group byte+0
and enable byte+3. An enabled matching node calls `func_150311C4` with five
arguments: cursor, node, actor, view and mode; its word return becomes the
next Gfx cursor. Actor group is read again on later iterations. Global head
and the initial actor resource gate are not read again after helper calls.

The inverse skip condition and separate assignments to the saved next pointer
recover the exact retail branch layout. The complete routine emits **all55
words and three relocations directly from C**, under the existing O2/g3
profile, without guards, insertions, omissions or frame adjustments. Its
original 56-byte frame saves S0..S5 at+28..+48 and RA at+52; the fifth helper
argument uses outgoing SP+16, giving a 20-byte outgoing area. The target
uses no incoming homes. View and mode are full-width signed words, not
matrix pointers; this follows the source caller and the retail forwarding.

The renderer provider `func_150311C4` remains its existing unrecovered stub.
Its existing word-return interface is declared before the recovered target;
the target explicitly casts that return to Gfx*. Its five-argument retail
call boundary is qualified with provider stubs. No new matching credit or
complete rendering behavior is claimed for that provider.

- Eight fresh canonical methods pass independently in both tools copies,
  plus shared checks. Production reruns two installed methods per copy;
  six unchanged semantic checks are reused only by full input/module/artifact
  identity. The older mirror retains 1,985 inherited dirty paths, with exactly
  three new qualification modules added there and no mirror commit.
- Guest: **3,980 cases / 11,940 original/raw/padded executions**, literal
  full-state equality and all55 instruction words covered. Coverage includes
  all256 actor-group and enable-byte values, empty/one/six-node lists,
  matching and skipped nodes, null/resource/group gates, full-width view and
  mode arguments, cursor wrap, caller clobbers, and **90 guest alias cases**
  where actor storage overlaps a node. Native alias acceptance is not claimed.
- Provider effects clear global head, remove the current link, change actor
  group, toggle a following node's enable/group, clear the actor resource
  word, or truncate a following link. Saved-next traversal and later live
  reads agree with the independent reference under all128 combinations.
  There are 124 access-prefix comparisons, nine sparse early-return runs,
  and three alternate layouts /72 rebased cases.
- Native32 O0/O2/O3 each pass **1,945 cases with UBSan**. Eight deliberate
  defects reject: missing resource gate, inverted group gate, inverted group
  match, inverted enable test, rereading next after the helper, cached actor
  group, ignored returned cursor, and wrong view forwarding. Full actor/node
  bytes, final head/cursor/marker, all five helper arguments and pre-call
  observations are checked. Guest alias cases are excluded from native tests.
- Full-ROM scan finds one direct JAL at ROM `0x5A980` / VA `0x1502D4D0`,
  and no aligned full-pointer words. Actual caller `func_1502CCFC` uses its
  mode home+0x168 to gate the call, loads view from home+0x158, passes cursor
  from S0 and actor from S5, sets argument4 to1 in the JAL delay slot, and
  captures V0 back into S0. The original eight-word window at VA
  `0x1502D4BC` / ROM `0x5A96C` runs48 cases; 12 executions verify nonzero
  caller mode skips the target. Earlier renderer gates and later graphics
  work are preconditions; no complete parent or gameplay execution is claimed.
- Complete-owner compile/padding preserves **39 neighbors** and pools. The
  existing Makefile requires `--rodata-symbol jtbl_80096F40_game`; supplying
  that unchanged setting reproduces the baseline and qualified object exactly.
  A preliminary pad without it had identical text/relocation bytes but wrong
  jump-table symbol names, and was rejected. Its diagnostic object is retained.
  Three actual Make commands pass with zero C diagnostics; the inherited
  duplicate-recipe Make warning remains. All223 raw-byte/binding controls
  and240 whole-image corruption controls reject.
- Independent prediction equals production: **162 changed bytes =161 target
  code +one symbol-extent byte**, zero metadata changes or exclusions. All
  6,055 other linked bodies and all function addresses remain fixed. Protected
  Game data stays exact across189,088 bytes /720 owners. Shared headers,
  compiler profiles, guard manifest and conversion inventory CSV are unchanged.

Fresh adopted-ELF count: **3,926/5,506 (71.30%)**, Game **3,253/4,833 (67.31%)**,
Init492/492 and Debugger181/181, zero drift. **204** more to4,130.
Tools committed first: `f21dabaedcbf7848da29f8d49537f4d2c546823e`. No push. Root README gets aggregate rows only.

The scoped eleven-file AST refresh retains or uniquely relocates all50,060
prior nodes and preserves103,779 valid old directed relationships. One
obsolete s32 return edge retires for the Gfx-pointer interface. Actual caller,
helper binding, cursor forwarding and saved-next semantics are annotated.
Outside manifest rows and analytics remain historical; no full-corpus claim.

Artifacts: `conker/build/game-group-node-render-match/`. Next screen `func_150CCCB4`
still needs full qualification. Other private candidates remain uncredited.
No host-port, frozen Release, save/editor, private-input or memory changes.
Zero Claude calls. The75% matching goal remains active.
