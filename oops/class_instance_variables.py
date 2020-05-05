import datetime

#  This program explains the difference between class ,
#  instance and static methods


class Employee:  # class name
    """[This tutorial expalain the difference between class and
    instance variables]

    Returns:
        [type] -- [description]
    """

    num_of_emps = 0  # class variable
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
        Employee.num_of_emps += 1

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

    @classmethod
    def set_raise_amount(cls, amount):
        """This is class method can be called directly using class name
        no instance is required for uisng this method
        Generally we use this as getter / setter methods for
        class variables.
        Other uses can be setting some proprty through method which needs to
        be used by all the objects

        Arguments:
            amount {[type]} -- [description]
        """
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        """[This is alternate constructor
        We generally call this as alternate constructor as this needs to be
        used sometimes only like some kind of preprocessing needs to be done
        In this case splitting the string and assigning to class variables]

        Arguments:
            emp_str {[type]} -- [description]

        Returns:
            [type] -- [description]
        """
        first_name, last_name, emp_str_1, salary = emp_str.split("-")
        return cls(first_name, last_name, emp_str_1, salary)

    @staticmethod
    def get_hello():
        """[Neither takes self , nor cls we can call like regular methods
        Whenever we neither access class or instance variables we can keep
        these as helper methods]

        Returns:
            [type] -- [description]
        """
        return "Hello"

    @staticmethod
    def is_workday(day):
        """[Checks if the day at which the code is running is either
        weekday or not.
        Use case : Can be used to check if the day is holiday
        Note : Here it neither refrences cls nor self ,
        Hence it would be appropraite to use this as static method]

        Arguments:
            day {[type]} -- [description]

        Returns:
            [type] -- [description]
        """
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


# This is the instance of the class , and we can reference
# corresponding methods using the obj

emp1 = Employee("Vipul", "Rai", "vipulrai8891@gmail.com", 5000)
print(emp1.display_full_name())

emp2 = Employee("Nikhil", "Rai", "nikhilrai@gmail.com", 5000)

# Note this also works , here we are directly calling the class method
# but passing the instance object
print(Employee.display_full_name(emp1))

print(emp1.raise_salary())
Employee.raise_amount = 1.06

emp1.raise_amount = 1.07
print(emp1.raise_salary())
print(emp2.raise_salary())
print(Employee.num_of_emps)

Employee.set_raise_amount(1.10)  # setting class variable using class method

print(emp1.raise_amount)
print(emp2.raise_amount)

emp_str_1 = Employee.from_string("John-Doe-john@doe.com-545333")
print(emp_str_1.email)

print(Employee.get_hello())
print(Employee.is_workday(datetime.datetime.now()))
