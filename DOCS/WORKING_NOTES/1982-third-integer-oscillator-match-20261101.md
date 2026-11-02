# 1982 - Third embedded integer oscillator recovered as guarded C

Verified 2026-11-01. Production **4,049/5,507 (73.52%)**, Game
**3,376/4,834 (69.84%)**, Init 492/492 and Debugger 181/181. Zero address
drift, 1,458 different; **82** more exact C functions are needed to reach
4,131/5,507 and 75%. One new match, unchanged C inventory.

## Recovery and independent reuse boundary

`func_150C673C`, generated_F3BA0.c, VA150C673C..150C682C, ROMF3BEC..F3CDC,
is the third and final literal copy of the complete 60-word integer oscillator
in the ROM. The other copies are F32BC and1D8540, recovered in [Note1981](1981-embedded-integer-oscillator-pair-match-20261101.md).
The new function remains 60 words with a40-byte frame. Its semantic C, types,
raw payload, four relocation bindings and private spill lifetimes are identical
apart from the function identifier. It replaces the zero-return placeholder.
The original assembly-backed cleanup `func_150C682C` remains intact.

Capture the notification before clearing it, narrow the wrapping countdown to
s16 before testing, call integer RNG before live range/minimum reads, then
call floating RNG before amplitude/base reads. Preserve binary32 subtraction,
multiplication and truncation followed by modulo32-bit rate addition. The
separate provider statements and target-field temporary are retained; IDO
emits the single final target store. Do not return to nested expressions:
GCC provider-mutation witnesses in Note1981 reject premature range evaluation.
The ordinary qualified domain excludes volatile/concurrent field observers,
private-stack aliasing and nonfinite/out-of-range float-to-integer casts.

Six append-only expected-word guards close the same two private stack lifetimes:
word SP+18 to SP+1C at offsets44/54/90, byte SP+23 to SP+27 at50/5C/98.
The raw payload SHA256 is
`011ba6f3f9cb1f60d7823aa80c3fc75fb5f2cf2d68576ac95086f88df745957f`.
No inserted instructions, frame change, register rewrite, padding compensation
or functional patch. Complete original and normalized C words/bindings agree.
Three independent GNU links verify the target address, clock low-half carries
and both provider calls. The original function was independently assembled.

## Fresh checks versus fingerprinted prior evidence

Fresh guest checks execute this function at all three layouts:
5,214 cases /15,642 executions across the1,738-case corpus. All59 reachable
words execute; break7 is retained as a structural zero-divisor boundary.
93 access-prefix triples and6 pre-DIVU zero-divisor triples agree across
original, raw C and normalized C. Full modeled state and private-stack write
projection include subsequent caller cleanup reuse. Hardware divide-zero HI/LO,
FCSR and portable C fault semantics are not claimed.

Fresh original RNG integration executes all18+25 helper words across216 cases
/648 executions. Helpers and floating scale37800080 match the current ELF and
retail ROM. An independent64-bit seed recurrence agrees.

Native O0/O2/O3 evidence is **explicit fingerprinted reuse**, not fresh execution.
The entire selected source equals the previously qualified source after only
renaming the function; headers, native harness, corpus, providers and result
receipt are frozen and checked. The prior run covered818 cases per target per
profile with UBSan, untouched owner bytes/fences and nine effective controls.
Both emitted raw payload and ABI are identical. No shared oracle or previous
qualification module was modified to obtain this reuse.

The callback has no direct JAL sites. The complete aligned-ROM census finds
one literal at22E754, slot9 of the14-entry80089C70 table. Cleanup is slot3 of
80089CA8. Fresh original188-word `func_1513C060` dispatch executes89 words in
the bounded no-fade/no-animation-wrap domain.1,536 cases /4,608 executions
cover active/timer/notification gates, scripted cleanup refusal/acceptance and
the original17-word cleanup, all instructions executed. Two zero-return-stub
witnesses are rejected. Release/detach lower providers are scripted. The
parent's production body remains a12-byte stub; full-parent/gameplay parity
is not claimed.

## Build and linked-image gates

All nine raw and padded neighbors, existing constant pools, and zero compiler
diagnostics are preserved. Five actual Make commands reproduce the independently
generated padded owner. Use generated-slice padding with F3BA0.s.

A literal entire-ELF prediction replaces only this240-byte retail slot and
updates its symbol size12->240. Actual private and production ELF equal it:
`50a5fd84eaff7f7f4bb61300e1ff9200987ba37e6fc4a6fcde83140f71748416`.
All6,052 function addresses,6,051 other bodies, entire named definitions,
map and189,088 protected data bytes across720 owners remain fixed. Zero
exclusions and no metadata permutation adjustments.

Both tools copies pass five focused methods and shared checks before adoption.
Two installed compile/image checks per copy pass afterward; unchanged pinned
semantics are explicitly reused. Production Make, complete prior17,770-file
seal audit and independent native-mounted recount agree. Only source, padded
object, guard CSV and ELF change before documentation. No dependent-object
exceptions. The focused input snapshot contains1,101 files and23 canonical
preparation artifacts are pinned. Four new tools modules import the existing
family model; inherited dirty work in the older tools mirror is preserved.

## Next work

Continue `func_1514F808`, generated_17CAF0.c, original asm/17CAF0.s,
ROM17CCB8,60 words,48-byte frame. It calls integer RNG and floating RNG,
then `func_15143874` with the low random byte and scaled radius, and writes
three scaled affine combinations from the source basis. Current source is
still a stub; no candidate or matching credit is assigned yet. Recover its
ABI/callers, helper outputs, live reads and output alias order before adoption.
Keep parked codegen experiments private, including sound-start's tail gap.

The 75% goal remains active. README changes are aggregate rows only; function
narratives stay here and in concise documentation indexes. Tools commit before
the consumer pin. No push, host-port work or frozen Release change is required.
