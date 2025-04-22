class Student:
    """
    A class to represent a student and their exam performance.
    Attributes:
        name (str): The name of the student.
        marks (int): The marks obtained by the student in the exam.            
    """

    def __init__(self, name: str, marks: int):
        self.name = name
        self.marks = marks
    
    def display(self):
        """Prints the student's name and their marks in a formatted string."""
        print(f"{self.name.title()} got {self.marks} in exam.")


if __name__ == '__main__':
    student1 = Student("Hoorain", 100)
    student2 = Student("Mantasha", 98.5)

    student1.display()
    student2.display()
