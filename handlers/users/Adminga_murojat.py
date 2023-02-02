from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.default.menu_uchun import tasdiqlash_buttons,menu_buttyons
from loader import dp,bot
from states.Murojat_uchun import Forma

# Echo bot
@dp.message_handler(text="Adminga murojat")
async def bot_echo(message: types.Message):
    await message.answer(text="Ismni kiriting ...")
    await Forma.ism_qabul_qilish_holati.set()

@dp.message_handler(state=Forma.ism_qabul_qilish_holati)
async def bot_start(message: types.Message,state:FSMContext):
    ism = message.text
    await state.update_data({"name":ism})

    await message.answer(f"Familyani kiriting ...")
    await Forma.fam_qabul_qilish_holati.set()


@dp.message_handler(state=Forma.fam_qabul_qilish_holati)
async def bot_start(message: types.Message, state: FSMContext):
    familya = message.text
    await state.update_data({"fam": familya})

    await message.answer(f"Yoshni kiriting ...")
    await Forma.yosh_qabul_qilish_holati.set()


@dp.message_handler(state=Forma.yosh_qabul_qilish_holati)
async def bot_start(message: types.Message, state: FSMContext):
    yoshi = message.text
    await state.update_data({"yosh": yoshi})

    await message.answer(f"Telefon raqamngizni kiriting ...")
    await Forma.tel_qabul_qilish_holati.set()


@dp.message_handler(state=Forma.tel_qabul_qilish_holati)
async def bot_start(message: types.Message, state: FSMContext):
    nomer = message.text
    await state.update_data({"tel": nomer})

    await message.answer(f"Murojaatingizni kiriting ...")
    await Forma.msg_qabul_qilish_holati.set()


@dp.message_handler(state=Forma.msg_qabul_qilish_holati)
async def bot_start(message: types.Message, state: FSMContext):
    matn = message.text
    await state.update_data({"text": matn})

    user_id = message.from_user.id

    malumot = await state.get_data()

    ismi = malumot.get('name')
    familyasi = malumot.get('fam')
    yoshi = malumot.get('yosh')
    teli = malumot.get('tel')
    murojati = malumot.get('text')

    text = f"Ism : {ismi}\n" \
          f"Familya : {familyasi}\n" \
          f"Yosh : {yoshi}\n" \
          f"Tel : {teli}\n" \
          f"Murojat : {murojati}\n"

    await bot.send_message(chat_id=user_id,text=text,reply_markup=tasdiqlash_buttons)
    await Forma.tasdiqlash_holati.set()

@dp.message_handler(state=Forma.tasdiqlash_holati,text='Bekor qilish')
async def bot_start(message: types.Message, state: FSMContext):

    await message.answer(f"Bekor qilindi",reply_markup=menu_buttyons)
    await state.finish()

@dp.message_handler(state=Forma.tasdiqlash_holati,text='Tasdiqlash')
async def bot_start(message: types.Message, state: FSMContext):
    malumot = await state.get_data()
    user_id = message.from_user.id
    ismi = malumot.get('name')
    familyasi = malumot.get('fam')
    yoshi = malumot.get('yosh')
    teli = malumot.get('tel')
    murojati = malumot.get('text')

    text = f"Ism : {ismi}\n" \
           f"Familya : {familyasi}\n" \
           f"Yosh : {yoshi}\n" \
           f"Tel : {teli}\n" \
           f"Murojat : {murojati}\n"
    await bot.send_message(chat_id='2139874256',text=text)
    await bot.send_message(chat_id=user_id,text="Adminga yuborildi",reply_markup=menu_buttyons)
    await state.finish()