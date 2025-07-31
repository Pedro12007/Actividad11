owners = {}

owners_amount = int(input('Ingrese la cantidad de propietarios a ingresar: '))

for i in range(owners_amount):
    owner = {}
    print(f'Propietario {i+1}')
    nit = input('\nIngrese el número de NIT: ')
    name = input('Ingrese el nombre del propietario: ')
    phone = input('Ingrese el número de teléfono: ')
    vehicles = int(input('Ingrese la cantidad de vehículos que posee: '))

    for i in range(vehicles):
        plate = input('Ingrese el número de placa: ')
        brand = input('Ingrese la marca del vehículo: ')
        model = input('Ingrese el modelo: ')
        year = int(input('Ingrese el año: '))
        tax = input('¿Ya pagó el impuesto de circulación?: (1. Sí| 2. No): ')

    