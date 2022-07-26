import logging
import requests
from aiogram import Bot, Dispatcher, types, executor

with open('token.txt', 'r', encoding=str) as t:
    BOT_TOKEN = t.read()
t.close()

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi " + message.from_user.first_name + "!\nI'm WeatherBot!\n" +
                        "Send me the name of the city " +
                        "and I will show you the time and weather in it")


@dp.message_handler()
async def get_data(message: types.Message):
    """
    This handler will be called when the user sends any message (not a command) 
    """
    # TODO: Add request error handling
    #     Format the data before sending it to the user
    city = message.text
    url = 'http://localhost:8080/stats?city=' + city
    res = requests.get(url)
    await message.reply(res)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
