import psutil
import time
import tkinter as tk
from tkinter import ttk
from datetime import datetime

# SALVA OS LOGS
def salvar_dados(cpu, memory, disk, net_sent, net_recv):
    log_entry = f"{datetime.now()} - CPU: {cpu}% | Memória: {memory}% | Disco: {disk}% | Enviado: {net_sent / (1024 * 1024):.2f} MB | Recebido: {net_recv / (1024 * 1024):.2f} MB\n"
    with open("monitoramento_log.txt", "a") as f:
        f.write(log_entry)

def atualizar_info():
    # CPU
    cpu_percent = psutil.cpu_percent(interval=1)

    # MEMÓRIA
    memory = psutil.virtual_memory()
    memory_percent = memory.percent

    # DISCO
    disk = psutil.disk_usage('/')
    disk_percent = disk.percent

    # REDE
    network = psutil.net_io_counters()
    bytes_sent = network.bytes_sent
    bytes_recv = network.bytes_recv

    # ATUALIZA
    cpu_label.config(text=f"Uso da CPU: {cpu_percent}%")
    memory_label.config(text=f"Uso da Memória: {memory_percent}%")
    disk_label.config(text=f"Uso do Disco: {disk_percent}%")
    net_label.config(text=f"Bytes Enviados: {bytes_sent / (1024 * 1024):.2f} MB\nBytes Recebidos: {bytes_recv / (1024 * 1024):.2f} MB")
    
    # SALVA O ARQUIVO
    salvar_dados(cpu_percent, memory_percent, disk_percent, bytes_sent, bytes_recv)
    
    # ATUALIZAÇÃO DE 2SEGUNDOS
    root.after(2000, atualizar_info)

# INTERFACE
root = tk.Tk()
root.title("Monitor de Desempenho do Sistema")
root.geometry("400x300")

# Labels para exibir as informações
cpu_label = ttk.Label(root, text="Uso da CPU: 0%", font=("Arial", 12))
cpu_label.pack(pady=10)

memory_label = ttk.Label(root, text="Uso da Memória: 0%", font=("Arial", 12))
memory_label.pack(pady=10)

disk_label = ttk.Label(root, text="Uso do Disco: 0%", font=("Arial", 12))
disk_label.pack(pady=10)

net_label = ttk.Label(root, text="Bytes Enviados: 0 MB\nBytes Recebidos: 0 MB", font=("Arial", 12))
net_label.pack(pady=10)

# INICIA A ATUALIZAÇÃO
atualizar_info()

# INICIA A INTERFACE
root.mainloop()
