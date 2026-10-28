# 1758 - Screen overlay direct C match

Verified: 2026-10-27. Target func_151ED1E0, owner generated_215960.
VA151ED1E0..151ED29C; retail ROM21A690..21A74C.

## Complete SDK behavior and byte match

Replace the zero-return placeholder with the complete pointer interface:
~~~c
Gfx *func_151ED1E0(Gfx *commands);
~~~
All 47 words /188 bytes emit directly from normal O2/g3 with a 32-byte
frame, RA at SP+28, seven relocation bindings and zero guards. No profile
override, inserted words or new padding fields are needed. The existing
GLOBAL_ASM func_151EC648 remains assembly and unchanged.

When unsigned D_800E0B96 is zero, return the original cursor without
accessing the output, dimensions or rectangle helper. Otherwise append:

| Command | Word zero | Word one |
| --- | --- | --- |
| Pipeline sync | E7000000 | 00000000 |
| Other mode | EF082C3F | 00504340 |
| Environment combiner | FCFFFFFF | FFFEFB7D |
| Black environment color | FB000000 | reloaded unsigned D_800E0B96 |

Use real SDK macros. The mode is one cycle, perspective texture correction,
bilerp texture filtering, filtered conversion, disabled alpha dither and
magic-square color dither. Preserve the retail reserved blend-mask bits F
explicitly. G_RM_CLD_SURF/G_RM_CLD_SURF2 preserve the exact coverage SAVE
mode; XLU_SURF is a different command. Both combiner cycles select the
black environment color and its alpha.

The alpha read occurs again after storing FB000000, so writable guest
aliases can change it. Load height D_800BE624 and width D_800BE620 only
after completing the four commands. Call the existing pointer-returning
func_1501A6CC(cursor+32,0,0,width,height), returning its actual result.
The real retained rectangle helper adds one more command (40 bytes total).

An early return plus a direct final helper return restores every word.
The initial equivalent-looking conditional-body/final-return shape had
47 words but a different branch/tail schedule; it was not adopted. Preserve
initial-fit/, fit-interfaces*.json, selected-input.c and all receipts.
Raw selected/original SHA256:
~~~text
756925b0c28243ecd139ec9a5128afb499ca92c678403f00cd8b5ee20632751c
~~~

## Correct both pointer interfaces without changing caller instructions

The sole direct caller is func_151E84B0 at VA151E84C8 /ROM215978. Its
old no-argument declaration depended on A0 passing through unchanged.
Recover Gfx *(Gfx *) for the overlay, parent and D_8008FFF4 callbacks.
Retain the parent's existing IDO debug local-slot gap. Removing that
already-present gap changes the frame and was rejected; no new gap or
uninitialized read is introduced. The corrected parent remains exact
across all 92 words, frame32, bindings and private result home at SP+32.
All 26 other owner functions and pools remain unchanged.

In conker/src/game_45B80.c, correct the parent prototype and pass/store the
Gfx cursor directly through D_800BE9D0. All 16 compact functions and pools
remain unchanged. Execute its actual three-command IDO/pad_c_object/GNU
Make recipe before and after: both complete padded objects equal the
frozen production object byte-for-byte. This dependent owner is audited
explicitly, with no whole-section exclusion.

## Canonical semantic and ABI qualification

Both tools copies pass eight fresh canonical_v3 methods and shared project
tool checks in 7.47s /7.473s. The initial canonical run
found a fixture-only macro/local name collision in the deliberately wrong
early-dimension variant. Rename the fixture pointers and retain -Werror,
all failed receipts, the original selected C and strict UBSan flags.
The final run also connects the real upper cursor-load/call/store window.
Installed copies pass two fresh owner/image methods and reuse six semantic
methods only after exact sealed input/module/artifact identity.

- 2,224 guest cases sweep all 256 alpha bytes, dimensions and stack phases.
  Independent GNU links alias the gate to all 32 command bytes and each
  dimension to all eight command words. Compare full private memory,
  GPR/FPR, HI/LO, events, calls, visits and ordered access traces against
  retail and an independent sequential-write reference. Visit all 47 words.
- 3,072 cases execute the complete original/retained 92-word parent,
  preserving the mode set/clear, optional pointer callback, signed player
  gate, both blink masks, four text routes, late table lookup and final
  result-home reload. Visit 90 feasible words; duplicate constants at
  151E8578 and 151E85B8 are unreachable from the entry and are not claimed
  as exercised. Callback/color/text implementations remain bounded.
- 484 connected cases execute the actual original/retained 38-word
  func_1501A6CC rectangle helper. Verify clipping, masked coordinates,
  command words and returned cursor across signed dimension boundaries.
  Another 24 cases execute the actual three-word upper window at
  VA15018C4C /ROM460FC with the complete parent and overlay connected:
  load cursor in the delay slot, call parent, store returned cursor.
- Native32 O0/O2/O3 with trapping UBSan each pass 219,648 positive cases
  using real SDK headers and retained rectangle source. Cover all alpha
  bytes, all 32 host byte aliases, dimension-word aliases, opaque and real
  helper returns, eleven safe signed-subtraction inputs and full arena
  fences. Nine wrong C variants fail by their results. Native source uses
  valid Gfx storage and char/signed-counterpart views; guest big-endian
  memory and private stack overlap are separate oracle evidence.
- 48 fired access-prefix pairs preserve complete private state, trace,
  fault PC and delay ownership. Disabled output requires no output or
  dimension mapping. Three independent GNU layouts pass 15 cases across
  all seven HI/LO/J26 bindings. Three raw/binding and six whole-image
  corruptions fail closed. Actually compiled cached-alpha and early-
  dimension variants fail by value under real GNU output aliases.

No complete RDP implementation, live rendering/gameplay acceptance or new
conversion credit for already-retained callers/helpers is claimed.
Routine Claude calls: zero.

## Production, image and measured progress

The actual five-command generated-owner Make recipe reproduces the
qualified object including its one GLOBAL_ASM routine. Main owner and
selected IDO diagnostics are empty. The auxiliary owner's three old
pointer/integer warnings at source lines567/574/606 are unchanged before,
after and in production; no new warning is introduced. The duplicate
Makefile generated_12D630 recipe warning also remains. Production Make
exits zero in 0.584s and rebuilds both dependent owners.

The entire adopted ELF equals the independent 145-byte prediction:
144 target-code bytes and one target-size byte, zero exclusions. Only the
target extent changes 12->188. All 6,056 function addresses, 6,055 other
bodies and every other named ELF definition remain fixed. Protected Game
data stays exact across 720 owners /189,088 bytes. The map, inventory CSV,
guard manifest and shared headers are unchanged.

ELF SHA256:
~~~text
a30809f3c21bb03a4e0f17b363ad96821600731160f7381e0e49d0915c798c61
~~~
Native CRLF guard SHA256 (Git-normalized LF content unchanged):
~~~text
f867c3817abab6b6ef822343afa48a4b188e7067ce1d4c69a078b54a6f4b4c40
~~~
Seal 16,217 Native/cache inputs and 209 focused inputs. Recount the captured
adopted Native ELF with the unchanged inventory:

| Section | Exact C functions | Different | Drift |
| --- | ---: | ---: | ---: |
| Total | 3,836 /5,506 (69.67%) | 1,670 | 0 |
| Init | 492 /492 (100.00%) | 0 | 0 |
| Game | 3,163 /4,833 (65.45%) | 1,670 | 0 |
| Debugger | 181 /181 (100.00%) | 0 | 0 |

Only func_151ED1E0 becomes exact. Converted totals stay fixed. Threshold
4,130 leaves 294 more matches to 75%. The remaining source screen contains
1,541 placeholders, 120 semantic/other definitions and nine unlocated
entries. Typed func_151725FC and NULL factory func_1518F5D0 remain
placeholders and uncredited.

Predecessor consumer 53dc829743f80a44e13f106907ae16c35b7f912f and tools
270010858c73aebeda411d70c12d69981ce70b5f. Bank tools first at
ad559bc41fa547b59e20c3ca38d4da9210105c76, then both sources, consumer
pin and measured documentation. Preserve the older mirror's 1,726 inherited
dirty paths plus two new tools files. No push. The root README changes
only its two aggregate matching rows; detailed recovery updates stay here.

Refresh eleven changed C/Markdown/tool sources structurally, accounting
for every prior node and relationship/context. Retire only source-proven
obsolete s32-return contexts for the recovered pointer functions; validate
new Gfx-pointer contexts and the real rectangle call against source and
relocation evidence. Outside freshness and communities remain historical;
no full-corpus extraction or global clustering/centrality claim. Graph
receipts and the independent final audit live under
conker/build/game-screen-overlay-match/.

Next inspect func_15149C58 in generated_176A00 with a new frozen predecessor
and caller/ABI audit. Keep func_1514E920 private and uncredited. The 75% goal
remains active.
