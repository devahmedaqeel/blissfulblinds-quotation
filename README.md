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
- Draft browser mein save rehta hai; "New Quotation" se blank form
- A4 PDF download, file naam: "<Customer Name> Quotation.pdf", ya "PDF File Name" box mein apna naam likhein
- Mobile par Form / Preview tabs, bade touch buttons
