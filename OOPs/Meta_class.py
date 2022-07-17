"""
In object-oriented programming, a metaclass is a class whose instances are classes.
Just as an ordinary class defines the behavior of certain objects, a metaclass defines the behavior of certain classes and their instances.
Not all object-oriented programming languages support metaclasses.
Among those that do, the extent to which metaclasses can override any given aspect of class behavior varies.
Metaclasses can be implemented by having classes be first-class citizens, in which case a metaclass is simply an object that constructs classes.
Each language has its own metaobject protocol,a set of rules that govern how objects, classes, and metaclasses interact

"""


class Student:
    y=45


s = Student()
print(type(s))

# output : <class '__main__.Student'>

print(type(Student))

# output : <class 'type'>
print("----------------------------------------------------")
a = 14
print(type(a))

# output : <class 'int'>
print("----------------------------------------------------")


def fun():
    pass


print(type(fun()))
# output : <class 'NoneType'>

"""Type is a default metaclass in python"""

print("----------------------------------------------------")
print(type(int))

# <class 'type'>

print("******************************************************")

a = type("python", (Student,), {"x": 10})
obj= a()
print(obj)
print(obj.x)
print(type(a()))
print(obj.y)
