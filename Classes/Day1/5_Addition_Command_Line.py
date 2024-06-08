import sys

# Ensure there are enough command line arguments

if len(sys.argv) !=3:
    print("Usage: python addition of two numbers <num1> and <num2>")
    sys.exit(1)


# Convert command line arguments to floats

try:
    num1 = float(sys.argv[1])
    num2 = float(sys.argv[1])
except ValueError:
    print("Both arguments must be numbers.")
    sys.exit(1)

sum_result = num1 +num2

print("The sum is:", sum_result)


