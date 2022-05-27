def calcular_media(array,n_clases):
    sum = 0
    for i in range(n_clases):
        sum+=(array[3][i]*array[2][i])
    media = sum/array[4][n_clases-1]
    print("Media: {:<5,.3f}".format(media))
def calcular_mediana(array,n_clases):
    pos_mediana = (array[4][n_clases-1]+1)/2
    for i in range(n_clases):
        if(array[4][i]>pos_mediana):
            clase = i
            break
    amplitud = array[1][clase] - array[0][clase]
    frecuencia_clase = array[3][clase]
    frecuencia_acumulada_anterior = array[4][clase-1]
    mediana = pos_mediana + ((((array[4][n_clases-1]/2) - frecuencia_acumulada_anterior)/frecuencia_clase) * amplitud)
    print("Mediana: {:<5,.3f}".format(mediana))
def calcular_moda(array,n_clases):
    max = None
    for i in range(n_clases):
        if(max is None or array[3][i]>max):
            clase = i
            max = array[3][i]
    lim_inf_clase_moda = array[0][clase]
    if(clase == 0):
        delta1 = array[3][clase]
    else:
        delta1 = array[3][clase] - array[3][clase-1]
    if(clase == n_clases-1):
        delta2 = array[3][clase]
    else:
        delta2 = array[3][clase] - array[3][clase+1]
    amplitud = array[1][clase] - array[0][clase]
    moda = lim_inf_clase_moda + ((delta1/(delta1+delta2))*amplitud)
    print("Moda: {:<5,.3f}".format(moda))