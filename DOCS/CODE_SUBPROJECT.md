# Code Sub-project

The `conker/` directory is the code sub-project. It pulls together the ROM's main code sections so they can be compiled in a standard way across versions.

For the full build from the repository root, see [Project overview](PROJECT.md).

## Code sections

The ROM has three code sections:

- `init`: initialization code plus libultra, loaded at `0x10000000`.
- `game`: core game code, loaded at `0x15000000`.
- `debugger`: debugger code, loaded at `0x16000000`.

In the `us`, `eu`, and `debug` ROMs, the `game` section is compressed. In the earlier `ects` ROM, it is not.

## Build loop

Run these commands from inside the `conker/` directory:

```sh
make extract
make --jobs
make replace NON_MATCHING=1
make -C ..
```

What each step does:

1. `make extract` unpacks the code sub-project's generated assembly and headers.
2. `make --jobs` compiles the code sub-project.
3. `make replace` writes the newly compiled code sections back into the split ROM output.
4. `make -C ..` returns to the repository root build and rebuilds the full ROM.

`NON_MATCHING=1` skips the code sub-project's own byte-exact sha1 check
before `replace` runs. Without it, `make replace` fails outright (rather
than proceeding) as soon as any section doesn't match, which - with most of
`game` still unmatched - is the normal state right now. `make -C .. ` still
reports `build/conker.us.z64: FAILED` in that case; that failure is expected
per [Project overview](PROJECT.md) and isn't specific to this step. The same
flag works with `make progress` (see below) for the same reason.

## Common contributor loop

When working on a function, the usual rhythm is:

1. Edit the C source in `conker/src/`.
2. Build with `make --jobs`.
3. Replace the section with `make replace`.
4. Rebuild the full ROM with `make -C ..`.
5. Compare mismatches with `tools/asm-differ`.

This loop is expected to produce mismatches until the edited function matches the original assembly exactly.
