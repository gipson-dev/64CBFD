# 1752 - Object event retarget callback guarded C match

Verified: 2026-10-27. Target `func_151D324C`, owner `game_1FFF60`.
VA `151D324C..151D3308`; retail ROM `2006FC..2007B8`.

## Result and recovered interface

Replace the false zero-return placeholder with a complete semantic event handler.
Its interface is `void(struct224 *object, struct223 *event, u8 command)`.
Reuse the shared records without changing any header or neighboring definition.
The object reference and tag are at +0x10 and +0x14; the callback selector byte
is at +0x1D. The event carries two word references at +0/+4 and their tags at
+8/+9. Read the first event word before the object's current reference.

Command zero calls the existing `func_151D33FC` release check. Command 0x2D
replaces a matching reference with the opposite event word and its associated
tag. The first reference has priority when both match. Load each tag after
storing its replacement reference, preserving guest overlays in which the store
changes the following tag byte. Other commands leave the pair untouched.
Finally, load the current selector and callback from `D_8008FC64`; call it
with the object, event and byte command when nonnull. The selector/table lookup
occurs after the release check or retarget writes, including provider changes.
The routine's physical V0 is not a public return value.

## Four checked compiler guards

Normal O2/g3 emits 46 words /184 bytes with the correct 24-byte frame and three
bindings. Four literal expected-word guards restore the 47-word /188-byte retail
slot. They check empty relocation lists at the guarded inputs:

| Raw offset | Expected | Replacement | Insert after |
| --- | --- | --- | --- |
| 0x014 | 14C00009 | 14C0000A | none |
| 0x034 | 10000013 | 93A60023 | 10000014 |
| 0x038 | 93A60023 | 9089001D | none |
| 0x070 | 54790005 | 57230005 | none |

This restores the command reload before the jump, moves the selector load into
its retail delay slot, adjusts the opening branch for the added word and
retains the equivalent order of two equality operands. It does not synthesize
missing behavior. The three raw bindings are +36 JAL `func_151D33FC`, +136
HI16 and +148 LO16 `D_8008FC64`; after insertion they are +36/+140/+152.
All inherited CSV bytes are preserved and exactly four rows are appended.
This is guarded C, not a compiler-only match. The clearer 46-word C was chosen
over a 47-word source variant requiring eleven register/scheduling guards.

This legacy owner uses `pad_c_object` with the retail layout CSV. Verify its
actual Make plan: IDO compact compilation, legacy padding, then assembly.
All 19 compact functions agree with that real recipe; all 18 neighbors and
pools remain unchanged. The owner retains its existing 14 type warnings, with
no new warning; the isolated target has no diagnostics. The inherited duplicate
12D630 recipe warning also remains. One retail redundant load at offset 112
is unreachable; all 47 words are checked literally and all 46 reachable words
are exercised.

## Registry and original caller boundary

The aligned whole-ROM census finds exactly one target pointer, at ROM 230C1C
(VA 8008C15C), and no direct JAL or tail J. The actual registry base is
`D_8008B4A8`: type 0x3E, stride 0x34, event callback field +0x1C. The nearby
`D_8008B4D4` label is not the base for this calculation. The tail dispatch
table at ROM 234724 is exactly `{NULL, func_15190550, NULL}`.

Ninety-six cases execute the authentic five-word caller window
`15169514..15169528`, including the current registry load, object/event setup
and byte mask in the indirect-call delay slot. The containing
`func_1516944C` C stub stays uncredited. Sixty more cases connect the complete
original 16-word release check, with a bounded release provider. These are
caller/helper boundary qualifications, not complete parent, object destruction,
tail-provider implementation or gameplay acceptance.

## Qualification and negative controls

Both tools copies pass eight fresh canonical methods and shared project-tool
checks. Each then runs two fresh installed owner/image checks, reusing the six
unchanged semantic checks only after exact module/input/artifact identity.

- 7,104 guest cases compare raw C, guarded output and retail behavior across
  every byte command, upper argument garbage, first/second/both/no reference
  matches, null/active callbacks, two stack phases and five layouts. Aliases
  include event data overlapping object fields and the incoming command home.
  Bounded helper effects change selectors, callback entries and the guest byte
  home. Full final private GPR/FPR/RAM/events agree; guarded PC/visit parity is
  literal. No portable C contract is inferred for guest stack overlays.
- Native32 O0/O2/O3 with trapping UBSan pass 9,216 positive cases per profile
  using valid shared records, typed helpers/callbacks and the three in-bounds
  table slots. Eight deliberate changes are rejected by result mismatches:
  missing release, wrong command, wrong tags, missing reference update, wrong
  priority, early selector capture and missing callback.
- Eighty-two injected access-prefix pairs compare full private state, memory
  trace and PC/delay ownership. Sparse mappings prove that unrelated commands
  with null callbacks need no event payload or current-reference mapping.
- Six GNU links across three layouts pass 18 guest rebase cases, including
  signed-low carries for the callback-table address. Three raw corruption
  controls and two actual legacy-padder controls fail closed.
- An actual compiled full-word-command mutant fails a high-word/low-byte-45
  case. Six whole-image corruptions and one inherited-manifest corruption
  are rejected. No sections or symbol metadata are excluded.

Initial test fixtures needed a mapped caller stop sentinel and a rebase helper
address outside the target's own instructions. Failed receipts are retained;
those fixture corrections do not alter the qualified C or retail output.
Routine Claude calls: zero.

## Production, recount and banking

The normal production build reproduces the independently predicted whole ELF:
137 changed code bytes plus one function-size metadata byte, 138 total.
The target extent changes from 12 to 188; all other named definitions remain
fixed. All 6,056 function addresses, 6,055 other bodies and 720 protected Game
data owners /189,088 bytes remain unchanged and exact. No new metadata cycle
is introduced. The inventory CSV is byte-identical.

ELF SHA-256:
`dbe02a2e46395ef932bc7f16f3e5edbd4d70796f073678c41766e786de4dbd3e`.
Native CRLF guard CSV SHA-256:
`f867c3817abab6b6ef822343afa48a4b188e7067ce1d4c69a078b54a6f4b4c40`.
Git stores the normalized LF form; verify both the inherited normalized prefix
and the four appended rows independently.

The Native/cache audit seals 16,187 inputs and 158 focused inputs. Only the
qualified source, four-row guard append, object, ELF and map differ before
documentation. Recount the captured adopted Native ELF against the unchanged
C inventory:

| Section | Exact C functions | Different | Drift |
| --- | ---: | ---: | ---: |
| Total | 3,830 /5,506 (69.56%) | 1,676 | 0 |
| Init | 492 /492 (100.00%) | 0 | 0 |
| Game | 3,157 /4,833 (65.32%) | 1,676 | 0 |
| Debugger | 181 /181 (100.00%) | 0 | 0 |

Only `func_151D324C` becomes exact; converted counts remain fixed. The 75%
threshold is 4,130, leaving 300 matches. Remaining source screens contain
1,547 placeholders, 120 semantic/other definitions and nine unlocated entries.
These screens are not qualification.

Predecessor consumer `bd1f46271aa8902cce54189d108aeabf435b8107` and tools
`d6359407c83911a42f902ddfab81e43ee2e01bec`. Bank tools first at
`48c9c089ae9380bddc235552a1ca59ec28a8a0ff`, then the consumer source, guards,
pin and measured docs. Keep the older mirror's 1,714 inherited dirty paths plus
two new tools files without committing its independent history. No push.
The root README changes only its two aggregate matching rows.

Refresh the ten changed C/Markdown/tool sources with Graphify, retaining or
uniquely relocating every old node and preserving every still-valid directed
relationship and its context. Retire only the obsolete placeholder s32 return
using both declarations; the recovered API returns void. The CSV ledger is
verified separately. Outside-scope freshness and communities remain historical;
no full-corpus extraction or global clustering/centrality claim. Raw, canonical,
production, graph and independent final-audit evidence remains under
`conker/build/game-object-event-retarget-match/`.

Next inspect `func_1507E114` in `game_A9D90`, then `func_150D2110` in
`generated_FF5C0`, with a new frozen predecessor and caller/ABI audit.
Keep `func_1514E920` private and uncredited. The 75% goal remains active.
