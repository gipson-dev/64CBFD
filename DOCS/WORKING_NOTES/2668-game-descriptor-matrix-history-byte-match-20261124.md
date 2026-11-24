# Descriptor matrix-history byte match - 2026-11-24

`func_15188F84` replaces its zero-return placeholder with the complete semantic
matrix-history updater. C emits **101 words / frame 48**, with **83 words already
exact**. A separately proved closed S2/S3 lifetime swap and three commutative
operand orders normalize 18 words. All **101 retail words and 15 binding sites**
then match. The CSV protects all 101 source words: 83 identity rows, 18 actual changes,
no insertions or omissions. This is a **guarded C match**.

Production rises from **4,647 to 4,648 / 5,528 (84.08%)**, Game **3,975 / 4,855
(81.87%)**. Init stays 492/492 and Debugger 181/181. Address drift remains zero;
880 functions differ, with **51 more matches needed for 85%**.

## Complete routine and compatible callback

Original `conker/asm/1B5CC0.s:558`, VA `15188F84..15189118`, ROM
`1B6434..1B65C8`, 404 bytes. Recovered interface is
`void func_15188F84(ListNode15188A58 *record)`. It uses the existing node prefix,
so the current dispatcher declaration `void(*D_8008D580[])(ListNode15188A58*)`
and the actual table slot 1 remain compatible C. The initial draft used the
layout-compatible DescriptorDraw view, but that would require a native callback
bridge. The final source uses the actual existing node type without retyping
the dispatcher or 14 neighboring definitions. No caller/helper gains extra credit.

For this node variant, byte 1 `kind` stores history depth, byte 2 `cleared` stores
the filled count, buffer +8 stores matrix records and integer key +0x10 holds the
descriptor address. The explanatory source comment makes that reuse explicit.

1. Capture unsigned history depth and page byte D_800BE9C0. Compute current
   slot=page*depth and alternate offset=(page^1)*depth before copy providers.
2. Scan the first D_80089240 pointer cell's four-byte entries, taking the first
   unsigned halfword as the descriptor ID. Compare the node key with
   D_800DBEF4+ID*0xA0. The shared struct131 definition confirms 0xA0 stride.
   The opening and final count checks read unsigned halfword D_800DBEE8[0];
   the scan condition rereads that count. Preserve the original zero-valued
   table selector used for the indexed count access.
3. If no entry matches, clear the filled byte and return. Otherwise capture
   the selected current matrix through `*D_80089250[page]+matchedID`.
   Both rodata arrays point to **pointer globals**, requiring the second
   dereference:89240 names DBED0/4/8/C;89250 names DBEE0/4. They are not direct
   entry or matrix buffers. The selected matrix pointer survives later calls.
4. For each captured history slot, choose the captured matrix for the final
   iteration; otherwise choose records+(index+alternate+1). Reload the live
   node buffer at every call, then bcopy exactly 64 bytes to records+current.
   Increment the full loop index/current slot. Provider changes to page,
   descriptor tables and current-matrix cells do not replace captured state.
5. Reload the live depth and filled bytes after the copies; increment filled
   modulo 256 only if unequal. A captured depth of zero still performs the
   descriptor lookup and current-matrix selection before this final byte rule.

The actual caller is the JALR through D_8008D580[1] in `func_15188B74`.
The qualified original **nine-word window 15188C00..15188C24** loads the active
byte, selects the actual table entry, calls this target with the node, and
reloads timer/opacity. It overwrites V0 with opacity and ignores the target's
result. The complete large dispatcher is not claimed.

## Source fit, profile and independent relation

The initial draft emitted 91 words/frame 48. The fit recovers the zero table
selector, captures both page offsets before the loop, separates initial/current
offset lifetimes, and merges the destination through a shared per-branch buffer
load. The final source is cleaned of an extra source-level reload. It has no
volatile, register hint or compiler-profile change. Ordinary O2/g3/MIPS2/o32
reproduces the frozen-before complete object literally. All **14 other raw and
padded definitions**, pools, bindings and diagnostics remain fixed.

Raw C uses S3 for the node and S2 for captured depth; retail uses S2/S3 in the
opposite roles. The normalizer pins every source word and binding, exchanges the
two incoming-save positions, renames only the active role interval, and swaps
operands for one BEQ and two nontrapping ADDU instructions. The named save homes
and full epilogue remain unchanged. It does not emit a retail instruction table
as its implementation; all 101output words are derived from those operations.

An independent checker imports no projection. It compares decoded operations
under separate owner/depth roles, checks exact 48-byte frame/private homes, and
walks both complete CFGs (89 states each). Every role read
is dominated by its definition; each incoming register is saved before overwrite
and restored from its named home. No private stack pointer escapes. The sole
provider uses three arguments, with homes limited to 16 bytes. This establishes an
inductive public-state/call relation for compatible o32 providers, including
arbitrary public mutations. Raw private prefix/register/fault identity is not
asserted. A further commutative source instruction is accepted independently;
four structural corruptions are rejected.

## Fresh qualification

- **392 cases per stream** across raw/generic/generated/original instructions
  compare complete public state, calls, live observations and copied bytes;
  padded streams also compare all private bytes/registers/accesses. All 101
  original words are reached. Boundaries include count 0/65535, high 16-bit IDs,
  depth 0/255, filled-byte wrap, first/last/missing entries, both pages, aliases,
  live buffer/depth/count/table changes and unaligned guest copies.
- **143 dispatched-access cut points** compare the three padded/original full
  states. This is emitted-instruction prefix evidence, not portable C faults.
- **24 connected cases per stream** execute the 196 words of the original SDK
  bcopy slot at 10023A10..10023D20 as needed. Both overlap directions, identical
  addresses, all modulo-4 alignments and differing source/destination alignments
  match the independent snapshot copy model. The SDK routine remains assembly.
- Four cases per stream execute the original nine-word table/JALR window,
  verify actual slot 1/argument, restored SP/saved roles and continuation timer
  and opacity. C native checks invoke the real compatible function pointer.
- **324 SDK32 native cases each at O0/O2/O3**, freestanding/static, strict aliasing
  and UBSan traps. Logical pointer codecs preserve both levels of pointer cells;
  hashes cover every mapped public/guard byte, call word, observation and copied
  byte. The 68 unaligned/partial-matrix-alias cases are guest-only and are not
  represented as portable typed Mtx-pointer arithmetic.
- **12 effective native source controls** fail known result comparisons, with
  no signal or UBSan trap counted: missing clear, descriptor stride, page/other
  page, final slot, source/destination slot, copy size/direction, stale buffer,
  stale filled-depth condition and missing final increment.
- All 101word and 15 binding sites are covered by **232 strict padder rejection
  controls**. Four independent code/callee/global arrangements produce
  **12 GNU links / 96 guest runs**, including HI16 carries and another J region.

The sibling overlay initially lacked nine imported bcopy-oracle support files.
Each was verified byte-for-byte against tools 7f9df5c, added to the frozen bank,
and copied into the isolated overlay. Both fresh pre-install receipts were then
rerun against the complete 3362-input/1937-copy bank. The earlier primary receipt
is retained as exploratory evidence. The real dirty sibling is preserved.
Complete frozen inputs are checked once in each fresh suite process, mutable
phase outputs at later gates, and native full-input audits bracket adoption and
production. No unchanged neighbor suite is called fresh.

## Linked image, production and commits

Private actual Make replays three real commands and reproduces the entire
qualified padded owner. Independent linking uses only frozen-before C plus
original target ASM. It reconstructs all named-symbol/string metadata from the
baseline, with no selected-target C as truth. The selected C link and production
Make equal the prediction **literally: 330 changed bytes, zero exclusions**.
All 189,088 protected Game data bytes across 720 owners, all other frozen definitions/
addresses/extents and all conversion CSV bytes remain unchanged. The 101 new guard
rows retain the complete old CSV prefix, including all neighbor guards.

ELF SHA256: `afc33a8b7de6a07d0d9fb219945bb1e5c99d6cf984d90c174d51960744029f9a`.
Raw target SHA256: `810ec836e85bec4ed2598fa4be8ce9bd396133e6ed508f785cf75fb9684a57c3`.
Padded owner SHA256: `0ebb5ff5849bb0d282331844838dd40be62e600af41ccc3d96943a7aaf59d281`.

| Phase | Time | Gates |
| --- | --- | --- |
| preinstall-primary | 81.514s | 5 fresh / 0 reused |
| preinstall-sibling | 73.496s | 5 fresh / 0 reused |
| installed-primary | 62.960s | 5 fresh / 0 reused |
| installed-sibling | 68.469s | 5 fresh / 0 reused |

Shared tools-check passes separately. Tools commit
`22b636023d0e2e4b091ca9c45f9143d46e034e19` precedes the consumer
source/guards/pin/docs commit. Codex used zero Claude calls. Graph receipts
separate normal update, observed commit-hook completion and scoped AST merge
retaining prior IDs and unchanged-owner qualification metadata; this is not
full-corpus re-extraction. Host configuration inputs are reverified with no
direct C consumer at the inspected path; no host/Release change or build.
README gets only two aggregate rows. Five DOCS indexes receive a concise entry
with all old bytes retained. Keep the 85% goal active; renderer 15197148 remains private.
