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

    def __repr__(self):
        """[Should be used for debugging and logging , this should be able to recreate the object]
        O/P : Employee(Vipul,Rai,vipulrai8891@gmail.com,5000)
        which is exactly the one which we used to create the object initially

        """
        return (
            f"Employee({self.first_name},{self.last_name},{self.email},{self.salary})"
        )

    def __str__(self):
        """[Visible representation for user , the code looks here first if no implementation
        found , then goes to __repr__]
        O/P : Vipul Rai , vipulrai8891@gmail.com
        """
        return f"{self.display_full_name()} , {self.email}"

    def __add__(self, other):
        return self.salary + other.salary

    def __len__(self,):
        """[total character in emp full name]
        """
        return len(self.display_full_name())


emp1 = Employee("Vipul", "Rai", "vipulrai8891@gmail.com", 5000)
print(emp1.display_full_name())

emp2 = Employee("Nikhil", "Rai", "nikhilrai@gmail.com", 6000)
print(emp2.display_full_name())

print(emp1)
print(repr(emp1))
print(str(emp1))  # This also changes the default behaviour of print

# Vipul Rai , vipulrai8891@gmail.com
# Employee(Vipul,Rai,vipulrai8891@gmail.com,5000)
# Vipul Rai , vipulrai8891@gmail.com

print(emp1 + emp2)  # 11000 , using the dunder add changed the functionality of +

print(len(emp1))  # 9
