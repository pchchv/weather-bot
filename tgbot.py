import asyncio
from aiogram import Bot

with open('token.txt', 'r') as t:
    BOT_TOKEN = t.read()
t.close()


async def main():
    bot = Bot(token=BOT_TOKEN)

    try:
        me = await bot.get_me()
        print(f"🤖 Hello, I'm {me.first_name}.\nHave a nice Day!")
    finally:
        await bot.close()
