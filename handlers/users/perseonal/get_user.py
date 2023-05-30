from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import message
from loader import dp, db
from states.user_state import GetUserState, EditUserState, DeleatedUserState





@dp.message_handler(state=GetUserState)
async def get_user (messaga: types.Message):
    global user_id
    user_id = int(messaga.text)
    user = db.get_user(user_id)
    if user:
        await messaga.answer_photo(photo=user[5],
                                   caption=f"Foydalanuvchini ismi: {user[1]},"
                                           f"Foydalanuvchini yoshi: {user[2]},"
                                           f"Foydalanuvchini telefon raqami: {user[3]},"
                                           f"Foydalanuvchini Emaili: {user[4]}")
