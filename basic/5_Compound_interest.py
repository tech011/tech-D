def compound_interest(p, r, t):
    return p * (1 + r/100) ** t - p
principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest: "))
time = float(input("Enter time period in years: "))
print("Compound interest:", compound_interest(principal, rate, time))
