class Person:
    """
    Represents a person with a name.
    Attributes:
        name (str): The name of the person.
    """
    
    def __init__(self, name: str):
        self.name = name


class Teacher(Person):
    """
    Represents a Teacher, which is a subclass of Person.
    Attributes:
        name (str): The name of the teacher, inherited from the Person class.
        subject (str): The subject that the teacher specializes in.
    """
    
    def __init__(self, name: str, subject: str):
        super().__init__(name)
        self.subject = subject


if __name__ == '__main__':
    teacher = Teacher("Zia Khan", "Agentic AI")
    print(f"{teacher.name} teachs {teacher.subject}")
