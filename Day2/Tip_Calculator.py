print("Welcome to the tip calculator")

bill = float(input("What was the total bill? $"))
tip = float(input("What kind of tip do you want to give? The answer will be interpreted as a percentage. "))
people = int(input("How many people split the bill? "))
price_each = (bill * (1 + tip / 100) / people)

print(f"Each person should pay ${price_each:.2f}")
