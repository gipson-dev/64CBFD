# IDO 5.3 Recomp Toolchain

The `ido/ido5.3_recomp/` directory contains the recompiled IDO compiler files used for byte-matching builds.

Most contributors do not need to rebuild this directory. Use these notes only if you need to reproduce or refresh the bundled compiler files.

## Reproduce the directory

Run this from a Linux or WSL shell:

```sh
cd
git clone https://github.com/n64decomp/sm64.git
cd sm64/tools/ido5.3_recomp
make all --jobs

# Copy the rebuilt files back into this repository.
cp ./* ../../../conker/ido/ido5.3_recomp/
```

## Notes

- The compiler is required for byte-matching builds.
- Native Windows without WSL or Docker is not supported for this toolchain.
- If the build environment changes, check [Project overview](PROJECT.md) for the current supported setup first.
