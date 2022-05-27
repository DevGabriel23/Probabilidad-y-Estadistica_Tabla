import json
import MedidasDeTendenciaCentral
from numpy import * #38 15 10 12 62 46 25 56 27 24 23 21 20 25 38 27 48 35 50 65 59 58 47 42 37 35 32 40 28 14 12 24 66 73 72 70 68 65 54 48 34 33 21 19 61 59 47 46 30 30
#Datos Ejemplo 1: 782 1333 515 1575 696 832 1052 700 987 542 1296 704 814 1482 1023 739 643 956 1023 784
#Datos Ejemplo 2: 1.82 1.43 1.51 1.47 1.69 1.88 1.52 1.72 1.78 1.54 1.61 1.66 1.70 1.81 1.58 1.48 1.53 1.73 1.61 1.56 1.57 1.78
array_num = []
array_str = []
datos = input("Ingresa una lista de datos\nDatos: ")
unidad_variacion = float(input("Ingrese el valor de la unidad de variación: "))
array_str = datos.split(" ")
for dato in array_str:
    if(dato.isdigit() or len(dato)>0):
        array_num.append(float(dato))#convertir string a float
array_num.sort() #ordena de menor a mayor
print("Datos ordenados:")
print(array_num)
def calcularClases(array_num):
    k = (1 + (3.322*log10(len(array_num))))
    print("Numero de datos: ", len(array_num))
    print("k: ", k)
    print("Numero de clases: ", round(k))
    calcularRango(array_num, round(k))
def calcularRango(array_num, k):
    r =  array_num[len(array_num)-1] - array_num[0]
    print("Rango: {:.2f}".format(r))
    calcularAmplitud(r, k)
def calcularAmplitud(rango, k):
    a_calc = (rango/k)
    print("Amplitud (segun la formula): ", a_calc)
    a_new = float(input("Ingrese el nuevo valor de la amplitud: "))
    crearTabla(array_num,a_new,k,a_calc)
def crearTabla(array_num, a,k, a_calc):
    limite_i = array_num[0]
    frecuencia = 0
    f_acumulada = 0
    f_complementaria = 0
    filas = []
    fila = {
        "clase" : "A",
        "l_inferior" : 0,
        "l_superior" : 0,
        "l_inf_exacto" : 0,
        "l_sup_exacto" : 0,
        "frecuencia" : 0,
        "f_relativa" : 0,
        "f_acumulada" : 0,
        "marca_clase" : 0,
        "f_complementaria" : 0,
        "angulos_grafica_circular": 0
    }
    for x in range(k): #repite una vez por clase
        fila["clase"] = chr(65+x)
        fila["l_inferior"] = limite_i + (x*a)
        if(x==0):
            fila["l_superior"] = (limite_i + ((x+1)*a))-unidad_variacion
        else:
            fila_anterior = json.loads(filas[x-1])
            if(a==a_calc):
                if(x!=k-1):
                    fila["l_superior"] = (limite_i + ((x+1)*a))-unidad_variacion
                else:
                    fila["l_superior"] = (limite_i + ((x+1)*a))
            else:
                fila["l_superior"] = fila_anterior["l_superior"] + a
        for num in array_num:
            if(num>= fila["l_inferior"] and num<=fila["l_superior"]):
                frecuencia+=1
        fila["l_inf_exacto"] = fila["l_inferior"] - (unidad_variacion/2)
        fila["l_sup_exacto"] = fila["l_superior"] + (unidad_variacion/2)
        fila["frecuencia"] = frecuencia
        frecuencia=0
        fila["f_relativa"]= fila["frecuencia"]/len(array_num)
        f_acumulada += fila["frecuencia"]
        fila["f_acumulada"] = f_acumulada
        fila["marca_clase"] = (fila["l_inferior"] + fila["l_superior"])/2
        f_complementaria+=fila["frecuencia"] 
        fila["f_complementaria"] = len(array_num) - f_complementaria
        fila["angulos_grafica_circular"] = (fila["frecuencia"] * 360)/len(array_num)
        filas.append(json.dumps(fila))
    print("{:<8} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<20} {:<20} {:<20} {:<10}".format("Clase","L. inferior","L. superior","Frecuencia","F. relativa","F. acumulada","Marca clase","F. complementaria", "Lim. inf. exacto","Lim. sup. exacto","Angulos grafica circular"))
    for fila in filas:
        fila = json.loads(fila)
        clase = fila["clase"]
        l_inferior = fila["l_inferior"]
        l_superior = fila["l_superior"]
        l_inf_exacto = fila["l_inf_exacto"]
        l_sup_exacto = fila["l_sup_exacto"]
        frecuencia = fila["frecuencia"]
        f_relativa = fila["f_relativa"]
        f_acumulada = fila["f_acumulada"]
        marca = fila["marca_clase"]
        f_complementaria = fila["f_complementaria"]
        angulos = fila["angulos_grafica_circular"]
        print("{:^6} {:^15,.2f} {:^15,.2f} {:^13} {:^20,.5f} {:^10} {:^20,.3f} {:^15} {:^25,.2f} {:^15,.2f} {:^28,.2f}".format( clase, l_inferior, l_superior,frecuencia,f_relativa,f_acumulada,marca,f_complementaria, l_inf_exacto, l_sup_exacto, angulos))
    # print("\nCopiar y pegar datos: \nNumero de clases: ",k)
    # print("Limites inferiores: ", end=" ")
    array_datos = [0*j for j in range(5)]
    array_lim_inf = [0*j for j in range(k)]
    array_lim_sup = [0*j for j in range(k)]
    array_marcas = [0*j for j in range(k)]
    array_frec = [0*j for j in range(k)]
    array_frec_ac = [0*j for j in range(k)]
    for i in range(k):
        array_lim_inf[i] = (json.loads(filas[i])["l_inf_exacto"])
        # print(json.loads(filas[i])["l_inf_exacto"], end=" ")
        array_datos[0] = array_lim_inf
    # print("\nLimites superiores: ",end=" ")
    for i in range(k):
        array_lim_sup[i] = json.loads(filas[i])["l_sup_exacto"]
        # print(json.loads(filas[i])["l_sup_exacto"], end=" ")
    array_datos[1] = array_lim_sup
    # print("\nMarca de la clase: ", end=" ")
    for i in range(k):
        array_marcas[i] = json.loads(filas[i])["marca_clase"]
        # print(json.loads(filas[i])["marca_clase"], end=" ")
    array_datos[2] = array_marcas
    # print("\nFrecuencia absoluta: ",end=" ")
    for i in range(k):
        array_frec[i] = json.loads(filas[i])["frecuencia"]
        # print(json.loads(filas[i])["frecuencia"], end=" ")
    array_datos[3] = array_frec
    for i in range(k):
        array_frec_ac[i] = json.loads(filas[i])["f_acumulada"]
        # print(json.loads(filas[i])["frecuencia"], end=" ")
    array_datos[4] = array_frec_ac
    MedidasDeTendenciaCentral.calcular_media(array_datos,k)
    MedidasDeTendenciaCentral.calcular_mediana(array_datos,k)
    MedidasDeTendenciaCentral.calcular_moda(array_datos,k)
calcularClases(array_num)
