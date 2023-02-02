from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

Maishiy_texnika_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Ichimliklar"),
            KeyboardButton("Shirinliklar")
        ],
        [
            KeyboardButton(text="Sut maxsulotlari"),
            KeyboardButton(text="Go'sht maxsulotlari")
        ]
    ],
    resize_keyboard=True
)
