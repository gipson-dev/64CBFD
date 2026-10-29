# 1842: Coordinate query float result match

Date: 2026-10-29. Target `func_1510F648`, owner `generated_13BB20`.
VA `0x1510F648..0x1510F720`, ROM `0x13CAF8..0x13CBD0`: 216 bytes / 54 words.

The false zero-return placeholder is replaced by complete semantic C returning
f32 and taking x/y/z floats through the original F12/F14/A2 ABI. It sets context
2, truncates x/z/y, narrows x/z to signed halfwords for `func_150A64C8`, passes
its output through `func_150A44F0` and `func_150A43E0` with scratch D_800D3830,
then returns signed D_800D3300 scaled by 1/256 on true, or D_800A2D98 on false.
The final query receives full signed 32-bit x/z. Output and global changes made
by helpers are read at the original times. Only the selected return global is
loaded. The slice-local signed-word view of D_800D3300 follows its retail signed
conversion; an older pointer declaration in variables.h is not included or edited.

The compiler emits all 54 instructions. Seven expected-word guards move three
locals by four bytes within the unchanged 48-byte frame: raw SP+24/28/36 become
retail SP+28/32/40. Guard offsets are 2C,5C,64,70,84,88,90. They change only these
local address/store/load offsets; all 12 relocations (four JAL and eight HI/LO)
remain unchanged. No insertions, omissions, saved-role, frame or profile changes.
RA stays at +20, input homes at +48/+52/+56, outgoing extent 16. Source-layout
screens either retained these local differences or enlarged the frame to 56.
This is a guarded match, not a direct raw C byte match.

Eight fresh canonical methods pass independently in both tools copies, plus
shared tools checks. Installed checks rerun two methods per copy; six semantic
methods reuse only complete input/module/artifact identity.

- Guest: 2,592 cases / 7,776 executions cover every word. Retail and padded C
  agree in literal full state. Raw C agrees in registers, public memory, calls
  and mapped events/traces using only the three local slots and A2's output
  pointer during its exact address-formation through query-delay lifetime.
  Raw unused stack padding equality is not claimed. Helpers clobber caller
  registers, FP registers, HI/LO and outgoing homes; cases exercise late output
  and global mutations, signed truncation/narrowing, both return branches,
  signed zeros, integer limits and quiet NaNs. Invalid conversion uses a
  bounded guest sentinel model, not actual hardware FCSR acceptance.
- Native32 O0/O2/O3 each pass 1,080 valid-conversion cases with UBSan and reject
  eight controls: context, axis, narrowed final x, scale, cached height, fallback,
  cached output and branch. Native invalid conversions and NaN payload equality
  are not claimed.
- 45 access prefixes, three layouts / 144 rebase cases and two sparse-global
  branches pass. Original callers pass: func_15058898 at VA15058A38/ROM85EE8,
  five words / 48 cases storing F0 at actor+118; func_1511617C at VA151161A4/
  ROM143654, ten words / 24 cases converting signed integer coordinates to the
  FP ABI and storing F0 at actor+7C. Earlier parent gates are preconditions.
- Complete owner and pools preserve 13 neighbors. Five actual Make commands
  reproduce the qualified object without C diagnostics. All seven padder guard
  preimage controls reject. 228 raw-byte/binding controls and 317 whole-image
  corruption controls reject. The inherited duplicate-recipe Make warning remains.
- Independent full-image prediction equals production: 192 changed bytes,
  171 target code + 1 extent + 20 named metadata bytes. The metadata change is
  exactly one closed permutation at symbol record 0x2BA0B4: old names
  D_800A2D98/D_80090AD8/D_80090598 become order 1/2/0. Original names, fields and
  contiguous string preimages are checked; nothing is copied from the observed
  output to hide differences. No image exclusions. All 6,055 other linked
  bodies, all function addresses and protected Game data (189,088 bytes / 720
  owners) stay fixed. Seven rows append to the unchanged inherited guard prefix;
  the conversion inventory CSV remains byte-identical.

Providers are bounded models. Their complete implementations, entire parents,
gameplay and hardware behavior receive no new acceptance or C credit here.

Fresh actual adopted-ELF count: **3,919/5,506 (71.18%)**, Game **3,246/4,833
(67.16%)**, Init492/492, Debugger181/181, zero drift. **211** more to 4,130.
Tools commit first: `27bbdcce43f0ee76ac0815d369724b6d961b518e`. No push. Root README contains aggregate rows only.

Scoped AST refresh retains or uniquely relocates all 49,691 prior nodes and
retains 103,042 prior directed relationships; one obsolete s32 return reference
retires against the recovered f32 interface. Eleven source/docs/tool files are
extracted; guard CSV validation is recorded separately on the target node.
Outside manifest rows and analytics remain historical; no full-corpus extraction.

Artifacts: `conker/build/game-coordinate-query-result-match/`. Next screened
target `func_151ACA60` needs complete qualification. Parked candidates stay uncredited.
Older tools mirror preserves 1,964 inherited dirty paths plus three new modules.
No host-port, frozen Release, save/editor, private-input or memory changes.
Zero Claude calls. The 75% goal remains active.
