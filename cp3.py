temperaturas = [[28, 31, 34, 33], [25, 27, 29, 28], [32, 35, 36, 34], [24, 26, 25, 27]]
medias=[]
counts=[]
for i in range(len(temperaturas)):
    temps = 0
    count = 0
    for j in range(len(temperaturas[i])):
        if temperaturas[i][j] >=33:
            count+=1
        temps+=temperaturas[i][j]
    medias.append(temps/len(temperaturas[i]))
    counts.append(count)
for i in range(len(medias)):
    print(f"Sala {i+1}")
    print(f"Média:{medias[i]}")
    print(f"Registros críticos:{counts[i]}")