# Effect-suite dispatcher - direct C match

2026-10-31. `func_151C9DE8` in `generated_1F4650` is recovered from its zero-return
placeholder. Its 236-byte slot at VA `0x151C9DE8..0x151C9ED4`, ROM
`0x1F7298..0x1F7384`, emits all 59 retail words and ten bindings directly from C.
There are no guards, insertions, omissions, alignment or profile changes.

## Recovered interface and behavior

The signature is `void func_151C9DE8(void *owner, u8 slot, s8 kind, u8 selector,
s32 value)`. It submits six ordered calls:

1. `func_151C9F38(owner,4,slot,kind,selector)`.
2. `func_151CC524(owner,0,50,255,slot,selector)`.
3. `func_151CC840(owner,0,50,255,slot,selector)`.
4. `func_151CCF08(owner,slot & 0xFF,kind,selector & 0xFF)`.
5. `func_150BDE90(owner,selector,value)`.
6. `func_151CB5FC(owner,2,slot,kind,selector)`.

After all six calls, read the live full-word `D_800BE9F0`; when it is 0x27,
store byte 1 to `D_8008CD00`. Otherwise retain the flag as left by the helpers.
The source does not interpret any helper result or promise a target return value.

Unsigned slot and selector values are latched in S2/S1. The signed kind is read
from its incoming byte home for each use; the fifth full-word value is loaded
at its late call site. Helper-induced guest home mutations distinguish these
lifetimes. Such mutations are machine evidence, not portable pass-by-value C.

The actual helper interfaces and two explicit integer masks recover the original
allocation and redundant byte extensions naturally. The large `func_151CCF08`
still has an unfinished C stub; its definition and output are preserved, with no
helper conversion credit. A typed forward prototype would conflict with that
stub. Its retained old-style declaration plus explicit masks expresses this
caller's byte ABI while preserving all 45 neighboring bodies.

The existing O2/g3 profile emits the 48-byte frame, RA at SP+0x2C, owner/S0 at
SP+0x20, selector/S1 at SP+0x24, slot/S2 at SP+0x28, kind byte at SP+0x3B and
fifth value at SP+0x40. Full copied-owner and actual-Make evidence agree.

## Qualification

- 1,756 guest cases / 5,268 original/raw/padded executions exercise all 59 words
  and compare complete final state, memory, ordered calls and traces. All 67
  access prefixes and 15 delay-slot cuts agree. Two symbol layouts provide six
  rebases, including independent code targets and signed low-halfword globals.
- The corpus covers all low-byte kinds, upper GP garbage, signed/unsigned byte
  boundaries, full-word payloads, full-word category gates, all flag bytes,
  live globals and saved/late argument-home behavior.
- Both retail direct caller windows execute in 64 cases: ROM JALs `0x52858`
  and `0x1F718C`, sixteen original caller words total. The latter supplies
  `(owner,1,-1,255,1)`; the former loads its owner and two byte parameters, with
  slot 0 and value 1. Neither consumes a target result. This does not recover
  the full parents. The aligned ROM census finds no literal function pointers.
- All 31 words of the original `func_150BDE90` execute in 64 connected cases,
  including allocation failure and eight-byte packet copying. Its factory
  arguments are `(300,-1,79,-1,0,60,8,selector,value)`. Factory and copy remain
  explicit ABI hooks. The packet has six defined and two unwritten bytes; its
  complete guest copy is not a claim of portable C padding initialization.
  The other five suite helpers are ABI hooks, without implementation claims.
- Native32 C passes 1,474,560 scalar cases per O0/O2/O3 profile with UBSan,
  covering every signed kind byte, byte and payload boundaries, live category
  and flag changes, exact call order and complete owner-buffer preservation
  outside provider effects. All thirteen wrong variants fail in both native
  and compiled guest checks. Void results are never interpreted.
- Eight fresh canonical tests pass in each tools copy, plus both shared tools
  checks. Two installed checks per copy run fresh; six unchanged semantic checks
  are explicitly reused under complete input/module/artifact fingerprints.
- Five actual Make commands, including GLOBAL_ASM preprocessing/postprocessing,
  reproduce the qualified padded object with zero C diagnostics. All 45 owner
  neighbors and pools agree. The inherited unrelated Make recipe warning remains
  separate from compiler diagnostics.
- Strict whole-image prediction accounts for exactly 186 changed bytes: 185
  target code bytes and one target extent byte, with zero metadata changes or
  exclusions. All 6,055 other linked bodies, all 6,056 addresses, the entire guard
  manifest and 189,088 protected Game data bytes across 720 owners remain fixed.

## Banking and continuation

Tools commit: `9eaed78114be7054b63ac25eef901782bb08e03a`. Production ELF SHA-256:
`bef3d6471a49ce7dca68d8753c91430d64e32db7ec428a6603bb23f49cb3992a`.
Actual recount: **3,998/5,506 (72.61%)** total, **3,325/4,833 (68.80%)** Game;
Init remains 492/492, Debugger 181/181, and address drift is zero.
**132** more functions are needed for 75% (4,130 total).

Receipts are under ignored `conker/build/game-effect-suite-dispatch-151C9DE8-match/`.
Only the two aggregate README status rows change. The scoped graph refresh
covers the source, three tools modules and seven documents, preserving all old
valid relationships; it does not claim full-corpus extraction or reclustering.
Next queued screen: `func_15073B38`. Private candidates remain uncredited.
No push or host-port/Release changes are included.
