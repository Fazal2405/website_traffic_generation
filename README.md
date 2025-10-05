# 🚀 GA4 Traffic Generation Automation (Selenium + Python)

This project simulates organic and referral traffic to a dummy website connected to **Google Analytics 4 (GA4)** using **Selenium WebDriver**, **rotating proxies**, and **dynamic user-agents**.  
It was built for experimentation and analytics visualization during my internship at **GM Infotech**.

---

## 🧠 Overview

The script automates browser sessions across multiple threads, each using a unique proxy and user-agent to simulate visits from various marketing sources (Google, Instagram, Email Campaigns, etc.).  
This helps visualize **real-time user traffic**, **session durations**, and **UTM tracking** on the GA4 dashboard.

**Core file:** `ga4_proxy_webshare_rotating_10threads.py`

---

## ⚙️ Features

- ✅ Multi-threaded Selenium sessions (parallel visitors)  
- 🌐 Rotating proxies for realistic geographic spread  
- 🧭 Randomized user-agents to mimic different browsers/devices  
- 📊 UTM parameter tagging for traffic-source attribution  
- 🕓 Automated scrolling & navigation to simulate user engagement  
- 🔁 Automatic ChromeDriver management with `webdriver-manager`  

---

## 🛠️ Tech Stack

| Component | Tool |
|------------|------|
| Language | Python 3.11 |
| Automation | Selenium WebDriver |
| Proxy Management | Webshare.io Rotating Endpoint |
| Driver Handling | webdriver-manager |
| Analytics | Google Analytics 4 (GA4) |
| IDE | Visual Studio Code |

---

## 📦 Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/fazal2405/website_traffic_generation.git
cd website_traffic_generation

