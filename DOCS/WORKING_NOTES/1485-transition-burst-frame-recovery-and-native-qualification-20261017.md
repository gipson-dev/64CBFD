# Transition Burst Frame Recovery And Native Qualification

Date: 2026-10-17

Continue consumer **aee47553**, tools **f36356e**, from
[Note 1484](1484-transition-completion-burst-candidate-and-frame-gap-20261017.md).
Recover **func_150CF800's 251-word length and retail frame 0x108** without
instruction guards, fake padding, compiler/profile changes or production edits.
It remains **uninstalled at 91 word differences**. Equal length and frame are
not full instruction, private-state or installation acceptance.

## Recovered Lifetimes

The previous complete typed candidate used frame 0x118 and differed at 93 words.
Three ordinary source changes recover the real frame:

1. The first flag holds only 0 or 2, so represent it with a byte-sized type.
2. After the transition completes, reuse the no-longer-needed progress
   temporary for the child speed range 2.0f. Reload the live transition
   progress after the children, retaining callback mutation behavior.
3. Assign the common child scale directly to both descriptor components;
   there is no need for another named scale temporary.

Use the literal 2.5f bias directly. The checked float pool remains the exact
six retail words from Note 1484, with no new or changed constant values.
The source comment explains the disjoint progress/speed-range lifetime.
The full 88-byte descriptor and 16-byte payload stay intact. No trailing
filler, initialized padding, volatile operation or additional call is used.
These are qualified reconstructed source forms, not proof of the original
source spelling or declarations.

The reproducible recipe is in
`tools/experiments/game_transition_frame_lifetimes.py`, based on the pinned
complete predecessor rather than another copied, diverging function draft.
The original screen and its six tests remain preserved as prior evidence.
Selected raw target SHA-256:
`2f9a5a88cf77008fb30b41025da490690fe3b135b3e9e761a8b41c8fae9d421b`.
All 31 bindings are unchanged. Raw and normally padded candidate words agree;
all **24 raw/padded owner neighbors** remain unchanged. There are **zero new
instruction guards**. Installation is still explicitly refused.

## Actual Compiler Evidence

Reuse the existing fingerprint-locked CFE/UOPT/UGEN capture in newly owned
compiler children. Both retained captures fire, complete their real producer/
consumer/driver lifetimes, remove their probes and reproduce the normal
whole-owner text/function/relocation/pool inventory. No attached game process,
compiler modification, provider setup or dependency installation is involved.

The target's actual CFE records show:

| Measurement | Previous | Selected |
| --- | ---: | ---: |
| Automatic storage DEF M | 144 bytes | 128 bytes |
| Compiler-created float temporary | M-144 | M-128 |
| Its VREG annotation | R / 4 bytes / level 1 | R / 4 bytes / level 1 |
| Emitted frame | 0x118 | **0x108** |
| Words | 251 | **251** |
| Different words | 93 | **91** |

VREG is a frontend annotation, not a claim of a particular saved register.
Suppressed compiler real-number diagnostics are not timing evidence. Additional
diagnostic-only captures in ignored `conker/build/game-transition-frame-lifetimes/`
also establish the intermediate 136-byte automatic region / frame 0x110.

Renaming the descriptor or payload, byte/struct output representations and an integer
pointer round trip do not repair register ownership. Explicit else/conditional
forms for the byte flag emit 252 words and are rejected. A staged scale update
gets the frame but worsens the instruction differences. These are not installable
alternatives and no compiler/build flags are changed to accommodate them.

## Public And Native Qualification

All **seven final tests pass in 53.736s**. Freshly rerun predecessor/context
checks pass **six tests in 24.634s**. Candidate identity controls positively
fire for all **251 words / 31 bindings**, and for **386 live/fixture mutations**
across **193 protected entries / 177 distinct paths**. Remove the caches/mocks
and re-read all live inputs afterwards; no stale fixture is accepted.

The independent finite-value guest reference now covers **2,688 three-way
original/raw-C/padded-C cases**, adding high-bit and all-ones RNG seeds to the
previous corpus. Preserve the actual 54-word factory, eleven-word SDK copy
and both three-word tag leaves. Keep RNG, direction outputs, sine and the
lower allocator explicitly scripted. Public bytes, call order, clobbers,
null/alternating allocations, mutable parent/selector state and live copied
padding agree. The original naturally visits 249 words; its two divide-by-zero
BREAK words remain unexecuted.

The complete C body and a separately compiled, properly typed one-pointer
caller pass native32 **O2 and O0, 1,728 cases per profile**, with UBSan.
Check the 82 initialized descriptor bytes, all sixteen payload bytes, factory
kind and argument values, all parent fields and outer/output canaries.
Exclude only the descriptor's six inherited representation bytes. Inputs are
actual typed Record/position/transition objects, not float pointers into
misaligned byte buffers. This is prepared native32 finite-value evidence,
not portable padding, N64 FCSR/NaN behavior or hardware acceptance.

Four effective native source controls exit **22**, not a sanitizer signal:
too few children, a short payload copy, the wrong speed bias and a stale
post-callback progress value. Two other controls intentionally **pass native**:
word-sized state and slot reads. On this little-endian native32 target their
low bytes agree, but their actual emitted big-endian N64 routines fail the
independent guest reference. Do not treat native-only success as a byte-width
or matching certificate. Preserve these positive endian-limit demonstrations.

The original eleven-word kind-12 caller window still passes **128 three-way
cases** with the pointer restore and success-return branch/delay load. It
does not qualify the entire dispatcher, timer, deletion path or real gameplay.
All live/frozen input gates and candidate word/binding guards are tested;
the guards validate input identity, not patch output instructions.

## Remaining Match

The frame is fixed, but these measured differences remain:

- Parent S3 / output-pointer S4 versus retail's S4 / S3.
- Descriptor at **SP+0xB0** and payload at **SP+0xA0**, still four bytes above
  retail's **SP+0xAC / SP+0x9C**, despite the same frame size.
- Opening progress accesses folded to parent+0x74, rather than the retail
  derived transition pointer, plus its branch-delay delta load.
- First flag zero hoisted into an earlier RNG delay slot, rather than the
  post-call branch. That branch is one word shorter than retail.
- A compensating extra tail address recomputation and different pointer
  reload ownership. Equal total length hides these opposing differences.
- Header/scale store and temporary-register scheduling.

Do not add a dummy field or shift copied objects with arbitrary expected-word
replacements to claim success. Recover the real object/register lifetimes,
then close independent relocation, exhaustive private/access-fault, complete
caller and first-whole-image gates before installation. Natural gameplay and
the broader Game/fade/pulse/renderer queue remain open.

Prepared-checkout commands:

```sh
python3 -m tools.experiments.game_transition_frame_lifetimes
python3 -m tools.experiments.game_transition_frame_lifetimes --capture
python3 -m unittest tools.tests.test_game_transition_frame_lifetimes -v
make tools-check
make -C conker match-progress NON_MATCHING=1
```

- [x] Recover the complete 251-word C candidate with the retail 0x108 frame.
- [x] Capture the actual frontend home reduction with unchanged emitted objects.
- [x] Qualify bounded guest/native behavior, caller window and effective controls.
- [ ] Close all 91 word differences and actual object/register lifetimes.
- [ ] Close remaining relocation/private/fault/caller/image gates, then install.
- [ ] Continue the wider Game matching objective; this is not its completion.

Production source, normal ELF, manifests, data, profiles and root README remain
the Note 1483 baseline. No matching/converted-function credit is added here.
No host-port/frozen Release action, extra agent, provider/dependency change or push.

## Bank And Aggregate

Tools **5a038ed** banks the three new frame/native/test files first. Three
exact task pairs / **six ASCII/AST parses** pass in both tools copies. Eleven
shared padder checks pass in the active checkout **0.055s**, and in the mirror
**0.022s + 0.037s**. Consumer tools-check passes. Preserve mirror HEAD
**ddbdd16b** and all **1,056 initial dirty-file hashes**; add only the three
task files, yielding **1,059 dirty paths**. No mirror commit, reset or push.

Fresh official matching remains Game **2,950/4,828 (61.10%)**, total
**3,623/5,501 (65.86%)**, **1,878** different, zero address drift. Init
**492/492**, Debugger **181/181** remain exact. Normal ELF SHA-256 stays
`9ff7f89b5a621b216a65e6018c4df1485c18cb4c4e92485bb5c94c53eb3592b4`;
owner-source SHA-256 stays
`645d71e6cf77a1f7f2940e27c983c0c79a53f0ca9d292a15d296b6bf56dcf328`.
No root README or production build change. Existing duplicate Makefile recipe
warnings remain. Unchanged broader renderer/compiler suites are prior, not
fresh evidence, and are not rerun merely for this uninstalled candidate.
