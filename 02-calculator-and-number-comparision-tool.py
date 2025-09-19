#numbers
num1 = int(input("Enter your first number:"))
num2 = int(input("Enter your second number:"))

# --- Calculator Results ----
print("\n--- Calculator Results ----")

# Addition
print("Addition:{num1} + {num2} = {num1 + num2}")

# Subtraction
print("Subtraction:{num1} - {num2} = {num1 - num2}")

# Multiplication
print("Multiplication:{num1} x {num2} = {num1 * num2}")

# Division (with condition to avoid division by zero)
if num2 != 0:
    print("Division:{num1} / {num2} = {num1 / num2}")
else:
    print("Division: Cannot divide by zero")

# --- Comparison Results ----
print("\n--- Comparison Results ----")

if num2 > num1:
    print("{num2} is greater than {num1}")
elif num1 > num2:
    print("{num1} is greater than {num2}")
else:
    print("{num1} is equal to {num2}")

# Check non-zero
print("\nBoth numbers are non-zero.")
