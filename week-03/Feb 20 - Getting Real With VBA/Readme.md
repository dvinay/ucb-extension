### Getting Real With VBA ###

The following **concepts** has been coverd in this class:
* Feb-20-2019

* [x] VBA basics - practice programs
	* [-] Iteration
		* [-] For loop
		```
		For i = 0 To 20
			stopSpreading()
		Next i
		```
		* [-] Nested For loop
		```
		For i = 1 To 4
			For j = 1 To 4
				MsgBox(Cells(i,j))
			Next j
		Next i
		```
	* [-] Python anaconda test
		* [-] to test anaconda version.
		```
		$ conda --version
		```
		* [-] to find anaconda env list.
		```
		$ conda env list
		```
* [x] Excercise
	* [-] Nested loop
	* [-] Coloring Excel sheet
	```
	Sub formatter()
	  ' Set the Font color to Red
	  Range("A1").Font.ColorIndex = 3

	  ' Set the Cell Colors to Red
	  Range("A2:A5").Interior.ColorIndex = 3

	  ' Set the Font Color to Green
	  Range("B1").Font.ColorIndex = 4

	  ' Set the Cell Colors to Green
	  Range("B2:B5").Interior.ColorIndex = 4

	  ' Set the Color Index to Blue
	  Range("C1").Font.ColorIndex = 5

	  ' Set the Cell Colors to Blue
	  Range("C2:C5").Interior.ColorIndex = 5

	  ' Set the Color Index to Magenta
	  Range("D1").Font.ColorIndex = 7

	  ' Set the Cell Colors to Magenta
	  Range("D2:D5").Interior.ColorIndex = 7

	  ' See this website for color guides: http://dmcritchie.mvps.org/excel/colors.htm
	End Sub
	```
	* [-] use & operator to get the string concatenation
	```
	Sub Helloworld():
    	MsgBox (Cells(i, column).Value & " and then " & Cells(i + 1, column).Value)
	End Sub
	```
	* [-] use set operator to refer a sheet
	```
		' this will ref the Combined_Data sheet from the worksheet
		Set combined_sheet = Worksheets("Combined_Data")
	```
	* [-] how to get the last sheet row
	```
		lastrow = Cells(Rows.Count, 1).End(xlUp).Row
	```
* [x] Excercise
	* [-] 
