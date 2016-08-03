from radio import Radio 
rad=Radio("sony")
desea_contunuar=True

while desea_contunuar:
	if rad.encendido:
		print(" 1.subir volumen \n 2.bajar volumen\n 3.subir emisora\n 4.bajar emisora\n 5.cambiar frecuencia\n 6.apagar")
		opc=int(input("que opcion quiere? "))
		if opc == 1:
			rad.subir_volumen()
		if opc == 2:
			rad.bajar_volumen()	
		if opc == 3:
			rad.subir_emisora()
		if opc == 4:
			rad.bajar_emisora()
		if opc == 5:
			rad.cambiar()
		if opc == 6:
			rad.apagar()
	else :
		print(" 1.salir \n 2.encender ")
		opc=int(input("que opcion quiere? "))
		if opc == 1:
			desea_contunuar=False
		if opc == 2:
			rad.encender()
	print("marca" ,rad.marca)
	print("estado" ,rad.encendido)
	print("volumen" ,rad.volumen)
	print("emisora AM" ,rad.emisora_AM)
	print("emisora FM" ,rad.emisora_FM)
	print("FM encendido" ,rad.en_FM)
			

				

