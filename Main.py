#Definicion de la Matriz
print("Definicion de la Matriz")


print("Ingrese los valores: ")
print("|x1 y1 z1 r1|")
print("|x2 y2 z2 r2|")
print("|x3 y3 z3 r3|")

x1 = float(input('Ingrese el valor x1: \n>>'))
y1 = float(input('Ingrese el valor y1: \n>>'))
z1 = float(input('Ingrese el valor z1: \n>>'))
r1 = float(input('Ingrese el valor r1: \n>>'))
x2 = float(input('Ingrese el valor x2: \n>>'))
y2 = float(input('Ingrese el valor y2: \n>>'))
z2 = float(input('Ingrese el valor z2: \n>>'))
r2 = float(input('Ingrese el valor r2: \n>>'))
x3 = float(input('Ingrese el valor x3: \n>>'))
y3 = float(input('Ingrese el valor y3: \n>>'))
z3 = float(input('Ingrese el valor z3: \n>>'))
r3 = float(input('Ingrese el valor r3: \n>>'))


#Determinante del Sistema

DetSys = ((x1*y2*z3)+(x2*y3*z1)+(x3*y1*z2))-((x3*y2*z1)+(z2*y3*x1)+(z3*y1*x2))
print(DetSys)
#Determinante de X
DetX = ((r1*y2*z3)+(r2*y3*z1)+(r3*y1*z2))-((r3*y2*z1)+(z2*y3*r1)+(z3*y1*r2))
print(DetX)
#Determinante de Y
DetY = ((x1*r2*z3)+(x2*r3*z1)+(x3*r1*z2))-((x3*r2*z1)+(z2*r3*x1)+(z3*r1*x2))
print(DetY)
#Determinante de Z
DetZ = ((x1*y2*r3)+(x2*y3*r1)+(x3*y1*r2))-((x3*y2*r1)+(r2*y3*x1)+(r3*y1*x2))
print(DetZ)
#Obtencion de las incognitas

X= DetX/DetSys
Y= DetY/DetSys
Z= DetZ/DetSys

print("Los resultados son: ", "X=",X,"Y=",Y,"Z=",Z)
