from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

Oziq_ovqat_buttons = ReplyKeyboardMarkup(
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
