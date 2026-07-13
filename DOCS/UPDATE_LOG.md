# Update Log

This log tracks repository-facing documentation, workflow, and project maintenance updates.

For code-level progress, run:

```sh
make -C conker progress
```

## 2026-07-13

### GitHub Actions

- Updated checkout steps from `actions/checkout@v4` to `actions/checkout@v7` so workflows use the Node 24-compatible action.
- Changed the ROM build workflow to skip baserom-dependent steps when `PRIVATE_REPO_ACCESS` or `CONKER_BASEROM_US` is missing.
- Added clear workflow notices explaining which secrets are needed to enable the full ROM build.

### Documentation

- Moved repository-owned README content into the `DOCS/` folder.
- Added the `DOCS/README.md` documentation index.
- Rewrote the project overview, code sub-project notes, compressed config notes, and IDO toolchain notes for clearer reading.
- Added this update log.
