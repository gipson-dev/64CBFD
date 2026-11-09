# Script-Selected Actor Scalars Direct Match - 2026-11-09

`func_150B2340` replaces a false zero-return placeholder with the complete
query-selected actor scalar and flag update. All **79 body words /316 bytes**
emit directly from semantic C under existing **O2/g3**. The complete
**80-word slot**, including one existing trailing NOP, is byte-exact.
Retail frame **0x28**, saved S0+0x18 and RA+0x1C. **No guards, profile or
binding changes** are required.

Production: Total **4,282 /5,513 (77.67%)**, Game **3,609 /4,840 (74.57%)**,
Init **492/492**, Debugger **181/181**, zero drift; **1,231** still different.
**129** more exact functions reach4,411/5,513 and80%. Conversion rows stay fixed.

## ABI and recovered body

Owner `conker/src/game/generated_DF260.c`; original `conker/asm/DF260.s`.
VA150B2340..150B247C body, slot through150B2480; ROMDF7F0..DF930 slot.

```c
void func_150B2340(s32 actorAddress);
```

Keep the actual callback's32-bit integer address interface and use inline
views through the existing struct108. All six field offsets and its
**2,464-byte layout** are asserted in native32. There is no shared layout or
header change. A pointer formal also emits79 exact words, but alone does not
prove compatibility with the legacy callback table's promoted integer
argument. A separate pointer local changes frame0x28->0x30 and six words;
reversing the two result locals changes four words. Both are rejected.

The aligned ROM census has no direct calls or interior entries and one
address value: ROM22E184/VA800896C4, entry21 of D_80089670. The complete
48-entry callback table remains unchanged in ROM and linked read-only data.
Actual consumer func_15130230 reads byte D_800B0DF0+0xF, skips0 and invokes
that entry with its first s32 argument, ignoring return. Its unprototyped
void callback type is compatible with this default-promoted s32 interface.
The complete17-instruction caller (20-word slot) is exact, and its full
source/object remains unchanged.

- First call func_1509BE40(0,0x2007,0xB7). OR its entire return word with
  0x2000 and use those flags in the following call with key0xBC. Capture
  that result as enabled, and query(0,0x2000,0xBB) as blocker. Both values
  survive all later calls in their original SP+0x24/+0x20 slots.
- Query flags0x5043/key0x1A. If nonzero, query0x5045/key0x1A and OR actor
  word+0x84 with0x4000 only for a nonzero result. Then OR+0x84 with0x400000
  and store positive0.0f at+0x190. Preserve all live actor reads.
- Otherwise call(1,0x4030,6,0x2000). Nonzero stores235.0f at+0x190; zero
  stores114.0f at+0x348 then+0x34C,384.0f at+0x374,60.0f at+0x190.
- Set actor word+0x5F0 bit0x100 only when enabled!=0 and blocker!=-1;
  otherwise clear only that bit. There is no original null check.

The helper's first parameter is **extra-argument count**, not an operation
code. Its original92-word body saves the old D_800D3840 count, writes
flags&0xFFF and key into D_800D2F60, copies the supplied extras after them,
sets count+2, and dispatches through D_80088498[((flags&0xF000)>>12)-1].
The callback receives(selector,key,packet), and the old count is restored
after its return. Target paths use counts0/1, hence three/four arguments.
Leftover A3 values on count0 calls are not extra arguments. The helper's
existing C stub stays unmatched and receives no credit.

## Qualification

- **117 frozen inputs** include owner/objects, both callback tables, the
  complete caller and original helper, handwritten neighbor assembly, ROM,
  compiler/headers, layout/guards and linker bindings. All316 raw bytes
  and six R26 relocations are pinned; every single-byte and binding-name
  corruption rejects. Retail-slot and strict-image corruption also reject.
- Both padders agree on all five owner functions. All **four raw/padded
  neighbors**, pools and exact register-mask union are fixed, including the
  handwritten two-block transform. Its existing GLOBAL_ASM requires the
  actual **five-command owner recipe**, including pre/postprocessing. That
  recipe and the caller's **three-command recipe** reproduce the qualified
  objects with zero compiler diagnostics. No shared helpers are modified.
- Entire-ELF prediction permits only this320-byte slot and symbol extent
  12->316: **255 changed bytes, zero exclusions, no metadata reorder**.
  All **6,052 addresses**, other bodies and **189,088 protected bytes across
  720 owners** remain fixed. The callback table, dispatch table, caller,
  Makefile, guards, headers and progress CSV remain unchanged.
- **512 guest cases per body** compare all public memory and all2,464 actor
  bytes at every provider boundary. Live callback mutations cover flags,
  scalar bit patterns and other bytes; arbitrary returns distinguish whole
  word OR, nonzero tests and the-1 sentinel. Raw and retail full literal
  state/access order agree. **78/79 body words execute**; retail word70 is
  an unreachable duplicate load. All80 slot words match literally.
- **Six independent GNU links /24 rebase cases per body** qualify all six
  R26 sites. **20 guest alias/wrapped-address cases per body** and **53 fired
  instruction-fault prefixes** compare GPR/FPR/HI/LO, memory, calls/snapshots,
  access trace, dispatched word, PC and delay origin. These do not claim
  portable C null/global-alias/fault behavior.
- **32 complete caller cases per body**, through both retail and actual
  production caller images, qualify entry21, zero-selector skip, arbitrary incoming
  second words and full return. The callback table is checked in
  full, and caller source/object bytes are identical.
- **64 original variadic-helper connection cases per body** execute the
  original92-word helper (66 words visited), counts0/1, its dispatch table,
  the full64-byte packet window and count restoration. Dispatch callbacks
  are bounded providers; their arbitrary actor mutations/return words are
  recorded independently. The unrolled count>=4 path is outside this
  target's call contract; no full-helper or hardware acceptance is claimed.
- Native32 **O0/O2/O3 each pass256 cases through both typed and legacy
  unprototyped callback entry forms**. Every actor byte and all five
  provider snapshots/arguments are checked, with actual variadic reads,
  existing struct108 size/offset assertions and trap UBSan. All **23 compiled
  incorrect bodies** fail observably in every native profile and IDO guest
  execution. Artificial aliases/null/wrapped addresses stay in guest checks.
- One incorrect negative-zero body requires a real IDO literal pool. Negative
  controls link their original objects/pools independently; those read-only
  bytes are retained in the guest fixture. This is test data, not production
  code/data substitution. The positive candidate needs no literal pool.

Seven fresh target checks pass in both tools environments before/after
installation. Shared smoke is fresh in both; three unchanged regressions
per copy are explicitly reused by exact helper/test fingerprints. Production
Make/recount agrees with prediction; only this owner compiles, with zero
diagnostics. The inherited whole-ROM checksum mismatch makes make all exit2;
duplicate generated_12D630 Make recipe warnings remain.

Tools commit before consumer. Sibling tools retain2434 inherited dirty paths;
frozen host Release is untouched. Scoped Graphify refresh retains existing
unscanned nodes with evidence and is not full-corpus extraction.

Receipts: conker/build/game-script-actor-scalars-150B2340-match/.
Next: func_150D88E0 has a private80-word direct match using byte-indexed
64-byte matrix records, with its original frame0x40 and no guards. It stays
uncredited pending caller/selector-domain, native/guest, owner and complete
image qualification; its unsupported selector paths require explicit audit.
The80% goal remains active.

Production ELF SHA-256: d727f4d7ce69cfbeff3fa1a2d258382cdee1b69318de29de9c2b34317cea21df.
Guard SHA-256: 6a6094f04735cb3127833e50b21f98c3374916605acd7aa79ccdebd80d22dfe7 (unchanged).
