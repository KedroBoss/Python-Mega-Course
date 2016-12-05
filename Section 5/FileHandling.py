file = open("example.txt", 'r')
content = file.read()
file.close()
print(content)

file = open("example1.txt", 'w')
lines=input('How many lines? ')
for i in range(1, int(lines)+1):
    file.write("Line "+str(i)+"\n")
file.close()

with open("example1.txt", "a+") as file:
    file.seek(0)
    content=file.read()
    file.write("\nWrite Line")
