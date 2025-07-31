propietarios = {}
placas = []

propietarios_amount = int(input('Ingrese la cantidad de propietarios a ingresar: '))

for i in range(propietarios_amount):
    owner = {}
    print(f'Propietario #{i+1}')
    while True:
        nit = input('\nIngrese el número de NIT: ')
        if not(nit in propietarios):
            break
        else:
            print('NIT ya registrado. Intente nuevamente.\n')

    name = input('Ingrese el nombre del propietario: ')
    phone = input('Ingrese el número de teléfono: ')
    vehicles = int(input('Ingrese la cantidad de vehículos que posee: '))
    print()

    owner['nombre'] = name
    owner['telefono'] = phone
    owner['vehiculos'] = {}

    for i in range(vehicles):
        car_details = {}
        print(f'Carro #{i+1}')
        while True:
            plate = input('\nIngrese el número de placa: ')
            if not(plate in owner['vehiculos']) and not(plate in placas):
                placas.append(plate)
                break
            else:
                print('Placa ya registrada. Intente nuevamente.\n')


        brand = input('Ingrese la marca del vehículo: ')
        model = input('Ingrese el modelo: ')
        year = int(input('Ingrese el año: '))
        while True:
            tax = input('¿Ya pagó el impuesto de circulación?: (1. Sí| 2. No): ')
            if tax == '1':
                tax = True
                break
            elif tax == '2':
                tax = False
                break
            else:
                print('Opción inválida. Intente de nuevo.\n')


        car_details['marca'] = brand
        car_details['modelo'] = model
        car_details['año'] = year
        car_details['impuesto_pagado'] = tax

        owner['vehiculos'][plate] = car_details

    propietarios[nit]=owner

print(propietarios)


