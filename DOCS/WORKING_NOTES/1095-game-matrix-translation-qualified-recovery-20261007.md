# Game Matrix Translation Qualified Recovery

Date: 2026-10-07. Baseline: `f4d880fa`,
[Note 1094](1094-game-cached-primitive-color-direct-match-20261007.md).

`func_15142314`, VA `0x15142314..0x151423D8`, ROM
`0x16F7C4..0x16F888`, now contains the recovered translation arithmetic and
explicit 32-bit address calculation. It emits a complete **49 words / 196
bytes**, **frame zero**, no pool, under unchanged **O2/g3 / MIPS2**.
It is **not byte-exact**: **34 positional word differences**, down from the
fresh baseline's 46. No guards, profile/header/padder edits, assembly fallback,
padding locals or scheduling-word insertion are added. Matching totals do
not advance. Continue matching this function; do not call the recovery done.

## Arithmetic And Address Contract

- Read `D_800C3E90` once. Every nonzero byte selects fixed mode; zero selects
  float mode. Do not treat the flag as an exact-one gate or reread it after
  output writes, even when output overlaps its storage.
- Select `(base + (index.low32 << 6)) mod 2^32`. The signed32 index ABI is
  unchanged. Use unsigned32 arithmetic before converting the address back to
  a pointer, avoiding signed index-shift/add overflow in the original C.
- Fixed mode reads signed high halfwords at `0x18/0x1A/0x1C` and signed low
  halfwords at `0x38/0x3A/0x3C`. For each component, convert the safely scaled
  signed high integer and signed low integer **separately** to float; add,
  then multiply by `1/65536`. Signed high times 65536 fits signed32 even at
  -32768. There is no signed negative left shift or overflowing integer sum.
- Float mode copies words at `0x30/0x34/0x38` without arithmetic. Preserve
  signed zeros, subnormals, infinities and NaN payload bits.
- Store each result immediately at output `0/4/8` before reading the next
  component. Output/input overlap may change later halfwords or float words;
  do not snapshot all three components. No calls or allocation occur.

The old C shifted a signed high half and added the low half in signed integer
arithmetic before converting. The compiled guest body gives the wrong sign
when that sum underflows. For example, high -32768 / low -1 should round to
-32768 under the bounded RNE contract, not +32768. Native execution of the
old undefined signed shifts/overflow is deliberately not used as a reference.

## Source Measurements

[Candidate driver](https://github.com/gipson-dev/64CBFD-Tools/blob/master/experiments/game_matrix_translation_candidates.py)
retains **152 measurements**, not distinct emitted bodies:

- 64 primary measurements: repeated/common address, sum operand order,
  safe integer multiplication/unsigned-shift-cast and named/inline scale,
  across four existing SDK optimization/debug profiles.
- 48 O2/g3 flow forms: ordinary/inverted if/else, either early-return form,
  goto and switch, with address/scale placement and multiply operand order.
- 24 O2/g3 meaningful scalar-temporary forms: high/low evaluation order or
  a reused sum, register-qualified scale, address and multiply order.
- 16 ISA/access controls: MIPS1/MIPS2, O2/g3/O2, ordinary/volatile output and
  flag views. MIPS1 bodies have 51/52 words and do not fit or match; access
  qualifiers are controls only and are not installed. A separate MIPS3 probe
  was rejected by the compiler's 32-bit ucode warning and is not a qualified
  measurement. The first common-address driver ordering error was corrected
  before the maintained measurements; no failed form is counted as evidence.

None is exact. The selected ordinary high-first, repeated-address, named-scale
form is 49/frame0/no pool/34 differences with empty diagnostics. It preserves
the original per-component register arithmetic but materializes the scale
later, emits a branch-likely float load instead of the original ordinary
branch/address delay slot, and moves the last fixed store into the return
delay slot. An extra unreachable float-load copy occupies the following
fallthrough block. These are unresolved compiler/control-flow scheduling
differences, not 34 independent arithmetic errors. Do not blindly patch them.

## Qualification

[Nine maintained tests](https://github.com/gipson-dev/64CBFD-Tools/blob/master/tests/test_game_matrix_translation_recovery.py):

- **65,536 guest tuples** cover every signed-halfword bit pattern in each of
  all six fields, all 255 nonzero flag bytes, ten signed/full-word index
  patterns, two stack phases and ordinary/top-of-address-space matrix storage.
  The tuples are correlated permutations, not the Cartesian six-field domain.
  Original assembly and raw C both agree on complete external memory, every
  ordered public read/write and saved state. The independent exact integer
  numerator/power-of-two scale gives the RNE result without reproducing the
  guest instruction implementation.
- **20,576 edge/alias fixtures**: 15,360 fixed matrix aliases, 5,120 float
  matrix aliases and 96 flag/output aliases. Cover signed-halfword extremes,
  all 49 words, wrapped indices/storage, sequential future-input overwrites
  and raw float bit copies, including signaling NaNs. Guest models do not
  claim general FCSR exceptions/rounding or hardware timing.
- **66,816 actual freestanding native 32-bit cases** run the new typed C body
  on a 65,536-tuple fixed sweep and 1,280 float-copy cases, with wrapped index
  arithmetic, sequential overlaps and all storage/fence bytes checked. The
  independent double numerator is exact over this integer range; power-of-two
  scaling commutes with binary32 RNE without overflow/underflow. Native alias
  expectations use native little-endian storage, not guest byte layouts.
  Pointer/integer conversion is tested for this actual 32-bit toolchain, not
  offered as generic ISO-C or 64-bit host-port acceptance.
- **1,152 connected cases** execute the complete original 98-word
  `func_15143134` on its null/positive-zero/negative-zero routes, calling
  either raw C or original translation instructions. Complete memory/traces/
  calls agree; independently check final external storage/status and actual
  forwarded three inputs. This does not cover the parent's nonzero routes;
  those retain their existing point-transform tests.
- Required flag/input/output bytes fail closed when removed; unused fields
  are not read. Seven effective compiled negatives expose integer underflow,
  unsigned-low conversion, wrong stride, exact-one mode gate, wrong scale,
  premature input snapshots and missing Z stores. Every negative changes
  public storage, not merely a trace. Explicitly assert the old underflow
  case's wrong `47000000` output versus the reference's `C7000000` on all
  three components. Detection is not based on private layout differences.
- All 152 controls pass **24 bounded public-effect fixtures each / 3,648
  candidate executions**. Compare complete external memory and ordered output
  writes, not every public-read order across different evaluation forms.
  Each measurement has empty diagnostics/no new pool and remains nonmatching.
- Production-preprocessed/postprocessed copied owner retains **89 functions /
  88 neighbors**, relative relocations, normalized pools and the same **two
  warnings**. The raw selected 196-byte body equals the isolated object.
  The actual padder retains all 49 words, no overflow/guards; rebase the flag
  by `0x18000` and verify both real HI16/LO16 relocations and signed-low carry.
- Installed source, complete linked raw slot/address, 34 differences and
  unchanged guard history are pinned by a separate production gate.

Seven pre-install behavior/owner/padder gates pass in **86.765 seconds**.
Repeated runs are not additional distinct behavioral cases.

```sh
python3 -m unittest tools.tests.test_game_matrix_translation_recovery \
  tools.tests.test_game_point_transform_match tools.tests.test_game_oriented_matrix_match \
  tools.tests.test_game_owner_pool tools.tests.test_pad_c_object_word_patches -v
```

The combined regression passes **38 tests in 322.863 seconds**, zero skips,
errors or failures. After strengthening the negative gates to require public
storage changes and the explicit wrong-sign case, rerun that gate: **one test
in 8.062 seconds**. It is a repeat gate, not another distinct fixture bank.
Final tools/syntax/whitespace gates pass; scoped documentation checks
**77 documents / 3,897 relative links**, zero broken.

## Build And Audit

US ELF rebuild succeeds with the existing duplicate-recipe warning and the
same two owner pointer warnings. Fresh baseline and post-link audits retain
**6,058 symbols / 6,042 retail slots / 16 overflows**. Only `func_15142314`
changes; every address/extent, **6,041 other retail bodies** and all overflow
bodies remain fixed. Parent, color emitters and sampler are unchanged.

Protected Init/Init-data/Debugger/Game-data sections and all **11,006 guards**
remain identical. Independently verify all **720 Game-data owners / 189,088
bytes** are exact. Neither translation nor sampler has guards. Converted
functions/bytes and matching
totals stay unchanged: **3,360 / 5,466 (61.47%)** overall,
**2,687 / 4,793 (56.06%)** Game, **2,106 different**, zero drift. Main README's
already-current aggregate rows remain unchanged; detailed progress stays here.

## Resume

Finish this translator's constant/ordinary-branch/return-delay schedule without
losing the recovered arithmetic, unsigned address calculation or sequential
aliases. The 152-measurement bank and all bounded qualification are retained;
do not repeat it as new evidence, claim byte matching, insert instructions or
patch private offsets. Installed raw and isolated bodies are the same 49 words.
Other ordinary owner candidates remain available, but translation matching is
still open rather than silently handed off as complete.

Sampler `func_151432BC` still needs its two legitimate per-path RA loads and
circle RNG-byte schedule; no new sampler sweep or installation occurs here.
No sibling/frozen Release, save/runtime, rendering/hardware acceptance or push.

Ignored receipts: `conker/build/game-matrix-translation/` and
`conker/build/game-matrix-translation-test/`.
