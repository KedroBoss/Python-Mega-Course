print("Excerciese 1. Convert Celsius to Fahrenheit")
lowest_tempr=-273.15
def cel_to_fah(temperature):
    if temperature < lowest_tempr:
        return "This is lower than the lowest possible temperature"
    else:
        fah = temperature * 1.8 + 32
        return fah

def cel_to_fah_file(temperature,file):
    if temperature > lowest_tempr:
        fah = temperature * 1.8 + 32
        file.write(str(fah)+'\n')




temperatures = [10, -20, -289, 100]
'''file = open('ex1Sup.txt', 'w')
for item in temperatures:
    print(cel_to_fah(item))
    cel_to_fah_file(item,file)
file.close()'''

with open('ex1Sup.txt', 'w') as file:
    for item in temperatures:
        print(cel_to_fah(item))
        cel_to_fah_file(item,file)
