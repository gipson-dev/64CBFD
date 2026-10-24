# Linked Owner Retirement Guarded C Match

Date: 2026-10-24. Consumer predecessor `56a2c05b`; tools predecessor
`a0858ab7`. Qualification tools committed first as
`d8ec960713ca0daedcc8833f10bf571154bdc74a`. No push requested/performed.

## Recovered Routine

`func_151A4ECC`, owner `conker/src/game/generated_1D0840.c`:
VA `0x151A4ECC..0x151A4F7C`, ROM `0x1D237C..0x1D242C`.

Complete semantic C emits 44 words/frame 32/one binding. Forty-two words
already match; two checked Boolean spill words produce the full byte-exact
retail body. This is guarded C, not compiler-only. No relocation moves,
branch changes, inserted/omitted instructions or profile changes.

Raw C SHA-256:
`20f50e01826db3824f9a83db98c5bc7ac8817685cc000254b03119101fa9e457`.
Resolved/retail SHA-256:
`1ccb298785c6746a86f2c60c85e36e5ce8547b880b9e4413b0876c9b6b5d4134`.

Use the actual `void(struct260 *)` update-callback interface. Reuse the
owner's local `PayloadOwnerLink` view at +0x28. Mark failure if the linked
owner's first word is zero or its identity byte +0x3B differs from link+4.
Both checks execute, even after the first failure.

If still valid, linked-owner word +0x1D4 must be nonzero and the low nibble
of linked-owner byte +0x74 must differ from 0xF before calling
`func_151A3504(link, rootByte0C)`. Ignore that helper's return and mark
failure. Failure sets the late root's signed lifetime +0xE to -1 and ORs
bit zero into byte +0xD. Preserve other bytes and post-helper flag reloads.

## Checked Spill Fit

| Offset | Expected C Word | Retail Word | Meaning |
| --- | --- | --- | --- |
| `0x070` | `AFA30018` | `A3A3001B` | Word store becomes low-byte Boolean store |
| `0x07C` | `8FA30018` | `93A3001B` | Word reload becomes unsigned-byte Boolean reload |

The semantic flag is only zero or one. IDO's ordinary s32 local spills a
word at SP+0x18; retail spills the byte at SP+0x1B. Changing the source local
to u8 did not reproduce the original frame/register lifetime. Keep the
complete C body and guard exactly the two measured words.

The binding at +0x74 remains `R_MIPS_26:func_151A3504`. Check the entire raw
body hash, size and binding map before normalization, not only the two words.
Guard append preserves every old CSV byte and adds exactly two rows with no
relocations. Existing CRLF bytes remain intact; no line-ending cleanup is
mixed into the recovery.

Raw C agrees on ordinary public behavior, but not complete guest private RAM
or fault schedules. A deliberately modified private spill demonstrates that
distinction: raw word reload can observe upper bytes that retail never reads.
Only the guarded body claims literal private-state and fault-prefix equality.
No portable native C guarantee is inferred from guest private-home aliases.

## Caller And Helper Boundaries

The sole aligned literal reference is slot ten in the 98-entry
`D_8008A4E8` table, ROM `0x22EFA8`, pointer slot `0x8008A510`.
There are no aligned direct target JALs.

The actual parent is `func_15149264`, 45 words/frame 24, in
`conker/src/game/done/game_1765E0.c`. It optionally decrements signed
lifetime, invokes the signed update selector unless -1, reloads lifetime,
optionally calls the destructor selector, reloads again and releases a still
expired record. Qualify every parent word across 216 guest phases, including
the actual target path, selector-disable sentinel and non-sentinel destructor
paths. Other callbacks/release services remain bounded. The complete parent
source and object are unchanged.

Retail `func_151A3504` is a 70-word/frame-168 factory taking a descriptor
and byte selector and returning a created pointer. Its first copy is 48 bytes;
a non-NULL created result receives an 80-byte payload copy. Preserve descriptor
holes and helper-failure paths. Execute all original helper words in 33
bounded phases, including the standalone NULL-descriptor-owner path.

Its current live C body remains the existing zero-return placeholder with
an unrecovered declaration. Neither source, emitted placeholder bytes nor
matching credit for that helper is changed. Adding formal parameters altered
its code size in a private experiment, so that ABI/body recovery remains a
separate task. Isolated/native callback fixtures use the observed retail
pointer/byte interface; their return is ignored as in the original caller.
Do not claim full native closure through the legacy placeholder or a working
live asset factory from this callback match.

## Focused Qualification

Both tools copies pass eight fresh checks before and after installation,
zero errors/failures/skips, no reused checks. Pre-install primary/mirror:
25.809s / 25.830s; installed: 27.422s / 26.873s.
Both shared tools checks exit zero.

- 8,384 guest phases cover liveness, identity, capability, every state byte,
  helper mutations, late incoming-home changes, four owner layouts and two
  stack phases. All 44 root words are visited. 8,192 raw/public comparisons
  pass; a private-spill counterexample is retained rather than hidden.
- Native32 O0/O2/O3 with trap UBSan: 65,536 selected calls per optimization,
  full typed root/link/actor storage, opaque bytes/fences and eleven effective
  defined wrong-C controls. Cover ignored NULL/non-NULL helper returns.
- The actual C-parent body receives 21,384 native boundary cases per
  optimization and three effective controls. Use complete typed parent
  headers and callback/release probes, not an undersized header object or
  a claim of full native parent/callee factory execution.
- Original factory execution preserves all copied/reserved bytes, creation
  failure and optional position output; memcpy/position/create providers
  are explicitly bounded. Current live helper acceptance is not claimed.
- Nine independent GNU links compare original, qualified padded and actual
  Make objects. 240 phases independently rebase root/helper addresses.
  All 642 literal root-access prefixes fire with equal state, PC and delay
  origin. Seven raw-normalizer and nine strict-image controls are rejected.

The native staging runner initially imported an unavailable YAML dependency.
It was corrected to validate the sealed CSV with standard-library structured
parsing and promote only its exact append-only output. No dependency/provider
installation, source relaxation or historical-input rewrite bypassed a gate.

## Production And Preservation

Preserve all 22 raw/padded neighbors and owner pools, including the unchanged
factory stub. The actual five-command asm-processor/padder Make recipe uses
normal O2/g3 and emits the qualified object byte-for-byte. Compiler diagnostics
are empty; inherited duplicate-recipe warnings remain unchanged.
Production Make exits zero in 0.612s.

Independent and production full links reproduce exactly 117 changed ELF bytes:
116 target-code bytes plus one symbol-size byte, zero exclusions. Symbol size
advances from 12 to 176. All other 6,054 bodies, all 6,055 addresses and the
complete caller object are fixed. Protected Game data remains exact across
720 owners / 189,088 bytes, SHA-256:
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

Result ELF SHA-256:
`d17262679d4a53f6f0621bf2dddd7b072f121850af56383f9bd670c0676e69f5`.
Target object SHA-256:
`fe6383674607f59c5e6153eff10ec4a78c526dc3c4e122a6507c37f6a073f056`.

Seal 15,926 files / 28 focused inputs / all 1,454 linker objects. Fresh native
capture, verified Linux cache and before/after live-adoption audits permit
only source/guard CSV/target object/ELF changes. Use native stdin and checked
tar, not DrvFS project reads. Preserve all 1,590 prior older-mirror dirty
paths/statuses/hashes and HEAD; add only the two task files.
Host Release, saves/configuration and unrelated processes are untouched.

## Recount And Handoff

Actual adopted Windows ELF bytes equal the independent and production images.
Fresh standard matcher exits zero in 1.359s:

| Section | Exact C Functions | Address Drift | Still Different |
| --- | --- | --- | --- |
| Total | 3,762 / 5,505 (68.34%) | 0 | 1,743 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 3,089 / 4,832 (63.93%) | 0 | 1,743 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

Denominator unchanged. Remove only this callback from the ELF-pinned queue:
1,612 placeholders, 122 semantic/other definitions and nine parser-unlocated
entries remain. The active 75% goal still needs 4,129 exact functions,
367 more. Do not credit the helper or private next-function screens.

Keep `func_1510D8C0` / `func_1518C850` triage and the remaining 44-word
queue open; preserve the separate 862-word `func_1508CAD8` owner stub.
Root README gets two aggregate rows only. Bank ten scoped consumer paths,
then audit the normal Graphify hook: all 43,883 old nodes retained/uniquely
relocated and all eight changed C/Markdown hashes, mtimes and memberships
verified. Do not forge a missing stamp or claim full corpus re-extraction.
