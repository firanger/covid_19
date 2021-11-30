import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
url='D:\covid_22_noviembre.csv'

covid_19= pd.read_csv(url)

covid_19.Sexo.replace('f','F',inplace=True)
covid_19.Sexo.replace('m','M',inplace=True)
covid_19.Estado.replace('leve','Leve', inplace=True)
covid_19.Estado.replace('LEVE','Leve', inplace=True)
covid_19['Nombre departamento'].replace('CASA','Casa', inplace=True)
covid_19['Nombre departamento'].replace('casa','Casa', inplace=True)
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

#7.  Ordenar de Mayor a menor por tipo de caso (Importado,  en estudio, Relacionado)

print(covid_19.groupby('Tipo de contagio').size().sort_values(ascending=False) )
#8.  Número de departamentos afectados 

print(covid_19[(covid_19.Recuperado != '')].groupby(['Nombre departamento']).size().shape[0])

#9.  Liste los departamentos afectados(sin repetirlos)

print(covid_19[(covid_19.Recuperado != '')].groupby(['Nombre departamento']).size())

#10. Ordene de mayor a menor por tipo de atención

print(covid_19.groupby('Ubicacion del caso').size().sort_values(ascending=False))

#11.  Liste de mayor a menor los 10 departamentos con mas casos de contagiados 

covid_19['Nombre departamento'].value_counts().head(10)

#12.  Liste de mayor a menor los 10 departamentos con mas casos de fallecidos

covid_19[covid_19['Recuperado'] == 'Fallecido']['Nombre departamento'].value_counts().head(10)
