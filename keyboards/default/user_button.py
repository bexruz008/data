from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def user_rkm() -> ReplyKeyboardMarkup:
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton(text="user")
    rkm.add(button)
    return rkm
