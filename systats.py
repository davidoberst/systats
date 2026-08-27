#cpu
#temperatira grados centigrados
#ghz
#ram usada
#ram disponible
#ram reservado y uso de la ram reservada
#gpu usage
#consumo de net
#consumo de disco

import os
import psutil

cpu = psutil.cpu_percent(interval=1)

temperature = psutil.sensors_temperatures()
for x, y in temperature.items():
    for z in y[:len(y)-1]: #solo mostrar temperatura actual
        temp = z.current


ram = psutil.virtual_memory()
totalRAM = round(ram.total / (1024**3),2)




print(f"CPU : {cpu}")
print(f"TEMP : {temp}°")
print(f"RAM : {totalRAM}")


