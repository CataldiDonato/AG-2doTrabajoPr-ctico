pesos = [150, 325, 600, 805, 430, 1200, 770, 60, 930, 353]
valores = [20, 40, 50, 36, 25, 64, 54, 18, 46, 28]
pesoMaximo = 4200

mejorValor = 0
mejores = [0] * 10

# 10 bucles for: cada variable vale 0 (no llevar) o 1 (llevar)
for x0 in range(2):
    for x1 in range(2):
        for x2 in range(2):
            for x3 in range(2):
                for x4 in range(2):
                    for x5 in range(2):
                        for x6 in range(2):
                            for x7 in range(2):
                                for x8 in range(2):
                                    for x9 in range(2):
                                        pesoTotal = (
                                            x0*pesos[0] + x1*pesos[1] + x2*pesos[2] + x3*pesos[3] + x4*pesos[4] +
                                            x5*pesos[5] + x6*pesos[6] + x7*pesos[7] + x8*pesos[8] + x9*pesos[9]
                                        )
                                        
                                        if pesoTotal <= pesoMaximo:
                                            valor = (
                                                x0*valores[0] + x1*valores[1] + x2*valores[2] + x3*valores[3] + x4*valores[4] +
                                                x5*valores[5] + x6*valores[6] + x7*valores[7] + x8*valores[8] + x9*valores[9]
                                            )
                                            
                                            if valor > mejorValor:
                                                mejorValor = valor
                                                mejores = [x0, x1, x2, x3, x4, x5, x6, x7, x8, x9]

# Reconstruir qué pesos se eligieron (los que quedaron en 1)
pesos_elegidos = [pesos[i] for i in range(10) if mejores[i] == 1]

print("El valor máximo es:", mejorValor)
print("Con los pesos:", pesos_elegidos)