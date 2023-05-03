from aiogram import types , Dispatcher , Bot ,executor
from api import obhavo

API_TOKEN = '6076876672:AAHG88QS5bwuh09UiydPVw6H3qFJIYA1udY'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
@dp.message_handler(commands='start')
async def send_welcome(message:types.Message):
    await message.reply("Assalom aleykum \n Xush kelibsiz ! \n Men WelicoDev tomonidan yaratilganman !\n Men shaharlardagi ob-havo haqida ma'lumot beraman .")
    await message.answer("Shahar nomini kiriting : >> ")

@dp.message_handler(content_types='text')
async def first_handler(message:types.Message):
    shahar = message.text
    data = obhavo(shahar)
    if data=='Error':
        await message.reply(f"{shahar} shahri haqida ma'lumotga topa olmadim ! \n O'zingiz yaqin bo'lgan kattaroq shahrni yozing !")
    else:
        await message.reply(data)

if __name__=='__main__':
    executor.start_polling(dp)