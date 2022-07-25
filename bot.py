import logging
from aiogram import Bot, Dispatcher, types, executor
from main import req

with open('token.txt', 'r') as t:
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
                        "Send me the name of the city and I will show you the time and weather in it")


async def get_data():
    # TODO: Get the city from the user, call the req(city) function, format the data and send it to the user
    city = 'Moscow'
    print(req(city))

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
