# 1729 - Inline Owner Identity Event Match - 2026-10-25

The adopted Native ELF now measures 3,805/5,505 exact C functions (69.12%),
Game 3,132/4,832 (64.82%), zero address drift and 1,700 different. Only
`func_150AEDF8` gains credit; 324 more matches reach the current 75% threshold.

## Recovered routine and interface

`func_150AEDF8`, ordinary owner `game_DBA60`, occupies VA
`0x150AEDF8..0x150AEEB0`, VROM `0xDC2A8..0xDC360`: 43 body words,
three preserved alignment words and a 24-byte frame. It replaces a 12-byte
zero-return placeholder and removes the old misleading commented pseudocode.

The recovered signature is `void func_150AEDF8(struct260 *record,
s32 eventAddress, u8 command)`. The existing common owner header matches the
real dispatcher callback interface. A local `InlineOwnerIdentityDBA60` view
exposes only the identity word at owner `+0x28` and saved key at `+0x2C`.
The existing typed release interface is preserved through `functions.h` and
an explicit `struct102 *` cast; no shared header or compiler profile changes.

Command `0x2D` captures the current identity and first event word. A first-word
match writes event word `+4`, then reads key byte `+9`; otherwise a second-word
match writes the captured first word, then reads key byte `+8`. First-match
priority and the late key reads remain observable under overlaps. Command
zero releases the owner when either its identity or saved key matches. Its
key comes from event byte `+4`, which overlaps the second-word view. Other
command bytes perform no packet or owner loads in emitted guest code.

The sole retail literal registration is slot 39 of the 74-entry table
`D_8008A8D8`, at VA `0x8008A974`, VROM `0x22F434`. There are no direct call
sites. The complete 23-word original and retained `func_15149434` dispatcher
is covered, including byte masking, range/NULL gates and other provider slots.

The 172-byte retail body is identical to the previously qualified
`func_151B1FAC` body, SHA
`f48e9051f177cb1bbaadfc59ab1437196177a8904ce2fe99da5b18f934111993`.
This allows reuse of its semantic shape and domain helpers while separately
qualifying this owner, alignment, registration and whole-image installation.

## Guard derivation and owner preservation

The complete C emits all 43 body words, the original frame and one unchanged
`R_MIPS_26:func_1516972C` binding. Eleven expected-word guards derive a closed
current/first-word register exchange, an independent release-read swap and
commutative equality operands. No instruction is inserted or omitted, and
no frame, lifetime, opcode or branch shape is manufactured. This is a guarded
C match, not compiler-only matching.

All seven raw and padded neighboring functions, their bindings and pools
remain identical. This plain-C owner has no `GLOBAL_ASM` routines. Its actual
Make recipe has three commands: normal `-O2 -g3` compile, ordinary C padder
and assembler. The first private attempt correctly rejected an inherited
five-command fixture assumption. The corrected three-command gate preserves
the already qualified raw objects; their exact bytes are not recompiled.

## Qualification and execution reuse

Both tools copies pass eight fresh private checks, zero errors, failures or
skips. Primary test execution is 471.988s (488.977s including resumed preparation);
the mirror executes its suite in 347.077s. These actual private executions are
accepted into the canonical checkpoint only after proving exact module,
snapshot and artifact identity. Their original receipts and execution phase
remain explicit; they are not silently rerun or described as later executions.

After production, each copy executes two fresh installation checks and reuses
six unchanged semantic checks through the complete fingerprint. Current source,
guard CSV, padded object, ELF, other inputs and all seven frozen artifacts are
checked. Shared tools checks pass in both copies.

- 7,168 guest cases cover all command/key bytes, full incoming command homes,
  first-match priority and nine overlap layouts. Raw C public semantics and
  fitted complete state are checked independently. Forty-two instructions are
  reachable; the original duplicate load at word 19 remains present.
- Thirty-two cases execute all 28 original/retained release-helper words,
  including the kind reload after bookkeeping mutation.
- 10,752 original/retained dispatcher cases cover all selector/command bytes,
  actual table entries, skipped calls and bounded provider clobbers.
- SDK/native32 O0/O2/O3 each pass 786,432 target cases and 131,072 dispatcher
  cases with trap UBSan. Twelve compiled semantic negatives are effective.
- Fifty-nine fired guest access-fault prefixes compare complete states.
  Ignored commands require no owner/packet mapping in guest tests; a compiled
  early-read control fails, as do altered dispatcher bound and NULL controls.
- Nine independent GNU links cover original, normalized and raw bodies across
  three layouts. Forty-three raw-word, one binding, extent/history, actual
  padder and seven strict-image corruption controls reject changed inputs.

Native fixtures use valid heap-backed storage and canonical function-pointer
types. Sparse invalid addresses, full incoming words and fault prefixes are
guest evidence, not portable C fault guarantees. Bookkeeping, callback and
fallback providers are bounded contracts. Full provider, hardware and gameplay
acceptance is separate; the retained caller/helper receive no new credit.

## Production image and sealed inputs

Independent and actual production links agree on ELF
`a27dd64990036c4f5002b03605985a2a1e97cd697876e3fcd1191ad671540ac9`.
The exact delta is 119 bytes: 118 target code bytes and one target symbol-size
byte, with zero exclusions. Actual Make exits zero in 5.964s.
All 6,055 function addresses and 6,054 other bodies remain fixed. All 720 Game
data owners / 189,088 bytes remain exact, SHA
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.
The inherited duplicate generated_12D630 recipe warning remains; no new target
compiler diagnostics are introduced.

Source SHA: `50bfc576a4bc20083bb16662c15bd448dfaa3fadcd3736634c7395a91e89d9dd`.
Guard CSV: `132fa27cc944fc9444479b16ae8a07f5ff11b2a7fec9e119dc292c555358e149`.
Padded object: `94c113dc7682966c88610531a36e92d07a5a26c479fa81f3125dded1132fac07`.
Raw code: `c85a7adaeb83153172857e9ba8072d604a6cc280a4d393976cdd93d92eef2f35`.

Baseline consumer `f49699ea`, tools `e338265`, Native ELF `08f3110e`.
All 16,082 current inherited/owned files and 55 focused inputs are sealed.
The older mirror's 1,668 preexisting dirty paths and history are preserved;
only this pair's two new files are added there. Tools `2bb4d786d9260756b188c9bd4db32f4f339b149e` are committed
first. Native adoption verifies the complete seal before and after exactly
four source/CSV/object/ELF changes; recount uses those actual Native ELF bytes.

The scoped graph closeout refreshes eight changed C/MD files and must retain
or uniquely relocate every one of the 44,255 previous nodes, preserving
historical freshness outside that scope. Tools AST extraction is separate
because the parent ignores `tools/`; no full-corpus extraction is claimed.

## Continuation

The ELF-pinned queue now has 1,571 placeholders, 120 semantic/other definitions
and nine unlocated screens. Continue with `func_150D7068`, owner
`generated_1028F0`. Its private 43-word/46-slot candidate fits the same eleven
role guards after the two inline-address offsets change to `0xA8`; source/ABI,
owner, guest/native and production qualification are still required. It is
uncredited. Keep the 75% goal active. Routine Claude calls: zero. No host port,
editor, Release or publication work is included.

Prepared-checkout focused command:

```sh
python3 -m unittest tools.tests.test_game_inline_owner_identity_match -v
```

Keep raw objects frozen between executions. A new raw compilation requires
new fingerprints; compiler debug-byte changes are not excluded.
