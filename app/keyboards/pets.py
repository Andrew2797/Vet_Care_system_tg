from aiogram.utils.keyboard import InlineKeyboardBuilder


def build_pets_keyboard(pets: list):
    builder = InlineKeyboardBuilder()

    for index, pet in enumerate(pets):
        builder.button(text=pet, callback_data=f"pet_{index}")

    builder.adjust(4)
    return builder.as_markup()


def build_pet_actions_keyboard(index: str|int):
    builder = InlineKeyboardBuilder()
    builder.button(text="Вилікувати тваринку", callback_data=f"healed_pet_{index}")
    builder.button(text="Забрати тваринку", callback_data=f"remove_pet_{index}")
    return builder.as_markup()
