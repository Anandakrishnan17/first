basic_salary=int(input("Enter the basic salary:"))
night_shifts=int(input("Enter the number of night shifts"))
if basic_salary < 10000:
    hra = 0.03 * basic_salary
    da = 0.05 * basic_salary
    pf = 0.07 * basic_salary
    allowance = 500
elif 10000 <= basic_salary <= 20000:
    hra = 0.04 * basic_salary
    da = 0.06 * basic_salary
    pf = 0.08 * basic_salary
    allowance = 700
elif 20000 <= basic_salary <= 30000:
    hra = 0.05 * basic_salary
    da = 0.07 * basic_salary
    pf = 0.09 * basic_salary
    allowance = 900
else:
    hra = 0.07 * basic_salary
    da = 0.08 * basic_salary
    pf = 0.1 * basic_salary
    allowance = 1100
    
gross_salary = basic_salary + hra + da
net_salary = gross_salary - pf + (night_shifts * allowance)
print("Net salary:",net_salary)