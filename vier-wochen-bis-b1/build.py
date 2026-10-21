#!/usr/bin/env python3
"""Assemble index.html from src/template.html + src/data.json.

    python3 build.py

The page is one self-contained file (plus fonts/), so GitHub Pages can serve it
as-is. Edit src/template.html for layout/behaviour and src/data.json for
content (plan, vocabulary, grammar, practice tests), then rebuild.
"""
import json
import pathlib
import sys

root = pathlib.Path(__file__).resolve().parent
tpl = (root / "src" / "template.html").read_text(encoding="utf-8")
data = json.loads((root / "src" / "data.json").read_text(encoding="utf-8"))

# sanity checks so a broken data edit fails here, not in a visitor's browser
assert isinstance(data["grammar"], list), "grammar must be a list of blocks"
assert len(data["exams"]) >= 1, "no practice tests"
for k in ("content", "vocab", "grammar", "exams"):
    assert k in data, f"missing {k}"

marker = "/*__DATA__*/"
if tpl.count(marker) != 1:
    sys.exit(f"template must contain {marker} exactly once")

# '</' inside a <script> would end it early
blob = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
out = tpl.replace(marker, blob)
(root / "index.html").write_text(out, encoding="utf-8")
print(f"index.html written ({len(out.encode('utf-8')) / 1024:.0f} KB)")
