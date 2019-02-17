### Vexing VBA ###

The following **concepts** has been coverd in this class:
* Feb-13-2019

* [x] VBA basics - practice programs
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
		```
		Dim words() As String
		words = Split("This is a sample line", " ")
		```
	* [-] conditions
		* [-] If This... Then That.
		```
		If pbThicknes > 1.0 Then
			stopSpreading()
		Else
			startSpreading()
		End If
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
- VBA ref file (https://github.com/dvinay/ucb-extension/blob/master/week-02/Feb%2013%20-%20Vexing%20VBA/template.vbs)

GIF created with [LiceCap](http://www.cockos.com/licecap/).
