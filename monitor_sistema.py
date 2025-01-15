import psutil
import time
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

# SALVA OS LOGS
def salvar_dados(cpu, memory, disk, net_sent, net_recv):
    log_entry = f"{datetime.now()} - CPU: {cpu}% | Memória: {memory}% | Disco: {disk}% | Enviado: {net_sent / (1024 * 1024):.2f} MB | Recebido: {net_recv / (1024 * 1024):.2f} MB\n"
    with open("monitoramento_log.txt", "a") as f:
        f.write(log_entry)

# CHAMADA DE ALERTA
def verificar_alertas(cpu_percent, memory_percent):
    alerta = ""
    if cpu_percent > 80:
        alerta += "⚠️ Alerta: CPU acima de 80%! "
        cpu_label.config(foreground="red")  # Altera a cor do texto da CPU para vermelho
    else:
        cpu_label.config(foreground="black")  # Reseta a cor do texto para preto
    
    if memory_percent > 50:
        alerta += "⚠️ Alerta: Memória acima de 50%! "
        memory_label.config(foreground="red")  # Altera a cor do texto da memória para vermelho
    else:
        memory_label.config(foreground="black")  # Reseta a cor do texto para preto
    
    # Exibe um pop-up caso haja alerta
    if alerta:
        messagebox.showwarning("Alerta de Desempenho", alerta)
    
    return alerta
# FINAL DE CHAMADA DE ALERTAS

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

    # Verifica alertas
    alerta = verificar_alertas(cpu_percent, memory_percent)

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
root.geometry("400x350")

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
