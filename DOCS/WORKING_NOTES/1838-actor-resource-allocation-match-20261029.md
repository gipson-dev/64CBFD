# 1838: Actor resource allocation match

Date: 2026-10-29. Target `func_150832AC`, owner `generated_AEB40`.
VA `0x150832AC..0x15083384`, ROM `0xB075C..0xB0834`: 54 retail words.

The false zero-return placeholder is replaced by a complete void routine with
one actor pointer. If the descriptor at actor+0x144 exists, its unsigned byte
at +0x2F supplies the resource count. Zero selects 5 for a zero actor+0x127 byte,
otherwise 3. The count is captured before allocation. The loop allocates one
resource per index from zero through the live signed `D_80082FA0` value,
rereading it after each provider call. It stores resource pointers starting
at actor+0x304. The final test is deliberately actor+0x300+index*4, not the next
entry at +0x304: even a negative initial view count can test the header word.
The count byte at +0x301 updates only for a nonzero tested word. A trailing
resource pointer from `func_1515D440` is then stored at +0x314. Larger loop
counts can overlap this trailing field; the retail ordering is preserved.

The generated C has 53 words and the exact 48-byte frame, including saved
S0/S1/S2/S3/S4/RA homes 0x18/0x1C/0x20/0x24/0x28/0x2C. There are no incoming
argument-home reloads or frame-size adjustments. Eighteen checked word/binding
rows close the register allocation and count-selection CFG. One word is
inserted: the existing count-3 literal moves to normalized +0x5C, with the
redundant retail common-exit branch at +0x58. No conditional behavior is added,
no instructions are omitted, and both provider bindings move by four bytes.
This is guarded byte-exact C; it is not direct compiler output.

Pointer interfaces were corrected before committing. The providers' restored
definitions return `u8 *`, while this owner previously declared integer returns.
Their declarations now precede the new routine and match the definitions.
Resource stores in this routine and the existing `func_15083AC8` use pointer
lvalues. All 30 neighboring compact/padded bodies remain byte-identical,
including that constructor. The corrected interface passed fresh private and
both-copy suites; superseded integer-interface evidence is archived and is
not used for acceptance. Both retained ASM callers ignore v0. The whole aligned
ROM scan has two direct JALs (0xB0538 and 0x5E95C) and no full pointer words;
computed/encoded references are not excluded by this scan.

Validation passed:

- Eight fresh checks in each tools copy plus the shared tools checks. Installed
  checks rerun two methods per copy; six semantic checks are reused only under
  complete input/module/artifact identity.
- 10,368 guest cases / 31,104 executions cover original, padded and raw C and
  all 54 retail words. Public C effects agree; normalized registers, FP state,
  full RAM, events, memory traces and HI/LO equal literal retail state. Cases
  cover null/shared descriptors, unsigned high count bytes, negative view counts,
  count growth/shrinkage, captured-descriptor mutations, global/actor aliases,
  overlapping entry/trailing fields and two stack phases.
- Native32 O0/O2/O3 each pass 5,184 cases with UBSan and reject six controls:
  cached/exclusive count, wrong final indexed test, unconditional count-byte
  update, wrong fallback and omitted trailing allocation.
- Both original caller windows pass 96 cases each: 4 words at 0x15083088 and
  7 at 0x150314AC. They establish the argument and ignored-result behavior;
  the latter reloads its saved v0 and resource entry. Earlier parent gates are
  preconditions; neither parent placeholder gains C credit.
- 150 dispatched access-prefix pairs preserve literal normalized state. A null
  descriptor needs no count global, flag bytes, unused fields or providers.
  Three GNU relocation layouts pass 486 cases. All 212 raw-byte/four-binding
  controls and all 18 real padder guard-preimage controls reject.
- Five actual Make commands, including retained-assembly preprocessing, reproduce
  the qualified owner object. Selected and owner C emit zero diagnostics. The
  inherited duplicate-recipe Make warning remains. All 30 owner neighbors and
  relocation-owned pools stay fixed.
- Strict independent prediction equals production: 161 changed bytes = 160
  target code + 1 target extent, zero metadata differences or exclusions. All
  6,055 other linked bodies and every function address remain fixed; protected
  Game data stays exact across 189,088 bytes / 720 owners.

Providers are bounded test contracts. Null return words probe the caller;
completion of a real allocation failure is not claimed, since the original
helpers subsequently zero their allocation. No hardware/gameplay acceptance
or complete-parent claim is made.

Fresh adopted-ELF recount: **3,915/5,506 (71.10%)** total,
**3,242/4,833 (67.08%)** Game, Init 492/492, Debugger 181/181, zero drift.
The conversion inventory CSV is unchanged. **215** more matches reach 4,130.
Tools commit first: `9126fa655fdf04f401f902913f36713f6df4f328`.

The scoped native AST graph refresh retains or uniquely relocates all 49,493
old nodes and accounts for all 102,638 old relationships. Only the old target
s32 return edge retires against its recovered void signature. The two pointer
store type changes in the unchanged constructor are source/binary-validated.
Outside-scope manifests and communities remain historical; no full extraction.

Artifacts: `conker/build/game-actor-resource-allocation-match/`.
Next screened target `func_150BE210` still needs qualification. Previously parked private
candidates remain uncredited. The older mirror preserves 1,952 inherited dirty
paths plus three new tools. No push, host-port, Release, saves/editor or memory
changes. Zero Claude calls.
