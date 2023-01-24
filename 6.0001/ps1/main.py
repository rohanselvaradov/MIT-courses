annual_salary_base = float(input("What is your annual salary? "))

portion_down_payment = 0.25
r = 0.04
current_savings = 0
savings_rate = 0.5
semi_annual_raise = 0.07
total_cost = 1000000
epsilon = 100
num_guesses = 1
low = 0
high = 10000


down_payment = portion_down_payment * total_cost

while abs(current_savings - down_payment) > epsilon:
	months = 0
	current_savings = 0
	annual_salary = annual_salary_base
	portion_saved = savings_rate * 10000
	while months <= 36:
		current_savings += annual_salary * savings_rate / 12 
		current_savings += current_savings * r / 12
		if months % 6 == 0 and months != 0:
			annual_salary += annual_salary * semi_annual_raise
		months += 1
	if abs(current_savings - down_payment) > epsilon:
		if current_savings - down_payment < 0:
			low = savings_rate
			savings_rate = (savings_rate + high) / 2
		else:
			high = savings_rate
			savings_rate = (savings_rate + low) / 2
		num_guesses += 1
		if low >= high or savings_rate > 1:
			possible = False
			break
	else:
		print("Best savings rate: ", round(savings_rate, 4))
		num_guesses += 1
		print("Bisection steps: ", num_guesses)
		possible = True

	
if not possible:
	print("Sorry")