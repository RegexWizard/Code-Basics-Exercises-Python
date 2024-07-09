import time
interval = 2

class School:
    def __init__(self, length_of_the_land, amount_of_teacher, amount_of_students, amount_of_classes):
        self._length_of_the_land = length_of_the_land
        self._amount_of_teacher = amount_of_teacher
        self._amount_of_students = amount_of_students
        self._amount_of_classes = amount_of_classes

    def Bell(self):
        print("DING DONG DING DONG")

    @property
    def length_of_the_land(self):
        return self._length_of_the_land

    @length_of_the_land.setter
    def length_of_the_land(self, number):
        self._length_of_the_land = number

    @property
    def amount_of_teacher(self):
        return self._amount_of_teacher

    @amount_of_teacher.setter
    def amount_of_teacher(self, number):
        self._amount_of_teacher = number

    @property
    def amount_of_students(self):
        return self._amount_of_students

    @amount_of_students.setter
    def amount_of_students(self, number):
        self._amount_of_students = number

    @property
    def amount_of_classes(self):
        return self._amount_of_classes

    @amount_of_classes.setter
    def amount_of_classes(self, number):
        self._amount_of_classes = number

# Create an instance of School
SMATAG = School(4, 34, 734, 16)

# Print the school information
print("Amount of the length of the land is %i KM with %i teachers including the administrator. There are %i students and %i classes." % (SMATAG.length_of_the_land, SMATAG.amount_of_teacher, SMATAG.amount_of_students, SMATAG.amount_of_classes))
print("====================INTERVALS====================")

# Wait for the interval and ring the bell
time.sleep(2)
SMATAG.Bell()
