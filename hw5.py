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


print(line[::])

###########  i #############


print(len(line))

#######################################################
                     # 2

#############################################

value_1 = "Hello world i am computer"
word_count = value_1.count(" ")
print(word_count + 1)


#################################################

                   # 3

###############################################

s = str(input("Enter your word \n"))

ch = "g"

for ch in s:
    if ch in len(s):
        print(s.find(ch))
    else:
        print("Specsymbol isn`t in your word/s ")

###############################################################

                        # 1/1


###############################################################

value_2 = "hhello world!"
for word in value_2:
    if value_2.islower():
        word = value_2.replace("h", "h")
        print(word)
    else:
        print("Error")
