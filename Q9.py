P = float(input("Enter the principal amount: "))
R = float(input("Enter the rate of interest:"))
T = int(input("Enter the time in years:"))
A = P * (1 + R / 100) ** T
CI = A - P
print(f"Compound Interest: {CI}")
