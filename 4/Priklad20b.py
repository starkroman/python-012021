'''https://faker.readthedocs.io/en/master/fakerclass.html'''
'''https://faker.readthedocs.io/en/master/locales.html'''


from faker import Faker

locale_list = ["cs_CZ", "sk_SK"]
generator_falesnych_dat = Faker(locale_list)
generator_falesnych_dat.locales

'''
print(generator_falesnych_dat.state())
print(generator_falesnych_dat.email())
print(generator_falesnych_dat.company())
print(generator_falesnych_dat.user_name())
print(generator_falesnych_dat.street_address())
print(generator_falesnych_dat.city())
print(generator_falesnych_dat.password())
print(generator_falesnych_dat.job())
print(generator_falesnych_dat.color_name())
print(generator_falesnych_dat.text())
print(generator_falesnych_dat.profile())
print(generator_falesnych_dat.ssn())
'''

# zkoušel jsem i jinou variantu než -> address()
class Balik:
  def get_info(self):
    print(f"Příjemce balíku: {self.name}")
    print(f"Balík doručte na adresu: {self.street}, {self.city}")

  def __init__(self, name, street, city):
    self.name = name
    self.street = street
    self.city = city

balik = Balik(generator_falesnych_dat.name(), generator_falesnych_dat.street_address(), generator_falesnych_dat.city())
balik.get_info();

