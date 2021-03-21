import pandas as pd

pocet = pd.read_csv('country_vaccinations.csv')
print(pocet.shape)
print(pocet.head())
print(pocet.info())

# vypíše vše jen pro [date == 10.3.2021]
print(pocet[(pocet['date'] == '2021-03-10')][['country','total_vaccinations']])

# vypíše jen pro [date == 10.3.2021], kde je naočkováno více > 1mil.
print(pocet[(pocet['date'] == '2021-03-10') & (pocet['total_vaccinations'] > 1000000)][['country','total_vaccinations']])

# vypíše jen pro [date == 10.3.2021] naočkováno více > 100000 nebo méně < 100000
print(pocet[(pocet['date'] == '2021-03-10') & (pocet['total_vaccinations'] > 100000) | (pocet['total_vaccinations'] < 100000)][['country','total_vaccinations']])

# přehlednější varianta:
'''
radky = (pocet['date'] == '2021-03-10') & (pocet['total_vaccinations'] > 100000) | (pocet['total_vaccinations'] < 100000)
sloupce = ['country','total_vaccinations']
vyber = pocet[radky][sloupce]
print(vyber)
'''
#& (pocet['city'] == 'Italy') | (pocet['city'] == 'Finland') | (pocet['city'] == 'United Kingdom')
radky = (pocet['date'] == '2021-03-10') | (pocet['date'] == '2021-03-11')
radky2 = (pocet['country'] == 'Italy') | (pocet['country'] == 'Finland') | (pocet['country'] == 'United Kingdom')
sloupce = ['country','total_vaccinations']
vyber = pocet[radky & radky2][sloupce]
print(vyber)

# varianta s isin
radky3_isin = pocet['country'].isin(['Italy','Finland','United Kingdom'])
sloupce = ['total_vaccinations']
vyber = pocet[radky & radky3_isin][sloupce]
print(vyber)

# celkový počet vakcím v daných státech
vyber = pocet[radky & radky3_isin][sloupce].sum()
print(vyber)

# výběr pro Japan ve dnech 3.3.2021 až 9.3.2021
radky = (pocet['date'] >= '2021-03-03') & (pocet['date'] <= '2021-03-09') & (pocet['country'] == 'Japan')
sloupce = ['date', 'total_vaccinations']
vyber = pocet[radky][sloupce]
print(vyber)
