# 2631 - Record sound scheduler direct byte match

Date: 2026-11-22. The total 85% matching goal remains active.

`func_150D0730` replaces its zero-return placeholder with complete semantic C.
All **97 body words / 388 bytes emit directly**, frame 56, **zero guards**,
inserted or omitted words. Its 100-word retail slot retains 12 zero tail bytes.
Production is **4,613 / 5,528 (83.45%) total**, **3,940 / 4,855 (81.15%) Game**,
zero drift, 915 different. Init 492/492 and Debugger 181/181 remain exact.
**86 more matches** reach 85%. Conversion rows are unchanged.

## Source and behavior

Source `conker/src/game/generated_FDBE0.c`; original `conker/asm/FDBE0.s:11`.
Body VA150D0730..150D08B4, ROMFDBE0..FDD64; slot ends at150D08C0.
S0@SP30, RA@SP34, unused incoming word home@SP38. The return is void.
Raw SHA256 `bb35f6d9587d6488722b2f84cb4ad6953462e817874b6cf15bd0e24db1f755b2`.

The routine first calls func151827D0, then reads byte D800D98F0. A nonzero
cooldown subtracts signed D800BE9E4 when smaller, otherwise clears. Explicit
unsigned subtraction preserves SUBU and byte wrapping for extreme signed
steps without C signed overflow. At zero cooldown it queries indices15,1A,
1B,1C,1D,20 in order and uses the first zero result. No selection means no RNG
or sound. Separate unsigned draws set delay(value&127)+128 and sound108+value%3.

The record pointer D800D3098 loads after the second draw. Local
AmbientSoundRecord names signed x/y/z at0/2/4, size0x34, leaving0x2E bytes
opaque. Existing shared variables.h describes an inline legacy array;
the actual instruction loads a pointer, consistent with other recovered
owners. This correction stays local. No shared header or dependent object
changes. The ten sound arguments are sound,24000,0,0,0,x,y,z,800,1500.

The initial source put the second RNG call inside the sound argument list.
Native mutable-provider tests exposed its unspecified evaluation order.
An explicit soundId assignment completes that call before coordinate reads,
and still emits all97 identical retail words with the same frame and ELF.
Both tested sequenced variants are exact; only the clear soundId form is
adopted. The initial unsequenced candidate remains private and uncredited.

## Actual caller and helper boundaries

Ignored assembly data231730.rodata.s contains the28-entry D8008CD04 table.
Index14/address8008CD3C registers this callback. The complete original/current
43-word caller151749F8 passes the saved incoming view word, ignores the
callback result, runs gated tail helpers and advances its wrapping phase.
Both streams pass224cases covering selection/cooldown/effects, two stack
phases, tail gating and view values. Zero scene gating and an effective
omitted-view-reload control pass. The complete table and caller bytes agree.
The decoded binary has one aligned absolute pointer reference and no direct
J/JAL references; compressed assets/runtime references are outside that census.

Original/current query73words, integer RNG18words and sound wrapper29words
execute in2,016cases per stream, covering every helper word. Independent
64-bit seed transitions verify both draws. Query bounds, actor-mask bitset
and collision paths pass. The sound wrapper forwards eleven correctly
typed words to10010E78, including its leading zero handle and signed narrow
coordinates. The actual recovered wrapper C also runs in native qualification.

Setup151827D0 is still a291-word zero-return placeholder in current source.
Its side effects remain an explicit test contract, including changes before
the cooldown read. Shift, collision, deeper audio and other caller helper
internals also remain contracted. This match establishes no full scene/audio
or gameplay acceptance and supplies no new credit for those helpers.

## Qualification and adoption

- Guest:4,951cases per candidate/original stream, all97 target words executed,
  all256 cooldown bytes, signed step extremes, first-zero and negative truth
  results, independent unsigned RNG values, signed coordinates, provider
  mutations and late pointer/record loads.48 access-fault comparisons pass.
- Native SDK32 O0/O2/O3:569cases each, actual52-byte record layout, strict
  aliasing and UBSan, all call-boundary states and eleven forwarded sound
  words. Ten effective controls cover signed timer/step comparisons, missing
  setup, query truth/priority, delay mask, remainder sign, coordinates,
  attenuation and incorrectly cached record pointers.
- Both padders preserve the97-word payload and12-byte zero slot tail.
  Sixteen independent GNU links cover all18 bindings and HI16 carry edges.
  This owner contains only the target; normalized pools/diagnostics agree.
- Natural existing O2/g3 Make uses three commands. Complete independent ELF
  prediction has **282 changed bytes, zero exclusions and zero metadata
  permutations**. All189,088 protected GameData bytes/720 owners, other
  bodies/addresses, old guards and conversion rows agree. ELF SHA256
  `e58e790f8c12ff99002933c18d65d541f77c13257bdbc52b2e59e11aad1996b7`.
- Both tools configurations pass all five checks before and after installation,
  with exact Python/data hashes. Shared tools-check passes. Real sibling edits
  and dependency hashes are preserved. Existing duplicate generated_12D630
  Make warnings remain unchanged.

Baseline consumer `da24f369f1d96da6f418baf28ccd552b27434ddb`, tools `1d5f14abc4a6732dc919e0abce286362ebf8c4af`.
Tools commit `83adf5f57576dfbcd7c73b62a2e9508118f722d1` precedes the
consumer commit. No push. Available host configuration applicability is
recorded separately; no direct C import, host/Release change or gameplay
acceptance is inferred from its different binary mapping. Zero Claude calls.
Complete graph retention and immutable banking before the next recovery.

The final whitespace audit removed one trailing blank source line. The
functional source body is unchanged; both installed configurations rerun with
the normalized source manifest, followed by the same literal image audit.

Graph maintenance: the native update exited 1 with all
70,762 prior IDs retained. The subsequent serial scoped extraction
covers 8 C/Python files with no missing AST sources, producing
70,821 nodes / 167,346 links and retaining prior qualification
metadata. This is a scoped refresh, not a full-corpus re-extraction. Actual
commit-hook producers must be terminal and their ID/metadata retention audit
must pass before the final immutable bank is accepted.
