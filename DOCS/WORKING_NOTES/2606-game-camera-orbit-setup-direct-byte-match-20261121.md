# Note 2606: Camera orbit setup direct byte match

Date: 2026-11-21. Consumer baseline `283c19887aefd1317a89949f9a1ce2215c9fc4d1`;
tools baseline `42c50ce3bf3f7e12f6d479d6d8852fd0acfb0138`. Qualified tools commit: `0d9cb61d9f34043f46007d256265371fdca5163f`.

`func_15125A6C` replaces its zero-return placeholder with the complete state-0x2A
camera orbit setup. All **117 words / 468 bytes**, the **72-byte frame**, saved
S0/S1/RA, stack float homes and **25 relocation sites** emit directly from C.
There are **zero guards, insertions or omissions**. Its recovered interface is
`void func_15125A6C(struct108 *camera)`. All **44 neighboring functions**, pools
and the five existing compiler warnings are unchanged.

Production recount: **4,590 / 5,528 (83.03%)** total and **3,917 / 4,855 (80.68%)**
Game, zero address drift and **938** still different. Init 492/492 and Debugger
181/181 remain exact. **109 more** matches reach 85% at this denominator.
Converted rows do not change: the former placeholder already counted as C.
The root README receives only its two aggregate matching rows.

## Recovered behavior and source shape

Owner `game_14FF90`; VA `0x15125A6C..0x15125C40`, ROM
`0x152F1C..0x1530F0`. State byte +0x23E selects the orbit setup. The routine
snapshots the selected actor's heading before any command-5 callback. Unless
the mode word is exactly 0x40000, it queues command 5 and then sets pending
byte +0x7E4. It selects global mode 3 and builds the inline setup at 0x800C3600.

The heading and heading-minus-90 phases use the two original conversion
coefficients. Their sine/cosine components combine with radii 138 and 46 and
the current actor position; vertical offset is 96. The remaining setup stores
include -180, heading-minus-180 and a **single-byte** clear at +0x5C, followed
by command 7 with the setup address. In other states, a nonzero pending byte
queues command 6 before that byte is cleared. Callback mutations remain
visible to the subsequent actor/coefficient reloads.

The broad SDK incorrectly declares 0x800C3600 as a pointer; retail addresses
an inline object. A private `CameraOrbitSetup14FF90` view names its measured
fields and preserves the three bytes after +0x5C. The legacy extern is renamed
only while this owner includes `variables.h`; no shared SDK declarations are
changed. The command provider's real signature uses `u8 *`, command and payload.
The source retains four unused scalar locals, with an explanatory comment,
to preserve the retail frame and floating homes under IDO O2/g3. Earlier
layouts had the right length but different register/home assignments and were
rejected. The obsolete commented draft is removed.

## Validation and limits

Raw payload SHA256:
`ef4d58c60a754873d1c050cb07ac59d5608d0f871bf00f041faf446f8770f992`.
Raw C, independently assembled retail and padded C agree in every word and
binding. The natural mixed GLOBAL_ASM Make recipe runs its five commands
under the existing profile and reproduces the whole qualified object.

The independent guest model passes **7,416 cases per stream** for retail,
raw and padded bodies, comparing complete public RAM, setup snapshots, modeled
registers, ordered accesses and private stack bytes. It exercises all 256 state
bytes, pending-byte edges, exact versus bitwise mode tests, phase coefficients,
queue boundaries, callback mutations and a guest actor/setup alias. Four
instruction mutations are rejected. All **116 normal-entry reachable words**
are executed. Word 104 (byte offset 416), a duplicate pending-byte load, is
statically unreachable from normal entry; a decoded control-flow traversal
proves that distinction. All **117 payload words** still match literally.

An additional **108 cases per stream** execute the original **41-word**
`func_1512D560` queue helper, visiting all its words. The original helper also
matches the sealed baseline ELF. The queue uses 0xB0-byte records, cursor at
+0xAC, and wraps only when the increment reaches 20. Other callback-mutation
cases deliberately use the bounded provider contract.

Native SDK32 checks pass **6,264 cases each at O0/O2/O3**, with strict aliasing,
UBSan traps, actual SDK camera/actor types, typed setup member aliases and the
recovered queue C body. Six source controls fail. The wrong-mode control would
activate intentionally null inactive actors, so those newly invalid rows are
excluded for that control only; the selected function runs every native row.
Four intentional frame locals receive a native-only unused-variable warning
suppression. Static assertions check the setup size/member offsets and actual
SDK camera/actor offsets. Native objects are separate and legally typed; the
guest alias experiment is not a portable C alias claim.

Sine and cosine providers are pure finite deterministic bit contracts. These
tests check arguments, return use, operation order and float32 rounding; they
do not establish libm approximation accuracy, FCSR or hardware acceptance.

A fresh original-ROM/loaded-ELF census finds one JAL at `0x15122E7C` inside
`func_15122C5C` and no aligned loaded-pointer literals. Its original four-word
window passes **384 cases per stream**, covering the S0-to-A0 delay argument,
target return and following call to `func_15128CB0`. Missing argument and skipped
target-call controls fail. The result is unused before the next JAL. The full
caller and following provider are outside this window's claim; computed
references are not excluded by the census.

Six GNU links cover original bases and code+0x10010 / data+0x18020, including
HI16/LO16 carry. The raw target is isolated with exact payload/binding equality;
unused raw-owner data is outside that link scope. The full padded owner is
covered by the actual Make and strict whole-image gates.

The strict predictor covers **6,051 slots**, **494 changed bytes**, **zero
exclusions** and no unexplained differences. Changes are the target body,
symbol size 16 to 468, and three closed symbol/string permutations involving
ten records and 120 name-string bytes. Every named definition is preserved
apart from the target size; section geometry is unchanged. The predictor
reorders only the declared old records/names, without copying actual metadata
or excluding sections. All **189,088 protected Game-data bytes / 720 owners**
remain exact. Production ELF SHA256: `4a4280e840ebf10a6898a1554950c2852baf70b6c3916013b70fe209cd4163ec`.

Five focused checks pass before and after adoption in the primary and isolated
sibling configurations; shared `make tools-check` passes. The package comprises
seven tools files committed before source adoption. The private hybrid uses
1166 files, while the real dirty sibling HEAD/status and
351 dependency hashes are preserved. The complete
production audit checks 2292 frozen baseline inputs.
Earlier unchanged broad suites are reused by fingerprint, not claimed fresh.

Graph updates retain old IDs and qualification metadata. A smaller-corpus
native refusal plus scoped serial extraction is not a full-corpus re-extraction.
The available host scene input/configuration is inspected read-only; no host
source import or runtime parity is inferred. No Make/profile/guard/shared-header,
host/Release/ROM/save changes, no push and zero Claude calls. The 85% goal stays
active. Next candidate: `func_151277B0`, still a placeholder; its retail slot
has 124 words and a 48-byte frame. Its ABI/body/callers need fresh qualification.

```sh
python3 -m unittest tools.tests.test_game_camera_orbit_15125a6c_match -v
make -C conker -j4 build/conker.us.elf progress.csv
make tools-check
```
