# print("Welcome to the game!!!")
# user1=int(input("""Player one make your move:
# 1.Stone
# 2.Scissors
# 3.Paper
# """))
# user2=int(input("""Player two make your move:
# 1.Stone
# 2.Scissors
# 3.Paper
# """))
# if user1 == user2:
#     print("No Winer")
# elif user1 == 1 and user2 == 2: 
#     print("Player one Winner!!!")
# elif user1 == 1 and user2 == 3:
#     print("Player two Winner!!!")
# elif user1 == 2 and user2 == 1:
#     print("Player two Winner!!!")
# elif user1 == 2 and user2 == 3:
#     print("Player one Winer!!!")
# elif user1 == 3 and user2 == 1:
#     print("Player one Winner!!!")
# elif user1 == 3 and user2 == 2:
#     print("Player two Winner!!!")

#_______________________________________________

# a = [1,2,3,5,8,13,21,34,55,89]
# for i in a:
#     if i <= 13:
#         print(i)
#_____________________________
# нужно вернуть список,который состоит из элементов,
#общих для этих двух списков

# a = [1,2,3,5,8,13,21,34,55,89]
# b = [1,2,3,4,5,6,7,8,9,10,11,12,13]
# c = []
# for i in a:
#     if i in b:
#         c.append(i)
# print(c)

#_____________________________________

# baza = {
#     "roman":"avtomobil",
#     "ruslan":"motocikl",

# }
# baza2 = {
#     "nikolai":"avtomat",
#     "sergey":"mekhanik",
# }

# baza.update(baza2)
# print(baza)

#__________________________________

# my_dict= {
#     "a":500,
#     "b":5874,
#     "c":560,
#     "d":400,
#     "e":5874,
#     "f":20
# }
# for i in my_dict.values():
#     if i >= 560:
#         print(i)

#_____________________________
# проверка слова на полиндром
# a = input()
# if a == a [::-1]: # ::-1 читает код наоборос(сзади)
#     print(a)
# else:
#     print("error")  
