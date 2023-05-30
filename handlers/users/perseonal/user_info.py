from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardRemove, inline_keyboard, ReplyKeyboardMarkup, message

from keyboards.default import user_button
from keyboards.default.user_button import user_rkm, cancel
from keyboards.inline import user_inline_button
from keyboards.inline.user_inline_button import inline_user_button
from loader import dp, db
from states.user_state import AddUserState, EditUserState, DeleatedUserState, GetUserState


@dp.message_handler(commands="cancel", state="*")
async def get_cancel(message: types.Message, state:FSMContext):
    await message.answer(text="Bekor qilindi",
                         reply_markup=inline_user_button())
    await state.finish()

@dp.message_handler(Text(equals="user"))
async def get_info(message: types.Message):
    await message.answer(text="Foydalanuvchilarni tahrirlash",
                         reply_markup=ReplyKeyboardRemove())
    await message.answer(text="Qaysi amalni tanlaysiz",
                         reply_markup=inline_user_button())



@dp.callback_query_handler()
async def user_callback(callback: types.CallbackQuery):
    if callback.data == "add_user":
        await callback.message.answer(text="Foydalanuvchini ismini kiriting",
                                      reply_markup=cancel())


        await AddUserState.name.set()
    elif callback.data == "all_user":
        users = db.all_user()
        for user in users:
            await callback.message.answer_photo(photo=user[5],
                                                caption=f"Foydalanuvchini ismi {user[1]},\n"
                                                        f"yoshi {user[2]},\n"
                                                        f"Telefon raqami {user[3]},"
                                                        f"Emaili {user[4]}")
    elif callback.data == "delete_user":
        await callback.message.answer("id ni kiriting",
                                      reply_markup=ReplyKeyboardRemove())

        await callback.message.answer(text="qaysi idli foydalanuvchini uchirasiz",
                                      reply_markup=cancel())
        await DeleatedUserState.id.set()

    elif callback.data == "get_user":
        await callback.message.answer("id ni kiriting",
                                      reply_markup=ReplyKeyboardRemove())

        await callback.message.answer(text="qaysi id li foydalanuvchini olmoqchisiz",
                                      reply_markup=cancel())
        await GetUserState.id.set()

    elif callback.data == "update_user":
        await callback.message.answer(text="foydalanuvchini id sini kiriting",
                                      reply_markup=cancel())
        await EditUserState.id.set()
