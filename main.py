import json
from numpy import *
#Datos Ejemplo 1: 782 1333 515 1575 696 832 1052 700 987 542 1296 704 814 1482 1023 739 643 956 1023 784
#Datos Ejemplo 2: 1.82 1.43 1.51 1.47 1.69 1.88 1.52 1.72 1.78 1.54 1.61 1.66 1.70 1.81 1.58 1.48 1.53 1.73 1.61 1.56 1.57 1.78
array = []
datos = input("Ingresa una lista de datos\nDatos: ")
diferencia_l_superior = float(input("Ingrese la diferencia que tendran los limites superiores: "))
array = datos.split(" ")
for dato in array:
    array[array.index(dato)] = float(dato) #convertir string a float
array.sort() #ordena de menor a mayor
print("Datos ordenados:")
print(array)
def calcularClases(array):
    k = (1 + (3.322*log10(len(array))))
    print("Numero de datos: ", len(array))
    print("k: ", k)
    print("Numero de clases: ", round(k))
    calcularRango(array, round(k))
def calcularRango(array, k):
    r =  array[len(array)-1] - array[0]
    print("Rango: {:.2f}".format(r))
    calcularAmplitud(r, k)
def calcularAmplitud(rango, k):
    a = rango/k
    print("Amplitud: ", a)
    crearTabla(array,a,k)
def crearTabla(array, a,k):
    limite_i = array[0]
    frecuencia = 0
    f_acumulada = 0
    f_complementaria = 0
    filas = []
    fila = {
        "clase" : "A",
        "l_inferior" : 0,
        "l_superior" : 0,
        "frecuencia" : 0,
        "f_relativa" : 0,
        "f_acumulada" : 0,
        "marca_clase" : 0,
        "f_complementaria" : 0
    }
    for x in range(k): #repite una vez por clase
        fila["clase"] = chr(65+x)
        fila["l_inferior"] = limite_i + (x*a)
        if(x!=k-1):
            fila["l_superior"] = (limite_i + ((x+1)*a))-diferencia_l_superior
        else:
            fila["l_superior"] = (limite_i + ((x+1)*a))
        for num in array:
            if(num>= fila["l_inferior"] and num<=fila["l_superior"]):
                frecuencia+=1
        fila["frecuencia"] = frecuencia
        frecuencia=0
        fila["f_relativa"]= fila["frecuencia"]/len(array)
        f_acumulada += fila["frecuencia"]
        fila["f_acumulada"] = f_acumulada
        fila["marca_clase"] = (fila["l_inferior"] + fila["l_superior"])/2
        f_complementaria+=fila["frecuencia"] 
        fila["f_complementaria"] = len(array) - f_complementaria
        filas.append(json.dumps(fila))
    print("{:<8} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format("Clase","L. inferior","L. superior","Frecuencia","F. relativa","F. acumulada","Marca clase","F. complementaria"))
    for fila in filas:
        fila = json.loads(fila)
        clase = fila["clase"]
        l_inferior = fila["l_inferior"]
        l_superior = fila["l_superior"]
        frecuencia = fila["frecuencia"]
        f_relativa = fila["f_relativa"]
        f_acumulada = fila["f_acumulada"]
        marca = fila["marca_clase"]
        f_complementaria = fila["f_complementaria"]
        print("{:^6} {:^15,.2f} {:^15,.2f} {:^13} {:^20,.5f} {:^10} {:^20,.3f} {:^15}".format( clase, l_inferior, l_superior,frecuencia,f_relativa,f_acumulada,marca,f_complementaria))
calcularClases(array)
