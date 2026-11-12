# Linked-actor transform byte match

Date: 2026-11-11. `func_15102D90` replaces the zero-return placeholder in
`conker/src/game/generated_12FDD0.c`; the retail assembly is in
`conker/asm/12FDD0.s`. Its 74-word retail body spans VA
`0x15102D90..0x15102EB8`, ROM `0x130240..0x130368`.

The typed C routine clears a status bit, validates a linked actor's identity
and active state, and transforms two vectors through either an optional
descriptor or the actor's matrix. It sets the bit after a successful transform;
an absent matrix or excluded actor mode returns success without transforming.
The declarations use the project actor, descriptor and vector types and the
existing helper signatures.

The compiler emits 73 raw words. **64 expected-word guards and one inserted
instruction** normalize the body and relocation bindings to the 74-word
retail function. This is a guarded, not an unguarded, C match.

Retail and raw C guest executions agreed across 2,048 cases and visited 72 of
74 retail words. SDK32 native O0/O2/O3 each passed those cases and nine
negative controls with undefined-behavior sanitization. The original
`func_1513CFE4` caller window passed 4,096 cases via `D_80089CB8[41]`; all
three helpers were modeled, and the full parent and helper implementations
were not qualified. The tests use valid, aligned, disjoint owner, actor,
matrix, descriptor and stack regions; arbitrary aliases, concurrent mutation
and native or hardware faults are not qualified.

Both padders agree with independently assembled retail code and bindings;
12 rebased GNU links, 112 bounded access-cut triples and 128 corrupted-guard
rejections pass. Actual Make and strict independent image comparison account
for **226 changed bytes** with zero exclusions. All 6,050 function
addresses, five neighboring functions and 189,088 protected data bytes remain
unchanged. Actual ELF SHA-256: `ea6052e46286c5531636a22aec8f171a5f9cd325620ccb159c1d3ec173e5bf6a`. The existing
complete-ROM checksum mismatch remains.

Fresh actual ELF recount: **4,347 / 5,513 (78.85%)** overall and **3,674 /
4,840 (75.91%)** Game, zero drift and 1,166 different. The 80% target needs
64 more exact functions. Tools commit `94ffa0db0c70264bf3b676546f6a444b4fee1fe1`
precedes the consumer change.
