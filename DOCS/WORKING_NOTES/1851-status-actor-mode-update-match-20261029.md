# 1851: Status-selected actor mode update match

Date: 2026-10-29. Target `func_151E7DC0`, owner `generated_20AE20`.
VA `0x151E7DC0..0x151E7E9C`, ROM `0x215270..0x21534C`: **220 bytes /55 words**.
The body fills its slot; no alignment words follow within the classifier slot.

The zero-return placeholder becomes `void func_151E7DC0(void)`. It returns
early when the level at current status `D_8008FDD4+8` is below `D_800ABA8C`
and signed flag byte+0x3E is zero. Otherwise it performs two lookups. For
each row in `D_8008FFB0`, a nonzero status flag selects column0; zero flag
selects the signed byte at status+0x2C. Each table byte is passed unsigned
to `func_151149AC`. A nonnull returned record receives word2 at+0x80.
The status pointer, flag/selector and table are read live after lookup calls.

Declaring the table as six-byte rows recovers retail's two indexing paths,
multiply/shift choices and saved constant6. All55 words and seven relocations
emit directly from semantic C using the existing O2/g3 profile. Its original
48-byte frame saves S0..S4 at+24..+40 and RA at+44. There are16 outgoing
bytes and no incoming homes. No guards, insertions, omissions, frame
adjustments, shared-header edits or compiler-profile changes. The guard
manifest and conversion inventory CSV remain unchanged.

- Eight fresh canonical methods pass independently in both tools copies,
  plus shared checks. Production reruns two installed methods per copy;
  six unchanged semantic checks reuse only full input/module/artifact identity.
  The older mirror retains1,991 inherited dirty paths and receives exactly
  three new qualification files without a mirror commit.
- Guest: **4,152 cases /12,456 original/raw/padded executions**, literal
  full-state agreement and all55 words covered. Cases cover all256 flag,
  selector and lookup-byte values, float thresholds/zeros/infinities/quiet
  NaNs, all32 provider-mutation combinations, null/nonnull/shared outputs,
  changed status pointers, changed flags/selectors, edited tables and output
  stores overlapping status/table fields. There are64 guest mode-store alias
  cases,112 access-prefix comparisons, three sparse early exits, and three
  layouts /96 rebased cases.
- Native32 O0/O2/O3 each pass **1,550 cases with UBSan**. Native selectors
  are restricted to0..5; negative/out-of-row selector reads remain bounded
  guest evidence. Guest aliases whose word stores affect selector/flag/table
  bytes differently on little-endian hosts are excluded from native acceptance.
  Full record/actor/table bytes, status pointer, threshold, helper arguments
  and pre-call observations are checked. Eight controls reject: inclusive
  float gate, inverted early flag gate, wrong table row, wrong stored mode,
  wrong output offset, cached record pointer, cached selector, and repeating
  the float gate after the first lookup.
- The original28-word lookup helper at VA `0x151149AC` / ROM `0x141E5C`
  executes48 connected cases, covering found/missing/zero keys and first
  duplicate selection. Its bytes equal the current ELF; its source and body
  are preserved, with no new matching credit. Its argument-home store fits
  the target's existing outgoing area.
- Full-ROM scan finds one direct JAL at ROM `0x20BDD4` / VA `0x151DE924`,
  and no aligned full-pointer words. Actual parent `func_151DE8F0` is verified
  from `conker/asm/20AE20.s`; its C body remains a separate stub. The original
  two-word JAL/delay window executes48 cases and ignores the result. Earlier
  menu-reset work and the following `func_151E81EC` call remain preconditions;
  no complete parent/gameplay or new parent matching credit is claimed.
- Complete-owner compile/padding preserves59 neighbors and pools, including
  the recent status-intensity recovery. Three actual Make commands reproduce
  the exact object with zero C diagnostics; the inherited duplicate-recipe
  warning remains. All227 raw-byte/binding controls and240 whole-image
  corruption controls reject.
- Independent prediction equals production: **162 changed bytes =161 target
  code +one symbol-extent byte**, zero metadata changes or exclusions. All
  6,055 other linked bodies and all addresses remain fixed. Protected Game
  data remains exact across189,088 bytes /720 owners.

Fresh adopted-ELF count: **3,928/5,506 (71.34%)**, Game **3,255/4,833 (67.35%)**,
Init492/492 and Debugger181/181, zero drift. **202** more to4,130.
Tools committed first: `ef0b6b63a93611ebb8e30d9afad574a53b3384d1`. No push. Root README gets aggregate rows only.

The scoped eleven-file AST refresh retains or uniquely relocates all50,159
prior nodes and preserves103,985 valid old directed relationships. One old
s32 return relationship retires for the recovered void interface. Actual
caller/helper binding, six-byte rows, signed selector and live post-call
reads are annotated. Outside manifest rows/analytics remain historical;
no full-corpus re-extraction, hardware FCSR or gameplay claim.

An earlier private `func_151A084C` screen remains uncredited. Its complete
candidate compiles55 words with a56-byte frame and38 word differences;
retail requires48 bytes and different boolean/saved-pointer lifetimes.
No source, guard or production-profile change was adopted for it. The
alternate autodraft also had incorrect byte-field widths and was rejected.
Private handoff: `conker/build/game-record-resource-transition-match/HANDOFF.md`.
Keep that candidate parked until its full frame/ABI/memory/linked gates pass.

Current artifacts: `conker/build/game-status-actor-mode-update-match/`.
Next screen `func_1505EEF4` still needs full qualification. Other private candidates
remain uncredited. No host-port, frozen Release, save/editor, private-input
or memory changes. Zero Claude calls. The75% matching goal remains active.
