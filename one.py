# ==========================================
#       EMPLOYEE SALARY CALCULATOR
# ==========================================

# Student Name        : Soni Sahu
# ERP ID              : RU-26-01131
# Programming Language: BCA
# Project Number      : PS No. 6
# Project Description : Employee Salary Calculator 
#
#======================================================"""


# Function to calculate gross salary
def calculate_gross(basic):
    hra = basic * 0.20
    da = basic * 0.10
    gross = basic + hra + da

    return hra, da, gross


# Function to calculate PF and Tax
def calculate_deductions(basic, gross):
    pf = basic * 0.12

    if gross <= 25000:
        tax = 0
    elif gross <= 50000:
        tax = gross * 0.05
    else:
        tax = gross * 0.10

    return pf, tax


# Function to print salary slip
def print_slip(basic):
    hra, da, gross = calculate_gross(basic)
    pf, tax = calculate_deductions(basic, gross)

    net_salary = gross - pf - tax

    print("HRA:", int(hra), "| DA:", int(da),
          "| Gross:", int(gross))

    print("PF:", int(pf), "| Tax:", int(tax),
          "| Net Salary:", int(net_salary))


# Main Program
print("===================================")
print("     EMPLOYEE SALARY CALCULATOR")
print("===================================")

# Run all four test cases
for i in range(1, 5):

    print("\n========== TEST CASE", i, "==========")

    try:
        basic = float(input("Enter Basic Salary: "))

        if basic <= 0:
            print("Invalid salary. Enter a positive number.")
        else:
            print_slip(basic)

    except ValueError:
        print("Invalid salary. Enter a positive number.")

print("\n===================================")
print("       ALL TEST CASES COMPLETED")
print("===================================")