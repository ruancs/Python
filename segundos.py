segundos=input("Por favor, entre com o número de segundos que deseja converter: ")
totalseg=int(segundos)
horas=totalseg//3600
segrest=totalseg%3600
minutos=segrest//60
segfinal=segrest%60
dia=totalseg//86400
if (horas>=24):
	horas= int(horas%24)

print(dia,"dias,",horas,"horas,",minutos,"minutos e",segfinal,"segundos.")

