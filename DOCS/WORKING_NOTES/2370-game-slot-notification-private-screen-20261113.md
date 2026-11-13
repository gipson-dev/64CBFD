# Game slot-notification callback: private screen

**Historical screen:** the callback was subsequently installed and qualified
in [Note 2380](2380-game-slot-notification-callback-match-20261113.md).

Date: 2026-11-13. `func_15156028` in `generated_182C30.c` remains a
zero-return placeholder. This screen is **not installed or counted**.
Its retail body spans VA `0x15156028..0x15156188`, ROM
`0x1834D8..0x183638` (88 words), followed by two alignment words. A retail
function-pointer table at ROM `0x230FC4` / data address `0x8008C504` contains
the target. That establishes an indirect reference, but this screen does not
qualify the dispatcher, all indirect callers, or their argument domains.

For event kind 0, the routine subtracts `D_800CC2D0` from the first event
word, interprets the 32-bit result as signed, divides by `0x32C` and, when
the quotient is 0..24 and equals the record byte at `+0x10`, invokes
`func_1516972C`. For kind `0x2D`, it derives two quotients from the two
event words, requires both to be 0..24, and exchanges the record's byte if it
equals either quotient. Other kinds do not trigger these actions. Division is
signed and truncates toward zero: non-aligned pointers just before the base
can therefore produce quotient zero. Treating this as exact array indexing or
adding alignment checks would change behavior. The code and parameter names
below are descriptive hypotheses, not proven game-level names.

The previous private draft emitted 89 words. Reading the two event words into
locals produced the 88-word candidate below. With relocation binding to the
current ELF it has 37 same-position words and 55 ordered-equal words against
retail. The 8 other raw owner functions, normalized constant pools and
compiler diagnostics are unchanged. These measurements do not establish
semantic equivalence or retail matching. The raw compiler moves the second
division after the first quotient's bounds checks; retail computes both
quotients before checking either. The divisor is a fixed nonzero `0x32C`,
but event access, record/stack overlap, signed wrap conversion, helper effects,
and fault prefixes still require independent qualification.

An 18-case local/data-layout screen produced 88 or 89 words and at most 37
same-position words; six additional cases failed IDO's C89 syntax rules.
Another 18 condition/qualifier variations produced up to 38 same-position
words, but no exact result. These are bounded source-shape screens, not an
exhaustive search. No guards were installed, no production object was built,
and no guest, native or full-image test has yet qualified the draft.

The existing owner SHA-256 is `21a26464e643ecfb9d715b7f50f0a039fccd92cef3b205e457c537d2d219f0bd`; the complete private owner source
`fit00.c` has SHA-256 `14557edc014f0643f65a7c533e1394eaeef5bd192d3a1002db2df8092f13a67f`. The ignored
`conker/build/game-slot-notification-15156028-screen/` directory contains
the screen scripts and generated objects; the candidate is reproduced here
independently of those disposable files:

```c
extern u8 D_800CC2D0[];
void func_1516972C(u8 *record);

/* Keep the record's actor slot in sync with removal and slot-swap events. */
void func_15156028(u8 *record, u32 *event, u8 kind) {
    s32 first;
    s32 second;
    if (kind == 0) {
        first = (s32)(event[0] - (u32)D_800CC2D0) / 0x32C;
        if (first >= 0 && first < 25 && first == record[0x10]) {
            func_1516972C(record);
        }
    } else if (kind == 0x2D) {
        u32 left = event[0];
        u32 right = event[1];
        first = (s32)(left - (u32)D_800CC2D0) / 0x32C;
        second = (s32)(right - (u32)D_800CC2D0) / 0x32C;
        if (first >= 0 && first < 25 && second >= 0 && second < 25) {
            if (first == record[0x10]) {
                record[0x10] = second;
            } else if (second == record[0x10]) {
                record[0x10] = first;
            }
        }
    }
}
```

Next, inspect the table dispatcher and argument provenance, including other
callback users; recover exact code scheduling or justify any narrowly scoped
guards with a separate oracle. Exercise signed subtraction/division edges,
both event reads, record/event/stack aliases, helper mutation and fault order.
Only after complete caller, raw/padded owner, guest/native and strict linked-
image qualification should a production build and actual recount be credited.
