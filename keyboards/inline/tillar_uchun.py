from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton

tillar_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="O'zbek tili"),
            InlineKeyboardButton(text="Ingiliz tili")
        ],
        [
            InlineKeyboardButton(text="Hamkorlarimiz",url=''),
            InlineKeyboardButton(text="Ulashish",switch_inline_query='')
        ]
    ],
)