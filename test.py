from Klib.files import *


r = openFile("data.txt", True)
print(len(r))
for i in range(6, len(r)):

    print(i)
    print(r[i])
    print("OK")
