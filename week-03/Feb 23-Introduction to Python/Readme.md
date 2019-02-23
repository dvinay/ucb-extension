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
