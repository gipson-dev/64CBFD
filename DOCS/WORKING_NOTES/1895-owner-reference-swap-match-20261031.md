# 1895 - Owner-reference command callback: guarded C match

Date: 2026-10-31. Function `func_15161F4C`, ordinary owner
`conker/src/game_18D770.c`. VA `0x15161F4C..0x15162034`, ROM
`0x18F3FC..0x18F4E4`: 58 words / 232 bytes, no alignment padding.

The old zero-return placeholder is replaced by semantic C. Mode0 removes the
record if either its reference pointer or saved identity byte matches the
command's single-reference view. Mode `0x2D` replaces a matching first pointer
with the second pointer and second ID, or a matching second pointer with the
first pointer and first ID. It then reloads the selector byte at record+`0x1D`
and optionally calls `D_8008B358[selector](record, command, mode)`.

## Interface and recovered layout

The local reference payload is at record+`0x18`, with pointer at+0, identity
byte at+4 and selector at+5 (six initialized bytes, sizeof8 under o32).
The command union exposes either pointer/ID at0/4, or two pointers at0/4
and their IDs at8/9. The frame is24 bytes: RA20; incoming record home24,
command home28, mode home32 with the low byte saved at35.

`D_8008B150` slot21 contains this target at ROM `0x22FC64` / VA
`0x8008B1A4`. Class53's original88-word dispatcher `func_151604A0` passes
record, command and truncated mode through its JALR at `0x151605E4`.
The enclosing original105-word list dispatcher `func_1516944C` invokes that
class handler through `0x15169520`, then reloads traversal state without using
the callback return. Both levels establish the recovered void, three-argument
interface. The outer dispatcher remains its pre-existing production placeholder;
its original ROM execution is qualification evidence, not new recovery credit.
The class handler remains its original assembly, unchanged.

The final table `D_8008B358` has three real entries: NULL, `func_150F1684`,
NULL. The original22-word final callback handles mode `0x43` with its own
pointer-or-ID removal check. Its entire body is retained and separately executed
in the connected suite. The aligned ROM census finds exactly one target literal
pointer and no direct J/JAL references.

## Narrow guarded normalization

IDO emits57 semantic C words under the existing O2/g3 profile. The first
one-argument callback draft lost command/mode lifetimes and was rejected.
The recovered three-argument draft retains all argument homes. A bounded set
of if/switch, operand-order and callback-local experiments is preserved.

Four expected-word/binding rows restore the closed retail control-flow layout:

- Raw offset `0x18`: adjust the conditional branch across the inserted word.
- Raw offset `0x40`: adjust the second conditional across that same word.
- Raw offsets `0x60/0x64`: move the existing owner-home reload before the
  unconditional branch, retarget that branch past the common selector load,
  and insert the existing common-tail selector load in its delay slot.

No side effects or fake C reads are added to force scheduling. The inserted
instruction is copied from the existing raw common-tail load; it is a static
duplication on a mutually exclusive path. Three relocation bindings are
preserved, with downstream offsets shifted by the inserted word. Eight invalid
expected-word/relocation preimages are rejected by the actual ordinary-C padder.
The complete inherited guard manifest remains a byte-for-byte prefix.

The retail body itself contains an unreachable duplicate second-pointer load
at `0x15161FE8`. Its predecessor is an unconditional branch's delay slot and
no internal branch targets it. All57 reachable words are visited; all58 words,
including this duplicate, remain byte-exact. It is not called alignment padding.

## Fresh evidence

- Both tools copies pass eight fresh focused methods plus shared tools checks.
  Production then passes two fresh installed methods per copy, with six
  unchanged semantic methods reused only under exact module/input/artifact pins.
- Guest: 6,048 cases / 18,144 executions cover raw C, normalized and original
  streams, all reachable words, all modes of interest and upper-bit truncation,
  live selector/table changes, command mutations and saved argument lifetimes.
  Raw C agrees on public state, calls, observations and memory access order.
  Normalized/original streams also agree on complete modeled machine state.
- 72 guest alias cases, three independent GNU layouts, 55 fired fault-prefix
  pairs and eight branch-delay cuts pass. Raw fault context is not equated to
  the guarded retail instruction schedule. Guest overlap cases are not portable
  C alias/union/memcpy claims.
- 168 original two-level dispatcher cases cover empty, single and two-node
  lists, both rows, argument-byte truncation, varied callback returns and stack
  phases. All three arguments reach the target and the callback return is dead.
- 288 cases / 864 executions connect the complete original22-word final
  callback, including all its instructions and mode67's identity-or-pointer
  check. Removal remains a bounded provider; no gameplay acceptance is claimed.
- Native SDK32 O0/O2/O3: 98,304 positive cases per profile with trapping UBSan,
  all256 mode values, disjoint typed record/command objects, whole-storage
  fences and11 effective semantic controls. The selected body and every control
  compile successfully; compiler/interpreter failures are not semantic controls.
- All77 raw/padded owner neighbors and normalized pools are unchanged. Five
  actual Make commands reproduce the exact qualified object. All48 inherited
  compiler warnings are unchanged after normalizing filename/line positions;
  the isolated selected C has no diagnostics. Shared headers are unchanged.
- The strict full ELF prediction has zero exclusions and exactly169 changed
  bytes:168 target-code bytes and one function-extent byte. No metadata bytes
  change. All6,055 other linked bodies, every address, and189,088 protected
  Game data bytes across720 owners remain identical. Conversion CSV is unchanged.

## Banked result

Tools commit `092a8a2100e080dc745ee384dffe243012674ab8` precedes the consumer commit. Production ELF SHA-256:
`3ccf015d8a0ced863337d5f965f0aed5c3dcac6ba684f2194f0c57c9fdd0caa2`.
Actual adopted-ELF recount: **3,972 / 5,506 (72.14%)** overall and
Game **3,299 / 4,833 (68.26%)**. Init492/492 and Debugger181/181 remain
exact; zero drift,1,534 C functions still differ. **158 more** are needed for
4,130/5,506 (75%). Next screen: `func_151A0A10`.

Receipts, failed/rejected private experiments and immutable before-inputs are
under ignored `conker/build/game-owner-reference-swap-15161F4C-match/`.
Only the two root README aggregate rows change. Scoped graph refresh retains
all prior nodes and valid relationships while retiring the stale placeholder
return-type edge. No full-corpus extraction, global clustering, hardware or
full-gameplay claim is made. No push.
