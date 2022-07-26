import logging
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
    # TODO: Format the data before sending it to the user
    city = message.text
    await message.reply(req(city))

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
