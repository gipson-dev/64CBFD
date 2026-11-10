# Game actor phase and response-state guarded match - 2026-11-09

`func_1504BE2C` now matches its complete **147-word / 588-byte** retail slot
at VA **1504BE2C..1504C078**, ROM **792DC..79528**. The typed semantic C
emits 146 words with the natural **0x28 frame**. **101 checked guard rows**
close register roles and argument-home scheduling, including **one actor-save
insertion**. This is a guarded match, not a direct compiler match.

Fresh production counts: **4,305 / 5,513 (78.09%)** overall; Game **3,632 /
4,840 (75.04%)**; Init 492/492 and Debugger 181/181. Drift is zero and 1,208
functions still differ. The active 80% goal needs **106** more matches to
reach 4,411/5,513. Conversion counts and conversion CSV stay fixed.

## Scope and behavior

Owner `conker/src/game_77AD0.c`; object `conker/build/src/game_77AD0.c.o`.
The original converted-function assembly file is absent; pristine ROM bytes
are frozen and independently reconstructed with the 14 identified relocation
sites. The ordinary five-command asm-processor/IDO O2-g3/postprocess/padder/
assembler route stays unchanged. No Makefile, profile or shared declaration
change. The target's stale ECTS nonmatching comment is replaced by focused
comments and actor/input/magnitude/output names; the address symbol is retained.

The interface is `void(struct127 *actor, u16 *inputValue, f32 *magnitude,
s8 *outputByte)`. Actor.child is at0x31C; phase is child+0x0B. Scale D_800991D8
has protected bits3CC90FDB. Set D_800CC2B4=16, preserve the contradictory
modeFlags tests and their statically dead1507EB2C block, initialize child+0x0E
to A6 if zero, and set mode+0x3C to5. An ordered magnitude>4 and actor typeAA
select mode1 and copy the unsigned input halfword to child+0x10. Reload the
child after stores as in retail.

Keep the150AD78C sine call at its retail boundary and discard its float result.
Reload actor/child, advance phase modulo256 by2, set actor+0xAA to25 for nonzero
child flags, otherwise50 for typeA7 or32. Halve actor float+0x54.
Types2C/E0 load the POINTER stored in D_800CC284, read signed byte+3, shift
arithmetically by1 and write the output byte. Other types call RNG150ADA20;
only a zero low-six-bit result triggers a second call. The second return uses
UNSIGNED modulo25000, subtracts12500 and stores the low halfword into a freshly
loaded child+0x14. Publish heading to signed D_800CC2B2 and divide by3 toward
zero when current child flags are nonzero. If D_800C35EA and current child
flags are both zero, set actor timer+0x282=30 and clear byte+0x276.

## Closed schedule and its limits

Raw target SHA256:
`22289c110c106c4d974d0a32831d414b681981b4ae536849c12a6e46c5c1412a`.
The normalizer pins all584 source bytes, all14 binding sites, function and
owner. Every output word derives from an identified source instruction.
Register edits touch operand fields only. Branch displacements are rebuilt
from the instruction-origin mapping. No arbitrary replacement body is copied.

The common actor incoming-home save is split onto three mutually exclusive
paths into sine: magnitude failure, type mismatch and accepted input update.
Two branch-likely edges replace the corresponding NOP schedules. One checked
spill copy is inserted after source word61. The input-pointer home save moves
from entry to the dead helper and sine-call boundaries; its live A1 value
serves the noncalling input load. The D_800CC284 high-address initialization
moves earlier across independent phase work. All14 relocation identities move
with their source instructions; expected/replacement binding maps are separate.
The discarded unsigned-float correction and contradictory helper block remain
statically byte-verified. No private float-home offset change was needed.

One deliberately tested guest extension differs in raw output: magnitude may
alias the incoming A1 home. Raw saves A1 at entry, whereas retail preserves the
old home until sine. The normalized body agrees with retail for this extension;
raw does not. This is disclosed rather than counted as raw guest-home alias
equivalence. The authentic caller's three distinct stack buffers do not have
that alias. Portable SDK32 C tests omit physical incoming-home aliases.

## Qualification and production

The complete owner has58 functions, including four retained assembly routines
15052260/15052760/1505327C/150538CC. All **57 non-target neighbors** remain unchanged
in raw and padded comparisons. Pools and reginfo stay fixed; diagnostics0->0.
Independent target generic/generated padders agree with the complete-owner
padder and original ROM. Actual Make produces the same padded owner.

Strict full-ELF prediction accounts for **480 changed bytes**, exclusively the
588-byte target slot and its st_size584->588 update. All6,051 function addresses
remain fixed; protected189,088 bytes across720 owners stay exact with SHA256
0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670.
There are zero unexplained image bytes or exclusions. The inherited whole-ROM
checksum mismatch (`make all` exit2) and duplicate12D630 Make warnings persist.

- Guest:909 cases per body across raw/normalized/retail =2,727 executions,
  plus8 rebases. Signed control bytes and flags cover all256 values; tests
  cover phase wrap, unsigned RNG reduction, signed heading division, ordered
  float boundaries/NaNs, input/output aliases, caller homes, helper child
  redirection, saved registers and all public bytes/call observations.
  Reachable coverage is133 raw and132 normalized/retail words; the unsigned
  correction, contradictory helper and duplicate unreachable loads are covered
  statically. No all-words-dynamically-visited claim.
- Native SDK32:845 defined cases at each O0/O2/O3 with UBSan and14 effective
  mutations per profile. Real canonical headers, typed void function pointer,
  retained actor/child/buffer bytes, numeric endianness normalization and helper
  observations pass. Physical caller-home aliases are guest-only.
- IDO:all14 semantic mutations are independently effective. All146 raw-word
  and14 binding corruptions are rejected; the generic padder rejects101 stale
  expected rows. Corrupting the inserted word changes the independently padded
  body and is detected. Seven literal whole-image corruptions are rejected.
  Four independent GNU links and8 executions cover HI/LO carry boundaries.
  Compiler/interpreter failures are never counted as control witnesses.
- Caller census:the ROM has one JAL at7B510, no aligned entry pointers or
  direct jumps. Its parent1504CB98 is still a padded zero-return placeholder,
  with no corresponding linked call. The authentic **30-word retail window**
  1504E000..1504E078 runs1,152 cases /768 target invocations against all three
  target forms, visiting every window word. Actual caller buffers SP+1BC input,
  SP+1B4 magnitude and SP+197 output, gating, delay-slot float save/reload and
  discarded void result pass. This qualifies the bounded retail window, not
  the whole parent or gameplay. Sine/RNG remain bounded service providers.

Six fresh focused tests run before and after installation in both tools
environments. The sibling uses a read-only overlay for the six new modules;
all2,439 preexisting dirty paths are preserved. Dependency origins/hashes are
recorded. Shared smokes are fresh; three unchanged regression checks per copy
are explicitly fingerprinted reuses. No native/control receipt reuse.

Graphify requests the owner and six new tools paths. Owner C source positions,
retained ASM and nodes outside changed paths are audited; tool-module node
coverage is recorded as observed. The extractor locates `func_1504B0FC` at
its archived `#if 0` definition, line436; the active placeholder is atline659.
Both source positions are checked and recorded separately. Other53 C names
have one audited definition. This is a scoped AST refresh, not full-corpus
semantic extraction. Tools are committed before consumer source/guards/docs/pin.
No push or host-port Release change. Evidence and717 frozen inputs remain in
`conker/build/game-actor-state-1504BE2C-match/`.

Next: `func_15078544` in `conker/src/game_A28B0.c`,150 retail words /148
screened differences. Recheck its current owner/ABI before qualification.
The hard private1510D404 remains uncredited. Keep the80% goal active.
