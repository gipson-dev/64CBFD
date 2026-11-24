# Point spray callback direct byte match - 2026-11-24

`func_150C71C0` replaces its zero-return placeholder with complete semantic C.
All **99 body words emit directly from C**, with the original **96-byte frame**
and **zero instruction guards, insertions or omissions**. The 100-word slot
retains its separate four-byte zero padding. Production advances from 4,655
to **4,656 / 5,528 (84.23%)**, Game **3,983 / 4,855 (82.04%)**; zero drift,
872 still different, **43 more matches reach 85%**. Init 492/492 and
Debugger 181/181 stay fixed. Conversion rows remain unchanged.

Source `conker/src/game/generated_F44D0.c`; original `conker/asm/F44D0.s:121`.
Body VA150C71C0..150C734C, ROM F4670..F47FC; padded slot ends at VA150C7350.
The other owner function, `func_150C7020`, remains unrecovered/uncredited.

## Recovered source and literal pool

The interface takes four float-vector pointers, an unused float fraction and
the actual SDK struct102 emitter pointer. Only the first two vectors and the
emitter are used. Compute `(second - first) * 0.4070000052f` component-wise
before any RNG call, preserving ordered single-precision subtraction/multiply.
The final submission receives the **live first vector pointer**, rather than
a copied position, and the previously captured velocity at incoming SP-12.

Five explicit RNG statements preserve call order: unsigned integer, three
floats, unsigned integer. Lifetime is firstInteger%31+42; opacity is
secondInteger%101+155. Final float parameters are firstFloat*70+30,
secondFloat*D800A0498+D800A049C,1,thirdFloat*D800A04A0+D800A04A4. Read these
globals and emitter bytes C/1 after the draws. Submit the fourteen-word helper
interface with lifetime repeated, signed 255/lifetime, enabled 1 and late bytes.

The first draft's external-global scale emitted 99words/frame 104. Recovering
the actual retail float literal **0x3ED0624E**, plus the scalar declaration
order, recovers frame 96, all spill homes and every instruction. The accepted
source keeps all five RNG draws explicit. A compact inline-call expression
also matched IDO but left argument evaluation order unspecified; it is not
used. Native tests qualify the same explicitly sequenced body.

IDO emits one 16-byte literal section: the four-byte coefficient followed by
twelve zero alignment bytes. `check_point_spray_150c71c0_pool.py` pins its
complete bytes/order, all 99 body words and 16 relocation sites, and rejects
another function using the pool. A scoped four-command Make recipe checks
this object before binding its `.rodata` references to retained `D_800A0494`.
The padder discards the compiler section and uses the existing retail data;
the coefficient word matches ROM 244F54 and the current ELF. No protected
data word or old guard row is changed. Native helper observations use byte
reads for the caller's float-array origin, avoiding struct-lvalue aliasing.

Raw body SHA256: `9dbfea063b72c9604ba1ca6e5ba653d5fe0c92b53f6671c00af13199c164bb5a`.
Literal section SHA256: `bd13222ada1b45f0e9c9338d63cc98303ff9ef773b2441901ad29ea097c58fb2`.

## Callback, RNG and arithmetic evidence

The complete aligned-ROM census finds no direct JAL and one entry pointer,
ROM22E5FC / VA80089B3C, index 1 of the nine-entry D80089B38 callback registry.
All original/current table bytes agree. The original 297-word parent 15134E48
supplies four vector addresses, fraction at outgoing SP10 and emitter atSP14.
The current parent remains a zero-return stub and receives no matching credit.

* Guest:665 cases per four instruction streams, all 95 reachable words,
  every identity byte, all 31 lifetime/all 101 opacity residues, unsigned
  boundary values, input aliases, two stack phases, mutable providers and
  four rounding modes. Packet values, all calls/registers/memory traces,
  saved ABI, sticky flags and bounded final FCSR agree. 123 access-fault quads
  compare identical emitted instruction streams.
* The four remaining body words, indices 85/89/90/91, are unreachable divide
  safety paths. For every u32 RNG result, lifetime is 42..72; it is never 0/-1.
  Thus the signed 255/lifetime division cannot trap for zero or overflow.
  These words remain present and byte-exact; execution coverage is 95/99,
  not a claim to execute unreachable instructions.
* The actual four-word registry origin, 13-word JALR/delay window and two
  continuation words pass 192 cases per four streams, checking all six
  argument words and caller-private float saves. Omitting the emitter home
  store is an effective poisoned-home control. A separate 46-word original
  continuation scan proves no callback V0 read before both the loop-delay and
  post-loop redefinitions; an inserted SW V0 control is rejected. Return is
  ignored. Complete parent execution is not claimed.
* Both original RNGs execute in 864 cases per four streams: all 18 integer and
  25 float instructions, five seed transitions per case, independent 64-bit
  seed reference, 12 seeds, vector aliases, stack phases and four rounding
  modes. The original float conversion uses coefficient 0x37800080. Two
  effective controls change integer return shifting and float scaling.
* Native SDK32 O0/O2/O3: 661 cases each, actual struct102/struct17 geometry,
  strict aliasing and UBSan. Independent guest-checked vectors compare all
  fourteen argument words and complete call-boundary state. Ten source
  controls return comparison exit 42, with no signal/trap counted as success.
  The first 255-to254 division control exposed a missing residue 9 case;
  final coverage includes every lifetime/opacity residue and makes it fail.
* Native tests use valid float arrays and a separate emitter. Incoming-home
  mutations and emitter/input overlaps are guest-only. IEEE tests are finite
  and bounded; they do not claim exhaustive VR4300 NaN/denormal exceptions.

The 235-word original `func_151DB5D0` helper remains unchanged assembly. Its
narrow homes and pointer-return epilogue are verified against the current
ELF. Internals are contracted rather than executed. Only this callback gains
credit; no effect-system, host rendering or gameplay parity is claimed.

## Build, negative controls and committed bank

Both complete-owner padders preserve the other function and padded pools;
before-C reconstruction equals the frozen production owner byte-for-byte.
The raw coefficient section is intentionally new, checked and discarded;
the padded owner/data remain at their original addresses. The new Make rule
replays all four actual commands, including the fail-closed pool checker.
GNU Make reports this explicit recipe overriding the generic three-command
recipe; the selected four commands are verified. The existing12D630 recipe
override warning also remains.
99 word pins, 16 binding pins, 18 pool/other-user/extent controls and 198 visible
unguarded word corruptions pass. A generic oversize remains explicitly
visible as overflow; the generated padder rejects it. Sixteen actual GNU
links and 32 guest rebases cover adjusted HI, negative LO and JAL regions.

A separate frozen-before-C/original-target-ASM reference reconstructs named
ELF definitions and strings from the baseline. The C link and production ELF
equal its prediction: **408 changed bytes, zero exclusions**. All 189,088
protected Game data bytes across 720 owners, other bodies/addresses/extents,
conversion rows, old guards and unrelated objects remain fixed.

ELF SHA256: `fb83e17f5dbd3fb87bc29ce11b7da7a140edf534820020d03828afc9e147c38f`.
Padded owner: `e70753f7adc3869f38d1331cadd4dff83b43755ee3af223c9bb35a341578c0f4`.

| Phase | Time | Gates |
| --- | --- | --- |
| preinstall-primary | 119.253s | 5 fresh / 0 reused |
| preinstall-sibling | 133.716s | 5 fresh / 0 reused |
| installed-primary | 149.788s | 5 fresh / 0 reused |
| installed-sibling | 118.502s | 5 fresh / 0 reused |

Shared tools-check passes. Tools commit
`73aa2e866a488b07b4235f9b711d9d4c44d2c4f4` precedes the consumer commit.
Exploratory runs and incomplete receipt-wrapper runs are excluded from final
qualification. All frozen live inputs/snapshot hashes and dirty sibling
dependencies are audited. README changes only aggregate rows; old DOCS
index bytes remain intact. Normal Graphify update, actual hook completion,
scoped AST/current-definition refresh and all old-ID/qualification retention
have separate receipts; this is not full-corpus extraction. One packet-only
Claude advisory ran with built-in tools and MCP disabled. Its suggestions
were rejected or already tested; the final source/pool fix was independently
measured locally. No host/Release edit/build, push or WSL restart. Keep the 85%
goal active. Older dimensions 15015FBC and renderer 15197148 remain private.

The final source removes one extra trailing blank line caught by the commit check.
Only bytes after the final C token changed. The source manifest was refreshed
and both installed five-gate suites rerun; the raw body, padded owner and
complete production ELF remain identical. Preinstall receipts retain their
original source fingerprint. The initial tools qualification commit is
`d0a52ea124be0b9dc05e761710edbfac4dd63b37`; the formatting fingerprint commit above is the final pin.
