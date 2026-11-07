names = input("Enter the names of your friends, separated by commas:\n").split(", ")
friends_number = len(names)
friends_money= []
for x in names:
   print(f"\n {x}\n")
   money = float (input ("How much money did you spend?\n $$"))
   print("_____**______")
   friends_money.append(money)
print("_____**______")
print(f"\nThe total amount of money spent is:\n {sum(friends_money)} $$")
print("_____**______")
print(f"\n Everyone's to pay:\n {(sum(friends_money))/friends_number}")
