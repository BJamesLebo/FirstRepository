#This program calculates and returns the monthly payments for a loan
def calculate_payment (principle,annual_interest_rate,duration):
    if annual_interest_rate==0:
        return principle/(duration*12)
    r = (annual_interest_rate/100)/12 #monthly interest rate
    n = duration*12 #no. of monthly payments during loan
    monthly_payment = principle * ((r*(1+r)**n) / ((1+r)**n-1))
    return monthly_payment
