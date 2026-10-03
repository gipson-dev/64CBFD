# Init Connected Semantic C Candidate And Differential Oracles

Date: 2026-10-03. Baseline: `7536125`.

## Result

The retained decompressor now has an isolated connected semantic C candidate
at `tools/experiments/init_decompressor_semantic.c`. It implements table
construction, fixed-table initialization, stored/compressed/dynamic blocks,
block iteration/cursor rewind, and enclosing header/limit setup. Nine host
differential tests compare it against the retained instruction-word oracles
from [Note 796](796-init-dynamic-multiblock-and-core-entry-oracles-20261003.md).

This is experimental C recovery, not production ownership or a matching
conversion. The file is not linked into `conker`, and no production source,
assembly, compiler profile, word guard, or README aggregate is changed.
Init stays at 492 C / 47 assembly rows with the exact baseline retained.

## Explicit State And Interface

The candidate replaces live-register dependencies with explicit cursor,
reservoir/available bits, output pointer/produced count/signed limit, workspace,
allocation index, and counter/table/sort/offset/length scratch arrays.
Table records contain operation/bit bytes and a halfword value. The host uses
native halfword storage; tests serialize entries big-endian before comparing
retail bytes. This is not a host renderer/RDRAM endian integration claim.

The core test entry takes nominal guest input/output/workspace addresses
separately from the host pointers to preserve the recovered signed overlap
arithmetic. That test interface is not the original guest ABI. Header bytes
are read without an unaligned native-word dereference. No helper substitutes
zlib for the retail algorithm; zlib remains an independent valid-output oracle.

The builder preserves allocation order, header links, replicated entries,
root-width clamping, incomplete-table status, and the narrow-root increment
behavior from Note 794. Scratch arrays are retained in the state rather than
silently clearing sorted/unused cells on each helper call. Tested initial
scratch/workspace bytes are seeded 0xA5 in both fixtures.

## Preserved Exceptional Behavior

- Stored/match output counts must remain strictly below the signed limit.
- Literal output lacks that match-limit check.
- Compressed output count is published only at end marker; failure can leave
  written bytes without publishing the intermediate count.
- The fixed wrapper ignores decoder status; incomplete fixed distance tables
  are retained rather than treated as unusable.
- Malformed stored complements preserve the branch-delay reservoir shift
  without decrementing the bit count on that failure path.
- Dynamic repeat-before-first-length uses the initialized previous value zero.
- The guarded synthetic history-underflow fixture retains its pre-output read.
- Prior stored output remains present when a later dynamic error makes the
  outer entry return zero.

These are candidate/model comparisons on explicit fixture memory, not proof
of arbitrary malformed-input safety or retail gameplay defects. The candidate
does not add a new defensive error policy to claim equivalence.

## Differential Coverage

`tools/tests/test_init_decompressor_semantic.py` compiles the candidate with
host `cc -O2 -std=c99 -shared -fPIC -fwrapv -Wall -Wextra -Werror` into a
temporary library. The ctypes state is test scaffolding, not a production API.

The nine tests establish:

1. All written fixed-table bytes and allocation index 658 match the assembly
   model, including roots one and 626.
2. Small/empty/incomplete trees, allocation append, and narrow-root layout
   match actual builder output bytes/status/root widths.
3. Stored and fixed whole streams, all literal bytes, and a 258-byte overlapping
   match agree with the model and zlib.
4. Dynamic repeat fixtures and two zlib-generated dynamic streams agree.
5. Reserved/error/repeat-first streams preserve partial-output/count states.
6. Stored/match strict-limit cases at limits zero through five agree.
7. Both header skips, all four alignments, guest-address limit choices, and
   core error return agree.
8. Mixed block sequencing and failure after prior output agree.
9. All length/distance extra-bit classes through distance 32,768 and the
   explicitly guarded pre-output read agree.

Whole-stream comparisons include status, produced count, final reservoir and
available bits, cursor offset, allocation state, every written dynamic-table
byte, and the complete bounded output/guard buffer. They do not merely compare
the visible prefix. For core state comparisons, the assembly fixture captures
registers at `0x100062F0` before its epilogue restores s7/gp/fp; comparing the
candidate's explicit decoder state against restored caller registers would
be the wrong contract. Saved-register restoration itself remains tested in
the original entry oracle.

## Verification And Remaining Gates

All nine candidate tests, all 67 focused Init tests, and all 522 tool tests
pass (full suite: 128.513 seconds). The final
candidate rerun also passes complete output-buffer/dynamic-table assertions.
Project tool checks and `git diff --check` pass. No guest compile/link or runtime execution is
claimed for this candidate; host warning-clean compilation is not a retail
compiler match.

Before production adoption:

- Qualify invalid lengths/oversubscription, capacity exhaustion, aliased or
  untouched scratch, and indirect/external calls. Candidate array bounds and
  supplied readable memory are preconditions, not enforced guarantees.
- Resolve exception/FPR context and how to expose the original external ABI
  while internal shared entries still have their retained callers.
- Perform a bounded guest compiler/layout trial and explicitly determine
  whether a complete matching ownership transition is possible. Do not use
  broad instruction replacement guards to manufacture a conversion.
- Require independently exact whole Init code/data sections before replacing
  production owners or increasing conversion totals.

The semantic candidate is now concrete source to investigate, rather than
another unexecuted rewrite proposal. It does not by itself finish Init or the
decomp project. The sibling port and frozen Release remain untouched.
