# Actor Handle Resource Retirement Byte Match

Date: 2026-10-18. Consumer predecessor **3a26c903**, tools predecessor
**e3717247**. This turn completes paired **func_15101090**, owner
`generated_12DAB0`, VA **0x15101090..0x15101148**, ROM
**0x12E540..0x12E5F8**. The wider Game matching goal remains active.

## Installed Recovery

Replace the false s32/no-argument return-zero placeholder with typed,
commented **void handle-first actor/resource retirement C**. All
**46 words / 184 bytes / frame0x20** match after three guarded scheduling
words. Raw C remains three differences; this is not a raw/direct match.
The first normal O2/g3/MIPS2/o32 source already reaches the correct extent,
frame and three-difference window. No compiler override or broad conversion
batch is installed.

The routine reads actor **+0x1A0 as u16**, calls **func_100111C8** only when
nonzero, then visits non-null object pointers in order **+0x138, +0x13C,
+0x134, +0x140, +0x144** through **func_1516972C**. Finally it calls
**func_1513CA6C** on the original actor. Unlike the previous destruction
callback, these providers retire objects rather than immediately free them.
Future fields are reloaded after callbacks, including the initial handle
callback; no pre-caching is introduced.

The local `ActorResourceOwner101090` view embeds the existing five-pointer
resource block at +0x110 and extends through the unsigned +0x1A0 handle.
Native32 verifies the handle offset, resource offset and 0x1A4 extent; this
does not pretend the smaller base struct210 includes the handle. A volatile
owner parameter recovers retail's argument-home reloads. Names describe only
observed roles; original source spelling and gameplay identity remain unknown.

The actual Init helper body and header confirm a u16 handle, including its
low-four-bit slot lookup and full-handle comparison. Existing sibling byte-
pointer wrappers require a legacy global unprototyped void declaration of
func_1513CA6C. The local typed resource and handle declarations introduce no
new owner warnings or sibling changes. Shared callback types are not rewritten.

## Caller And Three Guards

Table **D_80089EF8[1]**, slot **0x80089EFC**, selects the callback. Actual
**func_1513CB58** dispatcher bytes are all **76 bytes retail-exact** and
preserve original actor A0 through the indirect call. Connected qualification
uses this actual N64 ABI, not a portable-C claim about the legacy void(void)
dispatcher/table declarations. The flag at actor+0x58 and index at +0x19
select the base or specialized callback; both branches are exercised.

The expected-word guards at **+0x10/+0x14/+0x20**, indices **4/5/8**, change:

- LHU +0x1A0 destination A0 to T7, preserving zero extension.
- The likely branch's tested register A0 to T7.
- The first call's NOP delay slot to OR A0,T7, preserving its handle argument.

Both zero/nonzero edges close the register mapping. Word10 overwrites A0 with
the next resource argument, and the target suffix never reads T7. No equality
of dead ABI scratch registers or undocumented provider inputs is claimed.
All **seven R_MIPS_26** calls remain fixed; there are no inserted/omitted
words or moved relocations.

## Fresh Qualification

New tools: `experiments/game_actor_resource_retirement.py` and
`tests/test_game_actor_resource_retirement.py`. Ignored artifacts:
`conker/build/game-actor-resource-retirement/`. Seventeen inputs pin source,
ELF, guards, retail assembly/ROM, helpers, types, callback data, build/symbol
inputs and all four prepared compiler components. Old helpers/hashes and
prior fixtures remain unchanged; exact three-member historical readers reject
unknown/mixed states, nesting and input corruption without rewriting disk.

All **seven pre-install tests pass in 25.382s** and all **seven installed
tests pass in 26.835s**:

```sh
python3 -m unittest tools.tests.test_game_actor_resource_retirement -v
```

Fresh coverage includes **5,120 paired guest cases**, all 32 presence masks,
handles **0/1/0x7FFF/0x8000/0xFFFF**, four callback mutation modes, repeated
pointer aliases, low/high pointer values and both stack phases. Bytes +0x1A2
and +0x1A3 are separately poisoned. Opaque providers poison caller-saved
state. A harness-only mutation-mode name collision was corrected before
these passing receipts; production source was not changed to satisfy it.

Native32 **O2 and O0 with UBSan** each pass **1,280 cases**. All seven
wrong signed-handle/offset/omitted-call/order/cached-field/owner/immediate-free
controls fail observably in native and compiled guest execution. Native flat
views use `-fno-strict-aliasing`; this is not general ISO-C alias proof.

All **4,488 target-memory fault prefixes across 256 states** preserve calls,
memory and access events. Forty-six guard-window mutations, 46 raw object-word
mutations, all seven call-binding mutations, all 34 live/frozen input mutations
and nested historical views are rejected. **256 real dispatcher sequences**
preserve owner arguments. Provider/hardware faults, real object retirement and
complete gameplay are not claimed by these bounded models.

## First Prediction And Real Link

A disposable complete link, prepared before production edits, substitutes only
the qualified owner in a copied current linker script. The actual owner/ELF/
progress build reproduces that entire **3,257,636-byte** prediction exactly:
**141 changed bytes = 140 target-code bytes + one target symbol-size byte**.
The target st_size changes **12 -> 184**; no metadata exclusions are used.

The manifest timestamp initially triggered a broad dependency rebuild, stopped
on its uniquely identified owned make process. The remaining build uses the
existing manifest-old optimization and explicitly compiles the affected owner:

```sh
make -C conker -o retail_word_patches.us.csv -j4 \
    build/src/game/generated_12DAB0.c.o build/conker.us.elf progress.csv
make -C conker -o retail_word_patches.us.csv match-progress NON_MATCHING=1
```

All **6,057** function bodies/addresses are compared; only the target body
changes. Canonical symbol definitions differ only in its expected extent.
All **22 raw neighbors**, owner pools and relative relocations are fixed,
including the newly matched paired destruction callback. Actual production
padded owner bytes and seven call bindings equal the qualified object.
Game data stays **189,088 bytes / 720 owners / zero differences** and callback
slot 0x80089EFC stays 0x15101090. The complete guard prefix, including its
299 legacy CRLF lines, remains byte-identical; only three rows append.

| Prepared Artifact | SHA-256 |
| --- | --- |
| Complete installed ELF | `9f79786e248e2384422e8237865a30273a7ae17f1d3690cc9a4c87f1d46543c4` |
| Complete owner source | `ed80609aab48edc56a76802f3bd4d7b535f06da6b11480ae9e6e62cfb1ef2214` |
| Guard manifest | `625033dd1c2150ce2edb45badf13c05d09aa95b83a0c2b1231e092105d3fc2b3` |
| Raw target object | `da4af84c00105525c73151096368ed9f5f18a7a531c0d82bffb8bb2fc814a003` |

## Bank And Next Action

Tools **29952ff** is committed first. Both tools copies pass eleven shared
padder tests and project-tools smoke checks, plus four Windows ASCII/AST
parses and two exact task-file comparisons. Preserve older mirror HEAD
**ddbdd16**, all **1,188** initial dirty hashes, and its history; add only
two absent paths for **1,190** dirty paths. No mirror commit/reset, push,
Claude call or host/frozen Release edit/build/launch occurs.

Scoped graph refresh completes at **42,398 nodes / 82,502 links / 4,065
communities**, retaining all **19,398 excluded nodes / 2,972 files**. All old
node IDs remain except three shifted Update Log heading IDs with equivalent
labels retained. The recovered callback resolves to source line32 and this
note has seven graph nodes. No purge or full extraction is performed.

Fresh official totals: **Game 2,969/4,828 (61.50%)**, total
**3,642/5,501 (66.21%)**, **1,859 different**, zero drift. Conversion
counts/bytes are unchanged. Root README changes only its two matching rows;
recovery narratives stay here and in short documentation indexes. Unchanged
neighbor-suite receipts are reused, not represented as freshly rerun suites.

Fresh queue selects ordinary **func_151102CC**, owner `generated_13D350`, VA
**0x151102CC..0x15110360**, ROM **0x13D77C..0x13D810**, **37 words/frame0x68**.
Its empty body already has the matrix-and-three-floats signature recovered in
[Note382](382-game-indexed-matrix-compose-match-20260928.md). Retail calls
func_150A8050(output,0,arg2,0), builds temporary rotations for arg1 and arg3,
and composes each through func_150A7A48(output,temp,output). Read the actual
rotation helper and its matrix convention before naming axes; preserve the
already exact func_15110360 wrapper, float ABI, local 4x4 matrix and neighbors.
The handwritten func_150A76F0, both fade gaps, other gate, additional-source,
caller and inherited-stack work remain separate and open.
