import time
import os
import winsound
from turtle import clear

print("Iniciando CONTAGEM REGRESSIVA: ")
for i in range(10, 0, -1):
    time.sleep(2) 
    os.system("cls") #Limpa tela, apenas Windows
    print(i)

if i == 1:
    time.sleep(1)
    print("BOOOMMM!!!")
    # Som de Beep
    duration = 1500
    freq = 440
    winsound.Beep(freq, duration)