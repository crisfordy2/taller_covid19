import pandas as pd
import matplotlib.pyplot as plt

url = 'Casos_positivos_de_COVID-19_25_05_2022.csv'
data = pd.read_csv(url)


# Agrupar por columnas los resultados
data['Estado'].value_counts()


# ELIMINAMOS LAS COLUMNAS DEL DATASET 
data.drop('Código ISO del país', axis = 1, inplace=True)
data.drop('Nombre del país', axis = 1, inplace=True)
data.drop('Pertenencia étnica', axis = 1, inplace=True)
data.drop('Nombre del grupo étnico', axis = 1, inplace=True)
data.drop('Fecha de inicio de síntomas', axis = 1, inplace=True)
data.drop('Unidad de medida de edad', axis = 1, inplace=True)
data.drop('Código DIVIPOLA departamento', axis = 1, inplace=True)
data.drop('Código DIVIPOLA municipio', axis = 1, inplace=True)
data.drop('ID de caso', axis = 1, inplace=True)

# Normalizar la columna de Estado

data.loc[data['Estado'] == 'leve'] = 'Leve'
data.loc[data['Estado'] == 'LEVE'] = 'Leve'

data.loc[data['Estado'] == 'M'] = 'Moderado'
data.loc[data['Sexo'] == 'F'] = 'Fallecido'


data.loc[data['Sexo'] == 'm'] = 'M'
data.loc[data['Sexo'] == 'f'] = 'F'


cantidad_casos = data.shape[0]
print("1.Cantidad de contagios: ", cantidad_casos)

numero_municipios = data['Nombre municipio'].value_counts().count()
print("2.Cantidad de municipios afectados: ", cantidad_casos)

lista_municipios = data['Nombre municipio' ].unique().tolist()
print("3.Lista municipios afectados: ", lista_municipios)

personas_casa = data[data['Ubicación del caso'] == 'Casa'].shape[0]
print("4.Lista personas en casa: ", lista_municipios)

personas_recuperadas = data[data['Recuperado'] == 'Recuperado'].shape[0]
print("5.Lista personas recuperadas: ", lista_municipios)

cantidad_muertes = data[data['Estado'] == 'Fallecido'].shape[0]
print("6.Cantidad de personas que murieron por covid: ", cantidad_muertes)

tipocaso_mayor_menor = data['Tipo de contagio'].sort_values(ascending=False)
print("7.Mayor a menor por tipo de caso: ", tipocaso_mayor_menor)

numero_departamento = data['Nombre departamento'].value_counts().count()
print("8. Número de departamentos afectados: ", numero_departamento)

lista_departamento = data['Nombre departamento'].unique().tolist()
print("9. lista departamentos afectados: ", lista_departamento)

tipo_atencion_mayor_menor = data['Ubicación del caso'].sort_values(ascending=False)
print("10. Ordene de mayor a menor por tipo de atención: ", tipo_atencion_mayor_menor)

departamentos_mayores_casos = data['Nombre departamento' ].value_counts().head(10)
print("11. 10 departamentos con mas casos de contagiados: ", departamentos_mayores_casos)

departamentos_mayores_fallesidos = data[data['Estado'] == 'Fallecido'].groupby('Nombre departamento').size().sort_values(ascending=False).head(10)
print("12. 10 departamentos con mas casos de fallesidos: ", departamentos_mayores_casos)

departamentos_mayores_recuperado = data[data['Recuperado'] == 'Recuperado'].groupby('Nombre departamento').size().sort_values(ascending=False).head(10)
print("13. 10 departamentos con mas casos de recuperados: ", departamentos_mayores_recuperado)

departamentos_mayores_contagios = data['Nombre municipio'].value_counts().head(10)
print("14. 10 departamentos con mas casos de constagios: ", departamentos_mayores_contagios)

municipio_mayores_fallecidos = data[data['Estado'] == 'Fallecido'].groupby('Nombre municipio').size().sort_values(ascending=False).head(10)
print("15. 10 municipios con mas casos de fallecidos: ", municipio_mayores_fallecidos)

municipio_mayores_recuperado = data[data['Recuperado'] == 'Recuperado'].groupby('Nombre municipio').size().sort_values(ascending=False).head(10)
print("16.  10 municipios con mas casos de recuperados: ", municipio_mayores_recuperado)

municipio_departamento_mayores = data.groupby(['Nombre municipio', 'Nombre departamento']).size().sort_values(ascending=False)
print("17. agrupado por departamento y en orden de Mayor ciudades: ", municipio_departamento_mayores )

municipio_departamento_promedio = data[data['Sexo'] == 'M'].groupby('Nombre departamento').mean()
print("18. promedio de edad de contagiados por hombre ciudades: ", municipio_departamento_promedio )

fechas_contagios = data['Fecha de diagnóstico' ].value_counts().sort_values(ascending=False)
print("21. fechas mayor menor donde se presentaron mas contagios: ", fechas_contagios )

cantidad_muertes = data[data['Estado'] == 'Fallecido'].shape[0]
cantidad_recuperados = data[data['Recuperado'] == 'Recuperado'].shape[0]
tasa_mortalidad = cantidad_muertes / cantidad_casos * 100
tasa_recuperacion = cantidad_recuperados / cantidad_casos * 100
print("22. tasa mortalidad: ", tasa_mortalidad, )
print ("23. tasa recuperaccion: ", tasa_recuperacion )

cantidad_atencion = data.groupby(['Nombre municipio', 'Ubicación del caso']).size()
print('26. Cantidad de personas por atención:', cantidad_atencion)


data[(data['Nombre municipio'] == 'BOGOTA') & (data['Estado'] == 'Fallecido')].groupby('Fecha de diagnóstico').size().plot()









