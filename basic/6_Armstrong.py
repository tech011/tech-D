def is_armstrong(n):
    return n == sum(int(digit) ** len(str(n)) for digit in str(n))
num = int(input("Enter a number: "))
print("Is Armstrong Number:", is_armstrong(num))
