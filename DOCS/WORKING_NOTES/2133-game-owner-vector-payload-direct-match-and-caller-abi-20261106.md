# Owner/vector payload direct match and caller ABI

Date: 2026-11-06. Continue the active 80% goal from consumer
`ece4f0e03f7ee94c80d626e86e51ed90adb3f852` and mounted tools
`e3642d692978c86c578f5762f4ab3dee60cb0ce2`, following
[Note 2132](2132-game-byte-phase-and-sine-scale-callback-match-20261106.md).

## Recovered constructor

`func_15160A58` in `conker/src/game_18D770.c` now emits all **71 words /
284 bytes directly from C**, VA `0x15160A58..0x15160B74`, ROM
`0x18DF08..0x18E024`. There is no alignment tail. The unchanged O2/g3/MIPS2/O32
profile produces the retail frame `0x68`, RA at SP+0x34, zero vector at+0x38,
payload at+0x44, header at+0x5C and returned-record spill at+0x64.
There are **zero new guards** and two ordinary call relocations.

The proper interface returns struct225* and retains all **16 arguments**:
owner pointer, kind byte, vector pointer, header ID byte, signed16 lifetime,
four full32 words, two unused full32 slots, signed byte payload tag, full32
extra size, flags byte, priority byte and full32 user word. The old commented
draft omitted the two unused slots; that malformed draft and the stale
placeholder comment are removed. The old typed stub was **28 bytes**, with
four incoming argument-home stores and a zero return, rather than 12 bytes.

Null owner returns zero before reading the vector. Otherwise the Header has
ID, constant 5, lifetime and flags 0x10; Header2 contains three integer-zero
words. The local 24-byte OwnerVectorPayload15160A58 captures the owner address,
owner identity byte+0x3B, kind, all three raw vector words, tag and flags.
The payload is captured before any factory effect. Its four padding bytes
and the header's final padding byte have explicit guest/native boundaries.

The constructor forwards header and zero-vector pointers, the four full words,
255,0, extraBytes+24 modulo 32, priority and user word to func_151602C0.
A nonzero record receives all 24 payload bytes at record+0x18 through memcpy;
the returned pointer is preserved across that call. Allocation failure returns
zero. Size arithmetic uses unsigned word addition to preserve retail wrapping.

Declaring result before Header/payload/zero recovers the retail local homes.
Assigning header lifetime before flags and payload identity before kind lets
IDO recover the exact independent schedules and temporary register roles.
The earlier 30/21-difference shapes remain private controls. The final complete
body needs no instruction patch, omission, insertion, branch or frame change.

## Three complete owner and interface audits

The constructor's forward declaration and definition now agree. The existing
C caller 15163BE8 makes its owner-address conversion explicit. Two additional
owners had stale declarations: generated_11C2B0 used 16 s32 parameters and
generated_179F30 had an unspecified list and integer result. Both now use the
same proper pointer/byte/halfword/full-word interface. The latter includes
structs.h and explicitly converts the pointer result to its existing s32
address-return contract. Shared headers and original ASM remain unchanged.

Complete copied owners use the real ASM postprocessor and production padders:

| Owner | Raw/padded unchanged neighboring functions | Complete caller object fixed |
| --- | ---: | --- |
| game_18D770 | 77 / 77 | Target body changes |
| generated_11C2B0 | 44 / 44 | Yes |
| generated_179F30 | 78 / 78 | Yes |

All raw and padded allocatable pools, metadata and bindings stay fixed in all
three owners. The two caller objects are byte-for-byte identical before and
after their source repairs. No dependent body or section is excluded.
All **142 frozen inputs** are audited, with precise source-change closure.
The guard CSV remains byte-for-byte unchanged.

The root owner loses exactly two Warning712 messages at its old constructor
call, 44 to 42. generated_11C2B0 remains 0; generated_179F30 remains 4. Thus the
three-source total is 48 to 46, with no new diagnostic. Complete normalized
message/code/caret multisets are checked. The other warnings are preserved;
this is not a warning-free build claim.

## Qualification

Eight focused checks pass before and after installation in both actual tools
configurations. The sibling uses an ignored overlay for the five new modules
and its actual shared helpers, with exact source fingerprints; its six tracked
edits and 2,428 untracked files remain fixed. Both tools smokes are fresh.
Three shared suites per copy are exact-fingerprint reuses from Note 2124,
separately recorded. Routine work uses zero Claude calls.

- **3,088 guest cases per body** cover all 256 byte axes, signed lifetime
  boundaries, all 16 argument positions, arbitrary vector bit patterns,
  full-word size wrapping, null owner, actor failure, record failure and
  success. Mutable providers change owner/vector inputs after the capture.
  All 71 root words are visited. Original and direct C match complete RAM,
  registers, events, accesses, helper snapshots and literal guest padding.
- **128 stack/vector alias cases per body** and **143 fired access-cut
  prefixes** compare full literal states. This is an emitted-instruction
  proof; portable C stack aliases or particular padding values are not claimed.
- **384 connected cases per body** execute all 47 original factory words,
  all 32 record-helper words and all 11 Init memcpy words. Current linked helper
  slots equal retail. The actor constructor, allocator and free routine are
  explicit opaque boundaries. Failure cleanup, six-byte header copy, actor
  pointer store, header flag OR 2 and 24-byte payload copy are independently
  checked. This does not claim the entire allocator, geometry or game engine.
- **1,152 caller-window cases per body** execute all 12 authentic JAL sites
  in 10 parent functions across 5 owners. Each complete argument setup has an
  explicit 16-word expected matrix, including both unused slots and real delay
  stores. Priority bytes cover 0/127/128/255; all three outcomes, both stack
  phases, mutable inputs and null/non-null owners are exercised. Prior calls,
  branches and parent state are declared entry preconditions. Full parent
  functions are not claimed merely from these windows.
- **Six independent GNU links**, three entry/helper layouts and **75 cases
  per body** verify both call bindings and standalone zero alignment bytes.
  The actual retail slot has no alignment tail and its next word is protected.
- **4,620 SDK native32 positive executions** pass O0/O2/O3 with UBSan and a
  correctly typed 16-argument function pointer. Including ten wrong variants,
  **50,820 calls** execute. The header's defined fields, captured owner address,
  identity/kind/tag/flags, all three vector words, size/priority/user arguments,
  allocation result, copy length and output canaries are checked. Native
  addresses are checked as addresses; five padding bytes have guest-only
  value proof. All ten controls fail by checked state/result comparison,
  killed mask 1023; a sanitizer trap cannot satisfy this gate.
- All 284 raw-byte corruptions, both binding corruptions, five whole-image
  corruptions and the old 7-word stub are rejected. There is no new guard
  manifest to normalize the body.

## Actual production and recount

```sh
make -C conker -o retail_word_patches.us.csv -o Makefile --output-sync=target -j4 build/conker.us.elf progress.csv
make -C conker -o retail_word_patches.us.csv -o Makefile all
make -C conker -o retail_word_patches.us.csv -o Makefile match-progress NON_MATCHING=1
```

Exactly the three edited C sources compile, once each, in their original
profiles. Output synchronization groups each target's existing diagnostics.
A receipt assertion initially treated the normal rule's doubled whitespace
between flags as a profile change. Token-normalizing that comparison resumed
the remaining binary/recount gates from the already verified objects and ELF;
no source recompilation or object timestamp adjustment was needed for this fix.

The actual ELF equals the independent **207-byte prediction**, with **zero
exclusions or metadata permutations**. Only the constructor body and symbol
size 28 to 284 change. All **6,052 addresses**, conversion rows, progress.csv,
Make rules, guard bytes and **189,088 protected data bytes in 720 owners** stay
fixed. Both caller objects remain identical. The unfinished whole image retains
its expected checksum failure and duplicate generated_12D630 recipe warning.

| Section | Byte-exact | Drift | Still different |
| --- | ---: | ---: | ---: |
| Total | 4,202 / 5,512 (76.23%) | 0 | 1,310 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 3,529 / 4,839 (72.93%) | 0 | 1,310 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

**208 more** matches reach the current 4,410 threshold for 80%.

- ELF: `34996972e0bce5a5d3b33900f1bfb9d3eecdad507effb5dc3be2fee45a338f72`.
- Owner: `646ba33a0293cd64047b405cc186ddf490cf74bd7da59dc861543d03987212dd`.
- Code binary: `4d4a84aa86847d46195cfbb5f5e8b436a9876738d2ac6dfa3ff554c649f0012f`.
- Guard CSV: `ad8c4e24d535e3ccc7aa3d4c3ae7db4972c569bbf690238f68c65757438993c6`.
- Unchanged Makefile: `509371c33a6266fa242b20212c16cf42d4b61575a8773b053bfad43d0778ae1b`.

Evidence is retained in `conker/build/game-owner-vector-payload-15160A58-match/`.
Graphify receives a scoped AST refresh with old-node retention evidence; no
full-corpus extraction is claimed. Tools are committed before the three source
files, documents and consumer pin. Root README changes aggregate rows only.

Next static target: **func_151623F4**, also game_18D770, VA
`0x151623F4..0x15162510`, ROM `0x18F8A4..0x18F9C0`: 71 words/frame0x50.
Its unsigned byte selector accepts 0..2, copies two three-word table rows,
loads a selector-dependent float, builds a header and 32-byte payload, and
uses func_1516037C plus conditional memcpy. Inspect all eight argument types,
live selector homes, D_800A670C/D_800A6730/D_800A6754 bindings, field/padding
layouts and callers before qualification. It remains uninstalled/uncredited.
Preserve unrelated work, private inputs/saves, handwritten func_150A76F0 and
frozen host Release. The full 80% goal remains active.
