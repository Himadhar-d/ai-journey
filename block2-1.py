temperature = int(input("Enter temperature: "))

if temperature > 25:
    print("Warm")


integer = int(input("Enter integer: "))

if integer > 0:
    print("Positive")
else:
    print("Not positive")

score = int(input("Enter score: "))

if score >= 50:
    print("Pass")
else:
    print("Try again")

score = int(input("Enter score: "))

if score >=80:
    print("High")
elif score >= 50 and score < 80:
    print("Medium")
else:
    print("Low")

score = int(input("Enter score: "))
is_training_completed = input("Is training completed (true/false): ").strip().lower()
done = is_training_completed == "true"

if score >= 80 and done:
    print("Ready")
else:
    print("Not ready")
 