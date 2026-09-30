# Game fixed-payload object spawn byte match

Date: 2026-09-29

## Scope and behavior

`func_1514D978` in `conker/src/game/generated_179F30.c` occupies 31 words and
124 bytes at `0x1514D978..0x1514D9F4`. It constructs a 32-byte payload with
seven zero words and `12.0f` at offset `0x10`, allocates an object through
`func_15158BD0`, copies the payload to object offset `0x58`, and registers the
result with tag `0x13` when allocation succeeds.

## Source recovery

The previous body was a false zero-return placeholder. The recovered source
uses an eight-word local payload and the allocator/copy/register pattern
already established by adjacent helpers in the same slice. Declaring the
payload before the result pointer preserves retail's result spill at stack
offset `0x1C` and payload base at `0x20`.

IDO reproduces retail's 64-byte frame, payload initialization order, floating
store in the allocator-call delay slot, null gate, 32-byte `memcpy`, result
spill/reload, registration call, and epilogue directly from semantic C. No
expected-word guards are used.

## Verification

- The focused `generated_179F30` object reproduces all 31 retail words.
- The linked ELF and outer non-matching build pass.
- The authoritative matcher reports `3,021 / 5,463 (55.30%)` overall and
  `2,443 / 4,789 (51.01%)` in Game, with zero address-drift rows.
- Direct comparison reports zero differences across all 124 linked bytes.
- Both spans share SHA-256
  `88988aac1c2edc8f456aa37224844513cc58ef01dd750e045a040b8266ee8b3c`.
- `make tools-check` and all 10 tests under `tools/tests` pass.

## Resume boundary

Inspect `func_15183974` as the next ordinary 31-word Game candidate.
`func_15106E78` has recovered destructor semantics but is parked because
natural C emits 30 words with a saved `$s0`, while retail emits 32 words using
a caller-saved `$a1` spill cycle. Keep `func_15015F40` parked behind unresolved
indirect-table ownership and `func_150A76F0` in the handwritten-assembly queue.
