# Route Record Copy Direct C Conversion

Date: 2026-10-18. **Installed direct C match: all 40 words / 160 bytes exact.**

Convert `func_150885EC`, generated_B3020, VA `150885EC..1508868C`, ROM
`B5A9C..B5B3C`, after [Note 1578](1578-route-event-dispatcher-direct-c-conversion-20261018.md).
Consumer predecessor `2e81ff01`; tools predecessor `7bc7dfc`. Bank tools
**5d8bc93** first, then the consumer source/docs/pin. No push.

## Complete Source And Interface

Recover `void func_150885EC(s32 sourceIndex, s32 destinationIndex)`. If the
record table exists, save the destination's signed ID/state bytes as full-word
locals, copy all 0x84 bytes from source to destination, then restore ID followed
by state through fresh global-table reads. Keep both indices full-width and
their offset products unsigned/modular. Keep the address name, descriptive
locals and one concise purpose comment. Original assembly remains a reference.

The real caller at 150D78F4 passes the source in its JAL delay slot and does not
consume the copy result; subsequent instructions load a separate pointer into
V0. The recovered void interface is consistent with this observed usage and
the routine's lack of a defined return assignment. Do not invent original
source-name/type authenticity beyond the recovered ABI.

The initial named-offset form emits 39 words/frame48/32 differences. A pointer
destination expression restores the missing address operation but still has
frame48/13 differences. Repeating the unsigned destination-index expression,
instead of declaring its byte offset as a local, lets IDO retain its common
computed value in the original SP+0x18 spill. The final C emits all 40 words,
frame0x28, ID/state homes SP+0x24/+0x20 and full-word argument homes directly.
No padding, register bindings, volatile, new guards or compiler flags.

Raw unlinked code SHA:
`d5b9d7ec9aa6cbdf24aac2677200bb55a1913a7a9560b10e0d9bb29b93bced8e`.
All five bindings and isolated/full/no-unroll/normal-profile output agree.

## Fresh Qualification

All **ten strengthened pre-install tests pass in 17.254 seconds**; all
**ten post-install tests pass in 22.092 seconds**, no skips. The earlier
18.649-second run precedes the poisoned-copy-return caller profiles. Do not
sum overlapping guest/native corpora as independent cases.

- Run 448 target inputs in both stack phases. Cover all 256 ID bytes and all
  256 state bytes, four alignments, same/different records, partial overlaps
  constructed by unsigned modular indices, null tables and full-width index
  extremes. There are 228 normal/SDK profiles and 220 bounded redirected-table
  profiles; the normal count includes null cases that never call SDK code.
  Compare independent reference public memory/calls, plus complete modeled
  GP/FP/LO registers, RAM and ordered accesses between retail and source. All
  40 target words are visited; normal nonnull target paths read the table three
  times, null paths once.
- Connect all 193 real SDK bcopy words, independently equal to frozen ELF and
  ROM, using the existing SDK instruction oracle. Separately compare 144 SDK
  alignment/overlap cases with snapshot/memmove semantics. Helper ADD overflow
  remains outside the valid mapped domain; hardware exception behavior is not
  inferred from the software oracle.
- Run the same 448 inputs in freestanding native32 O0, O2 and O2+UBSan, with a
  bounded 132-byte snapshot-copy provider. Compare every byte in two 1,024-byte
  banks, using 52,838 independently generated expected-byte patches; also check
  exact call operands/count and the current-table result. An ordinary wrong-ID
  native control exits 21. This is not a native compilation of handwritten SDK
  assembly, and the special guest pointer/private aliases are not native cases.
- Pass 988 fired connected-access fault pairs across ten profiles and both
  stack phases. Include actual SDK accesses on real-helper profiles; exclude
  observer/provider internal reads from fault counting. Preserve literal
  register, memory and event comparisons; no fault is manufactured by a probe.
- Exercise provider table redirection, incoming-home mutation and an ID restore
  that changes the table pointer before the state restore. Also execute a real
  SDK destination that overwrites the global table pointer during bcopy. These
  are explicit mapped guest witnesses, not unknown-alias or gameplay acceptance.
- Five ordinary executed source negatives fail public comparisons: reversed
  copy, short copy, wrong saved ID, pre-copy cached table, and one post-copy
  cached table reused across both restores. All runs complete; crashes/timeouts
  are not counted as semantic controls.
- Sixteen actual four-word caller windows cover both phases and real SDK versus
  a poisoned copy return with volatile-register clobbers. A clearly synthetic
  stop trampoline bounds the window; the complete caller is not executed.
- Independent original assembly has identical raw words/five bindings. Three
  GNU maps exercise table/call addresses and HI/LO carries. Pass 32 paired
  code-rebased executions; changed-data-map execution is not claimed.

The first fixture omitted the reused runner's tail flag; set it explicitly.
The initial native wrong-ID control left an unused local under -Werror; use
an effective XOR control without suppressing diagnostics. No production fix
or shared oracle modification was needed. No debugger/capture/Claude call.

## Production And Progress

Both owner profiles preserve all 72 neighbors and pools. The actual mixed
padder preserves all 73 owner functions, the normal-profile projection and the
one remaining GLOBAL_ASM routine. The original first private ELF is literally
unchanged, including metadata. The real Make build and installed audit reproduce
the same image: all 6,057 bodies/addresses fixed, all 189,088 protected Game-data
bytes / 720 owners exact. All frozen inputs except the declared owner-source
change remain fixed, including SDK assembly, guards and Makefile. The existing
duplicate generated_12D630 recipe warnings remain; not a warning-free build.

Whole-ELF SHA remains
`44ecb171bef3c1e2c5f3afb2345953cf70d15224a51db37a1d4fc62c60105e0c`.
Owner-source SHA becomes
`30e5e821869754c8aa1e6d734cd85c842cadb9e22576de1ed79db559820a20dd`.

This adds one C function / 160 bytes from already-exact assembly. Executable
bytes and the different-C count do not change. Fresh matching: total
**3668/5504 (66.64%)**, Game **2995/4831 (62.00%)**, Init **492/492**,
Debugger **181/181**, **1,836 different / zero drift**. Conversion: total
**5504/6044 (91.07%), 86.07% bytes**; Game **4831/5323 (90.76%), 85.43% bytes**.
Exclude repeated CSV header rows when aggregating. README gets aggregate rows only.

Both tools copies pass three setup tests and their smoke check; consumer
`make tools-check` passes. Three new files are identical ASCII and AST-valid.
Preserve all 1,304 prior mirror hashes and its ddbdd16 HEAD; add only these three
files, leaving 1,307 dirty paths, without a mirror commit/reset. Post-commit graph
preservation is a separate final gate in the ignored `graph-audit.json`.

```sh
python3 -m unittest tools.tests.test_game_route_record_copy_match -v
python3 -m tools.experiments.game_route_record_copy_integration --audit
make -C conker match-progress NON_MATCHING=1
make tools-check
```

This routine is finished. Next audit retained `func_1508868C`, VA
`1508868C..15088780`, ROM `B5B3C..B5C30`, **61 words/frame0x28**. Its actual
end precedes the smaller C helpers; do not use the later 150888A8 address as its
extent. It reserves a free route slot for an actor, calls func_15088824, reloads
the table and sets state/actor ID. Qualify signed counts/base indices, mask
exhaustion, helper/table mutation and the full-width actor interface before
conversion. Broader Game work stays active; no host/Release or gameplay claim.
