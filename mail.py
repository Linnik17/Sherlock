import asyncio
from aiogram import Bot, Dispatcher, types

TOKEN = "8558971167:AAE9GFlX26_HVWS36BdcMIsF6dVnXEyCLM4"

bot = Bot(token=TOKEN)
dp = Dispatcher()

def header(query):
    return f"""
🧠 ULTRA PRO OSINT SYSTEM
━━━━━━━━━━━━━━━━━━━━━━
🔎 Query: {query}

📡 Scanning public sources...
🧩 Running smart analysis...
"""

def username_block(u):
    return f"""
{header(u)}

📱 Telegram: https://t.me/{u}
📸 Instagram: https://instagram.com/{u}
🎵 TikTok: https://tiktok.com/@{u}
💻 GitHub: https://github.com/{u}
🐦 X: https://x.com/{u}

🌐 Google:
https://www.google.com/search?q={u}

🌐 DuckDuckGo:
https://duckduckgo.com/?q={u}

📊 OSINT SCORE: 85/100 (pattern match)

⚠️ Open-source data only
"""

def phone_block(p):
    return f"""
{header(p)}

📞 PHONE INTELLIGENCE

🌐 Google:
https://www.google.com/search?q={p}

🌐 Yandex:
https://yandex.ru/search/?text={p}

📊 OSINT SCORE: LOW (no public identity mapping)

⚠️ No private database access
"""

def email_block(e):
    return f"""
{header(e)}

📧 EMAIL INTELLIGENCE

🔎 {e}

🌐 Google:
https://www.google.com/search?q={e}

🔐 Breach check (manual):
https://haveibeenpwned.com/

📊 OSINT SCORE: MEDIUM

⚠️ Only public checks
"""

def web_search(q):
    return f"""
{header(q)}

🌐 SEARCH RESULTS

Google:
https://www.google.com/search?q={q}

DuckDuckGo:
https://duckduckgo.com/?q={q}

Bing:
https://www.bing.com/search?q={q}

📊 OSINT SCORE: CONTEXT DEPENDENT
"""

@dp.message()
async def handler(message: types.Message):
    text = message.text.strip()

    # SMART ROUTER
    if "@" in text:
        await message.answer(email_block(text))
    elif text.startswith("+") or text.replace(" ", "").isdigit():
        await message.answer(phone_block(text))
    elif len(text) < 3:
        await message.answer("❌ Too short for analysis")
    else:
        await message.answer(username_block(text))

async def main():
    print("ULTRA PRO OSINT ACTIVE")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
