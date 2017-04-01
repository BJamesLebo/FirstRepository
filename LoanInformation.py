#This program calculates and returns the monthly payments for a loan
def calculate_payment (principal,annual_interest_rate,duration):
    if annual_interest_rate==0:
        return principal/(duration*12)
    r = (annual_interest_rate/100)/12 #monthly interest rate
    n = duration*12 #no. of monthly payments during loan
    monthly_payment = principal * ((r*(1+r)**n) / ((1+r)**n-1))
    return monthly_payment

#Calculate the remaining balance of a loan
def calculate_balance (principal,annual_interest_rate,
                       duration,number_of_payments):
    if annual_interest_rate==0:
        return principal*(1-(principal/(duration*12)))
    r = annual_interest_rate/100/12
    n = duration*12
    p = number_of_payments
    remaining_balance = principal * ((((1+r)**n)-(1+r)**p)/((1+r)**n - 1))
    return remaining_balance

#Program Episode III: Revenge of the Python
def get_loan_details ():
    principle=float(input("Enter loan amount: "))
    annual_interest_rate=float(input("Enter annual interest rate (percent): "))
    duration=int(input("Enter loan duration in years: "))    
    monthly_payment=calculate_payment(principle, annual_interest_rate, duration)
    print('LOAN AMOUNT:',principle,'INTEREST RATE (PERCENT):', annual_interest_rate)
    print('DURATION (YEARS):',duration,'MONTHLY PAYMENT:',int(monthly_payment))
    for year_number in range(1,1+duration):
        y=calculate_balance(principle, annual_interest_rate, duration, year_number*12)
        print('YEAR:', year_number, 'BALANCE:', int(y), 'TOTAL PAYMENT', int(monthly_payment*year_number*12))

#So, call get_loan_details() in the Python Shell to run the bottom program
        
