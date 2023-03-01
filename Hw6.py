##############  1 #############
my_list = [
    1,
    4,
    82,
    901,
    9493,
    72,
    91,
    9211,
]
for i in list(my_list):
    if int(i) > 100:
        print(i)

##############  2 ################

my_list1 = [
    120,
    7390,
    8267,
    7164,
    661,
    61,
    93,
    1677,
]
my_results = [

]
for j in list(my_list1):
    if j > 100:
        my_results.append(j)
print(my_results)


########## 3 ########


my_list2 = [
    92,
    99,
    1,
]

for k in list(my_list2):
    if len(my_list2) > 2:
        my_list2.append(0)
        print(my_list2)
    else:
        my_list2.append(my_list2[-1] + my_list2[-2])
        print(my_list2)
