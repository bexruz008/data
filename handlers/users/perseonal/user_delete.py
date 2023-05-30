from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.inline.user_inline_button import inline_user_button
from loader import dp, db, bot
from states.user_state import DeleatedUserState


@dp.message_handler(state=DeleatedUserState.id)
async def delete_user(message: types.Message, state: FSMContext):
    global user_id
    user_id = int(message.text)
    user = db.get_user(id=user_id)
    if user:
        await bot.send_photo(chat_id=message.chat.id,
                             photo=user[5],
                             caption=f"Foydalanuvchini ismi {user[1]},\n"
                                     f"yoshi {user[2]}, \n"
                                     f"telefon raqamini {user[3]}, \n"
                                     f"emaili {user[4]} \n")
        await message.answer("Shu foydalanuvchini o'chirishni hohlaysizmi? (ha/yo'q)")
        await DeleatedUserState.next()


@dp.message_handler(state=DeleatedUserState.confirm)
async def delete_user(message: types.Message, state: FSMContext):
    if message.text.lower() == "ha":
        db.delete_user(id=user_id)
        await message.answer("Ushbu foydalanuvchini muvuffaqiyatli o'chirildi")
    else:
       await state.finish()
       await message.answer(text="Bekor qilindi",
                            reply_markup=inline_user_button())