# Radial angle effect invariant normalization match - 2026-11-24

`func_150C16C0` replaces its zero-return placeholder with semantic C in
`conker/src/game/generated_EEB10.c`. The normalized 174-word/696-byte body
and slot match retail, frame 296: VA150C16C0..150C1978 / ROMEEB70..EEE28.
**98 words with bindings emit directly; 76 checked word/relocation guards
normalize invariant-address promotion, heading register allocation and the
associated schedule.** Seventy-five rows change words; one changes only a JAL
binding. This is a guarded match. Raw C is not byte-exact.

Actual production is **4,673 / 5,528 (84.53%)** total, Game **4,000 / 4,855
(82.39%)**, Init 492/492, Debugger 181/181, zero drift and 855 different.
**26 more matches are required for 85%**. Only this callback gains a match.

The callback receives 15 o32 words. X/y/z, word 8 heading and final slot are
active; source/index and other generic fields are unused. X/y capture GPR
inputs into FPRs and z loads before helpers. Only the first two incoming homes
are stored. Heading, quarter heading, scale D_800A01F0 and slot are captured
before the single-iteration loop. Poisoned coordinate homes and guest provider
mutations test these capture points. This qualifies the actual o32 interface,
without claiming every generic callback typedef is portable-compatible.

UnsignedRNG%13-63 sets signed 16-bit pitch. Four angle lookups use pitch/pitch-64/
heading/heading-64 narrowed to u8. Speed is floatRNG*capturedScale+25.5.
Two integer draws set count=draw%9+5 and lifetime=(draw&63)+90. Two more float
draws build payload fields00/10 from D_800A01F4/F8 and D_800A01FC/0200.
The five coefficient bits are 418B3333/41A1999A/41C5999A/3E4CCCCD/3ECCCCCD.
Velocity uses horizontal=speed*pitchValue, x=horizontal*headingQuarter,
y=-speed*pitchQuarter, z=horizontal*headingValue. Flags 40, kind 10, alpha 255 and
field1B = 255 are explicit. Factory 15147DA0 receives
`(request,payload,0,1,5,0,0,0,0,0,0,render,0,slot,0)`.
Its result is ignored; the loop decrements one to zero and returns one.

Records retain their actual 28/32/32 sizes. Payloadfield14/tail4 and other
source holes stay uninitialized. Declaring the real captured scale first
recovers retail record addresses without a private stack map. Plain/register
request/payload pointer probes grew the frame 304 and were rejected; array
probes did not fix allocation. Direct unsigned heading expressions within
the loop select the final source. No dummy local, enlarged object, alignment
override, instruction insertion/omission or compiler/profile/Makefile change.

Raw C keeps coefficient addresses in s7/fp, where retail keeps request/payload
addresses, and swaps heading register colors. Prologue bytes00..58 and
epilogue26C..end stay fixed, including saved GPR/FP-pair lifetimes. Matching
frame/length alone did not justify the guards. The committed scoped symbolic
interpreter compares the complete combined memory/FP-operation/helper-call
trace for arbitrary input bit patterns, provider results and fresh public
memory epochs. It preserves private frame/saved pairs under the stated o32
helper contract, permits incoming-home/global mutations, and permits factory
writes to all three bounded records. Valid disjoint stack/data regions and
the provider ABI/fixed-loop/divisor contracts are assumptions. This is a scoped
structural symbolic check, not a general SMT or all-machine-context proof.

Both streams produce 111 trace events /11 calls, branch outcomes true/true/false,
172 reachable words and equal saved-register/return state across four relocated
layouts. Six supported-execution controls change loop count, slot home, payload
kind, factory control, multiply operation or coefficient binding; every wrong
variant fails trace comparison. FP negation is observed and partial FP-pair
overwrites are rejected. No helper public effect is silently assumed absent.

Both complete owner padders agree; both neighbors retain raw/padded words and
bindings. Raw .rodata/.data stay absent; padded .rodata stays absent and .data
empty. Actual Make has three commands. The independent middle-owner reference
preserves following C1978. Production equals the complete predicted ELF:
**700 changed bytes, zero exclusions**. All 189,088 protected Game
data bytes / 720 owners, conversion rows and other inputs remain fixed.
Only 76 guard rows append to the original CSV. Existing duplicate-recipe warnings
for generated_12D630/F44D0/F5800 remain; Makefile hash is unchanged.
Unchanged broad neighbor suites are not repeated or claimed fresh.

Guest tests pass **510 cases per each of four normalized/original
streams plus raw C**, and 312 access-fault quads. All 256 heading/slot
bytes, 13 pitch remainders, 9 count remainders, 64 lifetime values, unsigned word
boundaries, four rounding modes, captured inputs, provider mutations and both
factory outcomes are covered. All 92 seeded record bytes agree at helper
boundaries. Exactly 172 of 174 words execute: two BREAK7 words guarded by fixed
nonzero divisors 13/9 are statically unreachable. Fault-prefix tests qualify
normalized emitted order, not portable C exception semantics.

SDK32 O0/O2/O3 each pass **502 legal cases**, with strict aliasing,
rounding controls and UBSan. Factory observes 75 initialized record bytes;
17 unspecified bytes are excluded. RNG helpers have no record pointer and
do not inspect private records before factory. Dual32 digests compare ordered
calls and public effects. All 25 source mutations compile and exit42 on
comparison, including an incorrectly late scale load. No compile failure,
signal or sanitizer trap counts as an effective control.

The aligned pristine-ROM census finds no direct entry J/JAL and one pointer
ROM22F4C8 / VA8008AA08, D_8008AA00[2]. Four original registry parents pass 384
cases per stream plus raw C, forwarding 352 child calls per stream. Eight
return-zero controls prevent the second child. Parent coverage is 95/96,
113/130,112/120,128/138; two parents remain unmatched live. Eight cases execute
all 24 wrapper C1660 words through original 96-word C2F0 and 200 child calls per
stream, including its actual 25-child request.

Original 27-word angle leaf executes 256 inputs and all 27 words against the
260-byte retail/frozen-ELF table. Original 70-word 15147DA0 and 11-word memcpy match
the frozen live image and execute all 81 words across 16 constructor cases.
Only allocator internals are contracted. All 32 descriptor and 32 render bytes
copy, including ten seeded unspecified bytes in guest; native excludes holes.
The 20 coefficient bytes and 260 table bytes agree with pristine ROM and frozen ELF.
Helper/caller matching credit remains zero.

Boundary checks reject 152 guarded corruptions, expose 196 unguarded changes,
pin 21 bindings, and verify full/scoped guard CSV equality. Twenty GNU links /
40 guest rebase runs include raw C and normalized/original bodies across
HI/LO carry/address regions. Both padders reject the oversized probe.
Shared `make tools-check` passes.

| Qualification | Elapsed | Coverage |
| --- | ---: | --- |
| preinstall-primary | 141.103s | 5 fresh / 0 reused |
| preinstall-sibling | 119.023s | 5 fresh / 0 reused |
| installed-primary | 117.143s | 5 fresh / 0 reused |
| installed-sibling | 119.218s | 5 fresh / 0 reused |

The fingerprinted second-tools overlay preserves the separately dirty sibling.
Tools commit before consumer. Claude Pro login was verified live. One 156.437s
packet-only advisory call used the existing firstParty Pro/default model,
tools=[]/mcp_servers=[], zero tool uses. Allocator cost claims remain unproven;
suggested pointers were already rejected, and store/call reordering was not
adopted. Local symbolic/execution evidence establishes the normalization.
No second call was made.

Baseline consumer: `db42c38fe4ac1b4d95a030416a4074a890cc392b`.
Tools commit: `046acc6408746651e181d240d153e0bac5015fd2`.
ELF SHA256: `e32d1f6be8bb952b145806d6a9650b42fa2a53332faae1ba5d450a9d2e398296`.
Padded owner SHA256: `74fc0e749b3a4dc666f0d4feabc493837de1aba2c14b2281a29b2fdc63c1e2ec`.
Freeze: 3662 inputs / 2267 copies.
Receipts: `conker/build/game-radial-angle-150c16c0-private`.

Root README changes only aggregate rows. This note and five concise indexes
hold detail. Graphify query precedes work; native update/scoped AST merge retain
old IDs/proof metadata after actual hook producers terminate. Heavy staging
and low-memory validation/publication run separately. No full-corpus extraction,
host/Release action, push or gameplay acceptance is claimed. Remaining Game
candidates including C9BDC and matrix callback stay private/uncredited.
The 85% goal remains active.
