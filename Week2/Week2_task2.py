minFixedMonthlyPayment = 10
old = balance
year = 12

while True: 
    while year >= 1:
        monthlyInterestRate = annualInterestRate / 12.0
        monthlyUnpaidBalance = balance - minFixedMonthlyPayment
        balance = monthlyUnpaidBalance + monthlyInterestRate * monthlyUnpaidBalance
        year -= 1
    
    if balance > 0:
        balance = old
        minFixedMonthlyPayment += 10
        year = 12
    else: 
        break
    
print("Lowest Payment: {}".format(round(minFixedMonthlyPayment)))