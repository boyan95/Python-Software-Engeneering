my_dict = {"orange": "портокал", "apple": "ябълка"}

sorted_dict = dict(sorted(my_dict.items(), key=lambda x: x[1]))
print(sorted_dict)
