# Game Matrix-Pair Resolver Semantic Recovery

Date: 2026-10-07

## Scope And Installed Boundary

Recover `func_15031070`, the separate matrix-pair resolver used by the matrix
wrapper in [Note 1104](1104-game-matrix-route-private-layout-and-semantic-recovery-20261007.md)
and the source audit in [Note 1105](1105-game-matrix-route-register-phases-and-branch-source-audit-20261007.md).
Retail is **85 words / 340 bytes / frame `0x20`**, VA `15031070..150311C4`,
ROM `5E520..5E674`; its reference is [asm/5D2C0.s](../../conker/asm/5D2C0.s).

The [production owner](../../conker/src/game/generated_5D2C0.c) now contains
complete recursive semantic C instead of the padded three-word zero-return
placeholder. SDK `Mtx **` outputs express the original 64-byte matrix stride.
The isolated/owner body emits **84 meaningful words / frame `0x20`**; the real
generated-slice padder adds one trailing zero word before the next function.
That gap is not a recovered 85th C instruction or a byte match.

**44 full-slot word differences remain**, versus 85 in the old placeholder.
No instruction guards, insertions, omissions, compiler-profile, shared-header
or conversion-ledger changes. Keep unchanged O2/g3/MIPS2. The wrapper remains
its independently qualified C120/60-difference recovery, not newly matched.

## Recovered Routes And Readback Order

The four incoming ABI words are node, actor, primary-output address and
secondary-output address. No new null/index/page/recursion policy is introduced.

- Attached node: read node `+48`, require attachment flag byte `+3F6`, select
  primary from attachment `+3E8[page]`, store it, then **reread global page and
  node attachment** before secondary selection from the reloaded `+3E0` bank.
- Node bank: select node `+34 + page*64`, store primary, reload the incoming
  actor home, read node slot byte `+2`, then actor bank `+1D4` for secondary.
- Keyed parent: read unsigned halfword `+1E`; call the original lookup ABI
  `(actor, key, 0)`. A missing parent or failed recursive resolution returns
  zero without a parent offset update. On success, reread this node's unsigned
  halfword `+20` **after child output stores**, advance primary by that many
  matrices, and return the full word one.
- Default actor bank: perform the real **unadjusted primary store first**,
  then read node slot byte `+2`, write adjusted primary and finally secondary.
  Omitting that intermediate store changes outputs when storage aliases node.
- Preserve saved S0/S1, SP and RA. The actor incoming home is entry-SP `+4`;
  secondary is saved/reloaded at entry-SP `+12` around lookup. Lookup can alter
  both homes before the recursive call; do not substitute cached arguments.

Failure routes remain lazy: an inactive attachment does not dereference actor,
page or outputs; lookup/child failure does not add output writes. Guest arithmetic
retains 32-bit address wrap and unclamped slot/offset values. Native tests use
valid allocated matrix objects and do not claim host wrapping-pointer behavior.
The acyclic fixture recursion bound belongs only to the tests.

## Source Fit Still Open

The [candidate driver](../../tools/experiments/game_matrix_pair_resolver_candidates.py)
retains **69 source/profile forms**, none raw exact: 32 register/key/bank/reread
forms, twelve matrix/byte-pointer/lifetime forms, sixteen switch/key/prototype
forms, five structured/label/carrier forms and four compiler profiles.
All 69 pass **1,104 ordinary executions**. This does not qualify alias/home/
fault/private contracts for every form; cached-attachment controls deliberately
lack the required reread behavior.

Selected matrix-pointer C matches the first fifteen opening words and all five
epilogue words directly. Its attachment route retains original read/store order.
It is one meaningful instruction short: the compiler loads the lookup key
directly into A1; retail loads V0 and moves the key into A1. The node-bank
secondary calculation also has a different GP cycle/commutative addition,
and the successful recursive update uses different return/store scheduling.

Switch-based controls can emit C85 but reverse the keyed/default block order.
The boolean-switch C85/24-difference control adds an SLTU and shifts the key
branch; it is not a recovered retail instruction. Do not insert the missing
key move, use an unrelated instruction as filler or normalize branch/read order
with a bulk 44-word guard list. Recover the complete retail source shape first.

## Maintained Qualification

[Eleven resolver tests](../../tools/tests/test_game_matrix_pair_resolver_recovery.py)
compare the complete C-derived MIPS body and original retail instructions:

- **640 ordinary guest cases**, all four routes, all failure returns, four
  slots through 255, five offsets through 65535, two SP phases and a four-parent
  chain. Only pinned unreachable branch-likely duplicate words remain unvisited:
  C indices `17,29,63,70`, retail `17,29,64,71`.
- **2,592 output-alias cases**, comparing ordered public reads/writes, full
  return words and public memory. Destinations include each other, node fields,
  actor bank and the page word; primary-induced rereads are observed directly.
- **32 actual 28-word lookup connections** and **96 incoming actor/secondary
  home mutations**, with bounded lookup hooks clobbering caller-saved GP words.
  Full lookup path coverage is not claimed.
- Three lazy failed routes, twelve required read faults with partial effects,
  three null-output store faults, and six guest-only wrapping actor-bank cases.
  No new gates or clamps.
- **2,304 native 32-bit cases plus three lazy gates**, actual complete recursive
  C, four valid output aliases, three storage patterns and a bounded validating
  native lookup callback. Native execution does not prove guest private homes.
- **648 complete caller cases / 2,592 executions**, including 72 recursive
  fixtures: both installed C and retail matrix wrapper, both C and retail
  resolver, and actual original lookup/converter/point/list/translation bodies.
  Compare full returns, public traces, calls and actual private argument addresses.
- Copied owner: **40 functions / 39 unchanged neighbors**, zero warnings,
  identical neighbor bytes/relocations and normalized pools; target exactly
  equals the isolated object.
- Real **generated-slice** padder preserves all six relocations, including the
  symbolic recursive self-call. Independently rebase page, lookup and function
  entry, including HI16/LO16 carry. Body size stays 336 bytes; the retail slot
  is 340 with one actual padding word, no target guards.
- Four compiled, output-detected negatives: cached attachment, cached page,
  omitted default intermediate store and wrong recursive offset. An unexpected
  fault is not accepted as a semantic negative.

Harness setup corrections precede qualification: ordinary output addresses
originally collided with saved stack storage and were moved out of that region;
the independent reference's unmapped-read exception now matches the ISA oracle.
The native warning, omitted zero-point translation probe and body-versus-slot
padding assertion were also corrected before passing receipts.

The first eleven-test run passes in **81.877 seconds**. All **40 combined
resolver/branch/layout/prior tests pass in 495.848 seconds**, zero skips/errors/
failures. Three installed/padder/previous-connection receipt rechecks pass in
**11.533 seconds**. The prior recovery test now derives its placeholder receipt
from the actual owner rather than retaining a stale hardcoded true value; its
original-helper test still executes the retail reference, not the new C body.
Tools, Python syntax, module CLI help and scoped whitespace checks pass. The
documentation checker verifies **88 documents / 4,016 relative links / zero
broken links**. No full stack-memory equivalence, complete helper path coverage,
hardware FCSR, PC-port rendering or gameplay acceptance is claimed.

```sh
make -C conker -j4 build/conker.us.elf
python3 -m unittest tools.tests.test_game_matrix_pair_resolver_recovery tools.tests.test_game_matrix_route_branch_recovery tools.tests.test_game_matrix_route_layout_recovery tools.tests.test_game_matrix_route_recovery -v
make tools-check
```

## Linked Audit And Next Work

The completed US ELF audit compares against the authoritative Note 1104
`conker/build/game-matrix-route-layout-test/after.json`, not the older wrapper
placeholder snapshot. **Only `func_15031070` changes** across 6,058 symbols /
6,042 retail slots; all 6,041 other slot bodies/addresses/extents, sixteen
overflows, protected sections, 720 exact Game-data owners / 189,088 bytes,
11,063 guard rows and conversion hash are unchanged.

New authoritative ignored checkpoint:
`conker/build/game-matrix-pair-resolver-test/after.json`, with `audit.py` and
`audit.json` in the same directory. The build passes; its pre-existing duplicate
Makefile recipe warning for `generated_12D630` is unchanged.

Matching stays **3,364/5,466 total (61.54%)**, **2,691/4,793 Game (56.14%)**,
**2,102 different**, zero drift; Init 492/492 and Debugger 181/181 exact.
The root README aggregate tables remain unchanged; detailed recovery belongs
in this note and the working docs. This is genuine installed semantic recovery,
not a new conversion count or byte-exact function.

Next: recover the resolver's V0 key lifetime/argument move in a complete
85-word body before considering narrow GP/schedule normalization. Retain the
wrapper's independently qualified register-phase evidence and its open key/
primary-read source fit. Basis, translator and sampler remain separately open.
No sibling, frozen Release, save, runtime/hardware or push action.
