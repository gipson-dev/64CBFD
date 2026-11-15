# 2487 - Side-ring renderer setup and geometry proof components

`func_1519FE6C` now has maintained symbolic component proofs for its six
graphics providers, initial seed, signed texture calculations, initial
three-vertex strip, repeated segment, lookahead and ABI return. Together with
the existing opening/fade proof, these exercise **72 component paths** and
reject **59 deliberate corruptions**. The components have not yet been joined
into a complete whole-function proof or normalization recipe.

The same private candidate remains **637 words / frame 0xF0**, with **621
positional word differences**, five excess words and S0-S3 rather than retail's
S0-S2. Production remains uninstalled/uncredited at **4,512 / 5,514 (81.83%)**,
Game **3,839 / 4,841 (79.30%)**, zero drift; **175** more matches to 85%.
No source, compiler profile, guards or aggregate README rows changed.

## Component evidence

All modules live under `tools/tests/game_side_ring_renderer_1519fe6c_`:

| Component | Symbolic paths | Effective corruptions | Checked transfer |
| --- | ---: | ---: | --- |
| `opening_proof.py` | 26 | 10 | Entry, allocator, inductive fades; unchanged checker rerun |
| `setup_proof.py` | 1 | 6 | Six opaque graphics calls, arguments, sync and captured pointers |
| `seed_proof.py` | 18 | 10 | Attached/ring seed, wrapping, epsilon normalization, FP/FCSR order |
| `texture_proof.py` | 12 | 10 | Signed halfwords, negative remainder, midpoint, mode orientation |
| `vertices_proof.py` | 2 | 7 | Initial three vertices, thirty public writes and next-loop negation |
| `segment_proof.py` | 4 | 9 | Arbitrary loop state, thirty vertex plus ten command writes, wrapping |
| `tail_proof.py` | 8 + 1 return | 7 | Lookahead, exact-zero normalization, repeat delay and saved ABI return |

The setup proof permits arbitrary o32 caller-state, public-memory and FCSR
changes by each provider. Packet and entry pointers captured before the calls
remain live across all six. The exposed sync address stays incoming-SP **-95**;
the allocator's cursor home stays **-4**.

Seed and texture models make unmodelled registers differ between streams and
reject uninitialized private reads. Seed width lives at **-40** in the candidate
and **-76** in retail; the high texture pointer is privately spilled at **-148**
in the candidate and retained in retail T5. Private-write inventories and live
values account for these differences without modifying production storage.

The seed calculation narrows opacity earlier in C. The vertex/segment models
therefore begin with a narrowed candidate byte and an arbitrary wider retail
value, then compare the actual byte consumers. A separate positive control
defers candidate narrowing and still passes. The initial epsilon remains
**0.0001f**; later joins retain their separate exact-zero comparisons.

The segment model verifies all three complete vertices and the VTX/four TRI1
commands in order, allowing arbitrary aliases among public output, effect and
record memory. It explicitly carries the current-point copy pointer from the
wrap branch's delay slot into lookahead. The initial lookahead probe omitted
that model input; different dead-register tokens exposed the omission. The
interface invariant was added before qualification, rather than equating the
unmodelled registers. Return tests dirty RA and F20-F23 before restoration and
require all saved GPR/FPR values and the output cursor to return correctly.

## Ordinary-memory and floating-point domain

All modeled public accesses target mapped ordinary RAM, with no asynchronous
writer or MMIO side effects. Seed has no public stores/providers; its read
addresses, widths and multiplicities may commute across FP operations while
FP/FCSR order remains exact. This does not claim raw read timing or fault-PC/
register identity. FP traps are not assumed disabled: ordered FP opcode,
operands and incoming status are retained independently of these mapped reads.

Texture permits duplicate stable ordinary reads to differ. Its cache retains
a value across a public store only when modular address/width arithmetic proves
the byte ranges disjoint. This accounts for the extent halfword at packet+0x4A
moving across the packet+0x46 store. Exact-address stores forward their narrowed
value; possibly aliasing cached reads are invalidated. Signed-width identities
are applied only with checked bit masks or proven integer intervals. Ordered
public writes and FP/FCSR operations remain checked without commutation.

Independent scratch allocations pass in setup, seed and texture. Positive
controls also defer opacity narrowing and replace a redundant texture read with
its retained value. Negative controls cover fields, widths, signs, mode gates,
remainder adjustment, FP operand/order changes, all vertex classes, command
indices/pointers, loop steps, delay annulment, private homes and ABI restoration.
These are instruction-driven component checks, not a retail-word template or
an all-input portable-C/hardware validation claim.

## Fresh checks and reused evidence

Seven focused symbolic tests pass in both tools configurations, including the
unchanged opening checker. Primary elapsed **23.782 seconds**; sibling
**24.84 seconds**, including startup. Thirteen task-file hashes are
captured before/after each suite. Both suites also freshly compile the complete
owner and all three pinned recoveries: raw 637 / 639 / 648 words and their 13
relocations remain fixed, all **38 neighbors** and pools are preserved, and all
**881 frozen production inputs** remain byte-identical. `make tools-check`
passes separately.

The Note 2486 guest/native/caller receipts are explicitly **reused**, not rerun:
299 guest cases per four streams, 299 native cases per six compiler/alias
profiles, UBSan/twelve controls, 128 connected allocator/dispatcher cases per
stream and lazy-pointer tests. Their compiler/source/oracle/native/caller/
opening fingerprints and production inputs are unchanged. The unit diff adds
only six new methods, leaving the earlier checks intact; this exact amendment
and both prior suite receipts are retained. No new production-Make/full-image
adoption check is claimed.

The sibling overlay preserves its HEAD and all **2,434** dirty paths byte-for-
byte. No host-port source/build applies; frozen Release artifacts and saves
remain untouched. Zero Claude calls were needed. Scoped AST extraction retains
old graph IDs; the native update still refuses a shrinking replacement. No
force or upgrade was used. Commit-hook IDs and the explicit target edge are
audited separately; no full-corpus re-extraction is claimed.

Candidate raw SHA-256:
`4f1d014df4dccc1d394183098667e837cda18e904d9992ad952a134af72b9b0a`.
Production ELF SHA-256:
`902b8b86f8ffc963c593e33b844245bf4d295dd69bd42944159f66be2b92d20e`.
Receipts: `conker/build/game-side-ring-renderer-1519fe6c-private/frame-2487/`.

Reproduce the full maintained target suite in the prepared consumer:

```sh
python3 -m unittest tools.tests.test_game_side_ring_renderer_1519fe6c_recovery -v
make tools-check
```

Continue with explicit cut-invariant composition and complete reachable-code
coverage, then derive a constrained normalization for saved-register/private-
home changes, scheduling, read reuse, branch forms and the five-word size gap.
Component success alone does not authorize copying the retail body over the
compiler output. Both padders, independent rebases, actual Make, strict image,
production recount and documentation gates remain prerequisites for adoption.
