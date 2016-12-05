print("Variable example")
money_value = 100
days_passed = 2
money_value_change = -5
text = ("The initial value is ", money_value, ".", days_passed, " days passed. Value of the currency now is ", money_value + money_value_change)
print(text)

print("Function example")
def currency_converter(base_rate, quote_rate):
	exchange_rate = quote_rate * base_rate
	return exchange_rate

base_rate = input("Base Rate = ")
quote_rate = input("Quote Rate = ")
print(currency_converter(float(base_rate), float(quote_rate)))

print("Convert Date Type Example")

decimal_num = 9.11
decimal_round = round(decimal_num)
print(decimal_round)

print("String Operations")

text = "Something important"
print(text[3:7])
print(text*2)

print("List")
li=["Today", "Tommorow", 3]
tu = (1,3,7)
def list_func(li):
	li_len = len(li)
	print("Lenth of the ist is "+str(li_len))
	print("The first item is "+ str(li[0]) + ". The last is "+ str(li[-1]))

def append_func(li, app_item):
	li.append(app_item)
list_func(li)
append_func(li, 7)
list_func(li)

print("Dictionaries")
dic  = {"Name":"Boss", "Professtion":"The King"}
a = list(dic.values())
print(a)
