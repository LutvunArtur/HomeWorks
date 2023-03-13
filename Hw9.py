from random import randint
from string import ascii_lowercase
import random

 ########### 1  ########

# my_list = [
#         "str",
#         "num",
#         "lock",
#         "print",
#         "asc",
#     ]
# res = [
#
# ]
#
#
# def list_sort(list_1, result):
#
#     for el in list_1:
#         if el in list_1[::2]:
#             result.append(el[::-1]), "".join(result)
#         elif el in list_1[::1]:
#             result.append(el), "".join(result)
#     return result
#
#
# print(list_sort(my_list, res))

########### 2  ########


# my_list = [
#     "Abccc",
#     "abccc",
#     "bcaaa",
#     "cdaaa",
#     "aaaacd",
# ]
#
#
# def str_w_a(list_1):
#     result = []
#     for el in list_1:
#         if el.startswith("a"):
#             result.append(el)
#     return result
#
#
# print(str_w_a(my_list))

########### 3  ########


# my_list = [
#     "bccc",
#     "abccc",
#     "bc",
#     "cdaaa",
#     "aaaacd",
# ]
#
#
# def have_a(list_1):
#     result = [
#
#     ]
#     for el in my_list:
#         if el.count("a"):
#             result.append(el)
#     return result
#
#
# print(have_a(my_list))

########### 4  ########


# my_list = [1,
#            2,
#            3,
#            "11",
#            "22",
#            33,
# ]
#
#
# def str_type(list_1):
#     result = []
#     for el in list_1:
#         if type(el) == str:
#             result.append(el)
#     return result
#
#
# print(str_type(my_list))

########### 5  ########


# my_str = "Kkakgflalsf"
#
#
# def unique_el(list_1):
#     my_res = []
#     for el in set(list_1.lower()):
#         if list_1.count(el) == 1:
#             my_res.append(el)
#     return my_res
#
#
# print(unique_el(my_str))

########### 6  ########

# my_str_1 = "Hello world!"
# my_str_2 = "We won this game"
#
#
# def have_el(list_1, list_2):
#     result = []
#     for el in list_1:
#         if el in list_2:
#             result.append(el)
#     return result
#
#
# print(have_el(my_str_1, my_str_2))

########### 7  ########

# my_str_1 = "aaaasdf1"
# my_str_2 = "asdfff2"
#
#
# def unique_2el(list_1, list_2):
#     result = []
#     set_1 = set(list_1)
#     set_2 = set(list_2)
#     unique = set_1.intersection(set_2)
#     for el in unique:
#         if my_str_1.count(el) == 1 and my_str_2.count(el) == 1:
#             result.append(el)
#     return result
#
#
# print(unique_2el(my_str_1, my_str_2))

########### 8  ########

# domain = ["net", "com", "ua"]
# name = ["Artur", "Drew", "Boss"]
#
#
# def create_email(domains, names):
#     i = randint(0, len(names))
#     i_dom = randint(0, len(domains))
#     letters = ascii_lowercase
#     ran_str = "".join(random.choice(letters) for i in range(7))
#
#     return names[i] + str(randint(100, 999)) + "@" + ran_str + "." + domains[i_dom]
#
#
# print(create_email(domain, name))
