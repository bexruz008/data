from aiogram import types

from keyboards.default.user_button import user_rkm
from loader import dp, bot


@dp.message_handler(commands='contact')
async def send_contact(message: types.Message):
    await bot.send_contact(chat_id=message.chat.id,
                           phone_number="+998978241511",
                           first_name="Mirafzal",
                           reply_markup=user_rkm())