segundos = int(input('Por favor, entre com o número de segundos que deseja converter: '))
dias = segundos // 86400
resto_seg_dias = segundos % 86400
horas = resto_seg_dias // 3600
resto_seg_horas = resto_seg_dias % 3600
minutos = resto_seg_horas // 60
segundos_final = resto_seg_horas % 60
print(dias,'dias,',horas,'horas,',minutos,'minutos e',segundos_final,'segundos.')
