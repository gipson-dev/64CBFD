# Paired Overlay Stack Contract And Random Direction Match

Date: 2026-10-15. Continue the additional-source / Game matching objective
from consumer **2b68b9d7** and tools **76e1e02**, both initially clean.
The separate older tools mirror starts at ddbdd16 with 705 dirty paths.
Preserve the archive, unrelated work and frozen host Release; no push,
host build/launch, dependency installation or Claude call.

## Steps

1. [x] Trace func_1516FE1C's real caller and callback table beyond the previous assembly-only text search.
2. [x] Qualify both complete packets, conditional inherited input, live homes, caller entry and effective contract controls.
3. [x] Defer FE1C C adoption rather than introduce an undefined local read, zero the ambient word or change its ABI.
4. [x] Recover func_15170034 as complete initialized C and resolve all 41 raw/padded words without guards or profile changes.
5. [x] Qualify private/fault/native behavior, output aliases, independent rebases, actual trig helpers, owner neighbors and archive fingerprints.
6. [x] Install the direction writer, rebuild normally, verify every predicted ELF/input byte, refresh aggregates and bank tools first.
7. [ ] Recover func_151700D8 and continue all additional-source repair/binding/unanchored, callback/caller and inherited-stack queues.

## FE1C Contract

**func_1516FE1C**, VA **0x1516FE1C**, ROM **0x19D2CC**, is **134 words /
536 bytes**, frame **0x100**, RA at SP+0xF4. Its production C remains the
unchanged placeholder. The archive's uninitialized `f32 spFC` is not usable
C or evidence that the branch can be removed.

The prepared 2,467,288-byte code image contains one aligned direct JAL to
FE1C at ROM **0xA22EC**. It is inside **func_15074E04**, VA 0x15074E04,
ROM 0xA22B4, **31 words**, already entirely byte-exact in the current ELF.
This caller was already C, so the prior original-assembly text search did
not find it. The caller is slot **7** of the real **39-entry D_80086694**
table, at ROM **0x22B154**; the current table is also retail-exact.

E04 passes `(actor - D_800CC2D0) / 0x32C, 180, 255, 0`. It has no local
actor-state gate. The target reads actor **word** 0, not a byte. Its
non-word-1 path loads **incoming SP-4**, which is **E04 entry SP-0x2C**.
Neither target nor caller initializes that location before the read.
This is not the fifth argument at incoming+0x10.

Static upstream table dispatches occur at **0x1505BD94** in
func_1505B9C4 and **0x1505C6F4** in func_1505C1E4. Their local windows
select the table by an event byte and pass the actor in A1. Full upstream
entry-path/state restrictions and natural gameplay remain unproven; these
windows do not justify omitting FE1C's non-word-1 branch.

Each branch submits two **49-word func_1516D99C** packets. Start with zero
in every field, then apply:

| Fields | First Packet | Second Packet |
| --- | --- | --- |
| 0, 1 | actor word 1: 4, 0; otherwise signed high/low halves of the byte address actor+0x14 | Same snapshot |
| 13 | 0 | 8 |
| 27, 28, 29, 30 | 170 each | Same |
| 31 | incoming scalar low 16 bits | Same snapshot |
| 32, 35, 36, 37 | 30, 30, 360, 24 | Same |
| 34 | actor word 1: index low byte; otherwise 255 | Same snapshot |
| 38, 39, 41 | actor word 1: 1, 4, 1; otherwise 33, 4, 1 | Same snapshot |
| 45 | actor word 1: 25; otherwise inherited full word | 27 |
| 47, 48 | Reload low flag byte / full context from incoming homes | Reload again |

Do not copy the archive's scaled `s32 * + 0x14` coordinate address or narrow
physical field 45 to a byte. The complete call packet forwards all 32
inherited bits even if the downstream factory ultimately consumes a byte.

Six contract checks pass: **1,440 original-code cases**, both stack phases,
all 134 words visited, all 49 fields per call, live flag/context versus
snapshot scalar/class, **27 connected caller cases**, **118 fired original
memory cuts** and **six effective instruction controls**. Removing the
ambient word succeeds on word-1 actors and faults before the first factory
call on other actors. Varying the fifth argument does not replace the input.
The connected target is explicitly **staged original assembly**, not installed
C. Factory returns/home writes are declared opaque guest providers, not
portable C behavior, complete upstream reachability or hardware acceptance.

As with the [earlier renderer deferral](1395-packed-fade-scale-callback-and-renderer-deferral-20261015.md),
do not adopt an undefined C local merely to gain matching credit. Further
stack provenance or an explicitly assembly-classified restoration is separate
work. No FE1C matching credit is added here.

## Direction Writer Recovery

**func_15170034**, VA **0x15170034**, ROM **0x19D4E4**, is **41 words /
164 bytes**, frame **0x30**, RA at SP+0x14. Restore its void/four-input ABI
in [generated_19A8B0.c](../../conker/src/game/generated_19A8B0.c), retaining
the address-based name and a short behavioral comment.

The first random draw is masked by 0x3F when flag 0x40 is set, otherwise
0x7F. The second draw is independently masked by 0xFF. The actual table
identifies **func_150489B0 as cosine**, and **func_15048A40 as sine**:
Y = cos(polar), X = sin(polar)*sin(azimuth), Z = sin(polar)*cos(azimuth).
Do not swap these names based on the archive's misleading temporaries.
Write Y first, X second, Z last, preserving aliased output behavior.

Unlike FE1C, both byte-angle reads are dominated by an initialized word
store. Separate the sampled word from its addressable angle copy, keep the
logical local declaration order, and name the final azimuth sine before
multiplication. This recovers the exact homes, frame, six calls and MUL.S
operand order. The final source has **41/41 raw and padded words**, no
target guards, artificial volatility, uninitialized locals, profile changes
or shared-header edits. All **29 owner neighbors**, relative relocations
and normalized pools remain unchanged.

## Qualification And Image

All **18 installed checks pass in 53.253 seconds**, exit 0: six FE1C
contract checks, nine direction checks and three whole-image/control checks.

- **24,576 paired guest cases**: every flag byte, high input bits, independent random words, four output-alias patterns, two stack phases and three provider modes. All 41 words execute and complete available private state agrees. Guest home mutations are explicitly not native C claims.
- **252 fired memory-fault prefix pairs**, with literal private state equal; no portable C or hardware fault claim.
- **Native32 O2/O0: 16,384 cases each**, selected source with undefined-behavior traps, exact call sequence and output aliases. All six compiled guest/native negatives fail through controlled semantic exits, not crashes.
- **Three independent original/C links** preserve all 41 words and all six relocated calls.
- **1,536 connected pairs** execute the current retail-exact trig helpers, including the sine wrapper's return delay, and the actual 65-word table. RNG remains opaque; no host/gameplay acceptance claim.
- All **801 original archive fingerprints** freshly agree. The whole-source compiler audit remains historical, not a fresh 1,717-object audit or a newly discovered raw donor.
- Before installation, all **57 live predecessor inputs** are unchanged. After the normal build, the entire **3,257,636-byte ELF** equals the pre-install prediction: **128 changed bytes**, only the target slot and symbol size **12 -> 164**, with no metadata exclusions. Every other ELF byte and **55 of 57 inputs** stay fixed; guard CSV, headers, profiles and conversion rows are unchanged. All **189,088 protected data bytes / 720 owners** agree.
- Reject all **57 live-input flips**, eight physical ELF flips, all 57 frozen-before flips, a changed manifest, unknown predecessors and both before/after captures for the two successor paths.

Initial harness corrections make the wrong-product control nonvacuous by
using azimuth 0x81 instead of the mock's zero at 0x80; include the sine
wrapper's physical return delay beyond its 44-byte symbol extent. Negative
mutants alone permit their intentional unused-variable/parameter warnings.
Selected source still compiles without diagnostics. An imported TestCase
initially triggered ten older fade checks; all passed in the 25-check
88.149-second pre-install run. Import the module instead to keep subsequent
runs focused. No production workaround was made for these fixture issues.

| Measurement | Before | After |
| --- | ---: | ---: |
| Game byte-exact | 2,905 / 4,828 (60.17%) | **2,906 / 4,828 (60.19%)** |
| Total byte-exact | 3,578 / 5,501 (65.04%) | **3,579 / 5,501 (65.06%)** |
| Still different | 1,923 | **1,922** |
| Address drift only | 0 | **0** |

Init stays 492/492 and Debugger 181/181 exact. Conversion counts/bytes
remain unchanged because the old C placeholder was already counted.

```text
ELF   f4f81f08c61c5592053d8faecc3a5699eb907b5d748c04a0af38e1b4cc2fafc2
owner 157edad8ef697e76e55171685be5b34562d9e349de38095d8a718b5201a0a2d8
```

## Banking And Next Target

Tools **9bc6852** is committed first. Preserve all **705 initial older-mirror
fingerprints**, HEAD ddbdd16, and five absent-only hash-equal owned copies:
**710 final dirty paths**. Windows syntax checks pass in both copies; all
11 shared padder checks pass under WSL in both copies, with no skips, and
`make tools-check` passes. Windows-only binutils skips are not counted as
MIPS passes. Root README changes aggregate rows only. No push or host action.

Reproduce from the prepared consumer WSL checkout:

```sh
python3 -m tools.experiments.game_random_unit_vector
python3 -m unittest tools.tests.test_game_actor_paired_overlay_contract tools.tests.test_game_random_unit_vector tools.tests.test_game_random_unit_vector_installed -v
make tools-check
make -C conker -j4 build/conker.us.elf progress.csv
make -C conker match-progress NON_MATCHING=1
```

Next ordinary target: **func_151700D8**, VA **0x151700D8**, ROM
**0x19D588**, **266 words / 1,064 bytes**, frame **0x190**, RA at SP+0xDC.
Audit its complete ten-input mixed word/float ABI, three copied tables at
D_8008CBF4/CC00/CC0C, loop bounds, byte/halfword widths and factory packets
before translating the archival draft's typed-pointer/table accesses.
This function remains unchanged. Keep FE1C's inherited-stack recovery,
the prior renderer deferral and all broader queues open; one additional
match does not complete the persistent objective.
