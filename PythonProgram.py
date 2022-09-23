from operator import length_hint
import pandas as pd
import numpy as np
from datetime import datetime
df = pd.read_excel("FECHAMENTO_MAIS__NEGOCIADAS_5minutos.xls")
x = np.asarray(df)
matrix = np.delete(x, [0], 1)
matrix_float = matrix.astype(np.float32)
line1 = 0
line2 = 12
while line2 <= len(matrix_float):
    print(matrix_float[line1:line2])
    det = np.linalg.det(matrix_float[line1:line2])
    det = round(det,15)
    if (det != 0):
        arr_inv = matrix_float[line1:line2]
        arr_inv = np.linalg.inv(arr_inv)
        print("\n")
        print(arr_inv)
        print("\n\n")
    elif (det == 0):
        print("\nNao foi possivel realizar a matriz inversa por determinante igual a 0\n\n")
    line1 = line1+1
    line2 = line2+1


