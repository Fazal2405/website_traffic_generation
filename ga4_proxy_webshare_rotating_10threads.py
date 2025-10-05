import threading
import random
import time
import math

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import WebDriverException
from webdriver_manager.chrome import ChromeDriverManager

# ── CONFIGURATION ──────────────────────────────────────────────────────────────

BASE_URL = "https://delightful-trifle-8ce1c5.netlify.app"
TOTAL_VISITS = 10000
THREAD_COUNT = 10 
VISITS_PER_THREAD = math.ceil(TOTAL_VISITS / THREAD_COUNT)

# load proxies (1 per line)
with open('proxies.txt', 'r') as pf:
    PROXIES = [line.strip() for line in pf if line.strip()]

# load user-agents
with open('user_agents.txt', 'r') as uf:
    USER_AGENTS = [line.strip() for line in uf if line.strip()]

UTM_SOURCES = [
    {"source": "google",         "medium": "organic"},
    {"source": "instagram",      "medium": "social"},
    {"source": "email_campaign", "medium": "email"},
    {"source": "referral_partner","medium": "referral"},
    {"source": "whatsapp",       "medium": "social"},
]

# ── SIMULATION FUNCTION ────────────────────────────────────────────────────────

def simulate_thread(thread_id, visits, proxy):
    ua = random.choice(USER_AGENTS)
    print(f"[T{thread_id}] Using proxy {proxy} with UA: {ua}")

    opts = webdriver.ChromeOptions()
    opts.add_argument(f"--proxy-server={proxy}")
    opts.add_argument(f"--user-agent={ua}")
    opts.add_argument("--headless")
    opts.add_argument("--disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=opts)

    for i in range(visits):
        utm = random.choice(UTM_SOURCES)
        entry_url = f"{BASE_URL}?utm_source={utm['source']}&utm_medium={utm['medium']}"

        try:
            print(f"[T{thread_id}] Visit {i+1}/{visits} → {entry_url}")
            driver.get(entry_url)
            time.sleep(random.uniform(2, 4))
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(random.uniform(2, 3))

            # Visit sub-pages
            for page in ("about.html", "contact.html"):
                purl = f"{BASE_URL}/{page}?utm_source={utm['source']}&utm_medium={utm['medium']}"
                print(f"[T{thread_id}] → {purl}")
                driver.get(purl)
                time.sleep(random.uniform(1, 2))
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(0.5)

            # Revisit homepage to simulate returning visitor
            print(f"[T{thread_id}] Revisiting homepage")
            driver.get(entry_url)
            time.sleep(random.uniform(1, 3))

        except WebDriverException as e:
            print(f"[T{thread_id}] Error: {e}")
            continue

    driver.quit()

# ── LAUNCH THREADS ─────────────────────────────────────────────────────────────

threads = []
for tid in range(THREAD_COUNT):
    proxy = PROXIES[tid % len(PROXIES)]  # Cycle through if fewer proxies
    t = threading.Thread(target=simulate_thread, args=(tid, VISITS_PER_THREAD, proxy))
    t.daemon = True
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print(f"✅ Completed at least {TOTAL_VISITS} visits across {THREAD_COUNT} threads.")
