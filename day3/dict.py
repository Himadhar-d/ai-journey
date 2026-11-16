# # Make a dict for a book with title, author and year. Print each value with a label. Then add pages, change year, and delete author.
# book_dict = {"title": "Python", "author": "Himadhar", "Year": 2026}
# for key, value in book_dict.items():
#     print(f"{key}: {value}")
# book_dict["pages"] = 45
# print(book_dict)
# book_dict.pop("author")
# print(book_dict)
# book_dict["Year"] = 2028
# print(book_dict)


# Read the key "price" from a dict that might not have it. Print “not found” if it’s missing. Do it two ways: with in, and with .get().
# book_dict = {"title": "Python", "author": "Himadhar", "Year": 2026}
# if "price" in book_dict:
#     print("Found")
# else:
#     print("Not found")
# get_check = book_dict.get("price", "Not found")
# print(get_check)


# Merge {"a": 1, "b": 2} and {"b": 9, "c": 3} into one dict. What happens to "b"?
# first_dict = {"a": 1, "b": 2}
# second_dict ={"b": 9, "c": 3}
# first_dict.update(second_dict)
# print(first_dict)
# if we give  first_dict.update(second_dict) then first_dict is changed and b=9 and if we revrse the order b=2


# Predict first, then run: d = {"a": 1}, then d["b"] = d.get("b", 0) + 5, then d.pop("a"), then print(d).
# output = {"b": 5}
# d = {"a": 1}
# d["b"] = d.get("b", 0) + 5
# d.pop("a")
# print(d)


# Predict first: what does print({"a": 1, "a": 2}) show? Then try using a list as a key ({[1, 2]: "x"}). Why does it fail?
# output = {'a': 2}, keys connot be changed so using list can be changable so it will get error. 
 