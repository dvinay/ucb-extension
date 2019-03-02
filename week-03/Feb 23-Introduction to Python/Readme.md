### Introduction to Python I ###

The following **concepts** has been coverd in this class:
* Feb-23-2019

* [x] Python basics - practice programs
    * [-] print statement
        ```
        print("Hello world")
        ```
    * [-] How to run a python program
        1. open terminal
        2. create a folder using mkdir command
        ``` $ mkdir LearnPython ```
        3. create a file using touch sample.py
        ``` $ touch sample.py ```
        4. open the file in some editor
        5. enter print("hello world") to display result
        ```
          print("Hello World!")
        ```
        5. save and go to terminal
        6. run python filename
        ``` $ python sample.py ```

    * [-] Python anaconda test
        * [-] to test anaconda version.
        ```
        $ conda --version
        ```
        * [-] to find anaconda env list.
        ```
        $ conda env list
        ```
    * [-] Create Python anaconda Virtual env
        * [-] to create a python anaconda Virtual env
        ```
        $ conda create -n PythonData python=3.6 anaconda
        ```
        * [-] to activate a python anaconda Virtual env
        ```
        $ source activate PythonData
        ```
## Boom, your env is set. Lets learn Python ##

* [x] Python basics - 
    * [-] creating a variable, just give name and value
        ```
        name = "Vinay"
        ```
    * [-] print name using string concatenation
        ```
        print("my name is : "+ name)
        ```
    * [-] print name using f-string format
        ```
        print(f"my name is {name}")
        ```
    * [-] if statement
        ```
        x = 5
        if len("Dog") < x:
            print("Question 2 works!")
        ```
    * [-] if else statement
        ```
        x = 2
        y = 5
        if (x ** 3 >= y) and (y ** 2 < 26):
            print("GOT QUESTION 3!")
        else:
            print("Oh good you can count")
        ```
    * [-] if elif statement
        ```
        name = "Dan"
        group_one = ["Greg", "Tony", "Susan"]
        group_two = ["Gerald", "Paul", "Ryder"]
        group_three = ["Carla", "Dan", "Jefferson"]

        if name in group_one:
            print(name + " is in the first group")
        elif name in group_two:
            print(name + " is in group two")
        elif name in group_three:
            print(name + " is in group three")
        else:
            print(name + " does not have a group")
        ```
    * [-] list example
      * [-] Create a variable and set it as an List
      ```
        myList = [1,"Sample",3,"Test"]
        print(myList)
      ```
      * [-] Add an element onto the end of a List
      ```
        myList.append("Matt")
        print(myList)
      ```
      * [-] Return the index of the first object with a matching value
      ```
        print(myList.index("Matt"))
      ```
      * [-] Change a specified element within an List at the given index
      ```
        myList[3] = 85
        print(myList)
      ```
      * [-] Returns the length of the List
      ```
        print(len(myList))
      ```
      * [-] Removes a specified object from an List
      ```
        myList.remove("Matt")
        print(myList)
      ```
      * [-] Removes the object at the index specified
      ```
        myList.pop(0)
        myList.pop(0)
        print(myList)
      ```
    * [-] tuple example
      * [-] Creates a tuple, a sequence of immutable Python objects that cannot be changed
      ```
        myTuple = ('Python', 100, 'VBA', False)
        print(myTuple)
      ```
    * [-] for loop
      * [-] to repeat a set of data
      ```
        myList = [1,"Sample",3,"Test"]
        for data in myList:
          print(data)
      ```
      * [-] to repeat all characters in the string
      ```
        data = "Vinay"
        for ltr in data:
            print(ltr)
      ```
    * [-] while loop
      * [-] to repeat until a certain condition is true
      ```
        x = 'y'
        while x == 'y':
            x = input("want to continue [y/n]")
            print("you have selected : "+ x)
      ```
      
* [x] Excercise
  * [-] Helloworld
  * [-] variable example and print using string concatenation
  * [-] f-string example
  * [-] input from user example using input() and int(input())
  * [-] Rock paper scissors game
    * [-] learning random module
    * [-] conditions
  * [-] display numbers from given range and ask user want to continue or not
    * [-] for loop with range
    * [-] while loop to check condition