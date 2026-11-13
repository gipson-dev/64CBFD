# Game bounded queue append byte match

Date: 2026-11-13. `func_1518ABD0` in `generated_1B7EC0.c` replaces a
zero-return placeholder with the queue insertion and bounded-eviction routine.
Its complete 82-word body at VA `0x1518ABD0..0x1518AD18` / ROM
`0x1B8080..0x1B81C8` matches retail. Two following alignment words remain
unchanged. The C body retains the retail 32-byte frame and saved-entry home;
17 expected-word guards normalize compiler register allocation. Both object
padders reproduce the retail body and relocation bindings.

A null queue or failed record allocation invokes the selector callback when
nonzero and returns zero. Success links a new record at the tail, increments
the wrapping count, copies the queue duration to its timer, and compares the
signed new count with the signed capacity. When the limit is exceeded it
removes the head, performs the original alias-sensitive next-link reload,
invokes the old entry's optional callback, and releases that entry before
returning one. Selectors are truncated to a byte. Retail callers at
`0x150BAF40` and `0x150CB698` use the result to decide whether to release their
input object. The existing adjacent `func_1518AB60` constructs the new record.

Tools commit `6c3c245` supplies the reproducible qualification packet:

```sh
wsl -d PSBBN --exec python3 -m unittest tools.tests.test_game_queue_append_1518abd0_match -v
```

The independent queue model passed 1,536 combinations against retail, raw C,
and both padded streams. A synthetic callback table covered all 256 selector
bytes in 768 null-queue, allocation-failure, and eviction cases. There were
360 allocation-pointer alias cases with zero observed differences; 36 reached
matching modeled stop conditions. Tests covered 384 incoming-home and callback
slot mutations, 137 memory-access cuts, 32 connected cases through both
original caller windows and the original record builder, and twelve GNU links
at three address layouts. Native 32-bit tests passed 1,024 cases at each of
`-O0`, `-O2`, and `-O3`, with UBSan and ten effective negative controls.
Allocation, release and callback providers are bounded models; high selector
indices use synthetic callback entries, not a claim about retail table size.
No hardware or live gameplay acceptance is claimed.

The pre-install suite passed in the mounted tools and with staged sibling
dependencies; the extra selector test also passed in both. The installed suite
passed eight checks in mounted tools, and three affected installed checks ran
fresh with staged sibling dependencies. The production owner and ELF match
the independently audited shadow byte-for-byte, and the other 1,453 linked
objects are unchanged. The strict full-image audit accounts for 247 changed
bytes with zero exclusions; only the target body changes, all 6,050 function
addresses stay fixed, and all 189,088 protected Game-data bytes remain exact.
Three other owner functions, constant pools, and compiler diagnostics remain
unchanged. The existing duplicate `generated_12D630` Make recipe warning remains.

The fresh recount reports Game **3,743 / 4,842 (77.30%)**, total **4,416 /
5,515 (80.07%)**, zero address drift, and **131** more Game matches required
for 80%. Keep the wider Game matching goal open. Routine work used zero Claude
calls.
