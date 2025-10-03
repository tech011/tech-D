def interest(p, r, t):
    return (p * r * t) / 100
principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest: "))
time = float(input("Enter time period in years: "))
print("Simple interest:", interest(principal, rate, time))
