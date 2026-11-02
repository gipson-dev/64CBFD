# 1991 - Wide-packet factory recovered as guarded C

Verified 2026-11-02. Production **4,058/5,507 (73.69%)**; Game
**3,385/4,834 (70.02%)**, Init 492/492 and Debugger 181/181. Zero address
drift, 1,449 different; one new installed match and unchanged C inventory.
The active 80% target remains **4,406/5,507**, requiring **348 more**. This is
progress toward that goal, not completion.

## Interface and recovered behavior

`void func_151539B4(WidePacketInput *input, u8 mode)` replaces the zero-return
placeholder in `conker/src/game/generated_17CAF0.c`. Original `17CAF0.s`:
VA151539B4..15153C84, ROM180E64, 720 bytes, 180 words, 184-byte frame and
thirteen relocation bindings. The recovered input has a natural 72-byte C
extent, a live extent through byte 70 and 70 bytes actually read. Byte 49 and
the natural tail byte 71 remain private and unread.

The factory chooses a randomized packet count, copies the origin, nine payload
bytes and three fixed fields, and draws two angles per packet. Four trigonometric
queries construct a fixed-length direction vector. Two randomized floating
values, a randomized short, float and byte complete the visible payload before
`func_15156190` submits it with the recovered kind and mode. The return contract
is `void`; both original callers ignore V0.

The draft in `Another Source/CBFD-Recompiled` was used only as a recovery lead.
Its names, types and comments were not adopted. Every credited field width,
caller contract, packet extent and behavioral claim was independently qualified
against this repository's retail image and build.

## Complete extents and closed compiler words

The submitted packet has a natural **60-byte** private extent and a live extent
through byte 57. The factory initializes 54 bytes. Six bytes remain untouched:
offset 41, offsets 46..47, offset 53 and offsets 58..59. Guest execution verifies
that all six private bytes survive every submission rather than treating the
visible writes as the whole object.

The semantic C emits exactly **180 words**, the retail 184-byte frame, all
thirteen relocation bindings and the retail stack geometry. One deliberate
volatile duplicate read of input offset 40 preserves the compiler's opening
load schedule without changing public state. IDO otherwise chooses closed
packet-pointer, saved-register, temporary-register and independent scheduling
roles differently from retail. Twenty-five checked expected-word
normalizations close only those roles and one commutative floating multiply.
No relocation word is guarded. After normalization every word equals retail at
three independently shifted GNU code/provider layouts.

Raw semantic payload SHA256:
`6b604155f0f95c0b49cf459376fd966cebcde5e9217d863dc000d3b77c721f96`.
Normalized payload SHA256:
`55fc20581320123f9891d01122a03b6926841dc87d0a705e000f10a3f7cd36cc`.

## Fresh qualification

- Guest execution covers 256 cases at each of three independent links, for
  2,304 original/normalized/raw-C executions. All 175 reachable non-trap words
  execute; five positive-divisor trap words remain unreachable under qualified
  ranges. All 256 mode bytes and zero/one/two-packet paths execute.
- Original and normalized code agree in full memory, register, FP, call,
  payload, event and access-trace state. Raw C agrees in public memory, calls,
  complete payloads and callee-preserved state. Its sole difference is the
  documented duplicate input-offset-40 read: one per execution, 768 total.
  The role comparison covers 47,760 events and 162 normalized access-prefix
  pairs.
- Live input mutation after the first RNG call and after each submission proves
  that later-loop ranges, values, kind and mode are consumed at their recovered
  times. Every private packet byte remains untouched.
- Native O0/O2/O3 runs 256 cases per profile, 768 total, with
  `-Wall -Wextra -Werror` and UBSan stopping at the first error. All profiles
  pass with no warning or sanitizer finding.
- The complete ROM census finds exactly two aligned JALs in two C parents, no
  aligned jump and no literal target pointer. Static pre-call provenance covers
  every one of the 70 input bytes read. Both callers establish the byte mode,
  and conservative V0 taint reaches no post-call read. Complete parent execution
  is not claimed.

The callers are `func_150B2740` at VA150B2AD0/ROM0DFF80, using input at
SP+0x14C and the low byte of S3, and `func_151568F8` at
VA15156A14/ROM183EC4, using input at SP+0x98 and its caller byte at SP+0xE7.
Both tools copies contain byte-identical five-module qualification suites. The
shared installed suite passes all five methods after validating those hashes.
The bounded 12-file AST refresh retains all 57,855 prior nodes and all 119,241
still-valid prior edge occurrences, archives the obsolete placeholder return
edge and uses zero LLM tokens. No full-corpus extraction or global reclustering
is claimed. No gameplay acceptance is inferred from byte and semantic controls.

## Owner, image and production result

All 40 raw and padded `generated_17CAF0` neighbors and normalized pools remain
identical; owner compilation has zero diagnostics. The real owner recipe uses
five commands and produces the qualified 29,988-byte object. Protected Game
data remains exactly 189,088 bytes across 720 owners, SHA256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

The strict complete-image predictor replaces the placeholder slot with the
720-byte target. It has zero exclusions and needs no metadata reorder closure.
All 6,052 function addresses, 6,051 other bodies and the complete named-
definition multiset remain fixed. The installed production object equals the
qualified five-command Make object, and the directly linked production ELF
equals the independent strict whole-image prediction exactly. Unlike the prior
checkpoint, this production link completed normally through the OneDrive/WSL
checkout; no fallback artifact was installed.

Installed object SHA256:
`514c392b527e29ade399eaf7a4f63a2fe80d9918c3e4dc6f14144494fbe93a5c`.
Linked ELF SHA256:
`35712bfe42fc4fac25904136609c5df5d840a7c08a3481b3a4cd2db2ceb93d8e`.
Linker-map SHA256:
`ebb679dbafe5095950abc7ea997853701ce7cf975c8529cf54230dc13f2f0b51`.

The public qualification tools were committed first at `f5ca125b`. The
retained stage is
`conker/build/game-wide-packet-factory-151539B4-match/`; it contains the layout,
guest, native, caller, owner, whole-image and installed receipts. The root
README changes only aggregate rows; detailed recovery stays here and in the
five concise indexes. No Claude call was needed.

## Next step

Privately audit `func_15153CCC`, the next C placeholder after the already
recovered `func_15153C84` wrapper. Qualify its ABI, complete object extents,
caller/provider ordering and owner neighbors before source fitting. Keep it
uncredited until guest/native/caller, owner/actual-Make, strict-image, installed
recount, documentation and bounded Graphify-retention gates pass.
