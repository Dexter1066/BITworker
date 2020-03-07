print("Welcome to Taobao!")
money = eval(input("How's your salary?"))
print("What do we have here?")
goods = [
["1", "电脑", 1999],
["2", "鼠标",  10],
["3", "游艇",  20],
["4", "美女",  998],
]
shopping_cart = []
count = 0
for i in goods:
    print(i)
while True:
    choice = input("Please input the number of the goods, or press n to quit:")
    if choice in ["1", "2", "3", "4"]:
        num = int(choice)
        if money >= goods[num-1][-1]:
            shopping_cart.append(goods[num-1][1])
            money -= goods[num-1][-1]
            count += 1
        else:
            print("You don't have enough money!")
    if choice == 'n' or choice == 'N' or count == 4:
        break
if not shopping_cart:
    print("Earn more money!")
else:
    print(shopping_cart, "Your account: %d" % money)
    print("Thank you for your purchase.")
