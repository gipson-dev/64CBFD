# Actor bound burst native/caller qualification and frame map - 2026-11-18

The two complete C recoveries of `func_150B7B40` now pass native32 execution
and the genuine actor-state caller. The preferred draft remains **484 words /
frame0x258**, versus retail **484 words / frame0x268**. It remains **uninstalled
and uncredited** until the complete private-state/register/FP relation and
production gates pass. No source body, guard or build input is adopted here.

Accepted totals remain **4,546 / 5,514 exact (82.44%)**, Game
**3,873 / 4,841 (80.00%)**, Init492/492 and Debugger181/181, zero drift and
968 different. **141 more matches** reach the active85% goal. The root README
is unchanged because its aggregate figures did not change.

Baseline consumer `067560916bea78d5057ab595441939c34d1d86f1`, tools
`4910a4cc456ccf02f41753a45ea015fbdfb1ac2a`. Source/interface/recovery and raw
hashes are in [Note2537](2537-game-actor-bound-burst-parent-recovery-screen-20261118.md).
The private `adoption-native` packet preserves that earlier phase's receipts,
objects and sibling overlay. Both final configurations pass **six tests** with
no errors/skips: **134.336s primary / 142.034s private
sibling overlay**, each fingerprinting **315 imported tool files**.

## Native32 exact transcripts

Both485- and484-word C drafts pass O0/O2/O3: six positive executions, each
with129 cases and4,160 provider calls. Tests use strict aliasing, UBSan,
SSE scalar arithmetic, no-fast-math, contraction disabled and standard excess
precision. Normal finite mapped/aligned execution is the tested domain;
hardware FP exception/fault behavior and arbitrary FP payloads remain separate.

Expected records come from independently executed retail MIPS instructions.
Each native call checks the exact function, argument count, every argument and
initialized observation byte, rather than relying on a transcript hash. The
floor effect includes both F12/F14 arguments. Public actor, model and constant
windows are also compared after execution, with explicit native/guest byte order.
Provider mutations preserve the guest test's actor and retained-object contracts.

The first descriptor compares **112 initialized bytes out of124**; the second
compares **132 out of136**. The12/4 unwritten bytes are not read by the native
comparison. Direction/bounds outputs are initialized before use. Eight compiled
negative sources exit3 because of argument, observation or missing-call errors:
heading, pitch, floor depth, child duration, spray kind, damping, upper clamp
and loop count. These are in addition to the existing eight MIPS source negatives.
Both child particle helpers and other providers remain modeled in this screen.

## Genuine actor-state caller

The complete **252-word `func_1507D754`** is independently GNU-assembled,
bound and verified against ROM and the current production ELF. Its two actual
jump tables select **actor state13**, reaching the real call at **0x1507DA90**.
That call passes the actor, slot255 and context1. Both tables are inside the
freshly audited189,088-byte protected data region; their bytes remain retail.

Retail and the preferred C parent's actual instruction streams each pass128
connected caller cases and4,160 provider calls. Saved GPR/FPR state, public
effects, observations and72 caller-owned frame/incoming bytes agree. The caller
returns zero and ignores the parent's emitted V0. Caller-saved dead temporaries
are not constrained by this ABI check. Other dispatcher states are unclaimed.

Each connected parent stream executes482 words: a valid caller actor cannot
take the null-only RA-load delay at0x150B7B8C. That word is covered in the
standalone129-case fixture. The remaining unvisited duplicate LUI is unreachable,
at0x150B7D60 in retail and0x150B7D5C in this draft. The earlier caller prototype
incorrectly expected the standalone coverage and all dead register values;
those assertions were corrected after both producers exited. The check states the
observable caller contract and separate null-path coverage.

## Measured private-home map for the next proof

The ledger collects own-instruction memory accesses across129 cases in both
streams. Thirteen escaped blocks have stable, disjoint homes. Offsets below are
relative to the function's incoming SP, before its prologue allocation.

| Object | Bytes | C offset from incoming SP | Retail offset from incoming SP |
| --- | ---: | ---: | ---: |
| Endpoint0 | 12 | -24 | -24 |
| Endpoint1 | 12 | -12 | -12 |
| Origin | 12 | -36 | -36 |
| Center | 12 | -192 | -216 |
| Bound A | 12 | -204 | -240 |
| Bound B | 12 | -216 | -252 |
| Height | 4 | -172 | -220 |
| Radius | 4 | -176 | -224 |
| Ratio | 4 | -180 | -228 |
| Floor result | 36 | -252 | -300 |
| Ground probe | 12 | -264 | -312 |
| Child descriptor | 124 | -160 | -180 |
| Spray descriptor | 136 | -400 | -476 |

The two additional radial-offset floats occupy source **[-168,-160)** and retail
**[-204,-196)**. The saved-register/outgoing prefix occupies128 bytes on each
side. These blocks account for528 bytes:128 prefix +392 escaped +8 scalar.
Source objects/scalars form a continuous400-byte upper region; retail spreads
them across476 bytes with gaps. The frame sizes differ by16 bytes overall.

Own instructions touch456 private bytes and incoming bytes4..11 in both finite
screens. The ledger reports144 source and160 retail private bytes unobserved
in those cases. Those counts do **not** prove the gaps unaccessed for arbitrary
state. The next symbolic interpreter must reject every unmapped private access,
relate all passed bytes and saved custody, and account for provider effects,
public aliases, loop state and ordered FP/FCSR before any normalization.

## Preservation and continuation

All **1696 frozen source/build/tool inputs** remain exact,
including all698 production objects and the ELF. Fresh protected-data audit,
tools-check and actual-ELF match-progress pass. Production ELF is unchanged:
`46cfd670adb3a01257e59f77734a12a6ce785c3b2807ce7ceb7b154044ad2ed2`.

The actual sibling tools HEAD,2,434 dirty paths and343 dependencies are preserved.
Its private overlay contains339 sibling files,398 pinned primary fallbacks and
eight task inputs. Seven tools paths change; the existing manifest is unchanged
and still fingerprinted. Host Release, saves and source are untouched. No Claude
call or push is used. Graph refresh retains old IDs with separate native/scoped
receipts and a screen-to-production-stub reference, not full-corpus extraction.

Next prove the opening through the first particle call using the measured
home map, then extend through the floor/descriptor setup and both loop trips.
Resolve the register and FP schedule from the484-word draft. Connect the two
qualified child bodies, derive guards only after the relation passes, exercise
both real padders/rebases and controls, predict the whole image, then use actual
production Make, audit/recount and tools-first commits before awarding a match.
