# Resource texture-phase and scroll updater byte matched

Date: 2026-11-07. Continues [Note 2159](2159-game-resource-texture-callback-match-20261107.md)
from consumer `04d04ac7599207959629dde102ca06e0b8abfd81` and tools
`aa6259fae5e83dee6e1501dad174cc5636e9824c`. One qualified Game function
advances the active 80% total goal.

## Recovered update callback

`s32 func_1513BEB0(u8 *resource)` in `conker/src/game_168A90.c` replaces the
owner's final zero-return placeholder. Its complete **107 words / 428 bytes**
match at VA 0x1513BEB0..0x1513C05C, ROM 0x169360..0x16950C. The following
alignment NOP remains literal. The routine retains its 32-byte frame and
S0/RA saves under the unchanged ordinary O2/g3 MIPS2/O32 compiler profile.

An independent production-ELF slot audit now confirms **all 13 functions in
game_168A90 are byte-exact**, including every alignment tail. This function
is the only new matching credit; the other 12 were already exact.

Capture the five-float payload at resource + word0x50 + 0xF8 once:

1. Advance phase[2] by D_800A4A84 times live frame time D_800BE9A4, then
   normalize it through `func_15144B68`.
2. Advance scroll[0] by D_800A4A88 times a fresh frame-time read. Set scroll[1]
   to sine of the normalized phase times D_800A4A8C.
3. Advance angles[3] and [4] using D_800A4A90 and D_800A4A94, retaining their
   separate live frame-time reads. Normalize both through the same helper.
4. Repeatedly subtract 4096 while each scroll is strictly greater than 4096;
   repeatedly add 4096 while it is strictly negative. Return 1.

The interval includes both 0 and 4096. Preserve single-precision rounding,
negative-zero behavior, the four actual loops, store order and the captured
payload pointer. A quotient/fmod rewrite would change the original behavior.
The five retained coefficient words are 3D178D50, 3FF33333, 429A999A,
3C9BA5E4 and 3C23D70B. No coefficient/data value is changed.

## One commutative integer operand guard

The selected semantic C already emits all 107 words with the correct frame,
register lifetimes, floating-point operations and branch-delay paths.
Raw target SHA-256:
`4a4ba11a3e841ea72a071ed7acfc02ebc6438762659b6099d5f678befc9b3d5c`.
Exactly one expected-word guard at offset 0x24 changes
`ADDU S0,T6,A0` (01C48021) to `ADDU S0,A0,T6` (008E8021).
This non-trapping integer addition is commutative. The derivation swaps only
its source-register fields; all other words and all 20 relocation bindings
stay literal. No instruction insertion, deletion, schedule rewrite, floating
operation rewrite or compiler-profile change is used.

Equivalent predicate, local-phase and address-expression source forms all
retained that one difference. Reversing delta multiplication operands added
13 differences and was rejected. Raw/padded owner pools, register masks,
options bytes and ABI metadata remain unchanged. Compact-object file offsets
may move as text grows; section geometry and complete metadata bytes remain
fixed. Corrupt register-info/options records are rejected.

## Real table, helper and dispatcher

The complete aligned retained-input census finds no direct target JAL, one
entry pointer at ROM 0x22E6E0 / VA 0x80089C20, and no interior pointers. This
is slot 2 of D_80089C18. The original **41-word func_1513B798** passes one
resource pointer through that update table. Its complete body is already
byte-exact in production.

**16 connected dispatcher cases per body** exercise flag/timer-gated active
lifetimes and the real indirect callback, with and without the original wrap
helper. This callback path executes 36 dispatcher words. The complete dispatcher
is retained for execution, but its unrelated expiry/sentinel/release paths
are not claimed as new coverage for this target.

The complete original **24-word func_15144B68** is also exact in production.
It wraps angles using retained bound D_800A56A4, word 40C90FDB. All 24 words
execute across **16 connected cases per body**, including positive/negative repeated
wraps and later sine-provider mutations. The original sine implementation
remains a bounded service, with controlled binary32 results.

## Focused qualification

Seven checks pass before and after installation in both tools configurations:

* **90 guest cases per body**, across retail, normalized and raw C, agree with
  an independent float32 memory/call/result model. All **107 instructions**
  execute. Cover strict 0/4096 endpoints, signed zero, repeated positive and
  negative wraps, retained angle bounds, live coefficient/frame-time changes,
  captured payload behavior and output/global aliases. Sparse wrapped resource
  addresses and aliases remain guest-only. Full private memory, GPR/FPR,
  HI/LO, PC, calls and access traces agree across all three bodies.
* **137 fired access cuts**, including 16 delay-slot cuts, preserve the complete
  private machine/access-prefix states across all three bodies, including
  original-helper execution. Saved S0/RA and stack lifetime checks pass.
* Native32 O0/O2/O3 each pass **85 finite fixtures** with pointer32/float32
  assertions, fixed disjoint banks, controlled sine, explicit float32 compiler
  options and UBSan traps. All ten compiled negatives fail with exit 1:
  stub, wrong phase, missing phase wrap, wrong sine input, wrong angle delta,
  non-strict upper/lower predicates, wrong bound/result and payload reload.
* Two independent GNU links verify all **20 bindings**, including signed
  LO16 carry across the five-coefficient block. Altered raw words, bindings,
  guard history, register metadata and six whole-image corruptions reject.
* All **12 raw and padded neighbors** remain literal. Four inherited compiler
  warnings are identical, with no new diagnostics. All **150 frozen inputs**
  and separately hashed tools/dependencies remain accounted for.

The guest interpreter is not a FCSR emulator. Finite fixtures and bounded
services do not prove nonfinite termination, portable invalid-conversion or
hardware exception behavior, actual sine accuracy, graphics output or gameplay
acceptance. Retail's repeated loops may not terminate for infinities.

## Linked image and production checkpoint

Actual Make recompiles only `game_168A90.c` and equals the independent strict
image prediction: **361 changed bytes, zero exclusions**. These are 320 Game
body bytes, 19 symbol-table bytes and 22 string-table bytes. The first strict
check rejected 39 unpredicted serialized metadata bytes. One closed adjacent
swap, `func_1518652C` / `D_80087358` at file offset 2809564, accounts for them.
The predictor pins predecessor slots, complete name bytes and permutation,
preserving every value/type/section field under its name. The complete named
definition multiset changes only this target's extent from 12 to 428.

All **6,052 function addresses** and other bodies remain fixed. All **189,088
protected Game bytes across 720 owners** remain exact. Exactly one guard row
appends; historical guard rows, conversion CSV and Makefile remain unchanged.
Compile/link succeed. The whole-ROM checksum retains its expected nonmatching
exit 2 and inherited duplicate generated_12D630 recipe warning.

Fresh shared smoke checks pass in both tools copies. Three unchanged shared
regression receipts per copy are reused after exact helper/test hashes. The
sibling uses a disposable new-module overlay and explicitly fingerprinted
read-only alloc_pools fallback; all 2,434 inherited dirty paths remain intact.
Claude calls: zero.

| Section | Exact / converted | Percent | Drift | Still different |
| --- | --- | --- | --- | --- |
| Total | 4,230 / 5,512 | 76.74% | 0 | 1282 |
| Game | 3,557 / 4,839 | 73.51% | 0 | 1282 |
| Init | 492 / 492 | 100.00% | 0 | 0 |
| Debugger | 181 / 181 | 100.00% | 0 | 0 |

**180 more exact functions** remain to 4,410/80%. Root README receives only
aggregate rows. Four index leads preserve all historical text. Refresh
Graphify on changed paths, retaining existing excluded legacy nodes
fail-closed; this is not a fresh full-corpus extraction. Commit tools before
consumer source/docs/pin, then verify the fresh hook and production stability.

| Artifact | SHA-256 |
| --- | --- |
| Production ELF | `d5f235f0a2ad7e6fce486e740d8edfdabd58c0a381c3c8dd1fba55ce60a7bf5a` |
| Production binary | `d69a5a6a4395628ce1dda68815834409a81820d2701a5ccbb185cef940898d07` |
| Padded owner | `f7b2051b5c3cc6a71fc18f591233c48648d261ed01dc9b44dea09b10cbea9277` |
| Guard manifest | `19dc597d93941d71986e91c20a4fba0b85ced4278b627490a1189da3ccb74c8e` |

Ignored receipts: `conker/build/game-resource-scroll-update-1513BEB0-match/`.
Original source screens: adjacent `...-private/` directory.

Next: inspect the adjacent unfinished owner `game_169510.c`, beginning with
**func_1513C060**, and its complete retail/caller interface before selecting
the next semantic source screen. Keep the 80% goal active and other private
candidates uncredited. Preserve frozen handwritten/hidden-ABI boundaries,
unrelated work, private inputs, saves and the frozen host Release checkpoint.
