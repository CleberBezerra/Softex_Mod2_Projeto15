import time

print("Iniciando contagem regressiva: ")

for i in range(10, 0, -1):
    time.sleep(2)
    print(i)

if i == 1:
    print("BOOOMMM!!!")