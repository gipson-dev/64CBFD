# Rate-driven emitter direct byte match - 2026-11-27

`func_150E9E34` in `conker/src/game/generated_116D40.c` now contains the
complete rate-driven particle-emission callback. Its **105 words / 420 bytes**
match retail directly after two checked literal relocation bindings. There
are **zero text-word guards**, insertions, omissions or instruction rewrites.
The retail 144-byte frame, saved GPR/FPR lifetimes and delay-slot work match.
VA body `0x150E9E34..0x150E9FD8`; ROM `0x1172E4..0x117488`. Two original
alignment words extend the slot through VA `0x150E9FE0` / ROM `0x117490`.
The existing O2/g3/mips2/o32 compiler profile is unchanged.

Actual production: **4,719 / 5,528 (85.37%) total**, **4,046 / 4,855 (83.34%)
Game**. Init remains 492/492; Debugger 181/181. Zero address drift, 809 still
different. This adds exactly one match, with conversion rows and denominators
unchanged. The **90% goal remains active**: **257 further matches** reach
4,976/5,528. Tools commit: `decfdf86688de5f2181017129fd9923e978e947f`; consumer baseline: `ceaad815`.

## Recovered interface and behavior

The original 104-entry `D_8008A4E8` callback table points index 41 at this
routine. The complete 45-word `func_15149264` invokes it as
`void (*)(struct260 *)`. The extended owner embeds `struct260` as its first
member, preserving that public interface and the valid containing-object
cast. Its emitter subobject begins at offset 0x28 and contains a descriptor
pointer, base/range emission rates, base/range scales and an accumulator.

One floating RNG call contributes to the rate even when the gate skips.
The accumulated rate uses the original ordered single-precision expression
and `D_800BE9A4`. Only an accumulator **strictly greater than one** emits.
Each emission obtains its random scale and position, calls the integer RNG
twice, and passes `first & 255`, `64 - second % 129` and the ordered
`random * 600.0f * 0.01f` speed to the angle helper. Both integer results are
explicitly unsigned before the remainder operation. Position and velocity
occupy distinct live local vertices. Mode/identity bytes at owner offsets
12/1 are loaded after the helpers. The accumulator is reloaded after the
submission provider, reduced by one, and tested again. NaN gates skip;
no all-input termination claim is made for an infinite accumulator.

The same-owner `func_150E9890` remains an unfinished zero-return C stub.
Only its interface is repaired: position/velocity pointers, a floating scale
and two 32-bit mode/identity words. This changes the compiler stub from three
to seven words because of its argument homes. **It receives zero matching
credit**. The strict image audit explicitly includes that body and symbol-size
delta; it is never excluded as an unchanged neighbor.

## Checked literal binding

The compiler emits one 16-byte pool: `0x3C23D70A` (0.01f), followed by twelve
zero alignment bytes. The new per-owner checker pins the entire compact text,
both function extents and body hashes, every relocation, the exact allocated
non-writable pool, and its two zero-addend HI16/LO16 references. Only those
two relocation symbols are transferred to original `D_800A140C`; no
instruction word is changed. The original ROM at 0x245ECC and the frozen
linked image at 0x800A140C independently confirm the same four literal bytes.
No shared padder implementation or retail word-patch CSV changes are made.

An explicit US Make recipe runs compiler, checker/binder, assembler, existing
padder and final assembler. A compiled source control using **0.02f** retains
all target words and bindings: an unchecked address-only map would hide the
mistake in both padders. The new checker rejects it. The actual expanded
recipe executed through GNU Make stops at the checker, before producing a
bound or final object. All 128 pool-bit controls, 112 target/provider word
controls, twelve relocation controls and further malformed-section/extent
controls reject: **268 effective rejection controls** in total.

## Qualification and limits

- Actual SDK/native32 C: **1,123 cases at each of O0/O2/O3**, separate
  translation units, strict aliasing, trapping UBSan and LTO type checks.
  The real 64-bit RNG transition and its low-halfword float coefficient are
  exercised without inventing owner mutations by RNG. A header-first owner
  is passed through the correctly typed callback. Seven semantic controls
  fail with logical exit 42, including signed remainder, wrong strict gate,
  wrong literal, identity byte, rate range and decrement.
- Guest: **1,123 cases per stream / 4,492 executions** of retail, raw-bound
  C and both padded streams. Complete terminal machine state, memory,
  ordered accesses, helper argument payloads and seed effects agree. Three
  pointer domains and both stack phases are covered. All **104 reachable
  words** execute; original word 70 is the unreachable divide-by-zero break
  for constant divisor 129 and is retained. **125 access-fault quadruples**
  preserve complete prefixes. This is emitted-code qualification; floating
  exception/FCSR behavior and portable C fault semantics are not emulated.
- Original caller: **576 connected executions**, the complete original
  45-word dispatcher and all 104 original callback-table entries pinned.
  All 45 caller words execute. Signed callback -1, timer/flag/end/release
  paths and three child return poisons preserve effects.
- Position, angle and submission helpers use explicitly bounded providers.
  Their modeled mutations exercise load lifetimes; these do not qualify the
  complete helper bodies or establish whole-program/gameplay parity.
- Both complete padders reproduce the frozen before object and agree on the
  selected owner. **Twenty independent GNU links** cover four rebases,
  separate global/helper addresses and signed HI16/LO16 carry boundaries.
- Actual five-command Make and an independent frozen-before-C plus ABI-only
  provider C and original target assembly predict the **entire ELF**:
  **347 changed bytes, zero exclusions**. Production Make, independent image
  equality and a fresh actual-ELF recount confirm the result. All **720 data
  owners / 189,088 protected bytes**, unrelated bodies, addresses and prior
  guards remain unchanged. No new compiler or Make diagnostics; six existing
  duplicate-recipe warnings for unrelated owners remain unchanged.

Five focused tests run freshly from both primary tools and an isolated tools
copy before and after installation: **20 successful fresh tests**. The real
dirty sibling tools checkout, including its 353 base and three additional
recorded dependencies, is preserved. Shared `make tools-check` passes. An
initial isolated-runner SDK include-path issue was corrected in the harness
before these successful paired checks; it did not change production C.

One tool-disabled, packet-only Claude review found no actionable defect.
Its identified dependency on the retail literal is checked independently
against the ROM and frozen ELF as described above. Codex verified the review;
no second writer, subagent, automatic review loop or publication was used.

Graphify is queried and refreshed with a scoped AST extraction and explicit
retention of prior IDs/qualification metadata. This is not a full-corpus
re-extraction. Current definition metadata marks the emitter qualified and
the provider ABI-only/unmatched. Final graph/hook/bank receipts are retained
in `conker/build/game-rate-driven-emitter-150e9e34-private/`.

The sibling host's generated `recomp_scene/cd64_out/func_150E9E34.c` is an
empty recompilation output stub. Read-only inspection supplies no active
host implementation to transfer or qualify. Host Release remains frozen;
no host build, launch or gameplay acceptance is claimed.

Next: continue ordinary unmatched Game qualification from this committed
checkpoint. N82 `func_1514EECC` remains parked pending its separate proof.

Paired installed receipt:

```json
{
  "labels": [
    "installed-primary",
    "installed-sibling"
  ],
  "passes": true,
  "fresh_tests": 10,
  "reused_tests": 0,
  "equal_report_rows": 7,
  "primary_imports": 321,
  "sibling_imports": 322,
  "equal_tool_data_inputs": 248,
  "independently_copied_task_files": 9,
  "closed_tools_root_proved": true,
  "source_installed": true,
  "matching_credit": 0
}
```
