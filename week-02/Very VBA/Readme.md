### Very VBA ###

The following **concepts** has been coverd in this class:

* [x] VBA basics
	* [-] variables
		* [-] variable declaration
		```
		dim ing1 as String
		dim ing2 as String
		dim budget as Double
		```
		* [-] variable Assignment
		```
		ing1 = "Peanut Butter"
		ing2 = "Jelly"
		budget = 5.00
		```
	* [-] arrays
		* [-] group of items together
		```
		Dim ingredients(0 to 2) As String
		ingredients(0) = "Peanut Butter"
		ingredients(1) = "Jelly"
		ingredients(2) = "Bread"
		```
	* [-] conditions
		* [-] If This... Then That.
		```
		If pbThicknes > 1.0 Then
			stopSpreading()
		Else
			startSpreading()
		```
	* [-] Iteration
		* [-] For loop
		```
		For i = 0 To 20
			stopSpreading()
		Next i
		```
	* [-] Functions and Sub
		* [-] The difference between a function and a sub in Excel VBA is that a function can return a value while a sub cannot.
		```
		Function Area(x As Double, y As Double) As Double
			Area = x * y
		End Function
		Sub Area(x As Double, y As Double)
			MsgBox x * y
		End Sub
		```
* [x] Excercise
	* [-] Hello world program
	```
	Sub Helloworld():
    	MsgBox ("HelloWorld1")
	End Sub
	```
	* [-] Hello world program
	```
	Sub Helloworld():
    	MsgBox ("HelloWorld1")
	End Sub
	```

## Video Walkthrough of concepts:

Here's a walkthrough of implemented basic cases:

1. Hello World
![Hello World](vba_helloworld.gif)

2. Button Click
![Button Click](vba_buttonclick.gif)

3. Cells function
![Cells function](vba_cells.gif)

4. Range function
![Range function](vba_range.gif)

5. Variables
![Variables](vba_cells.gif)

6. Arrays
![Arrays](vba_arrays.gif)

7. Split function
![Split function](vba_split.gif)

GIF created with [LiceCap](http://www.cockos.com/licecap/).
