# Owner Burst UOPT Reservations And Source Controls

Verified 2026-10-17. Consumer predecessor `805f8c62`; tools predecessor
`c2c5a97`. Both active trees began clean. The previous goal turn made concrete
progress on public packets; this turn continues the same frame mismatch in
`func_150F2D14`. **No candidate is installed and no matching credit is earned.**

Target: `generated_11FF10`, VA `150F2D14..150F3194`, ROM
`1201C4..120644`, 288 retail words / 1,152 bytes, frame `0x150`.
The aligned candidate from [Note1509](1509-owner-burst-frame-trace-and-aligned-packet-qualification-20261017.md)
still has 288 words, frame `0x160`, 85 differing words and the previously
measured 16-byte private SP gap. Its public packet qualification is unchanged.

## Twelve Reserved Bytes Accounted For

`tools/experiments/game_owner_burst_uopt_local_trace.py` extends the qualified
frame tracer through a scoped in-process adapter, not edits to earlier tools.
It watches compiler-emulated memory cursor `0x1001C4B4` in a newly owned UOPT
child. These are **compiler data/host PCs**, not Conker guest addresses.

An initial `f_gettemp` entry probe did not fire even though the complete compiler
run and ordinary frame probes succeeded. No allocation-absence claim followed.
The cursor watch then found the actual writer: **`f_spilltemps`, host PC
`0x450CF3`**, immediately after its cursor store. The final helper watches from
UOPT's first input read, records the writer and operand trees, captures the
complete descriptor chain on return, and removes all three owned probes before
the next compiler child. It does not attach to an existing debugger.

Both fresh qualified traces account for exactly three four-byte reservations:

| Source Form | Declared CFE Area | Reservation Ends | Output UOPT Area | Final Frame |
| --- | ---: | --- | ---: | ---: |
| Previous selected body | 188 | 192, 196, 200 | 200 | `0x158` |
| Aligned packet body | 196 | 200, 204, 208 | 208 | `0x160` |

Saved/outgoing budgets remain 96/48 bytes. The three descriptors have distinct
identities, indices 0/1/2, size four, negative caller-relative offsets, and an
exact checked next/head/tail chain. For the aligned form their offsets are
`-200`, `-204`, `-208`.

The reserved expression images are bound by live pointer identities and raw
operands to:

1. The incoming actor parameter plus constant `0x28`.
2. The one-byte owner-state load at `owner + 0x222`.
3. The integer conversion of that same state-load image.

The owner operand points to the exact frontend source home from
`owner = data->owner;`: `-184` in the selected form, `-192` in the aligned
form. Parameter/procedure and local-storage identities are checked separately;
no identical pointer values from unrelated compiler scopes are assumed equal.
The conversion's child also carries the descriptor assigned to the second
reservation, providing a second temporal identity check.

The [upstream IChain/Temploc declarations](https://github.com/n64decomp/ido/blob/master/src/uopt/uoptdata.h)
are a layout reference, not proof that an IDO 7.1 decompilation describes this
5.3 binary. The authority here is the prepared 5.3 fingerprints, observed
native writer, runtime opcode table, raw operands and matching frontend input.
No upstream compiler implementation is imported or substituted.

Neither output UCODE stream has an explicit `M` operand below its declared CFE
local area. Thus these are **reserved slots without explicit output M accesses**
in the observed streams. Do not turn the function name `spilltemps`, a zero
UGEN temporary pool, or absent output operands into a claim of actual spilling,
full machine-level nonuse, or original source types. The whole frame/private
mismatch remains real.

## Focused Source Screens

The new helper also reproduces five complete source forms under the unchanged
owner/compiler profile. No instructions, profiles or guards are patched.

| Form | Words | Frame | Overlapping Differences | Extent Gap |
| --- | ---: | ---: | ---: | ---: |
| Unchanged aligned baseline | 288 | `0x160` | 85 | 0 |
| Three scalar vector-field copies | 287 | `0x160` | 225 | -1 |
| Direct actor-data base instead of a local pointer | 289 | `0x158` | 254 | +1 |
| Direct base plus post-transform input-union reuse | 290 | `0x158` | 254 | +2 |
| Literal `58.14f` scale | 288 raw | `0x160` raw | Not linked | Unqualified pool |

The vector-copy control leaves the frame unchanged while worsening instruction
matching. The measured reservations belong to state/base expressions, not the
vector-copy expression; the control does not establish a usable frame fix.
Removing the redundant data-pointer declaration reduces the frame by eight
bytes but creates an executable overflow; the real padder rejects both +1/+2
forms. A smaller frame alone is not a usable restoration.

The literal form emits a new `.rodata` binding. Its first four pool bytes
`42688F5C` equal retail `D_800A196C` at ROM `0x24642C`; the remaining twelve
bytes are zero object alignment. The ordinary linker **rejects the unknown
binding**. Equal float bytes do not establish correct pool ownership,
relocation addends or a complete owner layout. No synthetic address is assigned
to get a favorable word comparison, and no linked matching claim is made.

These screens are measured/rejected proposals, not newly qualified semantic
implementations. The prior selected/aligned source bodies, earlier fixtures
and their documented native/rebase/private boundaries are preserved verbatim.

## Validation And Preserved State

Four final tests pass in **51.504s**, including **78 effective fail-closed
controls** over reservation sizes/offsets/identities, native writer, expression
trees, source home, explicit output operands and completed-child cleanup.
Two newly owned traces preserve complete normal isolated object code,
functions, relative relocations and pools, and reproduce their full-owner
target words/bindings exactly. Both compiler drivers and every child exit zero.

The earlier test run's malformed negative-control record caused a fixture
`KeyError`, not a production failure. The corrected control mutates a complete
valid record, and the final full four-test run above passes. That earlier failed
run is not counted as passing evidence.

All **266 protected entries / 244 paths** remain byte-identical, including
production source, guard/profile/conversion manifests and earlier checkpoint
fixtures. The complete installed ELF remains
`5efb8a9f598af0712d97eaf4d0f2ab2df134e349ad16eddfeb0f75e74128b7d4`:
all 6,057 bodies/addresses and 189,088 Game-data bytes / 720 owners are unchanged.
No new normal production build is claimed or needed for this uninstalled work.

Fresh match-progress remains Game **2,964 / 4,828 (61.39%)**, total
**3,637 / 5,501 (66.12%)**, 1,864 different and zero drift. Init 492/492 and
Debugger 181/181 remain exact among converted functions. Root README is
unchanged. Note1509's public/native qualification is reused unchanged prior
evidence, not freshly rerun or extended to these rejected source controls.

Tools **a825058** is banked before the consumer docs/pin. Both local tools
copies freshly pass 12 shared tests and smoke checks. Four ASCII/AST parses
and two byte-identical task pairs pass. Both mirror destinations were absent
before copying; all 1,137 prior hashes and HEAD `ddbdd16b` are preserved,
with 1,139 dirty paths afterward. No mirror commit/reset, push, Claude call,
host-port change, frozen Release action or dependency installation.

## Resume The Same Function

- [x] Identify all 12 optimizer-reserved bytes and bind their actual expressions.
- [x] Verify normal-object identity, completed lifecycle and effective rejection controls.
- [x] Reject misleading vector-copy/frame-only improvements; preserve every installed byte.
- [ ] Continue `f_spilltemps`' reservation eligibility/register dataflow for
  these three images, especially the owner-state load/conversion pair; account
  for reserved homes while retaining the retail caller-relative packet layout.
  Recover frame `0x150` without broad instruction guards or fabricated formals.
- [ ] Qualify the literal pool's ownership/addends before using it as a source
  alternative. It is not a linked candidate yet.
- [ ] Then recover V0/V1 and saved-FPR roles/setup scheduling and require all
  words, full private/fault prefixes, rebases, callers and the complete first
  linked image before installation. Keep the 139-word gate, fade gaps and wider
  Game goal open.

```sh
python3 -m tools.experiments.game_owner_burst_uopt_local_trace --form aligned-pairs
python3 -m tools.experiments.game_owner_burst_uopt_local_trace --screens
python3 -m unittest tools.tests.test_game_owner_burst_uopt_local_trace -v
make -C conker match-progress NON_MATCHING=1
make tools-check
```
