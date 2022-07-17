"""
A module is a file containing Python definitions and statements.
A module is a file containing group of variables, methods, function and classes etc.
They are executed only the first time the module name is encountered in an import statement.
The file name is the module name with the suffix .py appended.
Ex:- mymodule.py

import statement is used to import modules.
Syntax:-
import module_name
import module_name as alias_name
from module_name import function_name1, function_name2,……, function_nameN
from module_name import var_name1, var_name2,……, var_nameN
from module_name import class_name1, class_name2,……, class_nameN
from module_name import var_name, f_name, class_name, method_name……,
from module_name import f_name as alias_f_name
from module_name import *

Note - Modules can import other modules

"""

# Main.py <----Main Module
"""
import Cal

print("Cal Module's variable",Cal.a)

Cal.name()

a=Cal.add(4, 5)
print(a)

b=Cal.sub(20, 8)
print(b)

print("***********************************\n")

add=Cal.add
a=add(4, 5)
print(a)

sub=Cal.sub
b=sub(20, 8)
print(b)

print("-----------------------------------------------------------------------")

import Cal as c
print("Cal Module's variable",c.a)
c.name()

a=c.add(4, 5)
print(a)

b=c.sub(20, 8)
print(b)

print("***********************************\n")

add=c.add
a=add(4, 5)
print(a)

sub=c.sub
b=sub(20, 8)
print(b)

print("-----------------------------------------------------------------------")

from Cal import a, name, add, sub

print(a)
name()
print(add(4, 8))
print(sub(4, 8))

print("-----------------------------------------------------------------------")

from Cal import a, name, add as s, sub

print(a)
name()
print(s(4, 8))
print(sub(4, 8))

print("-----------------------------------------------------------------------")
"""

from Cal import *
print(a)
name()
print(add(4, 8))
print(sub(4, 8))

