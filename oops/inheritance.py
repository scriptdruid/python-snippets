#  From the Awesome tutorials by Corey Schafer at https://www.youtube.com/watch?v=RSl87lqOXDE


class Employee:  # class name
    raise_amount = 1.05  # class variable

    def __init__(self, first_name, last_name, email, salary):

        """Constructor ,automatically initialized at obj creation time
        These are the setting of instance variables,
        each instance would have seperate copies.

        Arguments:
            first_name {[type]} -- [description]
            last_name {[type]} -- [description]
            email {[type]} -- [description]
            salary {[type]} -- [description]
        """
        self.first_name = first_name  # instance variables
        self.last_name = last_name
        self.email = email
        self.salary = salary

    def display_full_name(self):
        """objects method or regular method , note the first argument
        is always self whihc means refrencing to the object which created this.

        Returns:
            [type] -- [description]
        """
        return self.first_name + " " + self.last_name

    def raise_salary(self):
        """Acessing class variable using class name , this can also be
        accessed using object  (in comments ) both returns the same o/p

        Returns:
            [type] -- [description]
        """
        return self.salary * self.raise_amount
        # return self.salary * Employee.raise_amount
        # Note : using class variable here.


class Developer(Employee):
    # Overiding the base class variable , does not effect Employee class
    raise_amount = 1.10

    def __init__(self, first_name, last_name, email, salary, prog_lang):
        super().__init__(first_name, last_name, email, salary)

        """ Adding prog_lang as additional variable

        Arguments:
            first_name {[type]} -- [description]
            last_name {[type]} -- [description]
            email {[type]} -- [description]
            salary {[type]} -- [description]
            prog_lang {[type]} -- [description]
        """
        self.prog_lang = prog_lang  # Only adding prog lang


class Manager(Employee):
    def __init__(self, first_name, last_name, email, salary, employees_reporting=None):
        super().__init__(first_name, last_name, email, salary)
        if employees_reporting is None:
            self.employees_reporting = []
        else:
            self.employees_reporting = employees_reporting

    def add_emp(self, emp):
        if emp not in self.employees_reporting:
            self.employees_reporting.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees_reporting:
            self.employees_reporting.remove(emp)

    def display_emp(self):
        for emp in self.employees_reporting:
            print("--->", emp.display_full_name())


# Base class objects


# emp1 = Employee("Vipul", "Rai", "vipulrai8891@gmail.com", 5000)
# print(emp1.display_full_name())

# emp2 = Employee("Nikhil", "Rai", "nikhilrai@gmail.com", 6000)
# print(emp2.display_full_name())


# Inherited class objects, here we can exactly create object and it refrences
# the base class constructor

# emp1 = Developer("Vipul", "Rai", "vipulrai8891@gmail.com", 5000)
# print(emp1.display_full_name())

# emp2 = Developer("Nikhil", "Rai", "nikhilrai@gmail.com", 6000)
# print(emp2.display_full_name())

# print(help(Developer))  # Very useful to find the flow

emp1 = Developer("Vipul", "Rai", "vipulrai8891@gmail.com", 5000, "Python")
print(emp1.display_full_name())
print(emp1.prog_lang)

emp2 = Developer("Nikhil", "Rai", "nikhilrai@gmail.com", 6000, "Golang")
print(emp2.display_full_name())


mgr1 = Manager("John", "Cena", "John@cena.com", 89000, [emp1])

print(mgr1.email)
print(mgr1.display_emp())
mgr1.add_emp(emp2)
print(mgr1.display_emp())

mgr1.remove_emp(emp1)
print(mgr1.display_emp())

#  isinstance usage

print(isinstance(mgr1, Employee))  # - True
print(isinstance(mgr1, Manager))  # - True
print(isinstance(mgr1, Developer))  # - False

#  issubclass usage

print(issubclass(Developer, Employee))  # - True
print(issubclass(Developer, Manager))  # - False
