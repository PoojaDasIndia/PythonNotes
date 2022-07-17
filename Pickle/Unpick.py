import pickle

# giving the data
# Unpickling --read the binary file
with open("Student.dat", mode="rb") as f:
    while True:
        try:
            obj = pickle.load(f)
            obj.disp()

        except EOFError:
            print("Unpickling Done!!")
            break






