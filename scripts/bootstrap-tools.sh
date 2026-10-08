#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."
git_command=(git)
# Windows Git retains the checkout's CRLF rules when this runs through WSL.
if [[ $PWD == /mnt/[a-zA-Z]/* ]] && command -v git.exe >/dev/null && command -v wslpath >/dev/null; then
    git_command=(git.exe)
fi
local_path() {
    local path=${1%$'\r'}
    if [[ $path == [a-zA-Z]:/* ]] && command -v wslpath >/dev/null; then
        wslpath -u "$path"
    else
        printf '%s\n' "$path"
    fi
}
root=$(local_path "$("${git_command[@]}" rev-parse --show-toplevel)")
cd "$root"
if [[ $("${git_command[@]}" config --file .gitmodules --get submodule.tools.path) != tools ]]; then
    echo 'bootstrap-tools: expected the pinned tools submodule in .gitmodules' >&2
    exit 1
fi
if [[ -L tools || ( -e tools && ! -d tools ) ]]; then
    echo 'bootstrap-tools: tools must be a normal directory, not a file or symlink' >&2
    exit 1
fi
read -r mode type revision path < <("${git_command[@]}" ls-tree HEAD -- tools)
if [[ $mode != 160000 || $type != commit || $path != tools ]]; then
    echo 'bootstrap-tools: commit the consumer submodule pin before bootstrapping' >&2
    exit 1
fi
url=$("${git_command[@]}" config --file .gitmodules --get submodule.tools.url)
if [[ ! -e tools/.git ]]; then
    # Legacy nested module directories and caches stay in place; no files are removed.
    mkdir -p tools
    "${git_command[@]}" init tools
    "${git_command[@]}" -C tools remote add origin "$url"
    "${git_command[@]}" -C tools fetch origin "$revision"
    # A normal checkout refuses conflicting local files; never force it.
    "${git_command[@]}" -C tools checkout --detach "$revision"
fi
if [[ $(local_path "$("${git_command[@]}" -C tools rev-parse --show-toplevel)") != "$root/tools" ]]; then
    echo 'bootstrap-tools: tools has unexpected Git metadata; inspect it before continuing' >&2
    exit 1
fi
if [[ -n $("${git_command[@]}" -C tools status --porcelain --ignore-submodules=none) ]]; then
    echo 'bootstrap-tools: preserve local tools/dependency changes before updating the pin' >&2
    exit 1
fi
"${git_command[@]}" submodule init tools
"${git_command[@]}" submodule sync --recursive
"${git_command[@]}" submodule update --init --recursive
"${git_command[@]}" submodule status --recursive
