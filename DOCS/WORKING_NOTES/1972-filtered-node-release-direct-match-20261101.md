# 1972 - Filtered linked-node release recovered directly from C

`func_15030310` now emits all **53 retail words**, with its natural **48-byte
frame and zero word guards**. Production Make and the independent Native ELF
recount confirm **4,040/5,507 (73.36%)**, Game **3,367/4,834 (69.65%)**, zero
address drift and 1,467 still different. Exactly one match is added. The 75%
threshold is 4,131: **91 more** matches are needed; the wider goal remains active.

## Recovered behavior and ABI

The actual unmatched inventory identified this false zero-return placeholder in
`generated_5D2C0`: VA `0x15030310..0x150303E4`, ROM `0x5D7C0..0x5D894`.
Restore `s32 func_15030310(u8 *actor, s32 filter, u32 skip)` and its local
prototype. The existing integer-carrier wrapper explicitly casts its first
argument to a pointer; all eight wrapper words remain unchanged.

An actor key of zero at byte +0x3B returns zero without reading the list head.
Otherwise capture the initial `D_800C3EE0` head and traverse next pointers at
node +0x54. Reload the actor key each iteration and compare it with node byte
+0; compare the complete signed filter with unsigned node byte +6. Negative
or greater-than-255 filters do not match. Cache next before releasing a node,
because the cleanup helper may unlink/free it and change the actor key or head.

For matching records, decrement a nonzero counter other than 255 and continue.
Counter zero releases one match and stops; 255 releases every later match.
The sentinel is checked on every iteration: **256 skips the first match,
becomes 255, then releases all subsequent matches**. Keep the counter unsigned
32-bit, rather than narrowing it or introducing signed decrement overflow.
Call `func_15030158(current, 0)` and return one if any release occurred.
The selected comment and local names describe this behavior without claiming a
larger gameplay meaning. Actor validity and a valid acyclic list remain preconditions.

The explicit `current = next; continue;` countdown arm recovers the original
schedule. Eight first screens missed; four of eight second screens emit all
53 words directly under the existing O2/g3/mips2/o32 profile. No guard, register
patch, compiler-profile change or inline assembly is introduced. Raw C SHA-256:
`df93afbea48b766642a70c3b64c13cac15c138f8be5fb44078bc75b9e77bb65c`.
All three relocation bindings equal the independently assembled original.

## Qualification and limits

- Complete raw and padded owners preserve **39 neighbors** and normalized pools.
  Target-owner diagnostics remain **0 to 0**. The actual three-command generated
  owner recipe produces the identical qualified padded object, with the original
  `jtbl_80096F40_game` rodata binding. Existing unrelated duplicate Make recipes
  and inherited diagnostics from other owners remain recorded in the full build.
- **18,144 guest cases / 36,288 executions** pass at three independent GNU link
  layouts. All **53 words** execute. Original/C memory, GPR, FPR, HI/LO and access
  traces agree. An independent semantic reference checks full public memory,
  release order and result. Poisoned freed nodes, live actor-key changes, changed
  global heads, full-width filters/counters and stack phases are covered.
- **113 access-prefix pairs / 226 executions** preserve memory/access traces.
  These do not claim complete fault register/PC equality or portable C fault
  behavior. Two sparse zero-key executions omit the head mapping entirely.
- Native32 O0/O2/O3 each pass **3,024 cases / 27,216 executions**, using UBSan,
  whole actor/node byte comparisons and eight effective controls: missing zero
  gate, reloading next after release, cached actor key, wrong filter byte,
  narrowed filter, narrowed countdown, wrong sentinel and wrong return.
- The original **102-word helper** is equal to its retained linked body.
  **288 cases / 576 executions** connect it to the root, checking deferred
  cleanup/resource call order, head/prev/next unlinking, actor/head mutations and
  final node poisoning. **83 helper words execute**; the 19 remaining PCs are
  recorded explicitly. This qualifies the root's immediate-zero route only.
  Lower resource/cleanup functions are modeled stubs, not complete engine proof.
- The only aligned direct JAL is **ROM 0x5D7A8**, in `func_150302F0`; no aligned
  direct J or pointer literal targets the root. **768 cases / 1,536 executions**
  connect all eight original wrapper words, the root and original helper. Full
  filter forwarding and forced A2=255 pass with four incoming A2 poisons. The
  wrapper's C return is void; its machine V0 observation does not change that ABI.
- Both tools checkouts pass **five target tests plus shared checks before and
  after installation**. The reusable-test refactor exposed two Python scope
  errors; those failed attempts are retained, corrected, and superseded by full
  successful runs. Private compiler/runtime evidence was unaffected.

## Production and retained artifacts

Independent whole-image prediction changes only the 212-byte target slot and
its ELF symbol extent from **12 to 212 bytes**. Private and production full links
are literally equal to that prediction, with **zero exclusions**. All **6,052
function addresses**, **6,051 other bodies**, named symbol definitions, ELF
length, linker map and guard CSV remain fixed. All **189,088 protected Game bytes
across 720 owners** remain exact. No dependent object changes are unplanned.
Native's actual ELF recount independently verifies the additional match.

Production ELF SHA-256:
`860997333f77ca8592380dc62a6be70141037cd54e8ae01e8455036e0d9e68fe`.

Stage `conker/build/game-filtered-node-release-15030310-match/` retains the frozen
input snapshot, **23 prepared-artifact pins**, all private/public test receipts,
actual Make commands/objects, image predictor, production and Native recounts,
seal, graph proof and final handoff. Four new public modules qualify the source,
guest/original-helper/wrapper, native controls and integration tests. Original
assembly, private candidates, current audit1968 and unrelated mirror work remain
preserved. The separately requested cleanup archived older completed checkpoints
with SHA-256-verified restoration; historical suites need explicit restoration.
No host port or frozen Release changes are made. Routine work uses zero Claude
calls. Root README receives aggregate rows only. Tools commit precedes consumer;
no push is performed.

Next verified unmatched candidate: **`func_15187EC0`**, 52 words in
`generated_1B5370`, a five-record initializer with byte arguments, a float field,
zeroed trailing vector and post-helper live counter reload. Recover caller ABI
and signed counter boundaries before installation. `func_150A76F0` uses a
handwritten nonstandard register ABI and belongs to the separate restoration
stream. Other parked private candidates remain uncredited and require explicit
snapshot rebasing before reuse.
