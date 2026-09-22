class Employee:
    def __init__(self, first: str, last: str, pay: int): # -- like a constructor in python, self should always be the first argument
        self.first = first
        self.last = last
        self.pay = pay
        self.full_name = f"{first.title()} {last.title()}"

    def emp_details(self) -> str : # self argument is always required for methods
        print("\nEmployee Directory\n")
        return f"Name : {self.full_name} \nSalary : ${self.pay:,}"

        


# instances of class
employee1 = Employee('nimisha', 'jith', 54000)
employee2 = Employee('hari','krishnan',60000)

print(employee1.emp_details())

# we can also do
print(Employee.emp_details(employee2))