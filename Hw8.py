############### 1 ###############


# my_list = [
#     "str",
#     "num",
#     "lock",
#     "print",
#     "asc",
# ]
#
# new_list = [
#
# ]
#
# for el in my_list:
#     if el in my_list[::2]:
#         new_list.append(el[::-1]), "".join(new_list)
#     elif el in my_list[::1]:
#         new_list.append(el), "".join(new_list)
#
#
# print(new_list)



############### 2 ###############


# my_list = [
#     "Abccc",
#     "abccc",
#     "bcaaa",
#     "cdaaa",
#     "aaaacd",
# ]
# result = []
# for el in my_list:
#     if el.startswith("a"):
#         result.append(el)
# print(result)

############### 3 ###############


# my_list = [
#     "bccc",
#     "abccc",
#     "bc",
#     "cdaaa",
#     "aaaacd",
# ]
# result = [
#
# ]
#
# for el in my_list:
#     if el.count("a"):
#         result.append(el)
#
# print(result)

############### 4 ###############
# Даний список словників людей у форматі [{"name": "John", "age": 15}, ..., {"name": "Jack", "age": 45}]
person_1 = {
    "name": "John",
    "age": 44
}

person_2 = {
    "name": "George",
    "age": 17
}

person_3 = {
    "name": "ALina",
    "age": 17
}
person_4 = {
    "name": "vika",
    "age": 25
}

person_5 = {
    "name": "Alex",
    "age": 20
}

peoples = [
        person_1,
        person_2,
        person_3,
        person_4,
        person_5,
]




############ a ##########
# age = [
#
# ]
# names = [
#
# ]
#
#
# for person in peoples:
#     ages = person["age"]
#     age.append(ages)
#
# value_age = min(age)
#
# for el in peoples:
#     el_age = el["age"]
#     if value_age == el_age:
#         names.append(el["name"])
#
# print(names)

############ b ##########
## б) Створити список та помістити туди найдовше ім'я. Якщо довжина імені збігається - помістити такі імена

# names = [
#
# ]
# bigger_name = [
#
# ]
#
# for person in peoples:
#     names.append(person["name"])
#
# for el in names:
#     for i in names:
#         if len(el) > len(i) and bigger_name.count(el) == 0:
#             bigger_name.append(el)
#
#
# print(bigger_name)

############ c ##########

# age = [
#
# ]
#
# for el in peoples:
#     age.append(el["age"])
#
# middle_age = sum(age) / len(age)
# print(middle_age)

############### 5 ###############

# my_dict_1 = {
#     "name": "George",
#     "age": "17",
#     "email": "blablabla@gmail.com",
#     "adress": "str. 1412 city: Kyiv ",
# }
# my_dict_2 = {
#     "name": "Ann",
#     "age": "22",
#     "Email": "ahfhasj@gmail.com",
#     "Adress": "str. 1244 city: New-york ",
# }
#
# result = {
#
# }
######### a #########


# keys_dict = [
#
# ]
#
# keys_dict.append(my_dict_1.keys())
#
# keys_dict.append(my_dict_2.keys())
#
# print(keys_dict)

######### b #########
# result = [
#
# ]
#
# key = my_dict_1.keys()
# if key != my_dict_2.keys():
#     result.append(key)
#
# print(result)

######### c #########


# for key in my_dict_1:
#     if key not in my_dict_2:
#         result[key] = my_dict_1[key]
#
#
# print(result)

######### d #########


# for key in my_dict_1:
#     if key not in my_dict_2:
#         result[key] = my_dict_1[key]
#     elif key in my_dict_2:
#         result[key] = [my_dict_1[key], my_dict_2[key]]
#
#
# print(result)
































