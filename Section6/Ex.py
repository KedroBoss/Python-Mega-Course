"""Merge files into one"""
import datetime

file_num = 3
content = []
for n in range(1,file_num+1):
    with open("file"+str(n)+'.txt','r') as file:
        temp = file.read()
        content.append(temp)

filename = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f") + '.txt'

with open(filename, 'w') as file:
    for i,v in enumerate(content):
        file.write("Content from file "+str(i)+'\n')
        file.write(v+'\n\n')
