import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
url='D:\covid_22_noviembre.csv'

data= pd.read_csv(url)


print(data.info())

#1.  Número de casos de Contagiados en el País.  Número de casos de Contagiados en el País.

print(data[data['Sexo']=='Activo'].shape[0])

