from time import sleep
c = 0
for c in range(10, 0, -1):
    print(c)
    c -=1
    sleep(1)
print('Fim!')