# Init Decompressor Frame-Backed C And Guest Call Frame Bounds

Date: 2026-10-03. Baseline: `e73223b`.

## Result

The isolated semantic decompressor now supports `INIT_DECODE_FRAME_BACKED`:
scratch arrays occupy the verified physical frame from
[Note 802](802-init-decompressor-physical-frame-mapping-and-contract-tests-20261003.md).
This implements that note's first next step rather than only describing it.
It is not linked into production, and has no original-entry adapter.

The candidate stores guest workspace addresses in the sixteen physical table
cells, reuses the fixed initializer's staging/output cells, and reuses the
dynamic code/literal root and width cells. A separate explicit scalar state
points to the frame. Host differential tests check the actual scratch bytes,
including address representation, rather than only final decompressed output.

Both guest profiles compile with empty logs, but remain overlong: 5,312/5,600
text bytes versus the retained 3,984-byte region. Production remains exact
assembly. Init totals and README aggregates do not change; pending Game
source/tests remain outside this checkpoint.

## Representation

The default candidate retains its owning arrays and 2,668-byte guest state.
The frame-backed variant has a 40-byte guest state: the existing cursor,
output/workspace pointers, reservoir/count/limit/allocation scalars, plus a
frame pointer and explicit nominal guest workspace address. Its caller must
also provide the full 2,696-byte physical frame. The smaller scalar object
does not imply a smaller total memory footprint or original stack compatibility.

The builder writes `workspaceAddress + 4*index` into `frame->tables[level]`
and translates a parent table address back to an index before accessing the
native workspace array. Host pointers are not truncated to manufacture guest
addresses. Direct builder tests cover nominal bases `0x00020000`,
`0x8003BE90`, and `0x807FD000`, with allocation append and table-byte checks.
The core sets the nominal address from its existing explicit workspace-address
argument. Direct builder/initializer test callers set it deliberately.

The fixed decoder temporarily switches the native workspace pointer to its
prebuilt fixed tables without building new tables. The nominal address field
is the builder workspace base, not an exported hardware register contract.
No claim of a working original-ABI register adapter is made.

Scratch accessors let the same algorithm use either owning arrays or frame
cells without a second copied decompressor implementation. Default mode's
measured guest text and state sizes remain the Note 798 baseline. No
production source, compiler profile, assembly owner, or word guard is altered.

## Physical Scratch Evidence

`test_init_decompressor_frame_backed.py` runs the existing nine semantic tests
under the new representation, then adds five physical-contract tests:

1. Empty/all-zero/complete/incomplete/oversubscribed builders and append state
   compare the full `0..0xA37` scratch region, including actual table addresses.
2. Dynamic success, repeat-first, and overflow failure compare scratch plus
   root/width output cells against the retained instruction model.
3. Original fixed-initializer words agree with every scratch byte they write,
   including roots/widths overlaying length cells at `0x9C8..0x9D7`.
4. An independently encoded dynamic stream uses the maximum connected domain:
   286 literal/length cells plus thirty distance cells, exactly 316. It outputs
   `A`, agrees with zlib and the retained model, and preserves frame sentinels.
5. Three distinct guest workspace bases produce correct frame addresses and
   the same table contents without relying on native pointer values.

Tests serialize native words and root halfwords separately into big-endian
frame bytes. Staging bytes are interpreted as word lengths during dynamic
decoding, and as root halfwords only during fixed initialization; treating the
union's inactive root view as always active would corrupt the comparison.
Sixteen-byte sentinels surround the frame. Save/return cells `0xA44..0xA87`
remain untouched, because this is ordinary C with no original-entry adapter.
The oracle's stream scratch is explicitly seeded to the same `0xA5` entry
state as the candidate, following Note 802's fixture-state boundary.

These are bounded native-C versus low-word instruction-model comparisons.
They do not establish arbitrary malformed-tree depth/capacity, aliasing,
invalid-pointer safety, all intermediate root-cell lifetimes on every failure,
guest execution, or exception/FPU-context equivalence.

## Guest Layout And Call Frames

Reproduce both representations from the repository root in WSL:

```sh
python3 tools/experiments/compile_init_decompressor.py
python3 tools/experiments/compile_init_decompressor.py --frame-backed
```

Default artifacts remain in ignored `conker/build/init-decompressor-semantic`;
frame-backed artifacts use `conker/build/init-decompressor-semantic-frame`.
The driver still rejects a mismatch in any of the 24 physical layout values.

| Measurement | Default O2/g3 | Default O1 | Frame-backed O2/g3 | Frame-backed O1 |
| --- | ---: | ---: | ---: | ---: |
| Text bytes | 4,928 | 5,328 | 5,312 | 5,600 |
| Explicit state bytes | 2,668 | 2,668 | 40 | 40 |
| Entry record bytes | 4 | 4 | 4 | 4 |
| Caller-provided physical frame | Not this representation | Not this representation | 2,696 | 2,696 |
| Frame-backed text excess over retail | N/A | N/A | 1,328 | 1,616 |

The driver now resolves `R_MIPS_26` JAL relocations and includes unnamed local
helper entrypoints in an acyclic call graph. IDO omits ordinary function symbols
for helpers such as bit extraction and lookup; reading only exported function
prologues misses their nested frames. The prior `functions` slot measurements
remain export-to-next-export intervals and can contain these private helpers;
the new `call_graph` splits units at the actual resolved call targets.

| Frame-backed entry | O2/g3 direct-call frame bound | O1 direct-call frame bound |
| --- | ---: | ---: |
| `init_decode_core` | 416 bytes | 328 bytes |
| `init_decode_stream` | 392 bytes | 280 bytes |
| `init_decode_dynamic` | 328 bytes | 224 bytes |
| `init_decode_fixed_tables` | 256 bytes | 192 bytes |
| `init_decode_compressed` | 104 bytes | 88 bytes |
| `init_decode_stored` | 80 bytes | 72 bytes |
| `init_decode_build` | 208 bytes | 128 bytes |

These are conservative sums of the accepted direct-call graph's negative
constant SP adjustments, not measured guest runtime high-water. They exclude
the caller-provided physical frame, explicit scalar-state allocation, any
adapter, and the exception caller. They do not prove original stack ownership
or whole-system maximum stack use. The analyzer rejects multiple allocations
in one unit, recursion, unresolved/indirect calls, absolute tail transfers,
and non-word text/targets instead of silently treating them as zero cost.
Five new synthetic tests pin those acceptance/rejection boundaries.

## Verification

- All fourteen frame-backed tests pass (7.905 seconds).
- All 95 Init tests pass (29.907 seconds), including five call-analysis tests.
- Both representations compile under both guest profiles with empty logs.
- Project tool checks and whitespace checks pass.
- All 570 project tool tests pass (95.464 seconds).
- Python syntax checks and documentation link checks pass.
- Production build is up to date; the matcher reports Init 492/492 exact,
  total 3,271/5,463, Game 2,598/4,790, Debugger 181/181, and zero drift.
- Independent linked ELF extraction remains retail-exact: `.init` 164,048
  bytes, SHA-256
  `34372ebc8b2e56b5b6c02c8b88ce33a1558d5d329397fdc6e9e984333df6d4bf`;
  `.init_data` 17,376 bytes, SHA-256
  `a3d3d56157fd9f9feb00a48a526c50ec51227b5a5afc277aa9a4b765c8fc6239`.

The known duplicate Makefile recipe warning remains. No gameplay,
original-entry adapter, matching production conversion, sibling-port build,
or Release change is claimed. This Init experiment and its handoff are banked
separately from the still-pending Game recovery source/tests.

## Next

1. Recover adapter placement and exception/FPR/stack/workspace ownership before
   using the physical frame in a production caller. Note 802's unconditional
   exception `f0` restore delay remains an explicit qualification gate.
2. Develop a code-generation representation addressing both overlong text and
   ordinary nested C frames. The smaller explicit scalar object alone does
   not settle either obstacle; do not copy retail words over this C body to
   manufacture a conversion.
3. Preserve root/staging lifetimes on additional failure paths and characterize
   any direct/indirect external helper contracts before changing ownership.
4. Only adopt an actual fitting, semantically/ABI-qualified candidate with
   independent complete-slot and whole-Init verification. Keep the existing
   exact assembly baseline intact in the meantime.
