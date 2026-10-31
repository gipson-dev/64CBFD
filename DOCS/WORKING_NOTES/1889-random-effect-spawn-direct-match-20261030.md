# 1889 - Random effect spawn matched directly from C

Verified 2026-10-30. `func_1500F290` in
`conker/src/game/generated_3C740.c`, VA `0x1500F290..0x1500F378`,
ROM `0x3C740..0x3C828`:58 words, no alignment words.

## Recovered source and ABI

The function accepts three float coordinates in f12,f14,a2 and returns a
`struct210 *`. It stores descriptor category0x38 and a zero word before
calling `func_151EF610`, then computes its signed remainder modulo4096 plus
0x4000. It submits flags0x20014,count1,color bytes[255,255,0,0,0,255],mode0x30001,
the original three coordinates, dimensions110/110 and the recovered
fourteen-argument provider packet. Channel255 and the remaining zero fields
are preserved. Return handling includes successful and null allocations.
The explicit SDK32 descriptor cast matches the existing provider's s32 ABI.
No shared header changes.

The local descriptor has the constructor's full copied extent of40 bytes.
Its untouched padding and unused bytes remain untouched. Declaring the RNG
result after the descriptor recovers the exact compiler layout:frame112,
RA atSP+60,descriptor atSP+72,float homesSP+112/+116/+120. This ordinary
semantic local produces all58 original words and both call bindings directly.
No guards, insertions, omissions or profile changes are required.

## Qualification and limits

Artifacts: `conker/build/game-random-effect-spawn-1500F290-match/`.

- Guest:832cases /2,496executions cover all58 words and preserve complete
  registers,memory,traces and fault context for original/raw/padded streams.
  Ninety access-prefix cuts include six branch-delay cuts. Nine independently
  linked rebase cases pass.
- Connected original RNG(12words) and provider(40words) visit51/52words; the
  RNG's final duplicate nop is unreachable. The RNG contract is unsigned
  modular multiplication followed by a two-bit right shift, so its actual
  returned values are nonnegative. Negative scripted RNG results exercise
  signed-remainder behavior as explicitly bounded extension cases.
- Guest descriptor comparison preserves all40 bytes, including seeded private
  padding. Native tests read only initialized fields; portable values for
  automatic padding and untouched bytes are not claimed.
- Native SDK32/UBSan:393,728cases per O0/O2/O3 profile cover scripted RNG
  magnitudes through8191 in both signs,12float bit patterns,allocation success
  and failure,and256seed patterns. The real existing provider C executes;
  constructor/setter effects are bounded. Its pre-existing pointer/word
  conversion diagnostics are suppressed only around that existing wrapper,
  with pointer size asserted32bits. Target diagnostics remain fully enabled.
- Thirteen effective IDO and native controls reject wrong descriptor fields,
  signedness/modulus/base,coordinate order,dimensions and channel. Compiler
  and interpreter failures are not counted as semantic controls.
- Four original call windows(10,6,6,10words),384cases,cover the entire aligned
  JAL census at ROM3C908,3C928,3C940,3C958. They verify f12/f14/a2 marshalling
  and all four returned-pointer stores into D_800D98D0. Natural retail rodata
  values are included. This is bounded caller execution,not the complete
  parent or hardware/gameplay acceptance.
- Two owner neighbors and all other owner definitions/pools are preserved.
  All three actual Make commands reproduce the qualified object with no
  diagnostics. Strict independent whole-image prediction equals the real
  first link,with170 changed bytes:169target code and one target-extent byte.
  There are no metadata deltas or image exclusions. All6,055 other linked
  bodies and every function address remain fixed. Game data189,088bytes,
  across720owners,remain byte-exact. The entire guard CSV is unchanged.
- Eight fresh canonical tests and shared tools checks pass in both tools
  copies. Installed source/input/image checks are fresh; six unchanged
  semantic checks are reused only by complete immutable fingerprints.

## Banked status and continuation

Tools commit `e2fbbdfe358b62e564eb5fcf5db5462a3dcb8b92` is banked before the consumer pin. Source,docs and tools
are committed in coherent groups; the older dirty tools mirror is preserved.
The adopted ELF recount gives Total3,966/5,506(72.03%),Game3,293/4,833(68.14%),
Init492/492 and Debugger181/181,zero drift. Inventory CSV is unchanged.
The README receives only its two aggregate rows; narratives stay in docs.
Scoped Graphify retains prior nodes and valid relationships,retiring the
obsolete placeholder return edge. No full-corpus,clustering,centrality or
hardware claim; no push.

The75% goal remains active:164 more to4,130. Next private screen:`func_150626EC`.
Private candidates remain uncredited until all qualification gates pass.
