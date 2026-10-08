# Game Piecewise Envelope Match

Date: 2026-10-06
Baseline: `4a087419` ([Note 1055](1055-game-piecewise-envelope-investigation-20261006.md)).

## Source And Compiler Recovery

Replace the false `func_151415D4` stub in
[`game_16DC80.c`](../../conker/src/game_16DC80.c), including local prototype:
**`s32 func_151415D4(u8 *actor)`**. Complete **69 words / 276 bytes**, VA
**0x151415D4..0x151416E8**, ROM **0x16EA84..0x16EB98**, **no frame**, existing
**O2/g3**. No shared header/profile/data change. Preserve Note1055's four
strict envelope branches, float operation order, live output/timestep/elapsed
aliases and unchecked repeated period subtraction; return1 after the loop.
No clamp, positive-period guard or modulo replacement. Even tiny positive
periods may fail to make single-precision progress.

Scope rise/fall **factor variables independently inside their branches**.
Product-first rise sum and baseline-first fall sum recover the missing retail
rise **store/branch/nop directly from C**, giving69 words/13 differences.
**56 words compile directly**. Apply four closed FPR lifetime permutations:

```text
0x44..0x68: f4 -> f18 -> f16 -> f4
0x84..0xA4: f4 <-> f8
0x88..0x90: f16 <-> f18   (plateau, nested in preceding range)
0xAC..0xB8: f4 <-> f16
```

Swap commutative operands at **0x58,0xA4,0xB8** after those permutations.
The latter two swaps cancel the register encoding changes, needing no guard
rows. Derive all69 retail words; exactly **13 guards** at
0x44,0x48,0x50,0x58,0x64,0x68,0x84,0x88,0x90,0x94,0x98,0xAC,0xB4.
No opcode, float function, memory offset, branch/likely target/delay, count,
frame, GPR, call or relocation change; no insertion, omission or copied ASM.

[Maintained driver](https://github.com/gipson-dev/64CBFD-Tools/blob/master/experiments/game_piecewise_envelope_candidates.py):
eight scope/sum forms, four profiles, **32 controls**, actual SDK, empty
diagnostics; installs nothing. Historical ignored artifacts remain intact in
`game-timed-interpolation-test/`. New `next-volatile.py/log` adds eight correct
pointee-volatile controls, still68 words; `next-lifetimes.py/log` adds32 scope/
compound/independent/operand controls. Earlier `f32 *volatile` casts qualified
the pointer, not its pointed-to float. Neither volatile family solves the gap;
branch-local scope does.

## Qualification

[Nine tests](https://github.com/gipson-dev/64CBFD-Tools/blob/master/tests/test_game_piecewise_envelope_match.py):

- **6480 finite guest cases / three bodies**: raw, derived, retail full external
  storage, ordered accesses, V0=1, saved GPR/FPR/SP/RA, two SP phases, signed/
  zero amplitudes, distinct baselines, strict boundaries and live aliases.
  **66/69 words reached**; duplicate preludes0x15141600/15141648/15141668 not
  forced. Branches/delays and every reachable loop instruction covered.
- **3240 native 32-bit actual-source finite cases**: full actor/timestep storage
  and independent shadow-state pass. Post-install fixture extracts owner C.
- **324 special-float cases / three guest bodies and native C**: ten input
  locations/three phases, signed zeros, subnormals, maximum finite, infinities,
  quiet/signaling NaN encodings. Direct-copy outputs/untouched fields exact;
  only arithmetic NaNs may classify. Derived/retail modeled storage/traces exact.
  **36 other combinations exceed128 reference iterations**: not accepted or
  executed as terminating native calls. Python can quiet signaling NaNs;
  no N64 FCSR/flush-mode/exception/NaN arithmetic payload claim.
- **18 bounded guest loop runs**: three bodies, zero/negative/negative-infinite/
  tiny positive periods, and infinite elapsed. Each hits50000-step budget,
  9995 elapsed stores/no callbacks. Bounded nontermination, not hardware or
  native-hang qualification.
- **Eleven compiled negatives**,30 cases each: gates, arithmetic, plateau,
  wrapping, stale timestep, return/stub. Real storage/access/return differences;
  unsupported instructions never count as successful rejection.
- Real object padder validates13 expected words/relocations, assembles/links
  full276-byte symbol, preserves relocation records and matches every word.
  Production source/prototype/full slot and guard metadata bound explicitly.

Initial eight-test pre-install run failed only start-gate negative fixture:
finite boundary outputs coincided. Add ordered-access comparisons; negative
rerun then exposes missing exact-period-equality input. Add elapsed4; corrected
negative-only run passes in13.639 seconds. Seven other initial methods passed;
the initial eight-test invocation is **not** claimed green.

Completed rebuild/audit against `4a087419`: only **`func_151415D4`** changes
across **6059 fixed slots**; addresses/extents unchanged. `.init`, `.init_data`,
`.debugger`, `.game_data` unchanged; **720 owners / 189088 Game-data bytes**
retail-exact. All **10747 old guards** remain in order, plus13: **10760 total**.
Owner warnings **0 -> 0**, zero new; shared headers unchanged. Target SHA-256:
`62f7911dbb51af41e51a1804cc3e0be90f38ec8bc0ec174560eeec58610c4880`.

Converted counts/bytes unchanged: **5464/6042**, Game **4791/5321**;
**85.57% total / 84.89% Game** converted bytes. Exact **3333/5464 (61.00%)**,
Game **2660/4791 (55.52%)**, **2131 different**, zero drift. Init492/492 and
Debugger181/181 unchanged. Root README changes aggregate rows only.

All **19 focused post-link tests pass in61.523 seconds**, no skips: the complete
nine-test envelope suite plus all ten retained production/metadata methods
whose total guard count changed. This is not a rerun of all earlier suites;
the6059-slot audit independently binds every prior routine's unchanged words.
**38 documents / 3420 relative links / zero broken**; tools, compileall and
diff checks pass. Required build/test sessions terminal, no runtime launch.

Ignored receipts: `conker/build/game-piecewise-envelope-test/`
build/audit/after, controls/guards/padder, special-float/negative/regression
receipts and owner diagnostics. No complete dispatcher/gameplay acceptance.

## Cross-Project And Next Work

Read-only sibling `64CBFDOGL/recomp_out/.c` contains retail-translated envelope
at line975418; no source override found. No import/regeneration/host-adoption
claim, sibling source/build/save/frozen Release, runtime or push change.

Next **`func_151416E8`**, **55 words / 220 bytes**, frame**0x18**, VA
0x151416E8..0x151417C4, ROM0x16EB98..0x16EC74. Optional callback from
`D_8008A02C[actor+0x168 byte]` forwards actor/event/byte command. Then live
event selector must equal payload+0x58 for commands0x22/0x24/0x25: cleanup,
payload+0x59=-1, or payload+0x59=2. Repeated table/index reads, saved argument
homes, callback mutations and narrowing need qualification. Larger
`func_151408A4` and other owner placeholders remain unrecovered.

Ignored `next-events.py/log`, `next-events/measurements.json`: **16 initial
controls**, four payload/switch/argument forms across four profiles, empty
diagnostics. Selected O2/g3: **47 words/frame0x18/49 differences**; switch
49/frame0x18/52; word-command48/frame0x18/52. Retail requires55 words. The
simple typed array form merges the two pre-call table/index reads and payload
address, and changes branch shapes. Recover that source before deriving a
normalization; no next-function semantic/native/padder/production qualification
or installation yet. `D_8008A02C` has only an undefined-symbol anchor, no shared
declaration. Cleanup's SDK pointer type is `struct102 *`; owner adaptation and
table declaration should remain local until validated.
