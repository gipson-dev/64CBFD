# 1865: Randomized position packet restored from C

Verified 2026-10-30. `func_150B6000` replaces its zero-return placeholder in
[`generated_E2DA0.c`](../../conker/src/game/generated_E2DA0.c). All 56 body/slot
words emit directly from semantic C with three original JAL relocations,
the original 80-byte frame and no padding. No guards, inserted/omitted words,
profile/Makefile/layout/shared-header changes or guard-manifest edits are needed.

Actual linked recount: **3,942/5,506 (71.59%)** total,
**3,269/4,833 (67.64%)** Game, Init 492/492, Debugger 181/181 and zero drift.
The 75% goal remains active: **188** more to 4,130/5,506. The C inventory and
progress CSV remain unchanged.

## Recovered behavior and source reuse

The routine initializes a `Header` with 3/-1, obtains an unsigned RNG remainder
modulo 9 plus 3 for its halfword field, and clears the following byte. After that
first RNG call it reads the live float position and truncates all three axes
to signed32 in a `Header2`. The second RNG supplies an unsigned remainder
modulo 201 plus 55. The typed constructor receives eleven arguments:
`(&header,&coordinates,value,255,255,255,255,0,0,kind,mode)`.

The kind is an unsigned byte and mode is a full32-bit payload. Both reload from
their incoming homes after RNG2. Mutating a disjoint input position during RNG1
affects the coordinates; mutating it during RNG2 does not alter the staged
coordinates. Guest aliases qualify the physical access order separately.

The existing qualified `func_151C56A4` provided a matching semantic template
and reusable packet/native oracles. Changing its target symbol, two RNG
expressions and constant constructor arguments recovered this complete56-word
routine on the first source screen. That is reuse of already qualified decomp
C, not adoption of the alternate donor's incorrect integer coordinate reads.

Only this owner's include list adds the existing `structs.h`; the shared header
is unchanged. The constructor prototype matches `game_18D770.c`. The frame
savesRA at SP52, coordinates occupy SP60..72 and Header occupies SP72..78. Only
five Header bytes are initialized; native tests do not claim a value for pad5.
Incoming homes are SP80/84/88, with the kind byte read at SP87. The seven stacked
constructor arguments occupy SP16..40, for a 44-byte outgoing argument area.

## Qualification

Ignored artifacts are in `conker/build/game-random-position-packet-match/`.

- Compiler/owner: all56 raw words and three relocations match original assembly.
  Eleven raw/padded neighbors and all pools are unchanged. Selected, owner and
  actual-Make compiler diagnostics are empty. Three actual Make commands
  reproduce the qualified padded object exactly.
- Guest: 329 cases / 987 executions cover all56 words and every pair of 13 RNG
  boundary values, including 8/9/10, 200/201/202 and signed-high-bit values.
  Independent ABI/position axes cover tag widths, full modes, float boundaries
  and mutation timing. There are 75 interrupted-access prefixes, 192 cases in
  three rebased layouts and 22 private-home/alias cases. Original, raw and
  padded programs agree on full registers, memory, access traces, calls and
  observed packet fields. All 11 constructor arguments are checked.
- Callers: original ROM has exactly two direct JALs, at 0xE30D0 and 0xE32CC,
  and no function-pointer words. Four-word windows at 0x150B5C18 and 0x150B5E14
  each execute 64 cases per program. They forward the pointer, byte kind and
  full mode in the original delay-slot order. The constructor's V0 is preserved;
  neither immediate caller inspects it before its epilogue. The C interface
  is void, consistent with the recovered effect wrapper; architectural return
  bits are preserved by exact emitted instructions. Complete parents are not
  claimed by these bounded windows.
- Native32: 132 finite/in-range cases each at O0/O2/O3 pass UBSan and nine
  effective controls. All initialized packet fields, coordinates, 11 arguments,
  two RNG draws, mutation timing and final position bytes are checked. Nonfinite
  and out-of-range casts are guest-only under the explicit nontrapping model;
  private argument-home aliases are not portable C claims.
- Full image: production ELF equals the independent full-file prediction,
  SHA-256 `6ecbadc6f3e717f2b5bc93d80af77e51e264bce346ec47fc8bbdb8bd69801ba3`.
  Exactly 160 bytes change: 159 target-code bytes and one symbol-size byte.
  Metadata reorderings 0, exclusions 0. All 6,055 other disassembled bodies,
  every function address, and 189,088 protected Game bytes / 720 owners are fixed.
- Both tools copies pass eight fresh checks and their project-tools check.
  After production, two fresh installed checks run per copy; six unchanged
  semantic checks are explicitly reused through identical module/input/artifact
  fingerprints. The 16,947-file seal verifies unchanged source and objects.

The RNG and constructor use bounded effect models with caller-saved clobbers.
Original helper instruction execution, complete parents, hardware FCSR traps
or NaN-payload behavior, and host-port/gameplay acceptance are not claimed.

## Banking and continuation

Tools are committed first at **029734240a1c1cd66d4c328f44339c2ca20442c6**, then the consumer pins that exact
commit. No push is performed. Older tools-mirror edits stay preserved.
The root README changes only its two aggregate exactness rows. Detailed updates
remain here and in the documentation indexes. Graphify receives a scoped
structural refresh with source-validated helper/caller edges and explicit
old-node/relationship retention; full-corpus re-extraction is not claimed.

Next screen **func_150E67D0** from the actual live ELF queue. Previously deferred
candidates remain private and uncredited until all qualification gates pass.
