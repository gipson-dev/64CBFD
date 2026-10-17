# Mirrored Texture Upstream Home Provenance

Date: 2026-10-17

Continue [Note 1477](1477-mirrored-texture-candidate-and-private-gap-20261017.md)
from clean consumer **502774f0**, tools **5deb8e2**. Same target:
**func_1517FB9C**, VA 0x1517FB9C..0x15180580, ROM 0x1AD04C..0x1ADA30,
**633 retail words / frame 0xD8**. This is compiler-origin progress, not
a C installation, instruction certificate or additional matching credit.

## Qualified Compiler Capture

The new target-specific helper reuses the existing CFE/UOPT stream decoder,
owned-child frame observer, producer/consumer lifecycle checks and read-only
UGEN load-node probe. It does not run the older text-measurer target unchanged.
All four prepared cc/cfe/uopt/ugen hashes are checked before and after.
No compiler binary, dependency, provider or configuration is changed.

Compile the complete original owner plus the complete SDK candidate first.
Remove other C definitions and the one neighboring GLOBAL_ASM only in an
isolated diagnostic source. Require identical target words and all four
bindings before tracing. The isolated function has no pools; the complete
owner retains its existing 16-byte projection pool, which belongs to its
neighbors. Do not require a removed neighbor's unused pool in the isolate.

Normal preprocessing, includes and O2/g3/MIPS2/o32 flags are retained.
Capture the actual CFE input to UOPT and actual UOPT output consumed by UGEN,
with observed producer completion before each input is read. All five owned
stages, including as1 and the driver, exit zero. The initialized descriptor/
type table gate and load-node probe fire; the probe is explicitly removed
after UGEN exit and before driver exit. Hash the source, processed source,
script, log, both objects, both streams and captured tables.

Normal/traced text, function metadata, relocations and pools are identical.
The literal ELF object files are not identical: **only .mdebug differs** in
the checked record case. No .mdebug identity or retail identity is claimed.
Existing output directories are refused; a timeout is not a compiler restart.

## Measured Origin

The record candidate's **2,259 CFE / 1,764 UOPT records and 301 UGEN node
events** show that its first private FP home already exists in UOPT output.
It is not an unexplained choice introduced only by late UGEN spilling:

1. UOPT computes centerY from viewport +0x10 and projected +4 into float
   register 44. It loads offsetY from incoming parameter +0x10 into register 50.
2. Records 90..95 add those values and store positiveY into **M-120**.
3. The observed frame is 216, so this home becomes **SP+0x60**. The actual
   emitted SWC1 is at **entry+0xAC**, the private gap measured in Note 1477.
4. UOPT also emits three distinct rate-related homes: **L M-144**, its
   promoted **J M-148** copy and negated **J M-152**, becoming **+0x48,
   +0x44 and +0x40**. The type conversion and negation are present in the stream.

UOPT declares 212 bytes of M storage; the observed final frame is 216 bytes,
locals=216, temporary=0, empty temporary pool. The two frame observations
are initial zero and final 216. This is positive evidence of the upstream
homes and final allocation, not a universal claim about every UGEN spill path.

Retail instead stores positiveX at **SP+0x54**, keeps offsetY/positiveY in
**F16/F18**, and uses **+0x34/+0x30** for positive/negative rate words.
Its positive rate also survives in T4. The original CFE/UOPT stream is not
available; do not claim that its internal variables or allocation decisions
have been recovered from these candidate traces.

## Bounded Comparisons

| Complete Source | Words | Frame | Ordinal Differences | UGEN Nodes |
| --- | ---: | ---: | ---: | ---: |
| Existing record/u16 candidate | 626 | 216 | 604 | 301 |
| Positive-Y assignment first | 622 | 216 | 599 | 301 |
| s32 rate assigned through (u16)(u32) | 620 | 208 | 608 | 295 |
| register u16 rate | 626 | 216 | 604 | 301 |

The Y-first form changes source homes/order and removes the early UOPT
floating-memory store before record 200, but also homes incoming offsetX
and changes live float roles. It is not a word-count-neutral repair.

Promoting the narrowed rate removes the separate L-memory copy: positive
and negative words become M-128/M-148. However, it also spills the first
integer bound, keeps the positiveY float home at M-120 (now **SP+0x58**),
and loses the retail frame/length. The register hint adds one CFE record
but emits literally the same 626 target words and bindings as the original
candidate. None of these diagnostics is installed or newly qualified as C.

Preliminary rejected observations remain in ignored build directories.
In particular, a requested f_gen_store breakpoint was unresolved because
that helper has no native symbol in this prepared compiler; its lack of
events is not absence evidence. An earlier node cleanup check also failed.
The final receipts use fired load-node gates and complete cleanup. The first
unittest attempt collided with unittest's run method; that test-only naming
error was corrected before the passing run below. No failed receipt is used
to establish a match, and no still-running compiler was restarted.

## Verification And Bank

All **five final tests pass in 28.916s**, with four freshly completed owned
compiler traces, pinned raw words/bindings, source-to-home checks, seven
effective log controls, eight artifact corruptions and no-restart/path gates.
All 156 protected input entries remain at baseline. The complete source,
Makefile, guards, normal ELF, conversion CSV and root README are untouched.
No normal rebuild is needed or claimed for these tools-only observations.

Fresh official matching remains Game **2,947/4,828 (61.04%)**, total
**3,620/5,501 (65.81%)**, different **1,881**, zero drift. Init **492/492**
and Debugger **181/181** are exact. Existing duplicate recipe warnings remain.
The seven-test public/native/caller/rebase qualification in Note 1477 is
prior unchanged evidence, not newly rerun in this compiler-only checkpoint.

Tools **b44bad7** banks two new files first. Both local copies have two exact
task pairs / four ASCII/AST checks. The mirror's trace validator replays all
four consumer captures using the consumer's qualified dependencies; this is
not a separate full mirrored compiler suite. Eleven shared padder checks pass
per copy: active **0.038s + 0.024s**, mirror **0.043s + 0.030s**. Consumer
tools-check passes. Preserve mirror HEAD **ddbdd16b** and all **1,029 initial
dirty-file hashes**, now **1,031 paths**. No mirror commit/reset or push.
No host build/launch or frozen Release action. No Claude call this checkpoint.

Prepared-checkout reproduction, sequentially (choose a new run name):

```sh
python3 -m tools.experiments.game_mirrored_texture_compiler_trace --run fresh
python3 -m unittest tools.tests.test_game_mirrored_texture_compiler_trace -v
make -C conker match-progress NON_MATCHING=1
make tools-check
```

- [x] Qualify actual producer/consumer streams, fired UGEN nodes and code identity.
- [x] Locate the positiveY and three rate homes in upstream UOPT records.
- [x] Reject source-order, promoted-rate and register-hint diagnostics as matches.
- [ ] Recover coordinate lifetimes and shared promoted-rate residency consistent
  with retail's positiveX home, F16/F18 and T4, without arbitrary storage effects.
- [ ] Close all 633 words, private/fault state and complete installation gates.

**Next: stay on func_1517FB9C.** Use the captured upstream expressions and
register/home lifetimes to derive the next source change. Preserve the full
SDK Y-sign predicate and unsigned conversion paths. Do not repeat the same
shape/type screens, reinterpret the length deficit as seven scheduling words,
or install guards on public agreement alone. Wider Game/additional-source
matching and the deferred pulse lifetime remain open.

Follow-through: [Note 1479](1479-mirrored-texture-float-color-saturation-20261017.md)
records actual float-color constraints and partial positiveX residency, still
not a match. [Note 1480](1480-overlay-mode-defaults-direct-match-20261017.md)
independently installs the neighboring 50-word reset and adds exact-successor
fixture adaptation. The mirrored emitter remains uninstalled and without credit.
