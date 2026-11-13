num_list = [1, 2, 3]
plus_ten_list = [num + 10 for num in num_list]
print(plus_ten_list)

num_list = [1, 2, 3, 4, 5, 6]
even_list = [num for num in num_list if num % 2 == 0]
print(even_list)

animal_list = ["cat", "dog", "bird"]
uppercase_list = [name.upper() for name in animal_list]
print(uppercase_list)

key_dict = {2, 3, 4}
value_dict = {num: num*num for num in key_dict}
print(value_dict)

name_list = ["Ravi", "Meera"]
value_dict = {name: "student" for name in name_list}
print(value_dict)