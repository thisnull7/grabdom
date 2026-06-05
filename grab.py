import requests
from bs4 import BeautifulSoup
from colorama import init, Fore, Style
import os, sys, time
import re
from urllib.parse import urlparse

init(autoreset=True)

MASTER_FILE = "all_domains.txt"

def show_banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    BANNER = f"""
{Fore.RED}{Style.BRIGHT}
   ██████╗ ██████╗  █████╗ ██████╗ ██████╗  ██████╗ ███╗   ███╗
  ██╔════╝ ██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔═══██╗████╗ ████║
  ██║  ███╗██████╔╝███████║██████╔╝██║  ██║██║   ██║██╔████╔██║
  ██║   ██║██╔══██╗██╔══██║██╔══██╗██║  ██║██║   ██║██║╚██╔╝██║
  ╚██████╔╝██║  ██║██║  ██║██████╔╝██████╔╝╚██████╔╝██║ ╚═╝ ██║
   ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═════╝  ╚═════╝ ╚═╝     ╚═╝
{Fore.RED}╔══════════════════════════════════════════════════════════════════╗
{Fore.RED}║ {Fore.WHITE}[ {Fore.RED}☠ GRABDOM v2.0 {Fore.WHITE}] {Fore.YELLOW}Domain Ripper - hax.or.id Archive Extractor   {Fore.RED}║
{Fore.RED}║ {Fore.WHITE}[ {Fore.RED}⚡ Created by null7 {Fore.WHITE}] {Fore.CYAN}Real-time save. One list to rule them all.  {Fore.RED}║
{Fore.RED}╚══════════════════════════════════════════════════════════════════╝

{Fore.WHITE}{Style.BRIGHT}  📌 TOOL DESCRIPTION:
{Fore.CYAN}  ─────────────────────────────────────────────────────────────
{Fore.YELLOW}  ⚡ Extract all defaced domains from hax.or.id by attacker name
{Fore.YELLOW}  ⚡ Auto-pagination through all archive pages
{Fore.YELLOW}  ⚡ Real-time saving: domains written instantly per page
{Fore.YELLOW}  ⚡ ALL attackers saved to single file: {Fore.GREEN}{MASTER_FILE}
{Fore.YELLOW}  ⚡ No duplicates: same domain won't be saved twice
{Fore.CYAN}  ─────────────────────────────────────────────────────────────

{Fore.RED}{Style.BRIGHT}  ☠  THE WINNER TAKES ALL :(

{Fore.RED}  ☠  USE AT YOUR OWN RISK - FOR RESEARCH PURPOSES ONLY  ☠

"""
    print(BANNER)

def clean_domain(url):
    """Extract only main domain from URL, no paths, no subdirs"""
    if not url.startswith('http'):
        url = 'http://' + url
    parsed = urlparse(url)
    domain = parsed.netloc
    if domain.startswith('www.'):
        domain = domain[4:]
    scheme = parsed.scheme if parsed.scheme else 'http'
    return f"{scheme}://{domain}"

def load_existing_domains():
    """Load already saved domains from master file to avoid duplicates"""
    if not os.path.exists(MASTER_FILE):
        return set()
    with open(MASTER_FILE, "r", encoding="utf-8") as f:
        return set(line.strip() for line in f if line.strip())

def save_domains_now(new_domains):
    """Instantly append new domains to master file"""
    with open(MASTER_FILE, "a", encoding="utf-8") as f:
        for d in sorted(new_domains):
            f.write(d + "\n")
        f.flush()

def scrape_attacker(name):
    base_url = "https://hax.or.id/archive/attacker/"
    existing_domains = load_existing_domains()
    attacker_domains = set()
    page = 1
    total_pages = 0
    total_new = 0
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }

    print(Fore.WHITE + Style.BRIGHT + f"[*] Target: {Fore.RED}{name}")
    print(Fore.WHITE + f"[*] Master file: {Fore.GREEN}{MASTER_FILE} {Fore.WHITE}| Existing domains: {Fore.YELLOW}{len(existing_domains)}")
    print(Fore.CYAN + "─" * 70 + "\n")

    while True:
        if page == 1:
            target = base_url + name
        else:
            target = f"{base_url}{name}&page={page}"

        print(Fore.CYAN + f"  [{Fore.WHITE}PAGE {page}{Fore.CYAN}] {Fore.YELLOW}{target}")
        
        try:
            resp = requests.get(target, headers=headers, timeout=15)
            if resp.status_code != 200:
                if page == 1:
                    print(Fore.RED + f"\n[!] Attacker '{name}' not found or server error.")
                    return
                else:
                    print(Fore.YELLOW + f"      ↳ Status {resp.status_code}. Pagination complete.\n")
                break
        except Exception as e:
            print(Fore.RED + f"      ↳ Connection failed: {e}\n")
            break

        soup = BeautifulSoup(resp.text, "html.parser")
        page_domains = set()
        
        for link in soup.find_all("a", href=True):
            href = link["href"]
            text = link.get_text(strip=True)
            
            if "/mirror/" in href and text and '.' in text:
                cleaned = clean_domain(text)
                page_domains.add(cleaned)
            elif text.startswith('http') and '.' in text:
                cleaned = clean_domain(text)
                page_domains.add(cleaned)
        
        if not page_domains:
            text = soup.get_text()
            domain_regex = re.findall(r'https?://[^\s<>"]+', text)
            for d in domain_regex:
                cleaned = clean_domain(d)
                if '.' in cleaned:
                    page_domains.add(cleaned)
        
        # Filter out domains already in master file
        new_on_page = page_domains - existing_domains
        
        print(Fore.GREEN + f"      ↳ Found: {Fore.WHITE}{len(page_domains)} {Fore.GREEN}| New: {Fore.WHITE}{len(new_on_page)}")
        
        if new_on_page:
            # SAVE IMMEDIATELY
            save_domains_now(new_on_page)
            existing_domains.update(new_on_page)
            attacker_domains.update(new_on_page)
            total_new += len(new_on_page)
            print(Fore.MAGENTA + f"      ↳ 💾 Saved {len(new_on_page)} domains to {MASTER_FILE} instantly!")
        
        if not page_domains:
            print(Fore.YELLOW + "      ↳ Empty page. Stopping.\n")
            break
        
        total_pages += 1
        page += 1
        time.sleep(0.3)

    if total_new == 0:
        print(Fore.YELLOW + "\n[!] No new domains found for this attacker (all already in master list).")
        return

    print(Fore.CYAN + "─" * 70)
    print(Fore.GREEN + Style.BRIGHT + f"\n[✓] HARVEST COMPLETE!")
    print(Fore.WHITE + f"    ├─ Attacker: {Fore.RED}{name}")
    print(Fore.WHITE + f"    ├─ Pages scraped: {Fore.YELLOW}{total_pages}")
    print(Fore.WHITE + f"    ├─ New domains added: {Fore.GREEN}{total_new}")
    print(Fore.WHITE + f"    ├─ Total in master list: {Fore.CYAN}{len(existing_domains)}")
    print(Fore.WHITE + f"    └─ Master file: {Fore.CYAN}{MASTER_FILE}")
    
    print(Fore.RED + "\n[☠] Latest captured domains:")
    print(Fore.MAGENTA + "─" * 70)
    for idx, d in enumerate(sorted(attacker_domains)[:15], 1):
        print(Fore.WHITE + f"  {Fore.RED}{idx:02d}. {Fore.YELLOW}{d}")
    if len(attacker_domains) > 15:
        print(Fore.CYAN + f"\n  ... and {Fore.WHITE}{len(attacker_domains)-15}{Fore.CYAN} more from this attacker")
    print(Fore.MAGENTA + "─" * 70)
    print(Fore.RED + Style.BRIGHT + "\n  ☠  THE WINNER TAKES ALL :(\n")

if __name__ == "__main__":
    show_banner()
    
    if os.path.exists(MASTER_FILE):
        existing = load_existing_domains()
        print(Fore.GREEN + f"[i] Master list found: {Fore.WHITE}{len(existing)} {Fore.GREEN}domains already collected\n")
    else:
        print(Fore.YELLOW + "[i] No master list yet. Starting fresh.\n")
    
    attacker = input(Fore.WHITE + Style.BRIGHT + "[?] Enter attacker name (e.g. Irene): ").strip()
    if not attacker:
        print(Fore.RED + "\n[!] You must specify a target. Exiting...")
        sys.exit(1)
    print()
    scrape_attacker(attacker)
