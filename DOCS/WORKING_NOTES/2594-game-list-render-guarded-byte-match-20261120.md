# Note 2594: List-flare renderer guarded byte match

Date: 2026-11-20. Consumer baseline `2596163a024dc1fb591bc6d2de8f2fd14bbfc6ff`;
tools baseline `05ed56bc3c15b99ceb25dd4a375b4ca8131c234d`.
Qualified tools commit: `cc9cfc5cea8da04075fe1a81bcd51c60a927160c`.

`func_1517E28C` replaces its zero-return placeholder with complete semantic C
and matches **all 135 retail words / 540 bytes / frame 120** after **43 checked
word/binding rows**. Raw C emits 132 words. This completes the uncredited
recovery in [Note 2593](2593-game-list-render-private-recovery-20261120.md).

Fresh production recount: **4,579 / 5,527 (82.85%)** total, **3,906 / 4,854
(80.47%)** Game, zero drift and 948 still different. Init 492/492 and Debugger
181/181 remain exact. Converted totals remain 5,527/6,048 (91.39%), 86.54% of
bytes. **119 more** matches are needed for 85% at this denominator; the goal
remains active. The root README changes only its two affected aggregate rows.

## Interface, state and caller

Owner `conker/src/game/generated_1AB530.c`; VA `0x1517E28C..0x1517E4A8`, ROM
`0x1AB73C..0x1AB958`. The 135-word slot has no alignment tail. The interface is
`Gfx *(Gfx *commands, s32 unusedCategory)`. The sole aligned-ROM direct JAL is
at `0x46FD0`; no literal target pointer is found, and computed callers remain
unexcluded. `game_45B80.c` now declares the pointer-return interface and passes
the cursor directly. All **16 caller functions, bindings and pools**, and the
**entire padded caller object**, remain identical. Its three existing Warning
712 messages are preserved, with only temporary filenames normalized.

The renderer captures the list head, clears D_800DDD60 and visits enabled nodes
at +0x30. It copies the two-byte group/count/falloff palettes `{0,1}`, `{7,3}`
and `{1,30}` into **SP+0x60/+0x5C/+0x58**. Flag 0x01 selects the gated fixed
point projection through `func_1517EAAC`; otherwise `func_1517EC1C` supplies
sampled depth. Both must return exactly one. Strength is 255/-1 for the point
route and 256/-1 for the signed wrapped depth difference below 30.

Flags are refreshed after helpers. Mask 0x02 chooses the optional D_800DD2D0
intensity pointer, which is cleared on a skipped record. Successful records
submit the cursor, node, selected group/count/falloff, strength and pointer to
`func_1517E4A8`, then adopt its cursor. The next link is read after helper effects;
the captured head is retained. The large draw helper remains a production stub;
only its pointer return type is repaired here without changing its bytes.

The **strength carry at SP+0x74** and **sampled depth at SP+0x6C** remain
uninitialized until their original paths write them. The depth helper can leave
its output untouched. No speculative zero, NULL or index gate was added.
All seven other raw owner functions, bindings and pools remain unchanged.
The 32-byte point/selector/palette block agrees in ROM and production ELF.

## Closed instruction derivation

Supported debug profiles and volatile/register-hint experiments did not recover
the layout. Volatile strength happens to produce 135 words but adds non-retail
memory accesses and changes saved roles, so it was rejected. The existing O2/g3
profile, 120-byte frame, saved roles and passed homes are retained.

The derivation consumes the exact raw payload SHA-256
`673fc386318f7a0843b64ca6459e55b846c499258bb536e0c780598798b49af5`
and exact relocation map. It retains **130 unique source origins** and removes
two duplicated operations: source word **67**, one conditional copy of the
sample halfword read, and word **76**, a duplicated flag-mask calculation.
The halfword read becomes a common read and the mask is evaluated on the
shared continuation. An independent proof checks their normal-execution effect.

Five output origins are added: control-delay NOPs at **45/71**, branch
continuations at **73/89**, and retail's unreachable duplicate flag read at
**91**. Net length is 132-2+5=135. Two likely branches become normal branches
with their corresponding delay-slot schedules. The depth-output address moves
to its call delay, and strength assignments return to their post-helper
positions. Branch targets and bindings are remapped from source origins.

The generator does not read ROM or original assembly to produce its output.
Independent assembly then confirms **all derived bytes and bindings equal the
original**, and two GNU link configurations, including code/data rebases and
low-half carry changes, agree. Payload and binding corruptions are rejected.
The CSV contains the same five insertions/two omissions, with 43 expected-word
and expected-binding rows. No whole-body replacement array is installed.

## Independent relation and focused tests

An instruction-driven proof is separate from the derivation. It checks **two
prefix paths and 38 iteration paths per palette choice**, composing one
iteration inductively for valid lists. It covers **132/132 raw instructions**
and **134/135 retail instructions**; retail word 91 is unreachable. Ordered
public writes, ABI arguments/calls, FCSR, all **144 private/incoming bytes** at
each call and exit/cut, returned cursor, loop carry and saved registers agree.
Eight semantic controls reject output-home, threshold, arithmetic, route-mask,
sample-sentinel, intensity-clear, saved-return-home and next-link errors.

The proof permits arbitrary public and retained-depth mutations by providers,
with ordinary reads stable between writes/calls. It requires valid disjoint
private storage, palette indices zero/one and the non-null point selector one.
Providers cannot inspect implementation PCs, unpassed locals or non-argument
registers. The verified readonly block remains immutable. This is normal
execution equivalence, not raw fault-register, timing or hardware parity.

Eight tests pass in each tools configuration **before and after installation**.
All **339 imported Python fingerprints** agree. The isolated bundle has
1,056 files: 347 matching sibling files, 701 primary fallbacks, seven task files
and one bootstrap. The real dirty sibling preserves HEAD, status and **351
dependency hashes**; it was neither overwritten nor committed.

The independent guest/reference comparison passes **1,024 cases per stream**,
including helper mutation, retained output, both stack phases, full-byte flags,
exact-one returns, empty lists, link changes, cursor and intensity effects.
All final public/private bytes, calls and returns agree. Four effective guest
instruction controls pass. Native SDK32 O0/O2/O3 each pass **745 cases** with
strict aliasing and UBSan; three source controls reject unsigned comparison,
nonzero-as-success and stale flags. Native inputs initialize the first sampled
depth before its read; later untouched outputs may retain that value. Guest
ambient reads are not claimed as defined portable C. Full downstream helpers,
parent execution, arbitrary private aliases and gameplay are not qualified.

## Actual build and literal image audit

Both layout and original-assembly padders produce the same complete owner
object. Actual Make executes **five renderer commands and three caller commands**
with the existing profile. The production build and installed suites pass.
The complete ELF equals a **452-byte prediction with zero exclusions**: target
code, its size from 12 to 540, and a closed three-name metadata rotation.
Baseline order `D_8008D008 / func_1503FB40 / D_8002BBE0` becomes
`func_1503FB40 / D_8002BBE0 / D_8008D008`. All named definitions are preserved;
48 symbol-table and 36 string-table bytes are rebuilt from the frozen records.

All **6,051 function slots/addresses** and **189,088 protected data bytes** are
preserved. The complete padded caller object and conversion CSV are identical.
Original guard bytes remain an exact prefix; only the 43 derived rows append.
All 2,140 frozen inputs are checked against the explicit task plan. ELF SHA-256:
`733102bfb973c3af410d3b3722a64132f475425a990877112eccc893b8ad239a`.

The scoped graph merge retains old IDs and qualification metadata. Native
Graphify's full scan remains subject to its shrink guard; no full-corpus
extraction is claimed. No Claude model call, push, save or Release action was
performed. The legacy 64CBFDOGL path has only `.codex`/`recomp_scene`, without
an active Git/source checkout; there was no host source change or build.

Reproduce from the prepared consumer root:

```sh
python3 -m unittest tools.tests.test_game_list_render_1517e28c_match -v
```

Next: qualify the remaining list unlink/free routine `func_1517E134` in this
owner, retaining the now-matched renderer and both projection/depth helpers.
