########################### 1  #############

# nums = 100
#
# find_zero = "0"
#
# num_str = str(nums)
# res = num_str.count(find_zero)
#
# print(res)


# ############ 2 ##########

# num = 1005000
# find_s = "0"
#
# result = 0
# num_str = str(num)[::-1]
#
# for i in num_str:
#     if i == find_s:
#         result += 1
#     else:
#         break
#
# print(result)


################ 3 ############

# my_list1 = [
#     2,
#     32,
#     5,
#     87,
#     561,
#
# ]
# my_list2 = [
#     123,
#     12,
#     995,
#     558,
#     265,
#     512,
# ]
#
# my_result = []
# my_result += list(my_list1[1::2])
# my_result += list(my_list2[1::2])
#
# print(my_result)

########### 4 ###########

# my_list = [1,
#            2,
#            3,
#            4,
# ]
#
# new_list = []
#
# popp = my_list.pop(0)
# new_list += my_list
# new_list.append(popp)
#
# print(new_list)

############### 5 ##############


# my_list = [1,
#            2,
#            3,
#            4,
# ]
#
#
# poppp = my_list.pop(0)
# my_list.append(poppp)
# print(my_list)

############ 6 ###########


# my_str = "43 більше ніж 34, але менше ніж 56"
#
# result = []
#
# for word in my_str:
#     if word.isalpha():
#         my_str.replace(word, "").split(" ")
#
# for word in my_str.split():
#     if word.isdigit():
#         result.append(int(word))
#
#
# print(sum(result))


############ 7 ###########

#
# my_list = [2,
#            4,
#            1,
#            5,
#            3,
#            9,
#            0,
#            7,
#            ]
#
# count = 0
#
# for i in range(1, len(my_list)-1):
#     if my_list[i] > my_list[i - 1] + my_list[i + 1]:
#         count += 1
#
# print(count)


########### 8 ##########


# my_list = [1,
#            2,
#            3,
#            "11",
#            "22",
#            33,
# ]
#
# new_list = []
#
# for el in my_list:
#     if type(el) is str:
#         new_list.append(el)
# print(new_list)


############# 9 ##############


# my_str = "Kkakgflalsf"
# my_res = []
#
# for el in set(my_str.lower()):
#     if my_str.count(el) == 1:
#         my_res.append(el)
#
# print(my_res)

########### 10 #############


# my_str_1 = "Hello world!"
# my_str_2 = "We won this game"
# result = []
#
# for el in my_str_1:
#     if el in my_str_2:
#         result.append(el)
#
# print(result)

############ 11 ###########

my_str_1 = "aaaasdf1"

my_str_2 = "asdfff2"

result = []

set_1 = set(my_str_1)
set_2 = set(my_str_2)

unique = set_1.intersection(set_2)

for el in unique:
    if my_str_1.count(el) == 1 and my_str_2.count(el) == 1:
        result.append(el)


print(result)

