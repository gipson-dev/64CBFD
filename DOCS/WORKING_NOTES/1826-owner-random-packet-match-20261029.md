# Randomized owner effect packet direct C match

Verified 2026-10-29. `func_151D0058` replaces its zero-return placeholder in
`conker/src/game/generated_1FA770.c`. VA151D0058..151D0128,
ROM1FD508..1FD5D8: 52 words/208 bytes, 80-byte frame, three call bindings.
All words emit directly from semantic C with no guards, alignment words,
instruction insertion/omission or compiler-profile changes.

## Recovered behavior

`void func_151D0058(void *owner, u8 variant, u8 priority, s32 context)`
builds a sixteen-byte packet containing owner pointer (+0), owner byte3B
(+4), halfword84 (+6), the single-precision mean of floats14C/150 (+8),
random byte (+12) and variant (+13). Padding bytes5/14/15 are not initialized.
The mean and owner identity are captured before the random provider call;
the halfword is read afterward. The randomized byte is the unsigned return
of `func_150ADA20` modulo56 plus200, giving200..255.

The factory receives `(300,-1,0x61,4,0,0x31,16,priority,context)`.
On success, all sixteen packet bytes are copied to effect+0x28. Failure skips
the copy. The result is ignored by the original caller; no pointer/integer
return contract is invented. Provider effects/clobbers are bounded test hooks;
no new C credit is assigned to the retained handwritten random provider.

The expression lists the150 load first so IDO emits retail's exact load and
floating-add operand order. The first source screen differed only in these
two load offsets. The final compiled words and bindings match the assembled
original exactly: raw SHA256
`88e0d06e834bf1bf9d3be2834a144f223c8bf478a9635ee267673372b0d03643`.

## Caller and complete owner

The full-ROM aligned scan found one direct JAL at ROM9EB00 and no aligned
full-address registration words. This is not a proof against computed or
encoded indirect calls. `func_15071628` in `game_981E0.c` is the direct caller.
Its prototype now names the four recovered arguments and void result.
Replacing the explicit255 mask with a byte cast preserves its original
sixteen-word body; adding the prototype alone produced a shorter body and
was rejected. All328 compact caller functions, pools and the entire actual
Make padded caller object remain byte-identical. No shared header changed.

The generated target owner retains all51 compact neighbors and pools. Its
normal O2/g3 profile is unchanged. Three actual Make commands produce the
qualified target object; five produce the unchanged caller object. Eight
target-owner warnings and the caller's inherited warnings retain the same
diagnostic meanings; no new diagnostic is accepted.

## Qualification

The local ignored stage is `conker/build/game-owner-random-packet-match/`.
Eight fresh canonical methods passed independently in both tools copies,
along with each copy's project tools check. Coverage includes:

- 384 guest cases with both allocation outcomes, raw high argument bits,
  unsigned random extremes, two stack phases and provider mutations.
- The entire original sixteen-word caller connected to the target in64 cases.
- Complete sixteen-byte guest packet/padding observations and24 access-fault
  prefix pairs. Native comparisons exclude unspecified padding bytes.
- Native32 O0/O2/O3 with UBSan:768 cases per profile and five rejected mutants
  (wrong modulus, signed remainder, wrong mean scale, wrong copy size and
  early halfword capture).
- Three independent GNU layouts with24 guest cases and211 raw-byte/binding
  mutation controls;212 strict-image mutation controls.
- Fresh full-owner compilation/padding, all51 neighbors, both actual Make
  routes and frozen caller-object identity.

These are instruction/C/ABI checks, not hardware FCSR, rendering or gameplay
acceptance. Guest fault-prefix checks describe emitted instruction behavior.
Negative/overflow caller commands are guest cases; portable native wrapper
overflow is not claimed.

Production then passed two fresh installed checks per copy with six unchanged
semantic checks reused only through complete input/module/artifact fingerprints.
The full ELF delta is exactly160 code bytes plus one target symbol-size byte,
with zero other metadata bytes or exclusions. All6,056 disassembled function
addresses and6,055 other bodies remain fixed. All189,088 protected Game data
bytes across720 owners remain exact. Guard CSV, linker map and C inventory
CSV remain unchanged.

Production ELF SHA256:
`56f07c4c2f7f0db6572f50ce0244bf47d270270e72a12d377f5b4c44013f2285`.
Target object SHA256:
`9e89eb8f89f679c38aa139915b55b2569121c4240f6986cbbc85a40a8d32db6e`.
Source SHA256:
`076c19d64cf7173c0bc84630fccb0fc6c35398fff34c867aff53e80b65197701`.

## Progress and handoff

Actual ELF recount: **3,903/5,506 (70.89%)**, Game3,230/4,833 (66.83%),
Init492/492 and Debugger181/181, with zero drift. **227 more** are required
for the 4,130-function75% threshold. The first queue reconciliation retained
a stale predecessor assertion; the corrected v3 recount completed against
the captured production ELF. No production failure occurred.

Canonical tools were committed first at `6ef3f3963987d4810635fccde529f50d55d1bb4c`.
The independent older mirror's1,916 inherited dirty paths are preserved;
only the three new canonical modules are added there, without a mirror commit.
The earlier documentation hook's lost relationships were source-validated
and restored before intake, retaining all48,928 previous nodes and101,581
relationships. Its receipt is in the allocator private stage. The target
refresh must preserve that repaired baseline.

The allocator `func_15187EC0` remains unfinished and uncredited in Note1825.
Next screen: `func_15084488`. Keep detailed function narratives in working
notes; the root README changes only the two aggregate matching rows.
