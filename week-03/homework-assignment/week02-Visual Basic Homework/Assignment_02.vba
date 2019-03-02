Sub Easy()
    Dim currentTicker, nextTicker As String
    Dim total As Double
    Dim openStock, closeStock As Double
    Dim resultPosition As Long
    Dim Lastrow As Long
    Dim greatestIncrease, greatestDecrease, greatestTotal As Double
    
    resultPosition = 2
    total = 0
    Lastrow = Range("A" & Rows.Count).End(xlUp).Row
    
    'First ticker value to compare with other value
    currentTicker = Cells(resultPosition, 1).Value
    openStock = Cells(resultPosition, 3).Value
    
    Call initializeResults
    
    'loop throgh the entire sheet
    For i = 2 To Lastrow
        nextTicker = Cells(i, 1).Value
        If currentTicker = nextTicker Then
            'compute total
            total = total + Cells(i, 7).Value
            closeStock = Cells(i, 6).Value
        Else
            'write total result
            Call writeResults(currentTicker, total, openStock, closeStock, resultPosition)
            
            'make zero total
            total = 0
            total = total + Cells(i, 7).Value
            openStock = Cells(i, 3).Value
            closeStock = Cells(i, 6).Value
                
            're-initialize variables
            currentTicker = nextTicker
            resultPosition = resultPosition + 1

        End If
    Next i
    
    'calculate "Greatest % increase", "Greatest % Decrease" and "Greatest total volume".
    For i = 2 To Lastrow
        If greatestIncrease < Cells(i, 11).Value Then
            greatestIncrease = Cells(i, 11)
            Range("P2") = greatestIncrease
            Range("O2") = Cells(i, 9).Value
        End If
        If greatestDecrease > Cells(i, 11).Value Then
            greatestDecrease = Cells(i, 11)
            Range("P3") = greatestDecrease
            Range("O3") = Cells(i, 9).Value
        End If
        If greatestTotal < Cells(i, 12).Value Then
            greatestTotal = Cells(i, 12)
            Range("P4") = greatestTotal
            Range("O4") = Cells(i, 9).Value
        End If
    Next i
End Sub
Sub initializeResults()
    Range("I1") = "Ticker"
    Range("J1") = "Yearly Change"
    Range("K1") = "Percentage Change"
    Range("L1") = "Total Stock Volume"
    
    Range("O1") = "Ticker"
    Range("P1") = "Value"
    Range("N2") = "Greatest % increase"
    Range("N3") = "Greatest % decrease"
    Range("N4") = "Greatest total volume"
    
    'Percentage format
    Range("P2").NumberFormat = "0.00%"
    Range("P3").NumberFormat = "0.00%"
    Range("P4").NumberFormat = "0000000000"
    
End Sub
Sub writeResults(ByVal currentTicker As String, ByVal total As Double, ByVal openStock As Double, ByVal closeStock As Double, ByVal resultPosition As Long)
    'Ticker value
    Cells(resultPosition, 9) = currentTicker
    
    'yearly change
    Cells(resultPosition, 10).NumberFormat = "0.000000000"
    
    Cells(resultPosition, 10) = closeStock - openStock
    If Cells(resultPosition, 10).Value < 0 Then
        Cells(resultPosition, 10).Interior.Color = vbRed
    Else
        Cells(resultPosition, 10).Interior.Color = vbGreen
    End If
    
    'percentage change
    Cells(resultPosition, 11).NumberFormat = "0.00%"
    If openStock = 0 Then
        Cells(resultPosition, 11) = 0
    Else
        Cells(resultPosition, 11) = (closeStock - openStock) / openStock
    End If
    
    'total stock value
    Cells(resultPosition, 12) = total
    
End Sub