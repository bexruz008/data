from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def inline_user_button() -> InlineKeyboardButton:
    ikm = InlineKeyboardMarkup()
    button = InlineKeyboardButton(text="Add User", callback_data="add_user")
    button2 = InlineKeyboardButton(text="All User", callback_data="all_user")
    button3 = InlineKeyboardButton(text="Get User", callback_data="get_user")
    button4 = InlineKeyboardButton(text="Update User", callback_data="update_user")
    button5 = InlineKeyboardButton(text="Delete User", callback_data="delete_user")
    ikm.add(button, button2, button3, button4, button5)
    return ikm

#
# def userbutton():
#     ikb = InlineKeyboardMarkup()
#     button = InlineKeyboardButton(text="Ha", callback_data="ha")
#     button2 = InlineKeyboardButton(text="Yo'q", callback_data="yo'q")
#     ikb.add(button, button2)
#     return ikb