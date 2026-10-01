# Init three-channel audio-mix coordinator match

Date: 2026-10-01

`func_1000D758` occupies 133 words and 532 bytes at
`0x1000D758..0x1000D96C`. The former implementation was empty. The recovered
routine coordinates the three active audio records before updating each
channel for the current frame.

When audio processing is enabled, the routine scans `D_800417B0` and classifies
each valid record from its `D_8002B074` command flags. Four three-bit masks
track flag `0x40`, command type 5, types 3/4, and types 1/2. Type 5 receives
the highest-priority channel policy, followed by types 3/4. The fallback path
uses types 1/2 only for audio mode 1 and the accepted level ranges; otherwise
it restores the default channel mask.

After selecting the mix, the routine calls `func_1000CEAC` for channels zero
through two, then forwards the frame's two float values and integer mode to
`func_1000D2F8` for the same three channels. Their local declarations now
express those argument contracts, but both callees remain separate nonmatching
rows and are not claimed complete here.

The recovered C reproduces the complete frame, branch graph, calls, constants,
loops, and 133-word slot. It emits 112 words directly. Twenty-one
stale-checked rows normalize one closed IDO register-allocation cycle in the
record-classification loop and its reused mode constant. Four rows retain the
original `D_800417B0` and `D_8002B074` HI16/LO16 relocations.

The complete ELF link passed after a full stale-check rebuild. The
authoritative matcher no longer lists `func_1000D758`; the linked and retail
532-byte spans share SHA-256
`9dc672958d710f32ad34fd9e7b08f3b4059ded72a7e096e7ce7438440241852c`.
Project tool checks and all 10 tool unit tests pass.

The matcher advances to `3,134 / 5,457 (57.43%)` overall and
`451 / 488 (92.42%)` in Init, with zero address drift and 37 genuinely
different Init C rows.
