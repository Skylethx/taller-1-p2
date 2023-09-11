DIAS_ENERO=31

DIAS_MARZO=31

DIAS_MAYO=31

DIAS_JULIO=31

DIAS_AGOSTO=31

DIAS_OCTUBRE=31

DIAS_DICIEMBRE=31

DIAS_ABRIL=30

DIAS_JUNIO=30

DIAS_SEPTIEMBRE=30

DIAS_NOVIEMBRE=30

DIAS_FEBRERO=28

DIAS_FEBRERO_BISIESTO=29

#Faltan las variables sobre festividades del año como DIA_TRABAJO etc

def es_bisiesto(a):
    if (a%4==0 and a%100!=0) or a%100==0:
        return True
    else:
        return False


def dias_mes(m,a):
    asoci={1:DIAS_ENERO,2:DIAS_FEBRERO,3:DIAS_MARZO,4:DIAS_ABRIL,5:DIAS_MAYO,6:DIAS_JUNIO,7:DIAS_JULIO,8:DIAS_AGOSTO,9:DIAS_SEPTIEMBRE,10:DIAS_OCTUBRE,11:DIAS_NOVIEMBRE,12:DIAS_DICIEMBRE}

    if es_bisiesto(a)==True and m==2:
        return DIAS_FEBRERO_BISIESTO

    else:
        return asoci[m]


print(dias_mes(2,2021))