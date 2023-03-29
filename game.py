import random
import json


def upd_file(filename, some_upd):
    with open(filename, "w", encoding='utf-8') as my_file:
        my_file.writelines(some_upd)


test = "Game_test.txt"


def create_a_random_hero(result=test):
    mage_semi_class = [
        "Иллюзий",
        "Телепат",
        "Огня",
        "Некромант",
        "Друид",
    ]
    fighter_semi_class = [
        "Рыцарь",
        "Варвар",
        "Воин",
        "Сорвиголова",
    ]
    clas = [
        "Маг",
        "Боец",
        "Торговец",
        "Странник",
        "Целитель",
    ]
    rand_clas = random.choice(clas)
    rand_semi_class = random.choice(fighter_semi_class) if rand_clas == "Боец" else "Не является Воином"
    rand_semi_mage_class = random.choice(mage_semi_class) if rand_clas == "Маг" else "Не является магом"
    weapon = [
        "Меч",
        "Копьё",
        "Топор",
        "Дубинка",
        "Молот",
        "Лук",
        "Ножи",
    ]
    if rand_clas == "Боец" and rand_semi_class == "Рыцарь":
        weapon = [
            "Меч",
            "копьё",
        ]
    elif rand_clas == "Боец" and rand_semi_class == "Варвар":
        weapon = [
            "Топор",
            "Дубинка",
        ]
    elif rand_clas == "Боец" and rand_semi_class == "Воин":
        weapon = [
            "Молот",
        ]
    elif rand_clas == "Боец" and rand_semi_class == "Сорвиголова":
        weapon = [
            "Лук",
            "Ножи",
        ]
    shield = [
        "Отсутствует",
        "лёгкая",
        "средняя",
        "хорошая",
        "усиленная",
    ]
    strenght = random.randint(1, 10)
    intelect = random.randint(1, 10)
    harism = random.randint(1, 10)
    agility = random.randint(1, 10)
    rand_weapon = random.choice(weapon)
    rand_shield = random.choice(shield)
    way = [
        "Месть за семью/дом",
        "Поиски лекарства",
        "Побег от смерти",
        "Путешествия/приключения",
        "Изгнание",
        "Поиски близкого",
    ]
    rand_way = random.choice(way)
    if rand_clas == "Боец":
        strenght = random.randint(5, 10)
    elif rand_clas == "Маг":
        intelect = random.randint(5, 10)
    elif rand_clas == "Торговец":
        harism = random.randint(5, 10)
    unit = f"Класс: {rand_clas} \n Под-класс: {rand_semi_class, rand_semi_mage_class} \n Сила: {strenght} " \
                 f"\n Интелект: {intelect} \n Харизма: {harism} \n Ловкость: {agility} \n \n Броня: {rand_shield}" \
                 f" \n Цель: {rand_way}\n Оружие:{rand_weapon} \n"
    upd_file(test, unit)
    return unit


def balk_insert(num: int):
    result = []
    for _ in range(num):
        info = create_a_random_hero()
        result.append(info)
    upd_file(test, result)


json_data = "data.json"
result_dict = {
    "unit": balk_insert(2)
}


def save_progress(file_name, res):
    with open(file_name, "w") as my_data:
        json.dump(res, my_data)


save_progress(json_data, result_dict)
