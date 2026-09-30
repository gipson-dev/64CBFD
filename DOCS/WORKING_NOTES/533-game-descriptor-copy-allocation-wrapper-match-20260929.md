# Game descriptor-copy allocation wrapper byte match

Date: 2026-09-29

`func_15157898` occupies 32 words and 128 bytes at
`0x15157898..0x15157918`. It forwards eight construction parameters to
`func_15157010`, adding `0x38` to the incoming auxiliary pointer. On success it
copies the separate 56-byte descriptor to returned-object offset `0x120` and
returns the object; allocation failure returns zero.

Typing the floating argument as `f32` restores retail's `mtc1`/`mfc1` forwarding
sequence. The direct call, null branch, and conditional `memcpy` emit all 32
words from C with no expected-word guards.

Verification: the full non-matching link succeeds; the matcher reports
`3,037 / 5,463 (55.59%)` overall and `2,459 / 4,789 (51.35%)` in Game with no
drift. The linked Game span at `0x157898` and retail ROM span at `0x184D48`
share SHA-256
`2b6f5e119f028f88171da469e55663785d9b29990910dd5d10dc1f2de93a07db`.
`make tools-check` and all 10 tool unit tests pass.

Resume with Game `func_15172CA8`, the next ordinary 32-word matcher row. Keep
the four documented special-case rows parked.
