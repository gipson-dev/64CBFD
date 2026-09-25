"""Render/rank a raw asset_dump.py file as candidate big-endian RGBA5551 images.

For a given file, tries every (w, h) factor pair of its pixel count in a
plausible range, decodes each as big-endian RGBA5551, and ranks candidates
by average local pixel-to-neighbor difference ("gradient"): a genuine
raster image has spatial coherence (low gradient in most regions), while
reinterpreting the same bytes at the WRONG width scrambles unrelated
rows/columns together, usually producing much higher gradient. Renders
only the top-N lowest-gradient candidates so a human can pick the real one
by eye - **always eyeball the result**, the score is a stopgap heuristic
and has been observed to fail outright for some files (see
DOCS/ASSET_FORMATS.md section 5, the 17,600-byte assets00 size class).

Usage:
    python tools/render_rgba5551.py assets00/0039.bin outdir/
    python tools/render_rgba5551.py assets00/ outdir/ --top 3
"""
import glob
import os
import struct
import sys

from PIL import Image


def decode_pixels(data, w, h):
    n = w * h
    if len(data) < n * 2:
        return None
    pixels = []
    for i in range(n):
        val = struct.unpack_from(">H", data, i * 2)[0]
        r = (val >> 11) & 0x1F
        g = (val >> 6) & 0x1F
        b = (val >> 1) & 0x1F
        a = val & 1
        pixels.append((r, g, b, a))
    return pixels


def gradient_score(pixels, w, h):
    total = 0
    count = 0
    for y in range(h):
        row = y * w
        for x in range(w - 1):
            r1, g1, b1, _ = pixels[row + x]
            r2, g2, b2, _ = pixels[row + x + 1]
            total += abs(r1 - r2) + abs(g1 - g2) + abs(b1 - b2)
            count += 1
    for y in range(h - 1):
        for x in range(w):
            r1, g1, b1, _ = pixels[y * w + x]
            r2, g2, b2, _ = pixels[(y + 1) * w + x]
            total += abs(r1 - r2) + abs(g1 - g2) + abs(b1 - b2)
            count += 1
    return total / max(count, 1)


def save_png(pixels, w, h, path):
    img = Image.new("RGBA", (w, h))
    px = img.load()
    for i, (r, g, b, a) in enumerate(pixels):
        r8 = (r << 3) | (r >> 2)
        g8 = (g << 3) | (g >> 2)
        b8 = (b << 3) | (b >> 2)
        px[i % w, i // w] = (r8, g8, b8, 255 if a else 0)
    img.save(path)


def factor_pairs(n_pixels, min_dim=4, max_dim=256):
    pairs = []
    for w in range(min_dim, max_dim + 1):
        if n_pixels % w == 0:
            h = n_pixels // w
            if min_dim <= h <= max_dim:
                pairs.append((w, h))
    return pairs


def process_file(path, top_n, outdir):
    with open(path, "rb") as f:
        data = f.read()
    n_pixels = len(data) // 2
    pairs = factor_pairs(n_pixels)
    base = os.path.splitext(os.path.basename(path))[0]
    if not pairs:
        print(f"{base}: {len(data)}B, {n_pixels}px, NO VALID FACTOR PAIR "
              f"(not a plain w*h RGBA5551 image - check header/CI4/CI8 hypotheses)")
        return
    scored = []
    for (w, h) in pairs:
        pixels = decode_pixels(data, w, h)
        if pixels is None:
            continue
        scored.append((gradient_score(pixels, w, h), w, h, pixels))
    scored.sort(key=lambda t: t[0])
    best = scored[:top_n]
    summary = ", ".join(f"{w}x{h}(grad={s:.1f})" for (s, w, h, _) in best)
    print(f"{base}: {len(data)}B, {n_pixels}px, {len(pairs)} candidates, best: {summary}")
    if outdir:
        os.makedirs(outdir, exist_ok=True)
        for (s, w, h, pixels) in best:
            save_png(pixels, w, h, os.path.join(outdir, f"{base}_{w}x{h}_grad{s:.0f}.png"))


if __name__ == "__main__":
    target = sys.argv[1]
    outdir = sys.argv[2] if len(sys.argv) > 2 and not sys.argv[2].startswith("--") else None
    top_n = 3
    if "--top" in sys.argv:
        top_n = int(sys.argv[sys.argv.index("--top") + 1])

    files = sorted(glob.glob(os.path.join(target, "*.bin"))) if os.path.isdir(target) else [target]
    for f in files:
        process_file(f, top_n, outdir)
