# Init Post-Pause Assembly Conversion Assessment

Date: 2026-10-03. HEAD: `47f7ce85`.

Follow-up: [Note 802](802-init-decompressor-physical-frame-mapping-and-contract-tests-20261003.md)
implements the physical frame map with guest/native offset and differential
scratch tests. This completes a bounded mapping step, not a production adapter
or matching conversion; its remaining context/layout gates supersede the
unexecuted decompressor mapping step below.

## Decision

Some remaining Init assembly is expressible in C, but none currently has a
proven additional byte-exact production C replacement. Init is not blocked
on 47 ordinary missing C bodies. Its remainder includes original SDK
assembly, privileged operations, and connected nonstandard entry contracts.

The two small matching-conversion candidates remain `func_10005BE0` and
`func_100038E0`. Their behavior is characterized; the unresolved question is
compiler output, not an unknown algorithm. The decompressor already has
tested experimental C, but not the original guest ABI or a fitting layout.
Retain production assembly until those separate requirements are established.

This assessment resumes the user's Init request after the pause. Existing
uncommitted Game updater source and tests are preserved. They are not part of
this Init assessment, and this note does not claim to finish or bank them.

## Fresh Baseline

Structured inspection of `conker/progress.init.csv` gives:

| Representation | Functions | Bytes |
| --- | ---: | ---: |
| C | 492 / 539 (91.28%) | 151,796 / 164,048 (92.53%) |
| Assembly | 47 | 12,252 |

`make -C conker NON_MATCHING=1 all match-progress -j4` succeeds. The build is
up to date; the matcher reports Init 492/492 exact, zero address drift, and
zero different C functions. All 67 tests selected by `test_init*.py` pass
in 19.479 seconds.

Independent big-endian ELF32 section extraction compares the complete linked
sections directly with the pristine `conker/conker.us.bin`:

| Section | Bytes | SHA-256 |
| --- | ---: | --- |
| `.init` | 164,048 | `34372ebc8b2e56b5b6c02c8b88ce33a1558d5d329397fdc6e9e984333df6d4bf` |
| `.init_data` | 17,376 | `a3d3d56157fd9f9feb00a48a526c50ec51227b5a5afc277aa9a4b765c8fc6239` |

The known duplicate Makefile recipe warning remains. These are static linked
and bounded host/model checks, not MIPS hardware execution or gameplay proof.
No full all-project test rerun or new compiler experiment is claimed here.

## Remaining Assembly

| Group | Rows | Bytes | Conversion decision |
| --- | ---: | ---: | --- |
| Bitmap `func_10005BE0` | 1 | 76 | C behavior demonstrated; full nineteen-word compiler match remains open |
| MMIO `func_100038E0` | 1 | 44 | C store trace demonstrated; full eleven-word match remains open |
| Separated SDK assembly | 19 | 2,288 | Retain original SDK implementations; not missing compiler-generated C |
| Boot `func_10001000` | 1 | 80 | Retain the clear-and-jump entry contract |
| Hardware/context/setup | 8 | 4,376 | Requires assembly/intrinsics and connected ABI work, not pure-C substitution |
| Shared-frame decompressor | 10 | 3,984 | Experimental C exists; recover original ABI/frame and fitting layout before production conversion |
| SDK thread queue leaves | 2 | 96 | Algorithms are C-expressible; original SDK assembly remains the exact owner |
| Cleanup/debug/glyph | 5 | 1,308 | Recover connected interior entries and live-register/link contracts first |
| Total | 47 | 12,252 | No new production conversion in this assessment |

The complete routine list and concrete register evidence are in
[Note 735](735-init-retained-assembly-reassessment-20261002.md), whose 48-row
historical inventory includes the subsequently converted `func_10001420`.
[Note 792](792-init-resume-remaining-assembly-conversion-decision-20261003.md)
contains the current 47-row grouping. Both agree with the fresh CSV count.

## What Can Be Converted Next?

### Bitmap: Smallest Ordinary C Candidate

The actual assembly in `conker/asm/init_5AB0.s` captures the start/end pointers,
stores `0xFF` inclusively before testing the endpoint, increments in the loop
branch delay slot, then reloads the signed count and masks the last byte for
a nonzero low-three-bit remainder. The neighboring routine begins at
`0x10005C2C`; an overlong body is not a valid replacement.

Caller and conditional allocator ownership evidence are already established
in Notes 788/789. Do not repeat that investigation as an unresolved first step.
The 55-shape/profile matrix in Note 751 did not match. The later volatile-store
trial in [Note 799](799-init-bitmap-volatile-store-scheduling-trial-20261003.md)
also failed: all three optimized forms emit twenty words rather than nineteen,
although all 237 host shape/case combinations pass.

Next attempt only with a new, explicit code-generation hypothesis explaining
the store/test/increment schedule and tail decrement. Keep candidates isolated;
do not add a zero-count early exit, hoist the post-fill count read, or normalize
an entire different control-flow body with instruction guards.

### MMIO: Small C Candidate With Ordered Hardware Stores

The retained source owner is `conker/src/init_38E0.c`; its assembly publishes
word `0xBC000C02` to `D_80038070`, halfword `0x4040` to `D_80038074`, then
writes halfword `0x4040` through the published address. Retail retains the
address register, materializes the value twice, and returns with a nop delay.

[Note 762](762-init-mmio-partial-volatility-trials-20261003.md) tested twenty
partial-volatility/profile variants. Their checked emitted store traces agree,
but no eleven-word retail match results. Equal length alone is insufficient:
the eleven-word variants still rematerialize the base and move the hardware
store into the return delay slot. Hardware behavior and host portability are
not established by these modeled traces.

Next attempt needs a source/compiler explanation of that address lifetime and
constant materialization, preserving volatile width/order and the full slot.
Repeating the same profile matrix is not a new conversion step.

### Decompressor: Substantial C Recovery, Not Ready To Link

`tools/experiments/init_decompressor_semantic.c` already implements the connected
algorithm and passes its nine differential tests. The follow-up in
[Note 798](798-init-decompressor-guest-layout-trial-and-conversion-boundary-20261003.md)
measured 4,928/5,328 guest text bytes against the retained 3,984-byte region.
Its 2,668-byte explicit state does not reproduce the original shared frame,
integer FPR state, helper entrypoints, or live-register interface. Even before
an adapter, these candidates exceed the available region by 944/1,344 bytes.

The next useful decompressor work is an explicit mapping from candidate state
to the original `0xA88` frame and live registers, with a caller/interior-entry
ledger and exception-workspace ownership evidence. Then prototype an isolated
original-ABI entry adapter and measure total text and maximum nested stack.
Do not mistake a smaller C algorithm or successful compilation for an exact
production ownership transition.

## Restart Checklist

1. Choose the objective: a byte-exact small Init conversion, or connected
   decompressor ABI recovery. These have different acceptance gates.
2. For a small conversion, write down a genuinely new bitmap/MMIO scheduling
   hypothesis before compiling. Preserve completed negative trial evidence.
3. Compile/link only isolated candidates; compare the entire original slot,
   including padding/delay slots, and establish any normalization equivalence.
4. For the decompressor, map frame/register ownership and all actual entry
   contracts before linking candidate C or changing its assembly owner.
5. Adopt production C only after semantic, ABI, slot-size, and matching checks;
   rerun focused tests, regenerate inventories, and compare both whole Init
   sections. Update README aggregates only for an achieved owner transition.

If both small candidates succeed, Init would reach 494/539 C functions (91.65%)
and 151,916/164,048 C bytes (92.60%), leaving 45 assembly rows / 12,132 bytes.
These are conditional targets, not current progress. A hardware-backed,
fully C-expressed redesign is a different objective from byte-exact decomp.

No production Init source, SDK assembly, compiler profiles, word guards, README
aggregates, sibling-port artifacts, or Release configuration changed here.
