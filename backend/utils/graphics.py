import pandas as pd
import matplotlib.pyplot as plt

def graficar_evolucion_gastos(data):
    # Extraemos los valores de los gastos y la descripción
    print(data)
    descripcion = [d["descripcion"] for d in data]
    gastos = [d["banco"] for d in data]

    # Creamos el gráfico de línea
    plt.plot(descripcion, gastos, marker='o')

    # Añadimos etiquetas a los ejes y título
    plt.xlabel('Mes')
    plt.ylabel('Gastos en pesos')
    plt.title('Evolución de los gastos')

    # Guardamos la imagen en un archivo llamado "evolucion_gastos.png"
    print("Estoy en graficar")
    plt.savefig('evolucion_gastos.png')

def generar_grafico(datos):
    # Crear un diccionario para almacenar los gastos totales por mes
    gastos_por_mes = {}
    
    # Iterar sobre los datos para sumar los gastos de cada mes
    for d in datos:
        mes = d['descripcion']
        gasto = d['banco']
        if mes in gastos_por_mes:
            gastos_por_mes[mes] += gasto
        else:
            gastos_por_mes[mes] = gasto
            
    # Convertir el diccionario en dos listas separadas (meses y gastos)
    meses = list(gastos_por_mes.keys())
    gastos = list(gastos_por_mes.values())

    # Configurar el gráfico
    plt.plot(meses, gastos)
    plt.xlabel('Mes')
    plt.ylabel('Gasto total')
    plt.title('Evolución de los gastos por mes')

    # Guardar la imagen
    plt.savefig('grafico_1.png')