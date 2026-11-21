# Note 2614: Timed effect updater direct byte match

Date: 2026-11-21. Consumer baseline `7b966970a657a4c99e2b6b746a2b69a0ec2a1ed4`; tools baseline
`f164dce9a4221afc98d78721dc91102262f60145`. Qualified tools commit: `a5c018c375652dffa1e0300de2df8ecd4180ef80`.

`func_15188B74` now replaces its zero-return placeholder with the complete
selected-list timer, fade, callback and unlink/free routine. All **99 words /
396 bytes** emit directly from semantic C, including the **0x38-byte frame**,
S0..S7/RA saves and nine code/data relocation sites. There are **zero guards,
insertions or omissions**. All **14 owner neighbors**, pools and compiler
diagnostics remain unchanged. No shared header or compiler profile changes.

Production recount: **4,597 / 5,528 (83.16%)** total, **3,924 / 4,855 (80.82%)**
Game, zero address drift and **931** still different. Init 492/492 and
Debugger 181/181 remain exact. **102 more** matches reach 85% at this denominator.
The placeholder already counted as C: conversion rows are unchanged. Root
README changes only its Total and Game byte-exact aggregate rows.

## Recovered behavior and source

Owner `generated_1B5CC0`, source `conker/src/game/generated_1B5CC0.c`, VA
`0x15188B74..0x15188D00`, ROM `0x1B6024..0x1B61B0`. Original assembly remains
in `conker/asm/1B5CC0.s:268`. The interface is `void func_15188B74(s32 list)`;
both retained calls pass list 0 or 1 and ignore the return value.

The routine snapshots each next link before calling its update callback.
A nonzero signed 16-bit timer subtracts the current frame ticks, truncates
back to 16 bits and then clamps negative results to zero. The update callback
can change timer, selector, opacity, next, heads or ticks; the code reloads
timer/opacity afterward while retaining the original next pointer.

Timed nodes fade in by ticks * 16, capped at 255, and become the predecessor.
Expired nodes with nonzero opacity fade out by ticks * 8, clamped at zero;
when that reaches zero the routine unlinks the node, reloads its selector,
calls the cleanup table and frees it. A node already expired and invisible
is skipped without becoming the predecessor. That retail behavior is kept,
including its effect when a later node is removed; no list repair is added.

Byte 3 is consequently named `opacity` instead of `recordSize` in the local
node view and its two constructors. The constructors and every other owner
routine still emit identical code. No public shared structure is changed.

The initial 100-word source repeated the opacity load. Capturing the value in
its working signed local restores 99 words / frame 56. A compound fade-in `+=`
then recovers retail's commutative ADDU operand order directly. Raw SHA256:
`94ccb4d20c38289e27e914c97002d3592f8a3e726841e002a0c5ec95fd3af812`.

## Qualification and measured limits

- Literal original, raw C and production-padded bodies and bindings agree.
  All 15 owner function definitions retain their addresses/extents, except
  target symbol size 12 -> 396. Both compilation diagnostics and pools agree.
- The natural unchanged O2/g3 Make recipe uses three commands. Its padded
  object agrees with the independently prepared object. Full-image prediction
  matches the actual production ELF exactly: **274 changed bytes**, zero
  exclusions or metadata permutations, across 6,051 linked slots. Game data
  remains 189,088 bytes / 720 owners exact. ELF SHA256:
  `de26692ab0bd367893da7fd0f26a44ec1d86270d3bc1275845064c7ab3e6cdca`.
- Guest execution passes 3,750 cases in each of three streams, all 97 statically
  reachable words (unreachable duplicate words 72/84), 157 access-fault prefixes
  and three effective instruction controls. Complete memory/private stack,
  saved registers, calls and ordered target accesses agree. Guest ticks include
  extreme 32-bit values and both stack phases.
- SDK32 native C passes 2,758 cases each at O0/O2/O3 with strict aliasing and UBSan.
  Node extent 20 and all used offsets are asserted. Seven defined source
  controls detect wrong fade rates, late next snapshot, cleanup dispatch,
  omitted timer clamp, wrong invisible-node predecessor and cached selector.
  The native typed adjacent-head fixture uses ticks [-32, 32] for defined signed
  arithmetic. It is not a portable-C claim for arbitrary 32-bit overflow.
- Both original call windows in `func_15019130`, at 150192CC and 1501931C, pass
  1,102 cases per stream each, including real delay-slot arguments 0/1. Both
  windows equal their current linked bytes. Skipped-call and wrong-delay-list
  controls are effective for each window. The entire caller is not executed.
- Six independent GNU links at two code/data bases agree with the separate
  binding calculation. R_MIPS_26/HI16/LO16 and signed-low carry are exercised.
- The two-entry update/cleanup tables are verified from the linked data.
  Update 0, both cleanup routines and free equal original code; update 1
  `func_15188F84` remains unmatched. Guest/native qualification uses explicit
  effectful callback/free contracts with caller clobbers, not full callback
  execution. No hardware or gameplay acceptance is inferred.
- Five focused checks pass freshly in each primary/sibling configuration
  before and after installation; shared `make tools-check` passes. The actual
  dirty sibling checkout and all 352 dependency hashes are preserved. The
  overlay is isolated, with its import/data fingerprints compared explicitly.

The available 64CBFDOGL scene configuration consumes code words and symbols;
it does not import this C source. Its saved scene input has no identical
function window/prologue and its configured symbols file is absent, so host
mapping/runtime acceptance is unknown. No host source/build/Release changes.

The earlier sequence query `func_15022024` stays private and uncredited.
Its corrected pointer/count/layout screens still miss the 91-word / frame 16
retail shape. The sentinel is -9999.0f; literal controls add a pool and are
not accepted. The camera transition return audit in Note2613 remains a
separate zero-credit result; its incomplete source is not adopted.

Next inspect the unmatched update callback `func_15188F84` in this same owner,
starting from a fresh immutable bank and its actual caller/fields. The wider
85% goal remains active. No push, ROM/save edits, model calls or host changes.

Graph maintenance: the native update exited 1 after refusing a
smaller graph; all 69,858 old IDs were retained. The subsequent
serial scoped extraction covers 6 changed C/Python files with no
missing AST sources, producing 69,896 nodes / 158,721 links while
preserving old IDs and qualification metadata. This is a scoped refresh, not
a full-corpus re-extraction. Commit-hook producers must be terminal and their
retention audit must pass before the final immutable bank is accepted.
