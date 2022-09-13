import pandas as pd

df = pd.read_excel("FECHAMENTO_MAIS__NEGOCIADAS_5minutos.xls")

x = df.values.tolist()

matrix = [x]
while x != []:
    matrix.append(x[:2])
    x = x[2:]

print (matrix)

