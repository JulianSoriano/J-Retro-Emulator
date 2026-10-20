#!/usr/bin/env python3
"""Builds the one-file emulator (index.html) from the readable source.

  src/index.html      the app (page, styles and code)
  src/cores/*.wasm    the four emulation cores (compiled to WebAssembly)
  index.html          the result: the app with every core embedded as text

Run from the repository root:   python3 tools/build_single_file.py
Needs only Python 3."""
import base64, os, sys
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
page = open(os.path.join(root, "src", "index.html"), encoding="utf8").read()

# 1. Make the core loader read the embedded copy first (it falls back to a normal download).
old = """    const r = await fetch(name + '.wasm');
    if (r.ok) core = await makeCore(new Uint8Array(await r.arrayBuffer()));"""
new = """    const emb = document.getElementById('wasm-' + name);
    if (emb) {
      const bin = atob(emb.textContent.trim()); const bytes = new Uint8Array(bin.length);
      for (let i = 0; i < bin.length; i++) bytes[i] = bin.charCodeAt(i);
      core = await makeCore(bytes);
    } else {
      const r = await fetch(name + '.wasm');
      if (r.ok) core = await makeCore(new Uint8Array(await r.arrayBuffer()));
    }"""
if old not in page: sys.exit("Loader code not found in src/index.html; the build script needs updating.")
page = page.replace(old, new)

# 2. Append each core as base64 text just before </body>.
blobs = ""
for name in ("fceumm", "gpgx", "mgba", "snes9x"):
    data = open(os.path.join(root, "src", "cores", name + ".wasm"), "rb").read()
    blobs += '<script type="application/octet-stream" id="wasm-%s">%s</script>\n' % (name, base64.b64encode(data).decode())
page = page.replace("</body>", blobs + "</body>", 1)

out = os.path.join(root, "index.html")
open(out, "w", encoding="utf8").write(page)
print("Wrote %s (%.1f MB)" % (out, os.path.getsize(out) / 1e6))
