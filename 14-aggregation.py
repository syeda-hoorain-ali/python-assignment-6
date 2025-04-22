class Employee:
    """Represents an employee with a name and an ID.
    Attributes:
        name (str): The name of the employee.
        emp_id (int): ID of the employee.
    """
    
    def __init__(self, name: str, emp_id: int):
        self.name = name
        self.emp_id = emp_id

    def __repr__(self):
        return f"Employee(Name={self.name}, ID={self.emp_id})"


class Department:
    """Represents a department that aggregates an Employee object.
    Attributes:
        dept_name (str): The name of the Department.
        employee (Employee): An instance of the Employee class associated with the department.
    """
    
    def __init__(self, dept_name: str, employee: Employee):
        self.dept_name = dept_name
        self.employee = employee

    def __repr__(self):
        return f"Department(Name={self.dept_name}, Employee={self.employee})"


if __name__ == "__main__":
    emp = Employee(name="John Doe", emp_id=101)
    dept = Department(dept_name="HR", employee=emp)
    print(dept)
