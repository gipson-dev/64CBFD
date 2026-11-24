# Effect floor query byte match - 2026-11-23

`func_1515A78C` replaces its zero-return placeholder with the complete effect
floor query and conditional contact submission. Semantic C emits **98 words /
frame 80**; independently proved pointer/home/register scheduling reproduces
all **101 retail words**, using **98 expected-word guards, three source-derived
insertions and no omissions**. This is a guarded C match.

Production rises from **4,644 to 4,645 / 5,528 (84.03%)**, Game **3,972 / 4,855
(81.81%)**. Init stays 492/492 and Debugger 181/181. Address drift remains zero;
883 functions differ, and **54 more matches are needed for 85%**.

## Source, interface and original dispatcher

The original complete routine is `conker/asm/185560.s:2730..2838`, VA
`1515A78C..1515A920`, ROM `187C3C..187DD0`. The recovered interface is
`s32(u8 *record, f32 *position)`, returning 0/1. Its former untyped placeholder
was 12 bytes; the new symbol extent is 404 bytes. No exported interior entry
or neighboring definition changes.

1. Set the private result byte to 1, call `func_1515A60C(record, position)`, then
   read the live vertical value at record+0x5C. Ordered negative values return 1;
   NaN does not take this branch.
2. Initialize a complete 12-byte point from the live x/z fields and offsets at
   +0x40/+0x4C and +0x48/+0x54, with y from position[1]. Capture payload+0xA8 and
   its value at +0x20. The existing `MotionPayload1515A11C` supplies this exact
   layout; its `rate` field is interpreted as a cached floor height here.
3. A cached value equal to `D_800A6408` selects the query route. A zero result
   from `func_1514672C(point)` returns 0 immediately. Otherwise call
   `func_15046C00(point, 0, live record.height44, record+0x80)`. Nonzero copies
   the live returned height into point.y and clears the result; zero retains 1.
   A nonsentinel cached height at or below the live record height instead
   replaces point.y and clears the result without either query call.
4. Result 0 selects `func_150ADA68()`. Only an ordered result below the live
   `D_800A640C`, followed by live state byte+0x9D equal to 3, submits a contact
   effect. Call `func_151D8E20()` first, then load all final arguments:
   selector.low8, live payload.center times live `D_800A6410`, byte+0x2B,
   record+0x84, point, byte+0xC and byte+1. Return the result byte.

The provider selector is a separate statement, preserving post-provider live
argument reads across native compiler evaluation orders. The actual helper
definitions establish `1514672C(struct17 *)`,
`15046C00(f32 *, u16, f32, HeightResult71820 *)`, `150ADA68(void)` returning f32,
`151D8E20(void)` returning u8, and the existing seven-argument `151DBCBC` ABI.
The exact tagged 0x24-byte height-result layout is reused locally; state is at
+0x1D. Shared headers and caller declarations remain fixed. The original
`1515A60C` and `151DBCBC` assembly remains intact, with no helper matching credit.

`D_800A6408/0C/10` retain original bits C7C34FF3 / 3E4CCCCD / 3E4CCCCD from
`asm/data/24AE60.rodata.s:111..121`. Callback table `D_80089760` slot 21, at
800897B4 in `asm/data/22E220.rodata.s:29`, references this routine. The actual
dispatcher is `func_151303EC`. The original 17-word window 15130A0C..15130A50
loads its signed callback byte, bypasses index -1 or nonzero A3, indexes the
table, passes record and SP+0x48, saves/restores record and A3 across JALR,
and converts a zero callback result to A3=1. This bounded window is executed
with the real callback connected; the complete enclosing dispatcher is not
claimed as newly qualified or credited.

## Source fit and independent proof

The initial complete body emitted 101 words/frame 80. Seven cache/operand/return
forms, 15 pointer/control/storage forms, six aggregate forms and six vector/
selector forms were measured. Explicitly capturing the cached height gives
98 words/frame 80. All **36 raw neighbors**, pools and diagnostic rows remain
fixed. Existing O2/g3/MIPS2 and ordinary types are retained, with no volatile
qualifier or compiler-profile change.

The pinned normalizer accepts only the measured source words and bindings.
It derives the retail payload address, save and reload from real C pointer,
store and load instructions; moves the initialized point and result homes;
replaces the redundant promoted result spill with retail byte loads; restores
the closed temporary-register schedule, branch/likely slots and symmetric FP
equality operand order. It takes no retail payload as a code-generation input.

An independent instruction model imports no projection map. All **10 finite
paths / nine branch keys**, with 1, 2, 3, 4 or 6 opaque calls, agree in ordered
public reads, calls, returned values and saved-register lifetimes. Float add
and multiply retain exact operands. The initialized point is related by its
12 bytes under private-address renaming. Every later provider may arbitrarily
replace all public RAM and all previously exposed point bytes, including
pointers retained by earlier providers. Initial dead roles, provider volatile
registers and outgoing homes differ independently between the two programs.

**19 effective instruction corruptions** are rejected by changed predicates,
public observations or returned values; unsupported-instruction failures do
not count. Complete T0/T1 alpha renaming and independent private-result-home
moves remain accepted. This proof concerns normal mapped-RAM execution with
compatible returning o32 providers, valid bounded point access and public
aliases. It does not establish raw private/fault/FCSR/trap identity, adjacent
private access, numeric private/code-address reflection, transitive provider
execution or physical gameplay acceptance.

## Fresh validation and complete image

| Paired run | Elapsed | Gates |
| --- | ---: | --- |
| preinstall-primary | 121.288s | 5 fresh / 0 reused |
| preinstall-sibling | 99.091s | 5 fresh / 0 reused |
| installed-primary | 102.140s | 5 fresh / 0 reused |
| installed-sibling | 90.783s | 5 fresh / 0 reused |

- **804 cases per stream** execute raw C, generic padding, generated padding
  and original retail instructions. Signed zero, subnormals, infinities, NaNs,
  sentinel/height/threshold boundaries, full-word gates, all 256 selectors,
  record/position aliases and retained-point/provider effects are covered.
  Padded/retail execution compares complete private bytes, registers and access
  traces. Original duplicate loads at words 19 and 55 are unreachable and stay
  protected literally by the strict guards.
- **137 fault-prefix triples** compare the three exact instruction streams;
  these qualify emitted instruction order, not portable C faults.
- **32 original dispatcher-window cases per stream** include eight connected
  calls and 24 bypasses; six zero results set the caller flag. Saved record/A3,
  public effects and callback arguments agree. No whole-caller claim is made.
- **804 SDK32 native cases at each of O0/O2/O3** pass with strict aliasing and
  UBSan. Typed record fields, float arrays, height results, guards, public
  aliases, pointer/endian codecs, observations and retained point effects are
  checked. **14 source controls** reach known comparison exits 10..14; no crash,
  signal, sanitizer trap or compiler failure is counted as a semantic rejection.
- Both **complete owner padders** preserve all 36 other definitions, bindings
  and pools, and produce identical metadata. **220 fail-closed word/binding
  controls** cover all 98 source words and 12 binding sites through both target
  padders. **12 GNU links / 96 guest rebase runs** cover four independent code,
  callee and contiguous-global arrangements, including split HI/LO carry.
- Actual Make replays five production commands and reproduces the entire
  padded owner. Frozen old C plus only original target ASM constructs an
  independent full reference. Prediction, actual C link and production Make
  agree literally: **307 changed bytes / zero exclusions**.
  The target-size change and 3 reordered
  symbol records are independently accounted. All **189,088 protected Game
  bytes / 720 owners**, other function bodies/addresses/extents, conversion
  rows, original assembly, layouts, headers and prior guards remain fixed.

```text
before ELF: 5352a14473b8a21c274371d6e8ecc9a72d3483d6a3fb4bd8922cc3aa34e21dc6
after ELF:  d0df9542f35f293a85c5561fe2a946cfc039c8ad911224fabeb5f0fa8ba3de1b
owner:      286aee7cd5896444fe93f83789c23fc9f4e98d799dcd707a1f9b89cc7a11d97f
```

The 98 guard rows append to the exact previous CSV bytes. Production Make holds
only the inherited guard-dependency timestamp old; the changed source rebuilds
and reads the new guards. Unchanged prior receipts remain fingerprinted and
are not called fresh tests. Shared tools checks pass.

Tools commit `6217872ff6f938ea555e310bfcbd20b84f8ad87e` precedes the consumer
source/guards/pin/docs commit. The dirty real tools sibling is preserved through
an isolated overlay. Host configurations consume binary artifacts and do not
reference this C owner; no host build or Release change occurs. Codex resolved
the work locally with zero Claude model calls. Graph receipts distinguish the
normal refresh, observed hook completion and scoped AST merge with old-ID
retention; this is not full-corpus re-extraction.

README changes only two aggregate rows. Five DOCS indexes receive this short
checkpoint entry while every previous byte remains intact. Continue the active
85% goal from this banked checkpoint; renderer15197148 remains private on its
older baseline.
