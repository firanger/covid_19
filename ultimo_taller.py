import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
url='D:\covid_22_noviembre.csv'

covid_19= pd.read_csv(url)

covid_19.Sexo.replace('f','F',inplace=True)
covid_19.Sexo.replace('m','M',inplace=True)
covid_19.Estado.replace('leve','Leve', inplace=True)
covid_19.Estado.replace('LEVE','Leve', inplace=True)
print(covid_19.info())

#1.  Número de casos de Contagiados en el País.  Número de casos de Contagiados en el País.

print(covid_19[covid_19['Recuperado']=='Activo'].shape[0])

#2.  Número de Municipios Afectados

print(covid_19[(covid_19.Recuperado != '')].groupby(['Nombre municipio']).size().shape[0])

#3.  Liste los municipios afectados (sin repetirlos)

print(covid_19[(covid_19.Recuperado != '')].groupby(['Nombre municipio']).size())

#4.  Número de personas que se encuentran en atención en casa

print(covid_19[covid_19['Ubicación del caso']=='Casa'].shape[0])

#5.  Número de personas que se encuentran recuperados

print(covid_19[covid_19['Recuperado']=='Recuperado'].shape[0])

#6.  Número de personas que ha fallecido

print(covid_19[covid_19['Recuperado']=='Fallecido'].shape[0])


