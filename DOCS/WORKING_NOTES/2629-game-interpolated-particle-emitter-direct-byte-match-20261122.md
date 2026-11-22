# 2629 - Interpolated particle emitter direct byte match

Date: 2026-11-22. The total 85% matching goal remains active.

`func_150D1204` replaces its zero-return placeholder with complete semantic C.
All **102 body words emit directly from C**, frame120, **zero guards**, inserted
or omitted words. Its103-word retail slot retains the separate four-byte zero
padding after the408-byte body. Production is **4,611 / 5,528 (83.41%) total**,
**3,938 / 4,855 (81.11%) Game**, zero drift,917 different. Init492/492 and
Debugger181/181 are unchanged. **88 more matches** reach85%. Conversion rows
are unchanged; this former C placeholder already counted as converted.

## Source and actual interfaces

Source `conker/src/game/generated_FDD70.c`; original `conker/asm/FDD70.s:648`.
Body VA150D1204..150D139C, ROMFE6B4..FE84C; slot extends toVA150D13A0.
RA is atSP3C. The interface takes four float-vector pointers, a fraction and
the actual SDK struct102 emitter pointer. The existing emitter type recovers
the original alias assumptions and floating schedule; byte-pointer variants
remain99/102 words or differ at32 scheduling/register words. Three vector
locals and original scalar declaration order recover the exact stack slots.

The routine interpolates both endpoints, scales their difference by three
reads of emitter->unk74, takes two float RNG draws followed by two unsigned
integer draws, and submits the position/velocity packets. Size is draw*61+60;
spread uses the late global multiplier/addend. The two unsigned fields use
low four bits+35 and remainder156+100. Identity byteC and context byte1 load
after the draws. Changes to inputs during RNG calls leave the captured vectors
unchanged; late changes to constants and identity affect the final submission.
Raw SHA256 `02c9fbdb9ae94b131d9e839c36598acedcbddc98cc57c6386af212fd02cc0e29`.

The emission helper's235 original words are preserved. Its fourteen-word ABI
has u8 kind; two vector pointers; four floats; s16,u8,s16,s16,u8,u8 fields;
and a final word context. Original narrow home loads and the pointer-return
epilogue are checked. This callback's return is ignored. Emission helper
internals remain contracted; no full effect-system or gameplay claim is made.

## Caller and original RNG execution

The nine-entry D80089B38 table registers this callback at index7/address80089B54.
Original/current table bytes agree. Original parent15134E48 supplies the four
vector addresses, fraction in its outgoingSP10 and emitter inSP14. Four origin
words, the actual13-word branch/JALR/delay window and two continuation words
are qualified in192 cases per stream. Thirty continuation words are also
checked for no V0 read before the loop and post-loop redefinitions. A poisoned initial home makes omitted
emitter-store control effective. The current parent remains a297-word zero
stub; these tests execute its original bounded window, not the complete parent.

Both original RNG routines execute in864 cases per stream: all18 integer and
25 float words, four seed transitions checked against an independent64-bit
reference,12 seeds, three vector-alias patterns, two stack phases, fractions
and four rounding modes. The actual float coefficient is **0x37800080**, not
1/65536; its conversion/multiplication flags and rounding enter the reference.
Effective controls alter integer return shifting and float scaling. Seed1
collapses both target integer reductions to the same results, so the final
controls use a seed with observable reductions. No ineffective control is
reported as a pass. Original code and coefficient bytes match the current ELF.

## Fresh qualification and limits

- Guest:1,489 cases per raw/original stream, all102 target words executed,
  every identity byte, two independent integer reductions, input aliases,
  mutable providers, all four rounding modes and153 access-fault pairs.
  Packet values, call order, public memory, saved registers, sticky flags and
  final bounded FCSR agree. The finite IEEE oracle preserves signed zeros;
  it does not claim exhaustive VR4300 NaN, denormal or exception emulation.
- SDK32 O0/O2/O3:529 cases each, actual struct102/struct17 layout assertions,
  strict aliasing and UBSan. Independent guest-checked vectors compare all
  fourteen argument words, every packet coordinate and call-boundary state.
  Signed-zero cases and vector aliases pass. Ten source controls cover wrong
  coordinates, velocity direction/coefficient, RNG count/sign/reductions,
  size/spread constants, identity and stack arguments.
- Input/emitter overlaps and incoming-home mutations are guest-only. Native
  tests use allocated float arrays and a separate valid struct102 object;
  no broader portable-C overlap or full private-caller execution is claimed.

Both padders preserve the original payload and all13 binding sites.16 GNU
links independently rebase all symbols across HI16 carry boundaries. Eight
possible GNU alignment bytes are zero; the first four are the retail slot's
separately checked padding. Four other owner functions and pools, all old
guards, other bodies/addresses and conversion rows agree. The natural existing
O2/g3 Make route uses three commands. The independently predicted complete
ELF has **348 changed bytes, zero exclusions**, including two closed metadata
swaps/four unchanged symbol definitions/44 name bytes. All189,088 protected
GameData bytes/720 owners are exact. ELF SHA256 `2be067b5e5f4c5d9000de90473497a639edfd46dbae5a3da9b95580bceb41bb9`.

Both tools configurations pass all five checks before and after installation;
Python and data hashes agree. The first adapted runner selected the previous
target and was rejected by its installed-state gate; its receipt is retained
as preinstall-wrong-suite and receives no emitter credit. The corrected runner
and manifest-backed source selection are used by the accepted paired runs.
Shared tools-check passes. Real sibling edits and352 dependency hashes are
preserved. Existing duplicate generated_12D630 Make warnings remain.

Baseline consumer `99d52d9783cf2504118a90fbf61f09cae6c91ed4`, tools `9928e7b77dca56b0ab50ab60e2879bf4f48c3ec4`.
Tools commit `0b85cce62976a12c338eeef6f63fb5cc0c3e33a8` is banked before
the consumer. No push. The available host scene artifact uses a different
mapping and binary input, so no direct C import, host/Release build or gameplay
acceptance is claimed. Zero Claude calls.

Finish graph retention and the immutable bank before the next recovery.
The remaining owner stub func_150D08C0 is the next local candidate to inspect;
earlier private candidates stay uncredited and the85% goal stays active.

Graph maintenance: the native update exited 1 with all
70,630 prior IDs retained. The subsequent serial scoped extraction
covers 8 C/Python files with no missing AST sources, producing
70,687 nodes / 166,217 links and retaining prior qualification
metadata. This is a scoped refresh, not a full-corpus re-extraction. Actual
commit-hook producers must be terminal and their ID/metadata retention audit
must pass before the final immutable bank is accepted.
