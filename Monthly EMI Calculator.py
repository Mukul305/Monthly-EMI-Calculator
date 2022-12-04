
loanAmount = input("Total Amount of Loan? ")
interestRate = input("interest rate % ")
noYears = input("Number of years for loan payment ")

loanAmount = float(loanAmount)
interestRate = float(interestRate)
noYears = float(noYears)

interestRate = interestRate / 100 / 12
noYears = noYears * 12

mortgagePayment = loanAmount * (interestRate * (1+interestRate) ** noYears) / ((1+interestRate) ** noYears - 1)
print("Monthly emi is %.2f " %mortgagePayment)