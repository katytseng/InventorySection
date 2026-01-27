import numpy as np
import pandas as pd

# Create a 19x18 matrix filled with ones
matrix = np.zeros((19, 18))

# Set specific elements to 1 based on the given pattern
## 1s mean walls (no such seat)
## 0s mean available seats
length = 9
for i in range(15):
    if (i+1) % 2 == 0 and i > 0:
        length += 1
    matrix[i, length:18] = np.nan
#print(matrix)
#matrix_df = pd.DataFrame(matrix)
#matrix_df.to_csv("seat_matrix.csv", index=False, header=False)