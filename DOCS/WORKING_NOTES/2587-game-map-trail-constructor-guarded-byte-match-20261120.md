# Note 2587: Map-trail constructor guarded byte match

Date: 2026-11-20. Consumer baseline `55be84c6eba2bc94789a01e03598abf72a5fa4c9`;
tools baseline `33ab2994f7a601239c0db9dcd689a9cbcea6ee32`.
Qualified tools commit: `a446347798ad2f0a8a5a2803b22afa010fccba9b`.

`func_15105CE0` is restored from GLOBAL_ASM to complete semantic C and matches
all **235 words / 940 bytes**, with its original **216-byte frame**. Raw C emits
233 words. **126 checked word/binding rows** restore count arithmetic, saved
roles, scratch roles and independent descriptor scheduling. Two instructions
are added: the live cached-count transfer and the original FP pipeline NOP.
No source instruction is omitted; no replacement retail-word array is used.
This completes the private recovery in [Note 2586](2586-game-map-trail-constructor-private-recovery-20261120.md).

Fresh production recount: **4,573 / 5,524 (82.78%)** total, **3,900 / 4,851 (80.40%)** Game, zero address drift and 951 different. Init 492/492 and Debugger 181/181 remain exact. Converted C: **5,524 / 6,048 (91.34%)**, 86.47% of bytes; Game **4,851 / 5,327 (91.06%)**, 85.87% of bytes. The 85% goal remains active: **123 more matches** at this denominator, which additional ASM conversions can increase.

## Packet interface and recovered behavior

Owner: `conker/src/game/generated_133190.c`; VA 0x15105CE0..0x1510608C,
ROM 0x133190..0x13353C. The original assembly remains unchanged.
The four arguments are the shared 80-byte packet pointer, extra allocation
bytes, priority narrowed to u8, and an s32 context. The result is an allocated
trail record or NULL. The complete C body copies the packet, initializes its
curve/sample state and creates two endpoint effects at points 0 then 3.

The allocation size is `0x88 + count*52 + (count+2)*12 + extraBytes`. The
initial count is retained for the end-of-storage pointer across the packet
copy. Input count is reloaded for `1.0f/(count+1)`; the random provider runs
before signed halfword duration bounds are read. Duration uses the unsigned
remainder and a halfword store. After both builder calls, the record's count
is reloaded for the segment-byte field. Each child gets a complete 112-byte
descriptor at SP+0x58; only its position and random flags are refreshed between
calls, preserving any edits made through the first passed pointer.

`conker/include/game/map_trail.h` now provides the common `MapTrailPoint` and
`MapTrailPacket` definitions plus the typed constructor declaration. Both
the constructor and the real `func_15104C44` emitter include it. The emitter
uses points[0..3] in place of its four former local point members; all offsets
remain 0x04/0x10/0x1C/0x28. Its local packet and point names alias the shared
types. This avoids incompatible packet structures across C translation units.
Two explicit Make prerequisites keep these owners dependent on the new header.
The existing broad SDK/variables/functions headers are unchanged.

The complete emitter owner retains **all 11 raw functions and pools**, and its
entire padded object remains byte-identical. The target owner retains its
**other 36 raw functions and pools**; its complete padded object is likewise
identical to the predecessor. Actual Make executes five commands for the mixed
constructor owner and three for the plain-C emitter owner. Both preserve the
existing O2/g3 profile and existing warnings. No compiler was changed.

## Arithmetic and instruction derivation

Natural initialization-order/type screens found a 235-word candidate, but it
changed constant sharing and multiple saved roles. That form was not adopted.
The selected, already tested 233-word body retains the original frame and all
passed homes. Its compiler reassociates `(count+2)*12` as `count*12+24` and
keeps count/point bytes in the opposite saved registers. The checked derivation
undoes that reassociation, restores the count's allocator-delay transfer,
closes the scratch register cycle through the duration update and relocates
descriptor setup/address materialization. It adds the original FP NOP.

The derivation consumes the fingerprinted source words and relocations,
performs explicit register/arithmetic changes and a closed instruction
permutation, and remaps branches and bindings. Every source origin occurs
exactly once; inserted output indices are 36 and 176. It does not read the ROM
or original body to generate its output. Independent assembly and GNU links
then verify the derived words and relocation behavior against the original.

An independent instruction-driven proof covers **all 17 finite paths** of
the two-iteration routine and **232/233 raw plus 234/235 retail words**. The
unreached instruction is the zero-divisor BREAK, excluded from the ordinary
nonzero-divisor C contract. Affine arithmetic proves the reassociation modulo
32 bits. Full 240-byte private frames, both complete 112-byte descriptors,
callee-saved registers, public writes, ABI calls, floating operations and FCSR
transitions agree. Quiet-epoch reads are stable; any public write or call
advances the epoch. Providers may change public memory and retained descriptor
bytes arbitrarily while preserving o32 saved registers. They cannot inspect
implementation PCs or unpassed locals. This is normal-execution equivalence,
not a raw fault-register, timing, hardware or gameplay acceptance claim.

Fourteen effective proof controls reject frame/return-home changes, priority
width, allocation kind, count arithmetic, copy length, signed duration,
timer destination, lifetime, endpoint, random flag, descriptor home, loop
bound and saved-register restore errors.

## Guest, native and actual call paths

The bounded independent guest reference passes **512 cases per stream**,
including failures, width/sign extremes, two SP phases, provider mutations
and complete descriptor bytes. Native SDK32 executes **512 cases each at
-O0/-O2/-O3**, with strict aliasing and UBSan; all pass. Eight effective native
source controls reject semantic errors. Native checks exclude descriptor
padding offsets 0x67/0x6A/0x6B; the guest/proof checks retain those physical bytes.

A further **96 connected cases** execute the original allocator wrapper,
list registration, byte copy, applicable bzero path, 64-bit PRNG and child
factory paths. PRNG updates and returns are independently checked against
the 64-bit seed equation. The executed word coverage is 28/28 for the allocator,
20/20 for list registration, 11/11 for memcpy, 18/18 for the PRNG, 22/40 for
bzero's called path and 38/61 for the child factory's NULL-owner path. The heap,
curve builder and sample builder remain bounded services; these results do
not claim complete provider or gameplay emulation.

All four real call-setup/return-use windows execute in **32 connected cases**,
covering NULL and non-NULL returns, two SP phases and valid list rows. They
check extra sizes 0/4/12/24, full return-pointer stores/uses, preserved ABI state
and the extra-data pointer. These are explicitly windows in func_15104C44,
func_151072BC, func_15107700 and func_15107C1C, not complete parent executions.
The original-ROM census still has exactly four aligned direct JALs; arbitrary
computed calls are not excluded by that census.

## Build, image and checkpoint gates

Nine focused tests pass in each tools configuration, with imported Python
hashes paired. The isolated sibling overlay preserves the dirty real sibling
checkout and its dependency files. It uses matching sibling files, mounted
fallbacks, the six task files and a namespace bootstrap; its exact composition
and fingerprints are retained in the ignored qualification folder.

The closed normalizer rejects all **248 source-word/binding corruptions**.
Sixteen representative stale-word/relocation controls exercise both real
padders across four guard groups. Eight independent GNU links cover four
symbol rebases, including low halves 0/0x7FFC/0x8000/0xFFFC. Four corruptions
exercise the complete-image gate, including nonloaded metadata.

Actual production Make, an independent before/after link and the production
recount pass. The **entire ELF is byte-identical** to the frozen prediction:
all **6,051 function slots/addresses**, all **189,088 protected data bytes**
and all other metadata are unchanged, with **zero exclusions**. All pre-existing
guard bytes are retained; only this function's 126 rows are appended.
One existing ASM conversion row becomes C. Frozen-input and dependency audits
cover every declared source/build change without excluding unexpected objects.
The ELF SHA-256 remains
`d428a774da73a7a019242548481f707cc7e7c6d670c233af41189771495dfb04`.

`make tools-check` passes. Tools are committed before the consumer. No push,
host/save/frozen-Release change, account action or Claude call is involved.
Root README receives aggregate rows only; this note and five concise indexes
hold the function narrative. Graphify retains prior IDs, records the installed
C definition and keeps the original ASM/private recovery as historical
references; scoped extraction is not described as a full-corpus rebuild.

Next: inspect `func_1510608C` in the same owner. Its 85-word active dispatcher
still uses original assembly; qualify its actual callback interfaces and
record-state accesses before conversion. Keep the wider 85% matching goal active.
