lst = list(map(int, input("Enter list elements separated by space: ").split()))
print("Even numbers:", [num for num in lst if num % 2 == 0])


lst = list(map(int, input("Enter list elements separated by space: ").split()))
print("Odd numbers:", [num for num in lst if num % 2 != 0])
