print("Conditions example and User Input")

v = input("Type a number: ")

if int(v)<3:
    print("Less")
    print("Really")
elif int(v)==3:
    print("Equal")
else:
    print("Greater")

print("Positive" if int(v)>0 else "Negative")



print("Loops example")

emails=["bob@email.com","boss@email.com","hilary@email.leaked"]
for item in emails:
    print(item)
    if ".com" in item:
        print("This one is legit")
    else:
        print("This one is not legit")

real_pas = 'python123'
password = ''
while password != real_pas:
    password = input('Enter password: ')
    if password == real_pas:
        print('You are logged in!')
    else:
        print('Sorry, try again.')
