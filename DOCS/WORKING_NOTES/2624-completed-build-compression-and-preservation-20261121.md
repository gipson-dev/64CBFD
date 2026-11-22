# 2624 - Completed build compression and preservation

Date: 2026-11-21. Matching progress was unchanged during this storage operation.

C: fell below 200 MiB free and two atomic graph writes failed during the prior
function's finalization. The valid graph survived and compact JSON writing
allowed that bank to finish. A fresh read-only build inventory then measured
582,365 files across 980 entries, totaling 85,813,799,513 logical bytes.

Transparent NTFS compression was applied to **22 older installed, completed
banks**. Every original path is retained. Nothing was deleted, moved, archived
or substituted. The plan excludes the latest three banks, all current protected
production inputs and uncredited/private candidate banks. Each selected bank
has a successful installed checkpoint and a consumer commit ancestral to HEAD.
The operation changes compression attributes; future reads use the same bytes.

Before/after SHA256 verification covers **58,607 files**, totaling
3,563,257,630 logical bytes. File membership, contents, sizes and modification
times agree exactly. All **2,470 current immutable inputs** were independently
rechecked. Decomp, nested tools and the real dirty sibling retained their Git
states and HEADs. The source/ROM/save inputs and host Release were outside scope.

At the measured checkpoints, volume free space rose from
204,005,376 to 2,160,099,328 bytes: an observed
increase of **1,956,093,952 bytes (about 1.96 GB)**. Volume
free space can subsequently change as compilation and other processes write.

The ignored `conker/build/_cleanup-20261121-build-space/` directory retains
the inventory, reviewed plan, per-bank compact logs, complete before manifest
and `compression-audit.json`. No historical restore step is required because
the file layout and logical bytes are unchanged. Existing dated archive plans
were inspected for policy and were not rerun.

The active matching push resumed with `func_151945CC`; see
[Note 2625](2625-game-source-heading-trail-guarded-byte-match-20261121.md).
