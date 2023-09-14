import calendar
import datetime
import locale
import os

locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')

while True:

    print('\n\t\t============')
    print('\t\t   AGENDA')
    print('\t\t============')

    fecha_actual = datetime.datetime.now()

    year = fecha_actual.year
    month = fecha_actual.month
    cal = calendar.month(year, month)

    cal_lines = cal.splitlines()

    nombre_mes = cal_lines[0].split()[0].capitalize() + ' ' + cal_lines[0].split()[1]

    print('\n\t      ' + nombre_mes)
    cal_formatted = '\t   ' + '\n\t   '.join(cal_lines[1:])

    print(cal_formatted)

    print('\n\t0. Anterior')
    print('\t1. Siguiente')
    print('\tx. Salir')

    op = input('\n\t').lower()
    
    if op == '0':
        
        os.system('cls')
        
        print('\n\t\t============')
        print('\t\t   AGENDA')
        print('\t\t============')
        
        cal = calendar.month(year, month-1)
        
        cal_lines = cal.splitlines()

        nombre_mes = cal_lines[0].split()[0].capitalize() + ' ' + cal_lines[0].split()[1]
        
        print('\n\t      ' + nombre_mes)
        cal_formatted = '\t   ' + '\n\t   '.join(cal_lines[1:])
        print(cal_formatted)
    
    elif op == '1':
        pass
        
    elif op == 'x':
        break
    
    else:
        print('Opción no válida. Por favor, eliga una opción válida.')