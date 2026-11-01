# Relative-direction CFE stack home recovered; 34 words still differ

The private `func_1506B3B8` candidate now uses retail's exact **SP+0x19**
choice byte. Its **77 words / 32-byte frame** retain **34 real differences**,
improving the 36-word boundary in [Note 1949](1949-relative-direction-private-semantics-and-codegen-boundary-20261101.md).
It remains uninstalled and receives no exact C credit. The later carried-actor
initializer checkpoint owns any production progress reported alongside this note.

## Compiler evidence and the source change

The existing fingerprint-locked CFE/UOPT/UGEN helper captured both wire streams
from newly owned compiler children. CFE, UOPT, UGEN and the compiler driver all
exited zero. The descriptor probe fired during UGEN's lifetime and was removed;
normal and instrumented text, function definitions, relocations and pools agree.
Compiler fingerprints retain the already qualified values; no compiler was
changed, replaced or patched.

The original declaration order places `choice` at CFE memory home **M-1**.
UOPT's one-byte rstr/rlod preserve that home across the angle-helper call,
producing SP+0x1F in a 32-byte frame. Moving only the existing declarations to
this order places it at **M-7**, producing retail's SP+0x19:

```c
s16 difference;
u8 magnitude;
u16 angle;
u8 choice = 0;
s32 signedHigh;
s32 highByte;
struct127 *actor;
```

The alignment calculation predicted the location before compiling. All 24
orders with this six-byte prefix produced the expected store/reload slot and
34 differences. A second complete wire capture independently confirms the
one-byte **rstr and rlod at M-7**. There are no extra variables, padding,
volatile accesses, register bindings or guarded words in this private change.
The two corrected retail words are the local byte store and reload.

Explicit 32-bit address arithmetic and compatible block-scoped extern views
did not improve the remaining table-address expression. They were not adopted.
The selected candidate retains ordinary typed pointer access.

## Behavioral evidence and remaining boundary

The 34-word candidate freshly passes **6,148 guest cases / 12,296 executions**
at retail and two rebases, with identical public memory, helper arguments and
public access traces. All **76 reachable words** execute; unreachable +0xFC
is retained. The helper provider includes upper return-bit poison, post-call
actor retargeting and field/table mutation. Float edge observations remain
model evidence, not hardware/FCSR acceptance.

The C operators, stores, calls and their order are unchanged from Note 1949;
only the non-effectful declaration order changed. That note's native
O0/O2/O3 4,096-case and seven-control evidence is reused explicitly, not called
a fresh native run for this declaration order. Full machine identity is still
unproven because the table-address and register allocation differ.

Raw payload SHA-256:
`1db2220b4471fe4d980cc6783866d3abda9a2371b1c09123f6f7d270e16acee2`.
Retail slot SHA-256 remains
`ae0be3144abf6933f86fafb0b14f6c505139cd51bf2e07c9efb21770e6546502`.

Remaining work is the early table HI16 versus shared complete-address
expression and its register/schedule consequences. Preserve this recovered
home and signedHigh-to-byte conversion. Continue from the actual optimizer
records rather than repeating the prior broad declaration/type/register screens.
The downstream callback invocation, owner/padder/Make/full-image/production and
recount gates still must pass before this function can be adopted.

## Retained artifacts

Stage: `conker/build/game-relative-direction-1506B3B8-match/`.
`frontend-v31/` holds the original-home capture; `frontend-v37/` holds the
recovered-home capture. Both include raw CFE/UOPT streams, captured descriptor
and type tables, decoded records, debugger log and validation receipts.
`home-order-screen-v32.json`, `home-semantic-input-v36.c`,
`private-semantic-v36.o`, `private-semantics-v36.json`, and the successful
v31/v32/v33/v35/v36/v37 driver receipts preserve the next starting point.

The 1,011 original frozen inputs are all retained as verified `before-*`
files in the carried-actor initializer stage. Exact paths and hashes are in
`historical-input-locations-v38.json`; those copies preserve reproducibility
when the current owner/guard/inventory changes for the separate initializer
adoption. Rebase a new qualification snapshot onto the latest production
checkpoint before resuming installation work on this candidate.
