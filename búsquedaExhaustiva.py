pesos = [1800, 600, 1200]
valores = [72, 36, 60]
pesoMaximo = 3000
mejorValor = 0
mejores = [0]*3
for i in range(3):
    for j in range(3):
        for k in range(3):
            pesoTotal = pesos[i] + pesos[j] + pesos[k]
            if pesoTotal <= pesoMaximo:
                valor = valores[i] + valores[j] + valores[k]
                if valor >= mejorValor:
                    mejorValor = valor
                    mejores[0] = i
                    mejores[1] = j
                    mejores[2] = k
print("El valor maximo es: ",mejorValor," con", pesos[mejores[0]],', ',pesos[mejores[1]],' y ',pesos[mejores[2]]) 