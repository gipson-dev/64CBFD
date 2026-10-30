# Note 1880: actor parameter byte clamp direct C match

2026-10-30. `func_150DB630`, owner `generated_108320`, replaces a zero-return
placeholder with `s32 func_150DB630(u8 *actor)`. All **57 words /228 bytes**
at VA `0x150DB630..0x150DB714`, ROM `0x108AE0..0x108BC4`, emit directly from
semantic C using the existing O2/g3/mips2/o32 profile. No guards, insertions,
omissions, bindings, compiler-profile changes or shared-header changes are needed.
Tools commit: `9770c2e80b8f8c0b19703fd47083301486ab773d`.

## Recovered behavior and source shape

The actor contains a parameter pointer at `+0x120`. Its pointed-to single-precision
value above255 stores255 at actor `+0x5C`. Otherwise retail reloads the pointer,
reads the lower-path value, stores0 if negative, or converts it to unsigned32
and stores the low byte. Every path returns1. The leaf has no stack frame and
does not save RA or any callee-saved register.

The first pointer access uses `f32 * volatile *` to preserve the two retail
pointer reads. The lower-path value is captured once for its negative test and
conversion. An inline comment explains this reload. The initial ordinary C
form emits55 words and merges the reads. Introducing a separate lower-path
value without the volatile pointer emits56 words. The selected source emits
all57 words, including the exact three compiler-dead duplicate instructions at
indices12,22,48. All54 reachable words are exercised. No hardware requirement
for volatile is inferred from this compiler-matching source form.

For stable finite samples, the observable operation is a clamp to[0,255] followed
by truncation. Unsigned conversion is retained because that is the retail compiler
sequence. The guest tests include NaNs, infinities, signed zero, subnormals,
integer boundaries and conversion-overflow fallback paths. Nonfinite conversion
and asynchronous pointer-switch cases are guest-only. The existing bounded
nontrapping FCSR model checks control save/restore; this does not claim real
hardware exception, signaling-NaN or concurrent portable-C semantics.

## Qualification and original callback interface

Ignored evidence: `conker/build/game-actor-byte-clamp-150DB630-match/`.

- Guest:864 cases /2,592 executions compare original, freshly compiled and
  padded code against independent byte/return/access-order expectations. Complete
  RAM and modeled state agree. Cases include384 aliases into the actor output
  or stack backing and288 pointer-switch cases between the two pointer reads.
  Twenty-eight access cuts include two delay-slot cuts;72 additional cases run
  at three alternate entry addresses. There are no relocations to rebase.
- Caller:the sole aligned literal pointer is at ROM`0x22E848`,
  VA`0x80089D88`, index10 of `D_80089D60`; there are zero aligned direct JALs.
  The original13-word window at`0x1513D074..0x1513D0A8` in `func_1513CFE4`
  executes the real table load, JALR, delay slot, actor reload and return test.
  It passes288 cases covering selector0 and10, incoming flag0/1/255, two stack
  phases, and all sample patterns. The signed-byte flag reload is modeled
  explicitly. The success return leaves the original flag unchanged. The full
  parent and gameplay behavior are not claimed.
- Nine IDO-compiled semantic controls are rejected through actual result/RAM
  mismatches:missing pointer reread, wrong pointer/output fields, upper/lower
  gates and clamp values, masked conversion and failed success return. Compiler
  or interpreter errors are not accepted as negative-control successes. An
  initially proposed lower bound of1 was semantically equivalent for byte
  truncation; it was replaced with an effective128-bound control.
- Native32:844 finite-input cases per O0/O2/O3 profile pass with trapping UBSan,
  actual pointer backing, every actor byte checked and pointed storage checked.
  The corpus covers every output byte and both sides of each integer boundary.
  Seven compiled controls are effective; asynchronous reload and alternate
  pointer controls remain guest-only. Nonfinite input is not credited natively.
- Owner:all five raw and padded neighbors, pools and unrelated inputs remain
  fixed. The actual three-command Make recipe reproduces the padded owner.
  Target, owner and command diagnostics are empty. Existing duplicate
  `generated_12D630` recipe warnings occur only in the inherited dry-run plan.
- Image:an independent literal whole-image prediction equals both the private
  first link and production ELF:141 changed bytes =140 code bytes +1 symbol
  extent byte, metadata0, exclusions0. All6,055 other linked bodies and all6,056
  addresses remain fixed. Protected Game data stays exact across189,088 bytes
  and720 owners. The guard CSV and C inventory CSV remain unchanged.

Both tools copies pass eight fresh canonical target checks and shared tool
checks. Production runs two fresh installed checks per copy and reuses six
unchanged semantic checks under exact input/module/artifact fingerprints. The
older tools mirror retains all2,078 inherited dirty paths and gains three new
qualification files; its HEAD and unrelated work remain untouched.

## Banked measurements and continuation

Raw/original function SHA-256:
`cc26e69f08d15e0d85350cdb61d25e7c977395a0a248f874b3d8c8bad30309e5`.
Owner source SHA-256:
`9cf9285134f7b048eee071b068d57107aa108475fdd9bda9bce43ca4bc2ab311`.
Padded owner SHA-256:
`031855278031de71e815fdf672ffb4b5c038730ffcf4863e61a92d9f5e938898`.
Adopted ELF SHA-256:
`d712b807e2feff412e14d72e437dc0e0170e0ef533df79882f4de5bf7f07a1df`.

Fresh recount of the captured adopted Native ELF gives **3,957/5,506 (71.87%)**
total exact C and **3,284/4,833 (67.95%)** Game, with zero drift. Init remains
492/492 and Debugger181/181. **173 more** matches are required to reach
4,130/5,506 and satisfy75%. The goal remains active. Next private screen:`func_1502378C`.
The root README changes only its two aggregate matching rows; detailed updates
remain here. Graphify uses the bounded eleven-file AST refresh, preserving the
live graph's historical nodes and valid relationships. No full-corpus extraction,
global clustering, full-parent or hardware acceptance claim is made. No Claude
review or REA provider setup was needed for these routine local screens.
