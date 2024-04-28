c = m = f = 0
while True:
    if c == 0:
        num = int(input('Digite um número de 1 a 100: '))
        if num < 1 or num > 1000:
            while num < 1 or num > 1000:
                num = int(input('Digite um número de 1 a 100: '))
        c += 1
    else:
        # 1 = homem,  2 = mulher
        for c in range(0, num):
            s = int(input('Sexo. 1 = M // 2 = F : '))
            if s > 2 or s < 1:
                while s > 2 or s < 1:
                    s = int(input('Sexo. 1 = M // 2 = F : '))
            if s == 1:
                m += 1 # contador homens
            if s == 2:
                f += 1 # contador mulheres
        break
    
print(m) # total homens
print(f) # total mulheres