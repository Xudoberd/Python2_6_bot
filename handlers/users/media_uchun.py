from aiogram import types
from aiogram.types import ContentTypes,InputFile

from loader import dp,bot



# Echo bot
@dp.message_handler(content_types=ContentTypes.DOCUMENT)
async def bot_echo(message: types.Message):
    await message.document.download()
    await message.answer(text=f"Fayl qabul qilindi")



@dp.message_handler(content_types=ContentTypes.PHOTO)
async def bot_echo(message: types.Message):
    await message.photo[-1].download()
    await message.answer(text=f"{message}")



@dp.message_handler(text="SMARTPONE")
async def bot_echo(message: types.Message):


    rasm_manzili = "https://t.me/HousemobileAAA/3258"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili)



@dp.message_handler(text="MUZLATKICH")
async def bot_echo(message: types.Message):


    rasm_manzili = "https://t.me/texnogrand_xolodilnik/2660"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili)



@dp.message_handler(text="Air Pods")
async def bot_echo(message: types.Message):


    rasm_manzili = "https://t.me/housemobileuz/467"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili)




