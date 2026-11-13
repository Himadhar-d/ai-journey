num = 1
while num<4:
    print(num)
    num+=1

num = 5
while num > 0:
    print(num)
    num-=1

while True:
    word = "stop"
    user_input = input("Enter word: ")
    if user_input == word:
        print("Entered word is correct.")
        break

num = 1
while num <= 8:
    if num % 2 != 0:
        num += 1
        continue
    print(num)
    num += 1


total = 0
while True:
    user_input = int(input("Enter number: "))
    if user_input == 0:
        print(total)
        break
    total += user_input