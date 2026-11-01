# Oriented displacement pair: direct C match and pointer ABI repair

Verified 2026-11-01. `func_15115E0C` now emits all 52 retail words directly
from semantic C. Its complete 35-word caller, `func_15115EDC`, also emits
directly after correcting the callee declaration and removing the single
legacy register guard that compensated for the false declaration.

The fresh production recount is **4,026/5,507 (73.11%)** total and
**3,353/4,834 (69.36%)** Game, with zero address drift and 1,481 different.
Init remains 492/492; Debugger remains 181/181. The 75% threshold is 4,131:
**105 additional exact C functions are needed**. This is one new match;
the caller was already counted as exact through its old guard. The converted
C inventory remains 5,507/6,045, including Game 4,834/5,324.

## Source and recovered interface

- Owner: `generated_142560`; source `conker/src/game/generated_142560.c`.
- Original assembly: `conker/asm/142560.s`, retained without modification.
- Root: VA `0x15115E0C..0x15115EDC`, ROM `0x1432BC..0x14338C`;
  208 bytes, 52 words, 32-byte frame, six relocation bindings.
- Caller: VA `0x15115EDC..0x15115F68`, ROM `0x14338C..0x143418`;
  140 bytes, 35 words, 32-byte frame, one JAL binding at offset `0x20`.
- Both interfaces are `void(u8 *state, u8 *target)`, with record pointers
  in A0/A1. The old root's integer return and two leading float parameters
  were placeholder artifacts. The caller's F12/F14 values are local snapshots.

The root calls cosine and sine with the state angle at `+4` multiplied by
the separate globals `D_800A2FA0` and `D_800A2FA4`. Both retail constants have
bits `0x3C8EFA35`; their distinct loads and the second angle reload matter.
After both calls it reads the signed origin halfwords at `+0x10/+0x14`,
the target's float coordinates at `+0x14/+0x1C`, and state flag bit 4 at
`+0x4F`. When enabled, it adds `sine*deltaX + cosine*deltaZ` to `+0x7C`
and subtracts `sine*deltaZ + cosine*deltaX` from `+0x80`. Preserve these
retail sums and operation order, including the two positive terms in the
second sum.

The caller captures both previous output coordinates before calling the root.
If the target's live unsigned halfword at `+0x84` equals `0x4B`, it adds
four times each change to the new coordinate. Helper mutations must affect
the live gate without changing the saved pre-call coordinates.

Exactly one guard row is removed: caller offset `0x018`,
`0x8FA60024 -> 0x8FA50024`. The corrected C naturally emits `0x8FA50024`.
The old manifest rejects this corrected owner as a stale word patch; all
other manifest bytes are preserved. No new guards, profiles, inserted words,
omissions, shared declarations, or Makefile changes are used.

## Qualification and limits

- All four programs—original assembly, qualified padded owner, actual Make
  object and isolated C—agree across **3,072 guest cases / 12,288 executions**,
  three address layouts, four record alias layouts and two stack phases.
  All 52 root and 35 caller words execute. Public memory, registers, FP
  registers, call packets, access traces and remaining modeled state agree.
- Helper mutations exercise the second angle/scale reload, post-helper signed
  origins, target coordinates, flag, output coordinates and live target type.
  Caller-saved GPR/FP state and outgoing homes are clobbered by providers;
  the saved cosine and original caller snapshots survive correctly.
- **116 access prefixes / 464 executions** agree across all four programs.
  These qualify emitted guest instruction order, not portable C fault behavior.
- **1,024 connected cases / 4,096 executions** run the original cosine/sine
  span, pinned against ROM and the baseline ELF, with twelve original
  coefficient words. All 73 executable helper words are reached; the complete
  76-word span also includes three padding words. A separate finite polynomial
  reference agrees, including tiny and huge finite angle paths. Full FCSR
  effects, arbitrary NaN payloads and hardware gameplay are outside this model.
- Native C passes **1,024 cases per profile** at `-O0`, `-O2`, `-O3`, using
  32-bit SSE single precision, disabled contraction, UBSan traps and complete
  record canaries. Eight compiled controls fail as intended: wrong first scale,
  cached angle, unsigned origin, wrong flag, wrong Z sign, wrong X coefficient,
  wrong wrapper gain and cached target type. Native records are disjoint;
  the overlapping record layouts are qualified by guest execution.
- ROM census finds the sole root JAL at `0x1433AC`. The caller has no direct
  ROM JAL/J and one aligned pointer literal at ROM `0x22D790`, VA `0x80088CD0`,
  byte offset `0x40` in `D_80088C90`. The complete immediate caller runs in
  the connected tests. This does not claim end-to-end execution of the larger
  state callback installation and invocation machinery.

## Owner, build, image and production audit

Both raw owners have zero warnings. All **82 other raw functions**, all
**83 other padded functions** including the caller, and normalized pools
are unchanged. The actual five-command production Make recipe includes
ASM preprocessing, IDO, ASM postprocessing, generated padding and assembly;
its object is byte-for-byte identical to the independently qualified object.

The independent complete ELF predictor changes the root slot and symbol
extent from 24 to 208 bytes and reconstructs three closed GNU linker
symbol/string permutations entirely from pinned baseline rows:

1. `D_800991C0 / D_8009E6D0`: swap.
2. `D_800A2FA4 / D_800907A4`: swap.
3. `D_800A2FA0 / D_8008F8C4 / D_800D35E4`: rotate left.

All definitions, metadata fields and string spans are preserved. No bytes or
metadata regions are excluded from the comparison. The complete first link
and production image match the prediction at **214 changed bytes**. All
6,056 function addresses and 6,055 other function bodies remain fixed;
all 189,088 protected Game data bytes across 720 owners remain exact.

Production ELF SHA-256:
`83346e7617b975a65e7af47e5b417a10b000edfe9f396728160827d438f36c42`.

The production Make, complete 17,572-input predecessor seal review, six public
tests per tools copy before and after adoption, both shared tool checks, and
independent Native actual-ELF recount pass. Only source, its owner object,
the one-row guard removal and the ELF change; no dependent objects change.

Reusable tools are `game_oriented_motion_pair_match.py`,
`game_oriented_motion_pair_oracle.py` and
`test_game_oriented_motion_pair_match.py`. The older dirty tools mirror
receives only these three identical owned modules; preserve its other work.
Commit tools before the consumer pin; no push.

## Continuation

The self-contained build checkpoint is
`conker/build/game-oriented-motion-pair-15115E0C-match/` with 1,027 frozen
focused inputs, 25 canonical prepared artifacts and separate before/after
production receipts. Failed fixture versions remain documented: the initial
Make expectation omitted two ASM-processor commands; the initial image
predictor omitted the three closed metadata groups; the initial call census
did not mask the JAL region bits; the trig interpreter needed `neg.s` support.
None required changing the recovered semantic C.

Next audit: `func_15116D7C`, another placeholder in the same owner, 74 retail
words. Establish its complete ABI, callers and behavior before attempting a
conversion. The packed-motion, identity-dispatch, relative-direction, scalar
smoother and other private candidates remain uncredited. The wider 75% goal
stays active. Host port/editor/Release artifacts are outside this change.
