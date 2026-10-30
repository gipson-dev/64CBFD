# 1858: Live resource-pair release restored from exact C

Verified 2026-10-30. `func_150843AC` is restored in `conker/src/game/generated_AEB40.c` with its original symbol name and a semantic release comment. Tools commit: `52cfcfec41155be1670c55d0da24d8ced89a0d39`; the consumer records that pin. No push.

The routine selects two resource pointers at `record+0x28C+slot*8` and `record+0x290+slot*8`. If both are null it returns before reading the identity list. Otherwise it captures the unsigned identity byte from the list at `record+0x2C4`, then visits both live resource slots. A non-shared resource is released through `func_100043B4(resource,3)`; a shared resource decrements its byte reference count. Each visited non-null slot is cleared after its release/count update. The captured identity survives helper calls, while the next slot and shared-resource globals remain live.

All **55 words / 220 bytes** emit directly from C, including the original unreachable duplicate load at offset `0x9C`. The original **48-byte frame**, RA at44, S5..S0 at40/36/32/28/24/20, and five relocation bindings are preserved. No guards, omitted words, insertions, frame changes, new compiler profile or shared-header edits. The old `s32 func_150843AC();` owner declaration is corrected to `void func_150843AC(u8 *, s32);`; it earns no extra matching credit.

The owner retains its existing `jtbl_8009CC40_game` rodata anchor. All **30 neighboring functions** and normalized pools are unchanged, and the actual **five-command Make recipe** reproduces the qualified object with zero C diagnostics. The inherited duplicate `12D630` Make recipe warning remains outside this change.

Validation:

- **6,192 guest cases / 18,576 executions** compare original assembly, fresh compiler output and padded output, including all256 identity-byte values, null pairs, modulo-byte counts, helper mutations, two stack phases and guest-only extreme slot words. Literal machine state and memory agree. All54 reachable words are exercised; a static no-branch-target proof accounts for the preserved unreachable word.
- **64 interrupted access prefixes**, **54 cases across three rebased binding layouts**, and **12 count-byte/pair-word alias cases** preserve literal state.
- Two original caller windows each pass36 cases: `1508437C..15084388` supplies the owner through S2 and slot through the S0 delay instruction; `15084B3C..15084B44` starts with the owner already in A0 and supplies the slot from S0 in the delay slot. Complete parent routines and the release helper's original instructions are not claimed.
- Native32 **2,573 cases per profile** pass at `-O0`, `-O2` and `-O3` with UBSan and nine effective negative controls. The portable domain uses valid aligned owner/list/resource storage, slots0/6, identity0..186 and static addresses with bounded signed32 arithmetic. Native test backing is256 entries to keep controls defined. Extreme guest slot words and deliberate guest aliases are not portable-C claims. Tests check all owner fields, fourteen resource pointers, both lists and all table/count backing entries.
- Both tools copies independently execute all eight canonical checks and their repository tool checks. Each installed copy freshly checks source/input identity and strict linked/protected data, reusing six unchanged checks only under complete module/artifact/input fingerprints.
- Independent whole-image prediction equals the production ELF byte-for-byte: **172 changes =171 target code bytes +1 target extent byte**, metadata0 and exclusions0. All **6,055 other linked bodies**, all function addresses and **189,088 protected Game bytes /720 owners** are unchanged.

The adopted ELF SHA256 is `a93e110f4776e19e1415de9eb0855e29dac775c0d794c8dce68cb8521b75917a`; qualified object SHA256 is `20267693a030f4200ea4259a1c9f8ee36d5a572dec82d84280e14f1a03816a73`.

Actual-ELF recount: **3,935 /5,506 exact C (71.47%)**, Game **3,262 /4,833 (67.49%)**, Init492/492, Debugger181/181, zero address drift. **195** further exact C functions reach4,130/5,506 (75%). Inventory CSV and all inherited guards remain unchanged. Private parked candidates are uncredited; `func_150A2864` is the next screen, not a qualified adoption.

Graphify uses an explicit eleven-file AST refresh with old-node and still-valid relationship retention. It records the recovered void signature, live resource lifetime and both original call windows. One obsolete s32 return relationship is retired. Historical corpus rows and communities remain historical; this is not a full-corpus extraction or gameplay validation.

Local evidence remains under `conker/build/game-resource-pair-release-match/`, including frozen inputs, selected raw objects, Make command evidence, canonical receipts, production proof, actual-ELF queue, graph retention audit and final banking audit. The older tools mirror's inherited2012 dirty paths remain preserved; the three new matching modules are mirrored without committing that older checkout.
