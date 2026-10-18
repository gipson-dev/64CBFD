# Route Projection Native Qualification And Installed Byte Match

Date: 2026-10-18. Consumer predecessor: `bdc4ab06`; tools committed first as
`b61d10a2ddcaa4c2e24e054ed5cd23f3e94de6f9`. Continues
[Note1557](1557-projection-complete-observational-proof-and-isolated-byte-match-20261018.md).

## Installed Result

Replace `func_150891E8`'s zero-return placeholder in `generated_B3020.c` with
complete typed `void func_150891E8(u8 *record, u8 *actor)` C and a concise
semantic comment. Preserve the address-derived symbol; no speculative game
name is introduced. The routine selects the nearer route node, constructs
a clamped projection payload and enqueues commands through the real helper.

Retail VA `150891E8..150896EC`, ROM `B6698..B6B9C`: **321 words /1284 bytes /
frame120, all words byte-exact** after guarded normalization. This is not a
direct335-to321 compiler match or recovered original source text. The raw
semantic body remains Note1556's335-word/frame120 source, retaining the six
opening saved roles and SP+0x48 node spill.

- Raw unlinked SHA-256:
  `3489534941741d693be663d176f5a0317142535fc75abd62513d10721befb305`.
- Normalized unlinked SHA-256:
  `5936953663607ec290a2477db4347861ac88136b1ba4a02f64e0a5e2486b733a`.
- **335 complete expected-word/relocation guards**, including identity guards,
  **14 omissions** and **18 moved bindings**. All335 changed input words and
  all18 removed bindings fail in the actual padder (353 effective controls).
- The recipe retains321 distinct semantic source-instruction origins; the
  normalizer reads no retail bytes/files. Note1557's closed register/schedule,
  redundant-word and payload-base derivation is unchanged.

## Mixed-Profile Production Rule

The owner already disables loop unrolling and retains four GLOBAL_ASM bodies:
`func_1508802C`, `func_150880F8`, `func_150885EC`, `func_1508868C`.
Do not globally switch this owner to normal flags or skip assembly processing.

The qualified Make rule preprocesses once, compiles/postprocesses the original
no-unroll primary, separately compiles/postprocesses a normal-profile object,
and overrides **only func_150891E8** through the existing generated padder.
Filter only `B3020_NO_UNROLL_FLAG` from the override flags. Every other72
primary body/binding and all pools remain fixed. The target is246 words/
frame128 in the unused primary and335/frame120 in the selected override.

Seven actual expanded Make commands pass in a private shadow using only
qualified source/guard path substitutions. Both four-routine assembly passes,
all73 primary functions, normal raw body/bindings and padded code/metadata
equal qualification. Cleanup is skipped only in that shadow to retain receipts.
The real build completes with the normal cleanup rule.

An earlier attempted `-Wo,-loopunroll,1` after the owner's0 did not re-enable
unrolling:246/frame128 persisted. Its rejected object/command receipt remains
ignored; no such override is installed. Removing B3020 from the overlapping
generic assembly groups prevents a new duplicate recipe. The unrelated
pre-existing `generated_12D630` Make warning remains; old unrelated CFE warnings
are not changed or represented as target diagnostics.

## Native32 C Qualification

O0, O2 and O2+UBSan each pass **8225 cases**, compiling the actual complete
parent, selector and enqueue C. Logging wrappers delegate to those real C
helpers. An independent native C reference compares the complete aligned
0x14000-byte arena and call log, not only selected outputs.

Coverage includes all256 banks/all20 valid cursors; signed counts and nulls;
states/modes/preferences; negative coordinates; record/actor/table aliases;
safe queue/actor-pointer overwrite and bank-changing aliases; extended root258;
and selected signed zeros, subnormals, maximum finite values, infinities and
quiet/signaling NaNs. Arithmetic NaN fields compare by class; direct copies
and all other bytes compare exactly. Host-endian aligned memory is explicit.
Guest private-stack, misaligned and unmapped low-pointer aliases are excluded.
No FPU status/trap, hardware or gameplay claim follows from native agreement.

Six compiled O2+UBSan controls fail by ordinary semantic mismatch, with no
diagnostic/runtime crash accepted as success:

| Control | Exit |
| --- | ---: |
| Wrong enqueue command | 23 |
| Wrong preference bit | 23 |
| Unsigned node coordinates | 21 |
| Clamp before normalization | 21 |
| Cache payload coordinates across aliasing stores | 21 |
| Reload instead of retaining entry object | 21 |

## Guest And Caller Boundaries

The installed ELF's321 parent words and both installed helper spans are used
after independently confirming equality with retail. **575 paired guest cases**
match complete memory, GP/FP registers and calls, plus the independent public
reference. Sixteen nonnull cases pass **2148 actually fired access-fault
prefixes**, including **780 helper accesses**. Compare full memory, GP/FP,
calls, PC and delay-slot ownership at every synthetic boundary. Instrumentation
counts each access once; the existing oracle already counts helper accesses.
These are synthetic instruction-access boundaries, not hardware exceptions.

Scanning every Game retail function span finds one direct call site:
`func_15087CC0` at `15087D4C`. Execute its actual67-word caller body connected
to both actual helpers and the installed parent in **40 cases**: states2/3,
signed actor slots0/1/127/-1/-128, flags0/64 and two stack phases.

Record stride is0x84; actor stride is0x32C. The actor base is **0x800CC2D0**,
not800DC2D0: LUI800D plus signed low C2D0 resolves to800CC2D0. At15087D54 the
caller immediately overwrites V0 with LUI, supporting the parent's void
interface. These cases qualify this projection call path, not unknown indirect
callers, the caller's other branches or installation of the caller itself.

## Fresh Tests And Linked Audit

Run from the prepared consumer under WSL:

```sh
python3 -m unittest tools.tests.test_game_route_projection_integration -v
python3 -m tools.experiments.game_route_projection_integration --audit
make -C conker match-progress NON_MATCHING=1
```

Pre-install nine tests pass in49.389s. **Installed nine tests pass in47.972s,
no skips**, with an actual installed linked audit. Strict gates include four
corrupted successor artifacts, four mixed live stages, complete historical
input fingerprints and real padder/Make controls. The installed suite manages
its own historical view; do not nest an outer historical context around it.

Reuse Note1557's unchanged23-test proof receipt explicitly; it was not rerun
this turn. Shared padder/PC16 checks pass eleven per tools copy; both smoke
checks and consumer tools-check pass. No new Claude, debugger or compiler
capture call. New tools pairs are byte-identical and ASCII/AST valid.

The real `make -C conker -j4 build/conker.us.elf progress.csv` succeeds and
reproduces the immutable first linked prediction: **974 changed ELF bytes**,
only target instructions and its12->1284 symbol size. All6057 function
addresses and6056 other bodies remain fixed. Every other ELF byte is identical.
The production owner equals the qualified padded owner. Protected Game data:
**189088 bytes /720 owners /zero differing bytes**. Prior mixed-EOL guard bytes
remain an exact byte prefix; do not normalize the entire CSV.

Successor SHA-256 values:

- ELF: `7eb93e57d28fed26f58b58751c8884b3478f1db71b3fc8b2766022c7d75d27c6`.
- Owner: `2c7d59f471640e516240dfe340ec3344eba574cbd371251b73e248d5804f7ed7`.
- Guards: `07994470d0e3d22e880a7bbd18188badd28eb5fde11ced8ec40bfa3176ff6647`.
- Makefile: `5d18b2170461785d270be99353e9bacdf4717ff2fd5d85231b702132740cb99d`.

Fresh matching: **Game2987/4828 (61.87%)**, **total3660/5501 (66.53%)**,
Init492/492, Debugger181/181, **1841 different /zero drift**. The old stub
already counted as C, so conversion counts remain5501/6044 (91.02% functions,
86.04% bytes), Game4828/5323 (90.70% functions,85.41% bytes). Fresh progress
CSV byte sums are1941784/2256728 total and1770348/2072880 Game. Root README
changes only its two aggregate matching rows; detailed updates stay here.

## Preservation And Resume

Ignored receipts: `conker/build/game-route-projection-integration/`, including
native32, actual shadow Make plan, guard controls, normalized guest/fault and
connected caller receipts, first prediction, immutable before/after files and
the installed audit. Older source points/captures remain unchanged.

Standalone mirror HEADddbdd16 remains fixed; preserve all1248 prior dirty leaf
hashes and add only three previously absent task files (1251 dirty paths).
No mirror commit/reset, push, host-port/frozen Release action or save/config
change. The user confirmed the accidentally overwritten space-truncated
compiler scratch path was disposable; no recovery or deletion is needed.

Scoped Graphify refresh:42648 nodes,82712 links,4005 communities. Retain42635
old IDs; three duplicate UPDATE_LOG headings relocate uniquely with their line
offsets. Preserve19398 nodes from2972 excluded-but-existing files, with no full
purge. Tools remain outside the configured current corpus; no new Python AST
coverage is claimed. Before-graph and scoped-ID audit stay ignored receipts.

Next recover **func_15087CC0 (67 words/frame48)**. Preserve its signed slot,
live record-table and signed-count reloads, no-object skip, state>=2 projection
branch, and both150896EC branches. The latter remains a separate unrecovered
callee. Vector15088F30, parent150896EC and the wider Game queue remain open.
Do not treat this one installed guarded match as completion of the Game goal.
