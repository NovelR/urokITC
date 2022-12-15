# set , dictionary
#_______________________________
# megi = {
#     "name": "Ablay",
#     "age": 42
# }

# print (megi['name'],megi["age"])

# print(megi.keys())

# print(megi.items())

# print(megi.values())

# megi.pop("name")
# print("megi")

# megi.popitem()
# print(megi)

# t = {
#     "last_name":"naz"

# }
# megi.update(t)
# print(megi)

# megi.fromkeys()

# m = {"x":4,"y":5}
# m.setdefault("z",123)
# print(m)

# a = {"x":4,"y":5}
# b = a.copy()
# b[2] = 123
# print(a)
# print(b)

# b = frozenset([1,2,3,4,4])
# print(b)

#___________

# a = {"name",123, 321, "name", True, False, False, False}
# b = {"name",123, 321, "asd", "asds", 23.342}
# c = {"1", "13"}

# print(c.isdisjoint(a))
# print(b.isdisjoint(a))

# print(a.union(b))
# print(a | b)

# print(a.intersection(b))
# print(a & b)

# print(a.difference(b))
# print(a - b)
# print(b - a)

# print(a.symmetric_difference(b))

# a.add(98765)
# print(a)

# a.discard(123)
# print(a)

# a = {0,1,2,3,4,5,6,7,8,9,10,11,12}
# a.discard(7)
# print(a)

# a = {1,2, "True" ,0,1,2}
# b = {1,2, "False" ,0,1,2}
# print(a.intersection(b))

# print(a.difference(b))
# print(b.difference(a))

#problem 3
#__________

# a = {1,2,3,4,5,6,7}
# a.add(8)
# print(a)
# g  = a.pop()
# print(g)
# print(a)

# menu = {
#     "besh":1234,
#     "lagman":798
# }
# menu["lagman"]=321
# print(menu)
# menu['borsh'] = 654
# print(menu)
# menu.pop('borsh')
# print(menu)


# menu["napitki"] = ["kola", "fanta", "sprite"]
# print(menu)


#________matody
# a ={

#     "add","update", 
#     "intersection", "remove",
#     "difference", "intersection_update", 
#     "clear", "discard", "pop" 
# }
# d = {'update'}
# a.difference(d)
# print(a.difference(d))
# print(d.difference(a))


# name = input()
# pasword = input()
# s = {
#     "name1":name,
#     "pass":pasword,
# }
# print(s)








