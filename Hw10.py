# Всі пункти зробити як окремі функції та їх виклики.
#
# 1. Написати функцію, яка отримує як параметр ім'я файлу назви інтернет доменів (domains.txt)
# та повертає їх у вигляді списку рядків (назви повертати без крапки).
#
# 2. Написати функцію, яка отримує як параметр ім'я файла (names.txt)
# і повертає список усіх прізвищ із нього.
# Кожен рядок файлу містить номер, прізвище, країну, кілька (таблиця взята з вікіпедії).
# Розділювач - символ табуляції "t"
#
# 3. Написати функцію, яка отримує у вигляді параметра ім'я файлу (authors.txt) та повертає список
# словників виду {"date": date}
# у яких date - це дата з рядка (якщо є),
# Наприклад [{"date": "1st January 1919"}, {"date": "8th February 1828"}, ...]
#
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#
# 4* (*здавати не обов'язково).
# Написати функцію, яка отримує у вигляді параметра ім'я файлу (authors.txt) та повертає список
# словників виду {"date_original": date_original, "date_modified": date_modified}
# у яких date_original - це дата з рядка (якщо є),
# а date_modified - ця ж дата, представлена у форматі "dd/mm/yyyy" (d-день, m-місяць, y-рік)
# Наприклaд [{"date_original": "8th February 1828", "date_modified": 08/02/1828}, ...]


#################################################################################################
                                  # 1 #
# domains_txt = "domains"
# testt = "test"


# def return_domaim(name = domains_txt):
#     with open(name, "r") as new_data:
#         read_upd = new_data.readlines()
#         testing_list = [
#
#         ]
#         for el in read_upd:
#             if el.startswith("."):
#                 element = el.translate({ord("."): ""})
#                 testing_list.append(element)
#     with open(testt, "w") as data:
#         write_upd = data.writelines(testing_list)
#
#     return None

################################################################
                                    # 2 #
# test_1 = "test_1"
# names_txt = "names"
# ban_str = "1234567890,"
# set_1 = set(ban_str)
#
#
# def return_names(name=names_txt):
#     with open(name, "r") as new_data:
#         read_upd = new_data.readlines()
#
#     test_list = [
#
#     ]
#     for strs in read_upd:
#         for el in strs:
#             if el in set_1:
#                 strs = strs.replace(el, "")
#         test_list.append(strs)
#     result_list = [
#
#     ]
#     for elements in test_list:
#         start_in = elements.index(elements[2])
#         cut_1 = elements.find("\t", start_in)
#         cut = elements.index(elements[1])
#         elements = elements[cut:cut_1]
#         result_list.append(elements + "\n")
#     with open(test_1, "w") as new_data:
#         write_upd = new_data.writelines(result_list)
#     return None
#
#
# return_names(names_txt)
################################################################
test_2 = "test_2"
authors_txt = "authors"
result_list = [

]


def date(name=authors_txt):
    with open(name, "r") as my_file:
        read_upd = my_file.readlines()

    for el in read_upd:
        find_1 = el.find("-")
        cut_1 = el[0: find_1]
        if find_1 != -1:
            result_list.append(f"data: {cut_1}" + "\n")
    with open(test_2, "w") as new_data:
        write_upd = new_data.writelines(result_list)
    return None


date()













