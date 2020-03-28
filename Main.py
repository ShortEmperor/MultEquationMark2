#!/usr/bin/env python
#This code is only intended for linux however i'm working on make it available for all platforms and in multiple languages



import os

def main():
	try:
		os.system("clear")
		print("Defining the matrix")


		print("Type in the values (They will be stored as shown): ")
		print("|x1 y1 z1 r1|")
		print("|x2 y2 z2 r2|")
		print("|x3 y3 z3 r3|")

		x1 = float(input('Type the value for x1: \n>>'))
		y1 = float(input('Type the value for y1: \n>>'))
		z1 = float(input('Type the value for z1: \n>>'))
		r1 = float(input('Type the value for r1: \n>>'))
		x2 = float(input('Type the value for x2: \n>>'))
		y2 = float(input('Type the value for y2: \n>>'))
		z2 = float(input('Type the value for z2: \n>>'))
		r2 = float(input('Type the value for r2: \n>>'))
		x3 = float(input('Type the value for x3: \n>>'))
		y3 = float(input('Type the value for y3: \n>>'))
		z3 = float(input('Type the value for z3: \n>>'))
		r3 = float(input('Type the value for r3: \n>>'))


		#System determiner

		DetSys = ((x1*y2*z3)+(x2*y3*z1)+(x3*y1*z2))-((x3*y2*z1)+(z2*y3*x1)+(z3*y1*x2))

		#X determiner
		DetX = ((r1*y2*z3)+(r2*y3*z1)+(r3*y1*z2))-((r3*y2*z1)+(z2*y3*r1)+(z3*y1*r2))

		#Y determiner
		DetY = ((x1*r2*z3)+(x2*r3*z1)+(x3*r1*z2))-((x3*r2*z1)+(z2*r3*x1)+(z3*r1*x2))

		#Z determiner
		DetZ = ((x1*y2*r3)+(x2*y3*r1)+(x3*y1*r2))-((x3*y2*r1)+(r2*y3*x1)+(r3*y1*x2))

		#Obtaining the results

		X= DetX/DetSys
		Y= DetY/DetSys
		Z= DetZ/DetSys

		print("The results are: ", "\nX=",X,"\nY=",Y,"\nZ=",Z)

		#Repeating the program
		rep = str(input("Do you wanna repeat the program? (Y/n): \n>>"))
		if rep.upper() == "Y":
			main()
		elif rep.upper() == "N":
			os.system("clear")
			exit()
		else:
			print("Not a real option, exiting!")
			exit()
	
	#Handle Keyboard Interrupt error
	
	except KeyboardInterrupt:
		os.system("clear")
		exit()
	
	finally:
		exit()

if __name__=="__main__":
	main()
