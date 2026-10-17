# Dual Buffer Fade Candidate And Private Payload Gap

Date: 2026-10-17

Continue consumer **76ae6be1**, tools **fed3c57**, from
[Note 1489](1489-game-link-event-callback-match-20261017.md).
Target **func_150D01A0**, VA **150D01A0..150D02B4**, ROM **FD650..FD764**,
**69 words / frame 0x30**, in generated_FC5F0.c. A complete semantic candidate
is qualified for bounded public behavior but **remains uninstalled**: it emits
**65 words / frame 0x30**, keeps the wrong saved role/private homes, and fails
an actual variadic-helper payload comparison. No guard, conversion or matching
credit is added. This is progress on the broader Game goal, not its completion.

## Interface And Recovered Semantics

The actual table **D_800888A0[0]** points to this routine. Execute the complete
35-word **func_150D0034** caller: the callback takes one record pointer and
returns **s32 1**, retaining the caller's cursor and allowing its flag clear.
Keep proper color **void(u8,u8,u8,u8)** and text-command
**void(s32,s32,u8,s32,...)** declarations. The alternate auto-decompiled source
has incorrect word reads for the flag/index bytes; no alternate code is adopted.

Record+0x48 holds a pointer to a **signed countdown byte**. A low bit at
record+0x30 resets it to eight. Positive values produce a previous-buffer
weight **(count * 31) & 255** and a current-buffer weight **255 - oldWeight**;
the counter then subtracts the live 32-bit clock and stores its low byte.
Nonpositive signed bytes retain weights zero/255 without loading the clock.
Use an unsigned clock subtraction before narrowing so the prepared native32
checks do not introduce signed-overflow UB for extreme clock words. This
change emits the identical IDO instructions and bindings.

Each nonzero weight calls color(206,196,97,weight), then text(146,190,129,
selectedBuffer). Read the live index byte at record+0x3D **after** the color
call; the previous-buffer window uses **index ^ 1**. Preserve the buffer-base
pointer lifetime across the second color call. Guest checks include the full
byte-index domain beyond the bounded two-buffer native struct, countdown
aliases with flags/index/buffer/pointer/clock bytes, and callback mutations.

## Measured Lifetime Gap

The normal candidate's complete 260-byte raw function SHA-256 is:
`e0058c9fb6336f0c05c7eac7b85bc0ba35b0f5307850d6aa4886b97763c942a7`.
All six bindings are fixed: clock HI16/LO16 at **+0x38/+0x44**, color JALs
at **+0x78/+0xBC**, and text JALs at **+0x98/+0xE4**.

Retail saves **previousWeight in S0**, keeps **record at SP+0x30**, and saves
the second-window subrecord pointer at **SP+0x20**. The candidate instead
keeps **record in S0** and spills previousWeight at **SP+0x24**. Frame equality
does not establish these identities. The complete raw and padded candidate
bodies agree with each other, not with the 69-word retail routine. All **24
raw/padded owner neighbors** and all owner pools/data remain unchanged.

Do not pad away the gap or describe it as two independent scheduling words.
The installation admission helper rejects both the current extent and any
attempt to substitute literal retail words without the outstanding private,
caller, fault and full-image gates. Production retains its existing stub.

## Actual Helper Counterexample

Execute the original **22-word color leaf** and **42-word text wrapper**,
not merely scripted first-four-argument providers. The latter copies **sixteen
caller-stack words** to its private array before calling func_15042ECC.
Capture that actual copied array at the consumer boundary; do not execute or
invent the unfinished text consumer.

All six tested countdown cases produce the same ordinary helper arguments
and success return, but different copied payloads. For count one, the current
candidate's word **5** exposes its spilled previousWeight **31** at SP+0x24;
word **8** lacks retail's record argument-home value **0x20000** at SP+0x30.
On the second text call, word **4** also lacks retail's state pointer
**0x20028** at SP+0x20. Inherited stack bytes are modeled explicitly rather
than silently zeroed or excluded. This is a positively observed private-ABI
gap, not a claim that the displayed text or hardware rendering differs.

The actual wrapper runs to completion in both versions. Its downstream text
consumer, final presentation, portable C missing-varargs semantics, complete
private register/access-fault parity and a full installation prediction remain
unqualified. Native stubs deliberately read no missing variadic arguments.

## Discriminating Screens And Advisory

Six committed screens reproduce:

| Source/profile | Words | Frame | Result |
| --- | ---: | ---: | --- |
| Normal O2/g3 | 65 | 0x30 | S0=record; old weight at SP+0x24 |
| O2 without g3 | 64 | 0x30 | Still wrong lifetimes |
| O1/g3 | 74 | 0x30 | Automatic locals spill; no retail S0 role |
| Explicit positive/else weight assignments | 64 | 0x30 | Recovers redundant join branch, not homes |
| Same with register previousWeight | 64 | 0x30 | Identical full raw function/bindings |
| Staged shift/subtract/weight mask | 63 | 0x30 | Does not recover S0 or argument home |

Additional ignored probes rejected O1 with all register locals (76 words,
frame0x48), O2/g2 (87 words, optimization-disabled warning), byte-weight and
typed-buffer variations, and volatile parameter/snapshot forms. These are
diagnostic source experiments, not recovered volatile declarations or an
approved compiler-profile change. The generic asm-processor rejects O1/g3;
the committed pure-C screen retains normal preprocessing and changes only the
owned compiler child's flags, matching the existing function-override pattern.

One bounded Claude invocation uses print/safe mode, no tools, strict MCP,
no persistence and the configured default model/auth selection unchanged.
Its single response recommends staging the weight calculation to change the
allocation priority. The real IDO test above **falsifies** that prediction:
63 words and S0 still holds record. No supported correction is accepted, and
there is no automatic second advisory call. Its semantic agreement does not
override the actual sixteen-word payload counterexample.

Ignored request SHA-256:
`88989e155ef163a18690d4d5d88856bcc4dc4b88911fea84e67bc00c366af265`.
Ignored response SHA-256:
`3605a2d1a6924c2136294b4dc60c3ef53484a1d6b588a47f54a135be9fa9e1be`.
The receipt records one completed analysis turn and zero web requests. No
provider, account, model setting, billing setting or dependency is changed.

## Qualification And Bank

All **eight tests pass in 34.140s**, without skips:

- **9,216 three-way public-memory/helper-call/return cases**, nine alias
  placements, four mutation modes, two stack phases and all 69 original words.
- **Nine independent original/raw/padded links**, three symbol sets,
  signed-low carries, all six bindings and **144 three-way public cases**.
- The **complete 35-word actual caller**, table slot zero, **256 three-way
  public cases**, bypass and active callback paths, and the success contract.
- Prepared native32 O2/O0 + UBSan, **6,144 cases per profile**, separately
  compiled complete body/typed caller and **six effective negative controls**.
- **Six actual-helper private counterexamples**, all 16 copied words retained.
- **65 raw-word / six binding corruption controls**, **207 protected inputs /
  190 distinct paths / 414 live/frozen corruption controls**, six profile screens
  and explicit non-installability checks.

The signed-byte oracle initially lacked LB. Reuse the established local
LBU-plus-sign-extension adapter pattern; do not change the shared interpreter
or misclassify an unsupported test opcode as a production defect. Full
private/fault, consumer, presentation, hardware and gameplay gates stay open.

Tools **7960b37** commits the two new qualification files first. Eleven shared
tests pass in the active checkout (0.054s), and in the mirror (six in 0.039s,
five in 0.022s); tools-check and four ASCII/AST parses pass. Both task pairs
are identical. Preserve mirror HEAD **ddbdd16b** and **all 1,076 initial dirty
hashes**, resulting in **1,078 dirty paths** after two new files. No mirror
commit/reset/push. Earlier installed-neighbor suite receipts are reused only
with their input fingerprints unchanged, not reported as fresh broad tests.

The production source, normal ELF, guard history, Makefile and regenerated
progress CSV retain their exact input fingerprints. No production build is
needed for uninstalled experiments. Fresh official matching remains Game
**2,953/4,828 (61.16%)**, total **3,626/5,501 (65.92%)**, **1,875** different,
zero drift; Init **492/492**, Debugger **181/181**. Root README is unchanged.

- [x] Recover the complete candidate and proper one-pointer/helper interfaces.
- [x] Qualify public behavior, aliases, actual caller, native and rebased code.
- [x] Demonstrate the actual sixteen-word payload gap; reject unsupported fixes.
- [x] Bank tools and the precise handoff without production or matching credit.
- [x] Inspect formal-argument exposure and allocation constraints in owned
  normal/branch captures; recover the real argument home in Note 1491.
- [ ] Complete S0/RA/subrecord homes while retaining the qualified parameter
  home. Note 1491 isolates the remaining caller-save/callee-save decision.
- [ ] Require complete private/helper-payload/fault parity and the first full
  linked-image prediction before installing. Keep the broader Game goal open.

No host-port or frozen Release action, push or unrelated cleanup.

```sh
python3 -m tools.experiments.game_dual_buffer_fade
python3 -m tools.experiments.game_dual_buffer_fade --profiles
python3 -m unittest tools.tests.test_game_dual_buffer_fade -v
make -C conker match-progress NON_MATCHING=1
make tools-check
```
