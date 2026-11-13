food_items = ["biryani", "dosa", "fish"]
print(food_items[0])

number_list = [2, 5, 7, 9]
number_list[1] = 10
print(number_list)

names_list = ["vishnu", "fazil"]
names_list.append("Hari")
print(names_list)

colors_list = ["Black", "Red", "Green", "Yellow"]
has_blue = "Blue" in colors_list
print(has_blue)

labels = ["Name", "Address", "Role"]
has_role = "Role" in labels
if has_role:
    labels.remove("Role")
    print(labels, len(labels))
else:
    print(labels, len(labels))
    