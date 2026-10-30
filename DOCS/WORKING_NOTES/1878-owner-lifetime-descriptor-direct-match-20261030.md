# Note 1878: owner lifetime descriptor direct C match

2026-10-30. `func_151AE7B0`, owner `generated_1D92F0`, replaces its zero-return
placeholder with `void *func_151AE7B0(u8 *owner, f32 scale, s16 duration,
u8 selector, s32 category)`. VA `0x151AE7B0..0x151AE890`, ROM
`0x1DBC60..0x1DBD40`: all **56 words /224 bytes** and four relocation bindings
match directly from semantic C. No guards, insertions, omissions, alignment
tail or compiler profile changes are needed. Tools commit: `9452b6022b51f545598992be96300b9e59c661a3`.

## Behavior, packet and argument lifetime

A null owner returns NULL. Otherwise the function calls
`func_1516962C(40,owner,17)` before reading the owner's identity byte at+0x3B,
global `D_800A9D80`, and the incoming scale used in its48-byte attached-effect
descriptor. The packet contains zero prefix words and vector, owner identity
and pointer, attachment1, the global value and scale. Zero duration selects
300 with flags2; any nonzero signed halfword supplies the duration with flags6.
Kind6, callback-1 and mode5 complete the packet. The function returns
`func_1513418C(&descriptor,0,selector,category)`.

The80-byte frame saves RA at SP+20 and holds the descriptor at SP+28. Incoming
owner/scale/duration/selector homes are SP+80/84/88/92; the fifth word is SP+96.
The original signed-halfword and unsigned-byte reads are at SP+90 and SP+95.
There are no saved S registers. Callback changes to saved incoming homes are
qualified in the guest only; native C tests use real allocated backing.

The existing `OwnerEffectDescriptor1D92F0` type and notification/constructor
declarations are moved before this new routine so both it and the already
banked `func_151AF270` share the same declarations. Only the new float extern
is added. Other function bodies, shared headers and caller source remain fixed.
All padding bytes in the local descriptor retain their original representation;
there is no blanket zero initializer or invented field meaning.

The first semantic source already emits all56 words, including every frame,
argument-home and packet offset. Returning the constructor call directly gives
the same object. Replacing the explicit lifetime branch with a conditional
assignment emits57 words with23 positional differences and is rejected.

Raw C and original unresolved assembly SHA-256:
`6b567d46838f59df37ef9be033469a24b4ddbeaa6c180f3dd9e7542eaefa4767`.
Recovered owner source SHA-256:
`9d4214189faac5c4e8788e0311a3ac4d81986a2b150e0095ddee1fb02829dd0d`.
Padded owner SHA-256:
`aab9e0f96cd6add2dd7d678abcca1865b18bef196cdb3ca0d6188566dc7ea418`.

## Qualification and boundaries

Ignored evidence: `conker/build/game-owner-duration-descriptor-151AE7B0-match/`.
Both tools copies pass eight fresh canonical checks and shared tool checks.
Production repeats two installed checks per copy; six unchanged semantic
checks are reused only through exact input/module/artifact fingerprints.

- Guest:2,568 cases /7,704 executions, all56 words, all unsigned byte lanes,
  signed duration boundaries and ignored upper argument bits, null owners,
  constructor success/failure and notification mutations. All48 packet bytes,
  including eight untouched padding bytes, are checked. Full modeled final
  registers, RAM, calls and access traces agree across retail/raw/padded code.
- Prefixes:66 access cuts include eight delay-slot cuts. Actual PC/delay state
  and complete modeled state agree. These check emitted instruction order,
  not portable C fault behavior or arbitrary native stack aliasing.
- Rebases:144 cases across three independent GNU-linked entry/global/helper
  layouts, including signed low-half carry boundaries, preserve all bindings.
- Native32:67,584 cases per O0/O2/O3 profile with trapping UBSan, typed mixed
  pointer/float/halfword/byte/fifth-word ABI, real allocated objects and canaries.
  Every one of the65,536 duration representations reaches the non-null lifetime
  path;2,048 additional cases cover null owners and notification/outcome modes.
  Eighteen compiled semantic controls are effective. Indeterminate padding is
  omitted from native comparisons and checked in the guest instead.
- Eighteen separately IDO-compiled controls reject wrong notification, identity,
  attachment, zero prefix/vector, constant/scale, signed duration predicate,
  default duration/flags, override flags, kind/callback/mode, selector/category,
  returned pointer and premature constant capture. Failures are actual semantic
  mismatches; compilation or oracle errors are not accepted as witnesses.
- Caller:one aligned direct JAL at ROM `0x1C1908`, zero aligned literal pointers.
  Sixty-four cases execute the original eight-word window at
  `0x15194440..0x15194460` in `func_15194408`. It passes scale bits0x3F19999A,
  duration90, selector255 and category1, and ignores the return. The rest of
  the parent remains bounded; its complete execution is not claimed.
- Connected providers:384 cases execute the original/current15-word notify
  wrapper,76-word constructor and11-word memcpy. All102 loaded words are
  byte-exact in the current ELF; coverage is15/74/11. The two unvisited words
  are `0x15134234` and `0x15134284`. Allocation, dispatch, deletion and matrix
  transformation are bounded services. This is not a gameplay/hardware claim.
- Owner/Make:all32 neighbors and pools remain fixed. The actual five-command
  recipe, including assembly post-processing, reproduces the complete padded
  owner. Target/owner/command diagnostics are empty. The existing duplicate
  `generated_12D630` Make recipe warnings remain in the dry-run plan.
- Fingerprints reject224 one-byte corruptions and five size/binding/scope
  controls. The equivalent conditional-duration source is rejected by the
  exact payload/frame contract. Whole-image comparison has zero exclusions.

The original native sweep paired some duration values with null owners.
Its receipts and old oracle are retained under `canonical-attempt-v13/`.
The strengthened sweep forces every duration through a non-null call, keeps
the separate null cases, and passes fresh qualification in both tools copies.
This changes test coverage only; selected C and its exact object stay fixed.
Earlier failed fixture receipts are also retained: an overbroad text replacement
changed a length assertion, the initial owner driver assumed three rather than
five Make commands, and an unused native helper tripped -Werror. These were
corrected in fresh drivers without relaxing compilation or matching gates.
Routine work used zero Claude/REA calls and no dependency/account changes.

## Image, measured progress and banking

Production equals the independent complete ELF prediction:
**168 changed bytes =167 target-code bytes +one extent byte**, metadata0,
with zero exclusions. All6,055 other linked bodies, all6,056 addresses and
189,088 Game-data bytes across720 owners remain fixed. The inventory CSV,
linker script, map and complete inherited guard manifest remain unchanged.
All17,038 current sealed inputs are verified under declared changes. The older
tools mirror retains its2,072 inherited changed paths plus the three new modules;
that mirror is not committed.

Adopted ELF SHA-256:
`c3891dca9d33bc176ac88b07f416aa043b32712995e2c59d506f8a6ca44ba2fe`.
Actual Native ELF recount: **3,955/5,506 (71.83%)**, Game
**3,282/4,833 (67.91%)**, Init492/492 and Debugger181/181, zero drift.
The75% threshold remains4,130/5,506, requiring **175** further exact functions.

Tools are committed before the consumer source/docs/pin commit. Root README
changes only its two aggregate rows. Graphify refreshes the eleven changed
source/tools/docs files, retaining old nodes and valid relationships and
retiring obsolete placeholder s32 return edges using the actual pointer-return
declaration. No full-corpus extraction, global clustering or centrality claim
is made. Private and parked candidates remain uncredited.

Next private screen: `func_1510F720`. The wider matching goal remains active. No push
or pause.
