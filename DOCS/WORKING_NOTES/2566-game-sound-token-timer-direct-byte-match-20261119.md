# Note 2566: Sound-token timer direct byte match

Date: 2026-11-19. Consumer baseline `a1c0aeae1ecda544c0d6e5c0b2ecf2535fdadabe`,
tools baseline `5cadd5afc6696360c90ea7efbd004204818fb5ae`.
Matching tools are committed as `18fc5e52530ac25f97a52d3dde577c0d4489927d`.

`func_15103AA0` is installed as **directly byte-exact C across all 93 words /
372 bytes / frame 0x30**. There are **zero guards**, no compiler-profile
changes. Actual production Make, complete-image
prediction, installed qualification and fresh recount pass.

Total is **4,560 / 5,514 (82.70%)**, Game **3,887 / 4,841 (80.29%)**,
Init **492 / 492**, Debugger **181 / 181**, with zero address drift and
954 different C functions. **127 additional matches** are needed for 85%.
Conversion stays **5,514 / 6,048 (91.17%)**, **86.19%** of bytes; the
progress CSV is byte-identical to the preceding checkpoint.

## Recovered source and interface

Owner: `conker/src/game_130CB0.c`. VA `0x15103AA0..0x15103C14`, ROM
`0x130F50..0x1310C4`. The fixed interface occupies seven O32 word slots:
the typed state pointer, five unused 32-bit arguments and the pending-token
pointer. The obsolete unprototyped forward declaration is removed.

The routine caches its actor pointer, snapshots all three coordinates as
truncated signed integers into halfwords, and updates the low 15 timer bits
and high 16 token. A new pending token starts command 0x5B0; expiry copies the
cached high token through the output, preserving the observed post-output
packed-word reload. With no timer and no handle it emits 0x5B1 and returns 1.
Other no-timer paths issue the gated handle control, clear bit 0x80 and finish
the packed state update. Remaining paths return 0. Descriptive names are not
claimed as recovered debug identifiers; the two sound parameters remain
explicitly named by their unresolved record offsets.

The pending pointer is not dereferenced on a zero-timer path and may be null
there. Native tests require valid actor coordinates in the signed 32 bit conversion
range and a valid pending pointer whenever the timer is nonzero. Guest-only
word/pointer aliases and wrapped addresses are kept separate from defined
native alias cases.

## Source-derived frame and lifetime recovery

The initial complete C recovery was 94 words / frame 56. Its three named
locals reserve 12 bytes, rounded to 16 by the backend. A misleading 93-word /
frame 48 parameter-reuse candidate drops an original incoming argument-home
store and shifts the timer spill; matching dimensions do not qualify it.

Two fingerprint-locked traces follow newly owned compiler children through
CFE/UOPT/UGEN, capture their actual wire inputs and observe the UGEN frame
field writes. Both drivers/children terminate successfully and their ordinary
text, function maps, relocations and pools remain identical to the traced
objects. The baseline frame sequence is 0/16/40/56 with the locals field 16;
the final source is 0/16/40/48 with locals 8. The decoded M definition shrinks
from 12 to 8 bytes. These are observed internal frame components, not timing
or performance measurements.

The final body uses two named locals. Inlining the packed-word view removes
the redundant named reservation. Copying the expired token from the output
eliminates the extra shift. Declaring the timer local before the actor local
recovers its actual SP+0x2C call-save home. All three original incoming
register-home stores remain intact; the complete 93-word stream, original
frame and saved-register lifetimes emit directly. No volatile fields or
frame-normalizing guards are needed.

## Exact owner, linking and production boundaries

All **four other owner functions remain byte-identical before/after**.
Raw and padded constant pools, diagnostics and the register-mask union pass. The ordinary C padder and an
independent generated padder reproduce all five owner routines. The copied
actual three-command Make recipe reproduces the exact qualified object
under the existing O2/g3 profile.

The independent prediction changes only this function's slot and its symbol
size 12 to 372. There are **264 changed bytes, zero metadata permutations and
zero exclusions** across the entire 3,254,384-byte ELF. All 6,051 function
entries retain their addresses, and only this body changes. Protected data
is exact across **189,088 bytes / 720 owners**. Production Make exits 0 and
the actual object/ELF equal those predictions. All **1886 frozen inputs**
are checked: only the declared source, target object and ELF change. Guard
history, Makefile, original assembly, progress CSV and unrelated objects stay
byte-identical.

## Fresh qualification and limits

Tools: `experiments/game_sound_timer_15103aa0_match.py`, its manifest,
guest/native helpers and `tests/test_game_sound_timer_15103aa0_match.py`.
Run from the prepared consumer root:

```sh
PYTHONPATH=. python3 -m unittest tools.tests.test_game_sound_timer_15103aa0_match -v
make -C conker -j4 build/conker.us.elf progress.csv
python3 tools/match_progress.py conker/progress.csv conker/build/conker.us.elf conker/conker.us.bin --version us
make tools-check
```

- **490 guest cases per stream**, comparing literal retail and compiled C
  with an independent byte-memory/token model. Every one of the 93 original
  words is visited. Cases include timer boundaries and unsigned tick values,
  signed high tokens, all call/return paths, coordinate truncation, halfword
  widths, helper clobbers/mutations, output aliases and guest-only sparse
  pointer/word overlaps. Actor backing is explicitly separate from the stack.
- **167 exact fault-prefix pairs**, five effective instruction controls and
  three fired pre-actor-load cuts establish the original argument-home
  stores and complete emitted access state.
- **418 actual native SDK32 C cases each at O0/O2/O3**, with strict aliasing,
  UBSan and float-cast-overflow checks. Expected fields and helper snapshots
  are serialized from the independent Python model. Seven executed semantic
  negatives per profile are rejected.
- **Twelve independent GNU links** compare fresh original assembly and
  isolated C across six relocation rebases. All 372 single-byte corruptions,
  every changed-binding control and three image corruptions are rejected.
- Four-test suites pass in the primary checkout and isolated sibling overlay,
  both before and after installation. Their 313/314 imported tool files are
  byte-identical apart from the overlay bootstrap. The real sibling's dirty
  status, HEAD and 343 relevant dependency hashes are preserved.

The complete ROM scan finds no direct JALs or literal pointers to this
entrypoint. Computed/external calls are not excluded by that census. Callee
word-slot accesses and native fixed-argument calls establish the tested ABI;
no original full-parent execution is claimed. Sound helpers remain bounded
opaque providers. Float-invalid/overflow hardware behavior, interrupts and
gameplay acceptance are not inferred from the finite native tests. Literal
instruction identity is separately established for the entire target.

## Records and continuation

Private receipts: `conker/build/game-sound-timer-15103aa0-private/`,
including both owned-frame captures, paired installed suites,
`production-audit.json`, independent image receipts and the fresh recount.
Zero Claude calls; local compiler evidence resolved the bounded question.

Detailed recovery stays here and in concise DOCS indexes. Root README
changes only its two aggregate matching rows. Next inspect the adjacent
**100-word `func_15103910`** using this owner/ABI groundwork, while preserving
its own signed-counter and sound-parameter behavior. The older actor-burst
candidate remains private and uncredited.

Graphify's native update refuses a shrink; a scoped five-file AST merge
retains all 67,301 preceding IDs and adds the literal manifest target edge.
This is not full-corpus re-extraction. The consumer hook must finish before
historical heading retention and the final graph SHA are sealed privately.
