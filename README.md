<p align="center">
  <img src="https://raw.githubusercontent.com/thisnull7/grabdom/refs/heads/main/grab.png" alt="GRABDOM Preview" width="100%">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Version-2.0-red?style=for-the-badge&logo=github">
  <img src="https://img.shields.io/badge/Python-3.7+-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20Termux-green?style=for-the-badge&logo=linux">
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge">
</p>

<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=600&size=28&duration=3000&pause=1000&color=FF0000&center=true&vCenter=true&width=600&lines=%E2%98%A0+GRABDOM+v2.0+%E2%98%A0;Domain+Ripper+%26+Archive+Extractor;hax.or.id+Deface+Scraper;THE+WINNER+TAKES+ALL+%3A(">
</p>

---

## ☠ ABOUT GRABDOM

**GRABDOM** is a powerful domain scraping tool designed to extract defaced domain lists from the **hax.or.id** archive. Built with precision and a dark aesthetic, this tool silently rips through attacker archives, collecting every defaced domain across all pages automatically.

> *"Every domain has a story. I just collect them."*  
> — **null7**

### ⚡ Key Features

- 🔴 **Auto Pagination** — Scrapes ALL archive pages, not just the first
- 🔴 **Real-Time Saving** — Domains written to file instantly per page, no waiting
- 🔴 **Single Master List** — All attackers saved to one `all_domains.txt` file
- 🔴 **Duplicate Prevention** — Never saves the same domain twice
- 🔴 **Clean Output** — Strips paths, mirrors, and parameters — pure domains only
- 🔴 **Scary Aesthetic** — Red/black terminal UI with skull banner
- 🔴 **Lightweight** — Minimal dependencies, runs anywhere

---

## 📸 PREVIEW

<p align="center">
  <img src="https://raw.githubusercontent.com/thisnull7/grabdom/refs/heads/main/grab.png" alt="GRABDOM Screenshot" width="90%">
</p>

---

## 🎯 WHAT IT DOES

| Feature | Description |
|---------|-------------|
| **Target** | `https://hax.or.id/archive/attacker/[NAME]` |
| **Output** | `all_domains.txt` — clean domains, one per line |
| **Format** | `http://domain.com` or `https://domain.com` |
| **Scope** | ALL pages for that attacker |
| **Persistence** | Appends to master list, never overwrites |

### Example Output (`all_domains.txt`)
http://evandriaprimajasindo.co.id

http://ilmiteknik.co.id

http://panduwarta.com

https://e-umkmkediri.com

http://targetsite-get-deface.com


---

## 🛠 INSTALLATION

### Prerequisites
- **Python 3.7+** installed on your system
- **pip** (Python package manager)
- **git** (optional, for cloning)

### Step 1 — Clone the Repository
```bash
git clone https://github.com/thisnull7/grabdom.git
cd grabdom
pip install -r requirements.txt
pip install requests beautifulsoup4 colorama
python grab.py

