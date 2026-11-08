# Actor Context Loop Match and Overflow Closure - 2026-11-08

`func_1504ADD0` now matches all **73 words / 292 bytes**, with its original
**0x58-byte frame**. The recovered semantic C uses **44 checked guards** for
closed register allocation, invariant setup and derived branch destinations.
It replaces the existing oversized ECTS-derived body in the retail slot and
removes its obsolete **296-byte overflow copy**.

Total **4,254 / 5,513 (77.16%)**, Game **3,581 / 4,840 (73.99%)**,
Init **492 / 492**, Debugger **181 / 181**, with zero address drift. There
are 1,259 different converted functions and **157** additional exact functions
needed to reach 4,411 / 5,513 and the active 80% goal. Conversion rows and
denominators are unchanged.

## Source, caller and data interface

Owner: `conker/src/game_77AD0.c`. VA 0x1504ADD0..0x1504AEF4;
ROM 0x78280..0x783A4. Its interface remains:

```c
void func_1504ADD0(void)
```

The aligned pristine-image census finds one direct JAL at ROM 0x466C8 /
VA 0x15019218 in `func_15019130`, with no entry/interior pointer literals
and no interior direct entry. The four-word caller window executes the
target JAL/NOP and the following `func_1510F800` JAL with its explicit
delay-slot zero argument. Ninety connected cases poison the target's void
result and qualify that next packet, public effects, saved registers and
SP/RA. The larger parent routine is not fully emulated.

The existing SDK `struct127` is 812 bytes, with signed interaction state at
+0 and unsigned kind byte `id` at +4. The shared actor declaration contains
26 records; retail visits exactly **25**, leaving the spare record untouched.
The current slot global is an unsigned byte, the controller-slot limit is a
signed byte, and current actor/input globals retain their existing types.
The controller-pointer table is loaded through `D_800BE728`'s first word.
The local fallback remains six bytes; it is not assigned a speculative SDK
structure. A local typed declaration documents the one-actor callback.
No shared header or data-owner declaration is changed.

## Recovered behavior

Initialize the slot index to zero. Skip the traversal only when unsigned
`D_800C35EA` equals **one**; other nonzero values still run. For slots 0..24,
look up `D_800CC2D0[slot]` and read its complete interaction-state word.
Inactive actors leave the context globals untouched.

For each active actor, store the current slot byte and actor pointer, then
reload signed `D_8008FD8C`. If the slot is below that limit:

- Slots 0..3 reload the live controller table pointer and select its indexed
  word into `D_800CC284`.
- Slots 4..24 clear all **six** bytes at local SP+48 through `bzero`, then
  store that buffer's address into `D_800CC284`. Repeat the clear for every
  applicable actor, including after a callback dirties the prior buffer.

A slot at or beyond the signed limit leaves the prior input pointer intact.
After input selection, reload the actor's kind byte. Dispatch
`func_150ED578(actor)` only for **0x28** or **0x77**. Advance the index and
812-byte actor cursor on every iteration, including inactive and rejected
kinds. The disable byte is read only at entry; callbacks changing it do not
terminate an in-progress traversal. Limit and table changes remain live.

The original helpers are unchanged. Bounded tests model the six-byte clear
and hostile callback effects; they do not claim full execution of the
callback's complete gameplay implementation. Guest-only aliases test the
ordered global stores, signed-limit read and local fallback. Native tests
use ordinary separate objects and compare the temporary pointer as integer
bits after return, without dereferencing an expired local.

## Derived compiler schedule

The indexed actor source emits **73 words** and frame **0x58** under the
unchanged retail O2/g3 profile. Raw code uses all nine saved-register roles.
A closed mapping recovers retail's index, actor, selected-input destination,
buffer address, slot byte, limit byte and controller-table lifetimes.

The compiler hoists kind 0x77 and materializes loop bound 25 near the tail.
Retail keeps 25 across the loop and materializes 0x77 before its comparison.
The same two nontrapping constant loads exchange invariant placement and
register roles. Retail also sets up the same SP+48 fallback address before
the loop and moves its argument setup into the first-four test's delay slot.
Two equality/inequality operands commute. Branch destinations follow the
derived block mapping, including skip paths that bypass the hoisted bound
and the moved fallback argument setup. No literal, memory operation, call or
instruction slot is added. All sixteen bindings retain their kind/name
multiset. This is an explicitly guarded match, not a direct compiler match.

Raw relocatable C SHA256:
`bdb126c9d1b4accd1fff0856b4c5918c457dcb67ab1b03a0108915aefcf7f693`.
Retail linked body SHA256:
`82707cca00466c010818305913b3167731b187e65d25863206c47b9fbc978459`.
The complete inherited guard CSV remains an exact byte prefix; 44 rows are
appended. Seventy-three raw-word corruptions, sixteen altered bindings,
44 stale guard words, 44 stale guard relocations and 48 metadata-byte
corruptions are rejected. The memory-operation and opcode counts remain
closed, and executed memory/read traces agree across retail, raw C and
normalized C under all qualified fixtures.

## Complete owner and overflow image proof

The **107 frozen inputs** cover the complete owner, every retained GLOBAL_ASM,
caller/helper sources and assembly, SDK headers, assembler includes and exact
compiler/link inputs. All **57 neighboring raw and padded functions**, owner
pools and full register metadata remain fixed. The actual five-command
production Make recipe reproduces the complete 58-function padded object.
There are zero C diagnostics and no Makefile/profile changes.

The old 74-word C body did not fit the 73-word slot. Its canonical slot was
a jump to `__retail_overflow_func_1504ADD0` at 0x15F00000. The qualified
body fits, so the padder removes that private 0x128-byte implementation.
The independent full-image predictor accounts for every resulting byte,
with **zero exclusions**:

| Remaining private function | Old address | New address |
| --- | --- | --- |
| `func_1505210C` | 0x15F00128 | 0x15F00000 |
| `func_1506EE60` | 0x15F0028C | 0x15F00164 |
| `func_150768DC` | 0x15F002DC | 0x15F001B4 |
| `func_150A7B80` | 0x15F00560 | 0x15F00438 |
| `func_15125490` | 0x15F005E4 | 0x15F004BC |

All five private bodies retain every byte. The only live canonical
trampolines requiring retargeting are `func_1505210C` and `func_150768DC`.
The complete loaded-code J/JAL census proves this closure and the removed
entry's sole trampoline reference; no aligned pointer words into the moved
overflow range are present. Both live tail-jump windows independently
forward identical complete caller state to the derived new entries.

The overflow section shrinks from 0x64C to **0x524**. Its program-header
sizes change by 0x128; the 16-byte-aligned ROM cursors `__romPos` and
`debugger_overflow_ROM_START` move by **0x120**, from 0x25AC30 to 0x25AB10.
One private function symbol disappears. The owner's file symbol remains,
because another private body still belongs to this object. The shared
private/public string suffix is compacted and the public name reinserted
at its derived global-symbol position. Symbol offsets, local-symbol count,
section payload offsets, section headers and ELF header are rebuilt exactly.
The ELF shrinks by **328 bytes** overall.

The disassembly-entry census changes from 6,053 to 6,052 solely through the
deleted private copy. All **6,047 canonical addresses** remain fixed. The
only changed canonical bodies are the recovered target and those two jump
retargets. All 720 protected-data owners / 189,088 bytes remain exact.
Three independent GNU links and nine guest executions qualify global/helper
rebases and signed low-half carries. Eight corruption controls reject code,
trampoline, private-body, symbol, string, program-header and protected-data
changes against the complete prediction.

## Execution and production evidence

Both tools configurations pass six focused checks before and after
installation in four sequential fingerprinted runs. The sibling uses a
scratch overlay for these new modules, with read-only helper fallbacks
recorded explicitly. Its HEAD and 2,434 inherited dirty paths are preserved.
Both configurations pass fresh shared smoke checks. Three unchanged shared
synthetic regressions per configuration are reused under exact helper/test
hashes and are not represented as fresh runs.

- **908 guest cases** cover all 25 slots, all disable/signed-limit bytes,
  whole-word activity, both accepted kinds, rejected/high kind bytes, sticky
  input selection, live table/limit changes, repeated dirty-buffer clears,
  six aliases and both stack phases. All **73 words** execute.
- **725 executed target access-fault cuts** compare complete literal retail
  and normalized states. Raw C has identical memory effects and ordered
  reads; its register/fault schedule is not claimed literal. Helper fault
  behavior is outside this bounded target model.
- **90 connected caller cases** qualify the original target call and the
  following explicit zero argument independently of the poisoned void result.
- **644 native cases per executable** pass O0/O2/O3 with trapping UBSan,
  32-bit pointers and SDK size/offset assertions. Complete context/input
  packets, state/kind updates and untouched actor canaries are checked.
  Fifteen effective controls reject a stub, wrong gate, ignored inactive
  actors, unsigned limit, wrong first-four cutoff/table index, missing actor
  or slot update, wrong actor, 26-slot loop, both wrong kinds, byte-sized
  activity and cached limit/table values. Stack aliases remain guest-only.

The production build compiles exactly one C owner and reproduces the full
predicted ELF, including overflow and metadata closure. Compilation/link and
the fresh recount pass. `make all` retains the expected checksum exit 2 while
other functions remain unmatched. `progress.csv` and compiler profile remain
unchanged. README edits contain aggregate table rows only.

Production ELF: `c750ef3ced2079ca65c441ef9078decdb8ed3fc74678cf658e25ba75b45ee19f`.
Binary: `5b40099d2fe2946913c2e45a83a693f2c68b353446c4066cf5d2754f9991b883`.
Owner: `e8e7c93cc5fac1b0938e24573adf22cc8240207f49c3a0ceb9e3a938efe10664`.
Guard CSV: `8afb07a0bd5847fd90c6786e7f9e6d074d0f93a794f8bed58d61e702a12489cd`.

## Resume boundary

Next ordinary C candidate: `func_1509F354`, a 74-word routine in
`generated_CBDB0.c`, pending original caller/data qualification and all
adoption gates. It remains uncredited. Smaller handwritten/nonstandard
register routines remain separate work without false C-match credit.

Scratch receipts: `conker/build/game-actor-context-1504ADD0-match/`.
Tools are committed before the consumer pin. The scoped Graphify refresh
retains unscanned existing nodes and audits changed-path relocations; it is
not a full-corpus extraction. Frozen host Release artifacts are untouched.
