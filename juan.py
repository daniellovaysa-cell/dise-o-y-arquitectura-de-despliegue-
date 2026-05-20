# titulo y cargar de datos
print("problema de calculo del mayor entre tres numeros")
n1= int(input("N1:"))
n2= int(input("N2:"))
n3= int(input("N3:"))

#Procesos
if n1>n2 and n1>n3:
    may= n1
else:
    if n2>n3:
        may=n2
    else:
        may=n3        
        
#visualizacion de salidas:
print ("El mayor es:", may)               