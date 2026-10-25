# Global Identity Event Match - 2026-10-25

## Result

Recover `func_1519E818` in `conker/src/game/generated_1CA420.c` from its
zero-return placeholder. Complete semantic C plus eighteen checked operand
guards matches all 45 retail words. This is guarded C, not a compiler-only
match. Existing payload views and typed interfaces suffice; no shared-header
or caller-source changes are needed.

The production object and ELF are adopted in the Windows checkout. The fresh
recount uses the actual Native ELF, streamed to the verified Linux cache:

| Section | Exact C functions | Matching |
| --- | --- | --- |
| Total | 3,794 / 5,505 | 68.92% |
| Init | 492 / 492 | 100.00% |
| Game | 3,121 / 4,832 | 64.59% |
| Debugger | 181 / 181 | 100.00% |

Address drift is zero; 1,711 C functions still differ. Only `func_1519E818`
receives new credit. The unchanged denominator's 75% threshold is 4,129,
requiring 335 more matches. The wider goal remains open.

## Original And Interface

- Original: `conker/asm/1CA420.s`, VA `1519E818..1519E8CC`,
  VROM `1CBCC8..1CBD7C`.
- Body and slot: 45 words / 180 bytes, frame `0x18`, no alignment tail.
- Bindings: `+0x44 R_MIPS_26` to `func_1516972C`, and
  `+0x4C HI16` / `+0x50 LO16` to `D_800E0920`.
- Canonical callback: `void(struct260 *, s32, u8)`. Preserve the existing
  `func_1516972C(struct102 *)` and `extern u8 *D_800E0920` declarations.
- Reuse `PayloadOwnerLink` and `PayloadOwnerLinkEvent`; expose only the
  needed owner word at `+0x28`, identity byte at `+0x2C`, event words and keys.

Command zero releases this record when its saved word equals the first event
word OR its saved key equals event byte 4. A word match skips both key reads.
Call the release helper first, then unconditionally clear `D_800E0920`, even
when the helper changes that global or it does not point to this record.
Do not substitute event key byte 8 for the original comparison against byte 4.

Command `0x2D` exchanges the saved word against the two event words. The first
match wins. Store the replacement word before reading event byte 9 or 8;
overlap can change those late reads. Other command bytes perform no owner,
event or global data accesses in the emitted guest code. Preserve full incoming
command homes, all unrelated bytes and the original dead duplicate load.

## Actual Caller And Registry

The complete original and retained `func_15149434` are 23 words / 92 bytes,
VROM `1768E4..176940`, in `conker/src/game/done/game_1765E0.c`. Both the
caller source and its complete owner object are unchanged. It clamps an
invalid signed selector to slot zero, checks for NULL, and invokes the typed
callback with the byte command.

The immutable `D_8008A8D8` table has 74 entries, beginning at VROM `22F398`.
This target is entry 4, whose literal lies at VROM `22F3A8` / VA `8008A8E8`.
The whole-ROM encoded-call/literal scan finds no direct JAL and that one
literal; this is not proof against arbitrary computed calls. Other callbacks
remain bounded argument/mutation contracts, not newly recovered providers.

Execute the actual original/retained 28-word release helper as well. Its deeper
bookkeeping, callback and fallback providers remain explicitly bounded.
Neither the dispatcher nor the already-exact release helper receives new credit.

## Checked Compiler Boundary

The complete isolated and owner C body already has the original length, frame,
memory/branch schedule and all three bindings. Derive eighteen operand-only
rows at word indices `9,10,11,13,14,15,26,27,29,30,31,32,34,35,36,38,39,40`.
Release-phase register roles map `3->15, 4->24, 15->25, 24->8`; retarget-phase
roles map `3<->4, 9->11, 25->9, 8->10, 10->12`. Commute equality operands at
words 28 and 36; word 28 remains byte-identical and needs no row.

The full raw-body hash and complete binding map gate derivation. No inserted
or omitted instructions, changed branch displacement, frame edit, relocation
edit or compiler-profile change is allowed. Word 35 is the original unreachable
duplicate load; the qualified cases visit the other 44 words.

Normal owner Make uses three commands: IDO `-O2 -g3`, the real padder and the
assembler. Its shadow reproduces all 23 compact functions and the complete
padded object. Preserve all 22 neighbors, pools and diagnostics; this owner has
zero GLOBAL_ASM routines. Inherited duplicate-recipe warnings for another
owner remain unchanged. The Makefile is not edited.

## Qualification

Both actual tools copies pass eight genuinely fresh pre-install checks, with
zero errors, failures, skips or reused checks: active copy 320.887 seconds,
older mirror 334.109 seconds. Both shared tools checks pass, in 1.938 and
0.270 seconds. A separate native smoke check passes in 29.161 seconds.

- 9,728 partitioned guest cases cover all command/key bytes, full incoming
  command homes, first-match priority and late keys. Fourteen alias layouts
  include global-word/key and guest stack overlaps. Check raw C public
  behavior and identical fitted/original complete private state.
- 12,736 connected original/retained dispatcher cases cover the full 23-word
  caller, actual 74-entry registry, selector bounds/NULL slot, all selector
  and command bytes, masking and other-provider contracts.
- 32 connected release cases visit every original/retained helper word and
  verify the late kind reload after bookkeeping.
- Native32 `-O0`, `-O2` and `-O3`, each with trapping UBSan, pass 786,432 target
  cases and 131,072 dispatcher cases. Use canonical function-pointer types,
  actual retained release C and six heap overlap layouts. Runtime counters
  verify all 32 pattern/match pairs per command; all 16 negative controls are
  effective. Check the global on every path, including helper mutation.
- 96 paired fault prefixes and compiled early-read, parent-bound and NULL-call
  negatives preserve emitted access order. Global/stack aliases and faults
  are guest-instruction checks, not portable-C fault semantics or hardware proof.
- Reject all 45 raw-word corruptions, three binding corruptions, extent/history
  corruptions and a real-padder corruption. Six independent GNU links cover
  three layouts and eighteen rebased executions, including global HI/LO carry
  boundaries. Reject seven strict-image corruptions.
- The installed-input regression accepts the complete 73-input installed map,
  then rejects six independent mutations: source, guard CSV, target object,
  ELF, caller object and shared structs header.

The initial native fixture was tightened before acceptance: initialize pointer
members through their actual pointer lvalues, use character representation
writes, copy word reads into declared scalars, and implement the wrong-width
negative with character reads. The fixture explicitly binds little-endian
native32. This follows the effective-type/access distinction in the official
[WG14 N1570 draft, section 6.5 paragraphs 6-7](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf#page=95),
not a general ISO-portability claim. Preserve the 31 superseded evidence files
under `archived-checks/native-effective-type-368d60c`.

An initial production Make already produced the predicted image, but the
installed audit correctly failed closed: its input checker still expected the
old target object. Archive 23 exact files under
`archived-checks/installed-object-expectation-db6306a`, restore only the four
owned mutable inputs, fix the installed-object expectation and add the test-08
regression. Requalify and rerun all eight fresh checks in both copies; the final
receipts above are from that rerun. The C body and guard recipe did not change.

After final production installation, each copy passes two fresh checks in
0.619 / 0.620 seconds: literal owner/Make/registry identity and strict full
image/frozen inputs. Six semantic checks are explicitly reused only under
identical sealed inputs, module hashes, qualified artifacts and actual installed
source/object/ELF bytes. These are not eight fresh installed checks.

## Production And Preservation

The actual production command is:

```sh
make -C conker -j4 -o retail_word_patches.us.csv build/conker.us.elf progress.csv
```

The existing guarded-conversion route pins unchanged guard consumers while
freshly compiling this target with its normal compiler/padder/assembler path.
It is not an unmodified whole-tree rebuild. The old CSV prefix and every
non-target object/input are sealed and audited. Make passes in 0.452 seconds.

The complete ELF exactly reproduces the independent prediction: 127 changed
bytes, comprising 126 target-code bytes and one symbol-size byte (12 to 180).
There are zero exclusions or metadata permutations. All 6,054 other linked
bodies and all addresses are fixed. All 720 protected Game data owners,
totaling 189,088 bytes, remain exact.

The 16,038-file Native/cache seal covers all 1,454 linker input objects.
Native adoption verifies the full closure before and after promotion, with
only four overrides: source, guard CSV, target object and ELF. The actual
adopted-Native-ELF CLI recount passes in 16.443 seconds; full reclassification
removes only this function from the remaining queue, rather than manually
incrementing a counter. WSL uses the verified stdin/tar cache with explicit
`--cd`, never project-data reads through DrvFS or IDO paths containing spaces.

Tools are committed first as `0122290df8abdac615c0e358bc751c060bc41785`, then
the installed-input verifier fix as `84d483f76d41c524aa5b5a8f2806430f54cfcb3e`.
Preserve the older tools mirror's HEAD and 1,646 pre-existing changed paths;
its only additions are the two owned qualification modules. No mirror commit,
push, package/global/provider configuration changes, Claude calls, or host/
Release changes are made.

| Artifact | SHA-256 |
| --- | --- |
| Snapshot | `8214d7575dbc820bf84a1e22fa07ed8c86eed99c306b92871f6bcee077d7edda` |
| Raw 45-word body | `278254adcc7827674bc5247d93c66e98d2084a8f6051fe777802b76502ea6426` |
| Retail 45-word slot | `71c93baf6fbe91004c66eae513b361f611578086d2d9dc804976206332c1c090` |
| Qualified source | `558a4f59cbb2406666b136cea30a3c8fc1eb07dc9d5098d8874e7fda03e75f0a` |
| Qualified guard CSV | `cfcdcc86022c981b29793230450bbd9247a4b5eebbb92059e3feb01f217620f1` |
| Qualified target object | `9ca6b119355c8c23dcb58358709999ed0f1e6a43ee395427a9bc27b1f808ca24` |
| Adopted ELF | `8dadc4f74d356cc9e02c67d8b1a556d44b2ac17f5722fe2e157ed9a1d3ffa514` |

## Graph And Next Work

Use the current Graphify corpus for scoped target/caller/test navigation,
then verify relationships against source, objects and ROM. Both current-target
and next-target queries were used; budget-truncated output is not complete
relationship evidence. Preserve the existing filtered-corpus warning and audit
old-node retention after the consumer commit. Extract the two new tools modules
separately: the parent graph ignores `tools/`. Do not claim full-corpus
re-extraction or stamp missing producer provenance into graph artifacts.

The actual ELF-pinned queue contains 1,582 placeholder-shaped definitions,
120 semantic/other definitions and nine parser-unlocated entries. Keep the
existing-C `func_15014094` and parser-missed `Gfx *func_1510D8C0` separate.

The next ordinary placeholder is `func_151B19A4` in `generated_1DD500`.
Eight private refined source forms preserve 45 words/frame 24/one binding;
the best remain four words different. Preserve its eager owner read before
command gating, release modes zero/0x13 and late retarget key reads. Caller/
ABI/guest/native/fault/padder/Make/image and production gates remain open.
It is uninstalled and uncredited. The root README carries only aggregate rows.
