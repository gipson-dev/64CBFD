# 1765 - Position and alpha attenuation guarded C match

Verified: 2026-10-28. Target func_1517B6E8, owner generated_1A89B0.
VA0x1517B6E8..0x1517B7A8 /ROM0x1A8B98..0x1A8C58: 48 words, 192 bytes,
no frame and no external relocations.

## Source, ABI and live-store order

Replace the zero-return placeholder with:
~~~c
s32 func_1517B6E8(s16 *input, s16 *output, s32 *counter, u8 *alpha)
~~~
The original caller passes the input record position, output vertex position,
a counter in its stack frame at SP+0xBC, and vertex alpha at output+0xF.
Keep the address-based symbol; input/output/counter/alpha and current/scaled
names describe the recovered data. No shared declaration repair is needed.

1. Read the signed initial counter. Below0x600, copy input X then Y to output.
   This path never reads or writes alpha.
2. At or above0x600, store output Y =inputY +(initialCounter>>6) -24.
   Reread the live counter after that halfword store and store output X
   =inputX +(counter>>8) -6. Preserve this Y-before-X order and the live reads.
3. Reread counter after both stores. Divide unsigned alpha*128 by the signed
   denominator (counter>>6)-23, with truncation toward zero. Arithmetic-shift
   that quotient right four. Store its low byte only when the signed result
   is smaller than the original unsigned alpha. Then store counter=0x600.
4. Read and copy Z after the counter/alpha updates and return zero. Aliases may
   change this last input read. No clamp, early Z capture or cached counter is
   added to the recovered routine.

Signed right shifts and narrowing retain the target operations. Coordinate
sums, denominator subtraction and the unsigned-byte numerator remain within
signed32 range. A live counter alias can nevertheless produce a zero divisor;
the original compiler's break7 guard remains intact. Its signed-overflow break6
is unreachable for a numerator formed from an unsigned byte. The redundant
input-X load at+156 is also unreachable. All48 words are retained;46 are reached
across the guest corpus, including break7.

## Two-word register normalization

The final C emits46 linked words directly under normal O2/g3. At+16/+20 the
compiler assigns inputY and initialCounter>>6 to t6/t7 in the reverse order
from retail. Both immediately feed the identical commutative addu at+24.
Neither temporary is read again before its next overwrite: t7 at+60 and t6
at+80. The two expected-word guards exchange only those destination registers.
There is no instruction insertion, omission, relocation or profile change.

Seven additional source forms were screened; the two-word allocation difference
persists in the complete48-word forms. Retain the uncredited fit receipts.
The guard test proves the common addition and scans every intervening register
read/write to close both temporary lifetimes. Wrong expected words, raw length,
raw content, bindings and an actual bad padder CSV are rejected.

Raw compiler SHA256:
~~~text
5239edfc21fc76a2a75b01eb389682c67d02e3918ccc2d6320d80d5b7a18623c
~~~
Original/normalized/linked slot SHA256:
~~~text
ee6c15f1908be61a815e45dbe6762e925aea9eacc2207c4679ae456a02b19b6e
~~~

## Original registration and caller behavior

The aligned ROM census finds no direct JAL/tailJ and one pointer at ROM0x231994,
VA0x8008CED4. This is slot2 of the 12-byte entries rooted at D_8008CEBC.
The frozen231970.rodata owner bounds the visible table to17 words; its slot2
is {func_1517B6E8,0,func_1500BAB8}. Preserve that source and object unchanged.
The third entry is separate rendering behavior and receives no new C credit.

The original func_1517BBAC window at VA0x1517C6D8..0x1517C780 contains42 words.
It loads the registered pointer, invokes it with four pointer arguments, and
uses the s32 result as a skip gate. A zero result continues the RGB/alpha setup;
a nonzero result would branch to0x1517C864. The selected function returns zero.
The next instructions read alpha at output+0xF and copy it to+0x1F/+0x2F/+0x3F,
which establishes the alpha name and four-vertex role independently of a guess.
The source instructions at0x1517C65C/660/670 also establish output, counter
and alpha argument setup. The current parent remains its unchanged three-word
C stub. Bounded original-window evidence does not recover the full parent or
claim gameplay acceptance.

## Fresh focused qualification

Both tools copies pass eight fresh canonical methods and project-tool checks.
Each installed copy passes two fresh owner/image methods and reuses six semantic
methods only after exact module, snapshot, seal and qualified-artifact identity.

- 7,816 guest cases compare independent effects with both raw C and normalized/
  literal retail code. Cover all256 alpha bytes, signed counter and halfword
  boundaries,18 input/output/counter/alpha overlap layouts, negative divisors,
  narrowing, live reloads and arithmetic right-shift rounding. Sixty cases reach
  the actual break7 path; the46 reachable words are covered.
- 1,057 fired access-prefix pairs compare normalized complete private state,
  memory, trace, PC and delay ownership. Raw C preserves public partial memory
  and access trace; scratch registers are allowed to differ inside the proved
  exchange. A below-threshold counter needs no alpha mapping. A zero-divisor
  alias preserves the two coordinate stores before break7; it does not clamp
  the counter or finish Z. The model uses an explicit HI/LO sentinel on zero
  division because the subsequent break occurs before mflo. No hardware HI/LO
  result or native-C behavior is inferred for that undefined division domain.
- 180 connected cases run the actual42-word registry/call/continuation window,
  passing the counter in parent stack storage and alpha in the output vertex.
  Verify zero-return continuation and RGB/alpha replication over all4 vertices,
  along with exact private state and trace for literal and normalized code.
- Native32 O0/O2/O3 with trapping UBSan each pass68,608 positive cases. Use typed
  s16 array storage with valid overlapping input/output ranges, a distinct s32
  counter and permitted unsigned-char aliases. Cover all65,536 coordinate
  encodings and all256 alpha bytes with whole-storage fences. Ten wrong gate,
  signedness, divisor, clamp, alpha condition, X shift, numerator, copy-order
  and return variants fail by value. The signed-alpha negative uses multiplication
  rather than shifting a negative value, so it remains a meaningful C control.
  Counter-halfword aliases and divide-zero probes are separate guest tests.
- Three independent GNU layouts pass27 cases, including live aliases and break7.
  There are no external bindings. Real Make/padder/GNU output is byte-identical.
- Two actually compiled wrong C forms fail by written alpha in mapped memory.
  Caching the initial counter gives alpha200 where the late reload gives39.
  Replacing arithmetic >>4 with /16 after a negative quotient gives254 where
  retail gives253. Six complete-image corruptions are rejected as well.

The initial screen's stale previous-target census and declaration extraction
were corrected before final qualification. Preserve early failed/fit receipts;
all final tests pass without weakened flags or gates. Routine Claude calls:0.

## Actual Make, strict image and measured progress

The owner has14 compact functions and no GLOBAL_ASM routines. Preserve all13
neighbors, bindings and pools. The actual normal three-command IDO/padder/GNU
Make route and production reproduce the qualified object. Selected, owner and
actual-Make diagnostics are empty. Production retains the inherited duplicate
generated_12D630 Make-recipe warning.

The adopted entire ELF equals the independently predicted131-byte delta:
130 target-code bytes and one target-size byte12->192. There are zero exclusions
and no symbol/string permutation. All6,056 function addresses,6,055 other bodies,
named definitions,720 protected Game-data owners and189,088 protected bytes are
unchanged. Shared headers, the current parent, registry source/object, map,
inventory CSV and every inherited guard row are fixed. Append only these two
guards for this target.

ELF SHA256:
~~~text
f87a98be9f3ecb68cd8e36e4e7075a24cb28382ab5ab67d0c4457817de91639e
~~~
Native CRLF guard manifest SHA256:
~~~text
1383ae8599001c8769a2557ce1e4d2791f5f3bb5fcf8b59e822cdbc12e618f85
~~~

Seal16,252 native/cache files and250 focused inputs. The actual captured native
ELF recount preserves the C inventory and gives:

| Section | Exact C functions | Different | Drift |
| --- | ---: | ---: | ---: |
| Total | 3,843 /5,506 (69.80%) | 1,663 | 0 |
| Init | 492 /492 (100.00%) | 0 | 0 |
| Game | 3,170 /4,833 (65.59%) | 1,663 | 0 |
| Debugger | 181 /181 (100.00%) | 0 | 0 |

Only func_1517B6E8 becomes exact in this bank. The4,130 threshold leaves287 more
to75%. Remaining shapes:1,534 placeholders,120 semantic/other and9 unlocated.
These screens do not qualify the remaining code; keep the other pending
functions and the NULL factory uncredited.

Predecessor consumer27c3b44d19068494b5c0ebb55772cad527a07f32 and tools
fbd822387d04651909d49bc63a8b02fda20573cb. Bank tools first at
a4d9d22e4ac4634942b1c1594d3f52167bd394e1, then the source, two guards, tools
pin and seven measured documents. Preserve1,740 inherited dirty mirror paths
plus only the two new modules. No push. The root README changes only its two
aggregate matching rows; function narratives remain in these documents.

Refresh ten structural C/Markdown/tools files, retaining old nodes or unique
relocations and all still-valid directed confidence/context keys. Validate the
s32 return, s16 vector pointers, s32 counter pointer and u8 alpha pointer against
the committed signature. No helper/caller edge is invented. Outside freshness,
communities and global analytics remain historical; this is no full-corpus
extraction. Receipts and independent audit live under
conker/build/game-position-byte-attenuation-match/.

Next inspect func_15015E80 from a fresh predecessor. func_1514E920 stays parked
and uncredited. The75% goal remains active.
