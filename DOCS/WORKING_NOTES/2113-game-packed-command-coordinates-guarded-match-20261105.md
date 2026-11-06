# Packed command coordinate updater recovered and matched

Date: 2026-11-05. Target `func_15062D10`, owner `game_83300`.
Source `conker/src/game_83300.c`; original
`conker/asm/nonmatchings/game_83300/func_15062D10.s`.

## Result and six-word interface

The complete **69 words / 276 bytes**, frame **zero**, match at
VA `0x15062D10..0x15062E24`, ROM `0x901C0..0x902D4`.
This is complete semantic C with **39 register/scheduling guards** and
four unchanged HI/LO bindings. The normal O2/g3 profile remains in use.
No instructions are inserted or omitted, and no Makefile rule is added.

The recovered interface is
`void func_15062D10(s32 slot, s32 entry, s32 dx, s32 dy, s32 bank, s32 absolute)`.
The entry index, dx and dy are stored into their incoming O32 homes at
SP+4/+8/+12. Bank and absolute occupy SP+0x10/+0x14. The original V0
lifetime is preserved by the fitted instructions without inventing a C result.

1. Read the slot's word in the `D_800D19A0` resource table. A zero word exits
   after the three parameter-home stores and the bank-home delay-slot read.
   It does not read the command pointers or absolute-mode home.
2. Follow the slot/bank pointer chain rooted at `D_800C4488`, then select
   the eight-byte command by entry index. The second word supplies two
   twelve-bit extents, each increased by two: possible extents are 2..4097.
3. For any nonzero absolute argument, use the low twelve bits of dx/dy.
   Otherwise add each signed delta to its existing twelve-bit coordinate,
   wrapping the sum to 32 bits before signed tests. If the sum is strictly
   greater than its extent, subtract that extent once. If negative, add it
   once. Equal-to-extent values are retained. This is not modulo/repeated wrap.
4. Replace the first word's two coordinate fields, preserving its entire high
   command byte. The second word and all neighboring commands stay unchanged.

For example, extent three and sum three retain coordinate three; an inclusive
comparison would incorrectly produce zero. Sum -4 and extent three become
-1, then pack as 4095; a complete modulo operation would have different results.
The source uses explicit unsigned additions before narrowing back to s32,
preserving retail overflow behavior for full-word deltas.

The existing shared scalar declaration of `D_800D19A0` is retained through
an address-based table view. The pointer-chain interpretation agrees with
the loader/renderer owners. No shared header or global data layout changes.
The function retains retail's lack of slot/index/bank bounds checks.

## Source shape and constrained normalization

The first draft emitted 67 words. Taking the address of the entry parameter
recovers its incoming home and reload, restoring all 69 words. Its first
thirteen instructions match directly. The selected two-stage final packing
preserves the original high-byte/Y merge followed by the shifted X merge.

The remaining fit is explicitly constrained:

- Swap instruction positions 0x50/0x70 to move the dx-home and command-word
  reads, and swap positions 0x68/0x6C for the height update and mode branch.
- Change that moved branch's displacement from five to four, preserving its
  absolute target at function offset 0x80.
- Normalize only decoded GPR operand fields in the aligned instruction stream.
  All other opcodes, immediates and relocations are identical. Commutative
  addition/OR operand orders are checked as equivalent value operations.

The 39 appended expected-word guards encode only that bounded fit. Every
predecessor manifest byte is retained, with no insert/omit rows. Full raw and
original hashes and all four bindings are pinned before fitting.

`game_packed_coordinate_roles.py` explores **265 symbolic instruction states
and 17 syntactic terminal paths** of the aligned programs. It checks branch
conditions, ordered memory addresses/values, return control and the final
store using one symbolic initial memory, including the incoming-home stores.
Both global bindings retain distinct actual addresses. Branch-likely delay
annulment and conservative combinations of repeated mode tests are included.
The explorer is specific to this fixed, acyclic instruction window; it is
not a general MIPS proof system or a claim of hardware acceptance.

This proof follows the declared rescheduling. Raw C has a different read
schedule: in particular, the fitted dx-home load is unconditional on the
enabled path instead of remaining in the absolute branch. That home has
already been initialized by the original parameter store. Raw public values
and complete final memory are checked separately; raw access/fault/private
state equality is not claimed. The fitted/padded instruction window and its
fault/private state are literal retail equality.

All **88 other owner functions** and every compact/padded allocatable pool
remain identical. The eight inherited IDO Warning 712 diagnostics remain
unchanged after path/line normalization. The build is not warning-free.

## Caller and execution qualification

A full aligned ROM census finds **21 JALs**, all in original
`func_15061B4C`, and no tail jump or aligned address literal. Its current
placeholder is not converted or credited. The typed six-argument declaration
replaces the old-style local declaration; there are no C call sites to rewrite.

All 21 original argument/call windows execute, including the signed-byte
load in one call's delay slot. Prepared caller input memory supplies that
byte; the earlier producer and the complete enclosing parent remain outside
the acceptance claim. There are **84 window cases per body** across two
slot values and both stack phases. Each original prefix supplies the observed
six-word ABI, then original/raw/fitted/padded targets produce independently
checked command updates. This is not whole-parent gameplay acceptance.

Seven checks pass before and after installation:

- **442 guest cases per body**, all 69 words, both modes, zero/negative/nonzero
  resource words, exact X/Y ties, large positive/negative corrections and
  full-word overflow boundaries. Full memory includes the parameter homes.
- **52 alias/wrapping-index cases**, including command words in dx/dy homes
  and resource gates in the incoming homes. **50 fired fault prefixes** and
  three sparse cases check the fitted/padded original access order. A disabled
  slot still needs its bank home, while its absolute home/pointer tree may be
  absent. These unusual pointer/home/index probes are guest-only evidence.
- **Twelve independent GNU links**, three entry/data layouts and all four
  HI/LO bindings, including signed-low carry boundaries.
- Native32 O0/O2/O3 with UBSan pass **655,372 calls per profile / 1,966,116
  executions**. The grid covers all 4,096 coordinate values on both axes,
  extents 2/3/4096/4097, ten deltas including INT_MIN/INT_MAX, and four mode
  bit patterns. Twelve disabled-slot calls per profile use null pointer
  tables. An independent widened 64-bit formula checks single correction;
  command neighbors, extents and pointer tables are checked unchanged.
- **Fifteen effective IDO and fifteen native negative controls** reject gate,
  entry, bank, mask, extent, both strict ties, negative correction, mode,
  command-byte, field shift, store destination/absence and modulo errors.
- **276 byte, four binding, 78 guard and four symbolic data-flow corruptions**
  are rejected. Five full-image corruptions and the old stub are rejected.

Run the focused suite with:

```sh
python3 -m unittest tools.tests.test_game_packed_coordinates_match -v
make -C conker -j4 build/conker.us.elf progress.csv
make -C conker match-progress NON_MATCHING=1
make tools-check
```

The installed suite, nineteen mounted shared checks and tools smoke pass.
The dirty sibling tools checkout passes its twelve supported shared checks
and smoke without edits. Prior neighbor suites are reused through unchanged
complete function/binding/pool evidence. Routine Claude calls: zero.

## Literal production image and inputs

The immutable snapshot contains **154 files**, including every header,
target/owner and caller assembly inputs, ROM, manifests, Makefile, linker,
source/object, ELF, binary, progress and graph. Artifacts remain under
`conker/build/game-packed-coordinates-15062D10-match/`.
Consumer baseline: `0abdc4f5cffb79a6eb4f40950bae515579f06e69`.
Mounted tools baseline: `165d1f230c6fdedca76a1e310e5bb8f43486973a`.

Actual Make equals the independent owner and **entire ELF** byte for byte.
Exactly **214 bytes** change, confined to the target slot and its symbol
extent from 12 to 276. There are no metadata permutations or excluded bytes.
All **6,052 function addresses** stay fixed and every other body is unchanged.
All **189,088 protected data bytes across 720 owners** remain exact.
The entire progress CSV, original ASM, Makefile and headers are unchanged.

| Artifact | SHA-256 |
| --- | --- |
| Natural target | `e38cc4acee36c21691768f824e77badad7886cbed7a79aeaf1eebc48eab2f2f0` |
| Original target | `2b7d78b9c42e156ace1cc8a39679824c8e85cab22f537fc34be7994090ca22a2` |
| Production owner | `2c8859759bd0adc7cb431e0d7b04ee0e58e07ccf6007f5bed1f6c439d44c649f` |
| Complete ELF | `c41bae710fe29ede70d4c1adaaaf38a44fbd8b7c6170b80ff7713063f83b3c8f` |
| Code binary | `b759e3455a629bf6c331a22e97134a23c85bd5def97714b3bf13c956ae401c7a` |
| Extended guard manifest | `0524361a35e42383eeae5543dd7bb876d311824b5515880d8ed907f24c250353` |

The rebuild/recount takes **264.017 seconds**.
`make -C conker all` returns 2 only at the known incomplete-project retail
checksum mismatch. Source newline styles and prior documentation bytes are
preserved. Root README changes aggregate rows only. Unrelated sibling dirty
work, private inputs, real saves and frozen host Release remain untouched.

## Progress and continuation

| Section | Byte-exact / converted | Match | Drift | Different |
| --- | --- | --- | --- | --- |
| Total | 4,184 / 5,512 | 75.91% | 0 | 1,328 |
| Init | 492 / 492 | 100.00% | 0 | 0 |
| Game | 3,511 / 4,839 | 72.56% | 0 | 1,328 |
| Debugger | 181 / 181 | 100.00% | 0 | 0 |

Converted inventory remains 5,512/6,046. The 80% threshold is 4,410,
leaving **226 more** exact functions. Continue with **func_15077F64**,
68 original words / frame 0x28, owner `game_A28B0`, original
`conker/asm/nonmatchings/game_A28B0/func_15077F64.s`,
ROM `0xA5414..0xA5524`. It computes a heading from a record's signed
coordinates and current actor position, reloads the live actor after the
query, reduces the heading difference to an unsigned circular byte distance,
and conditionally updates state/calls the turning helper. Its signed initial
mode versus saved byte, pointer reloads, helper ABI, source shape and all
execution/production gates still need qualification. It is uncredited.

Retain the eight separate boundaries from Note 2103: func_150A76F0,
func_151F8870, func_150A613C, func_150AE280, func_15115F68,
func_151AE2BC, func_150A6760 and func_150A70C0. Keep the 80% goal active.

Mounted tools are committed first as
`478e79fcd5086a1612045e5b6ce53ce0fe529aad`
(`test(game): qualify packed command coordinate updates`). The consumer records
that exact pointer with the recovered C/interface, 39 guards and documentation.
These are local commits; no push is made.

The ordinary Graphify update refuses its smaller 25,028-node replacement.
The following refresh is scoped to the eight changed consumer paths. It
retains 31,816 nodes from 3,754 files outside the current scan corpus;
this is not a fresh full extraction or a graph-package/policy change.

The scoped refresh retains 58,829 old IDs and relocates three update-log
IDs through unique same-label/same-source replacements. No nodes outside
changed paths are lost. It adds 10 IDs. The result is **58,839 nodes /
112,601 links / 5,102 communities**, SHA-256
`1fb1fff80c9b324e7c3802cf5df4ff156e1244a86b55a7f3cd78f7c290a5ca41`.
The target node is refreshed to L1362; its outgoing graph labels are
`s32`. Emitted code and the original caller/ABI audit remain authoritative.
No edge is hand-added. A following refresh reports no topology changes and
leaves the graph hash stable.

The final production audit verifies the full ELF/binary/owner/guard hashes,
all 154 frozen inputs and unchanged progress/Makefile. Historical documentation
bytes are preserved; the root README changes only two aggregate rows. The
separate sibling dirty state and frozen host Release remain untouched, and
the wider 80% goal remains active.
