# Owner effect record constructor guarded byte match - 2026-11-17

`func_151B09BC` replaces its zero-return placeholder with the complete
owner-linked effect record constructor. Semantic C emits **115 words / 460
bytes**, retaining the original **0xE0-byte frame**. **33 checked guards**
normalize a category register, the binding home, a private initialization
schedule and a closed clear-loop cursor bias. There are no inserted or
omitted instructions, frame guards or embedded retail instruction ranges.

The independent production-ELF recount is **4,542 / 5,514 (82.37%)**, Game
**3,869 / 4,841 (79.92%)**, Init 492/492 and Debugger 181/181. Address drift is
zero and 972 converted functions remain different. The active 85% goal needs
**145 further matches**. Conversion counts, converted bytes and classification
rows are unchanged. Root README receives only its two aggregate matching rows.

## Interface and constructor state

Owner `conker/src/game/generated_1DD500.c`, VA151B09BC..151B0B88,
ROM1DDE6C..1DE038. The recovered interface returns a pointer and accepts owner,
optional source, **s16 duration**, **u8 channel** and full-word context. It
preserves all five o32 argument slots. Native callers narrow duration/channel;
guest cases separately exercise noisy high bits in their incoming words.

Null owner returns null. Null source and identities 0x53/0xA5 select type 4;
other sources call `func_15134070`. Type 99 and category 2 return null.
Category is the byte at `D_800A3FE6[type * 16]`; category 1 sets the captured
record selector, and all other enabled categories clear it. The category
replaces its consumed table-index temporary, recovering the original frame.

An eight-byte owner/identity binding is prepared before `func_151494E0(...,19)`.
Five bytes are written; three binding bytes remain unspecified. The payload
then rereads owner identity after that callback, while its selector stays
captured. Mutating the retained binding's owner pointer must not redirect the
payload owner. Later allocator changes to owner identity must not change the
already built payload.

Duration -1 becomes 300 with countdown flag 0. Every other signed 16-bit duration
passes through with flag 1. Allocation uses **eight arguments**:
duration,-1,19,countdown,15,152,channel,context. Failure returns null. Success
copies **152 bytes to created + 0x28** and returns **created**, retaining it across
`memcpy`, whose own return value is created + 0x28.

The record has owner pointer+identity, ten cleared words, eight three-word
clear groups, a positive floating zero and selector. These are **146 defined
bytes**. Six bytes at offsets 0x05..0x07 and 0x95..0x97 are unwritten; the guest compares
their seeded contents, while native checks assign no portable values to them.
There is no whole-record memset. The groups are neutral word groups, without
an inferred vector/physics interpretation.

The retail binding starts at SP+0x34, the 152-byte record at SP+0x44, positive zero
at SP+0xD4, captured selector at SP+0xD8 and saved allocated pointer at SP+0xDC.
The raw binding instead starts at SP+0x3C. Its eight bytes exchange with the
unused SP+0x34..0x3B range under an explicit entry/address relation; record and
saved-result homes are literal. No unsupported 16-byte binding is invented.

Raw body SHA-256:
`07881fff70cb75f360d496d5cd6cdba0a6decf5aef8fefb50f6eac766fb59ba3`.
All six original call/data bindings, 15 owner neighbors and normalized pools
agree. The existing O2/g3/mips2/o32 profile is unchanged. A flat 34-word clear
emits 99 words; grouped clearing emits 115 but an extra category temporary
enlarges the frame to 0xE8. Reusing the dead index for category recovers 0xE0.
Volatile and oversized-binding forms are rejected.

## Independent proof and focused checks

The normalizer derives the original category V0/V1 role, three binding-home
operands, a bijection of initialization words 64..76, and a **+0x24 loop cursor
bias**. Both loop bounds shift together, and every one of the 12 loop store
offsets shifts back by 0x24, preserving each concrete destination. The loop
still executes twice and clears the same 24 group words after ten prefix words.
Relocation records retain their original positions and identities.

The independent instruction-driven proof covers **38 complete paths**, all
**244 private/incoming bytes**, captured binding/record data, ordered calls,
the complete 152-byte public copy, return value and saved-register restoration.
It allows arbitrary public aliases and retained binding mutations under the
documented nonfaulting contract. A T8/T9 allocation is an independent positive
control. Nine effective negatives reject category, duration sentinel/default,
binding home, copy size, retained result, group component, loop bound and the
unreachable duplicate constant.

There are **114 reachable target words**. Original word 38 is an unreachable
duplicate constant; the source emits it and a separate literal gate preserves
it. Runtime coverage is not reported as 115 executed words. Every final target
word and all bindings are also checked independently against retail.

Both final tools configurations pass **six fresh checks** with zero failures,
errors or skips: **134.806s primary /129.798s sibling overlay**.

- Both real padders preserve the complete owner and all 15 neighbors.
  **12 GNU links** exercise four independent symbol/carry layouts. **121
  controls** reject corruption of each 115 source words and all six bindings.
- **206 guard controls** cover 198 wrong expected/replacement/missing-word rows
  and eight bad expected/replacement relocation fields through both padders.
  Exactly 33 rows append; all prior CSV bytes remain intact and no guard retires.
- Original/raw/derived streams each pass **928 guest cases**. They cover all 114
  reachable target words and execute all **11 original memcpy words** against
  the actual 152-byte payload. Complete compared RAM agrees under the binding
  entry/address relation. Cases include source classifications, early exits,
  signed duration boundaries/-1, all 256 channel bytes, allocation outcomes,
  actor/source and output/owner aliases, two stack phases and mutable providers.
- Native32 source compiles fresh at **O0/O2/O3**, each passing 928 cases under
  strict aliasing and UBSan. Nine effective negatives cover sentinel/default,
  binding-owner misuse, selector, missing group component, negative floating
  zero, channel, short copy and returning memcpy's destination: **12 runs**.
  Five binding bytes and 146 payload bytes are credited; unwritten bytes are not.
- The three original caller connections pass **104 cases per stream**. The
  14-word prefix of func_15194794 covers the genuine constructor call/delay;
  its full parent is not qualified. The complete 18-word func_15195650 and
  func_1507003C wrappers execute and return. Their preceding func_151B01B8
  emitter is modeled in these focused tests; its linked body is independently
  proved unchanged by the full-image audit. Actual memcpy is connected.
  Three argument-corruption controls are effective.

The actual retail copy body and live installed copy bytes are verified.
Registration, classification and allocation remain modeled services; the
generic registry's callbacks and hardware allocation are not requalified.
Raw private pointer values/fault prefixes, native uninitialized bytes, timing
and gameplay acceptance are outside the claim. The normalizer does not feed
its mapping into the independent execution proof.

## Production and preservation

The independent shadow executes the actual five-command GLOBAL_ASM owner
recipe. Production Make compiles only this owner, then pads, relinks and
recounts. No prebuilt object is installed. Production equals the independently
predicted ELF: `d3caaa0bd472f25769a9ea5f9de1fcd23cdd35cf5c25aa1ae78344fc0159fe4b`.

Strict complete-image accounting changes **344 bytes** with **zero
exclusions**. No symbol/string permutation is required: only the target
instructions and declared target symbol size change. Four controls reject
symbol value, name byte, protected data and target-word corruption. All other
**6,050 bodies and all 6,051 addresses** are unchanged. One of 698 objects changes,
retaining 15 neighbors, including the two preceding recovered constructors
and the retained blood GLOBAL_ASM routine. All **189,088 protected bytes / 720
owners** remain exact. The progress classification CSV is byte-identical.

Fresh installed-source compilation agrees on all 16 owner functions. Actual
production words pass another 928 guest cases and 104 cases per original caller
connection per stream. Prior padder/link, proof and native checks are reused
only with exact task/input/fixture fingerprints. Production match-progress,
tools-check and an independent actual-ELF recount pass. The existing duplicate
generated_12D630 recipe warning remains unchanged.

The baseline freezes **1631 inputs**, including the observed registry assembly
interface, with no links to live-tree files. Exactly four change: source,
guard CSV, owner object and ELF. Nine task files and actual imported helpers
are separately fingerprinted. The sibling's 2,434 dirty paths / 343 scoped
dependencies remain unchanged; testing uses a private overlay. Claude calls
are 0. Host Release/saves are untouched; no adjacent host source checkout is
available to synchronize.

Evidence is retained under `conker/build/game-next-151b09bc-private/adoption/`:
sealed paired checks/imports, derivation and proof, guard/padder/link controls,
guest/native/caller and real-copy receipts, Make prediction/production audits,
installed focus and actual recount. Native Graphify update fails closed on
its reduced scan. Scoped AST merging of eight files retains all
65360 old IDs and the explicit target reference; this is not full-corpus
extraction. Commit tools before consumer source, guards, notes, aggregate
README rows and pin, locally only.

Next inspect **func_151B0B88**, the **385-word** placeholder in the same owner.
The 85% goal remains active.
