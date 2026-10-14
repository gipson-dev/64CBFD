# Alternative Source Byte-Match Audit

Verified locally: 2026-10-14, after banking `func_151A77C0` in consumer
`41dfe733`; see [Note 1358](1358-game-actor-threshold-flags-guarded-match-20261014.md).
The user's source remains reference-only. No C body, header, configuration,
assembly, build artifact or matching guard is adopted into the active decomp.

## Supplied Source And Reconstruction

Requested directory:

`Another Source/CBFD-Recompiled/conker`

This is the outer decomp root; the code project is its nested `conker/`.
It is an archive, not a Git checkout. All801 archived files are hashed before
and after; every hash and the file count remain unchanged. There is no supplied
ELF, map, progress CSV, extracted assembly, linker script or pristine binary.
The n64splat/asm-processor submodule directories are empty. The README's
2026-09-07 figures are conversion counts, not byte-match measurements. The
retained build log ends in a failed US binary checksum, not a passing verifier.

Use only a disposable copy under the active project's ignored output:

`conker/build/alternative-source-byte-audit-20261014/`

Copy the archive, retain its compiler and Makefile, and supplement the missing
extraction/build tools from the installed workspace copies. Use the verified
decompressed US image, SHA1 `842e3d348e3c8ae0039e2ab367ad492f9b5266d8`.
The supplied `cc` matches the installed compiler SHA256
`ca4b4385eb89c5098b665ffe256f59aa1bfd73ccd8f104fcb3eee0314dcd236a`
(hexadecimal case is immaterial).

Extraction uses splat0.41.0/spimdisasm1.42.2 and recreates original assembly,
data and linker inputs. All archived C sources, C headers and other inputs
stay byte-identical in the snapshot except the extractor-generated
`include/macro.inc`. Declare that generated assembly support delta rather than
silently accepting it. A copied rzip helper is restored to the archived file;
all800 other archived snapshot inputs agree. No C fix script is run, and no
retail-word guard or matching padder is added.

All linked C objects compile. Ordinary linking fails on **1,110 explicitly
reported unresolved references**, all in generated standalone `.rodata`
objects. These include missing original jump-table local labels. No failed
reference is in executable code. Re-link with **`--noinhibit-exec` only for
diagnostic inspection**, retaining those errors instead of assigning invented
addresses. `DIAGNOSTIC-NOT-RUNNABLE.txt` marks the artifact. A zero exit code
from this diagnostic link is not successful ordinary-build verification.

Diagnostic ELF SHA256:
`2eecd116fb3eaa9ee54b8e07a8cb4ebe097d17d33765872962bb640ef07c95cc`.

## Function-Only Measurement

Measure actual linked executable C entries, excluding `.NON_MATCHING` metadata
and `D_` data labels. Anchor names and retail spans to the banked main project's
US catalogue; require matching section, unique address and a real linked body.
There are no unanchored C rows. Compare every emitted word against the original
slot without rebasing or modifying the candidate. Keep address-only differences
separate from real instruction differences.

Every selected function matches the **complete slot**, at its original linked
address. No trailing-padding exception is needed, and no relocation-aware
guard is applied to the candidate.

| Section | Candidate C Slots | Byte-Exact | Address-Only | Different | Exact C Bytes |
| --- | ---: | ---: | ---: | ---: | ---: |
| Init | 241 | 241 (100.00%) | 0 | 0 | 34,580 |
| Game | 1,217 | 1,217 (100.00%) | 0 | 0 | 123,512 |
| Debugger | 20 | 20 (100.00%) | 0 | 0 | 2,264 |
| Total | 1,478 | 1,478 (100.00%) | 0 | 0 | 160,356 |

This is **100% of its linked executable C subset**, not100% C decompilation.
The banked comparison catalogue has5,903 executable-style entries; this
candidate supplies C for25.04% of them. Most remaining code is original
assembly. The160,356 matching C bytes are7.11% of the2,256,728 compared text
section bytes; the latter include Debugger data and original assembly.

For comparison, the active project's executable C subset, measured with the
same data-label exclusions, currently has these linked guarded results:

| Section | Active Byte-Exact / Converted C | Address-Only | Different |
| --- | ---: | ---: | ---: |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 2,836 / 4,823 (58.80%) | 0 | 1,987 |
| Debugger | 41 / 41 (100.00%) | 0 | 0 |
| Total | 3,369 / 5,356 (62.90%) | 0 | 1,987 |

The active result includes its installed expected-word guards. The alternative
does not use those guards. Different converted denominators mean percentages
alone do not establish that one entire source is a better replacement.

## Whole Text And Counter Caveats

The reconstructed candidate's entire text sections also agree byte-for-byte:

| Section | Compared Bytes | Different Bytes | Includes Unconverted Assembly |
| --- | ---: | ---: | --- |
| `.init` | 164,048 | 0 | Yes |
| `.game` | 2,072,880 | 0 | Yes |
| `.debugger` | 19,800 | 0 | Yes, plus embedded data |
| Total | 2,256,728 | 0 | Yes |

Text SHA256 receipts are in `comparison.json`. This does not verify the failed
standalone rodata link, a complete ROM image, gameplay or a host port.

Do not use the unfiltered legacy result, **1,508/2,609 (57.80%)**. Its C rows
include **991 `.NON_MATCHING` bookkeeping symbols** and **140 data labels**.
Across both languages its map contains4,581 bookkeeping rows. Their zero/
overlapping spans corrupt the legacy denominator and retail-length inference.
Excluding only the suffix is insufficient; use authentic retail boundaries
and distinguish data from executable functions.

The main README's existing Debugger181/181 similarly includes140 `D_` data
labels; its executable C subset is41/41. Consequently its legacy total3,509/
5,496 includes those140 entries, while the function-only total is3,369/5,356.
The historical/main progress pipeline and README counters are not silently
redefined during this source audit. Track a separate counter-correction task.

The supplied `src/game/game_1D43B0.c` is an **unlinked draft**. Its source
`func_151A77C0` has wrong-width/unaligned accesses, but the link map actually
uses `build/asm/1D43B0.s.o` for that routine. Do not count the draft as a C
match or transplant it over the newly banked implementation. Source files
being present is not evidence that the Makefile links them.

## Potential Individual Donors

There are **22 exact candidate C functions** where the active source is still
non-matching or not converted. All are Game functions. Nineteen are currently
converted but different; three still use assembly. This is a review queue,
not permission to import them, and not semantic/runtime acceptance.

| Function | Candidate Owner | Words | Active Converted |
| --- | --- | ---: | --- |
| `func_15008870` | `game_35D20.c` | 48 | Yes |
| `func_1501AF44` | `game_476D0.c` | 87 | Yes |
| `func_15042D94` | `game_70200.c` | 42 | Yes |
| `func_1505D1C4` | `game_83300.c` | 61 | Yes |
| `func_1506D74C` | `game_981E0.c` | 83 | Yes |
| `func_15074980` | `game_981E0.c` | 49 | Yes |
| `func_15079228` | `game_A28B0.c` | 46 | Yes |
| `func_1507D158` | `game_A9D90.c` | 32 | No |
| `func_1509B764` | `game_C8950.c` | 43 | Yes |
| `func_150C2FCC` | `game_EF410.c` | 48 | Yes |
| `func_15125628` | `game_14FF90.c` | 26 | No |
| `func_151411E4` | `game_16DC80.c` | 27 | No |
| `func_15168F84` | `game_1944C0.c` | 47 | Yes |
| `func_151F2E88` | `libultra/audio/game_21FC90.c` | 727 | Yes |
| `func_151F39E4` | `libultra/audio/game_21FC90.c` | 142 | Yes |
| `func_151F3DE0` | `game_221290.c` | 322 | Yes |
| `func_151F42E8` | `game_221290.c` | 788 | Yes |
| `func_151F578C` | `game_221290.c` | 782 | Yes |
| `func_151F6970` | `game_221290.c` | 110 | Yes |
| `func_151F6B28` | `game_221290.c` | 298 | Yes |
| `func_151F8088` | `game_221290.c` | 335 | Yes |
| `func_151F85C4` | `game_221290.c` | 59 | Yes |

The smaller26/27/32-word unconverted routines are useful initial review targets
if the user authorizes using this source. Review actual ABI, dependencies and
whole-owner effects; independently compile/qualify each before changing active
code. Larger audio functions require their verified `-g` owner profile and
existing local type/header compatibility. No broad header merge is justified.

## Validation And Banking

The read-only audit utility and tests are banked first in tools
`86b3df6858a58a4db83ad831cb291d6c2d12e58a`. Four checks pass4.314s: metadata
filters, full-slot versus omitted-padding distinction, real versus address-only
differences and a fresh complete audit with an effective one-word mutation.
That control reduces exact candidate functions to1,477 and produces one real
diff without changing the main comparison. Both tools copies pass smoke and
Windows byte-compilation.

Copy only the two new audit modules to the independently dirty older mirror.
Preserve all468 previous hashes and its `ddbdd16` HEAD; it now has470 dirty
paths. Main owner, guard, ELF and conversion hashes remain exactly as banked
in Note1358. No push, host source change, host build/launch or frozen Release
work. The wider Game backlog is not complete; this requested audit adopts nothing.

After receiving these measurements, the user authorizes using verified
byte-exact C with proper names/comments. Bank this read-only audit before
transferring functions in separately qualified groups. Preserve retail export
symbols and use descriptive names/comments for proven recovered roles.

Receipts retained outside the supplied archive:

- `source-before.json` and `source-after.json`:801 hashes/file-count preservation.
- `snapshot-input-delta.json`:one declared extractor-generated macro delta.
- `build-us.log`:ordinary link failure and1110 explicit rodata references.
- `comparison.json`:per-function words, addresses, strict matches, donors,
  section hashes and the diagnostic ELF identity.
- `DIAGNOSTIC-NOT-RUNNABLE.txt`:acceptance boundary.

```sh
python3 -m tools.experiments.alternative_source_byte_match_audit \
  conker conker/build/alternative-source-byte-audit-20261014/snapshot/conker \
  conker/build/alternative-source-byte-audit-20261014/comparison.json
python3 -m unittest tools.tests.test_alternative_source_byte_match_audit -v
```
