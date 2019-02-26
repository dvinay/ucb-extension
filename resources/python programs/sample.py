x = 'y'
while x == 'y':
    start = int(input("Enter starting value : "))
    end = int(input("Enter ending value : "))
    for i in range(start,end+1):
        print(i)
    x = input("you want to continue [y/n] : ")