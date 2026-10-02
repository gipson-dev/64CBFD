# Init formatted-output dispatcher match

Date: 2026-10-01

`func_100020D0` occupies 402 words and 1,608 bytes at
`0x100020D0..0x10002718`. Its former C placeholder was empty and omitted the
SDK-style formatted-output parser used by `func_10002088`.

The recovered routine scans literal runs and submits them through the caller's
output callback. For each conversion it recognizes the retail flag string
`" +-#0"`, parses direct or `*` width and precision values from the aligned
argument cursor, accepts `h`, `l`, and `L` length modifiers, and folds `ll`
into the retail `L` representation. Negative dynamic width enables left
alignment exactly as in the assembly.

`func_10002718` receives a 0x38-byte conversion descriptor and a 44-byte local
buffer. The dispatcher then emits right padding, prefix bytes, leading zeroes,
the main converted payload, middle zeroes, suffix bytes, trailing zeroes, and
left padding in retail order. Space and zero runs are capped at 32 bytes per
callback. A zero callback result returns the number of bytes accepted so far.

IDO emits a 361-word compact body from the semantic C. Ninety-five words match
retail directly. The remaining closed frame, register-allocation, branch-shape,
and scheduling difference is represented by 266 function-scoped,
stale-checked rows. Forty-four rows insert retail words, three omit compact-only
words, and ten validate relocation-bearing calls and data references.

The padded-object and linked builds pass, and the matcher no longer lists
`func_100020D0`. Direct comparison of `0x100020D0..0x10002718` reports zero
different bytes. Both 1,608-byte spans share SHA-256
`fbc33626d707e258fdce37f95a3d2c5a989c31b39ee14a00d1db74d7b7f00dfa`.

The matcher advances to `3,165 / 5,456 (58.01%)` byte-exact C functions
overall and `482 / 487 (98.97%)` in Init, with zero address drift and five
different Init rows. The next smallest measured Init candidate is the
422-word `func_10002718`, currently different in 418 words.
