# Type-46 Record Updater Guarded Match - 2026-11-08

`func_150C5568` replaces a false zero-return placeholder with the complete
point-pair distance updater and rejection cleanup. Semantic C emits all
**79 words / 316 bytes with the original 0x40-byte frame**. Fourteen checked
normalization rows recover the retail instruction schedule and temporary
register roles. No words are inserted or omitted. This is a guarded C match.

Production: Total **4,273 / 5,513 (77.51%)**, Game **3,600 / 4,840 (74.38%)**,
Init **492 / 492**, Debugger **181 / 181**, zero address drift. There are
**1,240** converted functions still different and **138** more exact functions
needed for 4,411 / 5,513 and the active 80% goal. Conversion rows are unchanged.

## Recovered behavior and interface

Owner `conker/src/game/generated_F2820.c`, original `conker/asm/F2820.s`.
VA **150C5568..150C56A4**, ROM **F2A18..F2B54**. Interface:

```c
void func_150C5568(u8 *owner);
```

The source reuses the established `Type46DistanceRecord` and payload types
from the adjacent recovered constructor. The record is 0xC8 bytes: active
flags at +0x10, the first point at +0x18/+0x1C/+0x20, the second point at
+0x24/+0x28/+0x2C, selector byte at +0x30, and cached distance at +0xC0.

1. Test bit zero of the active flags. Inactive records return without reading
   the payload or calling a helper.
2. Cache the three single-precision point differences before the callback.
   Read the selector as a signed byte; **-1 skips the callback**. Otherwise
   call `D_80088760[selector](record)`. Zero status sets the removal gate;
   any nonzero status preserves its restored value.
3. If the removal gate is clear, recompute the three live differences after
   the callback. Compare them against the cached values with the original
   exact floating equality and short circuit. Any unequal axis invokes
   `func_15143E64(delta)` and stores its returned float at the live record's
   +0xC0. Translating both points equally leaves the cache untouched.
4. A set removal gate invokes `func_1516972C(record)`. The function returns
   no public value. Live reloads after helper calls preserve the original
   byte gate, incoming pointer home, and cached-vector lifetime.

`D_80088760` contains **two authentic callback entries**, 150C5B88 and
150C5BD4, followed by other data. The original has no bounds clamp; none was
added. Native valid selector cases are -1, 0 and 1. Guest extended-table
fixtures check signed indexing without claiming other default entries safe.

## Actual dispatcher and connected helpers

The sole aligned entry pointer is **D_8008B4A8[70].unk0**, stride 0x34,
VA8008C2E0 / ROM230DA0. An aligned full-ROM census finds no direct J/JAL entry
or interior references. The descriptor's declared callback takes one
`struct102 *` and returns void.

The actual caller is the **14-word VA15167164..1516719C** window of
`func_151670C0` (ROM194614..19464C). It saves the next record before calling,
passes the current record in A0, reloads the signed nesting depth and cursor,
and walks the next record through the descriptor callback. It ignores V0.
Tests cover one- and two-record chains and depths 0, 1 and 3. The parent is
still a C placeholder; only this original dispatcher window is qualified.

Connected execution uses the actual two callback bodies, the 12-word length
routine, 28-word release routine and 20-word detach routine. All five bodies
were already byte-exact in the predecessor ELF. Reachable coverage is
18/19, 37/40, 12/12, 28/28 and 20/20 words respectively; the omitted callback
words are dead duplicate loads. Release detaches older cursor references
before dispatching descriptor +0x28. The type-70 destructor is 150C5470.
Matrix transform, destructor and fallback allocation cleanup are bounded
providers; full parent execution, full cleanup and gameplay are not claimed.

## Compiler and complete image proof

The selected scalar declaration order retains the retail private stack
layout: byte gate SP+0x3B, incoming record home SP+0x40, cached XYZ at
SP+0x2C/+0x30/+0x34, and live vector at SP+0x20/+0x24/+0x28. Compiler profile
remains O2/g3/mips2/o32. The 14 guards pin the full raw 316-byte hash and four
relocation bindings. They move an independent `li AT,-1`, retarget its moved
inactive branch, preserve the public payload read order while scheduling
loads/subtracts, rename three floating temporaries, and commute three
floating-equality operands. Calls, live payload operations and stack homes
remain intact. Raw scratch registers, private fault PCs and reordered private
fault events are not equated with C public behavior; fitted bytes and full
fitted private state are checked independently against retail.

The 15-function owner preserves all **14 raw and padded neighbors**, pools,
labels and register union. Both padders agree. The actual Make path uses
three commands, emits the predicted object and has no compiler diagnostics.
Makefile, shared headers, original assembly, ROM and conversion CSV remain
unchanged. No GLOBAL_ASM restoration is used.

Strict whole-ELF prediction accounts for **280 changed bytes, zero exclusions**.
Besides the sole target body, one closed two-row metadata/name exchange
involves `D_80088760` and `func_1500707C`. Their unequal string lengths are
rebuilt with the corresponding `st_name` offsets from the predecessor; no
metadata range is copied or exempted. All 6,052 function addresses are fixed,
all other bodies are preserved, and protected data retains **720 owners /
189,088 bytes**, SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

## Validation and limits

Both tools copies pass eight fresh focused checks before installation and
eight after installation, sequentially, with identical detailed receipts:

- **1,416 guest cases per body**, visiting all 79 words, including unmapped
  inactive payload, signed selectors, callback mutations, live reloads,
  floating equality, signed zero and modeled nonfinite cases.
- **72 alias cases per body**, **988 fired fault-prefix pairs** and **108
  delay-slot cuts**. Fitted/original complete private state agrees. Guest
  private pointer and stack aliases are not portable native C claims.
- **72 dispatcher cases per body** and **288 connected-helper cases per body**,
  with record chain, cursor/depth, real callback slots and null-destructor
  type-2 coverage.
- **Nine independent GNU links across three layouts**, including HI/LO carry
  edges, and **180 cases per body** for original/raw/fitted rebases.
- Ten separately compiled incorrect implementations are detected: active
  predicate, sentinel, signed selector, cached difference direction, AND in
  place of OR, unconditional length, wrong callback status, missing release,
  missing cache store and wrong cache destination. Comparison ignores only
  physical private length-buffer pointer placement; public arguments, call
  order, vector contents, snapshots and public RAM remain observable.
- Native32 **O0/O2/O3 each pass 2,430 finite cases**, trap UBSan, typed callback
  and record-layout assertions, and full 256-byte ledger canaries. All ten
  incorrect implementations fail observably in every profile. Nonfinite
  hardware NaN payload/FCSR behavior and guest-only aliases are excluded.

The production object and ELF equal the independent prediction. The linked
recount gives the totals above. The existing whole-ROM checksum mismatch
still makes `make all` exit 2; target build/link/progress and recount pass.
The inherited duplicate generated_12D630 Make warning is unchanged. Shared
tool smoke is fresh in both copies; three unchanged regressions per copy
are reused through exact helper/test fingerprints, not called fresh runs.

## Bank and next boundary

Receipts: `conker/build/game-type46-record-update-150C5568-match/`.
The 107 frozen inputs are audited throughout adoption. The sibling tools
checkout's 2,434 inherited dirty paths are preserved; the host Release remains
frozen. Tools commit before the consumer pin. The scoped Graphify refresh
retains existing unscanned nodes with evidence; it is not full-corpus extraction.

Next: **func_150EF910**, owner `generated_11C2B0`, a measured 79-word unmatched
Game routine. Audit its complete retail body, ABI, actual callers and owner
profile before drafting, adoption or credit. The 80% goal remains active.

Production ELF SHA-256: `d6a20624cb7128412a56c31ea27d6419ceb37a3166bb939651906a2b22f5b3b9`.

Production guard SHA-256: `89a39adda144f85f1501ffd04e94ac0b2da898172184c677d65da0c781c5dabf`.

Raw C SHA-256: `f8fd20a8a66effca85f8fa9ba1cf12a9f152a535a55aa79edf88c828f1474284`.
