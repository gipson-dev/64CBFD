# Working Note 1909: Settings packet writer and storage extents

Date: 2026-10-31. `func_15007558`, ordinary owner `game_33990`.
ROM `0x34A08..0x34AF4`; VA `0x15007558..0x15007644`. Tools: `dc6ec502c735574938c3bfe884fcdb7dd8d07714`.

## Recovered behavior

The former zero-return placeholder is now `void func_15007558(void)`.
It copies 28 settings bytes from `D_800E0BE0` into the EEPROM scratch
payload at `D_800BE358+2`. It then reads the unsigned bytes through
`D_800BE35A`, computes seed 0xCC plus the repeating weights 4,8,1,2,
and writes the 16-bit checksum into the first two scratch bytes.
The checksum domain is 204..26979; no 16-bit wrap occurs for this input
domain, although retail masks the unrolled accumulator.

If `D_8002AC5C` is zero after the checksum store, the function calls
`func_151DCEF0(&D_800BE900, 0, D_800BE358, 32)`. It stores the helper
status to a volatile local at SP+0x18 and returns void. The final two
bytes of the 32-byte record are preserved. The original caller reloads
V0 independently and clears the request state, confirming an ignored return.

## Corrected storage declarations

`D_800BE358` is shared **128-byte EEPROM scratch**, not an eight-byte
buffer. Retail `func_15006590` clears/loads length 0x80 at this address;
the neighboring save writer also uses the full span. The settings record
uses its first 32 bytes, and the erase routine uses the first eight.
`variables.h` now declares the full 128-byte extent with this distinction.

The persisted settings region `D_800E0BE0..D_800E0BFC` is 28 bytes.
Its definition in `generated_20AE20.c` is corrected from 23 to 28.
Both reset loops deliberately retain their explicit 23-byte bounds.
The final five settings bytes are not newly reset by this change.
All 60 functions and owner pools in that dependent source are unchanged;
its actual Make output is byte-identical to the previous production object.
All 17 other functions in `game_33990` are also unchanged.

An intermediate 32-byte scratch declaration was tested, then superseded
after neighboring retail routines established the full 128-byte extent.
Intermediate artifacts and receipts are preserved under the stage's
`record32-intermediate/` directory. Only seven owned task inputs were
restored to their frozen baseline before complete 128-byte qualification.
No pre-existing user work, old mirror edits, or private candidates were reset.

## Matching and qualification

The complete semantic C emits 59 words under existing O2/g3, with a
32-byte frame. Three expected-word/relocation rows normalize a closed
payload-pointer displacement and independent opening address schedule.
There are zero insertions or omissions. All 59 words and 15 named
relocation bindings match retail. This is a guarded C recovery.
All six actual padder stale-word/binding controls reject.

Guest validation: 1,296 cases, 5,184 normalized and 1,296 raw executions,
three independent address rebases, all 59 words reached, 48 alias cases,
266 fault-prefix cuts and 84 branch-delay cuts. Raw final architectural
state and access order agree with retail. Normalized prefix state agrees
exactly; raw prefix memory and access order agree despite the temporary
payload-pointer displacement. Overlapping copies, checksum/flag aliases,
and independently rebound payload labels are included.

Native32 O0/O2/O3 each pass 688,128 cases with trapping UBSan: every
payload position and every byte value, four backgrounds, gate values,
status patterns and callback mutations. Nine wrong semantic controls
exit 1. The 128-byte union-backed scratch and real interior/end labels
are used; bytes outside the 32-byte record remain unchanged.
Host checksum byte order is not claimed as guest serialization evidence.

The previous erase routine's unchanged C body also passes fresh
594,432-case native suites at O0/O2/O3 with the corrected 128-byte
scratch declaration. Original caller: six retail words, 96 cases,
1,536 normalized and 384 raw executions with four V0 poisons.
The aligned full-ROM census finds one JAL at 0x49B94 and no literal
function pointer. No full-parent, EEPROM hardware or gameplay claim is made.

## Whole-image and production evidence

The main and dependent owners each use three actual Make commands.
Independent image prediction accounts for 211 changed bytes: 196 code,
one target size byte, and 14 bytes in the closed two-symbol permutation
`D_800E0BFC` / `D_800A36CC`. Names, fields and the contiguous string block
are reconstructed from frozen input; no metadata or image region is excluded.
All 6,055 other bodies, all function addresses and protected Game data
(189,088 bytes across 720 owners) remain unchanged.
Production ELF SHA-256:
`86550723432dfe6516fb3cd3a0e5712e6a38aabd2cb9e2da7faab2c31013e772`.

Both tools copies pass eight fresh canonical methods and shared checks
for the final 128-byte declaration. Postinstall, two fresh checks per
copy validate adoption; six unchanged semantic checks are reused only
under identical complete input/module/artifact fingerprints.

The actual ELF recount is **3,986 / 5,506 (72.39%)** exact C.
Game: **3,313 / 4,833 (68.55%)**; Init: 492/492; Debugger: 181/181.
There are 1,520 differing C functions and zero drift. The 4,130-function
75% threshold requires **144** further installed recoveries.

Tools were committed before consumer source/guards/declarations/pin/docs.
Root README changes are limited to two aggregate rows. Graphify receives
a scoped thirteen-file structural refresh, retaining historical nodes and
valid directed links while retiring the obsolete placeholder s32 return edge.
No full-corpus, global clustering or centrality refresh is claimed.

Evidence: `conker/build/game-settings-packet-write-15007558-match/`.
Frozen inputs, failed probes, intermediate receipts, dependency audits,
canonical results, strict image, production and final seals are retained.
Next screen: `func_15043CA4`. The 75% goal remains active; private work is uncredited.
