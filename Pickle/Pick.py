import pickle, Student_class

# from Student_class import Student

# Storing the object in the file

# Pickling -- write the binary file

n=int(input("Enter Number of Students"))

with open("Student.dat", mode="wb") as f:

    for i in range(n):
        Name = input("Enter the name : ")
        Roll_no = int(input("Enter the roll no. : "))
        Address = input("Enter the address : ")
        stu = Student_class.Student(Name, Roll_no, Address)
        pickle.dump(stu, f)

print("Pickling Done!!")