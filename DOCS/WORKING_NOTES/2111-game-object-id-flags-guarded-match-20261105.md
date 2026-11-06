# Object ID classifier recovered with five scheduling guards

Date: 2026-11-05. Target `func_1503B840`, owner `generated_68C70`.
Source `conker/src/game/generated_68C70.c`; original `conker/asm/68C70.s`.

## Result and recovered interface

The complete **71 words / 284 bytes**, frame **zero**, match at
VA `0x1503B840..0x1503B95C`, ROM `0x68CF0..0x68E0C`.
The recovered interface is `void func_1503B840(struct127 *object)`.
The existing canonical object supplies the signed state at zero, unsigned
halfword `unk84.uh` at 0x84 and flag byte `unk2FB` at 0x2FB. No new structure,
header change, null guard or speculative field rename is introduced.

1. Reject every interaction state except one before reading the ID or tables.
2. Snapshot the unsigned ID and scan the three primary IDs in order. On a
   match, OR bit two into the existing flags and return immediately.
3. Compare the two singleton IDs in order, then scan all 88 lower-table IDs.
   On the first match OR bit one into the existing flags and return.
4. A miss leaves the flags untouched, without reading them.

The primary values are 233, 72 and 75. Singleton values are 206 and 233.
Consequently ID 233 takes the primary bit-two path, despite appearing in
the second singleton too. The end sentinel is zero and is never read.
The reference reads final fixture memory rather than a precomputed lookup,
so overlapping object/table probes retain the actual ordered behavior.

## Compiler schedule, aliases and unchanged neighbors

The normal O2/g3 profile already recovers the full length, frame and loop
shape. A u32 ID local preserves the zero-extended halfword and original
register allocation. A u16 local did not produce the selected layout.
There is no Makefile or compiler-profile change.

Five expected-word/relocation guards at offsets 8, 16, 20, 24 and 28
permute only the two opening table addresses and ID load. Their complete
instruction/relocation multiset is unchanged. The guard extension preserves
every predecessor byte and adds exactly five rows, with no insert/omit rows.
All other words emit unchanged from semantic C.

The lower loop naturally expresses its end as `D_80098780 + 176`, equal to
`D_80098830`. The original disassembly names the latter; the candidate keeps
the ordinary C addend in its HI/LO relocations. The GNU rebase fixtures
preserve this contiguous layout instead of moving aliases independently.
There are twelve raw and fitted bindings. Three signed-low carry layouts
qualify original, raw, fitted and padded objects through twelve GNU links.

All four other functions remain identical in both compact and padded owners.
The compact `.reginfo` mask alone adds bit 0x2000 for T5:
`a300dffe` becomes `a300fffe`; every other byte in that 24-byte record and
every other compact pool remains identical. Padded pools remain identical.
This explicit metadata comparison does not exclude `.reginfo`.

The 188-byte table group at `0x8009877C..0x80098838` remains identical to the
original ROM at `0x23D23C..0x23D2F8`, including both singletons, all lower and
primary entries, and the unread sentinel. Its SHA-256 is
`3604cee2ae24af0c6efdeef9195557fbc8e2becf8cda7b18dc7a80cafc777a9e`.

## Caller and qualification evidence

A full aligned ROM census finds exactly one direct JAL, at ROM 0x8FC90 /
VA 0x150627E0, and no tail jump or aligned address literal. The complete
11-word caller is `func_150627D4` at VA 0x150627D4..0x15062800,
ROM 0x8FC84..0x8FCB0. It clears flags, calls the classifier, then calls
`func_15039CC8` with the original object. The return value is unused.

The caller now has the correct void prototype. Its complete padded object
and all 89 owner functions stay byte-identical. Its eight inherited IDO
Warning 712 diagnostics are unchanged after filename/line normalization.
The production build is not claimed warning-free.

Seven focused checks pass before and after installation:

- 816 guest cases per original/raw/fitted/padded body, with both actual and
  synthetic unsigned tables, all lower/primary entries, state rejection,
  existing-flag preservation and exact ordered reads/stores.
- All **68 reachable words** execute. Static control-flow closure proves
  offsets 180, 208 and 236 unreachable from root entry: they are duplicate
  loads after return delay slots. All 71 words remain byte-exact.
- Twelve mapped alias cases, 510 fired access-fault prefixes and six sparse
  cases, including a state-only object, unmapped null, unaligned object and
  an unmapped sentinel. Invalid-address probes qualify guest order only.
- 256 cases per body connect the full original caller, both stack phases,
  flag clearing and either an effectful opaque consumer or the original
  consumer's five-word null-child gate. This does not qualify that helper's
  other 125 words or its currently nonmatching production implementation.
- Twelve GNU links and 129 cases per body at relocated entries/table bases,
  including signed-low carry boundaries and the lower-plus-176 alias.
- Native32 O0/O2/O3 with UBSan validate the canonical 0/0x84/0x2FB offsets
  and object size 0x32C. Per profile, 1,061,888 root and 512 wrapper calls
  total **3,187,200 positive executions**. All 65,536 IDs are tested against
  eight flag values in both datasets; wrong states cover all 256 flag bytes.
  Thirteen IDO and thirteen native negative controls each fail effectively.
- 284 raw-byte, twelve binding and ten guard corruptions are rejected.
  Seventeen literal-image corruptions cover the target, surrounding bytes,
  header, six symbol groups and six string blocks. The old stub is rejected.

The synthetic table makes the normally shadowed second singleton reachable
and includes IDs above 0x7FFF. Native invalid-pointer/alias behavior is not
claimed. Raw C shares the public contract and access order; its private
caller-save registers on the rejected-state path are not claimed identical.
Fitted and padded instruction/fault/private state is literal equality.

Mounted shared checks: nineteen passing tests and `make tools-check`.
The separate dirty sibling tools checkout passes its twelve supported
shared tests and smoke check without any edits. Existing neighbor-suite
receipts are reused through unchanged function/binding/pool evidence.
Routine Claude calls: zero.

## Literal production image and preserved inputs

The immutable snapshot contains **158 files**, including every header,
target/caller source and objects, original assembly and caller ASM inputs,
table data, ROM, manifests, linker, Makefile, ELF, binary, progress and graph.
Artifacts remain in `conker/build/game-object-id-flags-1503B840-match/`.
Consumer baseline is `756fe694cc46b0f1eb34b407a0735215aa7df138`;
mounted tools baseline is `f6749eb211c5b2789ab03756c8ee7566d2a194ab`.

Actual Make equals the independently assembled owner and entire ELF byte
for byte. The literal prediction accounts for **389 changed bytes**: target
slot, size from 12 to 284 and **161 symbol/string serialization bytes**.
Six fixed closed groups reorder existing records/names; all named definitions
remain identical apart from the declared target size. No ELF bytes are
excluded. All **6,052 function addresses** stay fixed and every other body
is unchanged. All **189,088 protected data bytes across 720 owners** are exact.
The complete caller object, Makefile and progress CSV remain unchanged.

| Artifact | SHA-256 |
| --- | --- |
| Natural target | `3794cd2eaa1de290c26f065c70aedf98a5e09acb67f689ceeeb32e5b2e389b3c` |
| Original target | `4945b7f8f3e1a2d8b575337cbd788d5517decb2181ad675f15bd8ce99e413306` |
| Production owner | `12512a6b8d91ccd8f07a01a45118e063a7ea9b61b397ff2d2b8a81dc587262e7` |
| Complete ELF | `3a9e879e9e2a27a2d73b27b77f012deba9017904b101b9487d4ca7b0c4a57d83` |
| Code binary | `dc10c498b944ca806d87f9cdda8155ee445c1ef4590d52494e336b371c031c99` |
| Extended guard manifest | `b784d5e46c4114cc4a67864835237bd0f85e4c49c451709ada41df8289314ee4` |

The rebuild/recount takes **285.520 seconds**.
`make -C conker all` returns 2 only at the expected incomplete-project retail
checksum mismatch. Existing recipe/compiler warnings remain. Source newline
styles are preserved; root README changes aggregate rows only. Unrelated
sibling dirty work, private inputs, saves and frozen host Release stay untouched.

## Progress and continuation

| Section | Byte-exact / converted | Match | Drift | Different |
| --- | --- | --- | --- | --- |
| Total | 4,182 / 5,512 | 75.87% | 0 | 1,330 |
| Init | 492 / 492 | 100.00% | 0 | 0 |
| Game | 3,509 / 4,839 | 72.51% | 0 | 1,330 |
| Debugger | 181 / 181 | 100.00% | 0 | 0 |

Converted inventory remains 5,512/6,046. The 80% threshold is 4,410,
leaving **228 more** exact functions. Continue with **func_1505F188**,
68 original words / frame 0x18, source `conker/src/game_83300.c`, original
`conker/asm/nonmatchings/game_83300/func_1505F188.s`,
ROM 0x8C638..0x8C748. It clears the 0x32C-byte object, sets defaults,
draws an unsigned RNG remainder, calls the component initializer and writes
trailing fields. The first private draft emits 69 words and preserves its
other 88 owner functions. It needs shape, declaration/field, caller, helper,
guest/native, padding and production qualification; it is not installed or credited.

Retain the eight separate boundaries from Note 2103: func_150A76F0,
func_151F8870, func_150A613C, func_150AE280, func_15115F68,
func_151AE2BC, func_150A6760 and func_150A70C0. Keep the 80% goal active.

Mounted tools are committed first as
`237f614ead7e57553bda6c3ae564c84059f288be`
(`test(game): qualify object ID flag classification`). The consumer records
that exact pointer with the recovered C, caller declaration, five guards and
documentation. These are local commits; no push is made.

The ordinary Graphify update refuses its smaller 25,014-node replacement,
leaving the prior graph byte-identical. The subsequent refresh is scoped to
the nine changed consumer paths. It retains 31,816 nodes from 3,754 files
outside the current scan corpus; this is not a fresh full extraction.

The scoped refresh retains 58,815 old IDs and relocates three update-log IDs
through unique same-label/same-source replacements. No nodes outside the
changed paths are lost. It adds ten IDs, seven for this note and the three
relocated headings. The result is **58,825 nodes / 112,597 links /
5,231 communities**, SHA-256
`53f0134a425cf0fe38a975e152ab45e149b69a8965f9751ad4d9116b016639b4`.
The target node is refreshed to L29 with its canonical struct127 reference.
Source/ABI and emitted-code evidence remain authoritative. No graph package,
policy or hand-added edge changes are made. A following refresh reports no
topology changes and leaves the hash stable.

The final production audit verifies the full ELF/binary/owner/guard hashes,
all 158 frozen inputs, unchanged Makefile/progress and the complete caller
object. The documentation diff preserves all pre-existing history bytes,
including non-ASCII text. The decomp result remains separate from host-port
gameplay acceptance.
