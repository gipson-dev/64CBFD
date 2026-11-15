# Note 2473: Actor exit effects and retained cartridge check

Date: 2026-11-15. Consumer baseline `a231b9486ab0d7433446aac317c22084fb589834`,
tools baseline `1d259161907b4d09f462f787c0e9f2e5e92a1325`.
Continuation of [Note 2472](2472-game-state-19-20-effect-phase-match-20261115.md).

`func_150C3D5C` replaces its false zero-return placeholder with complete
semantic C. Its **240 body words plus one alignment word** now match the
retail slot, with nine checked private-buffer address guards. Fresh production
recount is **4,506 / 5,514 total (81.72%)**, Game **3,833 / 4,841 (79.18%)**,
Init **492 / 492**, Debugger **181 / 181**, zero address drift, **1,008** still
different. Conversion counts remain **5,514 / 6,048 (91.17%) / 86.16% bytes**.
At the present denominator, **181** further matches reach 85%; that wider goal
remains active.

## Recovered behavior and interfaces

Owner `conker/src/game_EF410.c`, VA `0x150C3D5C..0x150C411C`, ROM
`0xF120C..0xF15CC`, body **960 bytes**, complete slot through `0x150C4120`
**964 bytes**. The frame is **0x100**, saving S0 at SP+0xD0 and RA at SP+0xD4.
The corrected local declaration is `void func_150C3D5C(u8 *actor)`; both
retained callers ignore a result. No global header or compiler profile changes.

The routine submits the sixteen-argument Type-07 record, retains the original
cartridge check, emits debris and a random spray, submits all **49** configuration
arguments, then builds a six-byte descriptor and three-word position for the
final effect. Random count and lifetime use unsigned remainders modulo 11 and
52. The position is captured between the two random calls, as in retail.
Current `func_151709B4` takes full signed 32-bit coordinates; the older historical
spray experiment's narrow declaration is not the current ABI. Constructor and
configuration coordinates retain their own original signed-halfword narrowing.

The signed cartridge local starts at `0xC23459B8`. Original decoder
`func_150C3D48` produces `0xB0000340`; the retained indirect call through
`func_151EF040` reads into that same local. When its value differs from
`0x0330C820`, retail writes `0x03E00008, 0` to `func_10004074`. Both the read
failure path and that conditional two-word write are preserved. Native tests
redirect these writes into a mutable eight-byte fixture, never native text.
The actual current PI wrapper acquires/releases PI access around `osPiRawReadIo`;
modeled provider results do not establish hardware timing or cache behavior.

## Compiler recovery and nine guards

The unsigned local emitted the right 240-word/frame shape but had **78** word
differences. Restoring its signed type recovers retail temporary allocation
and scheduling, leaving only **nine** private-buffer addresses. The raw body
SHA-256 is `6b9f78a86e13330cafd2a5164810f4e9ad72cf1f546b3f15a8952044575b1589`,
with all **14** relocation bindings pinned. No words are inserted or omitted.

| Instructions | Raw private home | Retail home |
| --- | --- | --- |
| Four descriptor stores | SP+0xF4..0xF8 | SP+0xEC..0xF0 |
| Three position stores | SP+0xE8,0xEC,0xF0 | SP+0xE0,0xE4,0xE8 |
| Descriptor/position address arguments | SP+0xF4 / SP+0xE8 | SP+0xEC / SP+0xE0 |

Each guard preserves opcode, registers and SP base, changing only displacement
by minus eight. The guest proof maps raw `[SP+0xE8,SP+0xFA)` down eight bytes,
and the unused raw eight-byte hole `[SP+0xE0,SP+0xE8)` to `[SP+0xF2,SP+0xFA)`.
This is a bijection of **26** frame bytes, including both complete aggregates
and descriptor padding. Outgoing arguments, saved registers and the check word
at SP+0xFC stay fixed. Pointer-valued A0/A1 are mapped only during the two final
address preparations through the emitter's delay slot; ordinary integer
coordinates are never interpreted as pointers.

The actual current `func_151602C0` passes the three position words by value;
`func_1516037C` copies exactly six header bytes into its allocation. Neither
retains the local descriptor or vector pointer. Their source is frozen among
the qualification inputs. Guest tests compare all six descriptor bytes under
the bijection. Native tests compare its **five defined bytes**, leaving its one
padding byte unspecified; they do not claim portable C padding contents.

## Fresh qualification

- **512 finite cases / three streams** (retail, raw C, normalized C), visiting
  all 240 retail body words, with helper mutations, register clobbers, two stack
  phases, allocation outcomes and three PI read policies. Original Type-07
  constructor **48 words** and decoder **five-word slot** execute in the guest.
- **1,582 fired memory-access prefixes / twelve complete routes**, comparing
  complete mapped memory, registers, FP state, calls, access traces, PC/delay
  position and all six descriptor bytes. **72** exceptional-coordinate model
  comparisons pass under two NaN policies. Explicit invalid conversions model
  `0x80000000`; these are not hardware FCSR or portable exceptional-C claims.
- **768 original caller cases / three streams**: the twelve-word exit window
  in `func_150C3994` and complete fifteen-word type-0x33 wrapper
  `func_151711C4`. Wrong-actor delay-slot and wrong-home controls are effective.
  The surrounding full state callback is not newly claimed as connected here.
- Native32 **512 cases each at O0/O2/O3**, UBSan traps, **eight** effective
  behavioral controls each. Native source is byte-identical to the privately
  recovered source; fresh executions are recorded separately from old receipts.
- All **240 body-word / 14 binding** corruption controls reject. Both owner
  padders reject each of nine corrupted expected words (**18 rejections**),
  preserve all 17 non-target neighbors and existing pools, and reproduce the
  complete slot through **twelve GNU links / four code/data carry layouts**.

Complete suite passes freshly before installation in **51.242 s**,
through the sibling overlay in **70.73 s**, and installed in
**54.154 s**. `make tools-check` passes. Tests qualify the stated
guest/native contracts, not full gameplay or arbitrary external providers.

## Production and preservation

Actual Make executes all **six** owner commands. The independent strict-image
prediction accounts for **786 changed bytes / zero exclusions**, including
the restored body/size and two closed symbol/string serialization reorderings:
`D_800A0338 / D_8009FF38 / D_800A4838` and
`.L1509D7C0_game_data / D_82F`. Named definitions otherwise stay fixed.
Ordinary production Make produces the identical qualified ELF. All **6,051**
function addresses stay fixed; only **one of 698** production objects changes.
Its changed sections are exactly `.text`, `.rel.text`, `.symtab`, `.strtab`.
Added names are exactly the target's newly referenced symbols.

All **189,088 protected bytes / 720 owners** stay exact, SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.
Of **853** frozen production inputs, only the four planned source/guard/owner
object/ELF hashes change; **849** others remain fixed. All eighty headers,
eighty-two include inputs, Makefile, conversion CSV and layouts remain fixed.
Nine guard rows append to the complete prior CSV bytes. No new pool is emitted;
the existing production checker still verifies the 243-word motion emitter,
its 58 bindings and **80-byte** literal pool.

Production ELF SHA-256:
`f6500a14961e2c876619e1491b0245c7b5ec2f81fd7efe43f58ab345ef229939`.
Tools commit **`449daf3fb89b6ec4167d7695957d8992cfae4506`** precedes the consumer source/guard/docs/pin commit.
The nine-file ignored overlay preserves sibling HEAD
`ddbdd16b53ce60b054fb6e11bf0649a41f48375a`, all **2,434 dirty paths** and status
SHA-256 `a3712de44f2fc37079df4a789a5015f134f6ab977a2c2da90a3fde1851606cd9`.
Evidence remains in `conker/build/game-actor-exit-150c3d5c-match/` and the earlier
`game-actor-exit-150c3d5c-private/` directory, including immutable pre-install
receipts under `qualified-private/`.

Scoped Graphify AST refresh covers **9** files, retains all
**61,828** old IDs, and records **61,883 nodes /
115,958 links**, zero lost IDs. It is not a full-corpus extraction.
Root README receives only its two aggregate matching rows. Existing duplicate
Make recipe and line-ending notices remain. The host path has scratch folders
only; no host import/build applies, frozen Release stays untouched, no push.

Next: qualify `func_150C4120` in `generated_F15D0.c`, currently retained assembly
at VA `0x150C4120..0x150C44A4`, **225 words / frame 0xF0**. Recover its complete
argument/record interfaces and current callers before converting or assigning
new C credit. The 85% total matching goal remains open.
