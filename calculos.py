import math

def calcularClases(array):
    k = (1 + (3.322*math.log10(len(array))))
    return k
def calcularRango(array):
    r =  max(array) - min(array)
    return r
def calcularAmplitud(rango, k):
    a_calc = (rango/k)
    return a_calc
def buscar_valor(filas, n_clases,valor):
    for i in range(n_clases):
        if(filas[i][1]>valor):
            clase = i
            break
    return clase
def calcular_nx(filas,clase,uv,valor):
    nx = (((filas[clase][1] - valor) + uv)/((filas[clase][1] -filas[clase][0]) + uv))*filas[clase][2]
    return nx
def calcular_ny(filas,clase,uv,valor):
    ny = (((valor - filas[clase][0]) + uv)/((filas[clase][1] -filas[clase][0]) + uv))*filas[clase][2]
    return ny
def calcular_intervalo(nx,ny,clase1,clase2,filas,n):
    sum = round(nx)+round(ny)
    for i in range(n):
        if(i>clase1 and i<clase2):
            sum+=filas[i][2]
    print("Desde la clase: ",clase1+1)
    print("Hasta la clase: ",clase2+1)
    print("Nx: ",nx)
    print("Ny: ",ny)
    print("{:<1,.0f} datos cumplen con la condicion dada".format(sum))