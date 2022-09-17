import pandas as pd
import numpy as np
from datetime import datetime
df = pd.read_excel("FECHAMENTO_MAIS__NEGOCIADAS_5minutos.xls")
x = np.asarray(df)
matrix = np.delete(x, [0], 1)
matrix_float = matrix.astype(np.float64)
print (matrix)
line1 = 0
line2 = 12
while line2 < 6200:
    print(matrix_float[line1:line2])
    arr_inv = matrix_float[line1:line2]
    arr_inv = np.linalg.inv(arr_inv)
    print("\n")
    print(arr_inv)
    print("\n\n\n")
    line1 = line1+1
    line2 = line2+1


