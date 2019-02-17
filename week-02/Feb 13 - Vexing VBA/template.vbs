Sub ChangeNameHere()
  
  'STEP 1 -- Declare Variables/Arrays
  '---------------------------------------------------
  'Integer, Double, String, Long
  Dim price As Double
  Dim tax As Double
  Dim someOtherVariableNotUsed As String
  Dim newPrice As Double

  'Retrieve and store the data values in each variable
  price = Range("G9").Value
  tax = Range("G10").Value
  someOtherVariableNotUsed = Cells(14, 7).Value

  'Am I under budget? No, set new price... round down by converting to an Integer
  newPrice = Int(price / (1 + tax))

  'Correct the price
  Range("G11").Value = newPrice

  'Show the new total under budget
  Range("G12").Value = newPrice * (1 + tax)

  'Throw in a variable reference from one cell to another cell
  'Throw in a MOD example for Cell at row 3, column B -- remainder 1
  Cells(15, 7).Value = someOtherVariableNotUsed
  Cells(17, 7).Value = 5 Mod 4
  '---------------------------------------------------


  'STEP 2a -- (could be...) Conditionals
  '---------------------------------------------------
  If Range("G9").Value > Range("G11").Value Then
      MsgBox ("Original price is greater than new Price")
  End If

  If Range("G11").Value < Range("G12").Value Then
      MsgBox ("Under budget, new price is under budget")
  Else
      MsgBox ("Over budget, should never get here if new price calculated")
  End If

  If Range("A2").Value > Range("C2").Value Then
      MsgBox ("Num at A2 is greater than num at C2")
  ElseIf Range("A5").Value < Range("C5").Value Then
      MsgBox ("Num C2 is greater than num at A2")
  Else
      MsgBox ("Num A2 and Num C2 are equal, or there are no values yet...")
  End If
  '---------------------------------------------------


  'STEP 2b -- (could be...) Iterations AND/OR Conditionals
  '---------------------------------------------------
  Dim i As Integer
  Dim j As Integer

  For i = 1 To 20
      Cells(i, 1).Value = i Mod 2
      Cells(1, i).Value = 5
      Cells(i, 3).Value = i + 1
  Next i

  For i = 1 To 10
      If Cells(i, 1).Value Mod 2 = 0 Then
          Cells(i + 2, 2).Value = "Even Row"
      Else
          Cells(i + 2, 2).Value = "Odd Row"
      End If
  Next i

  For i = 1 To 3
    For j = 1 To 5
      MsgBox ("Row: " & i & " Column: " & j)
    Next j
  Next i
  '---------------------------------------------------


End Sub
