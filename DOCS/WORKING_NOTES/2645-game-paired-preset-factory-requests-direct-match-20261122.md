# 2645 - Paired preset factory requests direct match

Date: 2026-11-22. The total 85% matching goal remains active.

`func_150BEF7C` in `conker/src/game/generated_EC420.c` replaces its false
zero-return placeholder with two preset factory requests. All **94 words emit
directly from C** in the original **224-byte frame**, with **zero guards,
insertions or omissions**. Both full-owner padders and the actual Make recipe
preserve all nine other compiled owner functions, pools and diagnostics.

Production: **4,626 / 5,528 (83.68%) total**, **3,953 / 4,855 (81.42%) Game**,
zero address drift, **902 different**, **73 more matches to 85%**. Init remains
492/492 and Debugger 181/181. Converted-function and byte rows are unchanged.

Original: `conker/asm/EC420.s`, line 17. VA `150BEF7C..150BF0F4`;
ROM `EC42C..EC5A4`; 376 bytes. There is one JAL relocation, to `func_1516D99C`.

## Recovered source, widths and calls

The interface is `void func_150BEF7C(s32 parameter)`. Its normal do/while
loop makes two calls to the existing 49-argument packed-record factory, with
signed positions 380 and -380 and otherwise fixed preset fields. The input
remains a word at this wrapper's ABI; only the factory's argument 31 narrows
to its low unsigned halfword. The exact existing mixed-width factory prototype
is copied locally from its recovered definition, including its void return.
No shared header or callee implementation changes.

The factory stores this shared halfword at record+0x20 and its low byte at
record+0x3C. The requests pass coordinates 8155, 37 and the mirrored position,
kind 13, the four 0x555 halfword fields, the remaining fixed byte/halfword
settings, a low-byte allocation flag of 255 and context zero. The loop always
submits both requests, including when the first allocation fails.

The all-word prototype draft was 97 words. Recovering the actual factory
prototype gives 95; changing the wrapper's wrongly narrowed input to a word
removes its spurious incoming-home store and restores all 94 words directly.
The original saved S0/S1/S2/S3 and RA locations, parameter lifetime, outgoing
49-word argument area, loop branch and delay-slot position negation all match.

The pinned literal direct-edge census finds calls at `15027058` in
`func_150265CC` and `1509D534` in `func_1509D180`, with no aligned exact-word
pointer to this wrapper. Each loads a full word in the JAL delay slot, then
sets V0 to one in its outgoing branch delay slot. Neither consumes the
wrapper's return value. Computed or separately materialized pointers are not
excluded by this census. No existing source caller declaration needs changing.

## Fresh focused qualification

Five gates pass freshly in each tools setup before adoption. Installed runs
freshly repeat the complete-owner compile, actual Make and independent whole
image gate, then reuse four semantic gates only after exact source, object,
binding, original-target, native-artifact, manifest and import hashes agree.
Those reused semantic tests are not described as fresh installed executions.

- Raw, padded and original target streams each pass **300 direct cases** and
  **400 complete factory-chain cases**. Every target word executes. The chain
  executes the actual/current **125-word factory** and **28-word allocation
  wrapper**, whose complete slots equal ROM. Cases cover zero/byte/halfword
  boundaries, high and negative input words, two stack phases, incoming-home
  mutation after capture and all four combinations of allocation success.
  All 49 arguments, both 0x4C-byte records, opaque bytes, markers and full
  private machine states compare. Heap allocation and record registration
  remain bounded providers; their internals and gameplay are not claimed.
- Both real **four-word caller windows** pass **300 cases per target stream**,
  including the actual delay-slot word loads and outgoing delay-slot V0=1.
  This is window coverage, not complete execution of the large dispatchers.
- **548 full access-prefix triples** compare raw/padded/original memory,
  GPR/FPR state, HI/LO, ordered accesses and calls. Cuts fire at dispatched
  own accesses, including a connected factory/allocator case. Provider internals,
  asynchronous faults and hardware are outside this model.
- Native actual SDK32 O0/O2/O3 each pass **196,608 cases**, sweeping every
  low-halfword value under three high-word patterns. The noinline typed
  provider checks every one of the 49 mixed-width arguments on both calls.
  Strict aliasing and UBSan remain enabled. Six independently compiled C
  controls fail through comparison: byte-only input, wrong position, missing
  mirror, one request, wrong kind and wrong fixed field.
- The actual factory C retains a big-endian byte-home read for argument 47.
  Its unmodified native execution is not asserted for this preset's word 255.
  Native coverage checks the complete new wrapper and its real typed boundary;
  the complete original/current factory executes in the guest instead. This
  work introduces no host-endianness adaptation or helper behavior change.
- Both full-owner and isolated-target padding paths preserve the direct
  bytes and named binding. **12 GNU links** and **168 guest rebase runs** cover
  four independent code/callee address arrangements, including another J26
  region. Four wrong-word/binding outputs fail comparison. An oversized
  nonzero body is rejected by the generated padder; the generic padder's
  supported overflow trampoline also fails this target's exact comparison.
  The accepted target has no overflow body or trampoline. No shared padder
  implementation changes.
- `make tools-check` passes. The real sibling tools checkout's HEAD, dirty
  state and 353 retained dependency hashes are preserved through a disposable
  overlay. Routine Claude calls: 0. Existing duplicate Make recipe and legacy
  compiler warnings remain; the changed owner's diagnostic set is unchanged.

The first packaged suite exposed a test-report module/function name collision.
That fixture alias was corrected and the complete five-gate suite rerun.
It changed no recovered C, target instructions or production configuration.

## Independent image and production audit

The complete actual ELF equals an independent prediction: **295 changed bytes,
zero exclusions and no metadata permutations**. Only the 376-byte target slot
and symbol size 12->376 change. The independent reference compiles the frozen
OLD owner with OLD guards, requires its whole padded object to equal the old
production object, and replaces only this slot with independently assembled
original instructions. The recovered new C is not used to construct the
reference. Named definitions, string-pool coverage and ELF geometry are checked.

All **189,088 protected Game data bytes across 720 owners**, other loaded
bytes, all function addresses and other function extents, conversion rows, guard history, headers,
profiles and private inputs remain fixed. Production Make and a fresh live
recount provide the totals above. Documentation and the graph cache are
accounted for separately in the final input bank, rather than being described
as unchanged production bytes.

Raw target SHA256:
`2e95ce74c28d78b20f83422a48a407522cdb1ae7143ffd5420853dc70a01e3f5`.
Qualified owner SHA256:
`d0cda77dd0c601d012042414cd89f55c8fd181db771c919790e42535d6db5d39`.
Production ELF SHA256:
`7fe81de603419059cdc3e32fdf698e710f8e87af9a66bf28807a33aed62a1c5c`.

```sh
python3 -m unittest tools.tests.test_game_opposed_effect_spawn_150bef7c_match -v
```

Artifacts: `conker/build/game-opposed-effect-spawn-150bef7c-private/`.
The retained fixture fails closed if its production/compiler/source inputs
change beyond the declared phase. Codex owns implementation and validation.
No push, provider change, sibling host import/build or Release change.

## Decoder handoff and next work

The separate `func_150A6760` flow screens are retained in
`conker/build/game-visibility-bitplane-150a6760-fit-private/`. A branchless
child lookup shortens its private C form to 67 words/frame zero, and a
single-next-loop form is 69. These change control shape and are not matches.
The earlier access-preserving qualifier experiment remains 74 words/frame
zero, with no established original volatile provenance. None is installed
or credited. [Note 2644](2644-game-visibility-bitplane-decoder-private-recovery-20261122.md)
retains the decoder's semantic qualification and limitations.

The fresh queue has 902 remaining Game differences. The next same-owner target
is `func_150C04C0`: 98 words/frame 152, ROM `ED970..EDAF8`. It builds local
packets and calls `func_15150400`; start by recovering that helper's real
packet/argument types and the local layout. It is still an unchanged stub.
Continue remaining Game conversions toward the full 85% goal, without counting
the private decoder forms or forcing a broad normalizer.
