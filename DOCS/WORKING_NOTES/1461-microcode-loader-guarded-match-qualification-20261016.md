# Microcode Loader Guarded Match Qualification

Date: 2026-10-16. Consumer predecessor **e30824bc**, tools predecessor
**932b4de**. Continue the complete but non-matching candidate from
[Note 1460](1460-microcode-loader-recovery-and-matching-boundary-20261016.md).

## Status

**The experimental padded object now matches all 97 retail words. It is not
installed in production.** The complete semantic C emits **96 words** with
the original **frame 0x30**. Twenty-three relocation-aware guards recover
retail's address materialization, schedule and temporary-register allocation.
This is a **guarded match, not a direct C match**. The production source,
guard manifest, linked image and matching percentages remain unchanged.

Target: func_1501CC3C in conker/src/game/generated_49D30.c, VA
**0x1501CC3C..0x1501CDC0**, ROM **0x4A0EC..0x4A270**. Keep the existing
**O2/g3/no-unroll** profile, S0/RA saves and all original homes: range at
**SP+0x20**, paired offset at **SP+0x28**, variant at **SP+0x2C**.
The recovered interface remains **void(void)**; the existing Init DMA
provider remains **s32(s32, void *, u32, s32)** and is not modified.

## Source And Guard Boundary

A flat four-word record view recovers the original opening temporaries and
**add-before-shift** paired index. Each row is text start/end, data start/end,
relative to the ROM base. Preserve the unsigned input byte promoted to a word,
signed cache bytes, exactly-one full-word flag, four blocking DMA packets,
post-DMA table reloads and cache/data-pointer publication from Note 1460.

The new experiment retains **25 measured source configurations**. Flat s32
and u32 table forms emit **96 words / frame 0x30**; a nested first publication
emits 97/frame0x30 but duplicates a table load and changes its lifetime.
Do not select the smaller positional difference count as proof of a better fit.
Use the clean, separate-publication 96-word body and account for every guard.

Raw C object SHA-256:
**fcb10bf8144b781ba048515f26237c72c7d1aa29d1576c17d1e9819287c09e82**.
Pin all **34 relocation bindings**, reject private pools, preserve all **56
raw owner neighbors**, including the already matched **239-word** parent.

Exactly three bounded groups, using offsets in the raw 96-word function:

- **Five schedule/branch guards:** +0x70 repairs the cached-hit branch span
  after the one-word expansion; +0x88/+0x8C/+0x90/+0x94 reorder A3 setup and
  the three existing spill stores. No home address or frame repair.
- **Eleven primary-publication guards:** +0xAC, +0xB8, +0xBC, +0xC0, +0xC4,
  +0xC8, +0xCC, +0xD0, +0xD4, +0xD8 and +0xDC. Recover the full destination
  address in T2, before-store data-field loads and V1 start lifetime. This
  expands LUI/SW-lo to LUI/ADDIU/SW-zero. Move the existing call/argument
  schedule and emit the original size subtraction as its delay slot after
  raw +0xDC. The inserted word is the delay-slot subtraction; the net growth
  comes from address materialization, not dummy padding or a missing action.
- **Seven final register-cycle guards:** +0x134, +0x138, +0x140, +0x14C,
  +0x150, +0x15C and +0x168. Recover retail's final base/start/span/end
  temporaries. S0, RA, field offsets, calls and their lifetimes are unchanged.

All other words/bindings remain identical under the explicit one-word position
map. Pin the complete original GNU words and binding map as well. Append only
these 23 experimental guard rows to the frozen manifest; preserve its entire
existing byte prefix and CRLF lines. **The live manifest is not changed yet.**

## Fresh Qualification

All **seven final tests pass in 42.751s**, no skips:

```sh
python3 -m tools.experiments.game_microcode_loader_lifetimes --qualify
python3 -m unittest tools.tests.test_game_microcode_loader_lifetimes \
  tools.tests.test_game_microcode_loader_native -v
```

- **770 three-way guest cases** compare original assembly, raw 96-word C and
  guarded 97-word emission against the independent reference. Compare raw C's
  complete public RAM, packets and publication snapshots; compare original
  and guarded versions' literal private RAM/GPR/FPR/access/delay state too.
  Every raw 96-word and normalized 97-word instruction position executes.
- **80 positive callback cases**, all requested gates fired, and **24 real
  eight-record table cases** retain correct cached locals and live reloads.
- **449 native32 cases each at O2 and O0**, UBSan, no fwrapv, execute separate
  typed caller/body/provider units. Use actual SDK struct104 with selector
  offset 43; compare all **25,240 public bytes** and surrounding state/table/
  scalar/arena canaries. Normalize only explicit numeric lanes and declared
  pointer fields. Four functional controls return mismatch **22**, never
  compiler failures or sanitizer/signal traps: unsigned cache, nonzero flag,
  early cache publication and a stale text span.
- **192 connected three-way cases** execute the real **239-word parent**,
  **61-word two-row setup** and loader instead of the old microcode hook.
  Every setup word executes. Queue/cache/PI leaves remain bounded.
- **346 fired original/guarded memory-fault prefix pairs:** 105 isolated and
  241 across the real parent/setup/loader chain. Raw C's differing schedule
  is not represented as fault-order equivalent, nor are PI hardware faults.
- Three original GNU and three independently linked guarded-C rebases compare
  all 97 words, including HI/LO carries. Reject every raw 96-word corruption,
  every original 97-word corruption, all 34 raw bindings plus an extra,
  private pools, the original binding-map fingerprint and **253 guard-field
  corruptions**. All **135 production input hashes** are unchanged.

The original eight-record table and valid transfer lengths are retained.
High selector cases use an explicitly synthetic extended table; DMA payloads
are deterministic test bytes, not original microcode. No OS PI/cache/queue
hardware, complete startup, natural gameplay or host-port acceptance claim.
The prior unchanged seven-test research receipt remains in Note 1460; it was
not rerun or counted as fresh coverage in this checkpoint.

## Advisory Disposition

One bounded, tool-free Claude analysis used the existing claude.ai/firstParty
Pro route and default model; effective tools=[] and mcp_servers=[], one turn,
exit0, no tool use, no provider/model switch or retries. Packet SHA-256:
**004def74a3d905d4c459760621d827add14e2d3351232dcb396064ca66269013**.
Packet, answer, stream and receipt are ignored target diagnostics.

Accept the independently verified address-materialization description. Test
all three concrete proposals: a named publication pointer and named data
pointer each emit **96/frame0x38**, so reject them; byte-pointer arithmetic is
identical to **96/frame0x30**. Reject the stronger claim that no source-only
solution can exist: there is no exhaustive proof. Direct emission remains a
possible future improvement, not a claim of this guarded qualification.

## Bank And Remaining Gates

Tools **27dc235** banks all four new files first. Both copies pass eight
Windows AST checks and all eleven WSL padder checks without skips: active
**0.030s + 0.020s**, mirror **0.031s + 0.018s**. Consumer tools-check passes.
Preserve mirror HEAD **ddbdd16b53ce60b054fb6e11bf0649a41f48375a**, all **931**
initial dirty-file hashes and **935** final paths; four new file pairs match.
No mirror commit/reset, push, host-port or frozen Release action.

- [x] Qualify the complete guarded 97-word match without frame/home/save repairs.
- [x] Pass native32, independent rebases, real parent/setup/loader execution and applicable ordered/fault checks.
- [x] Bank tools first and the consumer handoff; retain the uninstalled production baseline.
- [ ] Qualify the other actual caller, func_15007B3C, at its real call/post-call cut; keep full startup and hardware acceptance separate.
- [ ] Reproduce the predecessor and independently predict every ELF byte before installing the source and exactly 23 guard rows.
- [ ] Complete the normal dependency rebuild, installed image/protected-data/input audit and fresh official progress, then bank tools first and the consumer pin/docs. Root README gets aggregate rows only.

Next is **installation qualification for this same function**, not another
conversion batch. The literal production ELF remains
**5ae0082dd77652314c8e63569a43439a330d133b749907fa5db2d5b76fe41d9e**.
Note 1459's measured Game **2,936/4,828 (60.81%)**, total **3,609/5,501
(65.61%)**, different **1,892**, zero drift and conversion **5,501/6,044**
are preserved, not freshly rebuilt or increased. Root README is unchanged.
Keep timing's 141 differences and the wider Game goal open.
