from aiogram import Bot, Dispatcher, executor, types

API_KEY = '6101167784:AAEYbdJVgyfxLGvhJMuZ5njEkVkqWlv70Yc'

bot = Bot(token=API_KEY)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(msg: types.Message):
    print('Start command called')
    await msg.reply('Start command...')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
