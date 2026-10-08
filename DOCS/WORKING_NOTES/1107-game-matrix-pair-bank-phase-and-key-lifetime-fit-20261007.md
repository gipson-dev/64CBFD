# Game Matrix-Pair Bank Phase And Key-Lifetime Fit

Date: 2026-10-07

## Scope And Baseline

Continue `func_15031070` from semantic-recovery commit `5f66ffe2` and
[Note 1106](1106-game-matrix-pair-resolver-semantic-recovery-20261007.md).
Retail remains **85 words / frame `0x20`**, VA `15031070..150311C4`,
ROM `5E520..5E674`. The installed baseline was complete recursive C84,
one trailing retail-layout padding nop and **44 raw word differences**.

This follow-up installs one expression change in the
[production owner](../../conker/src/game/generated_5D2C0.c):

```c
*secondary = node[2] + *(Mtx **)(actor + 0x1D4);
```

Both pointer-addition forms calculate the same matrix address. Placing the
slot integer first recovers retail's node-bank temporary bindings directly:
T9 actor home, T2 node slot, T0 actor bank and T1 shifted slot. The complete
five-word sequence at body indices `37..41` now emits as retail without guards.
Only indices **37, 38, 39, 40** differ from the previous linked body; each of
these four new words equals its original retail word. The final ADDU word was
already numerically equal; its operand meanings now agree with retail too.

The result is **C84 / frame `0x20` / 40 full-slot differences**, still not
byte-exact. No inserted/omitted instruction, guarded register cycle, compiler
profile, production struct, shared-header or conversion-ledger change. The
function's original saved-register/home/output behavior remains qualified.
The root README aggregate tables stay unchanged.

## Key And Source-Lifetime Evidence

The [key-fit driver](https://github.com/gipson-dev/64CBFD-Tools/blob/master/experiments/game_matrix_pair_resolver_key_candidates.py)
retains **86 additional measured forms**, none raw exact:

- 24 signed/unsigned key-parent-child-result carriers, common/early returns
  and register declarations. Sharing key and parent/result storage usually
  forces another saved register and frame `0x28`, rather than retail's V0 phase.
- Twelve attachment/parent/node pointer carriers, eight typed-node views and
  twenty early/goto/comma/logical/switch return shapes. Common-return switches
  remain C83; logical/comma forms add real instructions or alter the frame.
- Twelve incoming-actor capture and parent condition/inner-scope forms.
  Capturing actor earlier and moving the parent declaration do not recover
  the key move; their raw bodies remain C84.
- Six matrix/byte/address bank-addition forms. Integer-first pointer, byte and
  address forms close the bank cycle. The ordinary SDK matrix-pointer form
  is the smallest production edit and retains valid native pointer arithmetic.
- Four lookup declarations: signed/unsigned/halfword key prototypes and a
  pointer return. They do not fix the key's register assignment. The isolated
  compiler helper accepts an optional lookup declaration, preserving its
  original default and all previous source/profile measurements.

Together with Note 1106, **155 forms** are retained. All 86 new controls pass
**2,752 ordinary executions**, comparing full returns, public memory and calls
across all eight fixtures, both pages and both SP phases. This does not qualify
alias/home/fault/private contracts for every control.

The experimental typed-node local view with a cached key emits exactly the
same 84-word body as the smaller production pointer-addition change. Its
32-bit offsets/size are checked independently; no view is added to production
or confused with the existing shared `struct126` declaration.

An initial node-as-key control could overwrite the node formal before its
default slot read. These controls now keep the original node for both slot
and post-child offset reads; the incorrect version was neither installed nor
counted as passing qualification.

The remaining key issue is unchanged and explicit: C emits `LHU A1,+1E(S1)`;
retail emits `LHU V0,+1E(S1)` followed by the key-to-A1 move. The C body is
one meaningful word short, not a complete C85 body with one scheduling issue.
The successful recursive update also has different return/store scheduling.
Do not insert a key move, promote a padding nop or normalize branch/read order
with a bulk forty-word guard list.

Six further isolated incoming-actor/node signed-word, unsigned-word and void-
pointer probes all remain C84/frame `0x20`/40 differences. They are ignored
exploratory artifacts, not additional ordinarily qualified forms; changing
the argument declaration alone does not recover the missing word. Production
keeps its original four-word pointer ABI.

## Maintained Qualification

[Eleven key-fit tests](https://github.com/gipson-dev/64CBFD-Tools/blob/master/tests/test_game_matrix_pair_resolver_key_fit.py)
reuse the independent reference and established resolver/caller/owner gates:

- **640 ordinary cases** and all four routes/failure returns, four slots through
  255, five offsets through 65535, two SP phases and a four-parent chain.
  The only unvisited words remain the pinned unreachable branch-likely duplicates.
- **2,592 output aliases**, comparing ordered public reads/writes, full returns
  and public memory, including node/actor/page fields and shared outputs.
- **32 actual lookup connections / 96 incoming-home mutations**; caller-saved
  GP words are clobbered by validating hooks. Full lookup coverage is not claimed.
- Three lazy routes, twelve required-read faults with partial effects, three
  null-output store faults and six guest-only wrapping actor-bank cases.
- **2,304 native 32-bit cases plus three lazy gates**, actual complete selected
  C, valid matrix objects and four output aliases. The unused diagnostic node
  type's size `0x4C` and offsets `2/1E/20/34/48` are also checked; it is not
  a new production type or a native proof of guest home/private behavior.
- **648 complete caller cases / 2,592 executions**, including 72 recursive
  fixtures: C/retail matrix wrapper and C/retail resolver, actual original
  lookup/converter/point/list/translation instructions, public traces and actual
  private argument addresses. Full helper and full stack equivalence remain open.
- Copied owner: **40 functions / 39 unchanged neighbors**, zero warnings,
  identical pools/neighbor bytes/relocations; selected target equals isolated C.
- Actual generated-slice padder: all six relocations including symbolic self-call,
  independently rebased page/lookup/function symbols, 336-byte meaningful body
  and 340-byte retail slot, one tail padding word, no target guards.

All **eleven pre-install tests pass in 81.271 seconds**, zero skips/errors/failures.
The original recovery tests keep their earlier C84/44 experimental reference
and now explicitly recognize either qualified installed source variant; their
native/owner helpers accept a candidate without changing the default. They do
not silently rename the prior reference as the new production body.

All **51 combined key-fit/resolver/branch/layout/prior tests pass in 577.143
seconds**, zero skips/errors/failures. Tools, Python syntax, module CLI help
and scoped whitespace checks pass. The documentation checker verifies
**89 documents / 4,025 relative links / zero broken links**. These are bounded
guest/native/source-fit qualifications, not hardware or PC-port acceptance.

```sh
make -C conker -j4 build/conker.us.elf
python3 -m unittest tools.tests.test_game_matrix_pair_resolver_key_fit tools.tests.test_game_matrix_pair_resolver_recovery tools.tests.test_game_matrix_route_branch_recovery tools.tests.test_game_matrix_route_layout_recovery tools.tests.test_game_matrix_route_recovery -v
make tools-check
```

## Linked Audit And Next Work

The completed US ELF audit compares against Note 1106's authoritative ignored
`conker/build/game-matrix-pair-resolver-test/after.json`. Only `func_15031070`
changes across **6,058 symbols / 6,042 retail slots**. The target changes only
the four now-exact bank words. All **6,041 other slot bodies/addresses/extents**,
sixteen overflows, protected sections, **720 exact Game-data owners / 189,088
bytes**, **11,063 guard rows**, all target relocations and conversion hash remain
unchanged. The build passes with the same pre-existing duplicate Makefile
recipe warning for `generated_12D630`.

New authoritative ignored checkpoint:
`conker/build/game-matrix-pair-key-test/after.json`, with `audit.py` / `audit.json`.
Matching stays **3,364/5,466 total (61.54%)**, **2,691/4,793 Game (56.14%)**,
**2,102 different**, zero drift; Init 492/492 and Debugger 181/181 exact.
This is four directly recovered retail words, not another byte-exact function.

Next source work must recover the key's V0-to-A1 lifetime in a genuine 85-word
body, retaining the now-exact bank phase. Only then consider the independent
recursive return/store schedule. Wrapper key/primary-read, basis layout,
translator scheduling and sampler lifetime remain separately open. No sibling,
frozen Release, save, runtime/hardware or push action.
