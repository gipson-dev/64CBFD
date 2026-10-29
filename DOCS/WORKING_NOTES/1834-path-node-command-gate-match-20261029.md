# 1834: Path-node command gate callback match

Date: 2026-10-29. Target: `func_1507B974`, owner `game_A28B0`.
VA `0x1507B974..0x1507BA48`; ROM `0xA8E24..0xA8EF8`.

The zero-return placeholder and incorrect commented attempt are replaced by a
complete semantic **void, no-argument callback**. Its registration is
`D_80086730[0x44]`, at ROM `0x22B300` / VA `0x80086840`.
The retained declarations and real dispatcher ignore any result. The source
forward declaration now agrees; shared headers and other routines are unchanged.

The current actor's nonzero selector chooses one of 26 actors with stride
`0x32C`. The selected actor's byte at `0x13F` chooses a pointer-table row;
its byte at `0x21E` and parameter byte `D_800D1893` advance that row in separate
eight-byte steps. The unsigned halfword at record offset six is compared with
`D_800D1891`. Equality XORs bit zero of `D_800D1892`; the updated flag gates
`func_15075400(D_800D1890)`. The older comment's flattened lookup was incorrect.

The source emits 53 words, frame `0x18`, and 17 relocation bindings. Thirty-one
expected-word/binding guards normalize closed GPR allocation and independent
address/load scheduling. No instructions are inserted or omitted. This is
guarded byte-exact matching, not unmodified compiler-output matching.
The initial combined record-offset expression emitted only 52 words and was
rejected. The retail assembly remains intact.

Validation:

- 7,488 guest cases / 22,464 executions compare original, normalized and raw C
  bodies. All 53 words are visited. Raw public memory/calls agree; normalized
  full tested register, FPR, memory, event and access-trace state agrees.
- Parameters alias the command/key and flag/offset halfwords. Selector tests
  stay within the declared `0` or `1..26` native actor domain. Big-endian guest
  key behavior is separate from native numeric halfword storage.
- The actual 29-word dispatcher window `0x1507BD00..0x1507BD74` passes 1,728
  cases: command `0x44`, `>=0xF7` skip, four operand stores, indirect call and
  post-provider script-pointer reload plus five. Earlier parent gates are
  explicit preconditions; full-parent/gameplay behavior is not claimed.
- Native32 `-O0/-O2/-O3`, each with UBSan, passes 10,368 cases and rejects eight
  effective source mutants. Static assertions verify actor size and three offsets.
- Forty-two actual memory-access fault prefixes agree for normalized/original
  code. A sparse skip requires neither the command byte nor unused actor pool.
- Three GNU relocation layouts, including low-half carry boundaries, pass 864
  cases. All 212 raw-byte and 17 binding mutations reject; all 31 guard preimage
  mutations reject. No portable raw-C fault equivalence is claimed.
- Full compact/padded owner comparison preserves 210 neighbors and normalized
  pools. Actual Make's five-command pipeline reproduces the qualified object.
  Fourteen inherited owner warnings retain exact normalized diagnostic/source
  context; selected standalone C has zero warnings. Added/changed/deleted
  diagnostic controls reject. Existing duplicate-recipe build warnings remain.
- Eight fresh canonical methods run independently from each tools copy, plus
  each copy's shared tools check. After installation, two checks per copy run
  fresh and six semantic checks reuse only exact module/input/artifact identity.
- Production ELF equals the independent literal prediction: 181 changed bytes,
  comprising 180 target code bytes and one target extent byte. Zero metadata
  changes or exclusions. All other linked bodies and addresses are fixed;
  189,088 protected Game data bytes / 720 owners are exact.

Measured from the adopted ELF: **3,911/5,506 (71.03%)** total,
**3,238/4,833 (67.00%)** Game, Init492/492, Debugger181/181, zero drift.
The C inventory is unchanged. The 75% threshold remains 4,130: **219** more.

Tools are committed first at `c0bf692caf79401b218a734fd3771a994037ef40`; the consumer pins that commit.
The older tools mirror retains all 1,940 inherited dirty paths and three new
uncommitted tool files. No push and no host-port/Release changes.

Graphify receives a scoped native structural refresh with old-node/edge
retention and source-validated void signature, callback registration and actual
provider call. One obsolete placeholder s32 type reference retires only
against their before/after declarations. Historical outside-scope manifest and
community data stay historical; no full-corpus extraction claim is made.

Artifacts: `conker/build/game-path-node-gate-match/`, including immutable inputs,
private receipts, canonical checks, production/adoption audit and live recount.
Two earlier harness-packaging failures were fixed before the accepted private
execution; they are retained as diagnostics, not passing qualification evidence.
Zero Claude calls: the local source, compiler, original instructions and bounded
oracles resolve this routine. No REA/provider setup changes were needed.

Next screened target: `func_1518A214`. Screening is not ABI/source/matching
qualification. `func_15030310` and the previously parked candidates remain private
and uncredited. Continue the same full qualification gates before further credit.
