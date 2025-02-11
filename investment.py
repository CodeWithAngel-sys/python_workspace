input_initial_investment=int(input('Enter initial amount: '))
input_years=int(input('Enter number of years: '))
input_interest_rate=float(input('Enter interest rate: '))

def investment():
    investment=input_initial_investment
    for i in range(input_years):
        investment= investment + (investment* 0.055)
    return investment

print(investment())
print('at the end of ',input_years,' years you will have ',investment(),' dollars')


