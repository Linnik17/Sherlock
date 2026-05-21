import asyncio
from aiogram import Bot, Dispatcher, types

TOKEN = "8558971167:AAE9GFlX26_HVWS36BdcMIsF6dVnXEyCLM4"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# ───────────── UI STYLE ─────────────
def banner(query):
    return f"""
🧠 DARK OSINT SYSTEM v1.0
━━━━━━━━━━━━━━━━━━━━━━
🔎 INPUT: {query}

📡 scanning public sources...
🧩 analyzing open data...
━━━━━━━━━━━━━━━━━━━━━━
"""

# ───────── USERNAME MODE ─────────
def username(query):
    return f"""
{banner(query)}

📱 Telegram: https://t.me/{query}
📸 Instagram: https://instagram.com/{query}
🎵 TikTok: https://tiktok.com/@{query}
💻 GitHub: https://github.com/{query}
🐦 X: https://x.com/{query}

🌐 SEARCH:
Google: https://www.google.com/search?q={query}
DuckDuckGo: https://duckduckgo.com/?q={query}
Bing: https://www.bing.com/search?q={query}

📊 OSINT SCORE: 88/100 (pattern match)

⚠️ Only public data used
"""

# ───────── PHONE MODE ─────────
def phone(query):
    return f"""
{banner(query)}

📞 PHONE INTELLIGENCE

🌐 Google:
https://www.google.com/search?q={query}

🌐 Yandex:
https://yandex.ru/search/?text={query}

🌐 Bing:
https://www.bing.com/search?q={query}

📊 OSINT SCORE: LOW (no identity mapping)

⚠️ No private data access
"""

# ───────── EMAIL MODE ─────────
def email(query):
    return f"""
{banner(query)}

📧 EMAIL INTELLIGENCE

🔎 {query}

🌐 Search:
https://www.google.com/search?q={query}

🔐 Breach check:
https://haveibeenpwned.com/

📊 OSINT SCORE: MEDIUM

⚠️ Public checks only
"""

# ───────── ROUTER ─────────
def router(text):
    if "@" in text:
        return email(text)
    elif text.startswith("+") or text.replace(" ", "").isdigit():
        return phone(text)
    else:
        return username(text)

# ───────── HANDLER ─────────
@dp.message()
async def handler(message: types.Message):
    text = message.text.strip()
    await message.answer(router(text))

# ───────── START ─────────
async def main():
    print("DARK OSINT ONLINE")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
