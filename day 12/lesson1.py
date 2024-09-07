#1
choice = input("which academy do you go to: ")
if choice == "GOA":
 print("good")
else:
 print("bad")

#2
 price = int(input("enter the price: "))
 budget = int(input("enter your budget: "))
 if budget > price or budget == price:
     print("you got enough")
 else:
     print("you need", price - budget, "more")

#3
 num = int(input("enter the number: "))
 if num <= 5:
     print(num * 2)
 else:
     print(num * 4)

#4
 price = 10
 quantity = int(input("enter the amount of tickets you want to purchase: "))
 if quantity < 5:
     print(price * quantity)
 else:
     print(price * quantity * 0.7)

#5
 num1 = int(input("enter the first number: "))
 num2 = int(input("enter the second number: "))
 choice = input("Enter the operator(+, -, *, /): ")

 if choice == "+":
     print(num1 + num2)
 elif choice == "-":
     print(num1 - num2)
 elif choice == "*":
     print(num1 * num2)
 elif choice == "/":
     print(num1 / num2)