class Employee:
  def get_info(self):
    return f"{self.name} pracuje na pozici {self.position}."

  def __init__(self, name, position, salary, children):
    self.name = name
    self.position = position
    self.salary = salary
    self.children = children

  def get_tax(self):
    tax = self.salary * 0.15 - self.children * 1500
    return tax

  def get_net_salary(self):
    net_salary = self.salary - self.get_tax()
    return net_salary

frantisek = Employee("František Dobrota", "Programátor", 30000, 2)
frantisek.get_info()
print(f"Daň z příjmu je: {frantisek.get_net_salary()}")