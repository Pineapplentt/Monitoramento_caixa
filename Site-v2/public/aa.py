from datetime import datetime
from time import sleep
from dashing import (
    HSplit, 
    VSplit, 
    VGauge, 
    HGauge, 
    Text
)
from psutil import (
    virtual_memory,
    sensors_battery,
    cpu_percent,
    disk_usage,
    users,
    boot_time,
    pids,
    process_iter
)


def bytes_to_gigas(value):
    return value / 1024 / 1024 / 1024


ui = HSplit(  # ui
    VSplit(
        Text(
            ' ',
            border_color=9,
            title='Processos'
        ),
        HSplit(  # ui.items[0]
            VGauge(title='RAM'),  # ui.items[0].items[0]
            title='Memória',
            border_color=3
        ),
    ),
    VSplit(  # ui.items[1]
        HGauge(title='CPU %'),
        HGauge(title='cpu_0'),
        HGauge(title='cpu_1'),
        HGauge(title='cpu_2'),
        HGauge(title='cpu_3'),
        title='CPU',
        border_color=5,
    ),
    VSplit(  # ui.items[2]
        Text(
            ' ',
            title='Outros',
            border_color=4
        ),
        Text(
            ' ',
            title='Disco',
            border_color=6,
            
        ),
    ),
)

while True:
    
    # # Processos
    proc_tui = ui.items[0].items[0]
    p_list = []
    for proc in process_iter():
        proc_info = proc.as_dict(['name', 'cpu_percent'])
        if proc_info['cpu_percent'] >= 0:
            p_list.append(proc_info)

    ordenados = sorted(
        p_list,
        key=lambda p: p['cpu_percent'],
        reverse=True
    )[:10]
    proc_tui.text = f"{'Nome':<30}CPU"

    for proc in ordenados:
        proc_tui.text += f"\n{proc['name']:<30} {proc['cpu_percent']}"

    # # Memória
    mem_tui = ui.items[0].items[1]
    # # Ram
    ram_tui = mem_tui.items[0]
    ram_tui.value = virtual_memory().percent
    ram_tui.title = f'RAM {ram_tui.value} %'

    # # CPU
    cpu_tui = ui.items[1]
    # CPU %
    cpu_percent_tui = cpu_tui.items[0]
    ps_cpu_percent = cpu_percent()
    cpu_percent_tui.value = ps_cpu_percent
    cpu_percent_tui.title = f'CPU Total {ps_cpu_percent}%'

    # Porcentagem dos cores
    cores_tui = cpu_tui.items[1:9]
    ps_cpu_percent = cpu_percent(percpu=True)
    for i, (core, value) in enumerate(zip(cores_tui, ps_cpu_percent)):
       core.value = value
       core.title = f'Core_{i} {value}%'
    
    # # Outros
    outros_tui = ui.items[2].items[0]
    outros_tui.text = ''
    outros_tui.text += f'\nUsuário: {users()[0].name}'
    outros_tui.text += f'\nBateria: {sensors_battery().percent}%'
    boot = datetime.fromtimestamp(boot_time()).strftime("%Y-%m-%d %H:%M:%S")
    outros_tui.text += f'\nHorário do boot: {boot}'
    outros_tui.text += f'\nProcessos: {len(pids())}'
    
    # # Disco
    disk_tui = ui.items[2].items[1]
    disk_tui.text = ''
    disk_tui.text += f'\nEspaço em disco utilizado: {disk_usage("/").percent}%'
    
    try:
        ui.display()
        sleep(1.75)
    except KeyboardInterrupt:
        break