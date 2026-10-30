# 1888 - Signed ring render submission callback

Verified 2026-10-30. Function `func_151668B8`, owner
`conker/src/game/generated_193430.c`, retail VA `0x151668B8..0x15166998`.
The 224-byte body occupies a 232-byte slot through `0x151669A0`, including
two unchanged zero alignment words. ROM slot `0x193D68..0x193E50`.

## Recovered behavior and ABI

The callback takes and returns a `Gfx *` cursor, plus three unused ABI words.
The real indirect dispatcher at `0x1516774C..0x151677A8` selects record four
from `D_8008B4A8`, stride 52, callback offset 20. The sole aligned retail
pointer is at ROM `0x23004C`; no direct aligned JAL exists. The dispatcher
passes the record index, saved packed word and its signed high half, then
consumes the returned cursor before writing its geometry command.

The routine captures `D_800DCE40` as a signed halfword, adds 128 with halfword
truncation, and clears the stored value only when the reloaded signed value
is at least 1280. Negative offsets and signed wrap remain meaningful; this
is not an unsigned modulo conversion. It publishes the resource source,
captured offset and mode, then calls `func_15094F70` with nine ABI words.
The returned cursor feeds `func_15142FBC`. Flags and both table words are
read after the first provider, allowing its side effects to remain visible.
The local sync byte starts at one. The final renderer's cursor is returned.
The first helper retains its existing s32 cursor ABI with explicit SDK32
casts; its exact source-record layout is reused. No shared header changes.

## Compiler match and normalization

Retail O2/g3 produces 56 body words, frame 56, RA at SP+44, sync at SP+55,
and unused incoming argument homes at entry-SP+4/+8/+12. All 18 bindings
match. Words 0 through 42 already match directly. Five expected-word guards
at word indices 43,44,46,47,51 normalize independent table-read order and
caller-saved temporary roles. There are no inserted or omitted words.

The symbolic proof covers bytes `[172,208)`, including the unchanged JAL
at byte 200 and its argument-update delay slot. ABI-live GPR argument DAGs,
SP, RA, saved registers and memory agree. All FPRs are untouched. Temporary
register values and the order of the two private reads differ in raw code;
all-register or raw fault-prefix equality is not claimed. Ten deliberately
wrong preimages/bindings are rejected by the actual generated-object padder.
Three independent GNU rebase layouts exercise relocation carries.

## Qualification evidence

Artifacts are retained under `conker/build/game-ring-render-submit-151668B8-match/`.

- 2,688 guest cases / 8,064 executions cover all 56 root words. Connected
  original first-wrapper (30 words), descriptor updater (29) and final
  renderer (34) visit 92 of 93 helper words. The lower ten-argument draw
  service is explicitly bounded and checks its descriptor and packet.
- Original versus normalized state, traces and 67 access-fault cutoffs agree,
  including six branch-delay cuts. Raw code agrees on ABI-visible state and
  public effects. Nine independent rebased cases pass.
- Native SDK32 tests at O0/O2/O3 each pass 1,572,864 cases, covering all 65,536
  starting halfword bit patterns, both descriptor source modes, all provider
  mutation combinations, cache-hit/miss paths and output/scratch canaries.
  They execute the real first-wrapper, descriptor updater and renderer C.
  UBSan is enabled. Twelve effective native and IDO semantic controls fail
  for their intended packet/state reasons; compiler failures are not controls.
- The original 23-word indirect caller window tests null/non-null callback
  and display-list paths, four-word marshalling, signed high-half handling
  and returned-cursor consumption. This is a bounded window, not complete
  parent execution or hardware rendering acceptance.
- Four owner neighbors, pools and definitions remain identical. All three
  actual Make compiler/padder/assembler commands reproduce the qualified
  object with no diagnostics and no profile changes.
- Independent full-image prediction equals the first real link with zero
  exclusions: 192 changed bytes = 177 target code + one symbol-extent byte
  + 14 explicitly predicted symbol-table/string serialization bytes.
  Only the complete named records `D_800DCE40` and `D_8008F890` swap order;
  their definitions and addresses remain intact. All 6,055 other linked
  bodies and every function address remain fixed. All 189,088 Game data
  bytes across 720 owners remain exact. Inherited guards are unchanged.
- Eight fresh canonical methods and shared tools checks pass independently
  in both tools copies. Installed checks are fresh for source/inputs/image;
  six unchanged semantic checks are reused by complete fingerprints.

## Banked status and continuation

Tools commit: `3691b933a4ac5ad0c7ba92c6c70ca71353d2f2ff`, banked before the consumer pin. The independently dirty
older tools mirror is preserved without a commit or reset. The fresh adopted
ELF recount gives Total **3,965/5,506 (72.01%)**, Game **3,292/4,833 (68.12%)**,
Init 492/492 and Debugger 181/181, with zero drift. Inventory CSV is unchanged.
The target is credited only after complete qualification, actual Make,
production/adoption, recount, docs, graph and commit audits. The root README
receives only two aggregate status-row changes. Scoped Graphify refresh retains
all prior nodes and valid relationships; it does not claim full extraction,
new clustering or global centrality. No push or hardware claim.

The 75% goal remains active: **165** more exact functions to 4,130. Next private
screen: `func_1500F290`. Existing private candidates remain uncredited.
