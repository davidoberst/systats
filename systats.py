# cpu
# temperatura grados centigrados
# ghz
# ram usada
# ram disponible
# ram reservado y uso de la ram reservada
# gpu usage
# consumo de net
# consumo de disco

import os
import psutil
import subprocess

while True:

    cpu = psutil.cpu_percent(interval=1)

    temperature = psutil.sensors_temperatures()

    vram = subprocess.run(
        ["cat", "/sys/class/drm/card1/device/mem_info_vram_used"],
        capture_output=True,
        text=True
    )

    vramtotal = subprocess.run(
        ["cat", "/sys/class/drm/card1/device/mem_info_vram_total"],
        capture_output=True,
        text=True
    )

    for x, y in temperature.items():
        for z in y[:len(y)-1]:
            temp = z.current

    ram = psutil.virtual_memory()

    totalRAM = round(ram.total / (1024**3), 2)
    usedRAM = round(ram.used / (1024**3), 2)

    VRAMusage = round(int(vram.stdout) / (1024**3), 2)
    VRAMtotal = round(int(vramtotal.stdout) / (1024**3), 2)

    print("\033[H\033[J", end="")
    print(f"CPU       : {cpu}%")
    print(f"TEMP      : {temp}°C")
    print(f"RAM       : {usedRAM}/{totalRAM} GB")
    print(f"RAM USAGE : {ram.percent}%")
    print(f"VRAM      : {VRAMusage}/{VRAMtotal} GB")