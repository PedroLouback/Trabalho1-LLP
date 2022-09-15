import pandas as pd
import numpy as np
df = pd.read_excel("FECHAMENTO_MAIS__NEGOCIADAS_5minutos.xls")
x = np.asarray(df)
line1 = 0
line2 = 12
while line2 < 6200 :
    print(x[line1:line2])
    arr_inv = x[line1:line2]
    arr_inv = np.linalg.inv(arr_inv)
    print("\n\n")
    print(arr_inv)
    print("\n\n\n")
    line1=line1+1
    line2=line2+1


