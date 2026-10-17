# Transition Completion Burst Candidate And Frame Gap

Date: 2026-10-17

Continue consumer **6a0e4173**, tools **791eb66**, after the installed
[fixed transition constructor](1483-fixed-transition-constructor-direct-match-20261017.md).
Recover **func_150CF800** as a complete typed C experiment, but **do not install**
it or claim matching credit. The production placeholder and normal ELF remain
unchanged. This is concrete source/ABI/qualification progress, not a match.

## Retail Contract

- Owner: `conker/src/game/generated_FC5F0.c`; original `conker/asm/FC5F0.s`.
- VA **0x150CF800..0x150CFBEC**, ROM **0xFCCB0..0xFD09C**.
- **251 words / 1,004 bytes / frame 0x108**; interface **s32(u8 *record)**.
- Kind-12 callback at **D_8008ACC8 + 48 = 0x8008ACF8**. The real dispatcher
  `func_15154C90` supplies one record pointer and consumes the returned 1.

Read the state as a **byte at +0x70**, not the reference source's word read.
If bit 0 is clear, return 1 without updating the record. Otherwise advance
the float at +0x74 by the rounded product of **0x3E428F5D** and the timestep.
At progress >= 1, clamp to 1, clear only bit 0, choose **2..5** children and
snapshot the parent's two position floats and its Y+15 floor value.

Each child receives a complete **88-byte descriptor** and a complete
**16-byte, four-float payload**, not the reference draft's undersized scalar
objects. Recover unsigned random remainders 101, 65 and 26; the signed
16-bit direction is -160..-96. Read slot/context as bytes at parent +12/+1.
Call the same **seven-word factory** used by the fixed constructor:
`descriptor, 13, NULL, 0, 16, slot, context`. Attach the payload at +0x70
only on non-null allocation. All random requests still occur on allocation
failure. Resume with the live transition progress/base/delta, update X, call
sinf(progress*pi), and update Y as the rounded product -17.5 plus 72.

The selector table is properly typed **u8 (*D_8008FCD0[])(void)**. Entry 2
is the actual three-word `func_151D8EBC`, returning 29; the alternate entry
used by mutation tests is `func_151D8EB0`, returning 117. Do not misdeclare
the table as a struct containing a signed-word callback.

## Compiler Recovery

`tools/experiments/game_transition_completion_burst.py` retains the complete
candidate, checked raw words/bindings and a strict uninstalled-only screen.
No production source, Makefile, profile or instruction guard changes.

The selected candidate emits **251 words**, but **93 still differ** and its
frame is **0x118**, not retail's **0x108**. Retail keeps the parent in S4 and
the payload pointer in S3; C reverses those roles. The opening progress
accesses fold to parent+0x74 rather than the retail derived pointer. Header
store scheduling, the first random-flag branch, loop/tail reload scheduling
and local object homes also remain different. These are not all independent
instruction reorderings and are not authorized for guard normalization.

Measured source screens in ignored `conker/build/game-transition-burst/`:

| Form | Words | Frame | Different Words |
| --- | ---: | ---: | ---: |
| Initial typed complete body | 246 | 0x120 | 250 |
| Named global captures and real float multiplier locals | 251 | 0x130 | 109 |
| Retail float literals, two multiplier locals | 251 | 0x118 | 96 |
| Ascending fixed-header initialization, selected | 251 | 0x118 | 93 |
| Direct literal multiply by 2, no multiplier locals | 246 | 0x108 | 248 |

The last form recovers the frame but strength-reduces multiplication to
addition and loses the retail six-pair FP save/constant setup. It is not an
improvement sufficient for installation. Pointer/record views, register hints,
lexical scopes, common flag/random carriers, chained scale assignment and
left/right literal multiplication do not close the match. A joined aggregate
and packed form overflow the slot and are rejected. A no-g3 diagnostic does
not recover the normal-profile match. Do not repeat or adopt failed -g0
asm-processor options. There is no dependency or compiler configuration change.

The literal pool is exactly the six retail float words at **0x245320..0x245338**:
`3E428F5D 3FD99999 3FE51EB8 3ECED917 3EAA7EFA 40490FDB`.
The compact object adds eight section-alignment zero bytes; those are not
claimed to be the following retail constants. A private link script and the
existing padder's rodata-symbol option map only the experiment. Both linked
candidate bodies are identical; all **24 raw/padded owner neighbors** remain
unchanged. A production rodata mapping is still an open installation gate.

Raw target SHA-256:
`7078b69bf81d2546d26b134ae2a7e48cf1763e36b53029102e13469467ed7940`.
All **31 bindings**, all 251 words, the pool and immutable inputs are pinned.
The tool refuses installation even if a caller changes a summary row to zero.

## Qualification And Limits

All **six final tests pass in 21.605s**. There are **2,304 three-way public
cases**, **128 three-way original caller-window cases**, four effective
full-source controls, **251 word controls**, **31 binding controls**, and
**376 positively fired live/fixture input controls** across **188 protected
entries / 172 distinct paths**. The original paths naturally visit **249 of
251 words**; the two divide-by-zero BREAK words are not executed. This is
coverage of the original routine, not a claim that the C words match it.

The bounded finite-value guest reference compares public bytes and ordered calls across
**2,304 original/raw-C/padded-C cases**. Cases cover inactive/active/high-bit
state bytes, partial/completing progress, negative/positive timestep, all
child counts, both stack phases, all/none/alternating allocation outcomes,
volatile helper clobbers, mutable parent fields and a changed tag callback.

Execute the actual **54-word factory**, **11-word SDK memcpy**, and both
three-word tag leaves. RNG, direction outputs, sine and the lower allocator
remain explicitly scripted boundaries. A live-padding mode overwrites the
six descriptor representation bytes before the actual copy and compares
them too; otherwise exclude only those six bytes from public comparisons.
All sixteen payload bytes are initialized and compared. This does not prove
native padding behavior, private stack state, real allocation, libm accuracy,
CP0/FCSR, hardware timing or natural gameplay.

The original **eleven-word callback window**, **0x15154CE8..0x15154D14**,
supplies the one pointer through the kind-12 table, saves/restores that
pointer, executes the success-return branch and its signed-byte delay-slot
load. Its cases do not qualify the entire dispatcher, timer or deletion path.

Four full-source negative controls must fail public reference: word-sized
state gate, word-sized slot read, too few children and a 15-byte payload copy.
The real input gates reject injected corruption in every live input and
frozen fixture; re-read live inputs after caches/mocks are removed. Candidate
word/binding guards are validation only, not output instruction patches.

Native32, independent relocation rebases, exhaustive access-fault/private
state, complete caller and first-whole-image prediction remain open. In
particular, public agreement cannot certify the differently sized frame.

## Resume

```sh
python3 -m tools.experiments.game_transition_completion_burst
python3 -m unittest tools.tests.test_game_transition_completion_burst -v
make tools-check
make -C conker match-progress NON_MATCHING=1
```

- [x] Audit the complete retail body, correct byte/float widths and callback ABI.
- [x] Recover complete descriptor/payload objects and a reproducible C candidate.
- [x] Verify the retail literal pool, 24 preserved neighbors and bounded public behavior.
- [ ] Recover all **251 words and frame 0x108**, with the real register and local-object lifetimes.
- [ ] Close native, relocation, fault/private, caller and first-image gates before installation.
- [ ] Keep wider Game matching, deferred fade/pulse/renderer work and gameplay open.

Production remains the installed Note 1483 baseline: owner SHA-256
`645d71e6cf77a1f7f2940e27c983c0c79a53f0ca9d292a15d296b6bf56dcf328`,
ELF `9ff7f89b5a621b216a65e6018c4df1485c18cb4c4e92485bb5c94c53eb3592b4`.
No additional converted/exact function is credited. Root README stays unchanged.
No host-port/frozen Release build, agent call, provider/dependency change or push.

## Bank And Fresh Aggregate

Tools **f36356e** banks the three new candidate/oracle/test files first.
Three task pairs are byte-identical in both tools copies; all **six ASCII/AST
parses** pass. Eleven shared padder checks pass in the active checkout
**0.054s**, and in the mirror **0.019s + 0.030s**. Consumer tools-check passes.
The separate mirror retains HEAD **ddbdd16b** and all **1,053 initial dirty-file
hashes**, adding only the three task files for **1,056 dirty paths**. No mirror
commit, reset, push or unrelated rewrite. The existing duplicate Makefile
recipe warnings remain.

Fresh official matching is unchanged: Game **2,950/4,828 (61.10%)**, total
**3,623/5,501 (65.86%)**, **1,878** different, zero address drift; Init
**492/492**, Debugger **181/181** exact. Existing broader renderer/compiler
suites are prior evidence, not fresh tests. They are not rerun merely for
this uninstalled candidate. Native and installation qualification remains
explicitly outstanding.
