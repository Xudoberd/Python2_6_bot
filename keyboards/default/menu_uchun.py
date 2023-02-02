from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
from loader import obyekt

# menu_buttyons = ReplyKeyboardMarkup(
#     keyboard=[
#         [
#             KeyboardButton(text="SMARTPONE"),
#             KeyboardButton(text="Oziq ovqat")
#         ],
#         [
#             KeyboardButton(text="MUZLATKICH"),
#             KeyboardButton(text="Air Pods")
#         ],
#         [
#             KeyboardButton(text="Adminga murojat")
#         ],
#         [
#             KeyboardButton(text="Lokatsiya",request_location=True),
#             KeyboardButton(text="Kontakt",request_contact=True)
#         ]
#     ],
#     resize_keyboard=True
# )

menular = obyekt.select_barcha_menular()

j = 0
ingex = 0
keys = []
for menu in menular:
    if j % 2 == 0 and j != 0:
        ingex += 1
    if j % 2 == 0:
        keys.append([KeyboardButton(text=f'{menu[1]}', )])
    else:
        keys[ingex].append(KeyboardButton(text=f'{menu[1]}', ))
    j += 1

keys.append([KeyboardButton(text='Adminga murojat')])
menu_buttons = ReplyKeyboardMarkup(keyboard=keys,resize_keyboard=True)

tasdiqlash_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Tasdiqlash"),
            KeyboardButton(text="Bekor qilish")

        ]
    ],
    resize_keyboard=True
)