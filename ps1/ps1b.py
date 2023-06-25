def monthly_values(annual_salary, portion_saved):
    monthly_salary = annual_salary / 12
    monthly_saved = monthly_salary * portion_saved
    return (monthly_salary, monthly_saved)

portion_down_payment = 0.25
current_savings = 0.0

annual_salary = input('Enter your annual salary: ')
portion_saved = input('Enter the percent of your salary to save, as a decimal: ')
total_cost = input('Enter the cost of your dream home: ')
sa_raise = input('Enter the semi annual raise, as a decimal: ')

annual_salary = float(annual_salary)
portion_saved = float(portion_saved)
total_cost = float(total_cost)
sa_raise = float(sa_raise)

down_payment = total_cost * portion_down_payment
monthly_salary, monthly_saved = monthly_values(annual_salary, portion_saved)
months = 0

while (current_savings <= down_payment):
    interest_earned = (current_savings * 0.04) / 12 # 4% is annual rate
    current_savings += interest_earned
    current_savings += monthly_saved

    if ((months + 1) % 6 == 0):
        annual_salary += annual_salary * sa_raise
        monthly_salary, monthly_saved = monthly_values(annual_salary, portion_saved)

    months += 1

print('Number of months: ', months)
