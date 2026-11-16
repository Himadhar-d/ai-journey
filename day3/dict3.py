# Given a list of numbers, return {"even": [...], "odd": [...]}.
num_list = [2, 5, 6, 7, 3, 2, 10, 15, 12]
even_num = [num for num in num_list if num % 2 == 0]
odd_num = [num for num in num_list if num % 2 != 0]
new_dict = {}
new_dict["Even"] = even_num
new_dict["Odd"] = odd_num
print(new_dict)

# Given a list of words, group them by length: {3: ["cat", "dog"], 5: ["apple"]}
words_list = ["dog", "cat", "hen", "mango", "apple", "banana", "pencil", "laptops", "pig"]
new_list = {}
for word in words_list:
    new_list.setdefault(len(word), []).append(word)
print(new_list)

# Find the first character in a string that doesn’t repeat, using a dict of counts. ("swiss" gives "w".)
char = "swiss"
new_dict = {}
for letter in char:
    new_dict[letter] = new_dict.get(letter, 0) + 1
print(new_dict)
for letter in char:
    if new_dict[letter] == 1:
        print(letter)
        break


# 15. Two Sum with a dict: given nums = [2, 7, 11, 15] and target = 9, return the indexes of the two numbers that add up to the target. This is the LeetCode problem from Day 1, now with a dict.

nums = [2, 7, 11, 15]
target = 9
seen = {}
result = []
for index, number in enumerate(nums):
    needed = target - number
    if needed in seen:
        result = [seen[needed], index]
        break
    seen[number] = index
print(result)

# Count how often each character appears in a string, ignoring spaces.
string = "Hi How are you how is your learning"
simple_string = string.replace(" ", "")
new_dict = {}
for word in simple_string:
    new_dict[word] = new_dict.get(word, 0) + 1
print(new_dict)