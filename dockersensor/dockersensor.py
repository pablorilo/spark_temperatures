import time
import random
import json
import string

def generate_sensor_id(length):
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for _ in range(length))

def generate_temperature(data):
    """función que genera de forma aleatoria las temperaturas creando de diferencias de temperatura y signo de la operación"""
  
    # definimos la temperatura actual a la temperatura que nos llega 
    current_data = data['temperature']

    #generamos una diferencia aleatoria entre 0, 0.5
    diff_temp = random.uniform(0,0.5)
    add_or_substract = random.randint(0,1)
    data['timestamp'] = time.time()

    if add_or_substract and current_data < 60:
        data['temperature'] += diff_temp
    elif current_data > 10:
        data['temperature'] -= diff_temp

    
def main():
    sensors_data = []
    
    # Generar datos iniciales para cada sensor
    for i in range(6):
        sensor_id = generate_sensor_id(8)
        data = {
            'device_id': sensor_id,
            'sensor_type': 'temperature',
            'temperature': 25,
            'timestamp': time.time()
        }
        sensors_data.append(data)
    print(sensors_data)
    while True:
        # Generar temperatura para cada sensor
        for data in sensors_data:
            generate_temperature(data)
         # Crear lista de datos de los sensores
        all_data = [json.dumps(data) for data in sensors_data]

        # Escribir lista completa en el archivo JSON
        with open('C:/Users/prilo/OneDrive/Desktop/KeepCoding/proyectos/spark-temperaturas/spark_temperatures/dockersensor/output_temp.json', 'a') as output_file:
            output_file.write('\n'.join(all_data) + '\n')
        # Esperar 1 segundo antes de generar la siguiente temperatura
        time.sleep(1)

if __name__ == '__main__':
    main()

