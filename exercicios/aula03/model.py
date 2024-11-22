from sklearn.linear_model import LinearRegression
import numpy as np

horas_estudo = np.array([1,2,3,4,5]).reshape(-1,1) # Valor referência
notas = np.array([40,50,60,70,90])

modelo = LinearRegression()
modelo.fit(horas_estudo, notas)
horas = float(input("Digite o número de horas estudadas: "))

nota_prevista = modelo.predict([[horas]])
print(f"Com {horas} de estudo, a nota prevista é {nota_prevista[0]:.2f}")