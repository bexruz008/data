from aiogram.dispatcher.filters.state import StatesGroup, State


class AddUserState(StatesGroup):
    name = State()
    age = State()
    phone_number = State()
    email = State()
    photo = State()


class EditUserState(StatesGroup):
    id = State()
    chec_name = State()
    name = State()
    chec_age = State()
    age = State()
    phone_number = State()
    email = State()
    photo = State()


class DeleatedUserState(StatesGroup):
    id = State()
    confirm = State()



class GetUserState(StatesGroup):
    id = State()
    confirm = State()