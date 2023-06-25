portion_down_payment = 0.25
current_savings = 0.0

annual_salary = input('Enter your annual salary: ')
portion_saved = input('Enter the percent of your salary to save, as a decimal: ')
total_cost = input('Enter the cost of your dream home: ')

annual_salary = float(annual_salary)
portion_saved = float(portion_saved)
total_cost = float(total_cost)

down_payment = total_cost * portion_down_payment
monthly_salary = annual_salary / 12
monthly_saved = monthly_salary * portion_saved
months = 0

while (current_savings <= down_payment):
    interest_earned = (current_savings * 0.04) / 12 # 4% is annual rate
    current_savings += interest_earned
    current_savings += monthly_saved
    months += 1

print('Number of months: ', months)





