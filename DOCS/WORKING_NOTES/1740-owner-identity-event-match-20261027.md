# 1740 - Owner identity-event callback match

Verified 2026-10-27, following [Note 1739](1739-owner-radial-height-match-20261026.md).

## Result

Replaced the zero-return placeholder for `func_151D08F0` in
`conker/src/game/generated_1FA770.c` with its semantic owner/event callback.
Its complete 184-byte / 46-word retail body now matches at VA
`0x151D08F0..0x151D09A8`, ROM `0x1FDDA0..0x1FDE58`.
The routine retains its 24-byte frame, saved RA lifetime and full incoming
third-argument home. One expected-word guard commutes a comparison's operands;
no instructions are inserted or omitted.

This remains the existing C inventory row, so converted function/byte totals
do not change. The actual adopted Native ELF recount is **3,817 / 5,506 exact
(69.32%)**, Game **3,144 / 4,833 (65.05%)**, Init 492/492 and Debugger 181/181.
Address drift is zero; 1,689 C functions differ. The 75% threshold stays 4,130,
requiring **313 more** exact functions. The wider goal is still open.

## Recovered behavior and interfaces

The actual 74-entry registry `D_8008A8D8` registers this function at slot 49
(literal ROM `0x22F45C`). The complete 23-word dispatcher `func_15149434`
uses the callback interface `void(struct260 *, s32, u8)`, clamps invalid
selectors to the NULL slot and masks the command byte before the indirect call.
The restored definition uses that typed callback interface. Its retained release provider is `void func_1516972C(struct102 *)`.
The existing call in `func_151D0ED8` receives a proper pointer cast with no
word changes. Shared headers are unchanged.

- Commands 0 and 0x18 release the owner if either its embedded identity word or
  identity byte matches the event record.
- Command 0x2D retargets the embedded word/byte pair. The first identity match
  takes priority when both event identities match; the two paths use event
  byte 9 and byte 8 respectively.
- Other commands leave packet/owner storage untouched, including sparse guest
  mappings where those objects do not exist.

The original and retained 28-word release helper are connected in guest
checks; its actual C body is also used in native32 tests. Large bookkeeping,
callback and other-provider bodies remain bounded contracts. This is not a
claim of whole-parent gameplay, hardware or interrupt acceptance.

## Guard and complete-owner preservation

Raw selected C is 46 words with one `R_MIPS_26` binding at +0x50 to the
release helper. The only guard is at +0x94:

| Offset | Expected | Retail replacement | Reason |
| --- | --- | --- | --- |
| 0x94 | 0x548A0005 | 0x55440005 | Commute the two BNEL comparison registers; retain opcode, displacement and delay-slot behavior.|

The entire raw body and relocation map are pinned before this transformation.
The actual padder rejects altered expected words, bindings, extents, offsets,
repeated application and changed guard history. Six independent GNU links over
three address layouts agree with original assembly and preserve the call
binding. Guest rebases include 768 cases per tools copy.

All 51 other functions and normalized pools in this generated owner are fixed.
The normal O2/g3 three-command Make route reproduces all 52 compact functions
and the complete padded object. Eight inherited CFE Warning 712 diagnostics
are identical before/after; isolated target diagnostics are empty. Existing
duplicate generated_12D630 Make recipe warnings remain separate.

## Qualification and adoption evidence

Both primary and independently dirty older tools copies passed eight fresh
canonical methods with zero errors, failures or skips (88.389s / 88.600s).
Both shared tools checks passed. Coverage per copy includes:

- 9,728 command/key/pattern/alias guest cases, all command/key bytes, full
  incoming command homes and nine alias layouts. 44 reachable instructions are
  exercised; the two original unreachable words are preserved literally.
- 64 original/retained release-helper cases and 12,288 complete original/retained
  dispatcher cases over all selector and command bytes.
- Native32 O0/O2/O3, 786,432 target and 131,072 dispatcher cases per profile,
  ten effective semantic controls, typed function-pointer dispatch and trapping
  UBSan. These fixtures allocate typeless heap storage for the actual 32-bit ABI.
- 64 actual guest fault prefixes, ignored-mode lazy mapping, and effective
  compiled MIPS controls for early reads, caller bounds and NULL calls.
- Eight guard/input/padder negative controls, six GNU links, seven strict-image
  corruptions and three wrong-input controls.

The sealed set contains 16,127 Native inputs and 76 focused frozen inputs. The
ordinary production Make completed in 0.484 seconds and reproduced the independent
complete-image prediction exactly: **128 changed bytes = 127 target code + 1
symbol-size byte**, **zero exclusions**. All 6,056 function addresses and all
6,055 other function bodies remain fixed. Protected Game data stays exact across
720 owners / 189,088 bytes, SHA256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

After installation each tools copy ran two fresh owner/image methods; the six
unchanged semantic methods were reused only after exact snapshot, module and
qualified-artifact fingerprint checks. Their earlier fresh executions remain
preserved. Five adopted outputs are source, guard manifest, target object,
complete ELF and map. Progress CSV bytes and the inherited guard prefix are
unchanged. Recount reads the captured, actually adopted Native ELF, not an
isolated body or projected increment.

| Artifact | SHA256 |
| --- | --- |
| Tools commit | 639a115cee651280c544cdd2886eb41bacae4ade|
| Adopted ELF | 86c5549e999b5bb3262b5513195b892c8e3c04a153cae3e95ea4a57cc765c30d|
| Recovered owner source | 30e0caea0bad63e95f83e3c77ba683c45588d799e01707c1bfe5a5ba51bcb6ab|
| Padded target owner object | 87781ccd6e553d24c7287620a822c7048e2be94f8f98e74d6459f03cc57af624|
| Raw selected C payload | 4bcf1eced66a0a3fea23f9f60bd95cd4d88ff99b88bd2544fe074885f3432c64|

Receipts, original failed WSL startup attempts and fresh resumed executions
are in `conker/build/game-owner-identity-event-match/`. The explicit resumed
qualifier archives prior receipts instead of relabeling failed attempts as
passing. Existing IDO/binutils/GCC were reused; no compiler installation or
host-port/Release changes were needed. Codex owns implementation and review;
Claude calls: 0 for this routine recovery.

## Next boundary

`func_150222E0` / `generated_49D30` remains a private, uncredited candidate.
Its original guest semantics and supplemental Win32 C checks are recorded
separately. Use the actual O2/g3/no-unroll compiler profile and preserve its
actor pointer across the five-argument callback. Isolated byte matching alone
does not close complete-owner, caller/ABI, guest/native, real Make/padder,
independent image, production adoption and documentation gates.

Refresh the changed C/Markdown sources and the two committed tools modules
with scoped AST extraction. Preserve old nodes and valid edges; historical
communities/centrality remain historical rather than a full-corpus analytics
claim. Keep function narratives out of the root README; its updates are the
verified date and aggregate rows only.
