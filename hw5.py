line = "Hello world"

########  a ##############


print(line[3])


######## b ################


print(line[-2])

######### c ############


print(line[:5])


############## d ##########


print(line[:9])


########### e #############


print(line[::2])

####### f ##########


print(line[::-2])


###### g #######


print(line[::-1])


############## h #############


print(line[:1:-2])


###########  i #############


for i in range(len(line)):
    print(i)


#######################################################
                     # 2

#############################################

value_1 = "Hello world i am computer"
word_count = value_1.count(" ")
print(word_count + 1)


#################################################

                   # 3

###############################################


my_str = str(input("Here:"))
ch = "g"
gg = True
count = 0
while gg:
    index = my_str.find(ch)
    my_str = my_str[index + len(ch):]
    if index == -1:
        gg = False
    else:
        count += 1
print(count)


###############################################################

                        # 1.1


###############################################################

value_2 = "hhello world!"
for word in value_2:
    if value_2.islower():
        print(value_2.replace("h", "H"))
    else:
        print("Error")
