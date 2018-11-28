# Write a program to calculate the credit card balance after one year if a person only pays the minimum monthly payment required by the credit card company each month.

year = 12
while year >= 1:
    monthlyInterestRate = annualInterestRate / 12.0
    minMonthlyPaymentRate = monthlyPaymentRate * balance
    monthlyUnpaidBalance = balance - minMonthlyPaymentRate
    balance = monthlyUnpaidBalance + monthlyInterestRate * monthlyUnpaidBalance
    year -= 1
print("Remaining balance: {}".format(round(balance, 2)))