# 1841: Owner default-lifetime factory match

Date: 2026-10-29. `func_150B53D0`, owner `generated_E2880`.
VA0x150B53D0..0x150B54A8; ROM0xE2880..0xE2958,216bytes /54words.

The zero-return placeholder becomes a four-argument pointer-returning function.
Null owners return NULL. Otherwise it captures the owner pointer and unsigned
byte+0x3B in a16-byte payload with two zero floats. Signed16 lifetime -1 selects
300 and factory flag0; other lifetimes retain their signed value and flag1.
The factory receives -1/type0x24/-1/flag/0x23/16/unsigned priority/mode. On
success it copies the payload to created+0x28, calls func_151D2AB0(6), then
returns the retained created pointer. Failure neither copies nor enables.

All54 retail words and three relocations emit directly from semantic C using
the existing O2/g3 profile. Recovering the explicit ternary `lifetime == -1 ?
0 : 1` closes the match: equivalent `lifetime != -1` yields a different IDO
sequence. No register hint or cast is needed. The80-byte frame saves RA+44,
uses incoming homes+84/+88/+92, payload+60 and retained result+76. No guards,
insertions, omissions, profile/frame adjustment or shared-header edits.

Qualification passes eight fresh methods independently in each tools copy,
plus shared tools checks. Installed checks rerun two methods per copy; six
semantic checks are reused only by complete input/module/artifact identity.

- Guest3,840 cases /11,520 original/raw/padded executions cover every word
  and agree in literal registers/FP/RAM/calls/events/access traces/HI/LO.
  Cases include null owners, signed16 narrowing from high input words, -1,
  signed limits, unsigned priority, modes, allocation failure, an output whose
  payload aliases owner storage, helper mutations and both stack phases.
- Native32 O0/O2/O3 each pass1,920 cases with UBSan and reject eight controls:
  wrong default, reversed flag, wrong size, omitted copy/enable, lost result,
  offset result and owner identity captured after the factory mutation.
-81 memory-access prefixes agree in full literal state. Three independent
  layouts pass216 cases. Original7-word caller window in func_1509D180,
  VA1509D518 /ROMCA9C8, passes72 cases. It loads a signed halfword lifetime,
  fixes priority255/mode1 and replaces v0 from its own stack after return.
  Earlier parent gates and provider output are preconditions; full parent
  execution is not claimed.
- Complete owner and pools preserve five neighbors. Three actual Make
  commands reproduce the padded object without C diagnostics. The inherited
  duplicate-recipe Make warning remains.
- Strict independent whole-image prediction equals production:160 bytes,
  159 target code plus one target extent; zero metadata changes/exclusions.
  All6,055 other linked bodies and all addresses remain fixed. Protected Game
  data stays exact across189,088bytes /720owners. Guard/inventory CSV unchanged.

Factory, memcpy and enable helpers are bounded models, with interfaces checked
against retained sources. This does not execute their complete allocator,
copy-loop or enable-system implementations. Packet bytes5..7 remain padding
as in retail: literal guest copies agree across all16bytes, while native checks
compare known fields without inventing portable values for uninitialized
padding. No complete provider/parent/gameplay/hardware acceptance is claimed.

Actual adopted-ELF count:3,918/5,506 (71.16%), Game3,245/4,833 (67.14%),
Init492/492 and Debugger181/181, zero drift.212 more to4,130. Tools commit
first: `35917518bdf922a17c08957e44b02a15c2b3196f`. Root README aggregate rows only. No push.

Scoped AST refresh retains or uniquely relocates all49,640 old nodes and
retains102,937 directed relationships. One obsolete s32 return reference
retires against the recovered pointer interface. Helper call edges and caller
metadata are source/binding checked. Outside manifest rows/analytics historical;
no full-corpus extraction. The75% goal remains active.

Artifacts:conker/build/game-owner-default-lifetime-match/. Next screened
target `func_1510F648` still needs complete qualification. Parked candidates uncredited.
Older mirror preserves1,961 inherited dirty paths plus three new modules.
No host-port/frozen Release/save/editor/private-input/memory changes. Zero Claude.
