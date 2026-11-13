dup_list = [2, 5, 7, 3, 2, 5, 4]
new_list = []

for num in dup_list:
    if num in new_list:
        continue
    new_list.append(num)
print(new_list)

user_input = input("Enter sentence: ")
word_counts = {}

for word in user_input.lower().split():
    word_counts[word] = word_counts.get(word, 0) + 1

if word_counts:
    most_frequent_word = max(word_counts, key=word_counts.get)
    print("Word counts:", word_counts)
    print("Most frequent word:", most_frequent_word)
else:
    print("No words entered.")

students = [{"name": "Ravi", "marks": 72}, 
            {"name": "Asha", "marks": 91}, 
            {"name": "Kiran", "marks": 55}]
class_average = sum(student["marks"] for student in students) / len(students)
above_average = [
    student["name"] for student in students
    if student["marks"] > class_average
]
print(above_average)

words = ["apple", "ant", "bat"]
words_by_letter = {}
for word in words:
    first_letter = word[0].lower()
    words_by_letter.setdefault(first_letter, []).append(word)
print(words_by_letter)

odd_list = [num*num for num in range(1, 21) if num % 2 !=0]
print(odd_list)

marks = {"ravi": {"math": 80, "sci": 70}, "asha": {"math": 95, "sci": 88}}
for student, subjects in marks.items():
    total = sum(subjects.values())
    print(student, total)


