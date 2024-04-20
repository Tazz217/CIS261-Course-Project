#Antonio Nace
#CIS261
#Course Project


#add (1% = .01 in print)


def payroll(emp, hour,hrate,trate):
    gross_pay = hour * hrate
    income_tax = trate * gross_pay
    net_pay = gross_pay - income_tax
    return gross_pay, income_tax, net_pay
    
def main():
    emp = input("Enter the Employee's Name: ")
    hour = float(input("Enter the amount of hours the Employee worked: "))
    hrate = float(input("Enter the Hourly Pay Rate for the Employee: "))
    trate = float(input("Enter the current Income Tax Rate in decimal form (8% = .08): "))

do: payroll
    while emp =! "End"