#Antonio Nace
#CIS261
#Course Project

def employee_name():
    return input("Enter the Employee's Name: ")

def hour_amt():
    return float(input("Enter the amount of Hours worked: "))

def hourly_rate():
    return float(input("Enter the Empoloyee's Hourly Rate: "))

def income_tax_rate():
    return float(input("Enter the Income Tax Rate of the Employee (8% = 8): "))

def payroll(hours, hrate, trate):
    gross_pay = hours * hrate
    income_tax = (trate/100) * gross_pay
    net_pay = gross_pay - income_tax
    return gross_pay, income_tax, net_pay
    
def individual_payroll(emp, hours, hrate, trate, gross_pay, income_tax, net_pay):
    print("\nEmployee Name: ", emp)
    print("Total Hours Worked: ", hours)
    print("Hourly Rate: ", hrate)
    print("Gross Pay: ", gross_pay)
    print("Income Tax Rate: ", trate, "%")
    print("Income Tax: ", income_tax)
    print("Net Pay: ", net_pay)

def total_payroll(total_emp, total_hours, total_gp, total_tax, total_np):
   print("\nTotal Summary:")
   print("Total Employees: ", total_emp) 
   print("Total Hours Worked: ", total_hours)
   print("Total Gross Pay: ", total_gp)
   print("Total Tax: ", total_tax)
   print("Total Net Pay: ", total_np)

def main():
    employees = []
    total_emp = 0
    total_hours = 0
    total_gp = 0
    total_tax = 0
    total_np = 0

    while True:
        emp = employee_name()
        if emp.lower() == "end":
            break
    
        hours = hour_amt()
        hrate = hourly_rate()
        trate = income_tax_rate()
       
        gross_pay, income_tax, net_pay = payroll(hours, hrate, trate)
        
        employees.append((emp, hours, hrate, gross_pay, trate, income_tax, net_pay))
        
        total_emp += 1
        total_hours += total_hours
        gross_pay += gross_pay
        total_tax += income_tax
        net_pay += net_pay
        
    for emp, hours, hrate, gross_pay, trate, income_tax, net_pay in employees:
        individual_payroll(emp, hours, hrate, trate, gross_pay, income_tax, net_pay)
        
    total_payroll(total_emp, total_hours, total_gp, total_tax, total_np)

if __name__ == "__main__":
    main()