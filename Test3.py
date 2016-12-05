print('For loop in more then one list')
names = ['James','John','Jack']
email_domains = ['gmail','yahoo','hotmail']

for i,j in zip(names, email_domains):
    print (i,j)
