# 2024 - Owner enable gate matched as guarded C

Verified 2026-11-02. Production is **4,094/5,511 (74.29%)**; Game is
**3,421/4,838 (70.71%)**, Init 492/492 and Debugger 181/181. Address drift is
zero and 1,417 functions remain different. The active 80% target is
**4,409/5,511**, requiring **315 more**. This is progress toward that goal,
not completion.

## Recovery and interface

`func_1514E920` replaces its zero-return placeholder in
`conker/src/game/generated_179F30.c`. It is the owner enable gate at
`0x1514E920`, ROM `0x17BDD0..0x17BE8C`, owned by `generated_179F30`. Its
recovered interface is:

```c
s32 func_1514E920(u8 *owner, s32 mode, s32 context);
```

Mode zero toggles bit zero of the owner word at `+0x10`. Mode one enables the
bit and mode two disables it. Both disable paths follow the attached pointer
at owner `+0x154` and, when non-null, clear its byte at `+0x30`. Other modes
delegate all three callback arguments to `func_1514E89C`; the handled modes
return one.

The adjacent `func_1514E9DC` wrapper is now typed as a complete three-argument
context forwarder. Its linked instructions are unchanged. The only direct
retail call to the gate is inside that wrapper at ROM `0x17BE94`. The callback
registry at ROM `0x22F624` retains the original five-entry family:
`func_1514E89C`, `func_1514E920`, `func_1514E9DC`, `func_1514E9FC` and
`func_1514EA1C`.

## Guarded compiler and image closure

Retail-profile IDO naturally emits a **44-word/frame24** semantic body. Retail
uses **47 words**. Nineteen checked rows close the compiler's control-flow,
register-allocation and scheduling cycles, and three of those rows insert the
independent retail scheduling words. The sole relocation remains bound to
`func_1514E89C`; symbolic padding moves it from the natural `+0x8C` location
to retail `+0x98` without hard-coding its linked address.

The guarded result matches all 47 retail words. All 77 other functions in
`generated_179F30`, normalized owner pools, all 6,051 function addresses and
the complete allocated image outside this function remain fixed. Strict
full-image prediction uses zero exclusions.

| Artifact | SHA-256 |
| --- | --- |
| Natural 44-word object payload | `e246d24a1783d7cabf1d658de33a8d1dabfd8294f7b82a88174f9a10576c50fc` |
| Retail linked 47-word payload | `e48659cef02f008661fb30cf57f7c67ac90547a1f449edf680974ec261d0df58` |
| Qualified/production owner | `d792860ff5caca206f39b033282de246274e5b98319630b228c4153b6bb0350f` |
| Predecessor linked ELF | `9b28d118b6f5e312f002dca0c717f2f6672772e676c85f934be7e97ce6fc9103` |
| Qualified/production linked ELF | `4f1a7767805854fe649a52f78c8b6ae4788586cb2f48ed4ec2410ff85651f2af` |
| Production map | `1cbc78ec7ba3bfd4cd8bef4b83bfdf51fc96dd1d5cf45ab59794d62d86946da1` |
| Production guard table | `c793bd74de121a50fc004e3413e589b35eb6dcf10075cad8421a8589599d722d` |

The natural object hash masks relocation immediates, while the retail body
hash is taken from the linked ROM, so those hashes are intentionally not
equal.

## Semantic and production qualification

The raw big-endian guest oracle executes **600 cases** across all modes,
enabled and disabled owners, null and non-null attachments, context values,
delegate returns and helper register clobbers. The recovered behavior and all
external memory bytes agree with an independent model. One duplicate attached
pointer load at retail `0x1514E984` is statically unreachable because the
preceding branch always bypasses it; every other retail body word is reached.

Native 32-bit O0/O2/O3 profiles and seven effective semantic mutations pass.
The permanent four-test suite additionally verifies all 19 stale-guard
mutations, the complete callback registry and wrapper, all 77 owner neighbors,
literal full-image prediction, protected data and installed
source/object/image coherence. Together with the 19 shared progress, PC16,
padder and protected-layout tests, all **23 tests pass in 35.941 seconds**.

The protected Game-data audit remains exact at 189,088 bytes across 720
owners, zero different bytes, SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.
The actual `make all -j4` rebuilt the complete guard-table dependency set,
linked `conker.us.elf` and produced `conker.us.bin`; it stopped only at the
expected whole-ROM SHA mismatch because the overall decomp is incomplete. A
fresh independent recount credits exactly this function.

The candidate screen, qualification module and tests were committed first in
the tools submodule as `a193518`. Retained stage:
`conker/build/game-owner-enable-gate-1514E920-guard-match/`.

This is instruction-level and bounded semantic proof, not natural whole-game
or gameplay acceptance. The README changes only its aggregate byte-exact
rows. No Claude call was needed.

## Graph retention

The required Graphify update extracted 24,227 nodes versus the retained 58,384
and failed closed without `--force`, preserving 31,816 nodes from 3,754
still-existing files outside the reduced scan corpus. The retained graph
SHA-256 remains
`2b00b0aa755a17017c25c30147af6ba7974722f5c50675421fc41f4bc545b0c8`.
This is old-node retention evidence, not a full-corpus refresh claim.

## Continuation

Continue from a fresh ordinary Game ranking after this banked match. Keep
`func_150A76F0`, `func_151F8870`, `func_150A613C`, `func_150AE280`,
`func_15115F68` and `func_151AE2BC` outside an ordinary direct-C screen until
their existing boundaries are resolved. Every candidate still requires
source, ABI/caller, owner, guest/native, actual Make, complete-image,
protected-data, production recount and documentation gates before credit.
