# # Print every item in the format apple -> 40, using .items().
# fruits_dict = {"apple": 40, "mango": 40, "banana": 20, "grapes": 10}
# for key, value in fruits_dict.items():
#     print(f"{key} -> {value}")

# # Given {"x": 10, "y": 30, "z": 20}, print the sum of the values and the key with the smallest value.
# values_dict = {"x": 10, "y": 3, "z": 20}
# print(sum(values_dict.values()))
# print(min(values_dict, key=values_dict.get))

# # Swap keys and values: {"a": 1, "b": 2} becomes {1: "a", 2: "b"}.
# swap_dict = {v: k for k,v in {"a": 1, "b": 2}.items()}
# print(swap_dict)

# # Build a new dict that keeps only items whose value is 50 or more. Why is it a bad idea to delete
# value_dict = {"x": 22, "a": 44, "b": 55, "c": 21, "d": 56}
# new_dict = {}
# for key, value in value_dict.items():
#     if value >= 50:
#         new_dict[key] = value
# print(new_dict)
# for key, value in value_dict.items():
#     if value < 50:
#         value_dict.pop(key)
# print(value_dict)
# # Deleting changes the dictionary’s size during iteration, which can raise a RuntimeError

# # Sort a dict of name: score by score, highest first, and print the top 3.
# score_dict = {"a": 90, "b": 55, "c": 99, "d": 79, "e":88}
# highest_score_dict = sorted(score_dict.items(), key = lambda kv: kv[1], reverse=True)[:3]
# print(highest_score_dict)


