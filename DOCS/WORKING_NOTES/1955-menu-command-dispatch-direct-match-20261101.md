# Menu command dispatcher matched directly from C

`func_150B6BC0`, owner `generated_E4070`, now matches all **52 words** directly
from its complete C switch. No word guards, insertions, omissions, volatile
accesses or compiler/profile changes are introduced. The existing no-unroll
profile is retained; one target-specific Make variable binds the compiler's
verified jump-table relocation to the preserved retail jump table.

Fresh Native actual-ELF recount: **4,025/5,507 (73.09%)** total,
Game **3,352/4,834 (69.34%)**, Init492/492, Debugger181/181; zero drift,
1,482 different. This replaces an existing C stub, so inventory stays5,507.
The75%threshold remains4,131: **106 more** functions are needed.

## Original interface and state map

Source `conker/src/game/generated_E4070.c`, original `conker/asm/E4070.s`;
VA150B6BC0..150B6C90, ROME4070..E4140, 208bytes/frame24. The signature is
`void func_150B6BC0(s32 unusedView)`. The original saves the incoming A0 at
its argument home and otherwise ignores it. Actual caller func151749F8 uses
`FrameLayerCallback(s32)` at D8008CD04[5], passing its signed view argument.
The former s32 zero-argument/zero-return stub is removed. No shared header
changes are needed. The nine callee declarations agree with their existing
source interfaces; their results are ignored and their incoming argument
registers are not consumed as parameters by the retail bodies.

Read the unsigned byte D800D9890 once and invoke at most one command:

| State | Target |
| --- | --- |
| 1 | func150B6C90 |
| 2 | func150B6D34 |
| 3 | Idle |
| 4 | func150B6D78 |
| 5 | func150B7484 |
| 6 | func150B7560 |
| 7 | func150B765C |
| 8 | func150B77A8 |
| 9 | func150B768C |
| 10 | func150B791C |
| 0 or11..255 | Idle |

Helpers can change the state byte, but this invocation must return without
redispatching. There is no generic fallthrough from one command to another.
Do not describe this dispatcher as implementing the still-unfinished helpers.

## Exact body and verified table binding

Raw SHA:
`3139f4c4d33bd2d975d765d43964060a508346d400fbd1e86892c4efb3223ef3`.
All52body words match after standard relocation binding. HI/LO global bindings
are+0C/+10; compiler .rodata table bindings+24/+2C; nine JALs+38 through+B8.
The raw isolated/whole-owner bindings and bytes are pinned separately from
actual padding and Make output.

The compiler emits48bytes of .rodata: ten R_MIPS_32 entries followed by two
zero words. Each table entry's function-relative target is checked against
retail: 38,48,C0,58,68,78,88,98,A8,B8(hex). The original table is at
ROM2447C0 / VA8009FD00 and retains both zero padding words. Every one-entry
corruption control rejects; the new table is the only new raw owner pool.
The padded owner retains its previous pools and all original exported case
labels. No compiler-generated table is copied into protected Game data.

The only Make addition is:
`generated_E4070.c.o: RETAIL_RODATA_SYMBOL := jtbl_8009FD00_game`
under the existing full BUILD_DIR/SRC_DIR target prefix. The owner's existing
`-O2 -g3 -Wo,-loopunroll,0` profile is unchanged. The actual compile/pad/assemble
recipe reproduces the qualified object exactly. The complete guard CSV is
byte-identical to baseline. Wrong profile preimages and duplicate Make binding
controls reject rather than silently rebinding a different table.

## Qualification evidence

- Freeze1,024 focused Native inputs against the prior17,565-file complete seal.
- Guest8,192cases/32,768executions across three entry/global/table/helper layouts:
  original, padded, actual-Make and isolated C programs all agree in complete
  machine state and trace. All52words execute. Covers all256 selector bytes,
  unsigned range boundaries, ignored signed view bits, changed helper results,
  changed state and controlled table mutation after dispatch.
- Nineteen access prefixes/76executions agree across all four programs. These
  qualify emitted guest instruction order, not portable C fault semantics.
- Three complete original command bodies execute: func150B6D34(17words),
  func150B765C(12),func150B768C(12). Forty-eight cases/192executions cover every
  one of their41words, null/non-null three-pointer masks and both descriptor
  argument pairs(60,1)/(230,2). The first scans pointers at cursor+14, i.e.
  D800D98AC/B0/B4, before selecting state3. The descriptor constructor and other
  command bodies remain bounded providers.
- The complete43-word original frame caller passes64cases/1,024executions,
  callback slot5, both post-call gate paths, clock/accumulator changes and four
  return poisons. All43caller words execute. Its other frame services remain
  providers; this is not a claim about every other frame-layer slot.
- ROM census finds no aligned JAL/tailJ and one pointer literal at2317D8,
  VA8008CD18 = D8008CD04[5]. The original data assembly and caller's JALR agree.
- Native32 O0/O2/O3 each pass4,096UBSan cases, canaries and eight effective
  controls: idle3 dispatch, missing10, wrong8, state1 fallthrough, missing2,
  duplicate5, masked selector and shifted selector. All selector bytes are
  covered; helper results are poisoned and state rewrites are observed.
- All20raw/padded neighbors are unchanged. Owner diagnostics remain zero.
  Both tools copies pass six public tests before and after installation,
  plus shared checks in both copies.
- Independent complete ELF prediction passes with exactly130changed bytes:
  only this slot and symbol extent12->208. No metadata serialization change,
  exclusion or object reorder is needed. All6,056 addresses are fixed and
  6,055 other bodies are unchanged. Game data remains189,088bytes/720owners,
  exact, including the original jump table.
- Full production Make, all17,565 prior sealed inputs and a fresh independent
  Native actual-ELF recount pass. Only Makefile, source, owner object and ELF
  change among old inputs. There are no unplanned dependent-object changes;
  all C inventory CSVs and the guard CSV remain unchanged.

Production ELF SHA:
`28aa241d6bd4b4d4edf654f0435d4762c39e2386be4e2f23c6bcb69a5ee7d80b`.

Retained non-passing receipts are fixture corrections, not completed gates:
the initial linker assignment needed spaces; the original global .L150B6C80
branch label needed its checked function-relative192 binding when extracting
one function; the connected-helper fixture initially omitted its+14 cursor
displacement; the intentional native fallthrough negative needed a recognized
fallthrough comment under -Werror. Candidate C and production build behavior
were not changed to satisfy these fixture corrections. Only corrected full
runs are credited.

## Bank and continuation

Stage `conker/build/game-menu-command-dispatch-150B6BC0-match/` retains original
inputs, source/Make proposals, full pool checks, raw/owner/padded/actual-Make
objects, first-link ELF,25canonical artifact fingerprints, runtime/census
results, both public suites, production audit and independent Native recount.
Finished work is committed tools first and consumer second. Root README gets
aggregate rows only; the five documentation indexes link here. Private identity,
relative-direction, motion and owner-gate candidates remain uncredited.

Next audit **func15115E0C**, owner generated_142560, source
`conker/src/game/generated_142560.c`, original `conker/asm/142560.s`.
Its52-word/frame32 slot is VA15115E0C..15115EDC, ROM1432BC..14338C.
The current `(f32,f32,u8*)` stub signature conflicts with the original A0/A1
record-pointer interface. Its existing semantic caller func15115EDC also uses
that false signature. Audit the complete original caller and both helper/return
contracts before selecting a C body; do not preserve a wrong ABI merely to keep
other bytes fixed. No next-target source is changed or credited. Goal stays
active. NoClaude, push, WSLrestart, host/editor orRelease changes.
