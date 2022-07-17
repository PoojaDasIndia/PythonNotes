import numpy as np
"""a=np.arange(12).reshape(3,4)
np.savetxt("test.txt",a)"""

# y=np.loadtxt("test.txt")
# print(y)

"""a=np.arange(12).reshape(3,4)
np.save("my_numpy",a)"""
y=np.load("my_numpy.npy")
print(y)