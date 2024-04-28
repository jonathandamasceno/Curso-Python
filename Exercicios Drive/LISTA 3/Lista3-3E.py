lista = []
# se 'p' > 't' == Alarme
# se não == Tranquilidade
while True:
    t = int(input("T: "))
    break

while True:
    p = int(input("P: "))
    if p == 0:
        break
    else:
        lista.append(p)
        
print(max(lista))  
if max(lista) > t:
    print("ALARME")
else:
   print("O Havai pode dormir tranquilo") 
   