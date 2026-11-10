# Actor audio handle ABI and spill audit

Date: 2026-11-10. Investigation checkpoint; no new function is installed or
credited. The 80% goal remains active.

The accepted baseline is consumer `e35f18d9e081f5fa30201304bc75611b43b25600`
and its tools pin `b62f00d2a945565e40edd565747e15878d241cb0`, from
[Note 2240](2240-game-actor-speed-approach-guarded-match-20261110.md).
Total remains **4,310 / 5,513 (78.18%)**, Game **3,637 / 4,840 (75.14%)**,
Init 492/492, Debugger 181/181, zero drift and 1,203 different. Reaching
4,411/5,513 needs **101 more** accepted matches. The unchanged ELF and progress
CSV fingerprints retain that baseline; this audit does not claim a fresh
production build or recount.

The reproducible compiler/dependency audit is banked in tools commit
`ccdb67b4be30b866be45f75d312a750c0590a666`:

- `experiments/game_actor_audio_handle_15060778_audit.py`
- `tests/test_game_actor_audio_handle_15060778_audit.py`

Both files operate on ignored private outputs. They preserve 16 fingerprinted
production inputs and write no production source, declaration, guard or
matching-credit changes. The consumer pin is advanced to retain this tooling.

## Game target and semantic findings

`func_15060778`, owner `conker/src/game_83300.c`, occupies VA
`0x15060778..0x15060A30`, ROM `0x8DC28..0x8DEE0`: **174 words / 696 bytes**,
frame **0x58**. The installed C is 171 words with frame 0x50. Original assembly
remains in `conker/asm/nonmatchings/game_83300/func_15060778.s`.

The routine selects actor sound handles at offsets 0x8C/0x8E using flag bits
0..1, derives an effect from offset 0x184 unless flag 8 disables it, and uses
flag 4 to select spatial audio. Mode 3 queries the existing handle, updates a
matching sound, or forces a restart with sound-ID bit 0x8000. Creation writes
the returned handle only when a slot was selected.

The private proposal recovers two source details omitted by the installed C:

- Retail computes `(func_1001147C(handle) == arg0) & 0x7FFF`. The mask applies
  to the boolean comparison, not to the requested sound ID.
- The nonspatial command-8 updater receives the full signed-word sum
  `arg2 + effect * 50`. The old eager `u16 volume` local narrows too early:
  input 65535 with effect 48 must pass 67935 to `func_1000F85C`. The spatial
  helpers and `func_10010BE8` still have unsigned-16 volume parameters.

The selected source uses a repeated small switch, a word-sized handle
carrier, late volume expressions, and the original helper argument widths.
Actor pitch/coordinate reads after the query must still observe callback
mutations. These are source/assembly findings; comprehensive functional
qualification remains outstanding.

## The discriminating API result

The current shared declaration and definition of `func_10010BE8` take a
signed-word first argument. Its retail entry explicitly saves the incoming
word and zero-extends the low 16 bits. A private, consistent proposal changes
both declaration and definition to `u16 arg0` and removes the synthetic
`volatile s32 normalizedHandle` local from the definition. It does not use an
incompatible function-pointer cast or a conflicting caller-only declaration.

That proposal brings the Game function to **174 words, frame 0x58, eight word
differences**. All six relocation sites already bind to retail instructions.
All **88 other Game functions**, their relocations, normalized pools and
register information remain equal; the eight inherited diagnostics remain.

The eight differences are words 38, 39, 43, 44, 93, 95, 96 and 98. Every
opcode, register field and other instruction bit is equal. Only two private
stack-home offsets differ:

| Value | Candidate home | Retail home |
| --- | --- | --- |
| Promoted handle | SP+0x40 | SP+0x44 |
| Cached effect | SP+0x48 | SP+0x54 |

The selected raw body SHA-256 is
`3be80c40626a62646943723826602d2e96f1895995a1aaca760414a40801c526`.
No normalization rows have been generated or installed. Earlier handle,
declaration, cast, control-flow and profile screens remain private; matching
length alone was never treated as a match.

## Init dependency boundary

The complete 54-function Init owner was compiled before and after the same
header proposal. Exactly two raw functions change: `func_10010BE8` and
`func_10010FFC`. The other **52 functions**, relocations, normalized pools and
register information remain equal. All 13 inherited diagnostics remain.

| Raw C body | Words | Frame | Differences from retail |
| --- | --- | --- | --- |
| Existing `func_10010BE8` | 164 | 0x60 | 85 |
| Narrow-handle proposal | 164 | 0x58 | 73 |

The proposed callee SHA-256 is
`4a8595bc493fe784ed3c931263c1d7b5da43077e22235cd1b45ab6bfe0c79175`.
Retail's frame is 0x50. Its existing 85 guards are tied to the previous raw
source and cannot be reused: the first expected word is `0x27BDFFA0`, while
the new source emits `0x27BDFFA8`. The audit explicitly checks this stale
boundary. It does not weaken or replace the guards.

`func_10010FFC` remains 115 words/frame 0x40, with 104 raw differences from
retail under either declaration, but its raw bytes change. Equal difference
counts do not establish equality. Its changed call argument setup requires
its own source/ABI/padder audit; it must not be excluded from an image audit.
The previously accepted, guarded Init production bodies remain untouched.

## Original caller census

An aligned whole-ROM encoding census finds five direct JAL sites, no direct
J encoding and no aligned literal pointer to the target:

| ROM call | VA call | Original parent |
| --- | --- | --- |
| 0x81904 | 0x15054454 | `func_150538CC` |
| 0x8DF34 | 0x15060A84 | `func_15060A30` |
| 0x8DF9C | 0x15060AEC | `func_15060A9C` |
| 0x8E008 | 0x15060B58 | `func_15060B04` |
| 0xA3748 | 0x15076298 | `func_15076250` |

The remaining assembly-file search exposed only three sites. The ROM census
resolves that inventory gap; it does not exclude computed indirect calls or
qualify the complete parent algorithms. Full caller execution is still due.

## Validation and advisory reconciliation

Four focused compiler/dependency checks pass freshly in each tools
environment. The sibling runs use a private overlay for the two new files,
with explicit read-only mounted fallbacks for `diagnostic_rows` and
`bound_blob`, which the sibling lacks. Every imported helper is fingerprinted.
Fresh shared smoke checks pass in both environments; three unchanged shared
regression receipts per environment are reused by exact fingerprints, not
reported as freshly executed. The sibling's **2,434** pre-existing dirty paths
are preserved; no file is written into that checkout.

One bounded Claude Pro advisory was used for the difficult call-save issue:
packet-only, no tools or MCP servers, no tool uses, and no second writer.
The packet and answer hashes are respectively
`34953b656a78b6bf05cf93d1e2bef5de3ecb925870f336d54e0ed3a88b491c3d`
and `a924f02f85aaf62492f61abf9647a2ff815a73609d01f4a9ecfa176730580eff`.
Removing eager initialization and adding an explicit query cast did not
recover the required homes; the measured screens reject those fit hypotheses.
The answer's wide-volume interpretation for `func_10010BE8` is rejected by
the actual declaration and retail width behavior. Its description of only
one handle save is incomplete: retail also saves/reloads the promoted handle
across the first `func_1000F85C` call. No further advisory call is authorized
by the current target's one-call analysis budget.

The requested scoped Graphify code refresh was attempted. Current filters
exclude the tools submodule and reported no tracked code in the change set.
The graph remains byte-identical at **59,645 nodes / 113,070 links**, with all
old nodes retained and zero indexed nodes for these two new Python files.
This is an explicit coverage gap, not a completed code extraction claim.

## Continue from here

1. Recover the narrow-handle Init callee and the affected `func_10010FFC`
   source shapes. Preserve their accepted linked bodies; audit every changed
   raw function and stale guard. No frame padding or blanket exclusions.
2. Qualify all three proposed bodies with the existing guest/native32 and
   caller helpers: argument widths, upper-bit inputs, cached handles/effect,
   late actor reads, callback clobbers and volume overflow. Bind immutable
   object programs once outside case loops to avoid repeated 9P parsing.
3. Close the two Game spill-home differences with supported source or checked
   normalization only after those proofs. Exercise both object padders,
   independent relocation rebases and effective negative controls.
4. Run actual Make, a strict whole-image prediction with every dependent
   owner audited, production checks, and the actual ELF recount. Only then
   install, credit and document a new match. Commit tools before the consumer.

Private receipts and rejected screens remain in
`conker/build/game-actor-audio-15060778-match/`. Reproduce the banked audit from
the consumer root under the prepared WSL environment:

```sh
python3 -m unittest tools.tests.test_game_actor_audio_handle_15060778_audit -v
```

No host-port source, saves or frozen Release artifacts are touched.
