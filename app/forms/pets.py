from aiogram.fsm.state import State, StatesGroup


class PetForm(StatesGroup):
    name = State()