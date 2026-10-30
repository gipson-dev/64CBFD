# 1856: Captured position effect chain match

Date: 2026-10-29. `func_150B2494`, owner `generated_DF930`.
VA `0x150B2494..0x150B2570`, ROM `0xDF944..0xDFA20`: **220 bytes /55 words**.
All55 words are reachable; no alignment tail. The former zero-return stub is
now `void func_150B2494(u8 *actor,s32 unused1,s32 unused2)`.

The routine captures actor floats at+0x14/+0x180/+0x1C before requesting a
random word. It passes the snapshot to `func_1514C678` with scale135,
arguments0/255, unsigned random remainder modulo15 plus27,7,0,float0,0,255.
It then passes the local vector to `func_151D5404` with floats1502/3000/
0.00033333333 and integers12/15/255/0, followed by `func_151D3FF4(vector,255,0)`.
Vector changes made by the penultimate provider remain visible to the last
provider. Actor changes made by the random provider cannot alter the earlier
snapshot. The random result is interpreted as an unsigned32 word for modulo.

All55 words and four call relocations emit directly from semantic C, with
no guards, inserted/omitted words, frame repair, shared-header or compiler
profile changes. The selected declarations use the existing provider widths,
including signed16 effect parameters, byte parameters and a pointer argument.
The72-byte frame saves RA at+52 and holds the12-byte vector at+60..+71;
outgoing arguments use48 bytes. Both unused callback words retain their incoming
home stores at entrySP+4/+8.

The callback table `D_8008A0B4` has eight-byte pointer/count pairs. Entry10's
pointer at VA0x8008A104 /ROM0x22EBC4 equals0x150B2494; count is-1.
The actual table dispatcher `func_15141A7C` uses `void(u8*,s32,s32)`.
Original windows15141B4C /ROM16EFFC (five words) and15141BAC /ROM16F05C
(eight words) reload the selected pointer and pass zero or a sign-extended
halfword as the third argument. A direct caller also exists in `50D80.s`:
window15027364 /ROM54814 (three words) loads the actor from the caller frame,
calls the target, and passes-1 in A2 in the delay slot. A1=9 is an entry
precondition from the preceding caller instructions. Each window executes24
cases. Earlier classification/list gates and later parent work are not claimed.

- Eight focused checks pass freshly in both tools copies, plus shared tools
  checks. Production reruns two installed checks and reuses six semantic checks
  only under complete module/input/artifact identity.
- Guest: **2,228 cases /6,684 original/raw/padded executions**, all55 words,
  literal register/private-memory/call agreement;50 access prefixes, three
  relocated layouts /90 cases,21 deliberate actor/vector alias cases.
  Aliases that overlap saved RA or incoming argument homes are excluded from
  the completed alias cases. Signed zeros, subnormals, infinities and quiet
  NaNs are copied as raw float32 words, with no arithmetic/FCSR claim.
- Native32 O0/O2/O3 each pass **1,227 cases with UBSan**, using the actual
  three-word callback type. Nine effective controls reject a wrong height
  field, scale, modulus, random base, signed remainder, priority, linear
  scale, late snapshot and cached vector. Native excludes deliberate private
  stack mutations and actor/stack aliases. All actor bytes and provider-visible
  vector words are checked. Helpers remain bounded providers; no complete
  PRNG/effect/parent/gameplay or hardware acceptance claim.
- Complete-owner compilation/padding preserves both other functions and pools.
  Three actual Make commands reproduce the qualified object with zero C
  diagnostics. The inherited duplicate12D630 Make recipe warning remains.
  All224 raw-byte/binding controls and240 whole-image corruption controls reject.

The independent complete-image prediction equals production:
**171 changed bytes =170 target code +one target extent byte**. There are no
metadata changes or image exclusions. Target extent changes from12 to220 bytes.
All6,055 other linked bodies and all addresses stay fixed. Protected Game data
remains exact across189,088 bytes /720 owners. Guards and conversion CSV are
unchanged. Only this target receives matching credit.

Fresh adopted-ELF count: **3,933/5,506 (71.43%)**, Game **3,260/4,833 (67.45%)**,
Init492/492 and Debugger181/181; zero drift. **197** more to4,130.
Tools committed first: `ba3a8d7c0768cf59bad29e597d39b3999979de09`. No push. Root README gets aggregate rows only.

The eleven-file scoped AST refresh retains or uniquely relocates all50,419 old
nodes and preserves104,518 valid old relationships. One obsolete s32 return
relationship retires for the recovered void interface. Callback registration,
both indirect windows, the direct caller and all four real helper call bindings
are recorded with source evidence. Global statistics and freshness outside the
scope remain historical; no full-corpus extraction or reclustering claim.

Private screen `func_150A23E4` remains uninstalled: its closest ordinary C form
emits54 words against55, with ten differences in the exit branch/reload shape.
Its arguments/frame/helper binding already fit; retail's extra RA reload is
not alignment and is not inserted by guards. Explicit exits, volatile controls,
no-unroll and supported O2/O1 profiles did not close it. See ignored
`conker/build/game-record-audio-submit-match/HANDOFF.md`; no matching credit.
Other parked candidates, including the mixed handwritten resume/C-entry slot
`func_150AE280`, remain uncredited with no denominator changes.

Artifacts: `conker/build/game-position-effect-chain-match/`.
Next screen `func_1518BBF4` requires the full qualification gates. No host-port,
frozen Release, saves/editor, private inputs or memory changes. Zero Claude
calls. The75% goal remains active.
