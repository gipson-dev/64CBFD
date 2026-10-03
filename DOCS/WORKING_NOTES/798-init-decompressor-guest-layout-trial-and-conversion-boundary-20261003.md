# Init Decompressor Guest Layout Trial And Conversion Boundary

Date: 2026-10-03. Baseline: `e7d7ea2`.

## Result

The isolated semantic C from [Note 797](797-init-connected-semantic-c-candidate-and-differential-oracles-20261003.md)
now compiles with the repository's IDO 5.3 guest compiler in two bounded
profiles. Neither object is a production replacement. Both exceed the
retained decompressor region, expose a different explicit-state ABI, and
do not reproduce the original shared-register/frame entry contracts.

Production ownership remains assembly. Init remains 492/539 C functions,
47 assembly rows / 12,252 bytes, and 492/492 byte-exact C functions.
No README aggregate increase, production word guards, sibling-port build,
or Release change is made.

## Reproducible Guest Trial

Run from the repository root in WSL:

```sh
python3 tools/experiments/compile_init_decompressor.py
```

The driver builds only the experimental source, writes objects/logs/
disassembly/measurements into ignored `conker/build/init-decompressor-semantic`,
and never links them into production. `--output` selects another artifact
directory. `INIT_DECODE_GUEST` supplies the original compiler's basic integer
types without modern host headers and exports layout sizes for ELF inspection.

Common flags are `-c -32 -G 0 -Xfullwarn -Xcpluscomm -signed -nostdinc
-non_shared -Wab,-r4300_mul -mips2 -o32 -DINIT_DECODE_GUEST`.
The two profiles are `-O2 -g3` and `-O1`. Both compiler logs are empty.

The first invocation used absolute source/output paths containing workspace
spaces. It returned success without producing the object. Relative paths
from `conker` produce both objects; the driver now removes any stale target
first and requires a newly produced object before measurement. Compiler exit
zero alone is not an artifact receipt.

The report parses big-endian ELF32 MIPS sections/symbols. Function slots run
to the next text function or section end. Body extent runs through the last
`jr ra` and its delay slot; frame measurements identify opening negative
`addiu sp,sp` instructions. These are bounded layout measurements, not a
control-flow equivalence proof or maximum nested-stack calculation.

| Measurement | `-O2 -g3` | `-O1` | Retained assembly |
| --- | ---: | ---: | ---: |
| Text bytes | 4,928 | 5,328 | 3,984-byte region |
| Text words including padding | 1,232 | 1,332 | 996 |
| Entry record bytes | 4 | 4 | 4 |
| Explicit state bytes | 2,668 | 2,668 | Shared frame/register scratch, different ABI |

The original region contains 3,976 instruction-body bytes plus eight padding
bytes. Candidate text exceeds the full region by 944 or 1,344 bytes before
any original-ABI adapter or data placement is addressed. This rules out
these two objects as direct exact replacements; it does not prove no other
source/compiler representation can match.

| Candidate | O2 slot words | O2 frame bytes | O1 slot words | O1 frame bytes |
| --- | ---: | ---: | ---: | ---: |
| `init_decode_build` | 576 | 208 | 575 | 128 |
| `init_decode_compressed` | 131 | 64 | 122 | 56 |
| `init_decode_stored` | 55 | 48 | 74 | 40 |
| `init_decode_fixed_tables` | 82 | 80 | 95 | 72 |
| `init_decode_dynamic` | 208 | 160 | 250 | 112 |
| `init_decode_stream` | 78 | 64 | 90 | 56 |
| `init_decode_core` | 47 | 24 | 69 | 48 |

Core body extents are 46 and 68 words, respectively; its slot includes one
padding word in each profile. The original core frame is `0xA88` / 2,696 bytes.
The candidate's 2,668-byte state is comparable in size but has not been mapped
onto that frame. Allocating it in a new adapter plus ordinary nested helper
frames must not be described as preserving the original stack contract.
Object compilation does not execute guest code or resolve exception/FPR state.

## Bounded Malformed And Scratch Evidence

Two oversubscribed-tree fixtures extend the existing semantic builder test:
`[1,1,1]` at root width one returns zero, and `[2,2,2,2,2]` at root width two
returns one. In both cases candidate status, root/width/allocation, and table
bytes agree with the retained instruction-word model. This preserves the
observed algorithm rather than introducing a general oversubscription reject.
It is not exhaustive malformed-tree qualification.

Source inspection narrows the connected callers' length domain: code-length
alphabet entries come from three-bit reads; decoded lengths are symbols below
16 or repetitions of those values (previous starts at zero). Fixed literal
lengths are seven/eight/nine and fixed distance lengths are five. Builder
counts are 19, 288, 30, or dynamic literal/distance counts at most 286/30.
The combined dynamic length array therefore needs at most 316 entries within
the candidate's 320 cells. This is a source-domain argument for these connected
calls, not a guarantee for arbitrary external builder inputs or invalid table
reads. Lengths above 16, capacity exhaustion, and arbitrary aliasing remain
unqualified; no unsafe native fixture is added to pretend otherwise.

`func_10003930` assigns startup `D_8003809C` to `0x803FE000` or `0x807FE000`.
These addresses are 8,192 bytes below the nominal end of the corresponding
4/8 MiB range. Startup uses that address as workspace. The arithmetic is not
a proof that every decompression path owns 8,192 writable bytes. In particular,
the exception workspace at `D_800340E8`, dynamic allocation maximum, original
scratch aliasing, and indirect/external entry contracts still need separate
evidence. Existing A5-seeded differential fixtures do not cover every physical
stack alias or memory ownership scenario.

## Verification

- All nine semantic differential tests pass, including the two added cases.
- All 522 tool tests pass (205.453 seconds).
- Guest compiler/layout trial and Python syntax check pass.
- `make tools-check` passes.
- `git diff --check` passes.
- `make -C conker NON_MATCHING=1 all match-progress -j4` succeeds; production
  is up to date and Init remains 492/492 exact with no drift/different C rows.
- Independent ELF section extraction compares equal to the pristine image:
  `.init` 164,048 bytes, SHA-256
  `34372ebc8b2e56b5b6c02c8b88ce33a1558d5d329397fdc6e9e984333df6d4bf`;
  `.init_data` 17,376 bytes, SHA-256
  `a3d3d56157fd9f9feb00a48a526c50ec51227b5a5afc277aa9a4b765c8fc6239`.

The known duplicate Makefile recipe warning remains. These checks do not
establish gameplay behavior or a production C ownership transition.

## Next Conversion Work

1. Keep the decompressor as exact assembly with its tested C reference. A
   matching conversion needs a new representation of the connected register,
   frame, entrypoint, and exception contracts, not another unchanged profile
   sweep or instruction replacement of most generated words.
2. For a small Init conversion, target `func_10005BE0` (bitmap, 19 words) or
   `func_100038E0` (MMIO, 11 words) only with a new code-generation hypothesis.
   Existing completed matrices do not match; preserve their pinned alias,
   loop-delay, volatile-width, and ordering behavior.
3. Treat original SDK/boot/privileged/context assembly as retained provenance,
   not ordinary C conversion backlog. Recover cleanup/debug/glyph connected
   entry interfaces before trying independent leaf replacements.
4. Before any production owner transition, rerun semantic/guard tests and
   independently compare both whole Init sections, then update aggregate
   totals only for actual linked C conversion.

The full remaining inventory and group-by-group decision remain in
[Note 792](792-init-resume-remaining-assembly-conversion-decision-20261003.md).
