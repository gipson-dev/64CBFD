# Parameterized Owner-Selector Payload Guarded C Match

Date: 2026-10-22

## Result

Recover `func_15192D48` in `conker/src/game/generated_1BFDD0.c` from its
zero-return placeholder. Complete semantic C emits **42 words / 168 bytes,
frame 56 and two call relocations**. Seventeen expected-word guards close
one argument/payload schedule. The installed body is byte-exact. This is
guarded C, not compiler-only matching.

VA 15192D48..15192DF0 / ROM 1C01F8..1C02A0, ends exclusive. Preserve
`conker/asm/1BFDD0.s`. Keep the address-based name and add the purpose comment.
Reuse the existing `Generated1BFDD0Payload` and allocator declaration; no
shared-header, profile, inserted-word, omitted-word or frame changes.

The old emitted body was 12 bytes in its 168-byte retail slot. Converted-C
totals and conversion rows do not change; this earns one additional exact C
match. Raw unlinked body SHA-256:
`e05cc6731ff218816a73d608e4dc2767763d53bf49bb215158fc28a8b668ed8f`.
Pin R_MIPS_26 bindings at +0x6C to func_151491F4 and +0x88 to memcpy.

## Recovered Contract

A null owner returns null without reading owner memory or allocating. Otherwise
capture its pointer and byte at +0x3B in the existing 12-byte local payload,
and set the payload float to positive zero. Preserve its three reserved bytes;
do not invent a clear of them.

Call func_151491F4 with `(lifetime, -1, 0x18, 1, 0x16, 12, selector, parameter)`.
The first argument is signed 16-bit, selector unsigned 8-bit, and parameter a
full 32-bit value. On success copy all twelve payload bytes to record+0x28.
Return the original allocation result, not memcpy's record+0x28 result.
Allocation failure returns null without copying.

The allocator stores its first argument in a field later decremented and
tested for expiry, supporting the `lifetime` name. Its final argument's deeper
meaning remains unproven, so use neutral `parameter`, not speculative flags.
Volatile parameter views retain retail's incoming homes and narrow reloads;
this does not establish the original author's source keywords.

After frame reservation: RA at SP+0x24, payload owner at +0x28, selector at
+0x2C, reserved bytes +0x2D..+0x2F, zero float at +0x30, and saved allocation
result at +0x34. Incoming homes are +0x38/+0x3C/+0x40/+0x44. Preserve the
signed halfword read at +0x3E and unsigned byte read at +0x43.

## Checked Schedule

Derive each replacement from an existing emitted word. The following map is
destination word index <- original word index:

```text
7<-13   8<-7   10<-8   13<-16  14<-17  15<-18  16<-15
17<-19  18<-20 19<-21  20<-22  21<-23  22<-14  23<-10
24<-25  25<-26 26<-24
```

Validate a closed permutation, the allowed non-control operations, every
expected word, complete raw-body hash, extent and both bindings. No register
field is changed. Branches, destinations, calls, return path and argument
values remain intact. Append exactly seventeen CSV rows with its old byte
prefix and line endings unchanged.

Retail hoists the second owner-home read before the null branch and uses a
different argument/payload schedule. Raw C agrees on tested ordinary public
results, but raw access order and private state are not literally identical.
Only guarded C claims the qualified full-state and fired root-fault-prefix
agreement. No portable C fault/MMU, hardware or general concurrency claim.

## Qualification

Tools, identical in both local copies:
`experiments/game_parameterized_selector_payload.py` and
`tests/test_game_parameterized_selector_payload.py`.

| Actual Run | Active Tools | Older Mirror | Errors / Failures / Skips |
| --- | --- | --- | --- |
| Full pre-install suite | 8 tests, 4.284s | 8 tests, 4.086s | 0 / 0 / 0 |
| Fresh installed checks | 2 tests, 1.905s | 2 tests, 1.903s | 0 / 0 / 0 |

Explicitly reuse the other six pre-install checks only under strict source,
raw/padded object, guard, helper/input and complete-image identity. They are
not fresh installed runs. Shared tool checks pass in both copies (0.142/0.103s).
Routine Codex qualification uses zero Claude calls.

- 1,312 guest phases cover every word, all selector bytes, signed lifetime and
  full-word input boundaries, null/failure paths, stack aliases, effectful
  callees, copied reserved bytes and output fences. Another raw execution per
  phase verifies its public contract, not raw private-state/fault identity.
- Native32 O0/O2/O3 each pass 128 selected-body cases with trap UBSan and full
  owner/output fences. Eight effective wrong-C controls cover narrowed
  lifetime, wrong owner byte, nonzero float, short copy, wrong allocation
  argument, changed selector, advanced return and shifted copy destination.
  Native input values are converted to their declared widths; noncanonical
  raw register words belong to guest evidence. Reserved native bytes are
  observed, not assigned a portable initial value.
- Six independent GNU links cover three entry/callee rebases and 24 phases.
  Check 112 fired guarded root-data fault prefixes, nineteen guard corruption
  controls, five strict whole-image corruptions and sixteen saved-result
  phases under adversarial caller-clobbered state.
- Fixture repairs are not production fixes: avoid inherited oracle attribute
  names; retain native noinline/noclone helper boundaries so O3 does not fold
  reserved-byte reads into negative-control bodies. Preserve unspecified native
  padding rather than suppressing warnings broadly or zeroing production data.
- Pin 26 historical inputs and the old padded object. Preserve all five raw/
  padded owner neighbors and pools. Independent GNU assembly agrees with the
  normalized body and bindings. The standard generated-slice Make rule has
  three productive commands, not the five-command GLOBAL_ASM-owner rule.

## Caller Bounds

The aligned retail scan finds one direct JAL at ROM 55310 / VA 15027E60 and
no literal target pointers. This is not proof against constructed targets.

Execute the actual ten-word caller window at 15027E48..15027E70, including
its final branch/delay slot, stopping before fetching 15029BA4. Across 48
phases verify subtraction/sign extension of lifetime, unsigned selector load,
zero final parameter, actual call, discarded leaf result and integer-1 caller
result. The containing func_150265CC remains an unchanged 12-byte production
stub. Earlier dispatch and later stages are not executed.

Allocator and copy effects are explicit hooked contracts in this qualifier,
not full original helper execution. Do not claim complete caller, allocator,
memcpy instruction-level acceptance or natural gameplay from these tests.

## Production

Commit tools first: `15e1f5ac58bc5585cced04444d7f6c84e8d3dff5`. No push.
Preserve all 1,552 prior older-mirror dirty paths, statuses, hashes and HEAD;
add only two task files, leaving 1,554 dirty paths. Do not reset or commit it.

Seal 15,850 files, including all 1,454 linker objects. Normal Make completes
in 0.517s in the verified Linux copy. Mark only the verified target-only guard
append old to avoid unrelated rebuilds. The existing duplicate generated_12D630
recipe warnings remain. Owner diagnostics are unchanged and isolated target
diagnostics are empty; this is not a warning-free clean-from-scratch build.

Every static input and non-target object remains byte-identical. Validate live
bytes before and after promoting only the owner object, ELF, linker script and
progress CSV; linker-script and conversion-CSV bytes remain unchanged. Live
adoption audit: 42.156s.

Reproduce the independent full-ELF prediction with zero exclusions:
**125 changed bytes =124 code bytes +1 target-size metadata byte**.
Preserve all other 6,054 bodies, all 6,055 addresses and all 720 protected
Game-data owners / 189,088 bytes. Protected-data SHA-256:
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.
ELF SHA-256:
`89134335a538fb554c187234e3c8760c25fd89a85470de9abe1fc96ae84a45f0`.
Padded owner SHA-256:
`058ef1f9169f6192d401bd1ee97f560901ce882cc628cb7511e9fe2cdd8cd052`.

## Handoff

The standard matcher against the actual live ELF completes in 33.547s:
total **3,738/5,505 (67.90%)**, Game **3,065/4,832 (63.43%)**,
Init 492/492 and Debugger 181/181 exact. Zero address drift; 1,767 different.
The 75% threshold remains 4,129 exact, requiring **391 more matches**.
Next func_151A4590 is screened only, unmodified and uncredited.
Keep func_1508CAD8's 862-word stub queued.

Root README changes only its two aggregate rows. Detailed updates belong here
and in concise indexes. Post-commit graph-worker and every-old-node audits
remain private receipts; retain excluded-corpus/large-HTML caveats without a
full re-extraction or fresh corpus-membership recount claim.
Frozen host Release remains untouched.
