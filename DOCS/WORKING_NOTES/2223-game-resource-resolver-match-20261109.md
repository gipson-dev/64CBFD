# Game resource resolver guarded match - 2026-11-09

func_1510D0EC now matches its full 162-word / 648-byte retail body after
76 strict expected-word and relocation normalizations. Its existing semantic
resource-loading C is fitted to the original control flow and natural frame
0x50. This is a guarded match; the unnormalized C is not byte-exact.
There are no inserted or omitted instructions, frame guards, helper-ABI changes
or compiler-profile changes. Source: conker/src/game/generated_139FC0.c;
original: conker/asm/139FC0.s. Historical semantic recovery is in Note 965.

Production total **4,292 / 5,513 (77.85%)**, Game **3,619 / 4,840 (74.77%)**,
Init 492/492 and Debugger 181/181. Zero address drift; 1,221 still different.
**119** further accepted matches are needed for 80%; the wider goal stays active.

## Semantic and source audit

VA 1510D0EC..1510D374; ROM 13A59C..13A824. The unchanged API is
u32 func_1510D0EC(s32 id, s32 *extent, s32 priority, s32 retain).
The compressed/expanded size tables contain unsigned halfwords; the cache
contains words, priority is signed byte, activity is unsigned byte, and the
minimum/maximum dirty IDs are signed words. Shared declarations remain fixed.

Minimum/maximum accounting happens even for invalid IDs. IDs outside 0..7761
return 0x80000000 before table or output access. Zero compressed length writes
that sentinel into the cache, then follows the normal extent/priority/activity
tail. Other resident cache values are returned without allocating. Cache
0xFFFFFFFF selects loading, sets the work counter to five and changes incoming
priority 0x3F to 0x3E only on that miss path.

The offset helper supplies the source. Odd sources decrement once and retain
skip=1; even sources retain skip=0. Compressed length plus skip first rounds
to even, then to sixteen bytes. The first allocation receives (size,1,2,1,2),
DMA receives (source,compressed,size,1), and the fresh expanded extent supplies
the second allocation (extent,1,1,0,2). The first failure returns immediately;
the second frees the compressed allocation before returning. Neither failure
writes extent, cache, priority or activity. Successful decode uses compressed
plus skip and the fresh scratch global, ignores the decoder result, frees the
compressed allocation, publishes the expanded allocation and resets activity.

Extent is read freshly after callbacks and written only when its output pointer
is nonnull. The return cache word is captured after that output store and before
priority/activity changes. This order matters for output/cache aliases. Signed
priority promotion and byte truncation are preserved; nonzero retain increments
activity only below 255. Provider mutation and alias cases are explicit in the
tests, rather than being inferred from ordinary success cases.

The former C emitted 155 words. Recovering the original upper-bound-first gate,
explicit odd-source branches, size reuse and six-local declaration order emits
162 words with the original frame. Seventy-six remaining normalizations cover
temporary registers, the aligned-size private spill and its independent
store/reload schedule. All branch/call positions, prologue and epilogue agree.
Private locals are not passed to SDK providers. Incoming-home mutations are
guest-only cases, separate from the native defined-input domain.

## Qualification and boundaries

- Thirteen raw and padded owner neighbors, constant pools and all .reginfo
  fields remain fixed. Both padders agree; both reject stale expected words
  and stale relocation annotations. The inherited CSV is a byte-identical
  prefix with exactly 76 appended rows for this target.
- Actual Make in an owned mirror uses the unchanged Makefile and the real
  source/manifest names. Its object equals the independent prediction.
  Production repeats one O2/g3 owner compile with zero diagnostics and yields
  the predicted object and ELF.
- Guest: 608 cases per body / 2,432 executions compare retail, normalized,
  raw candidate and former semantic C. All 162 retail words execute. There
  are 150 literal fault-prefix pairs, including 12 delay-slot faults, and six
  rebased layouts / 36 cases. Forty-eight connected cases execute the actual
  byte-exact 36-word source-offset helper. Original/normalized complete literal
  states agree; all four public contracts agree.
- Native32 O0/O2/O3 freshly execute the six established resolver contracts
  with strict aliasing and UBSan. Thirteen compiled semantic controls are
  effective in every profile and in IDO guest execution. Allocator, DMA,
  decoder and free are bounded providers; real DMA/decompression, hardware
  diagnostics, gameplay and host-port runtime acceptance are not established.
- The original retail JAL census contains 64 sites and no function-pointer
  literal references. Two sites are in ignored legacy GLOBAL_ASM files;
  explicit ROM/assembly inspection includes them. All 64 real JAL/delay
  windows run five allocation/cache outcomes, 320 cases / 1,280 executions
  across four root bodies. Register/load preconditions and caller stack
  boundaries are explicit. This does not qualify complete parent routines.
- Strict whole-ELF prediction changes only the 648-byte body and its symbol
  extent 620->648: **485 changed bytes, zero exclusions, no metadata
  permutation**. All 6,052 function addresses and every other function body
  remain fixed; all 189,088 protected bytes across 720 owners are exact.
  Six independent image corruptions are rejected. Progress CSV bytes,
  Makefile and compiler profiles stay fixed. Production recount adds exactly
  one total/Game match. The inherited whole-ROM checksum mismatch remains:
  make all exits 2; whole-ROM equality is not claimed.

## Regression and repository record

The original 17-test texture-resource suite was first verified against its
frozen old source and test module. Two historical assertions required the
resolver to stay unguarded and 155 words long. Their replacement preserves
setup/attachment checks and freshly compiles the complete resolver owner,
applies the production guards and compares every one of its 162 words with
retail. The six existing behavioral contract methods are unchanged. The
updated complete 18-test suite passes after installation in both environments.

Six focused checks pass before and after installation in both tools copies.
The sibling uses an isolated seven-file overlay, including the updated existing
SDK test, with explicit consumer roots and dependency fingerprints. Its 2,434
inherited dirty paths and file contents are preserved. Fresh shared smoke checks
accompany three unchanged, exactly fingerprinted regression reuses per copy;
reuses are not fresh tests. The package freezes 624 inputs, preserving the old
SDK test snapshot and explicitly allowing only the measured updated live test.

Tools commit before consumer; no push. Root README changes only aggregate rows.
Graphify receives a scoped AST refresh with old-node retention, not full-corpus
semantic extraction. Host-port Release stays frozen; zero Claude calls.
Next: audit func_1510D404 cache maintenance, still non-matching and uncredited.
Fresh measurement confirms 125 raw C words versus 129 retail words, 119
positional differences, and C frame 0x40 versus retail 0x60. Recover the real
saved-value lifetimes before considering guards; equal body lengths alone
would not establish the required frame. Its historical semantic and provider
contracts are recorded in Note 968.

Focused WSL check:
python3 -m unittest tools.tests.test_game_resource_resolver_1510d0ec_match -v
Receipts: conker/build/game-resource-loader-1510D0EC-exact-20261109/.

Production ELF SHA-256: d36c896fc5cca7674f52e388a79e381b9a8739a8cbafb8237e8d59da10ae16d9.
Guard SHA-256: 8ae864591b9da930c49961a14849ce9295bc81c5f30aa4ae950fee633e26019a.
