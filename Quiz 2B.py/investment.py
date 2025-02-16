input_initial_investment=int(input('Enter initial amount: '))
input_years=int(input('Enter number of years: '))
input_interest_rate=float(input('Enter interest rate (percent per year): ')) / 100

def investment():
    investment=input_initial_investment
    for i in range(input_years):
        investment= investment + (investment * input_interest_rate)
    return investment

final_amount = investment()
print(f"At the end of {input_years} years, you will have {final_amount:.2f} dollars.")


