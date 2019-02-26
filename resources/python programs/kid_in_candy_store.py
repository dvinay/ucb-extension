# The list of candies to print to the screen
candyList = ["Snickers", "Kit Kat", "Sour Patch Kids", "Juicy Fruit", "Swedish Fish",
             "Skittles", "Hershey Bar", "Skittles", "Starbursts", "M&Ms"]

# Enter the candyList
for candy in candyList:
    print("[" + str(candyList.index(candy)) + "]" + candy)

# The amount of candy the user will be allowed to choose
allowance = int(input("Enter amount of candy "))

# The list used to store all of the candies selected inside of
candyCart = []
for i in range(0,allowance) :
    candyValue = int(input("Which candy would you like to bring "))
    candyCart.append(candyList[candyValue])

for candy in candyCart:
    print("[" + str(candyCart.index(candy)) + "]" + candy)

