# 2632 - Particle emission accumulator direct byte match

Date: 2026-11-22. The total 85% matching goal remains active.

`func_150EC520` replaces its zero-return placeholder with complete semantic C.
All **100 words / 400 bytes emit directly**, frame128, **zero guards**, inserted
or omitted words and no padding. Production is **4,614 / 5,528 (83.47%) total**,
**3,941 / 4,855 (81.17%) Game**, zero drift,914different. Init492/492 and
Debugger181/181 remain exact. **85 more matches** reach85%. Conversion rows
are unchanged. Source is `conker/src/game/generated_1199D0.c`; original
`conker/asm/1199D0.s:11`, VA150EC520..150EC6B0, ROM1199D0..119B60.
Raw SHA256 `6219eb7583bc6635cd448ee164da8ef4a1e67c457b6b8df87d9aa1ca5b6f636b`.

## Source, interfaces and loop behavior

The entry uses the actual SDK struct260 common-header pointer supplied by
the dispatcher. The enclosing56-byte record has its emitter payload at28:
source pointer, rate float, gate pointer and accumulator float. Scratch is
20 bytes: top atSP68, then packet{x,y,z,parameter} atSP6C/70/74/78. RA lives
atSP54, S0..S6 atSP38..50 and the saved F20 pair atSP30. No shared headers
are changed. Six other raw/padded functions, pools and diagnostics agree.

If the gate returns zero, an explicit float RNG draw precedes the late loads
of the base/spread globals, rate and runtime timestep. The update is
accumulator += (base + draw*spread)*rate*timestep. Emission starts and repeats
strictly while accumulator>1.0f. Packet.parameter initializes once before
the loop. The sampler receives(source,&x,&z,&top,&y), with the fifth pointer
on the outgoing stack. A separately sequenced unsigned RNG draw supplies
lifetime%131+80. The factory receives(lifetime,-1,90,-1,1,0,16,byteC,byte1).
Successful allocation gets the16-byte packet at effect+28; null skips the
copy. The accumulator reloads after external calls and subtracts1.0f.

The owner's legacy factory declaration represented argument7 as struct37*.
Its actual semantics are an integer allocation byte count: original factory
instructions add the40-byte header size. The local declaration now uses u32
and both target and the existing ECa68 routine pass sizeof(payload), removing
its pointer-size cast. All six neighboring instruction/relocation streams
remain identical. This related local ABI cleanup changes no other owner or
shared declaration. Explicit RNG sequencing and the common-header entry also
retain all100 original words.

## Caller and connected original helpers

The98-entry D8008A4E8 table registers the target at index89/address8008A64C.
The complete original/current45-word dispatcher15149264 passes the common
record pointer, performs optional lifetime subtraction, dispatches the death
handler when needed, reloads lifetime after that handler and conditionally
releases the record. It overwrites callback V0 with the lifetime reload.
192cases per stream cover flags, positive/expired lifetimes, updates, callback
skip, death/revival/release, two stack phases and an effective missing-record
control. Death and release internals remain contracts.

5,184 connected cases per stream execute the original gate20words, float
RNG25, integer RNG18, sampler path3's50words, factory47/49words for fixed
flag1, and memcpy11words. Independent64-bit seed transitions and finite IEEE
rounding/status checks agree. The factory's actual six allocator arguments,
56-byte total allocation, signed/narrow header fields and16-byte zero region
are checked. Allocation/zero leaf internals remain contracted.

The current sampler151432BC remains a254-word placeholder. Connected sampler
tests execute only its original path3, which uses signed source coordinates
and upper/lower heights. Other sampler paths remain unqualified. The actual
base/spread literals33C221ED/33D3F4E6 and float RNG coefficient37800080 are
verified against the current ELF; the timestep is runtime state. No complete
sampler, allocator, effect-system or gameplay acceptance is claimed.

## Qualification and adoption

- Guest:1,486cases per candidate/original stream, four rounding modes,
  signed zeros, strict threshold, multiple emissions, null/success outcomes,
  escaped packet effects and mutable providers.135 access-fault comparisons
  pass.99/100 words execute; word69 is the unreachable divide-by-zero break
  after a divisor held at constant131 in a preserved register. The bounded
  finite IEEE oracle is not exhaustive VR4300 exception/denormal emulation.
- SDK32 O0/O2/O3:205cases each, exact common-header/record/scratch layouts,
  strict aliasing and UBSan, valid escaped packet casts, numeric packet values
  and call-boundary states. Uninitialized scratch fields are not read. Ten
  effective controls cover gate, threshold, rate/timestep, remainder sign,
  sampler output, packet initialization lifetime/size, effect kind and an
  incorrectly cached source pointer.
- Both padders preserve the100-word body without padding or guards. Sixteen
  independent GNU links cover all12 relocation sites and HI16 carry edges.
  Natural existing O2/g3 Make uses three commands. Complete independent ELF
  prediction has **302 changed bytes, zero exclusions and zero metadata
  permutations**.189,088 protected GameData bytes/720 owners, other bodies
  and addresses, old guards and conversion rows agree. ELF SHA256
  `f97755b8f20f92d20359be78de9c7b6986d96b3794bdb91efa71c061a1e9bcf3`.
- Both tools configurations pass all five checks before and after installation
  with exact Python/data hashes. Shared tools-check passes. Real sibling edits
  and dependency hashes are preserved. Existing duplicate generated_12D630
  Make warnings remain unchanged.

Baseline consumer `6f5a5764f4733f9b141c3fae9268be429942ecf2`, tools `83adf5f57576dfbcd7c73b62a2e9508118f722d1`.
Tools commit `b8f0ed451e570a757733b8d812e3f72905e4e3df` precedes the
consumer commit. No push. Available host configuration applicability is
recorded separately; its different binary mapping supplies no direct C import
or host/Release/gameplay claim. Zero Claude calls. Other owner placeholders
remain pending. Finish graph retention and immutable banking before the next
recovery, and keep the total85% goal active.

Graph maintenance: the native update exited 1 with all
70,829 prior IDs retained. The subsequent serial scoped extraction
covers 8 C/Python files with no missing AST sources, producing
70,893 nodes / 167,926 links and retaining prior qualification
metadata. This is a scoped refresh, not a full-corpus re-extraction. Actual
commit-hook producers must be terminal and their ID/metadata retention audit
must pass before the final immutable bank is accepted.
