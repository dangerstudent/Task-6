my_dict = {"Олег" : 1995, "Влад" : 1996, "Дима" : 1994}
print(my_dict)
print(my_dict["Дима"])
print(my_dict.get("Ольга"))
my_dict.update({"Ваня" : 1993,
                "Катя" : 1992})
print(my_dict["Олег"])
del my_dict["Олег"]
print(my_dict)

my_set = {1, 2, 3, 1, 2, 3, "grusha", "grusha", 20.5, 20.5}
print(my_set)
my_set.update({"robot",
              869})
my_set.remove(20.5)
print(my_set)