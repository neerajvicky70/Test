data = open("name.txt", "r")
# print(data.readable())
print(data.readline())
print(data.readlines()[-1])
data.close()

