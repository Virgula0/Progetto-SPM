total_investment = 17_500_000
inital_investment = 5_000_000

COUNT = 7 # number of semesters

coming_investment = (total_investment - inital_investment) / COUNT
print(f"COMING INVESTMENT {coming_investment}")

fixed_salary_per_year = 2_894_000 # per year
semestral_fixed_salary = fixed_salary_per_year / 2
print(f"SEMESTRAL SALARY {semestral_fixed_salary}")

values = []

def recursive(a , steps, count):
    if steps == count:
        return a
    
    steps = steps + 1
    outgoing_investment = (a  + coming_investment)-semestral_fixed_salary # cumulative remainings
    values.append(outgoing_investment)
    
    return recursive(outgoing_investment, steps=steps, count=count)

steps = 0
count = 7

print(f"BUDGET: {total_investment}")

init_comulative_remaining = inital_investment - semestral_fixed_salary
values.append(init_comulative_remaining)
recursive(init_comulative_remaining, steps=0, count=COUNT)

print("-"*10+ " CUMULATIVE REMAININGS "+"-"*10)
print(values)
print("-"*43)

summed_salary = semestral_fixed_salary*(COUNT+1)
annual_profit = (total_investment-summed_salary)/4
roi = (annual_profit/summed_salary)*100

print(f"SUMMED SALARY {summed_salary}")
print(f"Annual profit: {annual_profit}")
print(f"ROI: {roi}%")