import asyncio
import os
from aiogram import Bot, Dispatcher, types

TOKEN = os.getenv("TOKEN")

if not TOKEN:
    raise ValueError("TOKEN is not set in environment variables")

bot = Bot(token=TOKEN)
dp = Dispatcher()

def is_phone(text):
    t = text.replace(" ", "").replace("-", "")
    return t.startswith("+") or t.isdigit()

def is_email(text):
    return "@" in text and "." in text

def build_username(text):
    return f"""
🧠 OSINT REPORT

🔎 Username: {text}

📱 Telegram: https://t.me/{text}
📸 Instagram: https://instagram.com/{text}
🎵 TikTok: https://tiktok.com/@{text}
💻 GitHub: https://github.com/{text}

🌐 Google:
https://www.google.com/search?q={text}

🌐 DuckDuckGo:
https://duckduckgo.com/?q={text}

📊 Status: public sources only
"""

def build_phone(text):
    return f"""
📞 PHONE OSINT REPORT

🔎 Number: {text}

🌐 Google:
https://www.google.com/search?q={text}

⚠️ Only public sources
"""

def build_email(text):
    return f"""
📧 EMAIL OSINT REPORT

🔎 {text}

🌐 Google:
https://www.google.com/search?q={text}

🔐 Breach check:
https://haveibeenpwned.com/

⚠️ Public data only
"""

def router(text):
    if is_email(text):
        return build_email(text)
    elif is_phone(text):
        return build_phone(text)
    else:
        return build_username(text)

@dp.message()
async def handler(message: types.Message):
    try:
        text = message.text.strip()
        await message.answer(router(text))
    except Exception as e:
        await message.answer("⚠️ error processing request")

async def main():
    print("bot started")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
