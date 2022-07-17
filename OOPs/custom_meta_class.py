# Custom metaclass in python
"""
Custom metaclass can also be defined in the two ways:
 1.
 class MetaOne(type):
    def__new__(cls,name, bases, dict):
        pass


* The __new__ method creates and returns the new class object


2.
class MetaTwo(type):
    def __init__(cls,name, bases, dict):
        pass


* The __init__ method initializes the newly created object

"""


class MetaOne(type):
    pass


class Student(metaclass=MetaOne):
    pass


print(type(Student))

print("---------------------------------------------")


class MetaTwo(type):
    def __new__(self, name, bases, attr):
        print(attr)
        print("HEllo")
        print(type(name, bases, attr))
        return type(name, bases, attr)

    def __init__(cls, name, bases, attr):
        super().__init__()
        print("This")
        # return None


class Python(metaclass=MetaTwo):
    x=45
    y=78

a=Python()
a.x
print(a)



