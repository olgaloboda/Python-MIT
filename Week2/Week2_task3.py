# Write a program that uses these bounds and bisection search (for more info check out the Wikipedia page on bisection search) to find the smallest monthly payment to the cent (no more multiples of $10) such that we can pay off the debt within a year. Try it out with large inputs, and notice how fast it is (try the same large inputs in your solution to Problem 2 to compare!). Produce the same return value as you did in Problem 2.

monthlyInterestRate = annualInterestRate / 12.0
lower = round(balance / 12, 2)
upper = round(balance * (1 + monthlyInterestRate)**12 / 12.0, 2)
old = balance
while True: 
    balance = old
    year = 12
    minFixedMonthlyPayment = round((lower + upper) / 2, 2)
    while year >= 1:
        monthlyUnpaidBalance = balance - minFixedMonthlyPayment
        balance = monthlyUnpaidBalance + monthlyInterestRate * monthlyUnpaidBalance
        year -= 1
    if balance > 0:
        lower = minFixedMonthlyPayment 
    elif balance < -0.2:
        upper = minFixedMonthlyPayment
    else:
        break
print("Lowest Payment: {}".format(round(minFixedMonthlyPayment,2)))