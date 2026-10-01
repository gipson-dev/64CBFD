# Init channel event and timer updater match

Date: 2026-10-01

`func_1000CEAC` occupies 275 words and 1,100 bytes at
`0x1000CEAC..0x1000D2F8`. Its previous compiled body returned zero even though
the three-channel audio coordinator calls it once for every active channel.

The recovered routine selects the channel's audio root and drains its
24-byte message queue without blocking. Event messages use the low three bits
as a selector and bit `0x10` as the timer-update class. Selectors zero and one
refresh the channel timing state. The selected 16-bit event mask then updates
as many as sixteen slots using the root's mode table: modes zero and one
toggle phase flags and schedule countdowns, mode two updates the paired low
and high slots, and the default mode enables and schedules the slot. Non-timer
messages retain the global event callback path.

After the queue is empty, the routine synchronizes the low-level voice with
the root's active state and records status bit `0x80` when appropriate. Its
final two-at-a-time loop decrements all sixteen countdowns using the current
frame step and clamps expired values to zero.

The semantic C emits the exact 275-word extent and preserves the retail branch
graph, queue calls, mode behavior, and paired countdown loop. Two hundred
thirty function- and offset-scoped guards normalize the remaining closed IDO
register-allocation, frame-layout, and scheduling differences. Forty-one rows
declare source and retail relocations explicitly; 45 words emit directly from
the recovered source.

The targeted object rebuild accepts every expected word and relocation, and
the complete linked ELF no longer lists `func_1000CEAC` as non-exact. Direct
comparison of `0x1000CEAC..0x1000D2F8` reports zero different bytes. Both
1,100-byte spans share SHA-256
`3dd80b02cc6d85f41dedfcb2f18b5e7997d72a2f4370377755a16e75142f3618`.
The clean repository rebuild, `make tools-check`, all 11 focused tool unit
tests, and `git diff --check` pass.

The matcher advances to `3,156 / 5,456 (57.84%)` byte-exact C functions
overall and `473 / 487 (97.13%)` in Init, with zero address drift and 14
different Init C rows. The next smallest measured Init candidate is the
296-word `func_1001FB40`, currently different in 274 words.
