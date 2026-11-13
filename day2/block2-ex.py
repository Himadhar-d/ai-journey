# num = int(input("Enter number between 1 to 30: "))
# if num % 3 == 0 and num % 5 == 0:
#     print("FizzBuzz")
# elif num % 3 == 0:
#     print("Fizz")
# elif num % 5 == 0:
#     print("Buzz")

# num = 0
# while True:
#     user_input = int(input("Enter number: "))
#     if user_input == 7:
#         print(f"You have attempted {num} times")
#         break
#     num += 1

# num = int(input("Enter number: "))
# for i in range(1, 11):
#     tables = num * i
#     print(num, "*", i, "=", tables)

# Number triangle exercise:
# n = int(input("Enter height: "))
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(j, end="")
#     print()

number = int(input("Enter an integer: "))
digit_sum = 0

while number > 0:
    digit_sum += number % 10
    number //= 10

print("Sum of digits:", digit_sum)