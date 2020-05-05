class Employee:  # class name
    raise_amount = 1.05  # class variable

    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name  # instance variables
        self.last_name = last_name
        self.salary = salary

    @property
    def display_full_name(self):
        return self.first_name + " " + self.last_name

    @display_full_name.setter
    def display_full_name(self, name):
        self.first_name, self.last_name = name.split(" ")

    @display_full_name.deleter
    def display_full_name(self):
        print("Deleted !")
        self.first_name, self.last_name = None, None

    @property
    def email(self):
        return f"{self.first_name}{self.last_name}@gmail.com"


# emp1 = Employee("Vipul", "Rai", "vipulrai8891@gmail.com", 5000)
# print(emp1.display_full_name())

emp1 = Employee("Vipul", "Rai", 5000)


emp1.first_name = "Mark"
# print(emp1.first_name)
# print(emp1.email)
# print(emp1.display_full_name())

# Mark
# vipulrai8891@gmail.com
# Mark Rai -- this changed but the email did not change

emp1.display_full_name = "Vipul Rai"
print(emp1.display_full_name)

del emp1.display_full_name

print(emp1)
