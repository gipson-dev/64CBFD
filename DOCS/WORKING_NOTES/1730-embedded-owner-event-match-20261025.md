# 1730 - Embedded Owner Pointer Event Match - 2026-10-25

The actual adopted Native ELF measures 3,806/5,505 exact C functions (69.14%),
Game 3,133/4,832 (64.84%), zero address drift and 1,699 different. Only
`func_150D7068` gains credit; 323 more matches reach the current 75% threshold.

## Recovered routine and interface

`func_150D7068`, generated owner `generated_1028F0`, occupies VA
`0x150D7068..0x150D7120`, VROM `0x104518..0x1045D0`: 43 body words,
three preserved alignment words and a 24-byte frame. It replaces the complete
12-byte zero-return stub with semantic C. The existing `EmbeddedOwnerLink`
pointer view is reused without duplicating its declaration. Pointer and identity
fields reside at owner `+0xA8` and `+0xAC`; all neighboring definitions remain intact.

The canonical callback signature is `void(u8 *, s32, u8)`. The
existing release declaration remains `void func_1516972C(struct102 *)`; its
call uses an explicit owner cast. No shared header or compiler profile changes.

Command `0x2D` captures the current owner pointer and the first event pointer.
A first-pointer match writes event pointer `+4`, then reads identity byte `+9`;
otherwise a second-pointer match writes the captured first pointer, then reads
identity byte `+8`. First-match priority and the late identity reads remain
observable under overlaps. Command zero releases the owner when its pointer
or saved identity matches; the event identity byte `+4` overlaps the second
pointer view. Other commands perform no packet or owner loads in emitted guest code.

The sole retail literal registration is index 9 of the 14-entry `D_80089878`
table, at VA `0x8008989C`, VROM `0x22E35C`. There are no direct call sites.
The complete original and retained 22-word `func_15131C2C` dispatcher is
covered, including command byte masking, owner flag 0x4000, selector +0x75,
NULL skipping and every valid provider slot. It has no range clamp. Disabled
flag tests cover every selector byte without packet or table mapping; an
enabled out-of-range selector is checked as a guest access fault.

The body differs from the previously qualified `func_150AEDF8` only at words
9 and 28, whose owner address immediates change from `0x28` to `0xA8`. Those
address words emit directly from C. The owner, caller registration, generated
Make recipe and production image are independently qualified for this target.

## Guard derivation and preservation

All 43 body words, the 24-byte frame and one `R_MIPS_26:func_1516972C`
binding emit from complete C. Eleven expected-word guards derive a closed
current/first-pointer register exchange, an independent release-read swap and
commutative comparison operands. No instruction is inserted or omitted.
This is a guarded C match, not compiler-only matching.

All 16 raw/padded neighboring functions, their bindings and private pools
remain identical, including all six `GLOBAL_ASM` routines. The actual Make
recipe executes five commands: assembly preprocessing, normal `-O2 -g3`
compilation, assembly postprocessing, generated-object padding and assembly.
Its complete padded object equals the independent qualification object.

The first private run stopped when the generated padder was passed a layout
manifest instead of `asm/1028F0.s`. The corrected run completes the real padder, Make and full-link gates. The
first caller fixture then correctly rejects an unrelated registration assumption.
That failed experiment is preserved separately. A fresh 60-input snapshot, real
caller and corrected u8-pointer signature are recompiled and fully qualified;
no old ABI or caller execution is reused and no metadata is excluded.

## Behavioral qualification

Both tools copies pass eight fresh private checks. Canonical acceptance records
their actual private execution phase and exact module/snapshot/artifact identity.
After production each copy runs two fresh installation checks and reuses six
unchanged semantic checks through that complete fingerprint. Shared tools checks
pass in both copies.

- 7,168 guest cases cover all command/key bytes, full incoming command homes,
  first-match priority and nine overlap layouts. Raw C public semantics and
  fitted complete state agree. Forty-two instructions are reachable; original
  duplicate load word 19 remains present.
- Thirty-two cases execute all 28 original/retained release-helper words,
  including the kind reload after bookkeeping mutation.
- 9,040 original/retained dispatcher cases cover all selector/command bytes,
  all valid table entries, disabled flags and bounded provider clobbers. A positive
assertion requires actual target dispatches, rather than incidental provider tests.
- SDK/native32 O0/O2/O3 each pass 786,434 target and 138,240 dispatcher cases
  with trap UBSan; twelve compiled semantic negatives are effective. Pointer
  fields use pointer-typed values copied into heap storage through memcpy,
  not incompatible integer lvalue stores. The overlapping matrix uses pointers
  into the allocated arena; two separate nonoverlapping NULL cases are checked.
- Fifty-nine fired guest access-fault prefixes compare complete states. Ignored
  commands require no owner/packet mapping in guest tests. Compiled early-read,
  dispatcher-flag and NULL-call negative controls are effective.
- Nine independent GNU links cover original, normalized and raw bodies across
  three layouts. All 43 raw-word, binding, extent/history, actual padder and
  seven strict-image corruption controls reject changed inputs.

Sparse invalid pointer words, incoming high command bits and access-fault
prefixes are guest evidence. Native tests do not claim portable C fault behavior.
Bookkeeping/callback/fallback and other dispatcher providers are bounded
contracts. Full provider, hardware and gameplay acceptance remains separate;
the retained dispatcher and release helper receive no new matching credit.

## Production and sealed inputs

Independent and production links agree on ELF `d657fc688a62a3883830cf9a96a59ef95eba3318594c684e5be97a4a032be72f`. The exact delta is
119 bytes: 118 target code bytes and one target symbol-size byte, zero exclusions.
Actual Make exits zero in 4.252s. All 6,055 function addresses and
6,054 other function bodies remain fixed. All 720 Game data owners / 189,088
bytes remain exact, SHA
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.
The inherited duplicate generated_12D630 recipe warning remains unchanged.

Source SHA: `c5713d2c7b97a536fb4f8d67a70ba8989b1e9345b1ffb11676021a69daa9b142`.
Guard CSV: `0fc7da71a110d7ab703aa7ea98374fe69f6fddb14ad87b46e0085b82c0d4815e`.
Padded object: `dcc69a1370a42971d9255629d671b01db1b6ddb2adfdf4085d8eb1e579f9d117`.
Raw body: `22471dd83799f7b60af6f806deb10b9fba3de9c40e6a42ef26efe476f9fcd6e0`.

Baseline consumer `104e4f26`, tools `2bb4d786`, Native ELF `a27dd649`.
All 16,086 current inherited/owned files and 60 focused inputs are sealed.
The older mirror preserves all 1,670 existing dirty paths and its history;
only this target pair is added there. Tools `bed7f692eb0473cd8da281fedbbe7e1416019833` are committed first.
Native adoption verifies the complete seal before/after exactly four source,
CSV, object and ELF changes. Recount classifies those actual Native ELF bytes.

The scoped graph closeout refreshes eight changed C/MD files and must retain
or uniquely relocate all 44,264 previous nodes. Historical manifest freshness
outside that scope is preserved. Tools AST extraction is separate because the
parent ignores `tools/`; no full-corpus extraction is claimed.

## Continuation

The ELF-pinned queue contains 1,570 placeholders, 120 semantic/other definitions
and nine unlocated screens. Continue with `func_1510F820`, generated owner
`generated_13BB20`. Its actual body has 43 words; the 46-word queue extent
also covers the following three-word `func_1510F8CC` leaf, which is absent
from the current progress CSV. Audit that inventory/neighbor boundary first.
The private normalizer probe is within one body word, but remains uncredited
until source/ABI, owner, guest/native, Make and full-image gates pass. Keep
the 75% goal active. Routine Claude calls: zero. No publication or host-port work.

Prepared-checkout focused command:

```sh
python3 -m unittest tools.tests.test_game_embedded_owner_event_match -v
```

Keep raw objects frozen between executions. A new compilation requires new
fingerprints; compiler debug metadata is included in the strict image audit.
