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
import subprocess

while True : 
 cpu = psutil.cpu_percent(interval=1)

 temperature = psutil.sensors_temperatures()

 vram = subprocess.run(
    ["cat", "/sys/class/drm/card1/device/mem_info_vram_used"],
    capture_output=True,
    text=True
 )

 vramtotal = subprocess.run(
    ["cat","/sys/class/drm/card1/device/mem_info_vram_total"],
    capture_output=True,
    text=True
    
 )

 for x, y in temperature.items():
    for z in y[:len(y)-1]: #solo mostrar temperatura actual
        temp = z.current


 ram = psutil.virtual_memory()
 totalRAM = round(ram.total / (1024**3),2)
 usedRAM = round(ram.used / (1024 **3),2)
 VRAMusage = round(int(vram.stdout) / (1024 **3),2)
 VRAMtotal = round(int(vramtotal.stdout) / (1024 **3),2)

 print(f"\r CPU : {cpu}%", end="", flush=True)
 print(f"\rTEMP : {temp}°C", end="", flush=True)
 print(f"\rRAM USAGE: {ram.percent}%", end="", flush=True)
 print(f"\rRAM : {usedRAM}/{totalRAM}", end="", flush=True)
 print(f"VRAM : {VRAMusage}GB / {VRAMtotal}GB", end="", flush=True)






