from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from app.data import open_files, action_pets
from app.keyboards.pets import build_pets_keyboard, build_pet_actions_keyboard
from app.forms.pets import PetForm


pet_router = Router()


async def edit_or_answer(message: Message, text: str, keyboard=None, *args, **kwargs):
   if message.from_user.is_bot:
       await message.edit_text(text=text, reply_markup=keyboard, **kwargs)
   else:
       await message.answer(text=text, reply_markup=keyboard, **kwargs)


@pet_router.message(F.text == "Список тваринок на лікуванні")
async def show_pets(message: Message, state: FSMContext):
    pets = open_files.get_pets()
    keyboard = build_pets_keyboard(pets)
    await edit_or_answer(
        message=message,
        text="Список тваринок",
        keyboard=keyboard
    )


@pet_router.callback_query(F.data.startswith("pet_"))
async def pet_actions(call_back: CallbackQuery, state: FSMContext):
    pet_index = int(call_back.data.split("_")[-1])
    pet = open_files.get_pet(pet_index)
    keyboard = build_pet_actions_keyboard(pet_index)
    await edit_or_answer(
        message=call_back.message,
        text=pet,
        keyboard=keyboard
    )


@pet_router.callback_query(F.data.startswith("remove_pet_"))
async def remove_pet(call_back: CallbackQuery, state: FSMContext):
    pet_index = int(call_back.data.split("_")[-1])
    msg = action_pets.remove_pet(pet_index)
    await edit_or_answer(
        message=call_back.message,
        text=msg
    )


@pet_router.callback_query(F.data.startswith("healed_pet_"))
async def healed_pet(call_back: CallbackQuery, state: FSMContext):
    pet_index = int(call_back.data.split("_")[-1])
    msg = action_pets.healed_pet(pet_index)
    await edit_or_answer(
        message=call_back.message,
        text=msg
    )


@pet_router.message(F.text == "Показати список вилікуваних тваринок")
async def shoe_healed_pet(message: Message, state: FSMContext):
    healed_pets = open_files.get_healed_pets()
    msg = ""
    for i, pet in enumerate(healed_pets, start=1):
        msg += f"{i}. {pet}\n"

    await message.answer(text=msg)


@pet_router.message(F.text == "Зарахувати нову тваринку на лікування")
async def add_pet(message: Message, state: FSMContext):
    await state.clear()
    await state.set_state(PetForm.name)
    await edit_or_answer(
        message=message,
        text="Введіть назву тваринки"
    )


@pet_router.message(PetForm.name)
async def add_pet_name(message: Message, state: FSMContext):
    data = await state.update_data(name=message.text)
    await state.clear()
    msg = action_pets.add_pet(data.get("name"))
    await edit_or_answer(
        message=message,
        text=msg
    )