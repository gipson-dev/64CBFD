# Game object-request builder match - 2026-09-28

## Result

`func_1514F5CC` is byte-exact across its complete 29-word, 116-byte retail span
at `0x1514F5CC..0x1514F640`.

The fresh linked matcher reports 2,884 / 5,466 (52.76%) exact C functions
overall and 2,310 / 4,790 (48.23%) in Game, with one address-drift blocker and
2,581 genuinely different C rows overall.

## Recovery

The function constructs a 28-byte request on the stack. It clears the opening
word and float, stores the caller's object pointer and the object's byte ID at
offset `0x3B`, copies `D_800A5E5C` into the request parameter, and sets signed
count `20`, signed size `0x12C`, and mode byte `4`. It then submits the request
through `func_150C0AC0` with selector `0xFF` and flag `1`.

A typed `GameObjectSpawnRequest` reproduces the retail field offsets and the
complete store schedule. IDO naturally emits the 56-byte frame, preserves the
incoming object in `a3`, places the ID-byte store before the call, moves the
parameter store into the call delay slot, and leaves the callee result in
`v0`. The `D_800A5E5C` high/low relocation pair is preserved. No expected-word
guards or compiler-profile override are required.

## Evidence

The linked span at `conker/build/conker.us.elf` file offset `0x18F5CC` and the
pristine retail span at `conker/conker.us.bin` offset `0x17CA7C` compare equal
across all 116 bytes. Both have SHA-256:

`ca33bae70efffa880c0c760e50ce2f186c4f910c26c19dd03c12554941f4d97e`

The fresh linked matcher no longer lists `func_1514F5CC`.

## Validation

The focused object build, full non-matching replacement build, linked matcher,
direct byte comparison, outer ROM build, project tool checks, focused Python
tests, and whitespace validation pass. Fresh gameplay was not run.

## Sibling boundary

The sibling `64CBFDOGL` retains its pre-existing dirty state. Its frozen
Release checkpoint was not built, modified, or launched.

## Next boundary

Continue with ordinary unparked 26-word Game `func_15157F80`, currently at 25
real differences. Keep the documented smaller special and near-match rows,
Init SDK cache routines, address-drift-blocked `func_10012588`, and larger
parked HUD renderers in their existing lanes.
