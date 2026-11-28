# Channel fade and transition updater guarded byte match - 2026-11-27

`func_150617BC` replaces its zero-return placeholder in
`conker/src/game_83300.c` with the complete **108-word / 432-byte** routine.
Body and slot are VA `0x150617BC..0x1506196C`, ROM `0x8EC6C..0x8EE1C`.
The retail **32-byte frame**, S0 at SP+24, RA at SP+28, saved-register
lifetimes, ten external bindings and branch-delay effects are preserved.
The unchanged compiler profile is O2/g3. No shared header or Makefile changes.

Actual production recount: **4,718 / 5,528 (85.35%) total**, and
**4,045 / 4,855 (83.32%) Game**. Init remains 492/492 and Debugger 181/181;
zero address drift, 810 different. This adds one match, with conversion rows
and denominators unchanged. The **90% goal remains active**: **258 more**
matches reach the required 4,976/5,528.

## Interface and behavior

The recovered public interface is `void func_150617BC(struct127 *actor)`.
The complete original 105-word caller `func_150619A8` passes one owner word;
after the child returns, it immediately calls `func_150623F4` and tests that
helper's result. Three child-V0 poisons preserve caller effects and argument
sequences. Historical C return spelling remains unknown; no transitive
whole-program return-liveness claim is made. The actual raw and normalized
machine V0 and complete terminal register states also match retail.

An inactive actor exits before accessing the global slot bound. For an
active actor, `D_80082FA0` is a signed inclusive bound. Negative values skip
the channel loop while still allowing transition processing. The loop uses
a moving byte cursor and a wrapping `u32` mask; actor byte 15 chooses the
direction for each channel byte beginning at offset 11. A selected channel
decreases by 50, saturating at 0. An unselected channel increases by 50,
saturating at 255. A nonzero corresponding byte of `D_800DBFF4` makes that
change instant. Zero decreasing channels and 255 increasing channels skip
both the gate read and store. After each actual store, retail reloads the
global bound; that reload is retained and matters for guest address aliases.

If actor byte 10 is nonzero, byte 7 approaches target byte 8 by step byte 9,
saturating at the target. The target is reloaded after the store. Once the
two values agree, mode 6 calls `func_15060F28(actor, 1)`, mode 5 calls it with 2,
and other modes clear byte 10. The helper runs after all updates; changes it
makes to actor/global state survive. Its body remains a separate unfinished
routine and receives no matching credit here.

Native tests use valid typed actors and the actual four-byte gate union,
with bounds -1..3 plus a dedicated INT_MIN skip. Guest-only count/gate aliases
do not imply a broader portable C object contract. In the count-high-byte
alias, the instant gate makes the stored high byte negative and ends the
loop. A non-instant positive high byte would grow the loop beyond that
mapped fixture; that case is not presented as a valid native object.

## Closed clamp control flow and complete owner

The semantic C emits all 108 words. **97 bound words already match**;
**11 expected-word guards** normalize only the two closed clamp branch
graphs. No insertion, omission, artificial padding, frame, floating-point
or value rewrite is used. All ten bindings retain their symbols/positions.

The structural certificate enumerates **130,560 cases**, covering all
decreasing/increasing channel-byte and gate-byte combinations. Every other
incoming GPR is symbolic and the global-bound reload is unconstrained.
Ordered store/load addresses, widths and values agree, and all 32 GPRs agree
at the loop join before its branch. Equal access sequences support memory
alias induction. Four effective controls reject wrong branch, arithmetic,
store byte and saturation. Raw instruction/fault PCs and intermediate full
scratch states may differ; literal raw fault-state parity is not claimed.

Both complete padders reproduce the frozen before object and produce the
same selected object. All **88 other functions**, pools, prior guards and
**18 GLOBAL_ASM bodies** remain fixed. The original owner reference pins
13,648 ROM words across 89 functions and 61 retained ASM files. Eight existing
IDO 712 diagnostics are unchanged; the target adds none.

## Qualification and production evidence

- Native actual C: **522,754 cases each at O0/O2/O3**, with actual SDK layout,
  all channel/gate bytes, all current/target byte pairs, every step byte on
  a boundary grid, all mode/mask bytes, negative bounds and callback-state
  mutations. Separate translation units, strict aliasing, trapping UBSan,
  and LTO interface checks are enabled. All ten negative controls fail with
  logical exit 42; signals or traps do not count as detected controls.
- Guest: **3,740 cases per stream / 14,960 runs** across retail, raw and both
  normalized streams. Complete public memory, ordered accesses, helper
  arguments, all terminal registers and machine V0 agree. Three pointer
  domains and guest-only count/gate aliases are covered. All **106 reachable
  words** execute. Static CFG analysis identifies original words 75/95 as
  unreachable duplicate instructions; both remain in all 108-word bodies.
  Normalized complete states agree at **122 fault triples**. A cached-bound
  alias control is effective.
- Caller: **384 connected runs**,32 cases and three child-result poisons,
  using the complete original 105-word `func_150619A8`. The 25-actor update
  loop and pending four-link loop run;97 parent and 95 child words execute
  in this scope. The separate guest corpus covers the child's106 reachable
  words. The classifier and lookup are explicitly bounded opaque models.
  Two caller controls detect wrong owner argument and a child-V0 consumer.
  No provider, whole-program, gameplay or hardware acceptance is inferred.
- Boundaries: **216 word mutations** (194 visible/22 rejected), **20 binding
  mutations** visible, **22 injected guard bindings** rejected and **22
  guard removals** visible. Both overflow controls reject. Twenty GNU links
  cover four rebases, independent globals, signed HI16/LO16 carries, and
  raw/manual/retail/both-padder routes.
- The actual **five-command Make recipe**, including 18 retained assembly
  bodies, reproduces the qualified owner. An independent frozen-before-C
  plus original-ASM prediction equals the entire private linked ELF:
  **320 changed bytes, zero exclusions**. Actual production Make and live
  recount confirm installation. All 720 data owners/189,088 protected bytes,
  neighbors, addresses, old guards and conversion rows remain unchanged.

The packet runs freshly from the primary tools checkout and an isolated
tools twin before and after installation. The real sibling checkout's HEAD,
dirty work, 353 base dependency hashes and the three additional dependencies
in the 356-entry extended receipt are checked and preserved. The tools commit precedes source installation and the
consumer commit.

| Phase | Elapsed | Tests |
| --- | ---: | ---: |
| pre-primary | 197.8 s | 5 fresh / 0 reused |
| pre-sibling | 187.995 s | 5 fresh / 0 reused |
| installed-primary | 193.965 s | 5 fresh / 0 reused |
| installed-sibling | 192.419 s | 5 fresh / 0 reused |

Paired reports agree across 323 primary / 324 twin imports and 247 tool data inputs. All 11 task files are independently copied; shared `make tools-check` passes. Frozen inputs: 4,296 hashes / 3,861 copies. Claude calls: **0**; no subagents or pushes.

Tools commit: `5a3a190792aaee17de0a591cca7bfcc65ad6568c`.
Production ELF SHA256: `28ba321f722120734f60585ce882dc9dc2505f2de859ebbe374a3c23ae818ac8`.
Complete owner C SHA256: `6d9e2d53e0658951f6178eda626ea6c9a078e310c8bf5a079d8081fe21ce12d4`.
Padded owner SHA256: `a1249bc0069f54b460fecd9dba5e52ac2590af24b4eade2a9b858e21e427efe1`.
Guard manifest SHA256: `a4305db99636344f2617e3887142320cdd27dd3e17393fead5e2661c6e4938f3`.

## Host applicability, graph and continuation

Read-only sibling audit: `64CBFDOGL/recomp_scene/cd64_out/func_150617BC.c`, present True, SHA256 `b54903eaae2dee55315285f26ffe4d0c67a13f597b81cd0e7d50593e4b14ee51`. No host implementation is transferred or qualified, and no host edit, build or launch is made. Release stays frozen.

The scoped Graphify refresh audits all 71 current C definitions and 18 assembly bodies, retains all prior IDs and proof metadata, and observes actual Git hook producers terminal before publication. Full-corpus re-extraction is not claimed. The sealed bank retains inputs, paired import closures, build/image proofs, graph and commit receipts.

Continue with another unmatched Game routine from this checkpoint. Private `func_1514EECC` remains uncredited because its 296-byte frame differs from retail 288. The 90% matching goal remains open.
