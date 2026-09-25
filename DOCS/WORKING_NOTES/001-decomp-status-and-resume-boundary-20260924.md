# Working Note 001: Decomp Status and Resume Boundary

Date: 2026-09-24

## Purpose

Re-establish the actual `64CBFD` decompilation state after extended work in
the sibling host port, then leave an evidence-backed place to resume.

## Measured facts

- `master` and `origin/master` both point to `2ed3523` (`tool updates`).
- Before this documentation update, the working tree had 123 changed tracked
  paths and 37 untracked paths. The existing work was left in place.
- `progress.csv` contains 6,038 function rows: 5,497 C and 541 assembly.
- Byte totals are 1,933,296 C and 323,432 assembly, or 85.67% C by bytes.
- The linked scan reports 2,517 exact C functions, one address-drift blocker,
  and 2,979 functions with real instruction differences.
- `func_10012588` is still the sole address-drift blocker.
- `make -C conker replace NON_MATCHING=1 -j4`, `make tools-check`, and the
  outer `make NON_MATCHING=1 -j4` all pass in the present checkout.
- `git diff --check` reports one pre-existing whitespace issue at
  `conker/src/game_161520.c:507` plus line-ending warnings. It was not changed
  during this status pass.

## Interpretation

The July snapshot was 5,978 C functions and 2,522 exact functions. The current
tree has 481 fewer C functions and five fewer exact functions. The new 45.79%
matching percentage therefore reflects a smaller C denominator, not a net
matching improvement. The restored assembly may still be the correct choice
for runnable port behavior, but decomp progress must count it as assembly.

No fresh gameplay run was performed for this audit. Build success is the
current behavioral confidence limit.

## Banked checkpoint

The restoration baseline was reviewed and split into coherent commits:

- `dae2a51` - generated-slice assembly padding and PC16 relocation support
- `8488db5` - restored guest assembly, C callers, and ABI declarations
- `5135f95` - OGL hand-port reference extraction
- `9de06b8` - RGBA5551 asset inspection tooling
- documentation and current-status handoff in the following checkpoint commit

The empty `DOCS/user notes.md` file is personal workspace material. It remains
on disk and is excluded locally through `.git/info/exclude`; it is not part of
the repository baseline.

## First matching steps

### Step 1: paired one-difference routines

Compare these together:

- `func_151906E0` in `conker/src/game/generated_1BA1D0.c`
- `func_151C1814` in `conker/src/game/generated_1ED0F0.c`

Both are 19-word event handlers. They test event `0x2D` and exchange one of
two values into an object field. Their layouts differ, but their C control
flow is effectively the same. Each currently has one real instruction
difference, so use the pair to isolate field typing, temporary lifetime, or
operand-order effects. Keep a variant only if the linked scan improves and
does not regress its counterpart.

### Step 2: finish the debugger near-match

If the paired game functions do not move cleanly, resume `func_16001390` from
[TEMP_DEBUGGER_TODO.md](../TEMP_DEBUGGER_TODO.md). It has two scheduling
differences after the 88-word body, 32-byte frame, saved-`s0` lifetime,
four-pixel unroll, and branch-delay pointer update were matched.

### Step 3: choose conversion work deliberately

The smallest current assembly rows include:

| Function | Owner | Bytes |
| --- | --- | ---: |
| `func_150AC9B0` | `generated_D86A0` | 16 |
| `func_151D8BE0` | `generated_205C90` | 32 |
| `func_15116984` | `generated_142560` | 48 |
| `func_150A81A0` | `D5650` | 48 |
| `func_15165B80` | `generated_191C30` | 48 |
| `func_150AA644` | `D7980` | 52 |

These are candidates for inspection, not promised easy conversions. First
confirm that each row is executable game code rather than padding, a mixed
slice, or intentionally restored original assembly. Keep init routines such
as `sqrtf`, CP0 accessors, and handwritten SDK code out of the first batch.

## Resume commands

```sh
make -C conker progress NON_MATCHING=1
make -C conker match-progress NON_MATCHING=1 LIST=1
make -C conker replace NON_MATCHING=1 -j4
make NON_MATCHING=1 -j4
make tools-check
git diff --check
```

Do not update headline metrics from an object-only comparison. Use the linked
`conker/build/conker.us.elf` scan against the pristine retail image.
