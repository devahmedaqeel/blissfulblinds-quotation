# Blissful Blinds Quotation Generator

Customer data bhar kar Blissful Blinds Ltd ki quotation ko PDF mein download karne ki website.

## Kaise chalayein
- `index.html` ko kisi bhi browser mein double-click karke kholein, ya
- `index.html` ko apni website/hosting (cPanel, Netlify, GitHub Pages, etc.) par upload karein.

PDF banane ke liye internet zaroori hai (html2canvas aur jsPDF libraries CDN se load hoti hain).

## Folder structure
- `index.html` — ready-to-use website (sab images andar embedded hain, akeli yehi file kaafi hai)
- `src/template.html` — source code (images ki jagah `{{HEADER}}` jaise placeholders)
- `assets/` — logo header, corner design aur icons (original template se)
- `build.py` — `src/template.html` mein badlav ke baad `python build.py` chala kar `index.html` dobara banayein

## Features
- Live preview, exact original template layout
- Deposit (50%) aur remaining balance ka automatic hisaab
- Payment status, T&C tick, signature, notes
- Site always opens with an empty template (no previous client data); a page refresh keeps what you typed in that tab
- "New" clears the form in one click
- PDF download at the exact template size (1149 × 1303 px page, no extra margins or blank space)
- Save Image: PNG at the original template size (1149 × 1303 px)
- File name: "<Customer Name> Quotation.pdf / .png" by default, or type your own in the "File name" box
- Mobile par Form / Preview tabs, bade touch buttons
- iPhone/iPad: image opens the share sheet ("Save Image" saves it to Photos); PDF saves to Files › Downloads in Safari (share sheet "Save to Files" in other iOS browsers)
- Android: PDF and image save to Downloads (images also show in the Gallery)
- The iPhone share sheet only works over https (e.g. GitHub Pages), not over a local http:// address
