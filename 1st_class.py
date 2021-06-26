import random
#---------------------------------Homework#1-------------------------------------


# a = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
# new = []
# for x in a:
#     if x not in new:
#         new.append(x)

# print(new)


#----------------------------------Homework#2-----------------------------

# list_1=[0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
# list_2=[]
# for i in list_1:
#     if type(i)==int:
#         list_2.append(i)
#     elif type(i)!=int:
#         for j in i:
#             list_2.append(j)
# print(list_2)

dict_2 = {}
for i in range(20):
    number = random.randint(1,20)

    if number >=10:
        if "over_10" in dict_2.keys():
            dict_2["over_10"]+=1
        else:
            dict_2["over_10"] =1
    else:
        if "under_10" in dict_2.keys():
            dict_2["under_10"] +=1
        else:
            dict_2["under_10"] =1
print(dict_2)