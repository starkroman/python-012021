from forex_python.converter import CurrencyRates
prevodnik = CurrencyRates()
pozadovano_v_cilove_mene = 100

cena_v_korunach = prevodnik.convert('USD', 'CZK', pozadovano_v_cilove_mene)
print(f"Za {pozadovano_v_cilove_mene} USD zaplatíme {round(cena_v_korunach,2)} Kč.")

cena_v_korunach = prevodnik.convert('EUR', 'CZK', pozadovano_v_cilove_mene)
print(f"Za {pozadovano_v_cilove_mene} EUR zaplatíme {round(cena_v_korunach,2)} Kč.")

cena_v_korunach = prevodnik.convert('DKK', 'CZK', pozadovano_v_cilove_mene)
print(f"Za {pozadovano_v_cilove_mene} DKK zaplatíme {round(cena_v_korunach,2)} Kč.")

mena = input("Zadej požadovanou měnu: ")
kolik = int(input("Zadej kolik chceč cizí měny: "))
cena_v_korunach = prevodnik.convert(mena, 'CZK', kolik)
print(f"Za {kolik} {mena} zaplatíme {round(cena_v_korunach,2)} Kč.")

'''
print(prevodnik.get_rates('CZK'))
rates = prevodnik.get_rates('CZK')
for key, value in rates.items():
    rate = 1 / value
    print(f"1 {key} = {round(rate,2)}")


currencyList = ["GBP", "EUR", "USD"]
for key, value in rates.items():
  if key in currencyList:
    rate = 1 / value
    print(f"1 {key} = {round(rate, 2)}")
'''