import os

directory = "Homeworks"


def return_names(file=directory):
    file_names = [
    ]
    dir_names = [
    ]
    res_dict = {
    }
    file = os.listdir()
    res_dict["filenames"] = file_names
    res_dict["dirnames"] = dir_names

    for el in file:
        if os.path.isfile(el):
            file_names.append(el)
        elif os.path.isdir(el):
            dir_names.append(el)

    return res_dict


def is_alphabetic(name, is_alpa=True):
    sorted(name.values(), reverse=is_alpa)
    return name


is_alphabetic(return_names())

name_1 = "test.py"
name = "test_3"


def file_or_dir(dicts, aded_file):
    if aded_file.find(".") != -1:
        dicts["filenames"] += aded_file,
    elif aded_file.find(".") == -1:
        dicts["dirnames"] += aded_file, "".join(aded_file)

    return dicts


print(file_or_dir(return_names(), aded_file=name_1))
print(file_or_dir(return_names(), aded_file=name))


