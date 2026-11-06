# Double-bank record constructor direct match and SDK vertices

Date: 2026-11-06. Continue the 80% goal from consumer
`96669e13e2c391b09a2b8efc3d5d3e4314e290ed` and mounted tools
`ef015084c29e587c8a97f7480f0882f997322630`.
This completes the next target in
[Note 2122](2122-game-keyed-buffer-registration-direct-match-and-shared-node-layout-20261106.md).

## Installed reconstruction

`func_1510D970`, owner `generated_13AE20`, emits all **69 words** directly
from semantic C. VA `0x1510D970..0x1510DA84`, ROM `0x13AE20..0x13AF34`,
276 bytes, frame `0x30`, saved RA at SP+`0x1C`. Its single factory relocation
matches. There are **no new guards, padding substitutions or profile changes**.
The recovered interface is `void *(s32 kind, void *owner, s32 mode, s32 flags,
s32 variant)`: five incoming words, including the fifth at incoming SP+`0x10`,
with an allocated pointer or NULL returned to the two original callers.

Flag bit 0 selects a `0x128`- or `0x13A`-byte record. The existing factory is
called as `func_15167A68(0x4B, 0, bytes, 1, 0xFF, 1)`, with its actual
`(s32, s32, s32, s32, u8, u8)` interface. Allocation failure skips all record
stores. Success initializes two 64-byte banks at offsets `0x90` and `0xD0`.
SDK `Vtx` views identify the four flags and texture-coordinate pairs in each:
flags zero, coordinate pairs `(0x800,0)`, `(0,0)`, `(0,0x800)`, `(0x800,0x800)`.
All other vertex bytes remain retained. The loops write 48 vertex bytes total.

The owner pointer is stored at `0x110`; the low bytes of kind, mode and variant
go to `0x120`, `0x121` and `0x124`. Their surrounding bytes remain retained.
Odd flags initialize all nine signed halfwords `0x128..0x138` to `0x7FFF`,
ending exactly at `0x13A`. The source's nine-iteration loop reproduces the
retail prologue store and two four-store iterations through normal compilation.
The even-size path leaves the optional region untouched.

## Frame and source fit

The first pointer-cursor source emitted 69 words/frame `0x38` with 27 word
differences. Indexed bank access recovered the register roles but retained
14 frame/home differences. Removing the named masked-flag local and repeating
the genuine `flags & 1` predicate at its two uses recovered frame `0x30`.
The compiler preserves the common masked result in T0 and SP+`0x20` across the
factory. That source differed only in three size-slot words, SP+`0x24` versus
retail SP+`0x28`. Declaring the size before the loop index recovered all three.

The byte-offset version and the clearer SDK `Vtx` version both emit every
word directly. The SDK version is installed. Masking the parameter in place
instead introduced incoming-home traffic and 72 words; register hints and
other local arrangements did not resolve the fit. Rejected variants remain
in the ignored screen directory and are not normalized into matches.

Codex is the single writer. Claude calls attempted/completed: **0/0**.
The source, ABI and compiler experiments settled this routine without advisory
calls or compiler changes. The standalone tools checkout remains untouched.

## Qualification

```sh
python3 -m unittest tools.tests.test_game_double_bank_record_constructor_match -v
```

All **eight focused checks** pass before installation and again after
installation in both tools configurations. The ignored sibling overlay uses
its actual compiler fixture, object parser, timing engine and native command
builder, recording helper paths/hashes and the five new module hashes.

- **5,112 cases per original/raw/padded guest body** execute all 69 words.
  They cover all 256 byte values independently for the three byte fields,
  full-word flag/owner extremes, both sizes, allocation failure, complete
  retained bytes, pointer return, provider effects, live argument homes and
  saved GPR/FPR/SP state.
- **924 private aliases per body** place returned records across incoming
  homes and saved temporaries, preserving the return address for complete
  runs. **205 own-access fault prefixes** compare complete literal states.
  Guest-only argument-home and saved-flag mutations are not portable C claims.
- **64 connected original-factory cases per body** execute every word of
  the **28-word factory**, which is also literal in the predecessor production
  image. Both stack-passed byte homes, allocator core arguments
  `(size, 1, 1, 0, 1)` and header stores at 1 and `0xC` are verified. The core
  allocator and record initializer remain bounded providers.
- **2,056 cases per body** execute the actual **18- and 10-word caller
  windows**, including every window word, existing-pointer gates, all 256
  first-caller type bytes, fifth-argument delay stores and returned-pointer
  stores to owner+`0x2D4` and owner+`0x94`. These are windows of the original
  parents, not claims that either complete parent is emulated. The aligned
  ROM census finds exactly two JALs, ROM `0x597C0` and `0x141290`, with no tails
  or literal function pointers.
- **Nine GNU links** and **90 rebased cases per body** verify the factory
  R26 binding with independent entry/provider addresses.
- **20,016 native32 positive calls**, 3,336 rows per direct/compatible-callback
  path and O0/O2/O3 profile, use SDK headers and UBSan. They check actual `Vtx`
  size/field offsets, the actual factory C, all retained record bytes and
  sentinels, and pointer-return ABI. Thirteen effective controls reject wrong
  flags/sizes/factory kind, one bank, bad stride/texture coordinates, wrong
  owner/mode/variant stores, short or zero tail and cleared retained padding.
- Fail-closed gates reject 276 raw-byte corruptions, one altered binding,
  five complete-image corruptions and the old zero-return placeholder.

Both project-tools smoke checks are fresh. Shared progress, word-guard and
PC16 suites are reused only after their helper fingerprints are checked;
these broad suites are not reported as freshly run. The sibling's six tracked
edits and 2,428 untracked files are preserved.

## Production closure

All **four raw and padded neighboring functions** remain unchanged, including
the existing guarded display-list accessor. All **98 frozen inputs**, guard
CSV bytes, compact allocated data and padded pools remain protected. The
compact `.reginfo` GPR mask changes from `A000C074` to `A300DFFE`; an independent
decode of the complete body derives the union with the old mask. The other
20 register-metadata bytes are pinned unchanged. The owner has no compiler
diagnostics. The existing duplicate `generated_12D630` Make recipe warning
remains.

The complete ELF equals the independent **218-byte** prediction with
**zero exclusions** and **zero named metadata permutations**. Only the target
slot and its symbol size, 12 to 276 bytes, change. All **6,052 function
addresses** remain fixed; no other body changes. All **189,088 protected data
bytes in 720 owners** remain exact. Actual Make equals that prediction.
`make -C conker all` retains the expected checksum exit 2 for the wider
unfinished decomp image. The production recount is:

| Section | Byte-exact | Drift | Still different |
| --- | ---: | ---: | ---: |
| Total | 4,192 / 5,512 (76.05%) | 0 | 1,320 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 3,519 / 4,839 (72.72%) | 0 | 1,320 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

Conversion rows and `progress.csv` remain unchanged. **218 more** matches
reach the current 4,410 threshold for 80%. Production fingerprints:

- ELF: `3ec248e2a5e65ba6ce6cf3a0d05946eb7e7f18fcc83fcfa4bfb6bf08afbb4cd9`.
- Owner: `eca6fe03474fa5b839cb7dc7f34f396014cfd3a660f195a2a6a8ec7a9a95f8c7`.
- Code binary: `3440ebe4efbc9ea1f5390ecf84162f653d4625b0ac48e8a4bf86e52883088455`.
- Unchanged guards: `b53721d727660eca66ed2771ba8fd8597642b08a123168033628a26ff92fd46b`.

Ignored evidence lives under `conker/build/game-double-bank-record-constructor-1510D970-match/`.
Graphify receives a scoped refresh with old-node retention accounting, without
claiming full-corpus re-extraction. Its existing package/skill warning remains.
Tools are committed before the consumer pin, source, aggregate README rows and
concise indexes. No host-port runtime or gameplay acceptance is claimed.

Next: `func_15015920` in `generated_42DC0`, a 70-word asset-block walker with
a signed-16-bit table selector, temporary allocation/copy, big-endian record
sizes and final free. Inspect its original caller, live table reloads and
record-consumer ABI before reconstruction; retain its actual allocation
contract rather than adding an absent failure branch. Keep handwritten
`func_150A76F0` separate and the full 80% goal active.
