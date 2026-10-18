"""Rebuild index.html from src/template.html and the images in assets/.
Run:  python build.py"""
import base64, pathlib
root = pathlib.Path(__file__).parent
h = (root / "src" / "template.html").read_text(encoding="utf-8")
for key, name in [("HEADER","header"),("LOGOMARK","logo-mark"),("LOGO","logo"),("CORNER","corner"),("PHONE","phone"),("MAIL","mail"),("WA","wa"),("WEB","web"),("SHIELD","shield")]:
    data = base64.b64encode((root / "assets" / f"{name}.png").read_bytes()).decode()
    h = h.replace("{{%s}}" % key, "data:image/png;base64," + data)
page = ('<!doctype html><html lang="en"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover,interactive-widget=resizes-content"></head><body>' + h + '</body></html>')
(root / "index.html").write_text(page, encoding="utf-8")
print("index.html rebuilt")
