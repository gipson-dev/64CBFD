# Note 2595: List unlink ABI and dead-home byte match

Date: 2026-11-20. Consumer baseline `ea15499b032d5f43e05c193d706f6135fe90eb2e`;
tools baseline `cc9cfc5cea8da04075fe1a81bcd51c60a927160c`.
Qualified tools commit: `15f923aae01392450f9e2c8a393e741e364d44c1`.

`func_1517E134` replaces its remaining GLOBAL_ASM with complete semantic C.
All **30 retail words / 120 bytes / frame 24** match after one checked omission
of the compiler's unused A1 argument-home store. The normalized owner, typed
caller object and **entire production ELF are byte-identical** to the baseline.
No instruction, data, symbol-table, address or size exclusion is used.

Fresh production recount: **4,580 / 5,528 (82.85%)** total and **3,907 / 4,855
(80.47%)** Game. Init 492/492 and Debugger 181/181 stay exact. Zero drift and
948 still different are retained. Converted totals are 5,528 / 6,048 (91.40%) | 86.54%;
Game 4,855 / 5,327 (91.14%) | 85.95%. The denominator increases because this was retained
assembly. **119 more** matches are needed for 85% at this denominator; the
85% goal remains active. Root README changes only four aggregate table rows.

## Interface and complete behavior

Owner `conker/src/game/generated_1AB530.c`; VA `0x1517E134..0x1517E1AC`, ROM
`0x1AB5E4..0x1AB65C`. Interface `void (void *target, void *unusedActor)`.
Retail ignores A1. The two known complete callers `func_151411E4` and
`func_15141250` pass the actor context in A1 and ignore the return. Their
local prototype now states that interface; both original volatile attachment
reads and both arguments remain intact. All **16 caller raw functions,
bindings and pools**, and its complete padded object, are unchanged. Neither
before nor after compilation emits diagnostics.

The routine captures D_800DDD64, unlinks a target at the head or searches for
its predecessor through +0x24 links, and calls `func_10004074(target)` only
after the corresponding head/link update. A non-null absent target is left
alone. There is no post-free target read or write. No speculative NULL gate
was added: a NULL target is outside the defined C test domain and can reach
retail's target+0x24 dereference. Finite well-formed lists, ordinary readable
records, and disjoint public/private storage are the supported domain.

An aligned full-ROM census finds exactly two direct JAL sites, ROM
`0x16E6B0` and `0x16E71C`; no aligned literal pointer is found. Computed callers
remain unexcluded. The independent tests execute both complete original
callers, including attachment gating, decrement, subtype lookup and callback.

## Checked omission and safety relation

The existing O2/g3 profile emits **31 raw words**. Its exact raw SHA-256 is
`3c060c08a4b4da480e0f48b6f34a81321a270a0db8819a92323d705b408a4abe`.
Source word 4 / offset 0x010 is `0xAFA5001C` (`sw a1,28(sp)`). With the
unchanged 24-byte frame this writes **incoming SP+4..+7**. It is not the saved
return-address home. A structurally checked derivation consumes only the raw
payload/hash and exact bindings and removes this one instruction. Relocations
after it move back four bytes; all 30 retained instructions remain untouched.
The CSV's single expected-word/binding row records exactly that omission.

The fixed stream reads A1 only in the removed store. Stack accesses otherwise
save/reload RA at SP+20; SP-derived addresses do not escape or become helper
arguments. The incoming A1 home is never read, and no branch reaches or crosses
the removed instruction. All retained branch sources and targets move together,
preserving immediate displacements and delay slots. Free receives only target
in A0. Under the ordinary o32/C provider contract, an unused, unpassed private
argument-home write has no public or ABI-observable effect. Providers may mutate
public state and clobber outgoing argument homes and volatile registers, but
cannot inspect unpassed incoming storage or non-argument registers. Public
objects cannot alias that private storage. This is a normal-execution relation,
without a fault-prefix, timing or hardware claim.

The raw and retail guest streams differ only in that explicitly dead incoming
word; the raw store holds the supplied context in all 2,184 cases. The full
24-byte private frame, saved-register lifetime, other incoming bytes and public
state agree. **Normalized versus original agrees in all memory**, including
all private/incoming bytes. Independent assembly confirms exact bytes AND
relocations; two GNU links, including code/data rebases with low-half carry,
agree. Payload and binding corruptions are rejected. A direct one-formal C
screen also emits all 30 words, but the adopted two-formal interface preserves
the known callers' compatible C types and original arguments.

## Fresh qualification

All **14 tests pass in both tools configurations before and after installation**:
six unlink checks plus the prior renderer's complete eight-check suite. All
**340 imported Python fingerprints** agree. The isolated
overlay has **1062 files**: 347 matching
sibling files, 704 primary fallbacks,
ten task files and one bootstrap. It is a hybrid overlay, not a claim that
the dirty sibling alone is current. The actual sibling retains its HEAD,
status and **351 dependency hashes** and is not committed.

- Guest: **2,184 cases per raw/normalized/retail stream**, lists of length 0..12,
  every head/interior/tail/absent position, four ignored contexts, three free
  mutation modes and both stack phases. All 31/30/30 instruction origins are
  covered. The free provider observes unlinking before any mutation.
- Connected callers: **2,184 cases** through both complete retail bodies,
  attached/empty attachment, ABI clobbers, mutated counter/subtype and callback
  dispatch. Raw's only possible private difference is the same unobserved home;
  normalized/original full memory is identical.
- Three effective guest controls reject a wrong next offset, missing head
  unlink and wrong free argument. Native SDK32 O0/O2/O3 each pass **1,092 cases**
  with compatible typed objects, strict aliasing and UBSan. Three source controls
  reject a wrong free argument, missing head update and inverted head predicate.
- Both padders produce the same complete owner object. Actual Make executes
  **three owner commands and three caller commands** with the existing profile.
  All seven raw neighbors/bindings/pools remain fixed. Shared tools checks,
  production Make, recount and installed suites pass.

The renderer's historical pre-restoration archive is left immutable. Its
fixtures accept one additional exact owner/guard hash pair, after confirming
its complete body, all neighboring raw functions and full padded output.
Unknown owner/guard snapshots remain rejected. Its original derivation,
inductive relation and literal 452-byte historical image prediction still run.
Removing the last GLOBAL_ASM changes this owner's natural Make recipe from
five commands to three. The shared fixture derives recipe membership from
the proposed source; only historical proposals with different membership use
Make's GLOBAL_ASM_C_FILES override. The installed C uses the unmodified natural
three-command recipe. The historical renderer retains its five-command route.
Both routes produce their independently expected complete objects. The first
installed run exposed the obsolete five-command fixture assumption; the fixed
14-test suites were rerun in both configurations before and after adoption.

The fresh complete ELF matches the frozen baseline with **zero changed bytes,
zero exclusions**, all **6,051 slots/addresses** and **189,088 protected data
bytes** retained. Exactly one conversion CSV row changes from asm to c; old
guard bytes remain an exact prefix. All **2147 frozen inputs**
are checked against the explicit task plan. ELF SHA-256 remains
`733102bfb973c3af410d3b3722a64132f475425a990877112eccc893b8ad239a`.

Graphify is refreshed with scoped AST/references and old-node/qualification
retention, observing commit-hook writers before the final merge. Native graph
updates remain subject to the shrink guard; no full-corpus reextraction is
claimed. No Claude call, push, host build, save or frozen Release change occurs.

Reproduce from the prepared consumer root:

```sh
python3 -m unittest tools.tests.test_game_list_unlink_1517e134_match -v
python3 -m unittest tools.tests.test_game_list_render_1517e28c_match -v
make tools-check
make -C conker -j4 build/conker.us.elf progress.csv
```

Next: qualify the remaining zero-return draw helper `func_1517E4A8`, preserving
the completed list unlink/renderer/projection/depth routines. The private next
audit verifies its complete **361 words / frame 184**, VA
`0x1517E4A8..0x1517EA4C`, ROM `0x1AB958..0x1ABEFC`, and seven-argument caller.
It records one direct JAL at `0x1AB8F8` and no aligned literal pointer.
`func_15095A48` currently has a void C wrapper even though this original caller
consumes V0; qualify a typed return repair and that helper owner's neighbors
alongside the packet layout, constants and palette bounds. This next audit has
no matching credit; semantic C still needs compilation and all adoption gates.
