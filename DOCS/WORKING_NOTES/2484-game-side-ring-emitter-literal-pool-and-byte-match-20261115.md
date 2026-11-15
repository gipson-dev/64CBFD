# 2484 - Side-ring emitter literal recovery and byte match

`func_1519F7F0` is adopted as complete semantic C and matches all **415 words /
1,660 bytes**, including its original **0x118 frame**. Total is now **4,512 /
5,514 (81.83%)**, Game **3,839 / 4,841 (79.30%)**, zero drift and 1,002 still
different. **175** additional matches are needed for 85% at this denominator.
Conversion classifications remain unchanged: the replaced body was a C stub.

## Source and literal recovery

Owner: `conker/src/game/generated_1CC440.c`; retail assembly: `1CC440.s`.
VA `1519F7F0..1519FE6C`, image `1CCCA0..1CD31C`. The complete C samples actor
movement, smooths the earlier ring entry, emits motion/height records, queries
the floor and advances the circular buffer. Typed actor fields and recovered
36-byte entries, 160-byte emitter and eight-byte transition are retained.

The previous extern-variable form had 240 differences and a real FP-order
counterexample. Retail's duplicate 20000.0 words in adjacent functions pointed
to per-function C literals. Recovering **0.0001f, 20000.0f and -9500.0f** restores
the original ordered delta calculations and F24/F26 lifetimes without an
artificial loop-spanning value. Using the natural transition owner temporary
also recovers the original base-plus-0x58 instruction.

The selected source emits 415 words directly, with **122 bound word
differences**. **126 expected-word/relocation guards** normalize closed register
roles, private spills and proved ordinary-memory schedules. Six literal HI/LO
bindings map the compact 12-byte literal group to existing retail symbols
`D_800A8CF4/8/C`; the compact section has four unused alignment bytes. Both
padders discard that compact pool and retain the original protected data.
There are **no inserted or omitted instructions and no compiler-profile or
Makefile changes**. Guard history remains an unchanged byte prefix.

Raw text SHA-256:
`15d83d28b8889c14488f175ad2361a60c88fe84426f520991007c62e2ecef59c`.
Relocatable normalized text SHA-256:
`c162b26ecafc4c9b5a05803148575a6824851c64ec94a40a943a78d8123df891`.

## Ordered proof and stack provenance

The independent instruction-driven symbolic relation has five inductive
phases: **7 entry paths, 4 transition paths, 68 FP/setup paths, 8 emission
paths and 14 tail/backedge paths**. These are local symbolic path counts,
not a bounded enumeration of complete emission loops. The identical epilogue
closes the saved-register/frame relation. Phase boundaries carry the live
registers and private slots; explicit write inventories protect all other
unpassed frame state, including ABI saves.

It compares public accesses, provider arguments, ordered FP opcode/operand/
FCSR transfers, and the joint sequence of public writes, calls and FP effects.
Public reads and aliases, initial FCSR and provider mutations/FCSR are
arbitrary under the ordinary mapped-memory/private-stack/o32 contract.
The proof does **not** assume disabled FP traps. Only three checked ordinary
memory commutes are admitted: the two adjacent identity-byte reads, a second
entry.X read across the disjoint entry.Z store, and adjacent threshold/actor
height reads. The RNG divisor is proved in **[1,256]**, making its BREAK path
unreachable. Every passed query/transition byte is checked.

**26 semantic corruptions are rejected**, with one independent temporary-GPR
renaming accepted for each phase. Another **430** corrupt word/binding cases
are rejected by the exact raw fingerprint/binding gate. Both padders agree
with retail at the original layout and three independent provider/time/literal
rebases, including **two HI16 carry-boundary placements**. The three literal
words remain one contiguous group at offsets 0/4/8; arbitrary independent
placement of individual literal words is not claimed.

ECOFF retains incoming-SP homes inverse=-36, transition=-44, position=-80,
velocity=-112 and query point=-140. Transition owner and mode initialize only
five bytes; copied offsets **-39/-38/-37 remain untouched**. The inverse word
also remains untouched when movement is below the epsilon. Guest instruction
proof preserves those bytes/words; portable C definedness is not asserted for
uninitialized-input states.

## Fresh execution and integration gates

- **568 guest cases per retail/raw/guarded stream**, identical public snapshots,
  ordered FP operations, raw provider arguments and all eight transition bytes;
  407 instructions visited in each stream, six effective guest controls.
- **2,048 connected cases per stream** through the original 94-word SIDE query,
  seven-word heading helper and 27-word sampler; **32 parent cases per stream**
  through the complete 100-word dispatcher, slot 5 of `D_8008A23C`.
- Original 32-word cleanup plus an injected query miss retains owner nulling
  and the twelve observed guest low-address store attempts at 0x5C/0x64. The
  ordinary real-query invariant excludes that miss; no source workaround hides it.
- **343 native defined-domain cases per profile**, O0/O2/O3 with and without
  strict aliasing, UBSan, complete public snapshots and **12 source controls**.
  The new native corpus fixes the recovered source literal to 20000.0f;
  arbitrary pool-value injection remains guest-only evidence. Nonfinite,
  opaque-miss, arbitrary-alias and bad no-motion/progress states remain excluded.
  The expected GCC inverseLength maybe-uninitialized warning is retained;
  other warnings still fail. A negative unit rejects the undefined inverse case.
- Primary qualification passed (62.162s directly observed); isolated sibling
  overlay passed (68.289s including startup); installed suite passed (57.937s).
  All fourteen task-source hashes agree. Sibling HEAD/status and its **2,434
  existing dirty paths** are unchanged; no sibling files were overwritten.
- `make tools-check` passed. Actual Make uses the existing five owner commands.
  The production rebuild passed with the existing duplicate generated_12D630
  recipe warning, so this is not described as a warning-free build.
- Independent shadow Make/link and production ELF are identical. The strict
  image prediction has **1,318 changed bytes, zero exclusions**; it explicitly
  accounts for the target body/size and two symbol/string permutation groups.
  All **6,050 other linked functions**, their addresses and extents are fixed.
- Of **880 frozen inputs**, only the declared source, guards, owner object and
  ELF change; **876 stay identical**. Exactly one of **698 objects** changes;
  its other **38 functions** and padded pools stay identical. All **189,088
  protected data bytes** remain exact, SHA-256
  `0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

Production ELF SHA-256:
`902b8b86f8ffc963c593e33b844245bf4d295dd69bd42944159f66be2b92d20e`.
The original 880-input freeze remains intact; it was not advanced or recreated.

## Review, graph and continuation

One bounded, packet-only Claude advisory was used for the earlier unresolved
FP/lifetime question. Codex rejected its unsupported disabled-trap assumption,
loop-spanning weightDifference claim and artificial lifetime extension. Codex's
independent literal-pool observation led to the selected source. Packet,
response and disposition remain ignored diagnostics; agreement is not a proof.
Packet SHA-256:
`dd010e668f72e2683863acc58f8d6dbce01e708e6ea18071587bed096a93f05c`.

The scoped AST refresh retains all **62,418 prior graph IDs**, records the
renamed private-screen test as superseded history and links the matcher to the
actual target. This is a scoped refresh, not a full-corpus extraction.
Native `graphify update .` refused a 62,500-to-26,725-node shrink caused by
existing scan exclusions and retained the graph; no force or upgrade was used.
The commit-hook completion/retention receipt is kept beside the other ignored
receipts. No host-port checkout/build applies here; frozen Release and saves
remain untouched. Exact decomp matching is separate from live gameplay or
hardware FCSR/fault-state acceptance.

Receipts: `conker/build/game-side-ring-emitter-1519f7f0-private/proof-2484/`.
`qualified-private/` preserves the preinstall reports. Historical 2482/2483
recovery artifacts and manifests remain available; the new matcher/manifest
and six proof modules are the adoption authority.

Reproduce the complete focused qualification in the prepared consumer:

```sh
python3 -m unittest tools.tests.test_game_side_ring_emitter_1519f7f0_recovery -v
make tools-check
```

Next: **func_1519FE6C**, the following **632-word / frame 0xF0** routine at
image `1CD31C..1CDCFC`, still a zero-return placeholder. Qualify its signed
third argument, graphics cursor return, allocation/output ABI, complete retail
body and caller before adopting it. Keep the 85% goal active and keep detailed
function updates out of the root README.
