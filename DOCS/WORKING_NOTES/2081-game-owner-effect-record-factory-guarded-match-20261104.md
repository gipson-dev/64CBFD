# Working Note 2081: Game owner-effect record factory guarded match

Date: 2026-11-04

## Result

`func_15158BD0` at `0x15158BD0` now replaces its zero-return placeholder
with typed semantic C in owner `generated_185560`. The recovered routine
allocates a type-`0x2E` record, binds it to the supplied owner, initializes its
fixed classification and position fields, delegates the final classification,
and releases the record if that helper rejects it.

Retail and natural IDO `-O2 -g3` C both contain 65 words and use a 48-byte
frame. Twenty-three fail-closed expected-word rows normalize one independent
compiler scheduling/register-allocation window at `+0x05C..+0x0C0`. No word
is inserted or omitted. The null routes, allocation, complete field writes,
classification call, rejection cleanup, and successful return remain in C.

The recovered interface is:

```c
OwnerEffectRecord15158BD0 *func_15158BD0(
        u8 *owner, u8 enabled, s32 extraBytes);
```

The caller declaration in `generated_179F30.c` now records the unsigned-byte
second argument and signed payload-size argument. Its rebuilt owner object is
byte-neutral; the strict production ELF is identical to the independently
predicted qualified ELF.

## Recovered record contract

The typed 0x58-byte base record preserves the retail layout and writes only
the fields observed in the original function:

- a null owner returns null without calling the allocator;
- `func_15167A68(0x2E, 0, extraBytes + 0x58, 1, 0xFF, 1)` allocates the base
  record plus caller-requested trailing payload;
- allocation failure returns null;
- the owner pointer and owner identity byte at `owner[0x3B]` populate offsets
  `+0x18` and `+0x1C`;
- the owner's binary32 XYZ fields at `+0x14`, `+0x18`, and `+0x1C` populate
  record offsets `+0x20`, `+0x24`, and `+0x28`;
- classification bytes `2, 2, 2, 3`, the fixed zero byte, and normalized
  enabled byte populate `+0x2C..+0x31`;
- active/state become `1/0` at `+0x10/+0x14`;
- `func_15159370(owner, &record->classification, record)` owns offset `+0x1D`;
- classification failure releases through `func_1516979C` and returns null;
- success clears the tail byte at `+0x50` and returns the record.

Reserved ranges `+0x1E..+0x1F`, `+0x32..+0x4F`, and `+0x51..+0x57` remain
untouched. Trailing bytes beginning at `+0x58` are owned by the seven callers,
not by this base factory.

## Byte and relocation proof

The natural body has 23 positional differences, all inside one closed
schedule/allocation window. Applying the checked normalization produces the
complete retail body:

- 23 checked replacements with no insertion or omission;
- three natural and retail `R_MIPS_26` bindings at `+0x044`, `+0x0C8`, and
  `+0x0D8` for allocation, classification, and release;
- all 36 neighboring owner functions unchanged;
- no unguarded replacement, exclusion, address shift, or protected-data
  change.

The compact natural object body SHA-256 is
`17a8d4b286a659d93699910c73e788584b14643a86635fd5adcda36314ca18c8`.
The naturally linked target SHA-256 is
`6e662259f683d7cb40f838267495c4d68eb709a6dc316a18cbfa4648c343b9ce`.
The qualified target equals retail with SHA-256
`7ed8b0367cb7731e439dff8f3b43df4a15cd0a1c15dec8536121f3625b2d5d1e`.

## Behavioral qualification

The big-endian guest model executes 192 cases per body across owner presence,
allocation success, classification success, four enabled inputs, three
trailing sizes, and two memory phases. Retail and natural C each visit all 65
words. Null-owner, allocation-failure, classification-failure, and success
paths produce identical calls, results, public record bytes, and reserved-byte
preservation.

Native 32-bit C passes 4,096 cases under each of `-O0`, `-O2`, and `-O3`, for
12,288 positive executions. Fourteen controls are rejected, covering record
kind/size, owner pointer and identity, XYZ routing, class bytes, enabled byte,
active/state, classifier output, release behavior, and successful tail clear.
Injected memory failures produce 122 observations across 39 unique active
boundaries.

The retail image contains seven direct `jal` callers at ROM offsets `0x9A268`,
`0x9A2EC`, `0xA08A4`, `0x17AE64`, `0x17AF14`, `0x17AF80`, and `0x17AFDC`, and
no aligned pointer literal. The focused installed suite passes all four tests
in 31.701 seconds. The shared match-progress, generated-PC16, guarded-object,
and protected-data suite passes all 19 tests in 6.223 seconds.

## Image and production closure

The strict whole-image comparison covers all 6,052 linked functions, changes
only `func_15158BD0`, keeps every function address fixed, and uses zero
exclusions. All 189,088 protected Game-data bytes across 720 owners remain
exact, with SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

The independently predicted qualified owner and ELF equal the fresh
production artifacts. Rebuilding the shared guard registry recompiles the
complete corpus without a stale preimage. A full `make all` path produces the
binary and stops only at the expected final retail SHA-1 check. The inherited
duplicate `generated_12D630` recipe warning is unchanged.

| Artifact | SHA-256 |
| --- | --- |
| Qualified / production owner object | `5e909a5670fb916808728bc4f2283121dfe8aa5ba8ddb74a3ef2ca0e6924a447` |
| Predecessor linked ELF | `f47123d56f10403eb92105e7ba6107ba81bb24dab4ce2e323d84cecd8185df92` |
| Qualified / production linked ELF | `a2d33316086de8de82d5ff347c247042f2a22513323ab052c828a9e711faae37` |
| Production rebuilt ROM image | `d526c5b596ed1b80f71a9006c3952cdad961a2855843efc5f6deb9ffa4a13483` |
| Production map | `2ab021cc02cab424a5dae0e96a4ed5df1fe5f65ea58964f8e4e04b689771fbeb` |

## Recount and continuation

The fresh production ELF reports:

- Total: **4,152 / 5,512 (75.33%)**, zero address drift, 1,360 different.
- Init: **492 / 492 (100.00%)**, zero drift.
- Game: **3,479 / 4,839 (71.90%)**, zero drift, 1,360 different.
- Debugger: **181 / 181 (100.00%)**, zero drift.

The converted inventory remains 5,512 / 6,046 functions. The active 80%
target is 4,410 exact functions, so **258 more** are required. Rerank the
ordinary Game queue from this production ELF. Keep the seven documented
custom-ABI/compiler-boundary cases (`func_150A76F0`, `func_151F8870`,
`func_150A613C`, `func_150AE280`, `func_15115F68`, `func_151AE2BC`, and
`func_150A6760`) separate until their specific boundaries are addressed.

## Graph retention

The retained graph baseline is 58,561 nodes / 112,408 links / 5,117
communities with SHA-256
`a29b3143d78eb37c2318c18ca17e3cf06f6f018ec648e3dc750a5afd47575b2e`.

The standard reduced `graphify update .` extracted nine uncached inputs but
proposed only 24,769 nodes, so Graphify correctly refused to overwrite the
retained corpus. Its fail-closed report retained 31,816 nodes from 3,754
still-present files outside the reduced scan.

An explicit nine-path incremental rebuild with `force=False` then produced
58,571 nodes, 112,343 links, and 5,093 communities. It retained 58,558 /
58,561 prior node IDs and removed no ID outside the changed-path set. The
three replaced IDs are line-derived `DOCS/UPDATE_LOG.md` nodes; thirteen IDs
were added for their relocated forms, the nine new Note 2081 nodes, and the
new typed record node. The qualified graph SHA-256 is
`2cd2ab45fc652706bf61c403a3a5e7e3d91ae0aef39066bb1b9728b5cc3a27b3`.

After adding this receipt, a one-path stabilization detected no topology
change and left every qualified node and link untouched. The final graph is
58,571 nodes, 112,343 links, and 5,093 communities with SHA-256
`2cd2ab45fc652706bf61c403a3a5e7e3d91ae0aef39066bb1b9728b5cc3a27b3`.
