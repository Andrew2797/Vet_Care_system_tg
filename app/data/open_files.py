import os
import json

from app.data import list_files


if not os.path.exists(list_files.PETS):
    with open(list_files.PETS, "w", encoding="utf-8") as file:
        json.dump([], file)

if not os.path.exists(list_files.HEALED_PETS):
    with open(list_files.HEALED_PETS, "w", encoding="utf-8") as file:
        json.dump([], file)

if not os.path.exists(list_files.REVIEWS):
    with open(list_files.REVIEWS, "w", encoding="utf-8") as file:
        json.dump([], file)


def get_pets(path: str = list_files.PETS) -> list[str]:
    with open(path, "r", encoding="utf-8") as file:
        pets = json.load(file)

    return pets


def get_pet(pet_index: int) -> str:
    pets = get_pets()
    return pets[pet_index]


def get_healed_pets(path: str = list_files.HEALED_PETS) -> list[str]:
    with open(path, "r", encoding="utf-8") as file:
        healed_pets = json.load(file)

    return healed_pets


def get_reviews(path: str = list_files.REVIEWS) -> list:
    with open(path, "r", encoding="utf-8") as file:
        reviews = json.load(file)

    return reviews