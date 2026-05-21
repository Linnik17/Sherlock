import asyncio
from aiogram import Bot, Dispatcher, types

TOKEN = "8558971167:AAE9GFlX26_HVWS36BdcMIsF6dVnXEyCLM4"

bot = Bot(token=TOKEN)
dp = Dispatcher()

def build_links(text: str):
    return f"""
🔎 OSINT SEARCH: {text}

📱 Telegram: https://t.me/{text}
📸 Instagram: https://instagram.com/{text}
🎵 TikTok: https://tiktok.com/@{text}
💻 GitHub: https://github.com/{text}

🌐 Google:
https://www.google.com/search?q={text}

🧠 Only public data used
"""

@dp.message()
async def handler(message: types.Message):
    text = message.text.strip()
    await message.answer(build_links(text))

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
