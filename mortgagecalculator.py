
#For the system clear command
import os

#Mortgage Payments Calculator Function
def mortgage_payments(principal, rate, amortization):

    #Calculates every periodic interest rate
    #Converts user input for rate into decimal from percentage
    r_monthly = (1 + (rate / 100) / 2) ** (2/12) - 1 
    r_semi_monthly = (1 + (rate / 100) / 2) ** (2/24) - 1
    r_bi_weekly = (1 + (rate / 100) / 2) ** (2/26) - 1
    r_weekly = (1 + (rate / 100) / 2) ** (2/52) - 1
    
    #Calculates number of payments
    n_monthly = amortization * 12
    n_semi_monthly = amortization * 24
    n_bi_weekly = amortization * 26
    n_weekly = amortization * 52
    
    #Calculates present value of annuity factors
    def pva(r, n):
        return (1 - (1 + r) ** -n) / r
    
    #Calculate payments and round to 2 decimals
    monthly = round((principal / pva(r_monthly, n_monthly)),2)
    semi_monthly = round((principal / pva(r_semi_monthly, n_semi_monthly)),2)
    bi_weekly = round((principal / pva(r_bi_weekly, n_bi_weekly)),2)
    weekly = round((principal / pva(r_weekly, n_weekly)),2)
    rapid_bi_weekly = round((monthly / 2),2)
    rapid_weekly = round((monthly / 4),2)

    return(monthly, semi_monthly, bi_weekly, weekly, rapid_bi_weekly, rapid_weekly)

#User Inputs and converts to proper variable type
principal = float(input("Enter The Principal Amount: "))
rate = float(input("Enter The Interest Rate: "))
amortization = int(input("Enter The Amortization Period In Years: "))

#Clears user input values for cleaner design
os.system('cls')

#Calculate payments using mortgage_payments function
payment = mortgage_payments(principal, rate, amortization)

#Displays formatted outputs
print(f"Monthly Payment: ${payment[0]}")
print(f"Semi-monthly Payment: ${payment[1]}")
print(f"Bi-weekly Payment: ${payment[2]}")
print(f"Weekly Payment: ${payment[3]}")
print(f"Rapid Bi-weekly Payment: ${payment[4]}")
print(f"Rapid Weekly Payment: ${payment[5]}")
