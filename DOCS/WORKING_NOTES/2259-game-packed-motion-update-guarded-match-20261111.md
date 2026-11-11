# Packed-record motion update guarded byte match

Date: 2026-11-11. `func_1516A648` restores a packed-record fade and motion
update in `conker/src/game/generated_197120.c`; its original assembly remains
in `conker/asm/197120.s`. The 73-word body occupies VA
`0x1516A648..0x1516A76C` and ROM `0x197AF8..0x197C1C`, followed by one
unchanged zero alignment word. The C body emits 73 words and the retail 0x20
frame. **Six expected-word guards** normalize three closed temporary-register
renames; one preserves a store in the helper-call delay slot. This is a guarded
match rather than a direct compiler match.

The routine updates a byte fade value using the global frame delta, retains
the retail state-byte rereads, updates signed motion, and invokes movement and
height helpers. It records the resulting height and applies a damped response
when the computed level exceeds the current value. The original packed-record
dispatcher `func_1516D678` calls this routine through index 7 of
`D_8008CBA0` and selects removal when the result is 1. The meanings of record
fields and helpers are inferred from their observed operations.

Validation covers 2,816 original/raw/normalized guest cases, including
32-bit wrapping and modeled helper mutations; 768 defined SDK32 native cases
per O0/O2/O3 with UBSan and ten effective negative controls; and 512 cases
through the bounded original dispatcher window. Another 2,250 cases connect
the original 34-word motion helper, 14-word contact helper, and both 12-word
damping helpers. The height helper remains modeled. Hardware FCSR, the full
parent, raw private-stack equivalence, and portable fault behavior are not
claimed.

Both padders agree with independently assembled retail code and preserve the
alignment word. Qualification rejects 306 corrupted byte/binding inputs and
six individually corrupted guards, and passes 16 rebased links and 89
access-cut quads. Actual Make and independent complete-image comparison
account for **221 changed bytes** with zero exclusions. The other three owner
functions, all 6,050 function addresses, and 189,088 protected data bytes
remain unchanged. The actual ELF SHA-256 is `01341a739f7f10d07421348b4463c76bc053e4d36eef6c434303969c6e962419`. The
existing full-build checksum mismatch remains, so this function match does
not imply a matching complete ROM.

Fresh actual ELF recount: **4,328 / 5,513 (78.51%)** overall and **3,655 /
4,840 (75.52%)** Game, zero drift and 1,185 different. The 80% target needs
83 more exact functions. The tools were committed first as
`7ca86a86893cfc2d1e5480369ee8624d6601f4bb`; the consumer change is committed
separately. No push is implied.
