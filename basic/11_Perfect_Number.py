num = int(input("Enter a number: "))
sum_ = 0
for i in range(1, num):
    if num % i == 0:
        sum_ += i
if sum_ == num:
    print("Perfect number")
else:
    print("Not a perfect number")
