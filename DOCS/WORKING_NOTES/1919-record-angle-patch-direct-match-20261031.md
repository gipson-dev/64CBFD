# Sentinel record angle patch - direct C match

2026-10-31. `func_150C7C90` in `generated_F4D20` is restored from its zero-return
placeholder as `void func_150C7C90(u8 *actor)`. All 59 words / 236 bytes at VA
`0x150C7C90..0x150C7D7C`, ROM `0xF5140..0xF522C`, emit directly from C with the
original JAL relocation. No guards, inserts, omissions, alignment words or
compiler profile changes are used.

## Behavior and source shape

When the actor's cached index at +0x7C is zero, scan eight-byte records from the
pointer at +0x1C until their signed opening byte is -14 (`0xF2`), then publish
that index. A sentinel at index zero retains zero and therefore scans again on
the next invocation. A nonzero cached index bypasses the scan.

Capture the selected record pointer before calling `func_151149AC` with the low
byte of the actor word at +0x3C. Read the returned object's signed heading at
+0x12, compute `-669 - heading`, and mirror as `836 - angle` when the live actor
word has bit 0x8000. The live word is read after the helper. Normalize by repeated
1024 additions/subtractions. Clear the selected record's low twelve bits, then
OR in the normalized angle using the two original separate word stores.

The lookup result is dereferenced without a null gate, as in retail. Native
tests use valid object returns and bounded record arrays; full-word guest or
arbitrary invalid-pointer portability is not claimed. The original offset-based
field names and address-based function name avoid speculative structure names.

An initial separate command cursor let the compiler strength-reduce the scan
and choose different registers. Reusing the record cursor and expressing the
scan offset as `index << 3` recovers the complete instruction stream naturally.
The existing O2/g3 owner profile is used through
`game_remaining_donor_candidates.compile_owner`. The frame is 32 bytes, RA is
at SP+0x14, the selected record at SP+0x18, and the actor is saved in its incoming
home at SP+0x20. The six neighboring bodies and all owner pools are unchanged.

## Callback and connected evidence

There are no aligned direct JALs to this function. Its one aligned literal
pointer is ROM `0x22D888` / VA `0x80088DC8`, inside the 12-byte callback table
`D_80088C90`. Two original dispatch windows load actor+0x38 and call through
JALR with the actor in A0, ignoring a result: ROM `0x141390` (five words) and
`0x141468` (four words). Both execute with the recovered target in 32 cases.
This is bounded caller evidence, not recovery of the complete update parent.

The complete original 28-word `func_151149AC` runs in 80 connected cases. Its
five-record fixture exercises first-match identity selection, duplicate IDs,
last-slot selection and 0xA0-byte object stride. No full-parent, gameplay or
hardware acceptance is claimed.

## Qualification

- Original, fresh raw C and padded C agree literally across 3,456 guest cases /
  10,368 executions, exercising all 59 words and preserving complete final
  machine state, memory, calls and traces. All 71 access-prefix comparisons pass.
- Three independent code/call-target layouts produce nine rebase cases. Cached
  and uncached paths, sentinel zero, signed heading boundaries and helper changes
  to flags, cached index, record base, selected word and heading are checked.
- Native32 C passes 524,288 cases per O0/O2/O3 profile with UBSan. Every signed
  16-bit heading, both mirror states, all sentinel positions and cached/uncached
  cases are represented. Entire actor, command, alternate and object buffers
  are compared; unrelated bits and bytes are retained.
- Thirteen distinct wrong variants fail native and compiled guest checks.
  An unsigned 16-bit heading variant was rejected as a negative-control design:
  after modulo 1024 it has the same final value. The final byte-width control
  changes behavior and is rejected; ineffective controls are not credited.
- Eight fresh canonical tests pass independently in each tools copy and both
  shared tools checks pass. Two installed checks per copy run fresh; six stable
  semantic checks are explicitly reused only under exact fingerprints.
- Five actual Make commands, including GLOBAL_ASM preprocessing/postprocessing,
  reproduce the qualified object with no C compiler diagnostics. The inherited
  unrelated Make recipe warning is separate from compiler diagnostics.
- Strict whole-image prediction accounts for 185 changed bytes: 184 target code
  bytes and one target extent byte, with zero metadata changes or exclusions.
  All 6,055 other bodies, all 6,056 addresses, the unchanged guard manifest and
  189,088 protected Game data bytes across 720 owners remain fixed.

## Banking and continuation

Tools commit: `904d09f675dbc08190001af5c9647f21b2e513a8`. Production ELF SHA-256:
`e24ab1f1ea77c2912eda733e38ac9d2b2cbc648ba6ac8bf3bf5343267bedd3ec`.
Actual recount is **3,996/5,506 (72.58%)** total, **3,323/4,833 (68.76%)** Game;
Init remains 492/492, Debugger 181/181, and address drift is zero.
**134** more functions are needed for the 75% threshold of 4,130.

Receipts are in ignored `conker/build/game-record-angle-patch-150C7C90-match/`.
Only the two aggregate README status rows change. The scoped graph refresh
covers this source, three tools modules and seven documents, preserving valid
old relationships without claiming full-corpus extraction or reclustering.
Next queued screen: `func_15108C38`. Private candidates remain uncredited.
No push or host-port/Release changes are included.
