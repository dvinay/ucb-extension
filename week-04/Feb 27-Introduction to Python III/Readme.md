### Introduction to Python III ###

The following **concepts** has been coverd in this class:
* Feb-27-2019

* [x] Python basics - practice programs
    * [-] Dictionaries
        ```
        # A List of an actors
        actors = ["Tom Cruise", "Angelina Jolie","Kristen Stewart","Denzel Washington"]

        # A dictionary of an actor
        actor = {"name": "Tom Cruise"}
        print(f'{actor["name"]}')
        print(actor)
        ```
    * [-] List Comprehensions
        ```
        # Normal for loop
        fish = "halibut"
        letters = []
        for letter in fish:
          letters.append(letter)
        print(letters)
        
        # Comprehensions List for alphabets
        fish = "halibut"
        letters = [letter for letter in fish]
        print(letters)
        ```

        ```
        # We can also add conditional logic (if statements) to a list comprehension
        july_temperatures = [87, 85, 92, 79, 106]
        hot_days = []
        for temperature in july_temperatures:
            if temperature > 90:
                hot_days.append(temperature)
        print(hot_days)

        # List Comprehension with conditional
        hot_days = [temperature for temperature in july_temperatures if temperature > 90]   
        ```

        ```
        # Functions
        def solution():
          print("Data")

        solution()
        ```
    * [-] Git Commands       
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