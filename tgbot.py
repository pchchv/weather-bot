import asyncio
from aiogram import Bot
from main import req

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


asyncio.run(main())


async def get_data():
    # TODO: Get the city from the user, call the req(city) function, format the data and send it to the user
    city = 'Moscow'
    print(req(city))
