import calendar
import datetime
import locale
import os

locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')

fecha_actual = datetime.datetime.now()
year = fecha_actual.year
month = fecha_actual.month


def mostrar_calendario(year, month):
    
    os.system('cls')
    
    print('\n\t\t============')
    print('\t\t   AGENDA')
    print('\t\t============')
    
    cal = calendar.month(year, month)
    cal_lines = cal.splitlines()

    nombre_mes = cal_lines[0].split()[0].capitalize() + ' ' + cal_lines[0].split()[1]

    print('\n\t      ' + nombre_mes)
    cal_formatted = '\t   ' + '\n\t   '.join(cal_lines[1:])

    print(cal_formatted)

    print('\n\t0. Anterior')
    print('\t1. Siguiente')
    print('\t2. Agendar Evento')
    print('\t3. Ver Eventos')
    print('\tx. Salir')

while True:

    mostrar_calendario(year, month)
    op = input('\n\t').lower()

    if op == '0':
        if month == 1:
            month = 12
            year -= 1
        else:
            month -= 1
    
    if op == '1':
        if month == 12:
            month = 1
            year += 1
        else:
            month += 1
    
    if op == '2':
        print('\n\tIngrese el día en que desea agendar el evento')
        dia = input('\n\t')
        os.system('cls')
        print('\n\t\t=================')
        print('\t\t  AGENDAR EVENTO')
        print('\t\t=================')
        print('\n\tTítulo del Evento')
        titulo = input('\t')
        print('\n\tHora de Inicio (formato de 24hrs)')
        hora = input('\t')
        print('\n\tDuración (minutos)')
        duracion = input('\t')
        
        guardar = open("agenda.txt", "a")
        guardar.write("Día: " + dia + "/" + str(month) + "/" + str(year))
        guardar.write("\nTítulo: " + titulo)
        guardar.write("\nHora de Inicio: " + hora)
        guardar.write("\nDuración: " + duracion + "\n\n")
        guardar.close()
    
    if op == '3':
        try:
            with open("agenda.txt", "r") as archivo:
                
                contenido = archivo.read()
                
                for linea in archivo:
                    print(linea)
                    
        except FileNotFoundError:
            print("No existebn eventos agendados.")
        except I0Error:
            print("Error al mostrar eventos agendados.")
        else:
            print("Eventos agendados:")
            print(contenido)
        
    elif op == 'x':
        break
      
    else:
        print('Opción no válida. Por favor, eliga una opción válida.')