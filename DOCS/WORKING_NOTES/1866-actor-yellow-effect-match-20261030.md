# 1866: Actor effect descriptor callback restored from C

Verified 2026-10-30. `func_150E67D0` replaces its zero-return placeholder in
[`generated_113480.c`](../../conker/src/game/generated_113480.c).
All 54 body words and both original JAL relocations emit directly from C.
The original 120-byte frame, RA at SP60, descriptor at SP72, incoming home
at SP120 and two slot-alignment NOPs are preserved. No guards, inserted or
omitted words, frame patches, shared-header changes or compiler-profile changes
are needed. The inherited guard manifest and progress CSV are unchanged.

Actual linked recount: **3,943/5,506 (71.61%)** total,
**3,270/4,833 (67.66%)** Game, Init 492/492, Debugger 181/181, zero drift.
The active 75% goal needs **187** more to 4,130/5,506.

## Recovered behavior and source decisions

The callback initializes a 40-byte effect descriptor's proven fields: word0=1,
halfword4=100, byte6=0x3A, words8/C=0, bytes10/11=255, bytes12/13/14=0,
byte15=255 and word18=0x130001. Exactly 25 bytes are initialized. Unknown
byte-field meanings retain offset names; no color/alpha interpretation or
portable value for the other 15 descriptor bytes is claimed.

It calls `func_1513C73C` with fourteen arguments: the descriptor, two zeros,
actor+0x124, three float payloads at actor+0x114/118/11C, 50.0f twice, the
RNG's low byte, two more zeros, actor byte0xC and actor byte1. The constructor
return is discarded and the callback returns zero. Its prototype uses the
provider's actual `struct210 *` result and original integer/pointer carriers.
The descriptor remains local to this owner; the existing shared header is used.

The alternate source supplied an expression-shape clue, but its integer
coordinate reads and word-sized tag reads were rejected. A typed inline RNG
call plus a named float range local and recovered declaration order emits the
retail body directly. No inferred volatile parameter or artificial frame
padding is adopted. The final field-name clarification leaves the complete
instruction body, padded object and linked image identical.

## Qualification and limits

Ignored evidence is in `conker/build/game-actor-yellow-effect-match/`.

- Compiler/owner: raw 54-word SHA-256 is
  `d8b39953f741dbe1775082af027d30e0ec090fffc3a5f4ca96c38e406a9a307c`.
  Both bindings, four raw/padded neighboring functions and owner pools are
  fixed. Actual Make's three commands reproduce the qualified padded object.
  Selected, owner and actual-Make diagnostics are empty.
- Guest: 1,536 cases / 4,608 executions cover all 54 body words, 93 access
  prefixes, 192 rebased cases across three layouts and 38 private-home/alias
  cases. Original, raw C and padded programs agree on full registers, memory,
  calls, access traces and the observed 40 descriptor bytes. RNG boundary bits,
  tag widths, finite/nonfinite float payloads and zero/nonzero constructor
  results are covered. The two alignment words are not executed.
- Original caller: a complete aligned ROM scan finds no direct JAL and one
  function-pointer word, at ROM0x22D4D0 / D_80088A10. The original twelve-word
  indirect window at VA0x150E62FC / ROM0x1137AC runs 64 cases per program.
  It forwards the actor, consumes the callback result as a signed byte and
  restores its actor register from the saved caller slot. The result is zero.
  This proves the window, not the complete parent routine or table-index gates.
- Native32: 128 finite payload/ABI cases each at O0/O2/O3 pass UBSan and eleven
  effective controls for descriptor fields, axes, range, random mask, payload
  pointer, tag and result. All initialized fields and fourteen arguments are
  checked. Private home mutations, uninitialized descriptor bytes and nonfinite
  native float payload preservation are not claimed.
- RNG contract: all 18 original instructions at ROM0xDAED0 are checked against
  retail, including an effective changed-store rejection control. Its only
  write is the eight-byte seed D_800885B0; it uses no actor pointer and calls no
  other routine. The native actor fixture is disjoint from that seed. An
  experimental actor-mutating native RNG exposed unspecified C argument
  evaluation order, so such mutations remain guest instruction-order stress
  only. No portable ordering against an actor-mutating RNG is claimed. Original
  RNG instruction execution and constructor body execution remain outside the
  bounded helper models.
- Full image: private and production ELF equal the independent prediction,
  SHA-256 `5c147a90638a41271d1206a9845007e82eedd11c90038a5f26ff3e3d0e46c615`.
  Exactly 161 bytes change: 160 target-code bytes and one target symbol-size
  byte. Metadata reorderings 0, exclusions 0. Every function address, all 6,055
  other bodies and 189,088 protected Game bytes across 720 owners are fixed.
- Both tools copies run eight fresh canonical checks and their project tools
  check against the final named source. Two fresh installed checks per copy
  follow production; six unchanged semantic checks are explicitly reused by
  identical module, input and artifact fingerprints. The full 16,954-file seal
  preserves all other inputs and objects.

Hardware traps/NaN payload behavior, complete parents/helpers and host-port
gameplay acceptance are not established by these checks.

## Banking and continuation

Tools are committed first at **7b89b7bfc0cdf20dd7872810124c86a42e713622**, then the consumer pins that commit.
No push is performed. The independently dirty older mirror is preserved.
Only the root README's aggregate exactness rows change; detailed updates remain
in this note and documentation indexes. Graphify receives a scoped AST refresh
with explicit old-node and relationship retention, not a full-corpus extraction.

Next private screen: **func_150EAF50**. Deferred candidates remain uncredited until all
source, ABI, owner, semantic, full-image, production and documentation gates pass.
