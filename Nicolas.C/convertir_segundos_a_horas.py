def convertir_segundos_a_horas(segs):
	horas=int(segs/3600)
	minutos=int((segs-(horas*3600))/60)
	segundos=segs-(horas*3600+minutos*60)
	return horas, minutos, segundos
