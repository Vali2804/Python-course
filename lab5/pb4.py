class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_salary(self):
        return self.salary

class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def get_salary(self):
        return super().get_salary() + self.bonus

class Engineer(Employee):
    def __init__(self, name, salary, tech_skill):
        super().__init__(name, salary)
        self.tech_skill = tech_skill

    def get_salary(self):
        return super().get_salary() + self.tech_skill * 100

class Salesperson(Employee):
    def __init__(self, name, salary, sales):
        super().__init__(name, salary)
        self.sales = sales

    def get_salary(self):
        return super().get_salary() + self.sales * 0.1
    
def main():
    employees = [Manager("John", 1000, 100), Engineer("Mary", 1000, 5), Salesperson("Bob", 1000, 1000)]
    for employee in employees:
        print(employee.get_salary())

if __name__ == "__main__":
    main()
