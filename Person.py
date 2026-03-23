class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Employee(Person):
    def __init__(self, name, age, emp_id, salary):
        super().__init__(name, age)
        self.emp_id = emp_id
        self.salary = salary


class Manager(Employee):
    def __init__(self, name, age, emp_id, salary, department):
        super().__init__(name, age, emp_id, salary)
        self.department = department

    def display(self):
        print(self.name, self.age, self.emp_id, self.salary, self.department)


# Driver Code
m = Manager("Atharv", 22, 501, 50000, "IT")
m.display()
