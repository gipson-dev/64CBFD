# Bone-selected ground hit and trail recovery - 2026-11-17

`void func_151AABC4(u8 *actor, u8 bone)` replaces the zero-return placeholder
with the complete bone-selected ground-hit and angular-trail constructor.
The complete **126-word / 504-byte slot and frame 0xC8** are byte-exact.
**96 words emit directly from C**; 30 relocation-aware expected-word guards
normalize one proved private initialization block. There are **no insertions,
omissions, dummy locals, explicit register bindings or profile changes**.
VA 151AABC4..151AADBC, ROM 1D8074..1D826C. This is a guarded C match.

Accepted production total **4,529 / 5,514 (82.14%)**, Game **3,856 / 4,841
(79.65%)**, Init 492/492, Debugger 181/181; zero drift, **985** still different.
**158 further matches** are needed for the active 85% goal. Conversion stays
5,514/6,048 (91.17%), 86.19% of bytes. Root README receives only the aggregate
snapshot date and Total/Game matching rows.

## Recovered behavior and actual interfaces

Null actor and null actor+0x1D4 matrix links return without helpers. Otherwise
the callback captures `func_151D8E20()`'s byte selector, freshly reloads the
matrix after that mutable provider, and resolves the selected bone through
`D_800A8F70[bone]` and `func_15142314`. The actual four-byte table is **5,10,19,23**.
The six complete callers select indices **0,1,0,1,2,3**; native qualification
uses that valid producer domain. Wider byte-index and incoming-word probes
remain guest-only rather than portable array-bound claims.

`func_1504715C` initializes the actual typed 36-byte `HeightResult71820`.
The upper bound is rounded as `boneY + 50.0f`; the lower bound is separately
rounded as `upper - 100.0f`. The query's X/Z copy and the ordered pair of FP
operations are retained. A zero `func_1504697C` result skips both effects.
On a hit, X/Z are freshly read from the exposed bone output and Y from the
post-query surface. The first call is
`func_151DBCBC(selector,40.0f,150,(s32)surface.vertices,&position,255,1)`.

The later `trail.position = position` deliberately occurs **after** this first
emitter: provider changes of that point must reach the trail submission.
Its coefficient globals are likewise read after the emitter. The final call
passes the separate eight-byte angular header, 68-byte localized descriptor,
surface address as an o32 word, slot 255 and context 1 to `func_15153F18`.
Both real emitter signatures, field widths and the height-result interface
are audited; the s32 address arguments preserve the existing 32-bit ABI.

The angular header has all eight bytes defined: 0/255 and -64/26 halfwords.
The trail has **65 defined bytes** and three indeterminate bytes at +0x35..0x37.
It retains time 2.5, five mutable coefficients, count 3/3, request selection
3/1, duration 30/20, mode 155/100, the saved byte selector, zero chance,
16/15 values and zero request word. Existing consumer field names are reused;
no meaning is invented for unmodeled fields or uninitialized bytes.

## Natural frame, fitting and proof

Seventeen complete source forms (v0..v16) were compiled. The first has the
correct 126-word length but a frame eight bytes too short. Array versus
three-float view and contiguous-aggregate probes do not recover that frame.
Giving the real query upper bound its own used float local recovers **frame
0xC8 and all original homes**, without padding or dummy storage. Keeping the
original query-field expression order also recovers every opening FP word.
Bounded field-order probes isolate the remaining descriptor schedule.

Selected v13 raw SHA256:
`374f77d57d574b0c8f17cf39320aff3f4a93f9cbbc52ac0685be609c48ad3585`.
Complete retail SHA256:
`cccebe7380a2790a430ef60eb9d5566f3624395a7810d4c67d7b2c0e6140610c`.

All 30 guards lie in **+0xE8..+0x16C**. They preserve the independent position
copy-address setup, equivalent constant-register roles and the timing of
private stores and global coefficient address materialization. Expected raw
words and exact relocation ownership are checked; no arithmetic operand or
control-flow behavior is substituted. Original 18 bindings are accounted for.

The complete instruction-driven proof passes **four paths and all 126 words**.
It compares ordered FP/FCSR transitions, arbitrary public aliases, **all 216
private/incoming-home bytes at every call and return**, complete return
registers and callee-save restoration. Providers can mutate previously exposed
bone/query/surface/hit ranges and public state; no immutable-output assumption
is used. Five semantic instruction controls reject. A closed T8/T9 allocation
cycle in the private block is a passing positive across all four paths.

## Fresh focused qualification

All **five maintained tests** pass in primary tools, the isolated sibling-tools
overlay and installed production at identical eight-file task fingerprints.

- Both real complete-owner padders preserve the 126-word body, all **40
  neighbors** and pools. **144 raw-word/binding corruptions** and **120 stale
  CSV controls** reject. Twelve independent GNU links compare both padded
  owners with independently assembled original code over four code/data
  layouts, including independent table/coefficient HI16 carries.
- Independent guest reference: **858 cases per retail/raw/strict/layout
  stream**, all 126 words, all byte selector values, actor/matrix/null/query
  paths, two stack phases and provider mutations. Ten cases are explicitly
  guest-only. Call arguments, public memory and all defined descriptor fields
  agree; five semantic defects reject.
- Native32: **848 cases each at O0/O2/O3**, SDK types, strict aliasing and UB
  traps, all 512 actor bytes, matrix identity, four table bytes, five coefficient
  words, marker and complete helper observations. Six broken C bodies compile
  and exit 3; all nine runs have their expected outcome. Unwritten trail bytes
  are never inspected, and private/incoming-stack aliases are not native claims.
- **Six complete 11-word retail callers**, each **168 cases per stream**,
  execute the complete constructor and every caller word. All are literal in
  production; each wrong-bone control rejects. No caller or shared header changes.
- All six complete providers are verified literal in production: selector
  19 words, bone lookup 49, surface initializer 89, query 161, first emitter
  113 and trail emitter 168. Their effects remain bounded services in this
  focused suite; complete helper systems or gameplay are not re-executed here.

The relation covers normal mapped/aligned public RAM with a disjoint private
stack and bounded o32 providers. Public alias coverage in the guest/proof is
not a general ISO C aliasing guarantee. Hardware traps/fault prefixes, runtime
gameplay and portable initialization of automatic holes are not claimed.
The guarded production stream separately has complete retail byte identity.

## Production and retained evidence

Predecessor consumer `429b751c`, tools `21d979d`. The **1,429-input** initial
snapshot and **1,437-input** maintained snapshot use only verified immutable
snapshot links and copied task bytes, never links to live worktree files.
Actual Make shadow and production compile the C; no prebuilt object is installed.
Exactly source, guard CSV, owner object and ELF change; **1,433 frozen inputs
remain unchanged**. Only one of 698 objects changes. All other **6,050 function
bodies**, all **6,051 addresses**, all 40 owner neighbors, normalized pools and
register metadata agree. Conversion CSV and build profiles remain unchanged.
The old guard file is an exact byte prefix with precisely 30 appended rows.

Complete production ELF equals its independent prediction: **559
changed bytes, zero exclusions**. All **20,289 named definitions**
agree except target extent 504, with explicit metadata serialization accounting.
Four symbol-value/name, protected-data and target-word corruptions reject.
All **189,088 protected bytes / 720 owners** remain exact.
Production ELF SHA256: `88c9ce8da565409f3219a394f71fb01bb8958449207e7a067901e96338a98f19`.

Prepared qualification requires the retained snapshot and a fresh owned output
directory supplied by `CBFD_BONE_HIT_WORK`. Run
`python3 -m unittest tools.tests.test_game_bone_hit_151aabc4_recovery -v`.
Receipts: `conker/build/game-next-151aabc4-private/adoption/`, including actual
module import origins and independently sealed primary/sibling/installed runs.
The separate sibling's 2,434 changed paths and 339 checked dependencies remain
unchanged. At `64CBFDOGL` only `.codex` and `recomp_scene` remain, with no source
checkout to synchronize. No host, Release or save change. Zero Claude calls,
no push or dependency upgrade. Graphify is refreshed through a scoped AST
merge with old-ID retention; no full-corpus re-extraction is claimed.
Tools are committed before the consumer source/docs/pin.

Next inspect `func_151AADF8` from the actual unmatched list. The 85% goal
remains active.
