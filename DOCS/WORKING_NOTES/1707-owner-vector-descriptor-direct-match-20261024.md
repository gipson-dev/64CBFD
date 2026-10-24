# Owner Vector Descriptor Direct C Match

Verified 2026-10-24. Recover `func_150E0348` in
[generated_10CD70.c](../../conker/src/game/generated_10CD70.c), replacing its
zero-return placeholder with a complete typed descriptor constructor.
All 44 retail words emit directly from C, without guards or profile changes.

## Layout And Contract

VA `150E0348..150E03F8`, ROM `10D7F8..10D8A8`, 176 bytes, no alignment
tail. Normal O2/g3; frame 72, seven symbolic bindings. Arguments are the
owner byte pointer, unsigned byte selector and full signed category word.
Return the pointer from `func_1513418C(&descriptor, 0, selector, category)`.

The 48-byte descriptor at SP+0x18 contains:

| Offset | Initialized Value |
| --- | --- |
| 0, 4 | zero words |
| 8 | snapshot of owner+0x3B identity byte |
| 0xC | owner pointer |
| 0x10 | attachment index zero |
| 0x14, 0x18, 0x1C | complete three-word vector preset |
| 0x20 | `D_800A0FB4`, retail bits 412E6667 |
| 0x24 | `D_800A0FB8`, retail bits 3E6CC250 |
| 0x28 | signed 16-bit duration 300 |
| 0x2A, 0x2B | flags 0x1B, kind 0x0B |
| 0x2C, 0x2D | signed callback -1, mode zero |

Leave bytes 9..11, 17..19 and 46..47 untouched. Guest checks seed and compare
all 48 bytes; native tests assert defined fields only. A compiled defined
wrong-C control that zeroes the eight unspecified bytes changes the guest
packet and is rejected. Do not invent a NULL-owner check: retail faults at
its identity read. Native tests use valid allocated owners.

The vector at `D_800A5480` is twelve zero bytes in protected initialized
Game data. Use a bounded local three-float declaration and aggregate copy,
not a fabricated zero literal or changes to shared scalar declarations.
Read the identity before publishing the owner pointer. Reversing those
assignments keeps 44 words but changes seven; three scalar vector assignments
emit 43 words with 41 differences. Neither rejected shape is installed.

## Caller And Constructor

[generated_97AA0.c](../../conker/src/game/generated_97AA0.c) now explicitly
declares the pointer/byte/word ABI. Its `func_1506A6FC` has a typed owner and
explicit pointer return, forwarding selector 255 and category one while
preserving the unused second word argument. The complete ten-word/frame-24
wrapper, all sixteen caller-owner functions and its complete padded object
remain byte-identical. It was already exact and earns no additional credit.

An aligned full-ROM scan finds the sole direct JAL at ROM `97BBC` and no
literal target registrations. Execute the complete original wrapper with
both original and recovered target bodies in twelve cases, including
NULL/full-word return values and provider mutations. This is not a claim
about every possible computed call.

Connect the unchanged original 76-word `func_1513418C` and eleven-word SDK
memcpy in 96 cases. Verify their words against the predecessor ELF. Exercise
allocation failure, owner first-word/identity rejection and deletion,
matrix/type gates, copied bytes and finite float32 reciprocal outputs.
Visit all 74 reachable constructor words and every memcpy word.
`15134234` is an unreachable duplicate load; `15134284` belongs to the
unselected flag-2-false arm. Both words remain present and exact.
Only allocator, delete and matrix-transform providers are bounded; the
observed transform A3 is the record pointer, not an inferred formal API.
Full matrix arithmetic, general FCSR and hardware behavior are not qualified.
The constructor's existing C placeholder and assembly remain untouched and
uncredited.

## Qualification

[Experiment](../../tools/experiments/game_owner_vector_descriptor.py) and
[focused tests](../../tools/tests/test_game_owner_vector_descriptor.py)
reuse the existing compiler/padder, object/pool parsers, descriptor oracle
and native32 helpers. Both copies pass eight fresh pre-install and eight
fresh installed tests, with no failures, errors, skips or reused checks.
Both shared project checks pass.

- 584 guest packet cases cover every selector and identity byte, full-word
  categories/results, both stack phases, provider mutation, private owner
  aliases and independently linked vector-preset aliases.
- Native O0/O2/O3 trap UBSan executes the actual recovered target and typed
  wrapper: 3,072 cases per profile, fourteen effective defined wrong-C
  controls, correct explicit returns and owner/record canaries.
- 81 fired root-access prefix pairs preserve emitted guest order and the
  actual NULL-owner fault; this is not portable C fault semantics.
- Six independent GNU links over three layouts include negative LO16 and
  HI16 carry boundaries. Original and recovered code relocate identically.
- Independently assemble original code and compare isolated/complete-owner
  raw C, bindings, pools, twelve neighbors and actual padded objects.
  Execute the real three-command target and five-command mixed caller
  Make recipes. All thirteen/sixteen compact functions and both complete
  padded objects agree. Isolated diagnostics are empty; owner diagnostics
  are unchanged. Inherited duplicate generated_12D630 Make warnings remain.
- Fourteen strict-image corruption controls reject changed code, metadata
  and unrelated bytes. No whole symbol/string table is excluded.

Raw body SHA256:
`6db8fd1ce12c6007b402799c69d6fbe2488c27ee2f1b3c27d484e2e527948596`.
Retail body SHA256:
`af41e78539ddde66a66ca00e85ed1ecaec3ba1b969ff350e4b04a00f0642ef1d`.

Routine work uses zero Claude calls. Prior unrelated neighbor suites are
not described as freshly run; their unchanged code/input basis is covered
by the linked image and sealed closure audits. No gameplay claim.

## Production And Progress

Tools `5a4132f249ebd1988088aaf298448d20d64e7240` committed first.
Preserve all 1,626 older mirror dirty paths, statuses, hashes and its HEAD;
add only the two owned modules, now 1,628 dirty paths. No push or host changes.

Seal 15,998 files, 34 focused inputs and all 1,454 linker objects in native
and Linux-cache copies, with checked stdin/tar transfer and no DrvFS project
reads. Production Make and fresh installed checks pass. Adopt only the two
C sources, target object and ELF as four qualified overrides. Caller object,
linker script, progress CSV and every guard-file byte remain unchanged.
All other 6,054 function bodies and all 6,055 addresses remain fixed.

Strict full-image delta is exactly 201 bytes: 136 target-code bytes plus 65
metadata bytes, zero exclusions. Metadata includes the target size change
12 to 176 and two closed symbol/string serialization cycles. The old
`(D_800A0FB4, D_80090AD0, D_800A2D90)` order becomes
`(D_80090AD0, D_800A2D90, D_800A0FB4)`; `D_800A0FB8` and
`func_1515F10C` exchange order. Predict all records, strings and adjusted
name offsets, including the unequal 11/14-byte names. Every named definition
is identical except the intended target size. No metadata normalization.

All 720 protected Game-data owners / 189,088 bytes remain exact:
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.
Adopted ELF SHA256:
`e828f0d65cc68d8ead6eea5c36cd2dfa2f4427ad8401bf5284b26998b93ee9b3`.

Fresh recount of actual adopted native ELF bytes: total **3,784/5,505
(68.74%)**, Game **3,111/4,832 (64.38%)**, Init 492/492, Debugger 181/181,
zero drift, 1,721 different. The 75% threshold remains 4,129, requiring
**345 more** exact functions. Goal remains open. The remaining source-shape
screen has 1,592 placeholders, 120 semantic/other definitions and nine
parser misses; it is not ABI or C qualification.

Next audit `func_150F887C` from the freshly ELF-pinned screen; private candidates
remain unqualified and uncredited. Keep existing `func_15014094` semantic-C
matching separate, and retain the `func_1510D8C0` parser-miss caveat.
Keep larger `func_1509E730`, `func_1508CAD8` and `func_15169070` separate.
Refresh the normal incremental graph after the consumer commit and
explicitly audit old-node retention; do not claim full-corpus extraction
or old-edge preservation.
