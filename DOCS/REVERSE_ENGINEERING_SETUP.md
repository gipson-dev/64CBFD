# Reverse Engineering Setup

Verified locally after the session restart: 2026-10-13. These are observations
of this workstation, not prerequisites promised for every contributor.

## Connected Codex Server

The restarted Codex session exposes the `rea` MCP server and 170 REA tools.
Its live `binary_session` response reports:

| Component | Observed Value |
| --- | --- |
| REA package and server | `rea-agents` 6.4.0 |
| Installed skill | `reverse-engineer-anything`, version 37, 170 tools |
| Codex MCP client | 0.162.0-alpha.17.2 |
| Windows Node | 22.23.1 |
| Ghidra provider | Available, installation version 12.1 |
| Java | Microsoft 64-bit JDK 21.0.11 |

The registration in `C:/Users/grego/.codex/config.toml` launches the existing
Node executable and installed public REA launcher. Its scoped environment is:

```toml
[mcp_servers.rea]
command = 'C:\Users\grego\AppData\Local\hermes\node\node.exe'
args = ['C:\Users\grego\AppData\Local\hermes\node\node_modules\rea-agents\scripts\rea.mjs', 'mcp']
startup_timeout_sec = 30

[mcp_servers.rea.env]
GHIDRA_INSTALL_DIR = 'C:/Tools/ghidra_12.1_PUBLIC'
JAVA_HOME = 'C:\Program Files\Microsoft\jdk-21.0.11.10-hotspot'
```

The live provider checks pass configuration, platform, architecture,
installation, version, headless launcher, native decompiler and Java checks.
No registration edits or dependency installations were needed after restart.
This verifies connection and provider readiness, not successful target analysis.

## Important MIPS Limitation

A real `open_binary` probe selected Ghidra for the existing uninstalled
matrix-reflection candidate:
`conker/build/game-matrix-reflection-dispatch-homes-test/selected.elf`.
REA identified the input as MIPS ELF, then rejected it with:

```text
capability_unavailable / unsupported_provider
Ghidra rejection: target_format_unsupported
Windows Ghidra P0 accepts PE targets only.
```

No analysis session was opened and no MIPS decompilation was produced. This is
a restriction of this REA adapter/version/host combination, not evidence that
Ghidra itself lacks MIPS support. Changing `GHIDRA_INSTALL_DIR` or `JAVA_HOME`
again will not remove that target-format restriction.

The only installed WSL distribution is `PSBBN`; `command -v node` and
`command -v java` find no Linux executables there. Its `rea` command resolves
to the Windows installation mounted under `/mnt/c`, not a verified Linux REA
stack. Do not claim a working Linux MIPS provider from that launcher alone.
No Linux dependencies, other providers or unrelated client registrations were
installed or changed during this verification.

Use the existing IDO/MIPS assembly, compiler, linker and oracle workflow for
the current decomp task. A separate Linux REA/Ghidra setup would require its
own authorized dependency work and a successful MIPS target probe before use.
REA's IDA adapter is unconfigured here; its reported MIPS lane is unverified.
Hopper's adapter reports an unsupported Windows host and MIPS architecture.

## Scoped CLI Check

The MCP server environment does not automatically become the terminal's
environment. A plain `rea doctor --client codex --json` reports an aligned
Codex registration while its independent shell provider inspection can say
`GHIDRA_INSTALL_DIR is not set`. That is not a failure of the connected server.

This process-local PowerShell check passes the requested Codex, Ghidra and
installed-skill scope without modifying global environment variables:

```powershell
$env:GHIDRA_INSTALL_DIR = 'C:/Tools/ghidra_12.1_PUBLIC'
$env:JAVA_HOME = 'C:/Program Files/Microsoft/jdk-21.0.11.10-hotspot'
rea doctor --client codex --provider ghidra --skill --json
```

The fresh result is `healthy: true`, with every requested scope check passing.
Unrequested client/provider diagnostics are not a reason to rewrite all other
registrations. Read the installed skill's connection-and-recovery guide only
for an observed blocker, and do not repeat setup before ordinary source work.

## Resume Point

Continue [the decomp workflow](AGENT_WORKFLOW.md) and
[current handoff](CURRENT_STATUS.md). REA connection readiness neither grants
matching credit nor qualifies gameplay or host-port behavior. Preserve the
frozen host Release checkpoint, real saves and unrelated checkout changes.
