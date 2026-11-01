# Selected actor health command restored directly from C

`func_150746F0` now emits all **61 retail words directly from C**, with its
original 32-byte frame and no guards, assembly insertion, omission or profile
change. The complete 244-byte slot is byte-exact under the existing O2/g3 profile.

Production Make and the live Windows-checkout recount agree on **4,018/5,506
(72.97%)**, Game **3,345/4,833 (69.21%)**, Init 492/492 and Debugger 181/181,
zero drift and 1,488 different. **112 more matches** are needed for the active
4,130/5,506 threshold. Tools were committed first at `acfc364`.

## Recovered operation and interface

Owner/source: `game_981E0`, `conker/src/game_981E0.c`.
VA **150746F0..150747E4**; ROM **A1BA0..A1C94**.
The old no-argument integer-return placeholder becomes `void func_150746F0(void)`.
The sole aligned ROM pointer reference is callback-table entry 156 in
`D_800863FC`, at VA8008666C / ROM22B12C. No aligned direct JAL or second
pointer literal targets this function. Its original indirect caller ignores
its return value; no shared header changes are needed.

- A nonzero unsigned selector `D_800BE616` selects the current actor
  `D_800D154C`. Otherwise the current actor's byte +0x13C selects pool slot zero
  when nonzero. If neither condition selects an actor, the routine returns.
- Compare the selected actor's unsigned health byte +0x1CA against the signed
  command amount `D_800D1580`. That amount is supplied by the script record;
  it is not assumed to be a frame delta or a nonnegative value.
- If amount is at least health, clear selected health, then reload the current
  actor pointer and clear its health. If selected interaction_state is exactly
  one, set immune (+0x125) to 255 and submit `func_1507CD64(actor, 6)`.
- Otherwise subtract the amount and retain the low byte. The source uses
  `(u32)D_800D1580` for defined modular arithmetic, including INT_MIN; comparison
  remains signed. Retain the state pointer loaded before the health store.
- When state (+0x31C), camera (+0x318) and the state's byte +0x197 are nonzero,
  submit `func_1517F488(255, 0, 0, 180, 20, camera->unk23D)`.
  The enable byte is accessed through a documented byte view of the existing
  state object; shared structure declarations are preserved.

The two helper declarations make their argument contracts explicit in this
owner. The state-change helper's existing integer-return convention is retained
and ignored. The effect helper's existing six-word void interface is retained.
No health/current-pointer/null/type validation is invented beyond the retail gates.

## Compiler, owner, Make and independent full image

Selected isolated C is warning-free. Raw body SHA-256:
`976d934344a6e53b764db94ec3b1c9376705196d78868affe11b55d962e7bd65`.
All 12 pinned relocation fields and the full body match the original
assembly object; independent links at three code/global address layouts agree.
All **327 other raw and padded owner functions** and owner data pools remain
unchanged, including the newly adopted ordinal actor lookup. All 36 inherited
owner warnings remain unchanged. The actual five-command Make recipe produces
the qualified padded object byte for byte.

An independent literal whole-image prediction changes only the target slot and
its symbol extent from 12 to 244 bytes: **192 changed bytes**, no exclusions,
metadata reordering, guards, layout or conversion inventory changes. The shadow
link uses the actual Make object's original basename to preserve the linker FILE
symbol for this owner with overflow code.

All **6,056 function addresses** and **6,055 other linked bodies** remain fixed.
All **189,088 protected Game data bytes / 720 owners** remain exact.
Production ELF SHA-256:
`880e6efb3a59c2d3b1d7d8af5f46ce08bcea6a9386940b1d9e8e14ac282b8793`.
Native installation changes exactly source, padded owner object and ELF.
All other prior **17,513 sealed inputs** remain unchanged before the explicit
new tools/documentation refresh. **1,005 focused inputs** are frozen.

## Instruction, indirect caller and native qualification

- **6,552 guest cases / 26,208 executions** compare original, isolated C,
  padded owner and actual Make object at three code/global address layouts.
  All machine states, memory, ordered accesses, saved registers and traces agree.
- All **60 reachable words** execute. The duplicate state-pointer load at +0x98
  follows an unconditional branch and is structurally unreachable; it remains
  present and is not counted as executed.
- Cases include all 256 selector bytes; exact, smaller and greater health
  amounts; negative amounts and INT_MIN; absent state/camera/enable gates;
  current actor equal to pool slot zero; helper register/home clobbers and
  explicit helper mutations of current pointer and amount.
- Guest-only alias fixtures place the command word across the selected health
  byte, or place the current-pointer word across health. The latter proves the
  current pointer is reloaded after clearing selected health, even if that store
  changes the pointer's representation. Native tests keep ordinary objects
  separate, except valid current/pool identity.
- **240 cases / 3,840 executions** run the original 19-word dispatch window
  at VA1506AEB0..1506AEFC. Its real table lookup and JALR select entry 156.
  Four independently injected callback-return values (0, 1, 80000000, FFFFFFFF)
  reach the caller, which overwrites v0 before use. Both script-index paths
  execute, including the caller's own +0x138 increment. This qualifies the
  indirect interface/window, not full script reachability or gameplay.
- **2,176 native cases each at O0/O2/O3**, with UBSan, real structure layout
  assertions and six effective controls: inverted selection, strict instead of
  inclusive boundary, unsigned comparison amount, missing current-health clear,
  wrong effect-enable byte and wrong fifth effect argument.
- Both tools copies pass six fresh tests before and after installation and their
  shared checks. Body/binding corruption and unrelated/target image corruption
  are rejected. Exact neighbor/pool identity reuses prior unchanged neighbor
  suites; those are not reported as freshly executed.

Helper services are explicit adversarial providers, not newly executed complete
implementations. Native checks normalize multibyte interaction_state numerically
when comparing byte canaries across host little-endian and guest big-endian layouts.
The production receipt's first display assertion expected an incorrectly rounded
percentage; fresh recount is 72.97%. Finalization verifies the installed image,
all prior seals and both completed installed suites without reinstalling over the
old baseline or repeating unchanged tests.

## Artifacts and next boundary

`conker/build/game-selected-actor-health-150746F0-match/` retains frozen inputs,
original/selected/owner objects, actual Make commands, literal first link,
caller census, runtime qualification, installed recount, Graphify proof,
current seals and bank receipts. Public modules are
`game_selected_actor_health_match.py`, `game_selected_actor_health_oracle.py`,
and `test_game_selected_actor_health_match.py`.

Graphify receives an eleven-file scoped AST refresh retaining prior nodes and
valid edge occurrences. The two obsolete integer-return edges are archived;
no full-corpus extraction, reclustering or centrality recalculation is claimed.

Next ordinary C placeholder: **func_1506B634**, same owner, VA1506B634,
ROM98AE4, 67 words and 24-byte frame. Audit its actual byte argument, random
remainder/zero-divisor behavior, state-byte update, float adjustment and caller
return contract before reconstruction. The scalar smoothing and other private
candidates remain uncredited. No Claude calls, host/editor/Release changes or push.
