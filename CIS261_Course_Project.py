def GetEmpName():
    # Prompt user to enter the employee's name
    empname = input("Enter employee name: ")
    return empname

def GetDatesWorked():
    # Prompt user to enter the start and end dates of work
    fromdate = input("Enter Start Date (mm/dd/yyyy): ")
    todate = input("Enter End Date (mm/dd/yyyy): ")
    return fromdate, todate

def GetHoursWorked():
    # Prompt user to enter the number of hours worked, convert to float
    hours = float(input('Enter amount of hours worked: '))
    return hours

def GetHourlyRate():
    # Prompt user to enter the hourly rate, convert to float
    hourlyrate = float(input("Enter hourly rate: "))
    return hourlyrate

def GetTaxRate():
    # Prompt user to enter the tax rate, convert to float
    taxrate = float(input("Enter tax rate: "))
    return taxrate

def CalcTaxAndNetPay(hours, hourlyrate, taxrate):
    # Calculate gross pay, income tax, and net pay
    grosspay = hours * hourlyrate
    incometax = grosspay * taxrate
    netpay = grosspay - incometax
    return grosspay, incometax, netpay

def printinfo(EmpDetailList):
    # Initialize total values
    TotEmployees = 0
    TotHours = 0.00
    TotGrossPay = 0.00
    TotTax = 0.00
    TotNetPay = 0.00

    # Iterate through each employee's details
    for EmpList in EmpDetailList:
        empname  = EmpList[0]
        fromdate  = EmpList[1]
        todate = EmpList[2]
        hours = EmpList[3]
        hourlyrate = EmpList[4]
        taxrate = EmpList[5]

        # Calculate pay details for the employee
        grosspay, incometax, netpay = CalcTaxAndNetPay(hours, hourlyrate, taxrate)
        # Print the employee's work and pay details
        print(fromdate, todate, empname, f"{hours:,.2f}", f"{hourlyrate:,.2f}", f"{grosspay:,.2f}", f"{taxrate:,.1%}", f"{incometax:,.2f}", f"{netpay:,.2f}")

        # Update total values
        TotEmployees = 5
        TotHours += hours
        TotGrossPay += grosspay
        TotTax += incometax
        TotNetPay += netpay

    # Create a dictionary with total values
    EmpTotals = {
        'TotEmp' : TotEmployees,
        'TotHrs' : TotHours,
        'TotGrossPay' : TotGrossPay,
        'TotTax' : TotTax,
        'TotNetPay' : TotNetPay,
    }

    return EmpTotals  # Return the dictionary of total values

def PrintTotals(EmpTotals):
    # Print total values in a formatted manner
    print()
    print(f"Total Number of Employees: {EmpTotals['TotEmp']}")
    print(f"Total Hours Worked: {EmpTotals['TotHrs']}")
    print(f"Total Gross Pay: {EmpTotals['TotGrossPay']:,.2f}")
    print(f"Total Income Tax: {EmpTotals['TotTax']:,.2f}")
    print(f"Total Net Pay: {EmpTotals['TotNetPay']:,.2f}")

def WriteEmployeeInformation(employee):
    # Open file in append mode and write employee details
    file = open("employeeinfo.txt", "a")
    file.write('{}|{}|{}|{}|{}|{}\n'.format(employee[0], employee[1], employee[2], employee[3], employee[4], employee[5]))
    file.close()  # Close the file after writing

def GetFromDate():
    valid = False
    fromdate = ""

    while not valid:
        # Prompt user to enter a start date or 'ALL'
        fromdate = input("Enter From Date (mm/dd/yyyy): ")
        if (len(fromdate.split('/')) != 3 and fromdate.upper() !='ALL'):
            print("Invalid Date Format: ")
        else:
            valid = True

    return fromdate

def ReadEmployeeInformation(fromdate):
    EmpDetailList = []

    # Open file in read mode
    file = open("employeeinfo.txt", "r")
    data = file.readlines()
    file.close()  # Close the file after reading

    condition = True
    if fromdate.upper() == 'ALL':
        condition = False

    # Iterate through each line in the file
    for employee in data:
        employee = [x.strip() for x in employee.strip().split("|")]
        if not condition:
            EmpDetailList.append([employee[0], employee[1], employee[2], float(employee[3]), float(employee[4]), float(employee[5])])
        else:
            if fromdate == employee[0]:
                EmpDetailList.append([employee[0], employee[1], employee[2], float(employee[3]), float(employee[4]), float(employee[5])])
    
    return EmpDetailList  # Return the list of employee details

if __name__ == "__main__":
    EmpDetailList = []
    EmpTotals = {}

    # Continuously get employee information until 'END' is entered
    while True:
        empname = GetEmpName()
        if (empname.upper() == "END"):
            break

        fromdate, todate = GetDatesWorked()
        hours = GetHoursWorked()
        hourlyrate = GetHourlyRate()
        taxrate = GetTaxRate()

        print()
           
        EmpDetail = [fromdate, todate, empname, hours, hourlyrate, taxrate]
        WriteEmployeeInformation(EmpDetail)  # Write employee details to file

    print()
    print()
    
    fromdate = GetFromDate()  # Get the start date for reading information
    
    EmpDetailList = ReadEmployeeInformation(fromdate)  # Read employee details from file
    
    print()
    EmpTotals = printinfo(EmpDetailList)  # Print employee details and calculate totals
    print()
    PrintTotals(EmpTotals)  # Print total values
