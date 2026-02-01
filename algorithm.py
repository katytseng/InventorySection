import numpy as np
import pandas as pd

def fill_seats(matrix, podSize, seatGap, rowGap):
    filledSeats = 0
    numRows, numCols = matrix.shape
    
    lastFilledRow = np.full(numCols, -rowGap - 1)
    
    for i in range(numRows):
        j = 0
        while j < numCols:
            if np.isnan(matrix[i, j]):
                break
            
            if matrix[i, j] == 0:
                canPlace = True
                for k in range(podSize):
                    if j + k >= numCols or np.isnan(matrix[i, j + k]):
                        canPlace = False
                        break
                    if matrix[i, j + k] != 0:
                        canPlace = False
                        break
                    # Check vertical distance constraint
                    if i - lastFilledRow[j + k] <= rowGap:
                        canPlace = False
                        break
                
                if canPlace:
                    # Fill the pod
                    for k in range(podSize):
                        matrix[i, j + k] = 1
                        lastFilledRow[j + k] = i
                        filledSeats += 1
                    j += podSize + seatGap
                else:
                    j += 1
            else:
                j += 1
    
    matrix_df = pd.DataFrame(matrix)
    
    return matrix_df, filledSeats


#matrixOutput, filledSeatsOutput = fill_seats(matrix, 2, 2, 1)
#print(matrixOutput)
#print(filledSeatsOutput)


def fill_seats1(matrix, podSize, seatGap, rowGap):
    filledSeats = 0
    numRows, numCols = matrix.shape
    
    lastFilledRow = np.full(numCols, -rowGap - 1)
    
    #modify algorithm so that you only try to fill seats on every (rowGap + 1)th row
    for i in range(numRows):
        if i % (rowGap + 1) != 0:
            continue
        j = 0
        while j < numCols:
            if np.isnan(matrix[i, j]):
                break
            
            if matrix[i, j] == 0:
                canPlace = True
                for k in range(podSize):
                    if j + k >= numCols or np.isnan(matrix[i, j + k]):
                        canPlace = False
                        break
                    if matrix[i, j + k] != 0:
                        canPlace = False
                        break
                    # Check vertical distance constraint
                    if i - lastFilledRow[j + k] <= rowGap:
                        canPlace = False
                        break
                
                if canPlace:
                    # Fill the pod
                    for k in range(podSize):
                        matrix[i, j + k] = 1
                        lastFilledRow[j + k] = i
                        filledSeats += 1
                    j += podSize + seatGap
                else:
                    j += 1
            else:
                j += 1
    
    matrix_df = pd.DataFrame(matrix)
    
    return matrix_df, filledSeats


#matrixOutput, filledSeatsOutput = fill_seats(matrix, 2, 2, 1)
#print(matrixOutput)
#print(filledSeatsOutput)


