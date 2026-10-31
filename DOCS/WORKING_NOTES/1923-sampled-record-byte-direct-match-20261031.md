# Sampled record byte callback - direct C match

2026-10-31. `func_151638E0` in `game_18D770` replaces its zero-return placeholder
with the recovered sampled-byte callback. Its complete 240-byte slot at VA
`0x151638E0..0x151639D0`, ROM `0x190D90..0x190E80`, emits all 60 retail words
and both JAL relocations directly from C. There are no guards, insertions,
omissions, alignment changes or compiler-profile changes.

## Recovered record and interface

The interface is `s32 func_151638E0(struct225 *state)`, returning 1. For this
callback the storage at `state+0x18` is an embedded record containing a signed
index, float base and float scale. The shared declaration describes the first
word as a pointer; a local `GameScalarSample` view recovers the measured layout
without changing shared structures or other callbacks.

First call `func_15187FC0(record->index, vector)`, then call
`func_15188010(record->index, &factor)`. The first helper writes three integer
words from byte-valued table entries; the scratch vector is retained even though
this callback does not consume it. After both calls, read the live base, scale
and target pointer; store `(u8)(base + scale * factor)` to
`state->unk14->unk2F`, then return 1. Helper effects distinguish cached index,
cached affine fields and cached target-pointer errors.

Declaring the record pointer before the vector and scalar locals recovers the
original 48-byte stack frame naturally: RA at SP+0x14, record-pointer spill at
SP+0x18, factor at SP+0x1C, three-word vector at SP+0x20, and incoming state
home at SP+0x30. Both original call bindings are unchanged at offsets 0x14/0x2C.
The former commented reconstruction is removed after recovering its actual
embedded record; no other function body is changed.

All 60 words are retained. Word 48 is the original unreachable duplicate `mfc1`;
the other 59 words are exercised. No branch, FP instruction, delay slot or
fallback word is replaced to obtain the match.

## Qualification and limits

- 2,016 scripted guest cases / 6,048 original, raw-C and padded executions agree
  in complete machine state, memory, access traces and helper calls. All 47
  access prefixes and six delay-slot cuts agree. Two independent symbol layouts
  pass eight rebased cases, including code targets and signed low-halfword globals.
- Both original getters execute all 35 words, with coverage 20/20 and 15/15,
  in 144 connected cases. The vector getter reads three bytes at
  `D_800DF700[index*36]+6/+7/+8` and stores integer words; the scalar getter
  reads `D_800DF70C[index*36]`. Twelve alias cases cover owner and stack storage.
- Invalid signed indices leave getter outputs untouched. Guest evidence preserves
  the unwritten scalar's initial stack bytes; zero-initializing it is an effective
  wrong variant. This is guest machine evidence, not portable C initialization.
- The aligned ROM census finds no direct JAL and one callback pointer at
  ROM `0x22FBF0`, VA `0x8008B130`, `D_8008B0F0[16]`. The actual 41-word
  dispatcher `func_151603FC` consumes the return value: 1 retains the owner
  when its timer permits; zero invokes the free helper. The corrected suite
  runs 48 callback cases and two timer-expiry cases, plus an independent
  return-zero control. The free helper remains an ABI hook. See
  [Note 1924](1924-retail-callback-table-attribution-correction-20261031.md),
  which supersedes the earlier unrelated 23-word caller fixture.
- Native32 SDK C passes 5,066 cases per O0/O2/O3 profile with UBSan. Its providers
  always write the scalar; inputs are finite and the final float-to-byte conversion
  is defined. Every output byte, fractional boundaries, live-record/target
  mutations, and entire owner/two-target canaries are checked. Twelve native
  wrong variants and thirteen compiled guest variants have semantic witnesses.
  The zero-initialization control is guest-only; internal scratch-address changes,
  compiler failures and oracle failures are not accepted as semantic witnesses.
- Guest FP checks use a bounded, nontrapping round-to-nearest model. They exercise
  out-of-range/nonfinite retail conversion paths and save/restore control
  instructions, without claiming full hardware arithmetic exception flags or
  full FCSR behavior. Native evidence excludes unwritten scalars, guest home
  mutations/aliases, nonfinite conversions and out-of-range C conversions.
- Eight fresh canonical tests pass in each tools copy, plus both shared tools
  checks. Two installed checks per copy run fresh; six unchanged semantic checks
  are explicitly reused under complete input/module/artifact fingerprints.
- Five actual Make commands reproduce the qualified padded object and preserve
  all 77 neighboring functions and pools. All 48 inherited compiler warnings
  match after exact source file/line relocation; new diagnostics are zero.
- Strict production whole-image prediction accounts for exactly 159 changed
  bytes: 158 target code bytes and one target symbol-extent byte. Metadata and
  exclusions are zero. All 6,055 other linked bodies, all 6,056 function addresses,
  the entire guard manifest, and 189,088 Game data bytes across 720 owners agree.

## Banking and continuation

Tools commit: `f11cc3eeeb9898a6a2bf535cba8ff7c3111c2dac`. Production ELF SHA-256:
`8c4b9914475e824e2d55b072ba7cba66b551b586d751835dc8dc84903deee91b`.
Actual recount: **4,000/5,506 (72.65%)** total, **3,327/4,833 (68.84%)** Game;
Init remains 492/492, Debugger 181/181, and address drift is zero.
**130** more exact functions are needed for 75% (4,130 total).

Receipts are in ignored `conker/build/game-sampled-record-byte-151638E0-match/`.
Only the two aggregate README status rows change. The scoped graph refresh covers
the source, three tools modules and seven documents and preserves all old nodes
and valid relationships; the `s32` return type remains valid. No full-corpus
extraction, reclustering or new global analytics is claimed.
Next queued screen: `func_15115F68`. Private candidates remain uncredited.
No push or host-port/Release changes are included.
