domains_txt = "domains"
authors_txt = "authors"
names_txt = "names"
testt = "test"
test_1 = "test_1"
test_2 = "test_2"


class FileRedactor:

    def __init__(self, name, res_list):
        self.name = name
        self.res = res_list

    def return_domaim(self):
        with open(self.name, "r") as new_data:
            read_upd = new_data.readlines()
            testing_list = [
            ]
            for el in read_upd:
                if el.startswith("."):
                    element = el.translate({ord("."): ""})
                    testing_list.append(element)
        with open(self.res, "w") as data:
            write_upd = data.writelines(testing_list)
        return None

    def return_names(self):
        with open(self.name, "r") as new_data:
            read_upd = new_data.readlines()
        test_list = [
        ]
        ban_str = "1234567890,"
        set_1 = set(ban_str)
        for strs in read_upd:
            for el in strs:
                if el in set_1:
                    strs = strs.replace(el, "")
            test_list.append(strs)
        result_list = [
        ]
        for elements in test_list:
            start_in = elements.index(elements[2])
            cut_1 = elements.find("\t", start_in)
            cut = elements.index(elements[1])
            elements = elements[cut:cut_1]
            result_list.append(elements + "\n")
        with open(self.res, "w") as new_data:
            write_upd = new_data.writelines(result_list)
        return None

    def date(self):
        with open(self.name, "r") as my_file:
            read_upd = my_file.readlines()
        result_list = [
        ]
        for el in read_upd:
            find_1 = el.find("-")
            cut_1 = el[0: find_1]
            if find_1 != -1:
                result_list.append(f"data: {cut_1}" + "\n")
        with open(self.res, "w") as new_data:
            write_upd = new_data.writelines(result_list)
        return None


test_domain = FileRedactor(domains_txt, testt)
test_domain.return_domaim()

test_names = FileRedactor(names_txt, test_1)
test_names.return_names()

test_data = FileRedactor(authors_txt, test_2)
test_data.date()
