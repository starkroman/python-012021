purchaseList = [
  {"person": "Petr", "item": "Prací prášek", "value": 399},
  {"person": "Ondra", "item": "Savo", "value": 80},
  {"person": "Petr", "item": "Toaletní papír", "value": 65},
  {"person": "Libor", "item": "Pivo", "value": 124},
  {"person": "Petr", "item": "Pytel na odpadky", "value": 75},
  {"person": "Míša", "item": "Utěrky na nádobí", "value": 130},
  {"person": "Ondra", "item": "Toaletní papír", "value": 120},
  {"person": "Míša", "item": "Pečící papír", "value": 30},
  {"person": "Zuzka", "item": "Savo", "value": 80},
  {"person": "Pavla", "item": "Máslo", "value": 50},
  {"person": "Ondra", "item": "Káva", "value": 300}
]

sumPerPerson = {}
for item in purchaseList:
  person = item["person"]
  value = item["value"]
  if person in sumPerPerson:
    sumPerPerson[person] += value
  else:
    sumPerPerson[person] = value

print(sumPerPerson)

totalValue = 0
for person, value in sumPerPerson.items():
  totalValue += value
  print(f"{person} utratil(a) za společné nákupy {value} Kč.")

averageValue = totalValue / len(sumPerPerson)
print(f"Průměrná hodnota na osobu je {round(averageValue)} Kč.")

for person, value in sumPerPerson.items():
    vyrovnani = value - averageValue
    print(f"Vyrovnání mezi kamarády: {person}->{round(vyrovnani)} Kč. ")