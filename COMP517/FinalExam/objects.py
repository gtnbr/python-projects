class Person:
    '''Person class with get_name and get_id methods.'''
    def __init__(self, name, id):
        '''Initialize a person object.'''
        self.name = str(name)
        self.id = int(id)

    def get_name(self):
        '''Getter function for the name'''
        return self.name

    def get_id(self):
        '''Getter function for the id'''
        return self.id

    def __str__(self):
        '''Returns a custom message when a person is printed'''
        return f"{self.get_name()} is a person with id number {self.get_id()}"


class Student(Person):
    '''Student class with set_grade and average_grade methods.'''
    nos = 0
    def number_of_students():
        '''Returns the number of student objects initialized.'''
        return Student.nos

    def __init__(self, name, id):
        '''Initialize a student object with person attributes.'''
        super().__init__(name, id)
        self.grades = {}
        Student.nos += 1

    def set_grade(self, code, grade):
        '''Sets a grade matched to a code in the student grades dictionary'''
        if grade not in range(0, 101):
            raise ValueError("Invalid grade.")
        self.grades[str(code)] = int(grade)

    def average_grade(self):
        '''Calculates the average grade and rounds it down to an int'''
        if not self.grades:
            return 0
        return int(sum(self.grades.values())/len(self.grades.values()))

    def __str__(self):
        '''Returns a custom message when a student object is printed'''
        return f"{self.get_name()} is a student with id number {self.get_id()} and average grade {self.average_grade()}%"


class Staff(Person):
    '''
    Staff class with add_advisee, is_advisee, get_advisees
    and advisees_average_grades methods.
    '''
    def __init__(self, name, id):
        '''Initialize a staff object with person attributes.'''
        super().__init__(name, id)
        self.advisees = []

    def add_advisee(self, student):
        '''Adds an student to the staff member's advisee list.'''
        self.advisees.append(student)

    def is_advisee(self, student):
        '''Returns a boolean for whether the student is an advisee of the staff member'''
        return student in self.advisees

    def get_advisees(self):
        '''Returns a sorted list of student objects in order of their id.'''
        return sorted(self.advisees, key=lambda x: x.get_id())

    def advisees_average_grades(self):
        '''Returns the average grades of the staff memebers advisees.'''
        if not self.get_advisees():
            return 0
        x = [i.average_grade() for i in self.advisees]
        return int(sum(x)/len(x))

    def __str__(self):
        '''Returns a custom message when a staff object is printed'''
        return f"{self.get_name()} is a staff member with id number {self.get_id()} and {len(self.get_advisees())} advisees."
