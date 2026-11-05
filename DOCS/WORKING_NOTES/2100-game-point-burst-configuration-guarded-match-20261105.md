# Copied-position burst configuration recovered as guarded C

Date: 2026-11-05. Target `func_151DCDE0`, owner `generated_20A290`.
Source `conker/src/game/generated_20A290.c`; original `conker/asm/20A290.s`.

## Outcome and recovered interface

The nine pre-install checks pass in **43.377 seconds**. The nine fresh
installed checks pass in **44.261 seconds**. Actual Make equals
the independently qualified owner and complete ELF byte for byte.

The semantic body is **66 words / 264 bytes**, followed by two unchanged
zero alignment words. It has the retail **104-byte frame**, thirteen
bindings and no owner neighbors. Body VA is `0x151DCDE0..0x151DCEE8`;
body ROM is `0x20A290..0x20A398`; the complete slot ends at VA `0x151DCEF0`,
ROM `0x20A3A0`. Ranking/progress includes the complete 68-word slot.

The recovered interface is
`void func_151DCDE0(Position20A290 *position, u8 channel, s32 context)`.
It copies all twelve coordinate bytes into a fully initialized 60-byte
configuration at SP+0x2C. This is a value copy; the callee receives the local
packet, not the incoming position pointer. Native layout checks
qualify its size, field offsets and typed/direct calls under the 32-bit ABI.
Shared headers and compiler profiles are unchanged.

The packet contains counts 12/5, angles 0/255, pitch -64/range 49, speeds 3/9,
vertical values from `D_800AB55C` and `D_800AB560`, lifetime 25/range 20,
two copies of the initial `D_800AB558` scale and spread `D_800AB564`.
The eight-argument `func_15152190` submission receives the local packet,
`&D_800AB550`, `&D_800AB554`, count 1, float 26, mode 0, the zero-extended
channel byte and the full signed context word. The wrapper's result is void.

Retail constants in `asm/data/250010.rodata.s` are selector 16, scale 1,
packet scale `0x3E4CCCCD`, vertical `0xBF316873`, vertical range
`0x3E9BA5E4` and spread `0x41CDB646`. Tests also vary these inputs rather
than qualifying only the default constants.

## Derived scheduling adjustments and source limits

The natural IDO body already has the correct 66-word length, frame, register
roles and operations. Four source screens retain either sixteen or thirty
scheduling differences. The selected form snapshots the scale explicitly.
Sixteen checked manifest rows implement two closed instruction permutations:
destination words 1..9 take source words6,9,1,2,3,4,5,7,8, and words46..52
take 51,52,46,47,48,49,50. No operation is invented, removed or duplicated.
Relocation bindings move with their whole instructions.

The first permutation restores the retail scale load before saved RA and
incoming argument-home writes; the second restores the two packet scale
stores before independent argument-address setup. Natural and fitted C
pass the ordinary public packet/caller contract. Private-stack alias and
fault-prefix parity is claimed only for original versus fitted instructions.
Portable C behavior for deliberately overlapping private frames is not claimed.

The normalizer checks all 264 raw bytes, thirteen bindings and sixteen
expected words before deriving the fitted body. Every raw-byte corruption,
every bad binding and every guard-preimage change is rejected. The production
manifest appends exactly sixteen rows; every prior manifest byte is retained.

## Original caller and connected callee boundary

A full aligned retail census finds one direct JAL, ROM `0x82D2C`, VA
`0x1505587C`, with no aligned target address literals or tail calls.
Its parent is `func_1505528C` in `game_77AD0.c`. The original twenty-word
window `0x15055838..0x15055888` compares actor surface at+0x118 with Y at+0x18.
Only strict less-than calls the wrapper; equality and NaNs skip it through
the original branch-likely behavior. The taken route copies actorX, Y+20
and actorZ to SP+0x4C and submits channel 255/context 1. It ignores the result
and restores the actor argument for the subsequent helper.

Sixty cases per body execute that actual window with height ties, NaNs,
coordinate patterns, both stack phases and two poisoned callee returns.
The original 56-word `func_15152190` prefix at ROM `0x17F640` is connected
through its first `func_150ADA20` call. Six connected runs verify its
240-byte frame below the wrapper's 104 and its mode 0 byte. Complete parent,
factory, random-provider and gameplay behavior remain outside this boundary.

## Focused qualification

The nine-check suite records:

* 720 guest cases per body across original, natural and fitted bodies, with
  all 66 target words visited, complete packet/argument checks and live
  provider changes to position, globals, packet, homes and caller registers.
* 2,560 original/fitted cases covering every unsigned channel byte and ten
  float bit patterns, including signed zero, subnormals, infinities and NaN.
* Eighty original/fitted private point/global layouts and 111 fired access
  prefixes with complete register, RAM and ordered-trace equality.
* Nine independent GNU links of original, natural and fitted objects at
  three layouts; all thirteen bindings, HI/LO carry edges and 36 rebased
  original/fitted cases pass. Raw GNU artifacts are retained separately.
* Native32 O0/O2/O3 pass 15,360 positive executions through typed/direct
  calls, all channel values, float patterns and provider mutation. UBSan is
  enabled. Eight native and eight separately compiled IDO controls reject
  wrong counts, pitch, scale, channel, mode, context, pointer and coordinate.
* Nine literal full-image corruptions and all sixteen real padder preimage
  corruptions are rejected; both alignment words remain zero.

The nineteen shared padder, relocation, matcher and protected-layout checks
pass freshly in **5.676 seconds**, and `make tools-check` passes. Unchanged
function suites are reused through complete linked identity rather than
claimed freshly executed. No FCSR, hardware or host gameplay acceptance is
added. Routine work uses zero Claude calls and the documented IDO/GNU path;
the Windows REA MIPS-adapter limitation is unchanged.

## Frozen inputs and complete production audit

The immutable private snapshot freezes **96 files**, including headers,
owner source/object, ELF, code binary, retail input, original target/caller/
callee/constants, caller C, layout, guard history, progress, Makefile,
linker and graph. Artifacts and source screens are retained under
`conker/build/game-point-burst-configuration-151DCDE0-match/` and the
adjacent candidate directory. The existing generated-owner padder is used.

All **6,052 function addresses** remain fixed; only the target body changes.
All **189,088 protected Game bytes across 720 owners** remain exact.
The literal complete ELF prediction accounts for **360 changed bytes**:
213 target/symbol-extent bytes and 147 bytes from five closed named GNU
symbol/string serialization permutations. These groups start at file
offsets `0x2A73BC`, `0x2AADAC`, `0x2AB1AC`, `0x2B8E2C`, `0x2D609C`.
Every symbol's original value, size, type, visibility and section is retained
except the declared target size 12-to-264 update; only group ordering and
derived string-name offsets change. Full-file comparison has **zero excluded
bytes**. Independent corruptions cover every group, strings and alignment.

| Artifact | SHA-256 |
| --- | --- |
| Natural target | `48e55cb6768699ad4e8c69efe30b48cd464407db817dab8f7029b9a08fd18a33` |
| Retail target | `c48ab78e23b381916876ed7555086bfa6271e675a796b3197d8c311aa5c3a8d6` |
| Frozen predecessor ELF | `2b159614d3d148da67218b70c03f8caa8e463dc23b675257e2c84325bdd5e5f9` |
| Production padded owner | `9ab3d4099a7950a8693fb6f2f8ed2b2fac44568f456b33c96f33674cb1a0d57c` |
| Production complete ELF | `efd54ec9785d8510c55ccd84cde8d252ccd096f554733cef46b0d34f35de9ee7` |
| Production code binary | `df06da6ac00f45fc245616e63fd00ddc3dd549593ca2d6050e4aa07fd44ef0c6` |
| Appended guard manifest | `20bbc5124bb1fbed3b51385d91e58a04bb6038226ab790facdeb19d372541839` |

Actual Make follows the guard-manifest dependency and performs its broader
rebuild. The inherited duplicate `generated_12D630` recipe warning remains.
`make -C conker all` produces the code binary and returns 2 at the expected
overall retail SHA mismatch for the incomplete decompilation. Frozen other
inputs and prior guard bytes are unchanged. The installed source's slice
comment now describes recovered code; the pre-install object evidence is
unchanged by that comment-only correction.

## Baselines, progress and continuation

Main baseline is `d4d6b335f121d9c13a03f9f974158a7c4db95695`; mounted tools
baseline is `5fb79574c85c98e288ac889f165eaabc1ff8a1b1`. Both start clean.
The sibling `64CBFD Tools` checkout remains at
`ddbdd16b53ce60b054fb6e11bf0649a41f48375a` with six tracked edits and 2,428
untracked files, as verified at the preceding checkpoint. It is untouched;
no fresh sibling qualification is claimed. Host-port Release stays frozen.

The fresh actual-ELF recount reports:

| Section | Byte-exact / converted | Match | Drift | Different |
| --- | --- | --- | --- | --- |
| Total | 4,171 / 5,512 | 75.67% | 0 | 1,341 |
| Init | 492 / 492 | 100.00% | 0 | 0 |
| Game | 3,498 / 4,839 | 72.29% | 0 | 1,341 |
| Debugger | 181 / 181 | 100.00% | 0 | 0 |

Converted inventory stays 5,512/6,046; root README edits are aggregate rows
only. The 80% threshold is 4,410/5,512, leaving **239 more** exact functions.
Fresh ranking selects **func_1501E2F8** as the next ordinary target.
Keep `func_150A76F0`, `func_151F8870`, `func_150A613C`, `func_150AE280`,
`func_15115F68`, `func_151AE2BC` and `func_150A6760` as separate documented
boundary cases. Keep the wider 80% goal open.

Mounted tools are committed first as
`629519a958dd186c12dcad8d9c4042ec2bddf3e8`
(`test(game): qualify copied-position burst configuration`). The consumer
records that pointer with the typed C, sixteen guard rows and documentation.

The ordinary AST-only Graphify update refuses its smaller 24,940-node
replacement, preserving the existing 58,732-node graph. The eight-path scoped
refresh then retains58,729 old IDs, removes three relocated update-log IDs
and adds twelve IDs. All three removed nodes have a unique replacement with
the same label and source path; **zero nodes outside changed paths are lost**.
The graph is **58,741 nodes / 112,497 links / 5,150 communities**, SHA-256
`34fad5be5e04786c6d39845781ce8b3ed23da4d0012a60c05eb814a4a0f25d52`.
Its31,816 retained nodes from3,754 files outside the current scan corpus are
preservation evidence only, not fresh full-corpus extraction. Eight new note
nodes are included. No force overwrite is used. The final receipt paragraph
adds no headings; a final scoped refresh verifies unchanged topology.
