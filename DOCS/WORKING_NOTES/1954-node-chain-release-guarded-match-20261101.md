# Snapshot child-chain release matched from guarded C

`func_151D3130`, owner `game_1FFF60`, now matches its complete **49-word** retail
body. The semantic C replaces an existing zero-return stub. Forty-six words
emit directly; three checked guards close the loop backedge schedule. There
are no inserted or omitted words and no compiler/profile change.

Fresh Native actual-ELF recount: **4,024/5,507 (73.07%)** total,
Game **3,351/4,834 (69.32%)**, Init492/492, Debugger181/181, zero drift,
1,483 different. C inventory stays5,507. The threshold is4,131: **107 more**
are required for75%. The separate identity screen in
[Note1953](1953-identity-change-dispatch-private-codegen-screen-20261101.md)
remains uncredited.

## Recovered interface and lifetime

Source `conker/src/game_1FFF60.c`; VA151D3130..151D31F4,
ROM2005E0..2006A4, 196bytes/frame48. S0..S4 andRA lifetimes match retail.
The function is `void func_151D3130(void *ownerData)`; private typed views
retain the owner's list reference+10, subtype byte+1D and child head+24.
Children have a signed callback index+2A, owner link+2C, payload+34 and next+40.
The padding at+30 is explicit. No shared headers are changed.

1. Read the optional callback from D8008FC5C[owner subtype] and call it with
   the owner. Reload the child head after that callback; it may have changed.
2. Capture each child's next link before invoking any child callback. Index-1
   skips the callback; other signed values index D8008FC48. Pass the child and
   its inline payload+34. The original five callback entries are contiguous
   although the original data assembly gives each entry its own label.
3. Clear the child's owner link before calling func1516972C, then advance using
   the captured next link. Changes to that live link inside either provider
   must not alter this traversal.
4. Reload owner+10 at the end and call the actual
   `func_1514EDF0(s32 key,u8 *listOwner)` interface with the owner's pointer bits
   as key. This removes the owner key from the referenced object's list; it is
   not a resource-free API. Its existing recovered C body was inspected.

Both original wrapper callers pass owner pointers and ignore the void result.
Correcting the local forward declaration removes exactly their two illegal
pointer/integer argument warnings. Twelve other inherited warnings remain
unchanged (14 before,12 after). Helper declarations and callback types are
local to this source. No synthetic argument or volatile access is introduced.

## Closed loop schedule

Raw SHA:
`efef53a5d5a4d70e6b02bc67864654cc00a11b06383a628e9cade99e7646d676`.
The complete C frame/saved-register lifetimes and all six helper/table bindings
match. The boolean loop exit keeps the compiler-generated49-word extent.

| Offset | Compiler | Retail | Effect |
| --- | --- | --- | --- |
| +8C | 0011402B | 02208025 | Move captured next into current before branching |
| +90 | 1500FFF1 | 5620FFF2 | Branch on captured next; target follows the preloaded byte |
| +94 | 02208025 | 8202002A | Preload next child's signed kind in the taken delay slot |

Together these replace the boolean temporary and branch-delay move with the
original branch-likely/preload schedule. No other branch, binding or word is
normalized. The three stale expected-word mutations reject in the actual
padder using the complete owner; raw and binding corruption controls reject.
Guest comparisons separately qualify the original and raw C behavior, rather
than relying only on the normalized bytes.

## Qualification

- Freeze1,022 focused Native inputs and the prior17,557-file complete seal.
- Guest1,120cases/4,480executions across three entry/table/helper layouts:
  original, guarded, actual-Make and rawC programs. All49words execute. Exact
  programs agree in full state and trace; rawC agrees in public memory, calls
  and trace. Includes all256 owner subtype bytes, signed child boundaries,
  empty/single/multiple chains, changed head, callback-table mutation, changed
  next links, owner-link clearing and live final list-owner reload.
- Sixty-six access prefixes/198executions agree across exact programs. These
  qualify emitted guest instruction order, not portable C fault behavior.
- The complete28-word original generic-release helper passes96cases/384exec;
  every helper word executes, covering type0/1, null dispatch and nested callback.
  Its iterator and nested free/dispatch remain bounded providers. The final
  owner-list detachment remains a provider with its actual ABI/semantics audited.
- Both complete11-word original wrappers pass36cases/576exec, four post-target
  return poisons and the two different final owner-release calls. A ROM census
  finds only JALs2006B0/2006DC; no aligned tailJ or literal function pointer.
- Native32 O0/O2/O3 each pass1,536UBSan cases, record canaries and eight effective
  controls: cached head, late next read, skipped kind0 callback, missing owner
  clear, wrong payload, cached list owner, missing owner callback and missing
  detach. A guarded provider bounds a broken late-next control so it terminates
  and fails. Native indices are only-1 or0..4; negative signed boundary accesses
  outside those actual arrays are guest-only.
- All18 raw/padded owner neighbors and pools remain unchanged. The actual owner
  Make rule is three commands (compile,pad,assemble), and its object is identical
  to the qualified object. The complete independent first-link prediction passes.
- All6,056 function addresses remain fixed;6,055 other bodies are unchanged.
  Protected Game data is exact across189,088bytes/720owners. Six public tests in
  each tools copy pass before and after installation, with both shared checks.
- Full production Make, all17,557 prior sealed inputs and a fresh independent
  Native actual-ELF recount pass. Only source, guard CSV, owner object and ELF
  change among old sealed inputs. No unplanned dependent object changes; all C
  inventory CSVs are unchanged.

## Complete ELF metadata prediction

The complete ELF differs from baseline in193bytes. This includes the intended
slot/symbol-size change16->196 plus35bytes of GNUld symbol/string serialization.
The new references swap the adjacent entries `func_150F85A0` and `D_8009E6F0`.
The predictor constructs both new symbol rows and their combined string range
from pinned BEFORE rows, verifies their original adjacency/string geometry,
retains every definition/field and preserves the total string-table size.
No metadata is ignored, no byte-diff exclusions are used, and input objects
are not reordered. The complete literal ELF and named symbol counter must agree.
Metadata and instruction corruption controls fail the same full-image check.

Production ELF SHA:
`4f536ba38e824b7487c0dbe0483303c7770732fc0354053c92e0e378f304133c`.

Retained non-passing receipts: the first scratch node view omitted+30padding
(corrected before selection/qualification); the first integration template
expected a five-command recipe while this owner actually uses three; the first
strict predictor caught the named symbol-pair serialization, which is now
explicitly predicted and tested. Only corrected complete gates are credited.

## Bank and continuation

Evidence: `conker/build/game-node-chain-release-151D3130-match/` contains frozen
inputs, complete source/guard proposals, raw/owner/padded/actual-Make objects,
strict first-link ELF, canonical fingerprints, runtime/census results, both
public suites, production audit and independent Native recount. Finished work
is committed tools first, consumer second; root README keeps aggregate tables.
Private identity/motion/owner-gate/direction work remains uncredited.

Next audit **func_150B6BC0**, owner generated_E4070, source
`conker/src/game/generated_E4070.c`, original `conker/asm/E4070.s`.
Its52-word/frame24 body dispatches on unsigned D800D9890 through the original
10-slot jump table to nine command helpers. Inspect the actual incoming unused
argument, callers and all table bindings before compiling C. No next-target
source was changed or credited. The75%goal stays active. NoClaude, push,
WSLrestart, host/editor orRelease changes.
