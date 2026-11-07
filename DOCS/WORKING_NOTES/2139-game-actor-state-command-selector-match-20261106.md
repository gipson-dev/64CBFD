# Actor-state command selector directly matched

Date: 2026-11-06. Continues [Note 2138](2138-game-channel-command-poller-and-reader-ABI-match-20261106.md)
from consumer `d2b5531d4387d6f4c0706a1fbaf022d9808206fe` and tools
`d148342f4968a630c2306cbc50d255e1632cedbb`, toward the active 80% goal.

## Source, interface and record-base type

`func_15080500` in `conker/src/game/generated_AD9B0.c` now emits all
**72 words / 288 bytes directly from C**, with **zero new guards**. VA
`0x15080500..0x15080620`, ROM `0xAD9B0..0xADAD0`, no alignment tail.
The existing O2/g3/MIPS2/O32 profile emits the original **0x20-byte frame**,
S0 and RA saves, incoming homes, branch-likely delay slots, signed record
index division and all **eleven relocation bindings**. All ten neighbors
remain fixed in both compact and padded owners.

The four consumed arguments are an actor pointer, pointer to a52-byte record,
full-word secondary-state selector and full-word command. Null actors, zero
interaction state and gate byte0xFF return before reading state storage.
Commands0x2B/0x2C store the original command in D_800D1940, retain the record
pointer in D_800D199C and select command0x2A. Other commands call the existing
func_15080738 predicate. Every nonzero result enables the availability test:
the signed command shifted right3 selects D_800D2E60's byte and its low3 bits
select the bit. The availability byte is read before the global command store;
an absent bit selects0x1A. A zero predicate leaves the original command intact.

The selected state byte is0x74 for a zero secondary selector or0x75 otherwise.
Bit0x80 protects either byte. A successful secondary write also stores the
signed record index, truncated to a byte, at0x7A. Both the record-base pointer
and actor state pointer are reloaded after the status write, preserving guest
aliases and callback changes. Native record differences stay within one valid
73-element array; arbitrary guest pointers and negative bitmap indices are
qualified separately and are not portable C acceptance claims.

The shared header incorrectly describes D_800D3098 as a fixed array. The first
draft reproduced72 words/frame0x20 but had ten real differences because it
used the symbol's address. Retail instead loads its pointer word. This owner
now uses the established game_40490/game_16EE20 pattern: temporarily rename
the legacy declaration while including variables.h, then locally declare the
actual **struct178 *D_800D3098**. No shared header changes are needed. The
selected source then matches every raw word. An alternative bitmap-capture
schedule remains rejected at17 differences.

## Qualification and corrected fixtures

Eight methods pass before and after installation in both tools configurations.
The completed mounted preinstall run is banked from its exit0 result and eight
fresh method receipts; it is not rerun merely to wrap the same result in JSON.
The sibling uses a disposable overlay for the five new modules and its own
existing parsers, compiler fixture, oracle and native command helpers. No
sibling files are overwritten.27 core input snapshots and80 include-header
snapshots remain fingerprinted; inherited guards and Make rules are fixed.

- **2,335 guest cases per body** cover all256 command, gate and status bytes,
  full-word commands/query returns, high-bit secondary values, single-bit
  availability and callback changes to the state/base pointers and actor gates.
  All reachable root words are visited; duplicate load word52 is unreachable
  and remains in the complete emitted body.
- **150 alias/home cases per body** cover status aliases with the global
  command, record-base word and owner's own state-pointer word, plus incoming
  home changes. **107 fired access cuts** compare literal complete guest states.
  These do not claim portable C fault equivalence.
- **1,024 connected cases per body** execute the original19-word predicate
  and8-word bit splitter. Every helper word is reached. Null/inactive/gated
  early outs also run with state storage unmapped.
- **72 caller cases per body** execute the original nine-word script window
  at VA0x150A1BFC..0x150A1C20, with its branch to0x150A1CF8. The only JAL is
  VA0x150A1C10 / ROM0xCF0C0 in func_150A11C4. Actor,52-byte record pointer,
  secondary1 and unsigned command byte are checked. Its extra fifth home word
  remains preserved and unused by this callee. Saved GPRs, GP, SP and FP stay
  fixed. The complete script interpreter is outside this window's claim.
- **Six GNU links**, three layouts and48 cases per body qualify all eleven
  bindings, signed-low16 carries, JAL regions and standalone zero tails.
- SDK native32 at **O0/O2/O3 with UBSan** runs **2,323 cases per profile**.
  All eight controls fire: special command, fallback, protection, bit selector,
  record index, cached state pointer, cached base pointer and narrowed command.
- **288 byte corruptions, eleven binding corruptions and six full-image
  corruptions** fail closed. The zero-return stub and legacy-array draft are
  rejected. Both tools copies pass fresh smoke checks; three unchanged shared
  regression receipts are fingerprinted and explicitly reused.

The first test fixture accidentally placed state storage over the guest stack.
Unmapped early-out tests exposed that overlap. State storage now lives at
0x60000, separate from the stack; public comparisons include all state writes.
Primary locked-byte coverage was added, and partial availability masks make
the incorrect-bit control effective. The raw .options mask also needed its
own measured baseline: A300C37E to A301FFFE; post-ASM .reginfo is A300C3FE to
A301FFFE. Other words in both records stay fixed. Padded pools and register
metadata are identical to the predecessor. Discarded raw debug/symbol tables
are not claimed byte-identical.

```sh
python3 -m unittest tools.tests.test_game_actor_state_command_selector_match -v
make -C conker -o retail_word_patches.us.csv -o Makefile --output-sync=target -j4 build/conker.us.elf progress.csv
make -C conker -o retail_word_patches.us.csv -o Makefile all
make -C conker -o retail_word_patches.us.csv -o Makefile match-progress NON_MATCHING=1
```

## Production and resume boundary

Only generated_AD9B0.c recompiles, once, with no C diagnostics. Actual owner
and ELF equal their independent predictions: **226 changed ELF bytes**, confined
to the target body and symbol size12 to288, with **zero exclusions**. All
**6,052 function addresses**, conversion rows, progress.csv and **189,088
protected Game bytes / 720 owners** remain fixed. No guard rows are added.
The existing duplicate generated_12D630 recipe warning and expected unfinished
image checksum failure remain. No live hardware or gameplay was exercised.

| Section | Byte-exact | Drift | Still different |
| --- | ---: | ---: | ---: |
| Total | 4,208 / 5,512 (76.34%) | 0 | 1,304 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 3,535 / 4,839 (73.05%) | 0 | 1,304 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

**202 more** matches reach the current4,410 threshold for80%.

- ELF: `e3dc92f6db0e71f6440868e6c095456dba668b22b07458067e6940c4ffc1d13b`.
- Owner: `b548b6e2344dc82538ca19bd1afdf2c459398bbd6f2890daa4f8f4ca12806a05`.
- Code binary: `753aac46c47f671f57d4d2482519fb3e646cd731d0a35b7420bad40c15e9b8ff`.
- Unchanged guard CSV: `28d7a491d60ac432579e06040e28e21cd7e074d6a47e5c665d1d466ef42670ee`.
- Unchanged Makefile: `509371c33a6266fa242b20212c16cf42d4b61575a8773b053bfad43d0778ae1b`.

Evidence: `conker/build/game-actor-state-command-selector-15080500-match/`.
Tools commit precedes source/docs/pin. Scoped Graphify refresh checks old-node
retention; it is not a full-corpus extraction. README changes aggregate rows
only. Claude calls: zero; routine local evidence resolves the ABI and schedule.

Next: **func_150A3194**, generated_CDE80,72 words/frame0x378, VA
0x150A3194..0x150A32B4, ROM0xD0644..0xD0764. Recover its real struct127 query,
seven coordinate stores, live unsigned record count/base pointer, record
filters and first successful query return. The nearby func_150A32B4 already
uses the same concrete query type. Preserve handwritten func_150A6FA0 and
func_150A76F0; the former has handwritten opcodes/interior entry labels and
is not a compiler-generated C target. The next candidate remains uninstalled
and uncredited. Preserve private inputs/saves, unrelated work and frozen host
Release, and keep the complete80% goal active.
