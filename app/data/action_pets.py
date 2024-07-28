import json

from app.data import list_files, open_files


def remove_pet(pet_index: int) -> str:
    pets = open_files.get_pets()
    pet = pets.pop(pet_index)

    with open(list_files.PETS, "w", encoding="utf-8") as file:
        json.dump(pets, file)

    msg = f"Тваринку '{pet}' було успішно забрано."
    return msg


def healed_pet(pet_index: int) -> str:
    pets = open_files.get_pets()
    pet = pets.pop(pet_index)

    healed_pets = open_files.get_healed_pets()
    healed_pets.append(pet)

    with open(list_files.PETS, "w", encoding="utf-8") as file:
        json.dump(pets, file)

    with open(list_files.HEALED_PETS, "w", encoding="utf-8") as file:
        json.dump(healed_pets, file)

    msg = f"Тваринка '{pet}' успішно вилікувано. Дякую що обрали нас."
    return msg


def add_pet(pet: str) -> str:
    pets = open_files.get_pets()

    if pet in pets:
        msg = f"Тваринка '{pet}' вже перебуває на лікуванні."
        return msg

    pets.append(pet)

    with open(list_files.PETS, "w", encoding="utf-8") as file:
        json.dump(pets, file)

    msg = f"Тваринка '{pet}' успішно додана."
    return msg