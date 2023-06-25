def monthly_values(annual_salary, portion_saved):
    monthly_salary = annual_salary / 12
    monthly_saved = monthly_salary * portion_saved
    return (monthly_salary, monthly_saved)

def get_savings(annual_salary, portion_saved, sa_raise):
    rate = portion_saved / 10000
    salary = annual_salary
    monthly_salary, monthly_saved = monthly_values(annual_salary, rate)
    savings = 0

    for month in range(1, 37):
        interest_earned = (savings * .04) / 12 # 4% is annual rate
        savings += interest_earned
        savings += monthly_saved

        if (month % 6 == 0):
            salary += salary * sa_raise
            monthly_salary, monthly_saved = monthly_values(salary, rate)

    return savings


# # annual_salary = float(input('Enter your annual salary: '))
annual_salary = float(150000)

tolerated_variance = 100
total_cost = 1000000
portion_down_payment = 0.25
down_payment = total_cost * portion_down_payment
sa_raise = .07
current_savings = 0

high = 10000
low = 0
guess = (high + low) / 2
steps = 0

while abs(down_payment - current_savings) >= tolerated_variance:
    current_savings = get_savings(annual_salary, guess, sa_raise)

    if (current_savings < down_payment):
        low = guess
    else: 
        high = guess

    guess = (high + low) / 2
    steps += 1

    # Most guesses can be log base 2 0f 10000, which is 13
    if steps > 13: 
        continue


print(steps)
print(guess / 100)


