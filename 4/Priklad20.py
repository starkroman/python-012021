from faker import Faker
generator_falesnych_dat = Faker("cs_CZ")

#print(generator_falesnych_dat.name())
#print(generator_falesnych_dat.address())

class Balik:
  def get_info(self):
    print(f"Příjemce balíku: {self.name}")
    print(f"Balík doručte na adresu: {self.address}")

  def __init__(self, name, address):
    self.name = name
    self.address = address

balik = Balik(generator_falesnych_dat.name(), generator_falesnych_dat.address())
balik.get_info();