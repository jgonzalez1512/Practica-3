print("salario de empleado")

def calcular_deducciones(sueldo):
    
    
 
    if sueldo < 52027.43:
        TasaIsr = 0.15
    else :
        TasaIsr = 0.20 
    
    TasaArs = 3.04
    TasaAfp = 1.44
     
    salarioanual = sueldo * 12
    excedente = salarioanual - 624329.01
    tasa = 31216.00 
    isr = tasa + excedente * TasaIsr
    ars = sueldo * TasaArs
    afp = sueldo * TasaAfp
   
    return isr, ars, afp


try:
    sueldo = float(input("Ingrese el sueldo del empleado: "))

    isr, ars, afp = calcular_deducciones(sueldo)

    print("ISR:"+str(isr))
    print("ARS:"+str(ars))
    print("ISR:"+str(afp))

except ValueError:
    print("Ingrese un monto válido.")
