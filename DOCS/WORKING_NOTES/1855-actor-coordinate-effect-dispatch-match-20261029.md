# 1855: Actor coordinate effect callback match

Date: 2026-10-29. Target `func_150D8A34`, owner `generated_105760`.
Body VA `0x150D8A34..0x150D8B0C`, ROM `0x105EE4..0x105FBC`:
**216 bytes /54 words**. The original zero alignment word at VA0x150D8B0C /
ROM0x105FBC remains, giving the classifier its original220-byte /55-word slot.

The placeholder becomes `void func_150D8A34(u8 *owner, s32 selector, s32 unused)`.
When owner+0x1D4 is nonnull, it asks `func_150D88E0` for a three-float attachment
position using the selector's low unsigned byte. It calls `func_151875E0` with
that position, integers30/15/7, and current `D_800A0B30` / `D_800A0B34` floats.
It then calls `func_15165F80` with `(-1,trunc(x),trunc(owner+0x180+4.0f),
trunc(z),4,50,0,255,0)`. The owner and vector values are read after the effect
call, preserving changes made by providers. The initial resource gate is not
repeated after a provider clears that field.

Both the initial byte-parameter candidate and the selected complete-word
callback candidate emit the same54 words and seven relocations directly.
The selected form matches the actual callback type `void(u8*,s32,s32)` and
narrows only the selector sent to the coordinate helper. It retains the unused
third argument's incoming word store. Frame64 saves RA at+44; the float vector
occupies+52..+63. Incoming words live at entrySP+0/+4/+8, with the owner home
stored conditionally in the first helper's delay slot. The final nine-argument
call uses36 outgoing bytes. There are no guards, frame adjustments, inserted
or omitted words, shared-header changes or compiler-profile changes.

The actual registration is `D_8008A0B4[8]`, an eight-byte callback/count pair.
Its pointer at VA0x8008A0F4 /ROM0x22EBB4 is0x150D8A34; count is-1. The original
dispatcher is `func_15141A7C` in `game_16EE20`, not a generic effect dispatcher
from another table. The existing C dispatcher uses complete-word callback
arguments. The coordinate helper remains a separate unrecovered C placeholder;
its original instructions are used for bounded interface tests, with no helper
adoption or helper matching credit.

- Eight focused methods pass freshly in both tools copies, plus shared tools
  checks. Production reruns two installed methods per copy and reuses six
  semantic checks only under exact input/module/artifact identity. The older
  tools mirror retains2,003 inherited dirty paths and receives three new
  qualification files without a mirror commit.
- Guest: **5,864 cases /17,592 original/raw/padded executions**, all54 body
  words and literal GPR/FPR/private-memory/call agreement. Cases include all256
  selector bytes, complete-word selectors and unused arguments, null/nonzero
  resource words, signed zeros, subnormals, finite conversion boundaries,
  infinities and quiet NaNs, globals changed by providers, retained-vector
  mutations and deliberate incoming-owner-home changes. There are81 access
  prefix comparisons, three layouts /72 relocated cases, and24 vector/height
  memory-alias cases. Invalid float-to-int tests use the bounded low-word
  integer-indefinite model; hardware FCSR/traps are not claimed.
- Native32 O0/O2/O3 each pass **1,166 cases with UBSan**. Calls use the actual
  three-word callback type, with no incompatible callback-pointer cast. All
  float-to-int operands remain finite and within signed32 range; the same
  condition applies to every independently compiled negative control.
  Unexposed argument-home mutations and guest private-address aliases are
  excluded from native claims. All owner bytes and provider-visible values
  are checked. Nine effective controls reject inverted gating, signed selector
  narrowing, wrong effect kind, wrong height increment, wrong final axis,
  wrong priority, cached height, repeated gating and cached vector components.
- The original80-word `func_150D88E0` executes64 connected cases for selectors
  3..6 with a checked matrix-provider boundary. Those selectors choose matrix
  records18/21/15/24 and their original local offsets. The helper's default
  selector paths are not promoted to portable native behavior or complete
  helper recovery. Its production C placeholder remains unchanged.
- Two original table-reloading windows in `func_15141A7C` execute48 cases each:
  VA0x15141B4C /ROM0x16EFFC, five words, clears the third argument in the JALR
  delay slot; VA0x15141BAC /ROM0x16F05C, eight words, reloads the callback and
  sign-extends the record's halfword into the unused third argument. Both use
  the real table/index. Earlier classification/list conditions and later parent
  work remain preconditions; no complete-parent or gameplay claim.
- Complete-owner compilation/padding preserves eight neighbors and pools.
  Three actual Make commands reproduce the exact object with zero C
  diagnostics. The inherited duplicate12D630 Make recipe warning remains.
  All223 raw-byte/binding controls and348 whole-image corruption controls reject.

Independent prediction equals production across the **complete ELF**:
**188 changed bytes =171 target code +one extent +16 named metadata bytes**.
The metadata is exactly two adjacent symbol/string permutations:

- At symbol record0x2DA2B4, `(D_800A0B34,D_800A06D4)` becomes the reverse order.
- At symbol record0x2DAB74, `(D_800A0B30,D_800A06D0)` becomes the reverse order.

The predictor verifies the original names, definitions and contiguous string
blocks before constructing those permutations. All symbol definitions/values
remain identical except the declared target extent change from12 to216 bytes.
There is no blanket symbol/string-table exclusion. All6,055 other linked
bodies and all addresses remain fixed; protected Game data stays exact across
189,088 bytes /720 owners. The guard manifest, conversion CSV and alignment
word are unchanged.

Fresh adopted-ELF count: **3,932/5,506 (71.41%)**, Game **3,259/4,833 (67.43%)**,
Init492/492 and Debugger181/181, zero drift. **198** more to4,130.
Tools committed first: `b0ed1b083b0019052509c6d42a5c140c21e8fe5f`. No push. Root README gets aggregate rows only.

The scoped eleven-file AST refresh preserves all50,365 previous nodes or unique
relocations and104,396 valid old relationships. One obsolete s32 return edge
retires for the recovered void callback. Complete callback words, original table
registration and both dispatcher windows, the alignment word and bounded helper
evidence are attached. Outside-scope freshness and global statistics remain
historical; no full-corpus extraction or reclustering claim.

Artifacts: `conker/build/game-actor-coordinate-effect-dispatch-match/`.
Next screen `func_150A23E4` still needs all qualification gates. The mixed handwritten
stack-resume/C-entry slot `func_150AE280`, `func_151A084C` and other private
candidates remain parked and uncredited. No denominator change or ASM-as-C
credit. No host-port, frozen Release, save/editor, private-input or memory
changes. Zero Claude calls. The full75% goal remains active.
